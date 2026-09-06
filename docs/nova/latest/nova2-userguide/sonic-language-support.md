

# Language support and multilingual capabilities
<a name="sonic-language-support"></a>

Amazon Nova 2 Sonic provides a diverse selection of voices across multiple languages, enabling you to create conversational AI applications that feel natural and culturally appropriate for your users. Each language offers both feminine-sounding and masculine-sounding voice options.

The following table lists all available voices and their corresponding language locales:


| Language | Locale | Feminine-sounding Voice ID | Masculine-sounding Voice ID | 
| --- | --- | --- | --- | 
| English (US) | en-US | tiffany | matthew | 
| English (UK) | en-GB | amy | - | 
| English (Australia) | en-AU | olivia | - | 
| English (Indian) | en-IN | kiara | arjun | 
| French | fr-FR | ambre | florian | 
| Italian | it-IT | beatrice | lorenzo | 
| German | de-DE | tina | lennart | 
| Spanish (US) | es-US | lupe | carlos | 
| Portuguese | pt-BR | carolina | leo | 
| Hindi | hi-IN | kiara | arjun | 

## Event structure using voices in your application
<a name="sonic-event-voice"></a>

You can specify the voice ID in the `audioOutputConfiguration` when starting a prompt in the `promptStart` event:

```
"event": {
        "promptStart": {
            "promptName": "string",
            "audioOutputConfiguration": {
                "mediaType": "audio/lpcm",
                "sampleRateHertz": 16000,
                "sampleSizeBits": 16,
                "channelCount": 1,
                "voiceId": "tiffany",
                "encoding": "base64",
                "audioType": "SPEECH"
            }
        }
    }
```

## Multilingual support
<a name="sonic-polyglot-voices"></a>

Amazon Nova 2 Sonic provides powerful multilingual capabilities that enable natural conversations across multiple languages. The service supports both polyglot voices (speaking multiple languages) and code-switching (mixing languages within the same sentence), allowing you to build truly global conversational applications.

The TIFFANY (en-US, female) and MATTHEW (en-US, male) are unique polyglot voices that can speak all supported languages:

1. English

1. French

1. Italian

1. German

1. Spanish

1. Portuguese

1. Hindi

This makes Tiffany and Matthew ideal for applications that need to switch between multiple languages seamlessly.