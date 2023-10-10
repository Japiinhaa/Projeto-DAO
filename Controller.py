from Model import *
import os

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):

        try:
            if tarefa == "":
                print("Digite uma tarefa válida.")

            else:

                try:
                    self.tarefa = tarefa
                    if TODO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa adicionada.")
                    else:
                        print("Algum problema foi encontrado.")

                except Exception as erro:
                    print("Erro ao adicionar a tarefa: {erro}")

        except Exception as erro:
                print("Erro ao adicionar a tarefa: {erro}")

class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir

        while True:
            try:
                try:
                    excluir_convertido = int(excluir)
                    excluir_convertido -= 1
            
                except Exception as erro:

                    print("Digite um número válido. Esta tarefa não existe.")
                    os.system("pause")
                    os.system("cls")

                if TODO.RemoverTarefa(self.excluir) == True:
                    print("Tarefa removida.")
                    break
                else:
                    print("Algum problema foi encontrado.")                
                    os.system("pause")
                    os.system("cls")

            except Exception as erro:
                print("Erro ao remover a tarefa: {erro}")
                os.system("pause")
                os.system("cls")

class ControllerListarTarefa():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        cont = 0

        for tarefas in ControllerLista:
            cont += 1
            print(f"{cont}. {tarefas}")