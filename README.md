# MP3 to WAV Converter
This is a simple Python script that converts MP3 files to WAV format. It includes two implementations: one using soundfile library and the other using pydub library. The soundfile version is implemented in a Jupyter Notebook while the pydub version is implemented as a Streamlit web application.

## [Dependencies](https://github.com/prathmeshdesai1996/mp3_to_wav-convertor/blob/main/requirements.txt)
To install the required dependencies, run the following command:
```
pip install -r requirements.txt
```

## Usage
### Using soundfile
To use the soundfile version, you can simply run the [mp3_to_wav_converter.ipynb notebook](https://github.com/prathmeshdesai1996/mp3_to_wav-convertor/blob/main/mp3_to_wav_converter.ipynb). Before running the notebook, make sure you have installed the soundfile library.

The [notebook](https://github.com/prathmeshdesai1996/mp3_to_wav-convertor/blob/main/mp3_to_wav_converter.ipynb) includes a convert_mp3_to_wav function that converts MP3 files to WAV format. You can specify the input folder and output folder for the function. If you don't specify the output folder, the function will create a folder named "converted_audio" and save the output files there.

Before running the script, make sure you have installed the streamlit and soundfile libraries.
```
pip install streamlit soundfile
```

The script runs a Streamlit web application that allows you to upload an MP3 file and convert it to WAV format. The converted file can be downloaded from the web application.

To run the web application, navigate to the project directory and run the following command:

```
streamlit run streamlit_app.py
```

## Sample Files
The [sample_mp3_files directory](https://github.com/prathmeshdesai1996/mp3_to_wav-convertor/tree/main/sample_mp3_files) contains sample MP3 files that you can use to test the converter.

## Output Files
The [converted_audio directory](https://github.com/prathmeshdesai1996/mp3_to_wav-convertor/tree/main/converted_audio) stores the converted WAV files.

## [Web Application](https://prathmeshdesai1996-mp3-to-wav-convertor-streamlit-app-9l0xnu.streamlit.app/)
A live version of the Streamlit web application is available [here](https://prathmeshdesai1996-mp3-to-wav-convertor-streamlit-app-9l0xnu.streamlit.app/).
