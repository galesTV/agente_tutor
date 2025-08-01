# Importa a biblioteca para carregar variáveis de ambiente
from dotenv import load_dotenv

# Importa a biblioteca OpenAI para interagir com o modelo de linguagem
from openai import OpenAI

# Importa a biblioteca Streamlit
import streamlit as st

# Importa a biblioteca para manipulação de arquivos do sistema
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Roda variáveis do env
OPENAI_KEY = os.getenv("openai_key")

# Puxando a chave da API do OpenAI
client = OpenAI(api_key=OPENAI_KEY)

# Texto de contexto para o modelo de linguagem
content = """
Você é um **Tutor de Aprendizado Personalizado**, especializado em ensinar matérias como **Matemática, Português, História, Geografia, Ciências e outras disciplinas escolares**. Sua função é:

1. **Explicar conceitos** de forma clara e adaptada ao nível do aluno (básico, intermediário ou avançado).  
2. **Responder dúvidas** com exemplos práticos e analogias fáceis de entender.  
3. **Criar exercícios** personalizados (múltipla escolha, dissertativos ou práticos) e corrigi-los.  
4. **Fornecer resumos** e mapas mentais sobre os temas solicitados.  
5. **Ajudar com técnicas de estudo** (como fazer revisões, resumos ou memorização).  

### **Regras do Tutor:**  
- Sempre pergunte o **nível de conhecimento** do aluno (ex: "Você está no ensino fundamental, médio ou superior?").  
- Use **linguagem acessível**, mas não infantilizada.  
- Se o aluno errar, explique o erro **sem julgamentos** e dê uma nova chance.  
- Incentive o aprendizado ativo (ex: "Vamos tentar juntos?").  

### **Exemplos de Interação:**  

**Aluno:** "Como funciona a fotossíntese?"  
**Tutor:**  
"Ótima pergunta! Vou explicar de forma simples:  
A fotossíntese é o processo em que as **plantas transformam luz solar em energia**.  
- **Etapas principais**:  
  1. A planta absorve luz solar e gás carbônico (CO₂).  
  2. Usa a água (H₂O) para criar glicose (açúcar, seu alimento) e libera oxigênio (O₂).  
  3. Ocorre principalmente nas folhas, nos cloroplastos.  

Quer um exemplo do dia a dia ou um exercício para fixar?"  

---  

**Aluno:** "Não entendi equações de segundo grau."  
**Tutor:**  
"Sem problemas! Vamos passo a passo:  
1. Uma equação de 2º grau tem a forma **ax² + bx + c = 0**.  
2. Para resolver, usamos a **Fórmula de Bhaskara**:  
   \[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]  
3. **Exemplo prático**:  
   - Equação: x² - 5x + 6 = 0  
   - Cálculo: a=1, b=-5, c=6 → Δ = (-5)² - 4*1*6 = **1**  
   - Soluções: x = (5 ± 1)/2 → x'=3 e x''=2.  

Quer tentar resolver outra comigo?"  

---  

**Aluno:** "Me dê um exercício de História."  
**Tutor:**  
"Claro! Sobre qual período? Por exemplo:  
1. **Brasil Colonial**: "Por que a cana-de-açúcar foi importante no século XVI?"  
2. **Idade Média**: "Como funcionava o feudalismo?"  
3. **Atualidades**: "Quais foram as causas da Primeira Guerra Mundial?"  

Escolha um tema e eu elaboro a pergunta com opções de resposta!  
"""

def chatbot(query):
    # Função que envia uma consulta para o modelo de linguagem da OpenAI e retorna a resposta.
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": content},
            {"role": "user", "content": query}
        ]
    )
    return response.choices[0].message.content

# Função principal para executar o Streamlit
def main():
    # Inicializa o histórico de mensagens
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    messages = st.session_state.messages

    # Título da app
    st.header("🧑‍🏫Tutor de Aprendizado Personalizado📖")

    # Renderiza o histórico de mensagens
    for msg in messages:
        chat = st.chat_message(msg["role"])
        chat.markdown(msg["content"])
    
    # Entrada de texto para o usuário
    message = st.chat_input("Digite sua pergunta ou solicitação...")
    if message:
        # Adiciona a mensagem do usuário ao histórico
        new_message = {"role": "user", "content": message}
        messages.append(new_message)

        # Exibe a mensagem do usuário
        chat = st.chat_message("user")
        chat.markdown(message)

        # Obtém a resposta do chatbot
        response = chatbot(message)
        
        # Adiciona a resposta do chatbot ao histórico
        message_response = {"role": "assistant", "content": response}
        messages.append(message_response)

        # Exibe a resposta do chatbot
        chat = st.chat_message("assistant")
        chat.markdown(response)

        # Atualiza o estado da sessão
        st.session_state.messages = messages

# Executa a função principal
if __name__ == "__main__":
    main()