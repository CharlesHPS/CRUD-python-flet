import flet as ft
from controles.cabecalho import Cabecalho
import sqlite3
from datetime import datetime
from telas.tela_listar_colab import imprimir_data

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

def dropdown(tamanho: bool|int, titulo=None):
    return ft.Dropdown(
        height=30,
        width=tamanho,
        hint_style=ft.TextStyle(size=11),
        hint_text= titulo,
        text_size=13,
        border_width=1.5,
        content_padding=10,
    )    


def textField(tamanho: bool | int,multli = None,dados=None):
    return ft.TextField(
        dense=True,
        width=tamanho,
        multiline=multli,
        min_lines=1,
        max_length=dados,
        text_size=13,
        border_width=1.5,
        content_padding=10,
        cursor_width=1,
        cursor_height=20,    
    )

def text_field_container_data(nome: str, control1: ft.TextField|ft.Dropdown,control2: ft.TextField|ft.Dropdown = 0,control3: ft.TextField|ft.Dropdown=0):
    return ft.Container(
        expand=False,
        height=60,
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value=nome, size=13, weight="bold"),
                ft.Row(controls=[
                    control1,
                    ft.Text(value="/", size=13, weight="bold"),
                    control2,
                    ft.Text(value="/", size=13, weight="bold"),
                    control3,
                ]),
            ],
        ),
    )

def field_container(nome: str, control1: ft.TextField|ft.Dropdown|ft.SearchBar):
    return ft.Container(
        expand=None,
        height=60,
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value=nome, size=13, weight="bold"),
                control1,
            ],
        ),
    )



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



def criar_colab(rota):

    def salvar_colab(e):

        page = e.page

        nascimento_data_value = juntar_data(nascimento_dia_value.value,nascimento_mes_value.value,nascimento_ano_value.value)
        admissao_data_value = juntar_data(admissao_dia_value.value,admissao_mes_value.value,admissao_ano_value.value)
        cnh_data_value = juntar_data(cnh_dia_value.value,cnh_mes_value.value,cnh_ano_value.value)
        febre_data_value = juntar_data(febre_dia_value.value,febre_mes_value.value,febre_ano_value.value)
        anti_data_value = juntar_data(anti_dia_value.value,anti_mes_value.value,anti_ano_value.value)
        hepatite_data_value = juntar_data(hepatite_dia_value.value,hepatite_mes_value.value,hepatite_ano_value.value)
        covid_data_value = juntar_data(covid_dia_value.value,covid_mes_value.value,covid_ano_value.value)


        try:
            c = conn.cursor()
            c.execute("""INSERT INTO colaborador(
                cpf,
                nome,
                razaosocial,
                rg,
                estado,
                nascimento,
                admissao,
                pispasep,
                cnh,
                ctps,
                esocial,
                vinculo,
                setor,
                treinamento,
                febre,
                anti,
                hepatite,
                covid,
                idfuncoes,
                idcoordenador      
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                (cpf_value.value,nome_value.value,razao_value.value,rg_value.value,estado_value.value,
                 nascimento_data_value,admissao_data_value.value,pispasep_value.value,cnh_data_value,
                 ctps_value.value,esocial_value.value,vinculo_value.value,setor_cor_value.value,
                 treinamento_value.value,febre_data_value,anti_data_value,hepatite_data_value,
                 covid_data_value,1,1))
            conn.commit()

            limpar_box()

            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Colaborador cadastrado!"))

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

    def fechar_modal(e):
        page = e.page

        razao_modal.open = False

        page.update()

    def abrir_text_modal(e):
        page = e.page

        razao_modal.open = False

        razao_socio.visible = True

        page.update()

    razao_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirme por favor!!"),
        content=ft.Text("O sócio possui mais uma razão social?"),
        actions=[
            ft.TextButton("Sim", on_click=abrir_text_modal),
            ft.TextButton("Não", on_click=fechar_modal),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal fechado!"),
        )
    
    def verificar_vinculo(e):
        page = e.page
        if vinculo_value.value == "Sócio":
            if razao_socio.visible == False:

                page.dialog = razao_modal
                razao_modal.open = True
                page.update()
        elif vinculo_value.value != "Sócio":
            razao_socio.visible = False 
            page.update()

        if (vinculo_value.value == "CLT") or (vinculo_value.value == "Intermitente"):
            esocial.visible = True
            ctps.visible = True
            pispasep.visible = True
            page.update()
        else:
            esocial.visible = False
            ctps.visible = False
            pispasep.visible = False
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
                valid_treina_value.value=""

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

    def can_cnh(e):
        page = e.page

        if cnh_verificar.value == True:

            cnh_dia_value.disabled = True
            cnh_mes_value.disabled = True
            cnh_ano_value.disabled = True
            cnh_dia_value.value = ""
            cnh_mes_value.value = ""
            cnh_ano_value.value = ""

        else:
            cnh_dia_value.disabled = False
            cnh_mes_value.disabled = False
            cnh_ano_value.disabled = False
            

        page.update()

    def juntar_data(dia,mes,ano):

        data = dia +" "+ mes + " " + ano

        return data

    def limpar_box():

        cpf_value.value = ""
        nome_value.value = ""
        razao_value.value = ""
        rg_value.value = ""
        estado_value.value = ""            
        nascimento_dia_value.value = ""
        nascimento_mes_value.value = ""
        nascimento_ano_value.value = ""
        admissao_dia_value.value = ""
        admissao_mes_value.value = ""
        admissao_ano_value.value = ""
        pispasep_value.value = ""
        cnh_dia_value.value = ""
        cnh_mes_value.value = ""
        cnh_ano_value.value = ""
        ctps_value.value = ""
        esocial_value.value = ""
        vinculo_value.value = ""
        setor_cor_value.value = ""
        treinamento_value.value = ""
        febre_dia_value.value = ""
        febre_mes_value.value = ""
        febre_ano_value.value = ""
        anti_dia_value.value = ""
        anti_mes_value.value = ""
        anti_ano_value.value = ""
        hepatite_dia_value.value = ""
        hepatite_mes_value.value = ""
        hepatite_ano_value.value = ""
        covid_dia_value.value = ""
        covid_mes_value.value = ""
        covid_ano_value.value = ""
        funcao_value.value = ""
        coordenador_value.value = ""

        cpf.update()
        nome.update()
        razao.update()
        rg.update()
        estado.update()           
        nascimento.update()
        admissao.update()
        pispasep.update()
        cnh.update()
        ctps.update()
        esocial.update()
        vinculo.update()
        setor_cor.update()
        treinamento.update()
        febre.update()
        anti.update()
        hepatite.update()
        covid.update()
        funcao.update()
        coordenador.update()

    def inserir_dados():

        data = datetime.now().year
        cont_ano = data - 100        
        cont_dia_mes = 0
        cont = 0

        while cont_dia_mes <= 30:

            cont_dia_mes += 1

            treina_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            nascimento_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            admissao_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            cnh_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            febre_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            anti_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            hepatite_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            covid_dia_value.options.append(ft.dropdown.Option(cont_dia_mes))
            

        cont_dia_mes = 0

        while cont_dia_mes <= 11:

            cont_dia_mes += 1
            if cont_dia_mes <= 9:
                valid_treina_value.options.append(ft.dropdown.Option(cont_dia_mes))

            treina_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            nascimento_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            admissao_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            cnh_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            febre_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            anti_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            hepatite_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            covid_mes_value.options.append(ft.dropdown.Option(cont_dia_mes))
            
            

        cont_dia_mes = 0
        

        while data >= cont_ano:

            nascimento_ano_value.options.append(ft.dropdown.Option(data))
            admissao_ano_value.options.append(ft.dropdown.Option(data))
            
            if cont <= 20:
                treina_ano_value.options.append(ft.dropdown.Option(data))
                cnh_ano_value.options.append(ft.dropdown.Option(data))
                anti_ano_value.options.append(ft.dropdown.Option(data))

            if cont <= 50:
                febre_ano_value.options.append(ft.dropdown.Option(data))    
                hepatite_ano_value.options.append(ft.dropdown.Option(data))
                covid_ano_value.options.append(ft.dropdown.Option(data))
            
            cont += 1
            data -= 1



        
        vinculo_value.options.append(ft.dropdown.Option("PJ")),
        vinculo_value.options.append(ft.dropdown.Option("CLT")),
        vinculo_value.options.append(ft.dropdown.Option("Sócio")),
        vinculo_value.options.append(ft.dropdown.Option("Intermitente")),


    
        estado_value.options.append(ft.dropdown.Option("AC")),
        estado_value.options.append(ft.dropdown.Option("AL")),
        estado_value.options.append(ft.dropdown.Option("AP")),
        estado_value.options.append(ft.dropdown.Option("AM")),
        estado_value.options.append(ft.dropdown.Option("BA")),
        estado_value.options.append(ft.dropdown.Option("CE")),
        estado_value.options.append(ft.dropdown.Option("DF")),
        estado_value.options.append(ft.dropdown.Option("ES")),
        estado_value.options.append(ft.dropdown.Option("GO")),
        estado_value.options.append(ft.dropdown.Option("MA")),
        estado_value.options.append(ft.dropdown.Option("MT")),
        estado_value.options.append(ft.dropdown.Option("MS")),
        estado_value.options.append(ft.dropdown.Option("MG")),
        estado_value.options.append(ft.dropdown.Option("PA")),
        estado_value.options.append(ft.dropdown.Option("PB")),
        estado_value.options.append(ft.dropdown.Option("PR")),
        estado_value.options.append(ft.dropdown.Option("PE")),
        estado_value.options.append(ft.dropdown.Option("PI")),
        estado_value.options.append(ft.dropdown.Option("RJ")),
        estado_value.options.append(ft.dropdown.Option("RN")),
        estado_value.options.append(ft.dropdown.Option("RS")),
        estado_value.options.append(ft.dropdown.Option("RO")),
        estado_value.options.append(ft.dropdown.Option("RR")),
        estado_value.options.append(ft.dropdown.Option("SC")),
        estado_value.options.append(ft.dropdown.Option("SP")),
        estado_value.options.append(ft.dropdown.Option("SE")),
        estado_value.options.append(ft.dropdown.Option("TO")),
    
        c = conn.cursor()
        c.execute("SELECT * FROM funcoes")
        users = c.fetchall()

        if not users == "":
            keys = ['idfuncoes',
                    'nome']

            result = [dict(zip(keys, values)) for values in users]
            
            for x in result:

                funcao_value.options.append(ft.dropdown.Option((x['nome'])))   

        c.execute("SELECT * FROM razao")
        users = c.fetchall()

        if not users == "":
            keys = ['idrazao',
                    'nome']

            result = [dict(zip(keys, values)) for values in users]

            for x in result:

                razao_value.options.append(ft.dropdown.Option((x['nome']))) 
                razao_socio_value.options.append(ft.dropdown.Option((x['nome']))) 

        c.execute("SELECT * FROM coordenador")
        users = c.fetchall()

        if not users == "":
            keys = ['idcoordenador',
                    'nome']

            result = [dict(zip(keys, values)) for values in users]

            for x in result:

                coordenador_value.options.append(ft.dropdown.Option((x['nome'])))
   
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

    treina_list_proj = ft.Container(
        height=250,
		padding=8,
		content=ft.Column([
			treina_list_proj_value
 
		])
	)

    recebe_treina_value = ft.ListView(
        visible = True,
        height=250,
        width=500,
    )


    #criação de variaveis responsaveis por receber dados inseridos

    nome_value = textField(400)
    cpf_value = textField(150,None,11)
    rg_value = textField(120)
    estado_value = textField(50)
    pispasep_value = textField(105,None,11)
    ctps_value = textField(100,None,10)
    num_ctps_value = textField(55,None,4)
    esocial_value = textField(60)
    setor_cor_value = textField(60)
    treinamento_value = textField(60)

    vinculo_value = dropdown(130)
    estado_value = dropdown(120)    
    funcao_value = dropdown(300)                               
    razao_value = dropdown(220)
    razao_socio_value = dropdown(220)
    coordenador_value = dropdown(300)
    valid_treina_value = dropdown(60,"ANO")

    treina_dia_value = dropdown(60,"DIA")
    nascimento_dia_value = dropdown(60,"DIA")
    admissao_dia_value = dropdown(60,"DIA")
    cnh_dia_value = dropdown(60,"DIA")
    febre_dia_value = dropdown(60,"DIA")
    anti_dia_value = dropdown(60,"DIA")
    hepatite_dia_value = dropdown(60,"DIA")
    covid_dia_value = dropdown(60,"DIA")
    
    treina_mes_value = dropdown(60,"MES")
    nascimento_mes_value = dropdown(60,"MES")
    admissao_mes_value = dropdown(60,"MES")
    cnh_mes_value = dropdown(60,"MES")
    febre_mes_value = dropdown(60,"MES")
    anti_mes_value = dropdown(60,"MES")
    hepatite_mes_value = dropdown(60,"MES")
    covid_mes_value = dropdown(60,"MES")
    
    treina_ano_value = dropdown(60,"ANO")
    nascimento_ano_value = dropdown(60,"ANO")
    admissao_ano_value = dropdown(60,"ANO")
    cnh_ano_value = dropdown(60,"ANO")
    febre_ano_value = dropdown(60,"ANO")
    anti_ano_value = dropdown(60,"ANO")
    hepatite_ano_value = dropdown(60,"ANO")
    covid_ano_value = dropdown(60,"ANO") 

    cnh_verificar = ft.Checkbox(label="Não aplicável",
                                splash_radius=8,
                                on_change=can_cnh,
                                value=False)       

    inserir_dados()

    


#/////////////////////////////////////////////////////////////////////////////////
    
    #Organização dos Dropdown
    vinculo = field_container("Vinculo:", vinculo_value) #apenas 1 colocar duas razoes sociais para pj tambem 
    vinculo_value.on_change = verificar_vinculo
    estado = field_container("Estado de emissão:", estado_value) #apenas 1 
    funcao = field_container("Função:", funcao_value) #apenas 1 
    razao = field_container("Razão Social:", razao_value) #podera ter duas se for socio 
    razao_socio = field_container("Razão Social:", razao_socio_value)
    
    coordenador = field_container("Coordenador:",coordenador_value) #guardar o coordenador inserido no banco e trocar apenas na tela pelo do projeto

    #organização de textfilds
    nome = field_container("Nome:",nome_value) #tudo em letra maiuscula e sem acento 
    cpf = field_container("CPF:",cpf_value) #guardar junto e imprimir padrão apenas numeros 
    rg = field_container("RG:",rg_value) #apenas numeros
    pispasep = field_container("Pis/Pasep:",pispasep_value) #guardar e imprimir com o padrão apenas numeros
    esocial = field_container("Matrícula do E-social:",esocial_value) #apenas numeros 
    setor_cor = field_container("Setor Cor:",setor_cor_value) #tudo letras maiusculas

    con_treina_modal = text_field_container_data("",treina_dia_value,treina_mes_value,treina_ano_value)

    con_valid_treina = field_container("validade em anos:",valid_treina_value)

    treinamento = ft.Container(
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

    recebe_treina = ft.Column(
        controls=[ft.Text(value="",size= 12),
        ft.Container(border_radius=6,
        bgcolor="black54",
        content=recebe_treina_value)])

    ctps = ft.Container( #Tirar e colocar pra fazer automático o numero do cpf
        expand=False,
        height=60,
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(value="CTPS:", size=13, weight="bold"),
                ft.Row(vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ctps_value,
                        ft.Text(value="-", size=13, weight="bold"),
                        num_ctps_value, 

                    ]
                ),
            ],
        ),
    )

    treina_dat_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Data de realização do treinamento!"),
        content=ft.Row(controls=[
                    con_treina_modal,
                    con_valid_treina,
                    
                ]),
        actions=[
            ft.TextButton("OK", on_click=salve_data),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal fechado!"),
    )

    lista_data_treina = []
    lista_treina = []
    lista_valid_treina = []
    
    razao_socio.visible = False
    esocial.visible = False
    ctps.visible = False
    pispasep.visible = False

    #dropdown de datas
    
    anti = text_field_container_data("Antitetanica:",anti_dia_value,anti_mes_value,anti_ano_value) 
    
    febre = text_field_container_data("Febre amarela:",febre_dia_value,febre_mes_value,febre_ano_value) 
    hepatite = text_field_container_data("Hepatite B:",hepatite_dia_value,hepatite_mes_value,hepatite_ano_value) 
    covid = text_field_container_data("Covid-19:",covid_dia_value,covid_mes_value,covid_ano_value) 
    admissao = text_field_container_data("Data de admissão:",admissao_dia_value,admissao_mes_value,admissao_ano_value) 
    nascimento = text_field_container_data("Data de nascimento:",nascimento_dia_value,nascimento_mes_value,nascimento_ano_value) 
    cnh = ft.Container(
        expand=False,
        height=85,
        border_radius=6,
        padding=8,
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Row([ft.Text(value="CNH:", size=13, weight="bold"),cnh_verificar]),
                ft.Row(controls=[
                    cnh_dia_value,
                    ft.Text(value="/", size=13, weight="bold"),
                    cnh_mes_value,
                    ft.Text(value="/", size=13, weight="bold"),
                    cnh_ano_value,
                ]),
            ],
        ),
    )
    

    botao_cadastrar = ft.ElevatedButton(
            text="Cadastrar",
            style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
            on_click= salvar_colab
    )

    icon_transf = ft.Column(controls=[ft.Text(value=" ",),ft.Row(controls=[ft.Icon(ft.icons.ARROW_RIGHT_ALT)])])

    #inserção de dados na tela

    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Colaborador",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[ft.Text("Dados Pessoais:",
                size=20,
                weight="bold")]),
            ft.Row(controls=[nome]),
            ft.Row(controls=[nascimento,cpf,cnh,rg,estado]),
            ft.Row(controls=[vinculo,razao,razao_socio]),
            ft.Row(controls=[admissao]),
            ft.Row(controls=[pispasep, ctps, esocial]),
            ft.Row(controls=[funcao]),
            ft.Row(controls=[setor_cor]),
            ft.Row(controls=[coordenador]),
            ft.Row(controls=[treinamento,icon_transf,recebe_treina],
                   vertical_alignment=ft.CrossAxisAlignment.START),
            ft.Row(controls= [ft.Text("Cartão de vacina:",
                size=20,
                weight="bold")]),
            ft.Row(controls=[febre, anti, hepatite, covid]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content
