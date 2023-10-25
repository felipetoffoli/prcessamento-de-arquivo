# Como Executar o Docker Compose

Este guia descreve como executar o seu arquivo `docker-compose.yml` para iniciar o serviço `process-file` que processa um arquivo usando um contêiner Docker.

## Pré-Requisitos

Certifique-se de que você tenha instalado o Docker e o Docker Compose no seu sistema. Se você ainda não os instalou, siga as instruções na documentação oficial:

- [Instalação do Docker](https://docs.docker.com/get-docker/)
- [Instalação do Docker Compose](https://docs.docker.com/compose/install/)

## Passos para Executar

Siga estas etapas para executar o seu serviço usando o Docker Compose:

1. Abra um terminal ou prompt de comando no diretório onde está o seu arquivo `docker-compose.yml`.

2. Execute o seguinte comando para iniciar os contêineres definidos no arquivo `docker-compose.yml`:

   ```bash
   docker-compose up
