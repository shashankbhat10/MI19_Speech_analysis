import json
from os.path import join, dirname
from pathlib import Path
from watson_developer_cloud import SpeechToTextV1
#from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
#import threading

# If service instance provides API key authentication
service = SpeechToTextV1(
     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
     url='https://gateway-wdc.watsonplatform.net/speech-to-text/api',
     iam_apikey='RMs3qp5i6BqBRpsX8t3VZyeHnA6XC1fyukmR2Qyzs1pA')


#models = service.list_models().get_result()
#print(json.dumps(models, indent=2))

#model = service.get_model('en-US_BroadbandModel').get_result()
model = service.get_model('en-US_NarrowbandModel').get_result()
#print(json.dumps(model, indent=2))


data_folder = Path(dirname(__file__))
file_to_open = data_folder / 'OSR_us_000_0010_8k.wav'

with open(file_to_open,'rb') as audio_file:
    print(json.dumps(
        service.recognize(
            audio=audio_file,
            content_type='audio/wav',
            model='en-US_NarrowbandModel',
            continuous = True,
            timestamps=False,
            word_confidence=False).get_result(),
        indent=2))
