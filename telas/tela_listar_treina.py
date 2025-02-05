import flet as ft
from controles.cabecalho import Cabecalho
import sqlite3

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

dt = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Açoes")),
        ft.DataColumn(ft.Text("Nome")),
    ],
    rows=[]
)

def deletar_treina(e):
    try:
        myid = int(e.control.data)
        c = conn.cursor()
        c.execute("DELETE FROM treina WHERE idtreina=?", (myid,))
        conn.commit()
        snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Treinamento deletado!"))
        snack_bar.open = True
        dt.rows.clear()
        listar_treina('')
        dt.update()

    except Exception as e:
        print(e)


 
def listar_treina(rota):

    dt.rows.clear()

    c = conn.cursor()
    c.execute("SELECT * FROM treina")
    users = c.fetchall()

    if not users == "":
        keys = ['idtreina',
                'nome']

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
                                data= x['idtreina'],
                                on_click= deletar_treina
                            )
                        ])),
                        
                        ft.DataCell(ft.Text(x['nome'])),
    
                    ],
                ),
            )

    content = ft.Column([
        ft.Row(controls=[dt],scroll="always")
    ])
    return content 