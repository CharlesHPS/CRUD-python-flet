import flet as ft

def Cabecalho(page):

    def modo_escuro_claro(e):
        page = e.page
        if page.theme_mode == "dark":
            page.theme_mode = "light" 
            botao_iluminacao.selected = False 
            page.update()
            
        else: 
            page.theme_mode = "dark"
            botao_iluminacao.selected = True
            page.update()
            

    botao_colaboradores = ft.SubmenuButton(
        content=ft.Text("Colaboradores"),
        style=ft.ButtonStyle(color="#2BA84A",shape=ft.StadiumBorder()),       
        controls=[
            ft.MenuItemButton(
                content=ft.Text("Cadastrar"),
                leading=ft.Icon(ft.icons.CREATE),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click=lambda _: page.go('/criarColab'),
                   
            ),
            ft.MenuItemButton(
                content=ft.Text("Listar"),
                leading=ft.Icon(ft.icons.LIST),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/listarColab') 
                        
            ),
            ft.MenuItemButton(
                content=ft.Text("Gerar planilha"),
                leading=ft.Icon(ft.icons.FORMAT_ALIGN_LEFT),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/planilhaColab') 
                    
            ),
            ft.MenuItemButton(
                content=ft.Text("Verificar validade"),
                leading=ft.Icon(ft.icons.CALENDAR_MONTH),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/validadeColab') 
                    
            )
        ]
    )

    

    botao_projeto = ft.SubmenuButton(
        content=ft.Text("Projetos"),
        style=ft.ButtonStyle(color="#2BA84A",shape=ft.StadiumBorder()),
        controls=[
            ft.MenuItemButton(
                content=ft.Text("Cadastrar"),
                leading=ft.Icon(ft.icons.CREATE),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                on_click= lambda _: page.go('/criarProj'),   
            ),
            ft.MenuItemButton(
                content=ft.Text("Listar"),
                leading=ft.Icon(ft.icons.LIST),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/listarProj') 
                    
            ),
            ft.MenuItemButton(
                content=ft.Text("Adicionar colaborador"),
                leading=ft.Icon(ft.icons.CREATE),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click=lambda _: page.go('/addColabProj'),
            ),
            ft.MenuItemButton(
                content=ft.Text("Gerar planilha"),
                leading=ft.Icon(ft.icons.FORMAT_ALIGN_LEFT),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/planilhaProj') 
                    
            ),
        ]
    )

    botao_item = ft.SubmenuButton(
        content=ft.Text("Cadastros"),
        style=ft.ButtonStyle(color="#2BA84A",shape=ft.StadiumBorder()),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Razão Social"),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Cadastrar"),
                        leading=ft.Icon(ft.icons.CREATE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                        on_click= lambda _: page.go('/criarRazao')    
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Listar"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarRazao') 
                            
                    )
                ]
            ),

            ft.SubmenuButton(
                content=ft.Text("Funçoes"),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Cadastrar"),
                        leading=ft.Icon(ft.icons.CREATE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                        on_click= lambda _: page.go('/criarFuncoes')    
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Listar"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarFuncoes') 
                            
                    )
                ]
            ),

            ft.SubmenuButton(
                content=ft.Text("Coordenador"),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Cadastrar"),
                        leading=ft.Icon(ft.icons.CREATE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                        on_click= lambda _: page.go('/criarCoordenador')    
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Listar"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarCoordenador') 
                            
                    )
                ]
            ),

            ft.SubmenuButton(
                content=ft.Text("Treinamento"),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Cadastrar"),
                        leading=ft.Icon(ft.icons.CREATE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                        on_click= lambda _: page.go('/criarTreina')    
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Listar"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarTreina') 
                            
                    )
                ]
            ),
        ]
    )
    
    botao_iluminacao = ft.IconButton(icon=ft.icons.LIGHT_MODE,
        selected_icon= ft.icons.DARK_MODE,
        style=ft.ButtonStyle(color="#2BA84A"),
        on_click = modo_escuro_claro,
        selected=False,
    )
    
    botao_perfil = ft.SubmenuButton(
        content=ft.Icon(ft.icons.PERSON,color="#2BA84A"),
        style=ft.ButtonStyle(color="#2BA84A",shape=ft.StadiumBorder()),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("ADM"),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Criar Perfil"),
                        leading=ft.Icon(ft.icons.CREATE),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}), 
                        on_click= lambda _: page.go('/criarPerfil')    
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Listar Perfils"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarPerfil') 
                            
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Editar Afazeres"),
                        leading=ft.Icon(ft.icons.EDIT),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/editarAfazeres') 
                            
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Auditoria"),
                        leading=ft.Icon(ft.icons.LIST),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                        on_click= lambda _: page.go('/listarAuditoria') 
                            
                    )
                ]
            ),
            ft.MenuItemButton(
                content=ft.Text("Afazeres"),
                leading=ft.Icon(ft.icons.LIST),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/listaAfazeres') 
                            
            ),
            ft.MenuItemButton(
                content=ft.Text("Deslogar"),
                leading=ft.Icon(ft.icons.LOGOUT),
                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: "#2BA84A"}),
                on_click= lambda _: page.go('/Deslogar') 
                            
            )
        ]
    )
            


    

    icon_logo =  ft.Image(src="/logoClam.png", width=32, height=32)
    
    botao_inicio = ft.Container(content = ft.IconButton(ft.icons.HOME,style=ft.ButtonStyle(color="#2BA84A"), on_click=lambda _: page.go('/inicio')))
    colaboradores = ft.Container(content = botao_colaboradores)
    projeto = ft.Container(content = botao_projeto)
    item = ft.Container(content = botao_item)
    perfil = ft.Container(content = botao_perfil)
    iluminacao = ft.Container(content = botao_iluminacao)
    
    botoes_itens = ft.Container(
        content = 
            ft.Row(
                controls=[ 
                    botao_inicio,
                    colaboradores,
                    projeto,
                    item,
                ]
            )

    )

    cabecalho = ft.AppBar(
        leading = botoes_itens,          
        leading_width=800,           
        bgcolor="#184268",
        actions=[ 
            ft.Row(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    iluminacao,
                    perfil
                ]
            )
        ]
    )

    return cabecalho
