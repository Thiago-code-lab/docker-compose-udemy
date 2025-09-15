# Aplicação Flask com Docker Compose

Este é um projeto de estudo que demonstra a utilização do Docker Compose para orquestrar uma aplicação Flask com Redis como banco de dados em memória.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte dos meus estudos pessoais sobre Docker e Docker Compose. O objetivo é criar uma aplicação web simples que conta o número de acessos à página principal, armazenando essa contagem em um banco de dados Redis.

## 🚀 Tecnologias Utilizadas

- **Flask**: Framework web em Python
- **Redis**: Banco de dados em memória
- **Docker**: Plataforma de contêineres
- **Docker Compose**: Ferramenta para orquestração de múltiplos contêineres

## 🛠️ Estrutura do Projeto

```
.
├── Dockerfile          # Configuração da imagem Docker da aplicação
├── docker-compose.yml  # Definição dos serviços e suas configurações
├── app.py             # Código-fonte da aplicação Flask
└── requirements.txt    # Dependências do Python
```

## 🚀 Como Executar o Projeto

1. Certifique-se de ter o Docker e Docker Compose instalados em sua máquina.

2. Clone este repositório:
   ```bash
   git clone <url-do-repositorio>
   cd "Projeto 5 - Docker Udemy"
   ```

3. Execute o comando para iniciar os contêineres:
   ```bash
   docker-compose up --build
   ```

4. Acesse a aplicação no navegador:
   ```
   http://localhost:5000
   ```

5. Para parar a aplicação, pressione `Ctrl+C` no terminal e execute:
   ```bash
   docker-compose down
   ```

## 🔄 Funcionamento

- A aplicação conta quantas vezes a página principal foi acessada.
- O contador é armazenado no Redis, garantindo que a contagem seja mantida mesmo que o contêiner da aplicação seja reiniciado.
- A cada acesso à página, o contador é incrementado e exibido na tela.

## 📝 Notas de Estudo

Este projeto foi desenvolvido como parte do meu aprendizado sobre:
- Criação e configuração de imagens Docker
- Orquestração de múltiplos contêineres com Docker Compose
- Comunicação entre contêineres em uma rede Docker
- Utilização de variáveis de ambiente para configuração

## 📄 Licença

Este projeto foi criado apenas para fins educacionais.
