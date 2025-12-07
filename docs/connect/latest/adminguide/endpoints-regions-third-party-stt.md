# Endpoints and Regions for third-party STT

providers

By default, Amazon Connect communicates with the following endpoints:

**Deepgram**: [https://api.deepgram.com](https://api.deepgram.com "https://api.deepgram.com")

**ElevenLabs**: [https://api.elevenlabs.io](https://api.elevenlabs.io "https://api.elevenlabs.io")

You can specify a different provider Region alongside your API key as part of the JSON
object:

```

{
  "apiToken": "XXXXX",
  "apiTokenRegion": "xx"
}

```

The following regions are supported:

| **Provider** | **apiTokenRegion**             | **Endpoint**                                                                                                                    |
| ------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Deepgram     | eu                             | [https://api.eu.deepgram.com](https://api.eu.deepgram.com "https://api.eu.deepgram.com") (only supported for<br>speech-to-text) |
| Deepgram     | {SHORT_UID}.{REGION_SUBDOMAIN} | https://{SHORT_UID}.{REGION_SUBDOMAIN}.api.deepgram.com (Deepgram Dedicated<br>endpoints)                                       |
| ElevenLabs   | us                             | [https://api.us.elevenlabs.io](https://api.us.elevenlabs.io "https://api.us.elevenlabs.io")                                     |
| ElevenLabs   | eu                             | [https://api.eu.residency.elevenlabs.io](https://api.eu.residency.elevenlabs.io "https://api.eu.residency.elevenlabs.io")       |
| ElevenLabs   | in                             | [https://api.in.residency.elevenlabs.io](https://api.in.residency.elevenlabs.io "https://api.in.residency.elevenlabs.io")       |
