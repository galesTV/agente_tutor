# 🧑‍🏫 Chatbot Tutor de Aprendizado Personalizado 📖

![OpenAI](https://img.shields.io/badge/openai-1.98.0-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.47.1-%23FF5D5D)
![python-dotenv](https://img.shields.io/badge/pythondotenv-1.1.1-ffd242)

Um chatbot inteligente desenvolvido como tutor de aprendizado personalizado, especializado em matérias escolares, utilizando a API da OpenAI. Este projeto foi criado em Python e oferece uma experiência interativa para auxiliar estudantes em seu processo de aprendizagem.

## 🛠️ Tecnologias Utilizadas
- Python
- OpenAI API
- Streamlit (para interface web)
- Python-Dotenv (para gerenciamento de variáveis de ambiente)

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado
- Conta na OpenAI para obter uma API key
- Gerenciador de pacotes PIP

### Instalação
1. Clone o repositório
   ```bash
   git clone https://github.com/galesTV/agente_tutor.git
   ```
   
2. Crie um ambiente virtual (opcional, mas recomendado)
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

3. Instale as dependências
    ```bash
    pip install openai streamlit python-dotenv
    ```

4. Obtenha sua OpenAI API key
    - Acesse https://platform.openai.com/settings/organization/api-keys
    - Faça login ou crie uma conta
    - Clique em "Create new secret key"
    - Copie a chave gerada

5. Configure o ambiente
    - Crie um arquivo .env na raiz do projeto
    - Adicione sua API key da OpenAI da seguinte forma:
      ```text
      openai_key=sua_chave_aqui
      ```

6. Execute a aplicação
    ```bash
    streamlit run main.py
    ```
## 🤖 Como Utilizar o Chatbot Tutor
1. Na interface do Streamlit, você verá um campo para digitar suas perguntas
2. Digite sua dúvida sobre qualquer matéria escolar
3. O tutor irá responder de forma personalizada e didática
4. Você pode refinar as perguntas ou pedir explicações adicionais
5. O chatbot mantém o contexto da conversa para um aprendizado contínuo

## 🌟 Recursos
1. Respostas personalizadas para dúvidas escolares
2. Explicações didáticas e adaptáveis ao nível do aluno
3. Suporte para diversas matérias (matemática, ciências, história, etc.)
4. Interface simples e intuitiva

## 📝 Notas Importantes
1. Mantenha sua API key segura e não a compartilhe
2. O uso da API da OpenAI pode gerar custos dependendo do volume de uso
3. Para dúvidas ou problemas, consulte a documentação da OpenAI ou abra uma issue no repositório
