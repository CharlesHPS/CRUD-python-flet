import flet as ft
import sqlite3
from datetime import datetime
from telas.tela_criar_colab import field_container,textField,dropdown,text_field_container_data
from telas.tela_listar_colab import imprimir_data

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

def add_colab_projeto(rota):
        
    def salvar_colab_projeto(e):
        page = e.page

        exame_data_value = juntar_data(exame_dia_value.value,exame_mes_value.value,exame_ano_value.value)   


        try:
            c = conn.cursor()
            c.execute("""INSERT INTO projeto (
                nomeproj,
                codigocor, 
                
                ) VALUES(?,?,?)""",
                ())
            conn.commit()
            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Projeto cadastrado para o colaborador!"))
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e)

    def salve_data(e):
 
        page = e.page

        data_treina = juntar_data(treina_dia_value.value,treina_mes_value.value,treina_ano_value.value)
            
        lista_data_treina.append(data_treina)
        
        lista_valid_treina.append(valid_treina_value.value)

        treina_dat_modal.open = False

        add_treina(1)

        page.update()

    def delete_treina(e):
        page = e.page

        nom = e.control.data

        del lista_treina[nom]
        del lista_data_treina[nom]
        del lista_valid_treina[nom]

        add_treina(1)

        page.update()

    def add_treina(e):

        
        
        if e == 1:
            pass    
        elif not e.control.data == "":   
            page = e.page

            id = e.control.data

            lista_treina.append(id)

            page.dialog = treina_dat_modal

            treina_dat_modal.open = True
        
            page.update()


        print(lista_treina)

        num_itens = len(lista_treina)
        num_itens_data = len(lista_data_treina)
        print(num_itens)
        cont = 0

        recebe_treina_value.controls.clear()
        recebe_treina.update()

        if num_itens_data > 0:
            while (cont < num_itens):
            
                treina_dia_value.value=""
                treina_mes_value.value=""
                treina_ano_value.value=""

                print(lista_treina[cont])  

                
                item_data = lista_data_treina[cont]

                item = lista_treina[cont]

                recebe_treina_value.controls.append(
                    ft.Column(
                        scroll=ft.ScrollMode.ADAPTIVE,
                        controls=[ft.Row(
                            controls=[
                                ft.Text(width=5),
                                ft.Text((item),
                                    width=340,
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(imprimir_data(item_data),
                                    expand=True,
                                    width=None,
                                    size=15,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.IconButton(
                                    icon=ft.icons.CLOSE,        
                                    icon_color="blue",
                                    data= cont,
                                    on_click=delete_treina
                                ),
                            ]
                        )]
                    )
                )
                

                cont = cont + 1

        if e == 1:
            pass

        elif not e.control.data == "":
            page.update() 

    def listar_treina(e):  
        page = e.page
        mysearch = e.control.value
        resulte = []

        c = conn.cursor()
        c.execute("SELECT * FROM treina")
        users = c.fetchall()

        
                        
        if not users == "":
            keys = ['idtreina','nome']

            result = [dict(zip(keys, values)) for values in users]
            print(result)

            if not mysearch == "":
                for item in result:
                    if mysearch in item['nome']:
                        resulte.append(item)
                page.update()

            if resulte:
                treina_list_proj_value.controls.clear()
                print(f"YOu result {resulte}")
                for x in resulte:
                    treina_list_proj_value.controls.append(
                        ft.Row([
                            ft.Text((x['nome']),
                                width=390,
                                size=15
                            ),
                            ft.IconButton(
                                icon=ft.icons.ADD_ROUNDED,        
                                icon_color="blue",
                                data= x['nome'],
                                on_click=add_treina,
                            ),
                        ])
                    )
                page.update()
            else:
                treina_list_proj_value.controls.clear()
                page.update()

    def juntar_data(dia,mes,ano):

        data = dia +" "+ mes + " " + ano

        return data

    def inserir_dados_dropdown():

        data = datetime.now().year
        cont_ano = data - 20        
        cont_dia_mes = 0
        cont = 0

        while cont_dia_mes <= 30:

            cont_dia_mes += 1

            aso_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            exame_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            treina_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))

        cont_dia_mes = 0

        while cont_dia_mes <= 11:

            cont_dia_mes += 1
            if cont_dia_mes <= 9:
                valid_treina_value.options.append(ft.dropdown.Option(cont_dia_mes))
            
            aso_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            exame_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            treina_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))    

        cont_dia_mes = 0
        

        while data >= cont_ano:

            exame_ano_value.options.append(ft.dropdown.Option(data))
            aso_ano_value.options.append(ft.dropdown.Option(data))

            if cont <= 20:
                treina_ano_value.options.append(ft.dropdown.Option(data))

            cont += 1
            data -= 1


        alimtrans_proj_value.options.append(ft.dropdown.Option("NA")),
        alimtrans_proj_value.options.append(ft.dropdown.Option("Alimentação")),
        alimtrans_proj_value.options.append(ft.dropdown.Option("Transporte")),
        alimtrans_proj_value.options.append(ft.dropdown.Option("Alimentação/transporte")),

        situacao_value.options.append(ft.dropdown.Option("Ativo")),
        situacao_value.options.append(ft.dropdown.Option("Inativo")),
        situacao_value.options.append(ft.dropdown.Option("Transferido")), # uma caixa para informar o codigo do projeto
        situacao_value.options.append(ft.dropdown.Option("Cedido")), # codigo do projeto tambem adicionar uma caixa para informar o projeto e uma caixinha para data ate quando ele vai ficar cedido

  

    nome_proj_value = textField(400)
    codigo_proj_value = textField(400)
    gerente_proj_value = textField(400)

    alimtrans_proj_value = dropdown(150)
    situacao_value = dropdown(150)
    exame_dia_value = dropdown(60,"DIA")    
    exame_mes_value = dropdown(60,"MES")   
    exame_ano_value = dropdown(60,"ANO")

    aso_dia_value = dropdown(60,"DIA")    
    aso_mes_value = dropdown(60,"MES")   
    aso_ano_value = dropdown(60,"ANO")

    treina_dia_value = dropdown(60,"DIA")
    treina_mes_value = dropdown(60,"MES")
    treina_ano_value = dropdown(60,"ANO")

    valid_treina_value = dropdown(60,"ANO")



    treina_proj_value = ft.TextField(
        dense=True,
        height=60,
        width=450,
        min_lines=1,
        text_size=13,
        border_width=1.5,
        content_padding=10,
        cursor_width=1,
        cursor_height=20,
        on_change=listar_treina    
    )

    treina_list_proj_value = ft.ListView(
        height=200,
        width=450,
    )

    recebe_treina_value = ft.ListView(
        visible = True,
        height=250,
        width=500,
    )

    treina_list_proj = ft.Container(
        height=250,
		padding=8,
		content=ft.Column([
			treina_list_proj_value
 
		])
	)

    lista_treina = []
    lista_data_treina = []
    lista_valid_treina = []
    
    inserir_dados_dropdown()
    
    nome = field_container("Nome do Colaborador:",nome_proj_value)
    cod_proj = field_container("CPF:",codigo_proj_value)
    gerente = field_container("Código padrão Cor(CL-HC):",gerente_proj_value)

    
    situacao = field_container("Situação:", situacao_value)  
    exame = text_field_container_data("Exames de atividades críticas:",exame_dia_value,exame_mes_value,exame_ano_value)   
    aso = text_field_container_data("ASO:",aso_dia_value,aso_mes_value,aso_ano_value)

    con_treina_modal = text_field_container_data("",treina_dia_value,treina_mes_value,treina_ano_value)

    con_valid_treina = field_container("validade em anos:",valid_treina_value)

    treinamentos = ft.Container(
        padding=8,
        height=350,
        border_radius=6,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.START,
            spacing=1,
            controls=[
                ft.Text(value="Treinamentos aplicáveis:", size=13, weight="bold"),
                ft.Row(height=30,
                    controls=[
                        treina_proj_value,
                    ],
                ),
                treina_list_proj,
                         
   
            ]
        )       
    )

    treina_dat_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Data de realização do treinamento!"),
        content=ft.Row(controls=[
                    con_treina_modal,
                    con_valid_treina
                ]),
        actions=[
            ft.TextButton("OK", on_click=salve_data),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal fechado!"),
    )

    recebe_treina = ft.Column(controls=[ft.Text(value="",size= 12),
                              ft.Container(border_radius=6,
                              bgcolor="black54",
                              content=recebe_treina_value)])

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_colab_projeto
    )
    icon_transf = ft.Column(controls=[ft.Text(value=" ",),ft.Row(controls=[ft.Icon(ft.icons.ARROW_RIGHT_ALT)])])
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Adicionar Colaborador à um Projeto",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),

            ft.Row(controls=[nome,cod_proj]),
            ft.Row(controls=[gerente]),
            ft.Row(controls=[situacao,exame,aso]),
            ft.Row(controls=[treinamentos,icon_transf,recebe_treina],
                   vertical_alignment=ft.CrossAxisAlignment.START),
            
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content