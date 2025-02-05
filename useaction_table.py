import sqlite3

conn = sqlite3.connect("novo_app/db/db_cor.db",check_same_thread=False)

def create_table():
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS projeto(
        projetoId INTEGER PRIMARY KEY AUTOINCREMENT,
        nomeproj TEXT,
        codigocor TEXT,
        preposto TEXT,
        gerente TEXT,
        gerenciacor TEXT,
        local TEXT,
        nucleo TEXT,
        cliente TEXT,
        razao TEXT,
        coordenador TEXT,
        numcontra TEXT,
        centrocusto TEXT,
        alimtrans TEXT,
        responsavel TEXT,
        gerencia TEXT,
        fiscal TEXT,
        fiscalemail TEXT,
        gestor TEXT,
        gestoremail TEXT,
        diretoria TEXT,
        objeto TEXT,
        localidade TEXT,
        treinamentos TEXT,
        proderac TEXT,
        cracha TEXT,
        documento TEXT,
        sistemamobi TEXT,
        gestaomobi TEXT,
        responmobi TEXT,
        segtrab TEXT,
        responprojadm TEXT,
        responprojcam TEXT,
        ordemserv TEXT)
        """)
    
    c.execute("""CREATE TABLE IF NOT EXISTS funcoes(
        idfuncoes INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT)
    """)

    c.execute("""CREATE TABLE IF NOT EXISTS treina(
        idtreina INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT)
    """)

    c.execute("""CREATE TABLE IF NOT EXISTS estar_treina(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projetoId INTEGER,
        idtreina INTEGER,
        FOREIGN KEY(projetoId) REFERENCES projeto(projetoId),
        FOREIGN KEY(idtreina) REFERENCES treina(idtreina))
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS coordenador(
        idcoordenador INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT)
    """)

    c.execute("""CREATE TABLE IF NOT EXISTS estar_projeto(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projetoId INTEGER,
        cpf INTEGER,
        FOREIGN KEY(projetoId) REFERENCES projeto(projetoId),
        FOREIGN KEY(cpf) REFERENCES colaborador(cpf))
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS ter_razao(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf INTEGER,
        idrazao INTEGER, 
        FOREIGN KEY(cpf) REFERENCES colaborador(cpf),
        FOREIGN KEY(idrazao) REFERENCES razao_social(idrazao))
        """)

    c.execute("""CREATE TABLE IF NOT EXISTS razao(
        idrazao INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT)
        """) 

    c.execute("""CREATE TABLE IF NOT EXISTS colaborador(
        cpf INTEGER PRIMARY KEY,
        nome TEXT,
        razaosocial TEXT,
        rg INTEGER,
        estado TEXT,
        nascimento TEXT,
        admissao INTEGER,
        pispasep INTEGER,
        cnh TEXT,
        ctps INTEGER,
        esocial TEXT,
        vinculo TEXT,
        setor TEXT,
        treinamento TEXT,
        febre TEXT,
        anti TEXT,
        hepatite TEXT,
        covid TEXT,
        idfuncoes INTEGER,
        idcoordenador INTEGER,
        FOREIGN KEY(idfuncoes) REFERENCES funcoes(idfuncoes),
        FOREIGN KEY(idcoordenador) REFERENCES coordenador(idcoordenador))
        """)
    conn.commit()
    conn.close()