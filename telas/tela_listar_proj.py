import flet as ft
from controles.cabecalho import Cabecalho
import sqlite3

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

dt = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Açoes")),
        ft.DataColumn(ft.Text('codigocor')),
        ft.DataColumn(ft.Text('nomeproj')),
        ft.DataColumn(ft.Text('preposto')), 
        ft.DataColumn(ft.Text('gerente')),
        ft.DataColumn(ft.Text('gerenciacor')), 
        ft.DataColumn(ft.Text('local')),
        ft.DataColumn(ft.Text('nucleo')), 
        ft.DataColumn(ft.Text('cliente')),
        ft.DataColumn(ft.Text('razao')),
        ft.DataColumn(ft.Text('coordenador')),
        ft.DataColumn(ft.Text('numcontra')),
        ft.DataColumn(ft.Text('centrocusto')),
        ft.DataColumn(ft.Text('alimtrans')),
        ft.DataColumn(ft.Text('responsavel')),
        ft.DataColumn(ft.Text('gerencia')),
        ft.DataColumn(ft.Text('fiscal')),
        ft.DataColumn(ft.Text('fiscalemail')),
        ft.DataColumn(ft.Text('gestor')),
        ft.DataColumn(ft.Text('gestoremail')),
        ft.DataColumn(ft.Text('diretoria')),
        ft.DataColumn(ft.Text('objeto')),
        ft.DataColumn(ft.Text('localidade')),
        ft.DataColumn(ft.Text('treinamentos')),
        ft.DataColumn(ft.Text('proderac')),
        ft.DataColumn(ft.Text('cracha')),
        ft.DataColumn(ft.Text('documento')),
        ft.DataColumn(ft.Text('sistemamobi')),
        ft.DataColumn(ft.Text('gestaomobi')),
        ft.DataColumn(ft.Text('responmobi')),
        ft.DataColumn(ft.Text('segtrab')),
        ft.DataColumn(ft.Text('responprojadm')),
        ft.DataColumn(ft.Text('responprojcam')),
        ft.DataColumn(ft.Text('ordemserv'))
        
    ],
    rows=[]
)

def deletar(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM projeto WHERE idproj=?", (myid,))
        conn.commit()

        snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Projeto deletado!"))
        snack_bar.open = True

        dt.rows.clear()

        listar_proj('')

        dt.update()

    except Exception as e:
        print(e)

 
def listar_proj(rota):

    dt.rows.clear()

    c = conn.cursor()
    c.execute("SELECT * FROM projeto")
    users = c.fetchall()

    if not users == "":
        keys = ['idproj',
                'nomeproj',
                'codigocor', 
                'preposto', 
                'gerente',
                'gerenciacor', 
                'local',
                'nucleo', 
                'cliente',
                'razao',
                'coordenador',
                'numcontra',
                'centrocusto',
                'alimtrans',
                'responsavel',
                'gerencia',
                'fiscal',
                'fiscalemail',
                'gestor',
                'gestoremail',
                'diretoria',
                'objeto',
                'localidade',
                'treinamentos',
                'proderac',
                'cracha',
                'documento',
                'sistemamobi',
                'gestaomobi',
                'responmobi',
                'segtrab',
                'responprojadm',
                'responprojcam',
                'ordemserv']

        result = [dict(zip(keys, values)) for values in users]
        
        for x in result:
            dt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Row([
                            ft.IconButton(ft.icons.CREATE, icon_color="blue",
                                data= x,
                            ),
                            
                            ft.IconButton(ft.icons.DELETE, icon_color="red",
                                data= x['idproj'],
                                on_click= deletar
                            )
                        ])),

                        ft.DataCell(ft.Text(x['codigocor'])),
                        ft.DataCell(ft.Text(x['nomeproj'])),
                        ft.DataCell(ft.Text(x['preposto'])),
                        ft.DataCell(ft.Text(x['gerente'])),
                        ft.DataCell(ft.Text(x['gerenciacor'])),
                        ft.DataCell(ft.Text(x['local'])),
                        ft.DataCell(ft.Text(x['nucleo'])),
                        ft.DataCell(ft.Text(x['cliente'])),
                        ft.DataCell(ft.Text(x['razao'])),
                        ft.DataCell(ft.Text(x['coordenador'])),
                        ft.DataCell(ft.Text(x['numcontra'])),
                        ft.DataCell(ft.Text(x['centrocusto'])),
                        ft.DataCell(ft.Text(x['alimtrans'])),
                        ft.DataCell(ft.Text(x['responsavel'])),
                        ft.DataCell(ft.Text(x['gerencia'])),
                        ft.DataCell(ft.Text(x['fiscal'])),
                        ft.DataCell(ft.Text(x['fiscalemail'])),
                        ft.DataCell(ft.Text(x['gestor'])),
                        ft.DataCell(ft.Text(x['gestoremail'])),
                        ft.DataCell(ft.Text(x['diretoria'])),
                        ft.DataCell(ft.Text(x['objeto'])),
                        ft.DataCell(ft.Text(x['localidade'])),
                        ft.DataCell(ft.Text(x['treinamentos'])),
                        ft.DataCell(ft.Text(x['proderac'])),
                        ft.DataCell(ft.Text(x['cracha'])),
                        ft.DataCell(ft.Text(x['documento'])),
                        ft.DataCell(ft.Text(x['sistemamobi'])),
                        ft.DataCell(ft.Text(x['gestaomobi'])),
                        ft.DataCell(ft.Text(x['responmobi'])),
                        ft.DataCell(ft.Text(x['segtrab'])),
                        ft.DataCell(ft.Text(x['responprojadm'])),
                        ft.DataCell(ft.Text(x['responprojcam'])),
                        ft.DataCell(ft.Text(x['ordemserv'])),                       
                    ]
                ),
            )

    

    content = ft.Column([
        ft.Row(controls=[dt],scroll="always")
    ])
    return content 
