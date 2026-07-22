import mysql.connector 
import json
class DataBase:
    def __init__(self):

        self.database()
    
    def connectDatabase(self, info: list):
        with open("Data_Base_config.txt", "a") as f:
            f.write(f"{info[0]}\n{info[1]}\n{info[2]}\n{info[3]}")

    def database(self):
        with open("config.json", "r") as f:
            self.config = json.load(f)
        
        self.conexao = mysql.connector.connect(
            host= self.config["host"],
            user= self.config["user"],
            password= self.config["password"],
            database= self.config["database"],
            use_pure = True,
            autocommit = True
            )
        self.cursor = self.conexao.cursor()


    def CriarTabelas(self, nome, StringQuery):
        print(nome, StringQuery)

        query = f"CREATE TABLE {nome} ({StringQuery})"
        self.cursor.execute(query)

        self.conexao.commit()

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