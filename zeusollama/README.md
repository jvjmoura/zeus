# Zeus Whisper

Zeus Whisper é uma aplicação Streamlit que permite transcrever e analisar áudio de vídeos e arquivos de áudio usando o modelo Whisper da OpenAI para transcrição e o Ollama com o modelo llama3.1:8b para análise de texto.

## Autor

João Valério de Moura Júnior
Juiz do Tribunal de Justiça do Estado do Pará (TJPA)

## Sobre o Projeto

Esta solução foi criada em Python, combinando tecnologias de ponta em processamento de linguagem natural para auxiliar na transcrição e análise de áudio e vídeo.

## Requisitos

- Python 3.8+
- FFmpeg
- Ollama

## Instalação

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

2. Instale o Ollama seguindo as instruções em [https://ollama.ai/](https://ollama.ai/).

3. Baixe o modelo llama3.1:8b para o Ollama:
   ```
   ollama pull llama3.1:8b
   ```

## Uso

Execute o aplicativo Streamlit:

```
streamlit run zeus_whisper.py
```

Abra seu navegador e acesse `http://localhost:8501`.

## Versão do Ollama

Este projeto foi testado com Ollama versão 0.3.9. Certifique-se de usar esta versão ou uma mais recente.

## Considerações sobre GPU

Se você tiver uma GPU disponível, considere usar modelos do Ollama com mais parâmetros para melhorar a qualidade da análise. Por exemplo:

- llama3.1:13b (13 bilhões de parâmetros)
- llama3.1:30b (30 bilhões de parâmetros)
- llama3.1:65b (65 bilhões de parâmetros)

Para usar um modelo diferente, modifique a linha no arquivo `zeus_whisper.py`:

```python
command = ['ollama', 'run', 'llama3.1:8b']
```

Substitua `llama3.1:8b` pelo modelo desejado.

Nota: Modelos maiores requerem mais memória GPU e podem ser mais lentos, mas geralmente oferecem resultados de melhor qualidade.

## Notas

- O modelo Whisper usado para transcrição está fixado na versão "medium". 
- Certifique-se de que o FFmpeg está instalado em seu sistema para o processamento de áudio e vídeo.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request para sugestões de melhorias ou correções.
