from reportlab.pdfgen import canvas
from PyQt5 import uic,QtWidgets
import mysql.connector

#variavel global
numero_id = 0

#conectar com o banco de dados
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro"
)

#define a funcao do botao login
def chama_logout():
    login.label_4.setText("")
    nome_usuario = login.lineEdit.text()
    senha = login.lineEdit_2.text()
    if nome_usuario == "admin" and senha == "admin" :
        login.close()
        logout.show()
    else :
        login.label_4.setText("                                                        ERRO: USUÁRIO OU SENHA INVALIDO")

#chamar a tela de cadastro   
def funcao_cadastro():
    cadastro.show()

#define a funcao do botao logout
def funcao_logout():
    logout.close()
    login.show()


def funcao_cadastro2():
    #dados do aluno
    codigo = cadastro.line_codigo.text()
    matricula = cadastro.line_matricula.text()
    nome_aluno = cadastro.line_nome_aluno.text()
    datanascimento = cadastro.line_dtnascimento.text()
    telefone = cadastro.line_telefone.text()
    alimento = cadastro.line_alimentos.text()

    #cadastrar no banco de dados
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO alunos (codigo, matricula, nome_aluno, datanascimento, telefone, alimentos) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (str(codigo), str(matricula), str(nome_aluno), str(datanascimento), str(telefone), str(alimento))
    cursor.execute(comando_SQL,dados)
    banco.commit()

    #limpar a area de cadastro
    cadastro.line_codigo.setText("")
    cadastro.line_matricula.setText("")
    cadastro.line_nome_aluno.setText("")
    cadastro.line_dtnascimento.setText("")
    cadastro.line_telefone.setText("")
    cadastro.line_alimentos.setText("")


#chamar a tela de pesquisa de alunos
def funcao_pesquisar():
    pesquisar.label_gerarpdf.setText("")
    pesquisar.show()

#pesquisa de um aluno específico
def funcao_pesquisar3():
    linha = pesquisar.line_codigo.text()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM alunos WHERE codigo = '{}'".format(linha)
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()

    pesquisar.tableWidget.setColumnCount(len(dados_lidos))
    pesquisar.tableWidget.setRowCount(7)

    for j in range(0, len(dados_lidos)):
        for i in range(0, 7):
            pesquisar.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[j][i])))

pesquisar_nomes = []

#adicionar alimentos na lista
def pesquisar_dados():
   dado_lido = pesquisar.lineEdit.text()
   pesquisar_nomes.append(dado_lido)
   pesquisar.listWidget.addItem(dado_lido)
   pesquisar.lineEdit.setText("")

#apagar a lista
def deletar():
    pesquisar.listWidget.clear()
    pesquisar_nomes.clear()

#gerar o pdf com os alimentos restritos
def gerar_pdf():

    pesquisar.label_gerarpdf.setText(" O PDF COM OS ALIMENTOS FOI GERADO ")
    data = pesquisar.lineEdit_data.text()
    y = 0
    pdf = canvas.Canvas('pdf_alimentos_restritos_{}.pdf'.format(data))
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(100,800, "Alimentos Restritos:")
    pdf.setFont("Times-Bold", 18)

    for nome in pesquisar_nomes:
        y = y + 50
        pdf.drawString(100,800 - y, nome)

    pdf.save()
    print(pesquisar_nomes)

#Chamar o aplicativo e declarar as funcoes e os botoes
app=QtWidgets.QApplication([])
login=uic.loadUi("login.ui")
logout=uic.loadUi("logout.ui")
cadastro=uic.loadUi("cadastro.ui")
pesquisar=uic.loadUi("pesquisar.ui")
pesquisar=uic.loadUi("pesquisar.ui")


login.pushButton_login.clicked.connect(chama_logout)
login.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
logout.pushButton_logout.clicked.connect(funcao_logout)
logout.pushButton_pesquisa.clicked.connect(funcao_pesquisar)
logout.pushButton_cadastro.clicked.connect(funcao_cadastro)
pesquisar.pushButton_pesquisar.clicked.connect(funcao_pesquisar3)
cadastro.pushButton.clicked.connect(funcao_cadastro2)
pesquisar.pushButton.clicked.connect(pesquisar_dados)
pesquisar.pushButton_excluir.clicked.connect(deletar)
pesquisar.pushButton_gerarpdf.clicked.connect(gerar_pdf)

login.show()
app.exec()