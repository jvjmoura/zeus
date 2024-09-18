# Zeus Whisper 🎙️

Zeus Whisper é uma aplicação web baseada em Streamlit que transcreve áudio de arquivos de vídeo e áudio usando o modelo Whisper da OpenAI. Foi projetado para ser uma ferramenta fácil de usar para converter palavras faladas em arquivos de vídeo e áudio em texto.

## Funcionalidades

- Transcreve áudio de arquivos de vídeo (.mp4)
- Transcreve arquivos de áudio (.mp3, .m4a)
- Interface amigável construída com Streamlit
- Suporta transcrição em português
- Exibe a transcrição original

## Uso

1. Execute a aplicação Streamlit:
   ```
   streamlit run app.py
   ```

2. Abra seu navegador web e vá para a URL exibida no terminal (geralmente `http://localhost:8501`).

3. Escolha entre as abas 'Vídeo' ou 'Áudio'.

4. Faça o upload do seu arquivo de vídeo (.mp4) ou áudio (.mp3, .m4a).

5. Aguarde a conclusão do processo de transcrição.

6. Revise a transcrição gerada.

## Status do Projeto

Este projeto está atualmente em desenvolvimento. Atualizações futuras podem incluir recursos e melhorias adicionais.

## Informações do Desenvolvedor

- **Desenvolvedor:** João Valério
- **Cargo:** Juiz do TJPA (Tribunal de Justiça do Pará)

## Observações

- A qualidade da transcrição depende da clareza do áudio original.
- Certifique-se de ter espaço em disco e memória suficientes para processar arquivos de vídeo grandes.

## Agradecimentos

- Este projeto usa o modelo Whisper da OpenAI para reconhecimento de fala.
- Construído com Streamlit, MoviePy e outras bibliotecas de código aberto.