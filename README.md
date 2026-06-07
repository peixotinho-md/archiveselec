#  Seletor de Sentidos — IA Multimodal

> Sistema de roteamento automático de arquivos baseado em lógica determinística.  
> Trabalho da disciplina de **Lógica Aplicada** — UCDB, 2026.

---

## Sobre o projeto

O **Seletor de Sentidos** recebe o caminho de qualquer arquivo e identifica automaticamente qual módulo de IA seria responsável por processá-lo, com base na extensão do arquivo. O sistema exibe um relatório com os metadados do arquivo e as funções disponíveis para aquele tipo.

A lógica central utiliza a estrutura `match-case` do Python 3.10+ (equivalente ao ESCOLHA-CASO), garantindo comportamento **determinístico**, **auditável** e **previsível** para qualquer entrada.

---

## Como funciona

```
Usuário informa o caminho do arquivo
        ↓
Sistema valida a existência do arquivo
        ↓
Extrai nome, extensão, tamanho e data
        ↓
Estrutura match-case roteia para o módulo correto
        ↓
Exibe relatório com módulo e funções disponíveis
```

---

## Módulos disponíveis

| Extensões | Módulo Ativado |
|-----------|---------------|
| `.jpg` `.jpeg` `.png` `.gif` `.bmp` `.webp` | Visão Computacional |
| `.mp4` `.avi` `.mov` `.mkv` `.webm` | Análise de Vídeo |
| `.mp3` `.wav` `.flac` `.aac` `.ogg` | Processamento de Áudio |
| `.txt` | Processamento de Linguagem Natural |
| `.pdf` `.docx` `.doc` `.odt` | Análise Documental |
| `.xlsx` `.xls` `.csv` | Análise de Dados |
| `.ppt` `.pptx` | Análise de Apresentações |
| `.py` `.java` `.c` `.cpp` `.js` `.html` `.css` | Análise de Código |
| `.zip` `.rar` `.7z` | Arquivo Compactado |
| qualquer outro | Formato Não Suportado |

> **Destaque:** arquivos `.txt` passam por leitura real do conteúdo — o sistema contabiliza palavras e caracteres em tempo de execução.

---

## Exemplo de saída

```
============================================================
SELETOR DE SENTIDOS - IA MULTIMODAL
============================================================

Digite o caminho completo do arquivo: relatorio.txt

============================================================
RELATÓRIO DE ANÁLISE
============================================================
Arquivo: relatorio.txt
Extensão: .txt
Tamanho: 2048 bytes
Data: 2026-06-07 14:32:10

MÓDULO SELECIONADO
------------------------------------------------------------
PROCESSAMENTO DE LINGUAGEM NATURAL
------------------------------------------------------------
• Leitura textual concluída
• Palavras encontradas: 312
• Caracteres encontrados: 2048
• Análise semântica disponível

PROCESSAMENTO CONCLUÍDO
```

---

## Como executar

### Pré-requisitos

- Python **3.10 ou superior** (necessário para `match-case`)

### Execução

```bash
python main.py
```

Ao executar, o sistema solicitará o caminho completo do arquivo:

```
Digite o caminho completo do arquivo: C:\Users\usuario\Downloads\foto.jpg
```

---

## Estrutura do projeto

```
seletor-de-sentidos/
│
├── main.py          # Código principal
└── README.md        # Este arquivo
```

---

## Decisões de projeto

**Por que `match-case` em vez de `if-elif`?**  
A estrutura `match-case` torna o mapeamento extensão → módulo mais legível e fácil de expandir. Adicionar um novo formato exige apenas um novo `case`, sem alterar o restante do código.

**Por que extensão e não conteúdo do arquivo?**  
A abordagem por extensão garante complexidade O(1) e comportamento totalmente previsível. Como limitação, arquivos com extensões incorretas podem ser mal roteados — uma melhoria futura seria a leitura dos *magic bytes* do arquivo para identificação real do tipo.

**Por que `.txt` tem tratamento especial?**  
Diferentemente dos formatos binários (`.pdf`, `.docx`), arquivos de texto puro podem ser lidos diretamente pelo Python sem bibliotecas externas, permitindo análise imediata de palavras e caracteres.


## Autores

| Nome | RA |
|------|----|
| Arthur Burali | 205573 |
| Vinicius Eduardo | 206319 |
| Gabriel Wommer | 206252 |
| Renato Peixoto | 205683 |

**Universidade Católica Dom Bosco (UCDB)** — Campo Grande, MS  
Disciplina: Lógica Aplicada · Junho de 2026

---

## Licença

Este projeto foi desenvolvido para fins acadêmicos.
