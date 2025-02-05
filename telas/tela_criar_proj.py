import flet as ft
from controles.cabecalho import Cabecalho
import sqlite3
from datetime import datetime
from telas.tela_criar_colab import field_container,textField,text_field_container_data

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)
     

def criar_projeto(rota):
        
    def salvar_projeto(e):

        page = e.page

        try:
            c = conn.cursor()
            c.execute("""INSERT INTO projeto (
                nomeproj,
                codigocor, 
                preposto, 
                gerente,
                gerenciacor, 
                local,
                nucleo, 
                cliente,
                razao,
                coordenador,
                numcontra,
                centrocusto,
                alimtrans,
                responsavel,
                gerencia,
                fiscal,
                fiscalemail,
                gestor,
                gestoremail,
                diretoria,
                objeto,
                localidade,
                treinamentos,
                proderac,
                cracha,
                documento,
                sistemamobi,
                gestaomobi,
                responmobi,
                segtrab,
                responprojadm,
                responprojcam,
                ordemserv
                ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                    ?,?,?,?,?,?)""",
                ())
            conn.commit()
            page.snack_bar = ft.SnackBar(bgcolor="#2BA84A",content=ft.Text("Projeto cadastrado!"))
            page.snack_bar.open = True
            page.update()
        except Exception as e:
            print(e) 

    def delete_treina(e):
        page = e.page

        nom = e.control.data

        del lista_treina[nom]

        add_treina(1)
        page.update()

    def add_treina(e):

        
        
        if e == 1:
            pass    
        elif not e.control.data == "":   
            page = e.page

            id = e.control.data

            lista_treina.append(id)

        print(lista_treina)

        num_itens = len(lista_treina)
        print(num_itens)
        cont = 0

        recebe_treina_value.controls.clear()
        recebe_treina.update()

        while (cont < num_itens):
            

            print(lista_treina[cont])
            
            item = lista_treina[cont]
            recebe_treina_value.controls.append(
                ft.Column(
                    scroll=ft.ScrollMode.ADAPTIVE,
                    controls=[ft.Row(
                        controls=[
                            ft.Text(width=5),
                            ft.Text((item),
                                width=330,
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
        
    def delete_proderac(e):
        page = e.page

        nom = e.control.data

        del lista_proderac[nom]

        add_proderac(1)
        page.update()

    def add_proderac(e):

        
        
        if e == 1:
            pass    
        elif not e.control.data == "":   
            page = e.page

            id = e.control.data

            lista_proderac.append(id)

        print(lista_proderac)

        num_itens = len(lista_proderac)
        print(num_itens)
        cont = 0

        recebe_proderac_value.controls.clear()
        recebe_proderac.update()

        while (cont < num_itens):
            

            print(lista_proderac[cont])
            
            item = lista_proderac[cont]
            recebe_proderac_value.controls.append(
                ft.Column(
                    scroll=ft.ScrollMode.ADAPTIVE,
                    controls=[ft.Row(
                        controls=[
                            ft.Text(width=5),
                            ft.Text((item),
                                width=330,
                                size=15,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.IconButton(
                                icon=ft.icons.CLOSE,        
                                icon_color="blue",
                                data= cont,
                                on_click=delete_proderac
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
                                width=350,
                                size=15,
                                weight=ft.FontWeight.BOLD,
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

    def listar_proderac(e):  
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
                proderac_list_proj_value.controls.clear()
                print(f"YOu result {resulte}")
                for x in resulte:
                    proderac_list_proj_value.controls.append(
                        ft.Row([
                            ft.Text((x['nome']),
                                width=350,
                                size=15,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.IconButton(
                                icon=ft.icons.ADD_ROUNDED,        
                                icon_color="blue",
                                data= x['nome'],
                                on_click=add_proderac,
                            ),
                        ])
                    )
                page.update()
            else:
                proderac_list_proj_value.controls.clear()
                page.update()   

    def tirar_text_ord(e):
        page = e.page

        botao_canord_con.visible = False
        numordser.visible = False

        page.update()

    def fechar_modal(e):
        page = e.page

        ord_modal.open = False

        page.update()

    def abrir_text_modal(e):
        page = e.page

        ord_modal.open = False

        botao_canord_con.visible = True
        numordser.visible = True

        page.update()

    ord_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirme por favor!!"),
        content=ft.Text("Existe ordem de serviço?"),
        actions=[
            ft.TextButton("Sim", on_click=abrir_text_modal),
            ft.TextButton("Não", on_click=fechar_modal),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal fechado!"),
        )
    
    def abrir_modal(e):
        page = e.page
        if numordser.visible == False:

            page.dialog = ord_modal
            ord_modal.open = True
            page.update()

    nome_proj_value = textField(400)
    codigo_proj_value = textField(400)
    preposto_proj_value = textField(400)
    gerente_proj_value = textField(400)
    gerencia_cor_proj_value = textField(400)
    local_proj_value = textField(400)
    nucleo_proj_value = textField(400)
    cliente_proj_value = textField(400)
    razao_proj_value = textField(400)
    coordenador_proj_value = textField(400)
    numordser_proj_value = textField(400) 
    centrocusto_proj_value = textField(400)
    responsavel_proj_value = textField(400)
    gerencia_proj_value = textField(400)
    fiscal_proj_value = textField(400)
    fiscal_email_proj_value = textField(400) 
    gestor_proj_value = textField(400)
    gestor_email_proj_value = textField(400) 
    diretoria_proj_value = textField(400)
    objeto_proj_value = textField(400,True)
    localidade_proj_value = textField(400)
    cracha_proj_value = textField(400)
    documento_proj_value = textField(400)
    sistemamobi_proj_value = textField(400)
    gestaomobi_proj_value = textField(400)
    responmobi_proj_value = textField(400)
    segtrab_proj_value = textField(400)
    responprojadm_proj_value = textField(400) 
    responprojcam_proj_value = textField(400) 
    ordemserv_proj_value = textField(400)
    obs_proj_value = textField(400,True)

    treina_proj_value = ft.TextField(
        dense=True,
        height=60,
        width=400,
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
        width=400,
    )

    treina_list_proj = ft.Container(
        height=200,
		padding=8,
		content=ft.Column([
			treina_list_proj_value
 
		])
	)

    lista_treina = []

    recebe_treina_value = ft.ListView(
        visible = True,
        height=250,
        width=400,
    )

    proderac_proj_value = ft.TextField(
        dense=True,
        height=60,
        width=400,
        min_lines=1,
        text_size=13,
        border_width=1.5,
        content_padding=10,
        cursor_width=1,
        cursor_height=20,
        on_change=listar_proderac   
    )

    lista_proderac = []

    recebe_proderac_value = ft.ListView(
        visible = True,
        height=250,
        width=400,
    )

    proderac_list_proj_value = ft.ListView(
        height=200,
        width=400,
    )

    proderac_list_proj = ft.Container(
        height=200,
		padding=8,
		content=ft.Column([
			proderac_list_proj_value
 
		])
	)

    numcontra_proj_value = ft.TextField(
        dense=True,
        width=400,
        on_blur=abrir_modal,
        min_lines=1,
        text_size=13,
        border_width=1.5,
        content_padding=10,
        cursor_width=1,
        cursor_height=20,    
    )

    alimtrans_proj_value = ft.Dropdown(
                height=30,
                width=200,
                text_size=13,
                border_width=1.5,
                content_padding=10,
                options=[
                    ft.dropdown.Option("NA"),
                    ft.dropdown.Option("Aplimentação/transporte"),
                    ft.dropdown.Option("Aplimentação"),
                    ft.dropdown.Option("Transporte"),
                    
                ],
            )
    
    nome = field_container("Nome do Projeto:",nome_proj_value)
    cod_proj = field_container("Código padrão Cor(CL-HC):",codigo_proj_value)
    preposto = field_container("Preposto do contrato:",preposto_proj_value)
    gerente = field_container("Gerente:",gerente_proj_value)
    gerencia_cor = field_container("Gerencia Cor:",gerencia_cor_proj_value)
    local = field_container("Local SSO:",local_proj_value)
    nucleo = field_container("Núcleo de mobilização:",nucleo_proj_value)
    cliente = field_container("Cliente:",cliente_proj_value)
    razao = field_container("Razão social COR do contrato:",razao_proj_value)
    coordenador = field_container("Coordenador COR responsavel:",coordenador_proj_value)
    numcontra = field_container("N° de contrato:",numcontra_proj_value) 
    centrocusto = field_container("Centro de custo do cliente:",centrocusto_proj_value)
    responsavel = field_container("Responsavel Vale pelo efetivo:",responsavel_proj_value)
    gerencia = field_container("Gerência executiva de área:",gerencia_proj_value)
    fiscal = field_container("Fiscal do contrato:",fiscal_proj_value) #adicionar mais caixinhas maximo 5 
    fiscal_email = field_container("E-mail do fiscal:",fiscal_email_proj_value)
    gestor = field_container("Gestor do contrato:",gestor_proj_value) #adicionar mais caixinhas maximo 5
    gestor_email = field_container("E-mail do gestor:",gestor_email_proj_value)
    diretoria = field_container("Diretoria:",diretoria_proj_value)
    objeto = field_container("Objeto:",objeto_proj_value)
    localidade = field_container("Localidade:",localidade_proj_value)  
    cracha = field_container("Passaporte/Crachá a ser emitido:",cracha_proj_value)
    documento = field_container("Documento legal utilizado quando necessário:",documento_proj_value)
    sistemamobi = field_container("Sistema de mobilização utilizado:",sistemamobi_proj_value)
    gestaomobi = field_container("Responsavel pela gestão do projeto(Contratos, subcontratos e colaboradores):",gestaomobi_proj_value)
    responmobi = field_container("Responsavel pela mobilização do projeto:",responmobi_proj_value)
    segtrab = field_container("Responsavel pela gestão de campo do projeto(Mobilizaçãode veiculos e documentação de campo):",segtrab_proj_value)
    responprojadm = field_container("TST responsavel pelo ADM do projeto:",responprojadm_proj_value)
    responprojcam = field_container("TST responsavel pelo campo do projeto:",responprojcam_proj_value)
    ordemserv = field_container("Vigência de ordem de serviço:",ordemserv_proj_value)
    obs = field_container("Observação:",obs_proj_value)

    treinamentos = ft.Container(
        padding=8,
        height=270,
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
    
    recebe_treina = ft.Column(controls=[ft.Text(value="",size= 12),
                              ft.Container(border_radius=6,
                              bgcolor="black54",
                              content=recebe_treina_value)])
    
    proderac = ft.Container(
        padding=8,
        height=270,
        border_radius=6,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.START,
            alignment=ft.MainAxisAlignment.START,
            spacing=1,
            controls=[
                ft.Text(value="PRO de RAC:", size=13, weight="bold"),
                ft.Row(height=30,
                    controls=[
                        proderac_proj_value,
                    ],
                ),
                proderac_list_proj,
                         
   
            ]
        )       
    )

    recebe_proderac = ft.Column(controls=[ft.Text(value="",size= 12),
                              ft.Container(border_radius=6,
                              bgcolor="black54",
                              content=recebe_proderac_value)])

    numordser = field_container("Ordem Serviço:",numordser_proj_value)
    alimtrans = field_container("Alimentação/transporte :",alimtrans_proj_value)
    

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar",
        style=ft.ButtonStyle(shape={"": ft.RoundedRectangleBorder(radius=8)}),
        on_click= salvar_projeto
    )

    botao_canord = ft.IconButton(icon=ft.icons.CLOSE,
                                 on_click= tirar_text_ord)

    botao_canord_con =ft.Container(
        content=ft.Column(
            spacing=1,
            controls=[
                ft.Text(""),
                ft.Row(controls=[
                    botao_canord,
                ]),
            ],
        ),
    )

    icon_transf = ft.Column(controls=[ft.Text(value=" ",),ft.Row(controls=[ft.Icon(ft.icons.ARROW_RIGHT_ALT)])])

    botao_canord_con.visible = False
    numordser.visible = False
    
    content = ft.Column([
            ft.Row(controls=[ft.Text("Cadastrar Projeto",
                size=25,
                weight="bold")],
                alignment=ft.MainAxisAlignment.CENTER),

            ft.Row(controls=[nome]),
            ft.Row(controls=[cod_proj,preposto]),
            ft.Row(controls=[gerente,gerencia_cor,local]),
            ft.Row(controls=[nucleo,cliente]),
            ft.Row(controls=[razao]),
            ft.Row(controls=[coordenador]),
            ft.Row(controls=[numcontra,numordser,botao_canord_con]),
            ft.Row(controls=[centrocusto,]),
            ft.Row(controls=[alimtrans,responsavel]),
            ft.Row(controls=[gerencia]),
            ft.Row(controls=[fiscal,fiscal_email]),
            ft.Row(controls=[gestor,gestor_email]),
            ft.Row(controls=[diretoria]),
            ft.Row(controls=[objeto]),
            ft.Row(controls=[localidade]),
            ft.Row(controls=[treinamentos,icon_transf,recebe_treina],
                   vertical_alignment=ft.CrossAxisAlignment.START),
            ft.Row(controls=[proderac,icon_transf,recebe_proderac],
                   vertical_alignment=ft.CrossAxisAlignment.START),
            ft.Row(controls=[cracha]),
            ft.Row(controls=[documento]),
            ft.Row(controls=[sistemamobi]),
            ft.Row(controls=[gestaomobi]),
            ft.Row(controls=[responmobi]),
            ft.Row(controls=[segtrab]),
            ft.Row(controls=[responprojadm,responprojcam]),
            ft.Row(controls=[ordemserv]),
            ft.Row(controls=[obs]),
            
            ft.Row(controls=[botao_cadastrar])          
        ]                   
    )

    return content