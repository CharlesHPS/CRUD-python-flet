import flet as ft
from datetime import datetime,timedelta
from controles.cabecalho import Cabecalho
import sqlite3

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

dt = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Açoes")),
        ft.DataColumn(ft.Text("Nome")),
        ft.DataColumn(ft.Text("Razão Social")),
        ft.DataColumn(ft.Text("CPF")),
        ft.DataColumn(ft.Text("RG")),
        ft.DataColumn(ft.Text("Estado")),
        ft.DataColumn(ft.Text("Idade")),
        ft.DataColumn(ft.Text("Data de Nascimento")),
        ft.DataColumn(ft.Text("Data de Admissão")),
        ft.DataColumn(ft.Text("PIS/PASEP")),
        ft.DataColumn(ft.Text("CNH")),
        ft.DataColumn(ft.Text("Prazo em dias")),
        ft.DataColumn(ft.Text("CTPS")),
        ft.DataColumn(ft.Text("Matricula do E-social")),
        ft.DataColumn(ft.Text("Vinculo")),
        ft.DataColumn(ft.Text("Função")),
        ft.DataColumn(ft.Text("Setor Cor")),
        ft.DataColumn(ft.Text("Coordenador Imediato")),
        ft.DataColumn(ft.Text("Situação")),
        ft.DataColumn(ft.Text("Treinamentos")),
        ft.DataColumn(ft.Text("Exames")),
        ft.DataColumn(ft.Text("prazo em dias")),
        ft.DataColumn(ft.Text("Febre amarela")),
        ft.DataColumn(ft.Text("Prazo em dias")),
        ft.DataColumn(ft.Text("Antitetânica")),
        ft.DataColumn(ft.Text("Prazo em dias")),
        ft.DataColumn(ft.Text("Hepatite B")),
        ft.DataColumn(ft.Text("Prazo em dias")),
        ft.DataColumn(ft.Text("Covid 19")),
        ft.DataColumn(ft.Text("Prazo em dias")),
    ],
    rows=[]
)


def cal_idade(niver):

    data = datetime.strptime(niver,"%d %m %Y")
 
    hoje = datetime.now()
    
    idade = hoje.year - data.year

    if data.month >= hoje.month:
        if data.day >= hoje.day:
            idade = idade + 1

    return idade


def imprimir_data(data):

    dat = datetime.strptime(data,"%d %m %Y")

    imprimir_dat = f"{dat.day}/{dat.month}/{dat.year}"

    return imprimir_dat


def cal_validade(data):

    val = datetime.strptime(data,"%d %m %Y")
 
    hoje = datetime.now()
    
    dias_validade = hoje - val

    return dias_validade.days  



def deletar(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM colaborador WHERE cpf=?", (myid,))
        conn.commit()
        snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Colaborador deletado!"))
        snack_bar.open = True
        dt.rows.clear()
        listar_colab('')
        dt.update()

    except Exception as e:
        print(e)

 
def listar_colab(rota):

    dt.rows.clear()

    c = conn.cursor()
    c.execute("SELECT * FROM colaborador")
    users = c.fetchall()

    if not users == "":
        keys = ['cpf',
                'nome',
                'razaosocial',
                'rg',
                'estado',
                'nascimento',
                'admissao',
                'pispasep',
                'cnh',
                'ctps',
                'esocial',
                'vinculo',
                'setor',
                'situacao',
                'treinamento',
                'exames',
                'febre',
                'anti',
                'hepatite',
                'covid',
                'idfuncoes',
                'idcoordenador']

        result = [dict(zip(keys, values)) for values in users]
        
        for x in result:
            dt.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Row([
                            ft.IconButton(ft.icons.EDIT, icon_color="blue",
                                data= x,
                            ),
                            
                            ft.IconButton(ft.icons.DELETE, icon_color="red",
                                data= x['cpf'],
                                on_click= deletar
                            )
                        ])),
                        
                        ft.DataCell(ft.Text(x['nome'])),
                        ft.DataCell(ft.Text(x['razaosocial'])),
                        ft.DataCell(ft.Text(x['cpf'])),
                        ft.DataCell(ft.Text(x['rg'])),
                        ft.DataCell(ft.Text(x['estado'])),

                        ft.DataCell(ft.Text(cal_idade(x['nascimento']))),

                        ft.DataCell(ft.Text(imprimir_data(x['nascimento']))),
                        ft.DataCell(ft.Text(x['admissao'])),
                        ft.DataCell(ft.Text(x['pispasep'])),
                        ft.DataCell(ft.Text(imprimir_data(x['cnh']))),

                        ft.DataCell(ft.Text(cal_validade(x['cnh']))),

                        ft.DataCell(ft.Text(x['ctps'])),
                        ft.DataCell(ft.Text(x['esocial'])),
                        ft.DataCell(ft.Text(x['vinculo'])),
                        ft.DataCell(ft.Text(x['idfuncoes'])),
                        ft.DataCell(ft.Text(x['setor'])),
                        ft.DataCell(ft.Text(x['idcoordenador'])),
                        ft.DataCell(ft.Text(x['situacao'])),
                        ft.DataCell(ft.Text(x['treinamento'])),
                        ft.DataCell(ft.Text(imprimir_data(x['exames']))),

                        ft.DataCell(ft.Text(cal_validade(x['exames']))),

                        ft.DataCell(ft.Text(imprimir_data(x['febre']))),

                        ft.DataCell(ft.Text(cal_validade(x['febre']))),

                        ft.DataCell(ft.Text(imprimir_data(x['anti']))),

                        ft.DataCell(ft.Text(cal_validade(x['anti']))),

                        ft.DataCell(ft.Text(imprimir_data(x['hepatite']))),

                        ft.DataCell(ft.Text(cal_validade(x['hepatite']))),

                        ft.DataCell(ft.Text(imprimir_data(x['covid']))),

                        ft.DataCell(ft.Text(cal_validade(x['covid']))),
                    ],
                ),
            )

    

    content = ft.Column([
        ft.Row(controls=[dt],scroll="always")
    ])
    return content 
