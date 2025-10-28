# How Amazon Polly works

Amazon Polly converts input text into life-like speech. To use an Amazon Polly voice, choose a
[voice engine](voice-engines-polly.md "voice-engines-polly.md"), call a speech synthesis method,
provide the text that you want to synthesize, then specify an audio output format. Amazon Polly
then synthesizes the provided text into a high-quality speech audio stream.

- **Input text** – Provide the text that you want
  to synthesize, and Amazon Polly returns an audio stream. You can provide the input as
  plaintext or in Speech Synthesis Markup Language (SSML) format. With SSML you can
  control various aspects of speech, such as pronunciation, volume, pitch, and speech
  rate. For more information, see [Generating speech from SSML documents](ssml.md "ssml.md").
- **Available voices** – Amazon Polly provides a
  portfolio of languages and a variety of voices, including a bilingual voice (for
  both English and Hindi). For most languages you can choose from several voices, both
  male and female. When launching a speech synthesis task, you specify the voice ID,
  and then Amazon Polly uses this voice to convert the text to speech. Amazon Polly is not a
  translation service—the synthesized speech is in the same language as the
  text. Numbers represented as digits (for example, _53_, not
  _fifty-three_) are synthesized in the language of the voice
  and not the text. For more information, see [Voices in
  Amazon Polly](voices-in-polly.md "voices-in-polly.md").
- **Output format** – Amazon Polly can deliver the
  synthesized speech in multiple formats. You can select the audio format that suits
  your needs. For example, you might request the speech in the MP3 or Ogg Vorbis
  format for consumption by web and mobile applications. Or, you might request the PCM
  output format for consumption by AWS IoT devices and telephony solutions.

###### Note

To hear example Amazon Polly voices in your browser, see the [Amazon Polly product overview](https://aws.amazon.com/polly "https://aws.amazon.com/polly").
