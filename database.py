import sqlite3


class Data_base:
    def __init__(self, name='system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)

################################################################
# CRIANDO O BANCO DE DADOS DOS PROFISSIONAIS E SEUS MÉTODOS
################################################################

    def create_table_profissionais(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Profissionais(
                    NOME TEXT,
                    CPF TEXT,
                    DATANASC TEXT,
                    GENERO TEXT,
                    primary key(CPF)
                );
            """)
        self.close_connection()

    def register_profissionais(self, fullDataSet):
        self.connect()
        campos_tabela = ('NOME', 'CPF', 'DATANASC', 'GENERO')
        qntd = ("?, ?, ?, ?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Profissionais{campos_tabela}

                VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "Ok", "Profissionais Cadastrado com Sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    def select_all_profissionais(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Profissionais ORDER BY NOME")
            profissionais = cursor.fetchall()
            return profissionais
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_profissionais(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Profissionais WHERE NOME ='{id}'")
            self.connection.commit()
            return 'Ok', 'Profissional deletado com Sucesso!'
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def update_profissionais(self, fulDataSet):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Profissionais set
                
                    NOME = '{fulDataSet[0]}',
                    CPF = '{fulDataSet[1]}',
                    DATANASC = '{fulDataSet[2]}',
                    GENERO = '{fulDataSet[3]}' 
                    
                    WHERE CPF = '{fulDataSet[1]}'""")
            self.connection.commit()
            return 'Ok', 'Dado atualizado com Sucesso!'
        except Exception as e:
            return 'Erro', str(e)

        finally:
            self.close_connection()


################################################################
# CRIANDO O BANCO DE DADOS DOS PACIENTES E SEUS MÉTODOS
################################################################

    def create_table_pacientes(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Pacientes(
                    NOME TEXT,
                    CPF TEXT,
                    DATANASC TEXT,
                    GENERO TEXT,
                    ALTURA TEXT,
                    PESO TEXT,
                    primary key(CPF)
                );
            """)
        self.close_connection()

    def register_pacientes(self, fullDataSet):
        self.connect()
        campos_tabela = ('NOME', 'CPF', 'DATANASC', 'GENERO', 'ALTURA', 'PESO')
        qntd = ("?, ?, ?, ?, ?, ?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Pacientes{campos_tabela}

                VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "Ok", "Paciente Cadastrado com Sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    def select_all_pacientes(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Pacientes ORDER BY NOME")
            pacientes = cursor.fetchall()
            return pacientes
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_paciente(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Pacientes WHERE NOME ='{id}'")
            self.connection.commit()
            return 'Ok', 'Paciente deletado com Sucesso!'
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def update_pacientes(self, fulDataSet):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Pacientes set
                
                    NOME = '{fulDataSet[0]}',
                    CPF = '{fulDataSet[1]}',
                    DATANASC = '{fulDataSet[2]}',
                    GENERO = '{fulDataSet[3]}',
                    ALTURA = '{fulDataSet[4]}',
                    PESO = '{fulDataSet[5]}'
                    
                    WHERE CPF = '{fulDataSet[1]}'""")
            self.connection.commit()
            return 'OK', 'Dados atualizados com sucesso!'
        except Exception as e:
            return 'erro', str(e)
        finally:
            self.close_connection()


################################################################
# CRIANDO O BANCO DE DADOS DOS AGENDAMENTOS E SEUS MÉTODOS
################################################################

    def create_table_agendamento(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute(
            """
                CREATE TABLE IF NOT EXISTS Agendamentos(
                    PACIENTE TEXT,
                    PROFISSIONAL TEXT,
                    DATA TEXT,
                    HORA TEXT,
                    primary key(HORA, PROFISSIONAL)
                );
            """)

        self.close_connection()

    def register_agendamento(self, fullDataSet):
        self.connect()
        campos_tabela = ('PACIENTE', 'PROFISSIONAL', 'DATA', 'HORA')
        qntd = ("?, ?, ?, ?")
        cursor = self.connection.cursor()

        try:
            cursor.execute(f"""INSERT INTO Agendamentos{campos_tabela}
            VALUES ({qntd})""", fullDataSet)
            self.connection.commit()
            return "Ok", "Agendamento Realizado com Sucesso!"
        except Exception as e:
            print(e)
            return 'erro', str(e)

        finally:
            self.close_connection()

    def select_all_agendamento(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM Agendamentos ORDER BY DATA")
            agenda = cursor.fetchall()
            return agenda
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def delete_agendamento(self, id):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute(f"DELETE FROM Agendamentos WHERE PACIENTE ='{id}'")
            self.connection.commit()
            return 'Ok', 'Registro deletado com Sucesso!'
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def update_agendamento(self, fulDataSet):
        self.connect()
        try:
            cursor = self.connection.cursor()
            cursor.execute(f""" UPDATE Agendamentos SET
                
                    PACIENTE = '{fulDataSet[0]}'
                    PROFISSIONAL = '{fulDataSet[1]}',
                    DATA = '{fulDataSet[2]}',
                    HORA = '{fulDataSet[3]}',
                    WHERE PACIENTE = '{fulDataSet[0]}'""")
            self.connection.commit()
        except Exception as e:
            print(e)

        finally:
            self.close_connection()
