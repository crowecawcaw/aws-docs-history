

# SynthesizeSpeech and StartSpeechSynthesisStream compared
<a name="bidirectional-streaming-choosing"></a>

**[SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/APIReference/API_SynthesizeSpeech.html)** is a request-response operation. You provide the complete text in a single request and receive the full synthesized audio in a single response. It supports all engines (standard, neural, long-form, generative), all output formats including speech marks, and has a text limit of 6,000 total characters (of which no more than 3,000 can be billed characters) per request. The response streams audio back as soon as the first bytes are available. Use this operation when you have all the text available upfront.

**[StartSpeechSynthesisStream](https://docs.aws.amazon.com/polly/latest/APIReference/API_StartSpeechSynthesisStream.html)** is a bidirectional streaming operation. It opens an HTTP/2 connection over which you send text incrementally and receive audio as it is synthesized. There is no per-request text limit since text is streamed continuously. It requires the generative engine and does not support speech marks. Use this operation when text arrives incrementally and you want audio output to begin before all input is available. Common scenarios include:
+ **Conversational AI and voice assistants**. A large language model generates response text in small chunks (tokens). Forward each text chunk to Amazon Polly as it arrives so the user hears speech while the model is still generating.
+ **Real-time translation**. A translation system produces translated text segment by segment. Stream each segment for synthesis without waiting for the full translation to complete.
+ **Long-form content exceeding SynthesizeSpeech limits**. Text longer than 6,000 characters can be streamed continuously without splitting into multiple requests or managing chunk boundaries.


**Comparison of SynthesizeSpeech and StartSpeechSynthesisStream**  

| Aspect | SynthesizeSpeech | StartSpeechSynthesisStream | 
| --- | --- | --- | 
| Protocol | Request-response | Bidirectional event stream (HTTP/2) | 
| Text delivery | Full text in request body | Streaming input text via TextEvent messages | 
| Audio delivery | Streaming audio response via HTTP response body | Streaming audio response via AudioEvent messages | 
| Engine support | standard, neural, long-form, generative | generative only | 
| SSML support | Yes (all engines; [Supported SSML tags](supportedtags.md)) | Yes ([Supported SSML tags](supportedtags.md)) | 
| Lexicons | Yes | Yes | 
| Speech marks | Yes | No | 
| Text limit | 6,000 total characters (3,000 billed) per request | 6,000 total characters (3,000 billed) per TextEvent | 
| AWS CLI support | Yes | No (bidirectional streaming requires an SDK) | 