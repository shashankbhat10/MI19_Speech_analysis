import json
from os.path import join, dirname
from pathlib import Path
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud.tone_analyzer_v3 import ToneInput
#from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
#import threading

# If service instance provides API key authentication
serviceSTT = SpeechToTextV1(
     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
     url='https://gateway-wdc.watsonplatform.net/speech-to-text/api',
     iam_apikey='RMs3qp5i6BqBRpsX8t3VZyeHnA6XC1fyukmR2Qyzs1pA')

serviceTA = ToneAnalyzerV3(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
     url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api',
     version='2017-09-21',
     iam_apikey='zvgefX4PvTTiZANZ1D-gjMRKwzsearhopLuvwO7Fqspd')



#models = service.list_models().get_result()
#print(json.dumps(models, indent=2))

#model = service.get_model('en-US_BroadbandModel').get_result()
model = serviceSTT.get_model('en-US_NarrowbandModel').get_result()
#print(json.dumps(model, indent=2))


data_folder = Path(dirname(__file__))
#file_to_open = data_folder / 'OSR_us_000_0010_8k.wav'
file_to_open = data_folder / 'harvard.wav'


#print("TEXT IS: ")
with open(file_to_open,'rb') as audio_file:
    json_result = serviceSTT.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='en-US_NarrowbandModel',
            continuous = True,
            timestamps=False,
            speaker_labels=True,
            word_confidence=False).get_result()
    #print(json_result["results"][0]["alternatives"][0]["transcript"])

    text = json_result["results"][0]["alternatives"][0]["transcript"]
    print(text)
    print("Tone is:")
    json_tone = serviceTA.tone(
        tone_input = text,
        content_type="text/plain").get_result()
    #print(json_result["results"][0]["alternatives"][0]["transcript"])
    print(json_tone)

'''print("Tone is:")
json_tone = serviceTA.tone(
    tone_input ='''
    
'''with open(file_to_open,'rb') as audio_file:
    print(json.dumps(
        service.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='en-US_NarrowbandModel',
            continuous = True,
            timestamps=False,
            speaker_labels=True,
            word_confidence=False).get_result(),
        indent=2))
'''

