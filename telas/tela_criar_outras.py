import flet as ft
from controles.cabecalho import Cabecalho
import sqlite3
from datetime import datetime
from telas.tela_criar_colab import field_container,textField

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)


def criar_treina(rota):
        
    def salvar_treina(e):
        page = e.page
        try:
            c = conn.cursor()

            c.execute("""INSERT INTO treina(
                nome
                ) VALUES(?)""",
                (nome_treina_value.value,))
            conn.commit()

            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Treinamento cadastrado!"))
            
            page.snack_bar.open = True

            #limpar textField

            nome_treina_value.value = ""
            nome.update()

        except Exception as e:
            print(e)

    nome_treina_value = textField(400)

    nome = field_container("Nome:",nome_treina_value)

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_treina
    )
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Treinamento",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[nome]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content



#////////////////////////////////////////////////////////////////////////////////



def criar_funcoes(rota):
        
    def salvar_funcoes(e):
        page = e.page
        try:
            c = conn.cursor()

            c.execute("""INSERT INTO funcoes(
                nome
                ) VALUES(?)""",
                (nome_funcoes_value.value,))
            conn.commit()

            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Função cadastrada!"))
            
            page.snack_bar.open = True

            page.update()

            #limpar textField

            nome_funcoes_value.value = ""
            nome.update()

        except Exception as e:
            print(e)

    nome_funcoes_value = textField(400)

    nome = field_container("Nome:",nome_funcoes_value)

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_funcoes
    )
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Função",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[nome]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content



#////////////////////////////////////////////////////////////////////////////////



def criar_razao(rota):
        
    def salvar_razao(e):
        page = e.page
        try:
            c = conn.cursor()
            c.execute("""INSERT INTO razao(
                nome
                ) VALUES(?)""",
                (nome_razao_value.value,))
            conn.commit()
            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Função cadastrada!"))
            page.snack_bar.open = True
            page.update()
            #limpar textField

            nome_razao_value.value = ""
            nome.update()

        except Exception as e:
            print(e)

    nome_razao_value = textField(400)

    nome = field_container("Nome:",nome_razao_value)

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_razao
    )
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Razão Social",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),

            ft.Row(controls=[nome]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content



#////////////////////////////////////////////////////////////////////////////////



def criar_coordenador(rota):
        
    def salvar_coordenador(e):
        page = e.page
        try:
            c = conn.cursor()
            c.execute("""INSERT INTO coordenador(
                nome
                ) VALUES(?)""",
                (nome_coordenador_value.value,))
            conn.commit()
            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Coordenador cadastrada!"))
            page.snack_bar.open = True
            page.update()
            #limpar textField

            nome_coordenador_value.value = ""
            nome.update()

        except Exception as e:
            print(e)

    nome_coordenador_value = textField(400)

    nome = field_container("Nome:",nome_coordenador_value)

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_coordenador
    )
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Coordenador",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),

            ft.Row(controls=[nome]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content


#////////////////////////////////////////////////////////////////////////////////