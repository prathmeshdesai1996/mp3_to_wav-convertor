import streamlit as st
import soundfile as sf
import base64

def convert_mp3_to_wav(file):
    # Load the MP3 file
    data, sr = sf.read(file)
    
    # Set the output filename to be the same as the input file but with a WAV extension
    out_filename = file.name.split('.')[0] + '.wav'
    
    # Save the WAV file
    sf.write(out_filename, data, sr, subtype='PCM_16')
    
    return out_filename

st.title("MP3 to WAV Converter")

# Allow the user to upload an MP3 file
mp3_file = st.file_uploader("Upload an MP3 file", type=['mp3'])

# If the user has uploaded a file
if mp3_file is not None:
    # Convert the MP3 file to a WAV file
    wav_filename = convert_mp3_to_wav(mp3_file)
    
    # Allow the user to download the converted WAV file
    with open(wav_filename, 'rb') as f:
        wav_contents = f.read()
        b64 = base64.b64encode(wav_contents).decode()
        href = f'<a href="data:audio/wav;base64,{b64}" download="{wav_filename}">Download {wav_filename}</a>'
        st.markdown(href, unsafe_allow_html=True)
