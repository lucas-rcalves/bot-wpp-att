# BotWppAtt - Relatório de Desempenho via WhatsApp

Este projeto é uma automação em Python utilizando BotCity Desktop Automation, capaz de gerar e enviar relatórios de desempenho dinâmicos via WhatsApp Web. O bot coleta informações de desempenho do dia, personaliza a mensagem com saudação adequada ao horário e envia para o contato desejado, registrando logs de execução no BotCity Maestro.

---

## Sumário

- [Funcionalidades](#funcionalidades)
- [Fluxo de funcionamento](#fluxo-de-funcionamento)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como executar](#como-executar)
- [Personalização](#personalização)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Funcionalidades

- **Login e controle pelo BotCity Maestro:**  
  Integração total para rastreio e logs de execução automatizados.

- **Saudação dinâmica:**  
  A mensagem enviada possui saudação personalizada com base no horário do envio (Bom dia, Boa tarde, Boa noite).

- **Envio automatizado via WhatsApp Web:**  
  Acessa o WhatsApp Web, pesquisa o destinatário e envia o relatório detalhado.

- **Preenchimento automático de relatório:**  
  Copia dados de desempenho de outras aplicações, insere no template e envia para o destinatário.

- **Logs e finalização:**  
  Registra logs em Maestro e marca a tarefa como finalizada ao término.

---

## Fluxo de funcionamento

1. **Inicialização e log:**  
   - O bot inicializa via BotCity Maestro, recupera o ID da tarefa e registra log de início.

2. **Saudação dinâmica:**  
   - Obtém data e hora atual, determina a saudação apropriada.

3. **Login e navegação:**  
   - Acessa o sistema desejado e prepara ambiente para coleta dos dados.

4. **Envio via WhatsApp Web:**  
   - Abre o WhatsApp Web, pesquisa o destinatário (`ADTSA TI`), monta e envia a mensagem do relatório.

5. **Preenchimento dos dados:**  
   - Realiza cópias e colagens entre telas para preencher os campos do relatório.

6. **Finalização:**  
   - Envia mensagem de agradecimento, fecha o WhatsApp Web e marca a tarefa como concluída no Maestro.

---

## Tecnologias utilizadas

- **Python 3**
- [BotCity Desktop Automation](https://github.com/botcity-dev/botcity-framework)
- **BotCity Maestro SDK**

---

## Pré-requisitos

- Python 3.7+
- Google Chrome instalado (recomendado para WhatsApp Web)
- BotCity Maestro configurado e acesso ao servidor
- BotCity Desktop SDK instalado
- Permissão para acessar WhatsApp Web no computador

---

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/lucas-rcalves/BotWppAtt.git
    cd BotWppAtt
    ```

2. Instale as dependências:

    ```bash
    pip install botcity-framework botcity-maestro-sdk
    ```

---

## Configuração

- **BotCity Maestro:**  
  Configure os parâmetros de execução e credenciais conforme sua organização.

- **Elementos visuais:**  
  Certifique-se de que os elementos visuais (ícones, botões, campos) usados nos métodos `.find()` estejam capturados corretamente no projeto BotCity.

---

## Como executar

Execute o script principal diretamente, preferencialmente pelo Runner do BotCity Maestro:

```bash
python botwppatt.py
```

---

## Personalização

- **Template do relatório:**  
  Edite as strings `primeira_parte` e `segunda_parte` para personalizar o texto do relatório.

- **Destinatário:**  
  Altere o nome digitado em `digitar_texto_com_quebra("ADTSA TI", quebrar_linha=False)` para enviar o relatório para outros contatos/grupos.

- **Elementos visuais:**  
  Ajuste os nomes dos elementos usados em bot.find() conforme o projeto visual do BotCity.

---

## Contribuição

Sugestões e melhorias são bem-vindas!  
Envie um pull request ou abra uma issue.

---

## Licença

MIT

---
