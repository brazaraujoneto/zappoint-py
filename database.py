import sqlite3

def criar_banco():
    conexao = sqlite3.connect('ponto.db')
    cursor = conexao.cursor()
    
    # Cria a tabela de batida de ponto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS batidas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,  
            horario TEXT NOT NULL,  
            status BOOLEAN NOT NULL  
        )
    ''')
    
    conexao.commit()
    conexao.close()
    
    print("Banco de dados e tabela criados com sucesso!")

# Chama a função para criar o banco
criar_banco()


def adicionar_batida(tipo, horario, status):
    conexao = sqlite3.connect('ponto.db')
    cursor = conexao.cursor()
    
    cursor.execute('''
        INSERT INTO batidas (tipo, horario, status)
        VALUES (?, ?, ?)
    ''', (tipo, horario, status))
    
    conexao.commit()
    conexao.close()
    
    print("Batida adicionada com sucesso!")