# Desafio Indicium Tech Code Challenge - Engenharia de Dados

O desafio consistiu em criar uma pipeline de dados para extrair e carregar dados de duas fontes: um banco de dados PostgreSQL e um arquivo CSV, utilizando ferramentas como **Meltano**, **Airflow** e **PostgreSQL** e envia´-los para o sistema local.
Então, os dados deveriam ser transportados para um único banco de dados do postgres.

## Ferramentas que deveriam ser Utilizadas

- **Airflow**: Para agendar e orquestrar as tarefas da pipeline.
- **Meltano**: Usado para a extração e carregamento de dados (ETL).
- **PostgreSQL**: Banco de dados para armazenar os dados extraídos.



A solução segue a arquitetura descrita no diagrama a seguir:

![Diagrama Embulk Meltano](https://github.com/DeniseMelo/code-challenge/blob/main/docs/diagrama_embulk_meltano.jpg)

## Iniciando o Projeto com Docker

### 1. Clone o Repositório

Clone o repositório do projeto em sua máquina local com o seguinte comando:

```bash
git clone https://github.com/techindicium/code-challenge.git
```
### 2. Crie o banco de dados com o docker Compose
```bash
docker-compose up -d
```

## Arquitetura

- **Meltano**: Antes de instalar o Meltano, é recomendado criar um ambiente virtual
```bash
  python -m venv venv
```
- Ative o ambiente e instale o Meltano
```bash
  source venv/bin/activate
  pip install meltano
```

## Como o projeto foi estruturado
![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2011-51-36.png)
### Extraçao e carregamento para o sistema local
1. **Projeto Indicium-postgres : Extração dos dados do banco postgres com o tap-csv e load com target-csv para o sistema local no formato csv**  
   
2. **Projeto Indicium-csv : Estração dos dados do arquivo em csv com tap-csv  e load com target-csv para o sistema local no formato csv**

3. **Requisito do desafio consistia em  organizar os dados localmente em data/nome da pasta/data do dia/ nome do arquivo.csv**  
   ![terminal](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2011-55-37.png)
   ***
   ![terminal](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2011-56-41.png)
### Extração dos dados locais e envio para o banco de dados do postgres localizado em outro container
1. **Projeto Indicium-csv1-to-postgres : Extração com o tap-csv e e load para o bancode dados do postgres com o target-postgres**
2. **Projeto Indiciun-csv2-to-postgres : Extraçao com o tap-csv e o load para o banco de dados do postgres com o target-postgres**

### Busca pela data do dia e Path dinâmino

1. **Com as Pipelines com python foi possivel enviar dinâmicamente o filepath absoluto para o meltano.yml. A imagem mostra que o script do python percorre as pastas com a data do dia e envia o filepath para o meltano.yml ao mesmo tempo também aciona o run**
   ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2003-59-55.png)
  
 ### Automação com Airflow   
  
- **Airflow**: **Com o airflow pude configurar que as pipelines do python fossem acionadas diariamente, cada dag corresponde a uma pipeline do python para assim, atuar de forma independente**
![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2008-53-16.png)
***
 ### O banco de dados final
- **O banco de dados final onde reunia todos os arquivos csv e os transformava em tabelas  foi o postgres rodando em um container docker**
1. **Todas as tabelas reunidas no banco de dados**
   ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2009-00-38.png)
2. **Query para buscar a junção de dados da tabela orders com a orders_details**
 ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2009-09-22.png)
3. **Resultado!!!!**
   ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-07%2009-08-53.png)

 ### Desafios!
 1. Instalaçao do Meltano e a sua limitação na filepath
### Melhorias no Projeto
1. **Meu próximo desafio é voltar a usar parquet, pois ao fianl do projeto quando já estava enviando dados para o postgres, ocorreu um erro com o tap-parquet**
   ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-05%2010-05-57.png)
   ***
2. **O erro ,aparentemente, uma incompatibilidade de versão com o Numpy. Uma nova versão foi reinstalada para que fosse compatível, mesmo assim o erro persistia!**
   ![](https://github.com/DeniseMelo/Indicium_challenge/blob/main/images/Screenshot%20from%202025-02-05%2010-05-17.png)
