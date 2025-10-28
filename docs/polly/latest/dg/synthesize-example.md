# Synthesizing speech with Amazon Polly example

This page presents a short speech synthesis example performed in the console, the AWS CLI, and with Python. This example performs speech synthesis from plain text, not SSML.

Console

###### Synthesize speech on the console

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/ "https://console.aws.amazon.com/polly/").
2. Choose the **Text-to-Speech** tab. The text field will load with example text so you can quickly try out Amazon Polly.
3. Turn off **SSML**.
4. Type or paste this text into the input box.

```
He was caught up in the game. In the middle of the 10/3/2014 W3C meeting he shouted, "Score!" quite loudly.
```

5. Under **Engine**, choose **Generative**, **Long Form**, **Neural**, or **Standard**.
6. Choose a language and AWS Region, then choose a voice. (If you select **Neural** for **Engine**, only the languages and voices that support NTTS are available. All Standard and Long Form voices are disabled.)
7. To listen to the speech immediately, choose **Listen**.
8. To save the speech to a file, do one of the following:
   1. Choose **Download**.
   2. To change to a different file format, expand **Additional
      settings**, turn on **Speech file format
      settings**, choose the file format that you want, and
      then choose **Download**.

AWS CLI
In this exercise, you call the `SynthesizeSpeech` operation by passing input text. You can save the resulting audio as a file and verify its content.

1. Run the `synthesize-speech` AWS CLI command to synthesize sample
   text to an audio file (`hello.mp3`).

The following AWS CLI example is formatted for Unix, Linux, and macOS.
For Windows, replace the backslash (\) Unix continuation character at the end of each line with a caret (^) and use full quotation marks (") around the input text with single quotes (') for interior tags.

```
aws polly synthesize-speech \
    --output-format mp3 \
    --voice-id Joanna \
    --text 'Hello, my name is Joanna. I learned about the W3C on 10/3 of last year.' \
    hello.mp3
```

In the call to `synthesize-speech`, you provide sample text to
be synthesized by a voice of your choice. You must provide a voice ID
(explained in the following step) and an output format. The command saves
the resulting audio to the `hello.mp3` file. In addition
to the MP3 file, the operation sends the following output to the console.

```
{
        "ContentType": "audio/mpeg",
        "RequestCharacters": "71"
}
```

2. Play the resulting `hello.mp3` file to verify the
   synthesized speech.

Python
To test the Python example code, you need the AWS SDK for Python (Boto). For instruction, see
[AWS SDK for Python (Boto3)](https://aws.amazon.com/sdk-for-python/ "https://aws.amazon.com/sdk-for-python/").

The Python code in this example performs the following actions:

- Invokes the AWS SDK for Python (Boto) to send a `SynthesizeSpeech` request
  to Amazon Polly (by providing some text as input).
- Accesses the resulting audio stream in the response and saves the audio to
  a file (`speech.mp3`) on your local disk.
- Plays the audio file with the default audio player for your local
  system.

Save the code to a file (example.py) and run it.

```
"""Getting Started Example for Python 2.7+/3.3+"""
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

# Create a client using the credentials and region defined in the [adminuser]
# section of the AWS credentials file (~/.aws/credentials).
session = Session(profile_name="adminuser")
polly = session.client("polly")

try:
    # Request speech synthesis
    response = polly.synthesize_speech(Text="Hello world!", OutputFormat="mp3",
                                        VoiceId="Joanna")
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
    # Note: Closing the stream is important because the service throttles on the
    # number of parallel connections. Here we are using contextlib.closing to
    # ensure the close method of the stream object will be called automatically
    # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
           output = os.path.join(gettempdir(), "speech.mp3")

           try:
            # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                   file.write(stream.read())
           except IOError as error:
              # Could not write to file, exit gracefully
              print(error)
              sys.exit(-1)

else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)

# Play the audio using the platform's default player
if sys.platform == "win32":
    os.startfile(output)
else:
    # The following works on macOS and Linux. (Darwin = mac, xdg-open = linux).
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])
```

For more in-depth examples, see the following topics:

- [Using SSML on the console](ssml-to-speech-console.md "ssml-to-speech-console.md")
- [Applying lexicons (Synthesizing Speech)](managing-lexicons-console-synthesize-speech.md "managing-lexicons-console-synthesize-speech.md")
- [Sample code and applications for Amazon Polly](samples-and-examples.md "samples-and-examples.md")
