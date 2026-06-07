import os
import mimetypes
from datetime import datetime

print("=" * 60)
print("SELETOR DE SENTIDOS - IA MULTIMODAL")
print("=" * 60)

arquivo = input("\nDigite o caminho completo do arquivo: ").strip().replace('"', '')

if not os.path.exists(arquivo):
    print("\nERRO: Arquivo não encontrado.")
    exit()

nome = os.path.basename(arquivo)
extensao = os.path.splitext(nome)[1].lower()
tamanho = os.path.getsize(arquivo)

print("\n" + "=" * 60)
print("RELATÓRIO DE ANÁLISE")
print("=" * 60)

print(f"Arquivo: {nome}")
print(f"Extensão: {extensao}")
print(f"Tamanho: {tamanho} bytes")
print(f"Data: {datetime.now()}")

modulo = ""
descricao = ""

match extensao:

    # IMAGENS
    case ".jpg" | ".jpeg" | ".png" | ".gif" | ".bmp" | ".webp":
        modulo = "VISÃO COMPUTACIONAL"
        descricao = """
• Reconhecimento de objetos
• Detecção facial
• Classificação de imagens
• OCR (extração de texto)
"""

    # VÍDEOS
    case ".mp4" | ".avi" | ".mov" | ".mkv" | ".webm":
        modulo = "ANÁLISE DE VÍDEO"
        descricao = """
• Extração de quadros
• Detecção de movimento
• Reconhecimento de ações
• Rastreamento de objetos
"""

    # ÁUDIOS
    case ".mp3" | ".wav" | ".flac" | ".aac" | ".ogg":
        modulo = "PROCESSAMENTO DE ÁUDIO"
        descricao = """
• Reconhecimento de fala
• Transcrição automática
• Identificação de sons
• Conversão voz-texto
"""

    # TEXTOS
    case ".txt":
        modulo = "PROCESSAMENTO DE LINGUAGEM NATURAL"

        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                texto = f.read()

            palavras = len(texto.split())
            caracteres = len(texto)

            descricao = f"""
• Leitura textual concluída
• Palavras encontradas: {palavras}
• Caracteres encontrados: {caracteres}
• Análise semântica disponível
"""

        except:
            descricao = """
• Arquivo textual detectado
• Não foi possível ler o conteúdo
"""

    # DOCUMENTOS
    case ".pdf" | ".docx" | ".doc" | ".odt":
        modulo = "ANÁLISE DOCUMENTAL"

        descricao = """
• Extração de conteúdo
• Classificação documental
• Busca semântica
• Resumo automático
"""

    # PLANILHAS
    case ".xlsx" | ".xls" | ".csv":
        modulo = "ANÁLISE DE DADOS"

        descricao = """
• Leitura de tabelas
• Estatísticas descritivas
• Identificação de padrões
• Geração de relatórios
"""

    # APRESENTAÇÕES
    case ".ppt" | ".pptx":
        modulo = "ANÁLISE DE APRESENTAÇÕES"

        descricao = """
• Extração de slides
• Resumo de conteúdo
• Identificação de tópicos
"""

    # CÓDIGO
    case ".py" | ".java" | ".c" | ".cpp" | ".js" | ".html" | ".css":
        modulo = "ANÁLISE DE CÓDIGO"

        descricao = """
• Identificação da linguagem
• Análise sintática
• Busca de erros
• Sugestões de melhoria
"""

    # COMPACTADOS
    case ".zip" | ".rar" | ".7z":
        modulo = "ARQUIVO COMPACTADO"

        descricao = """
• Verificação de conteúdo
• Extração automática
• Classificação dos arquivos internos
"""

    case _:
        modulo = "FORMATO NÃO SUPORTADO"

        descricao = """
• Tipo de arquivo desconhecido
"""

print("\nMÓDULO SELECIONADO")
print("-" * 60)
print(modulo)

print("-" * 60)
print(descricao)

print("\nPROCESSAMENTO CONCLUÍDO")

#Seletor de sentidos, realizado para trabalho da matéria de Lógica Aplicada 07/06/2026
#Objetivo é o usuário colocar um arquivo e o código dar informações
# Alunos: Arthur Burali RA: 205573, Vinicius Eduardo RA: 206319, Gabriel Wommer RA: 206252 e Renato Peixoto RA: 205683