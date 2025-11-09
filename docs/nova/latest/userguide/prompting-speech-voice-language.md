# Voice-specific prompting techniques

Even within the same language, responses and word choices can be enhanced by steering the model for a particular locale. Therefore, we suggest that you include instructions in the system prompt to feature language that is natural and specific to the locale of your voice.

The available voices and locales are as follows:

| Language     | Feminine-sounding voice ID | Masculine-sounding voice ID |
| ------------ | -------------------------- | --------------------------- |
| English (US) | tiffany                    | matthew                     |
| English (GB) | amy                        |                             |
| French       | ambre                      | florian                     |
| Italian      | beatrice                   | lorenzo                     |
| German       | greta                      | lennart                     |
| Spanish      | lupe                       | carlos                      |

British English
To specify British English usage, add the following line to your prompt:

`Use British English as your language for your responses.`

###### Example of a complete prompt with British English selection

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios. Avoid formatted lists or numbering and keep your output as a spoken transcript to be acted out. Use British English as your language for your responses.`

###### How to Specify a Voice Id

To select a specific voice for your interaction, include the `voiceId` parameter in your configuration. For example, to use the British English voice `amy`, use the following `audioOutputConfiguration`:

```
"audioOutputConfiguration": {
    "mediaType": "audio/lpcm",
    "sampleRateHertz": 24000,
    "sampleSizeBits": 16,
    "channelCount": 1,
    "voiceId": "amy",
    "encoding": "base64",
    "audioType": "SPEECH"
}
```

Spanish
To specify Spanish as the response language, add the following line to your prompt:

`Please respond exclusively in Spanish. If you have a question or suggestion, ask it in Spanish. I want to ensure that our communication remains in Spanish.`

###### Example of a complete prompt with Spanish selection

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios. Avoid formatted lists or numbering and keep your output as a spoken transcript to be acted out. Please respond exclusively in Spanish. If you have a question or suggestion, ask it in Spanish. I want to ensure that our communication remains in Spanish.`

###### How to Specify a Voice Id

To select a specific voice for your interaction, include the `voiceId` parameter in your configuration. For example, to use the Spanish voice `carlos`, use the following `audioOutputConfiguration`:

```
"audioOutputConfiguration": {
    "mediaType": "audio/lpcm",
    "sampleRateHertz": 24000,
    "sampleSizeBits": 16,
    "channelCount": 1,
    "voiceId": "carlos",
    "encoding": "base64",
    "audioType": "SPEECH"
}
```

French
To specify French as the response language, add the following line to your prompt:

`Please respond exclusively in French. If you have a question or suggestion, ask it in French. I want to ensure that our communication remains in French.`

###### Example of a complete prompt with French selection

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios. Avoid formatted lists or numbering and keep your output as a spoken transcript to be acted out. Please respond exclusively in French. If you have a question or suggestion, ask it in French. I want to ensure that our communication remains in French.`

###### How to Specify a Voice Id

To select a specific voice for your interaction, include the `voiceId` parameter in your configuration. For example, to use the French voice `ambre`, use the following `audioOutputConfiguration`:

```
"audioOutputConfiguration": {
    "mediaType": "audio/lpcm",
    "sampleRateHertz": 24000,
    "sampleSizeBits": 16,
    "channelCount": 1,
    "voiceId": "ambre",
    "encoding": "base64",
    "audioType": "SPEECH"
}
```

Italian
To specify Italian as the response language, add the following line to your prompt:

`Please respond exclusively in Italian. If you have a question or suggestion, ask it in Italian. I want to ensure that our communication remains in Italian.`

###### Example of a complete prompt with Italian selection

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios. Avoid formatted lists or numbering and keep your output as a spoken transcript to be acted out. Please respond exclusively in Italian. If you have a question or suggestion, ask it in Italian. I want to ensure that our communication remains in Italian.`

###### How to Specify a Voice Id

To select a specific voice for your interaction, include the `voiceId` parameter in your configuration. For example, to use the Italian voice `lorenzo`, use the following `audioOutputConfiguration`:

```
"audioOutputConfiguration": {
    "mediaType": "audio/lpcm",
    "sampleRateHertz": 24000,
    "sampleSizeBits": 16,
    "channelCount": 1,
    "voiceId": "lorenzo",
    "encoding": "base64",
    "audioType": "SPEECH"
}
```

German
To specify German as the response language, add the following line to your prompt:

`Please respond exclusively in German. If you have a question or suggestion, ask it in German. I want to ensure that our communication remains in German.`

###### Example of a complete prompt with German selection

`You are a friend. The user and you will engage in a spoken dialog exchanging the transcripts of a natural real-time conversation. Keep your responses short, generally two or three sentences for chatty scenarios. Avoid formatted lists or numbering and keep your output as a spoken transcript to be acted out. Please respond exclusively in German. If you have a question or suggestion, ask it in German. I want to ensure that our communication remains in German.`

###### How to Specify a Voice Id

To select a specific voice for your interaction, include the `voiceId` parameter in your configuration. For example, to use the German voice `greta`, use the following `audioOutputConfiguration`:

```
"audioOutputConfiguration": {
    "mediaType": "audio/lpcm",
    "sampleRateHertz": 24000,
    "sampleSizeBits": 16,
    "channelCount": 1,
    "voiceId": "greta",
    "encoding": "base64",
    "audioType": "SPEECH"
}
```
