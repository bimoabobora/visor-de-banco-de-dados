import mysql.connector 
class DataBase:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lrm2",
            database="mydatabase",
            use_pure = True,
            autocommit = True
        )
        self.cursor = self.conexao.cursor()
    
    def CriarTabelas(self, nome, colunasArgs):
        query = f"CREATE TABLE %s()"
        self.cursor.execute()

    def AdicionarInfo(self, info: list, tabela: str, colunas: list):
        for i in range(len(colunas)):
            query = f"INSERT INTO {tabela} ({colunas[i]}) VALUES (%s)"
            self.cursor.execute(query, (info[i],))
        
        self.conexao.commit()

    def ExcluirInfo(self, tabela, condicao, valor):
        query = f"DELETE FROM {tabela} WHERE {condicao} = %s "
        self.cursor.execute(query, (valor,))

        self.conexao.commit()

    def AlterarInfo(self, tabela: str, colunaIdentificador: str, valorIdentificador: str,alternaColuna: str, alternaValor: str):
        query = f"UPDATE {tabela} SET {alternaColuna} = %s WHERE {colunaIdentificador} = %s"
        self.cursor.execute(query, (alternaValor,valorIdentificador,))

        self.conexao.commit()

    def MostrarInfo(self, tabela: str, condicao: str, valor: int):
        query = f"SELECT * FROM {tabela} where {condicao} = %s"
        self.cursor.execute(query, (valor,))

        info = self.cursor.fetchall()
        return info
    
    def MostrarTabelas(self):
        self.cursor.execute(
            "SHOW TABLES"
        )
        
        tabelas = self.cursor.fetchall()
        return tabelas
        
    def getColunas(self, tabela:str, comId: bool):
        
        if tabela == None:
            pass
        else:
            self.cursor.execute(
            f"SHOW COLUMNS FROM {tabela}"
         )

            colunasCompleto = self.cursor.fetchall()
            colunas = []
            for i in range(len(colunasCompleto)):
                if colunasCompleto[i][0] != "id" or comId:
                    colunas.append(colunasCompleto[i][0])

            return colunas

    def getInfo(self, tabela: str):
        self.cursor.execute(
        f"SELECT * FROM {tabela}"
        )

        info = self.cursor.fetchall()
        if info == []:
             return False
        return info
    
   

'''db = DataBase()
print(db.getInfo("testes2"))'''