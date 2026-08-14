# Organizador de Arquivos

Automação desenvolvida em Python para monitorar uma pasta de entrada e
organizar automaticamente arquivos PDF, movendo-os para uma pasta de
arquivos processados do dia.

## Objetivo

O objetivo deste projeto é praticar conceitos de automação com Python
por meio de um cenário comum em ambientes corporativos: o monitoramento
contínuo de um diretório e o processamento automático de arquivos.

Sempre que um novo arquivo com extensão `.pdf` for identificado na pasta
monitorada, ele será movido para uma pasta de destino correspondente à
data atual, mantendo os documentos organizados por dia de processamento.

Embora a primeira versão seja focada em arquivos PDF, a arquitetura do
projeto foi pensada para facilitar a adição de novos tipos de arquivos e
novas regras de processamento.

## Funcionalidades

-   Monitoramento contínuo de uma pasta.
-   Identificação automática de novos arquivos PDF.
-   Movimentação dos arquivos para uma pasta de processamento.
-   Organização dos arquivos por data.
-   Criação automática das pastas de destino.
-   Registro das operações em logs.
-   Tratamento de erros durante o processamento.

## Estrutura do Projeto

``` text
organizador-arquivos/
│
├── src/
├── config/
├── data/
│   ├── input/
│   └── processed/
├── logs/
├── tests/
├── requirements.txt
├── README.md
├── .gitignore
└── main.py
```

## Fluxo da Automação

1.  A aplicação inicia o monitoramento da pasta de entrada.
2.  Um novo arquivo PDF é detectado.
3.  O arquivo é validado.
4.  A pasta correspondente à data atual é criada, caso ainda não exista.
5.  O arquivo é movido para a pasta de processamento.
6.  A operação é registrada em log.
7.  O monitoramento continua aguardando novos arquivos.

## Tecnologias

-   Python
-   Ambiente virtual (`venv`)
-   Git
-   Logging
-   Manipulação de arquivos e diretórios

## Próximas Evoluções

-   Suporte a outros tipos de arquivos.
-   Configuração por arquivo `.env`.
-   Evitar processamento duplicado.
-   Geração de relatórios.
-   Notificações por e-mail.

## Objetivos de Aprendizado

Este projeto foi criado para consolidar conhecimentos em:

-   Organização de projetos Python.
-   Boas práticas de desenvolvimento.
-   Manipulação de arquivos e diretórios.
-   Modularização.
-   Tratamento de exceções.
-   Registro de logs.
-   Versionamento com Git.

## Licença

Este projeto foi desenvolvido para fins de estudo e construção de
portfólio.
