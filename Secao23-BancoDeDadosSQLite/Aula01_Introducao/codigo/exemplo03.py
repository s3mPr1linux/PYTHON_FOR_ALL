import sqlite3


conexao = sqlite3.connect('agenda.db')
cursor = conexao.cursor()

cursor.execute("""
                create table if not exists contatos(
                id integer primary key,
                nome varchar(100),
                telefone varchar(15))
                """)

cursor.execute("""
                insert into contatos (nome, telefone)
                values(?, ?)
                """, ('Evaldo', "1234-5678"))

conexao.commit()
cursor.close()
conexao.close()