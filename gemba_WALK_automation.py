#programação selenium google chrome 117.05938.92

from selenium import webdriver
import time
import random
import sys

# Verifique se há argumentos suficientes
if len(sys.argv) < 4:
    print("Uso: python gemba_WALK_automation.py <numero_de_confirmações> <nome> <email>")
    sys.exit(1)

# Acesse os argumentos
numero_de_confirmações = int(sys.argv[1])
nome = sys.argv[2]
email = sys.argv[3]

# Converte a string em um número inteiro
try:
    numero_de_confirmacoes = int(numero_de_confirmações)
except ValueError:
    print("Erro: O argumento deve ser um número inteiro.")
    sys.exit(1)

# Agora você pode usar a variável 'numero_de_confirmacoes' como um número inteiro em seu código
print(f"Numero de confirmacoes: {numero_de_confirmações}")

contador = 1

# Define o caminho do ChromeDriver
chrome_driver_path = "C:\\Users\\iusle\\Desktop\\automacao-com-python\\chromedriver.exe"

# Inicia o ChromeDriver
driver = webdriver.Chrome(chrome_driver_path)

# Abre o site
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdzjpYzVuaa9vaGTAOuIdMj4Cc1ihkfIfTt3cj4tSMJx-MAlA/viewform")
# Aguarde 10 segundos (ou o tempo desejado)
time.sleep(15)


while contador <= numero_de_confirmações:
    time.sleep(2)
    # Localize o elemento de entrada do tipo email por classe
    email_input = driver.find_element_by_class_name('whsOnd')  # Substitua 'sua_classe' pela classe correta

    # Preencha o campo de email com o endereço de email desejado
    email_input.send_keys(f"{email}")
    time.sleep(2)

    # Encontre o elemento usando o XPath fornecido - UGB2
    elemento = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")

    # Clique no elemento
    elemento.click()
    time.sleep(2)


    # Encontre o elemento usando o XPath fornecido - TARDE
    elemento = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div")

    # Clique no elemento
    elemento.click()
    time.sleep(2)


    # Encontre o elemento usando o XPath fornecido - SUPERVISOR
    elemento = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div")

    # Clique no elemento
    elemento.click()
    time.sleep(2)

    # Encontre o elemento usando o XPath fornecido - SETOR:
    xpaths = {
        "prensas": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",
        "mistura_final": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div"
    }

    # Gere um número aleatório para escolher entre os nomes de XPath
    nome_xpath_selecionado_setor = random.choice(list(xpaths.keys()))

    # Use o XPath selecionado aleatoriamente
    elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_setor])
    elemento.click()

    js_code = f"console.log('Nome do XPath Selecionado: \"{nome_xpath_selecionado_setor}\"');"
    driver.execute_script(js_code)
    time.sleep(2)

    # Encontre o campo de entrada de texto usando o XPath (substitua pelo XPath correto)
    campo_texto_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input"

    # Localize o campo de entrada de texto
    campo_texto = driver.find_element_by_xpath(campo_texto_xpath)

    # Insira texto no campo de entrada
    texto_para_inserir = f"{nome}"
    campo_texto.send_keys(texto_para_inserir)
    time.sleep(2)

    # Encontre o elemento usando o XPath fornecido - MODO DE FALHA:
    xpaths = {
        "bolha": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
        "encolhido": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
        "sujeira_fragmento": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div",
        "falta_de_material": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",
    }

    # Gere um número aleatório para escolher entre os nomes de XPath
    nome_xpath_selecionado_modo_de_falha = random.choice(list(xpaths.keys()))

    # Use o XPath selecionado aleatoriamente
    elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_modo_de_falha])
    elemento.click()

    js_code = f"console.log('Nome do XPath Selecionado: \"{nome_xpath_selecionado_modo_de_falha}\"');"
    driver.execute_script(js_code)
    time.sleep(2)


    # Encontre o elemento usando o XPath fornecido - BOTÃO PRÓXIMO - FINAL DA PÁGINA
    elemento = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span")
    elemento.click()
    time.sleep(10)


    # Use a opção para decidir qual sequência de cliques executar
    if nome_xpath_selecionado_modo_de_falha == "bolha":                                                             #BOLHA
        #------------------------------------------------------------------------------------------------------------------------------------------------1
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------2
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------3
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------4
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------5
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------6
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------7
        xpaths = {
            #"sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------8
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------9
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------10
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------11
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------12
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------13
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------14
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------15
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[30]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[30]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------16
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[32]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[32]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------17
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[34]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[34]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------18
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[36]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[36]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------19
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[38]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[38]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)


        #------------------------------------------------------------------------------------------------------------------------------------------------20
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[40]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[40]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #--------------------------------------------------------------------------------------------------------------------------------------------------21
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[42]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[42]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------22
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[44]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[44]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------23
        xpaths = {
            #"sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[46]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[46]/span/div[3]/div/div/div[3]/div",
            "nao_aplica": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[46]/span/div[4]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------24
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[48]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[48]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------25
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[50]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[50]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------26
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[52]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[52]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------27
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[54]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[54]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------28
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[56]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[56]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------29
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[58]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[58]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------30
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[60]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[60]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------31
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[62]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[62]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------32
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[64]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[64]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------33
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[66]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[66]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------34
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[68]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[68]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------35
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[70]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[70]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------36
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[72]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[72]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------37
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[74]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[74]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------38
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[76]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[76]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------39
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[78]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[78]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)


        #------------------------------------------------------------------------------------------------------------------------------------------------40
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[80]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[80]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------41
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[82]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[82]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------42
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[84]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[84]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #BOTÃO ENVIAR------------------------------------------------------------------------------------------------------------------------------------
        elemento = driver.find_element_by_xpath(" /html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")

        # Clique no elemento
        elemento.click()
        time.sleep(4)

        # Atualize a página
        driver.refresh()
        time.sleep(60)

    elif nome_xpath_selecionado_modo_de_falha == "encolhido":                                                       #ENCOLHIDO
        #------------------------------------------------------------------------------------------------------------------------------------------------1
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------2
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------3
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------4
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------5
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------6
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------7
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #BOTÃO ENVIAR------------------------------------------------------------------------------------------------------------------------------------
        elemento = driver.find_element_by_xpath(" /html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")

        # Clique no elemento
        elemento.click()
        time.sleep(4)

        # Atualize a página
        driver.refresh()
        time.sleep(60)

    elif nome_xpath_selecionado_modo_de_falha == "sujeira_fragmento":                                               #SUJEIRA/FRAGMENTO
        #------------------------------------------------------------------------------------------------------------------------------------------------1
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------2
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------3
        xpaths = {
            #"sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------4
        xpaths = {
            #"sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------5
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------6
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------7
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------8
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[16]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------9
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[18]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------10
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[20]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------11
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[22]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------12
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------13
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[26]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------14
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[28]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------15
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[30]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)
    
        #------------------------------------------------------------------------------------------------------------------------------------------------16
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[32]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------17
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[34]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[34]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------18
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[36]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------19
        xpaths = {
            #"sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[32]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[38]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)


        #------------------------------------------------------------------------------------------------------------------------------------------------20
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[40]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[24]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)


                #BOTÃO ENVIAR-----------------------------------------------------------------------------------------------------------------------------
        elemento = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")

        # Clique no elemento
        elemento.click()
        time.sleep(5)

        # Atualize a página
        driver.refresh()
        time.sleep(60)

    else:                                                                                                           #FALTA DE MATERIAL
        #------------------------------------------------------------------------------------------------------------------------------------------------1
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------2
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------3
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[6]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------4
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[8]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------5
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[10]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------6
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[2]/div/div/div[3]/div",
            #"nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[12]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #------------------------------------------------------------------------------------------------------------------------------------------------7
        xpaths = {
            "sim": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[2]/div/div/div[3]/div",
            "nao": "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[14]/span/div[3]/div/div/div[3]/div",
        }

        # Gere um número aleatório para escolher entre os nomes de XPath
        nome_xpath_selecionado_sim_nao = random.choice(list(xpaths.keys()))

        # Use o XPath selecionado aleatoriamente
        elemento = driver.find_element_by_xpath(xpaths[nome_xpath_selecionado_sim_nao])
        elemento.click()
        time.sleep(2)

        #BOTÃO ENVIAR------------------------------------------------------------------------------------------------------------------------------------
        elemento = driver.find_element_by_xpath(" /html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")

        # Clique no elemento
        elemento.click()
        time.sleep(4)

        # Atualize a página
        driver.refresh()
        time.sleep(60)

    contador += 1