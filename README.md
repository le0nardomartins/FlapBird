# 🐦 Flappy Bird - Guia Completo

Bem-vindo ao Flappy Bird! Este é um jogo clássico onde você controla um pássaro que precisa voar entre canos sem colidir. Este guia vai te ensinar tudo que você precisa para jogar!

## 📋 Índice

1. [Como Baixar o Python](#como-baixar-o-python)
2. [Como Instalar as Bibliotecas](#como-instalar-as-bibliotecas)
3. [Como Rodar o Jogo](#como-rodar-o-jogo)
4. [Como Jogar](#como-jogar)
5. [Estrutura do Projeto](#estrutura-do-projeto)
6. [Conceitos de Programação](#conceitos-de-programação)

---

## 🐍 Como Baixar o Python

### Passo 1: Acesse o site oficial
1. Abra seu navegador e acesse: **https://www.python.org/downloads/**
2. Clique no botão grande amarelo que diz **"Download Python"** (a versão mais recente)

### Passo 2: Instale o Python
1. Abra o arquivo que você baixou (geralmente aparece na pasta "Downloads")
2. **IMPORTANTE**: Marque a opção **"Add Python to PATH"** antes de clicar em "Install Now"
3. Clique em "Install Now" e aguarde a instalação terminar
4. Quando aparecer "Setup was successful", clique em "Close"

### Passo 3: Verifique se funcionou
1. Abra o **Prompt de Comando** (no Windows, pressione `Windows + R`, digite `cmd` e pressione Enter)
2. Digite: `python --version`
3. Se aparecer algo como "Python 3.x.x", está tudo certo! ✅

---

## 📦 Como Instalar as Bibliotecas

Este jogo precisa de uma biblioteca chamada **pygame** para funcionar. Vamos instalá-la!

### Passo 1: Abra o Prompt de Comando
- Pressione `Windows + R`
- Digite `cmd` e pressione Enter

### Passo 2: Navegue até a pasta do projeto
Digite o comando abaixo (substitua pelo caminho da sua pasta):

```bash
cd C:\Users\pc\Desktop\projeto-aula-teste
```

**Dica**: Se a pasta estiver em outro lugar, arraste a pasta para o Prompt de Comando e ele vai mostrar o caminho completo!

### Passo 3: Instale o pygame
Digite o comando abaixo e pressione Enter:

```bash
pip install pygame
```

Aguarde até aparecer "Successfully installed pygame". Pronto! ✅

**Alternativa**: Note que existe um arquivo chamado`requirements.txt`, você pode instalar tudo de uma vez com:

```bash
pip install -r requirements.txt
```

---

## 🎮 Como Rodar o Jogo

Agora que tudo está instalado, vamos jogar!

### Passo 1: Abra o Prompt de Comando na pasta do projeto
(Siga os passos 1 e 2 da seção anterior)

### Passo 2: Execute o jogo
Digite o comando abaixo e pressione Enter:

```bash
python main.py
```

### Passo 3: Divirta-se! 🎉
Uma janela vai abrir com o jogo. Use **ESPAÇO** ou **clique com o mouse** para fazer o pássaro voar!

---

## 🎯 Como Jogar

- **ESPAÇO** ou **Clique do Mouse**: Faz o pássaro voar para cima
- **Objetivo**: Passe pelos canos sem colidir
- **Pontuação**: Você ganha 1 ponto cada vez que passa por um cano
- **Game Over**: Se você bater nos canos ou no chão, o jogo acaba
- **Reiniciar**: Quando o jogo acabar, pressione **ESPAÇO** para jogar novamente

---

## 📁 Estrutura do Projeto

### 📸 Pasta `assets/`
Esta pasta contém todas as **imagens** usadas no jogo:
- **`1.png`** e **`2.png`**: São os sprites (imagens) do pássaro em diferentes posições. O jogo alterna entre essas duas imagens para criar a animação de voo do pássaro
- **`cloud.png`**: É a imagem das nuvens que aparecem no fundo do jogo

**Importante**: Não delete ou mova essas imagens! O jogo precisa delas para funcionar.

### 📄 Arquivos do Código

#### `main.py` - O Cérebro do Jogo
Este é o arquivo **principal** do jogo. Ele:
- Cria a janela do jogo
- Controla o loop principal (atualizar e desenhar tudo)
- Gerencia os eventos (teclado e mouse)
- Coordena todos os outros módulos
- Mostra a pontuação e mensagens na tela

#### `player.py` - O Pássaro
Este arquivo contém a classe `Bird` que representa o jogador:
- Carrega as imagens do pássaro (`1.png` e `2.png`)
- Controla a animação (alterna entre as duas imagens)
- Gerencia o movimento e a rotação do pássaro
- Detecta colisões com o chão

#### `pipe.py` - Os Obstáculos
Este arquivo contém a classe `Pipe` que representa os canos:
- Cria canos com tamanhos aleatórios
- Move os canos pela tela
- Desenha os canos verdes
- Detecta quando o pássaro colide com os canos
- Verifica quando o pássaro passa por um cano (para contar pontos)

#### `gravity.py` - A Física
Este arquivo controla a **física** do jogo:
- Aplica a gravidade (faz o pássaro cair)
- Limita o movimento no topo da tela
- Calcula o ângulo de rotação do pássaro (quando cai, ele inclina para baixo)

#### `game_state.py` - O Estado do Jogo
Este arquivo gerencia os **estados** do jogo:
- Verifica colisões entre pássaro e canos
- Verifica colisões com o chão e o topo
- Conta a pontuação
- Controla o início e reinício do jogo

#### `cloud.py` - As Nuvens
Este arquivo cria e gerencia as nuvens decorativas:
- Cria nuvens em posições aleatórias
- Move as nuvens mais devagar que os canos (efeito de profundidade)
- Remove nuvens que saem da tela

#### `config.py` - As Configurações
Este arquivo contém todas as **configurações** do jogo:
- Tamanho da tela (largura e altura)
- Cores (azul do céu, verde dos canos, etc.)
- Velocidade da gravidade
- Força do pulo
- Velocidade dos canos
- Tamanhos e espaçamentos

#### `requirements.txt` - As Dependências
Este arquivo lista todas as bibliotecas que o projeto precisa:
- `pygame`: A biblioteca principal para criar jogos em Python

---

## 🧠 Conceitos de Programação

### 🏗️ Programação Orientada a Objetos (POO)

**O que é POO?**
POO é uma forma de organizar o código criando "objetos" que representam coisas do mundo real. Cada objeto tem suas próprias características (propriedades) e ações (métodos).

**Exemplo no nosso jogo:**
- **Classe `Bird`**: É como um "molde" para criar pássaros. Cada pássaro tem:
  - **Propriedades**: posição (x, y), velocidade, ângulo de rotação
  - **Métodos**: `jump()` (pular), `update()` (atualizar posição), `draw()` (desenhar na tela)

- **Classe `Pipe`**: É o molde para criar canos. Cada cano tem:
  - **Propriedades**: posição, largura, tamanho do buraco
  - **Métodos**: `update()` (mover), `draw()` (desenhar), `check_collision()` (verificar colisão)

**Por que usar POO?**
- Organiza o código de forma clara
- Facilita criar vários objetos do mesmo tipo (vários canos, várias nuvens)
- Cada objeto é independente e pode ter seu próprio comportamento

### 💥 Algoritmos de Detecção de Colisão

**O que é detecção de colisão?**
É verificar se dois objetos estão se tocando na tela. No nosso jogo, precisamos saber quando o pássaro bate nos canos ou no chão.

**Como funciona no nosso jogo:**

1. **Colisão com Canos** (em `pipe.py`):
   - O pássaro é representado por um **círculo invisível**
   - Verificamos se esse círculo está dentro da área dos canos
   - Se o pássaro está entre o cano de cima e o de baixo, não há colisão
   - Se o pássaro toca em qualquer parte do cano, há colisão!

2. **Colisão com Chão/Topo** (em `player.py` e `game_state.py`):
   - Verificamos se a posição Y do pássaro ultrapassou o topo ou o chão da tela
   - Se sim, o jogo acaba

**Por que é importante?**
Sem detecção de colisão, o pássaro poderia passar através dos canos, e o jogo não teria desafio!

### ⚙️ Física Aplicada

**O que é física aplicada?**
É usar conceitos de física real (como gravidade) para tornar o jogo mais realista e divertido.

**Conceitos usados no nosso jogo:**

1. **Gravidade** (em `gravity.py`):
   - A cada frame (60 vezes por segundo), a velocidade do pássaro aumenta
   - Isso faz o pássaro cair cada vez mais rápido, como na vida real
   - Quando você pressiona ESPAÇO, aplicamos uma força para cima (pulo)

2. **Velocidade e Aceleração**:
   - **Velocidade**: Quão rápido o pássaro está se movendo
   - **Aceleração**: A gravidade aumenta a velocidade constantemente
   - Quando você pula, a velocidade fica negativa (vai para cima), mas a gravidade logo começa a puxar para baixo novamente

3. **Rotação** (em `gravity.py`):
   - O pássaro rotaciona baseado na velocidade
   - Se está caindo rápido, inclina para baixo
   - Se está subindo, inclina para cima
   - Isso dá uma sensação mais natural ao movimento

**Por que usar física?**
- Torna o jogo mais desafiador e divertido
- Cria uma sensação de controle mais realista
- O jogador precisa aprender a "sentir" a física para jogar bem

---

## ❓ Problemas Comuns

### "python não é reconhecido como comando"
- Você não marcou "Add Python to PATH" durante a instalação
- Reinstale o Python e marque essa opção

### "ModuleNotFoundError: No module named 'pygame'"
- Você não instalou o pygame
- Execute: `pip install pygame`

### "FileNotFoundError: [Errno 2] No such file or directory: 'assets/1.png'"
- Certifique-se de que a pasta `assets` está na mesma pasta que `main.py`
- Não mova ou delete as imagens da pasta `assets`

### O jogo não abre ou fecha imediatamente
- Verifique se todas as imagens estão na pasta `assets`
- Certifique-se de que o pygame está instalado corretamente

