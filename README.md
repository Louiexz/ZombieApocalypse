# ZombieApocalypse

![ApocalipseZumbi](ApocalipseZumbi.png)

Este é um jogo arcade simples construído com Pygame.

## Funcionalidades

    Objetivo do jogo: Destrua os zumbis antes que eles te devorem.
    Variados inimigos: Cada um dos inimigos tem suas características.
    Nivelação: A cada 20 e 100 pontos, o jogo fica mais dinâmico.
    Multiplataforma, escolha onde jogar: Windows, Linux e APK.

## Pré-requisitos

### Certifique-se de ter o seguinte instalado antes de começar:
  
     Python 3
     Pygame

## Instalação e Uso

1. Baixe de acordo com sua plataforma:

    - Windows x64: 
    - Linux x86_64: 
    - Apk: Em breve.

2. Ou siga os seguintes passos:

- Clone o repositório:

        git clone https://github.com/Louiexz/ZombieApocalypse.git
        cd ZombieApocalypse
 
 - Instale as dependências:

        pip install -r requirements.txt

 - Execute o aplicativo:

        python run.py

## Instruções do jogo:

![Instruções](instrucoes.png)

## Estrutura do Projeto

    ZombieApocalypse/
    │
    ├── run.py             # Arquivo principal do aplicativo
    ├── assets/            # Diretório contendo arquivos necessários
    │   ├── imagens/           # Diretório contendo as imagens utilizadas
    │   |   ├── player/            # Imagens do jogador
    │   |   └── enemies/           # Imagens dos inimigos
    |   │       ├── idle/               # Imagens dos inimigos
    │   |       └── attack/             # Imagens dos inimigos atacando
    |   ├── scripts/           # Diretório contendo pastas de funções e/ou classes
    │   |   ├── game/              # Funções do jogo, loops e classe de botão
    │   |   |   ├── game_functs.py      # Funções de texto, sons e chamadas para funções
    │   |   |   ├── game_loop.py        # Funções de loop (Principal e Game Over)
    │   |   |   ├── screen_controls.py  # Funções de controle da tela
    │   |   |   ├── bullet.py           # Classe das balas
    │   |   |   ├── drop.py             # Classe dos drops
    │   |   |   └── button.py           # Classe dos botões
    │   |   ├── main/              # Inicialização e configurações
    │   |   |   ├── start.py            # Inicialização de classes, configurações e loop
    │   |   |   └── settings.py         # Configurações gerais
    │   |   └── characters/        # Funções e classe do jogador
    │   |       ├── player.py           # Classe do jogador
    │   |       ├── zombie.py           # Classe de alien
    │   |       └── functs/
    │   |           ├── input_controls.py   # Funções de entrada 
    │   |           └── zombie_functs.py    # Funções dos inimigos
    |   └── sound/              # Diretório contendo sons do jogo
    |       ├── game               # Sons de fim e pontos
    |       ├── zombie             # Sons referentes a zumbis
    |       └── player             # Sons referentes ao jogador
    └── requirements.txt    # Arquivo contendo as dependências do Python

## Contribuições
Louiexz - Autor e Desenvolvedor do jogo<br>

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.