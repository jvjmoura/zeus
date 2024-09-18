import streamlit as st
from pathlib import Path
import whisper
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import logging
import traceback

# Configuração de página do Streamlit
st.set_page_config(page_title="Zeus Whisper", layout="wide")

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

PASTA_TEMP = Path(__file__).parent / 'temp'
PASTA_TEMP.mkdir(exist_ok=True)
ARQUIVO_AUDIO_TEMP = PASTA_TEMP / 'audio.mp3'
ARQUIVO_VIDEO_TEMP = PASTA_TEMP / 'video.mp4'

@st.cache_resource
def load_whisper_model():
    try:
        logger.info("Tentando carregar o modelo Whisper...")
        model = whisper.load_model("medium")
        logger.info("Modelo Whisper carregado com sucesso.")
        return model
    except Exception as e:
        logger.error(f"Erro ao carregar o modelo Whisper: {e}")
        logger.error(f"Traceback completo: {traceback.format_exc()}")
        st.error(f"Não foi possível carregar o modelo de transcrição. Erro: {e}")
        return None

def transcreve_audio(model, caminho_audio):
    try:
        result = model.transcribe(str(caminho_audio), language="pt")
        return result["text"]
    except Exception as e:
        logger.error(f"Erro na transcrição: {e}")
        return "Erro na transcrição do áudio."

def exibe_resultado(transcricao):
    st.subheader("Transcrição Original")
    st.write(transcricao)

def _salva_audio_do_video(video_bytes):
    with open(ARQUIVO_VIDEO_TEMP, mode='wb') as video_f:
        video_f.write(video_bytes.read())
    moviepy_video = VideoFileClip(str(ARQUIVO_VIDEO_TEMP))
    moviepy_video.audio.write_audiofile(str(ARQUIVO_AUDIO_TEMP))

def _salva_audio(arquivo_audio, formato):
    with open(ARQUIVO_AUDIO_TEMP, "wb") as f:
        f.write(arquivo_audio.getvalue())
    if formato == 'm4a':
        audio = AudioFileClip(str(ARQUIVO_AUDIO_TEMP))
        audio.write_audiofile(str(ARQUIVO_AUDIO_TEMP), codec='mp3')
        audio.close()

def transcreve_tab_video(model):
    arquivo_video = st.file_uploader('Adicione um arquivo de vídeo .mp4', type=['mp4'])
    if arquivo_video is not None:
        with st.spinner("Processando o vídeo..."):
            _salva_audio_do_video(arquivo_video)
            transcricao = transcreve_audio(model, ARQUIVO_AUDIO_TEMP)
        exibe_resultado(transcricao)

def transcreve_tab_audio(model):
    arquivo_audio = st.file_uploader('Adicione um arquivo de áudio .mp3 ou .m4a', type=['mp3', 'm4a'])
    if arquivo_audio is not None:
        with st.spinner("Transcrevendo o áudio..."):
            formato = arquivo_audio.name.split('.')[-1].lower()
            _salva_audio(arquivo_audio, formato)
            transcricao = transcreve_audio(model, ARQUIVO_AUDIO_TEMP)
        exibe_resultado(transcricao)

def sidebar_info():
    # Logotipo
    logo_url = "https://cdn.midjourney.com/143dff27-3598-4ca6-becb-e6387047a007/0_1.png"
    st.sidebar.image(logo_url, use_column_width=True, caption="Zeus Whisper")

    st.sidebar.title("Como usar o Zeus Whisper")
    st.sidebar.markdown("""
    1. Escolha entre as opções 'Vídeo' ou 'Áudio'.
    2. Faça upload do seu arquivo de vídeo (.mp4) ou áudio (.mp3, .m4a).
    3. Aguarde o processamento e a transcrição.
    4. Revise a transcrição gerada.
    """)
    
    st.sidebar.info("Lembre-se: A qualidade da transcrição depende da clareza do áudio original.")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Informações sobre o Projeto")
    st.sidebar.markdown("**Status:** Em construção")
    st.sidebar.markdown("**Desenvolvedor:** João Valério")
    st.sidebar.markdown("**Cargo:** Juiz do TJPA")
    st.sidebar.markdown("Esta programação Python está atualmente em desenvolvimento.")

def main():
    try:
        sidebar_info()
        
        st.title('Zeus Whisper 🎙️')
        st.markdown('#### Transcreva áudio de vídeos e arquivos de áudio')
        
        model = load_whisper_model()
        
        if model is None:
            st.error("O modelo de transcrição não pôde ser carregado. Verifique os logs para mais detalhes.")
        else:
            tab_video, tab_audio = st.tabs(['Vídeo', 'Áudio'])
            
            with tab_video:
                st.header("Transcrição de Vídeo")
                transcreve_tab_video(model)
            
            with tab_audio:
                st.header("Transcrição de Áudio")
                transcreve_tab_audio(model)
    except Exception as e:
        logger.error(f"Erro não tratado na função main: {e}")
        logger.error(f"Traceback completo: {traceback.format_exc()}")
        st.error(f"Ocorreu um erro inesperado: {e}")

if __name__ == '__main__':
    main()