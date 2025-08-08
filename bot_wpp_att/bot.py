
# Import for the Desktop Bot
from botcity.core import DesktopBot
import time
from datetime import datetime

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False


def main():
    # Runner passes the server url, the id of the task being executed,
    # the access token and the parameters that this task receives (when applicable).
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # Importing datetime library to define the timestamp of the execution
    # Creating a new log entry in the BotCity Maestro
    maestro.new_log_entry(
        activity_label="BotWppAtt",
        values={
            "timestamp": datetime.now().strftime("%Y-%m-%d_%H-%M"),
            "records": "10",
            "status": "SUCCESS"
        }
    )

    # Inicializa o bot
    bot = DesktopBot()

    # Obtém a data e hora atual
    agora = datetime.now()
    data_atual = agora.strftime("%d/%m/%Y")
    hora_atual = agora.hour

    # Determina a saudação com base no horário
    if 5 <= hora_atual < 12:
        saudacao = "Bom dia"
    elif 12 <= hora_atual < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"



    # Searching for element 'IconNextIP '
    if not bot.find("IconNextIP", matching=0.97, waiting_time=10000):
        not_found("IconNextIP")
    bot.click()


    # Searching for element 'NEXT2 '
    if not bot.find("NEXT2", matching=0.97, waiting_time=10000):
        not_found("NEXT2")
    
    bot.paste("")
    bot.tab()
    bot.paste("")
    bot.enter()
    time.sleep(30)

    
    # Searching for element 'DropDownSeta '
    if not bot.find("DropDownSeta", matching=0.97, waiting_time=10000):
        not_found("DropDownSeta")
    bot.click()

    # Repete a ação type_down 24 vezes
    for _ in range(24):
        bot.type_down()

    bot.enter()
    bot.type_keys(["win", "up"])


    bot.browse("http://web.whatsapp.com")
    time.sleep(30)

    
    # Searching for element 'Lupa '
    if not bot.find("Lupa", matching=0.97, waiting_time=10000):
        not_found("Lupa")
    bot.click()
    
    
    # Função para digitar texto com quebra de linha
    def digitar_texto_com_quebra(texto, quebrar_linha=True):
        bot.type_keys_with_interval(50, texto)
        if quebrar_linha:
            bot.type_keys(["shift", "enter"])

    # Digita o nome do destinatário
    digitar_texto_com_quebra("ADTSA TI", quebrar_linha=False)
    time.sleep(3)
    bot.enter()

    # Primeira parte do relatório com saudação dinâmica
    primeira_parte = f"""
*Relatório de Desempenho - Dia {data_atual}*

{saudacao},

Segue o resumo do nosso desempenho no dia *{data_atual}:*

● Total de ligações recebidas: *XXX*
● Total de ligações atendidas: *XZX*
● Total de ligações abandonadas: *XYX*
● Porcentual de abandonos: *X1X*
● TMA: *X2X*
● TME: *X3X*
"""

    # Digita a primeira parte do relatório
    for linha in primeira_parte.strip().split("\n"):
        digitar_texto_com_quebra(linha)

    # Restante do código permanece igual...
    bot.type_keys(["alt", "tab"])
    time.sleep(4)
    bot.click_at(346, 98)
    bot.click_at(346, 98)
    bot.control_c()

    bot.type_keys(["alt", "tab"])
    
    # Searching for element 'XXX '
    if not bot.find("XXX", matching=0.97, waiting_time=10000):
        not_found("XXX")
    bot.double_click()
    bot.control_v()

    bot.type_keys(["alt", "tab"])
    bot.tab()
    bot.control_c()
    bot.type_keys(["alt", "tab"])

    # Searching for element 'XZX '
    if not bot.find("XZX", matching=0.97, waiting_time=10000):
        not_found("XZX")
    bot.double_click()
    bot.control_v()

    bot.type_keys(["alt", "tab"])
    bot.tab()
    bot.control_c()
    bot.type_keys(["alt", "tab"])
    
    
    # Searching for element 'XYX '
    if not bot.find("XYX", matching=0.97, waiting_time=10000):
        not_found("XYX")
    bot.double_click()
    bot.control_v()

    bot.type_keys(["alt", "tab"])
    bot.tab()
    bot.control_c()
    bot.type_keys(["alt", "tab"])


    
    # Searching for element 'X1X '
    if not bot.find("X1X", matching=0.97, waiting_time=10000):
        not_found("X1X")
    bot.double_click()
    bot.control_v()

    bot.type_keys(["alt", "tab"])
    bot.tab()
    bot.tab()
    bot.tab()
    bot.control_c()
    bot.type_keys(["alt", "tab"])
    
    
    
    # Searching for element 'X2X '
    if not bot.find("X2X", matching=0.97, waiting_time=10000):
        not_found("X2X")
    bot.double_click()
    bot.control_v()

    bot.type_keys(["alt", "tab"])
    bot.tab()
    bot.control_c()
    bot.alt_f4()

    
    # Searching for element 'X3X '
    if not bot.find("X3X", matching=0.97, waiting_time=10000):
        not_found("X3X")
    bot.double_click()
    bot.control_v()

    bot.type_down()
    bot.type_keys(["shift", "enter"])

    # Segunda parte do relatório
    segunda_parte = """

Agradecemos pelo empenho de todos e seguimos focados em melhorar nossos resultados!

Atenciosamente,
Departamento de TI.
"""

    # Digita a segunda parte do relatório
    for linha in segunda_parte.strip().split("\n"):
        digitar_texto_com_quebra(linha)

    bot.enter()
    time.sleep(3)

    bot.alt_f4()
    time.sleep(5)
    bot.enter()


    # # Uncomment to mark this task as finished on BotMaestro
    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )



def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()









