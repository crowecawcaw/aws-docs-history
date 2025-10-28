# Long-form voices

Amazon Polly has a **Long-form engine** that produces
human-like, highly expressive, and emotionally adept voices. Long-form voices are
designed to captivate listeners’ attention for longer content, such as news articles,
training materials, or marketing videos.

Amazon Polly Long-form voices are developed with a cutting-edge deep learning TTS
technology. The model learns to replicate phonemes, prosody, intonation, and other
phonetic and acoustic aspects of human language, resulting in a highly natural speech
output.

The Long-form engine uses text embeddings to interpret the meaning of a text. Using
text embeddings, the Long-form engine can generate the correct emphasis, pauses, and
tone of a natural voice. The result is a voice that combines the complete range of
emotional elements present in human communication. This includes mimicking surprisal or
differentiating dialogue from narration. Together, this creates a premium speech product
that sounds like a live human being.

###### Note

The state-of-the-art technology underlying these voices falls within the paradigm
of generative AI for language and voice modelling. A side effect of the technology is
that any updates to the training data and the model could result in a slight variations
to the way the voices sound, even in case when their overall quality improves with model
updates. This could have an impact on use cases with different content parts synthesized
over a long time period – for example, a season of podcasts.

## Available long-form voices

Amazon Polly currently offers four en-US and two es-ES long-form voices. Both languages have female and male voices available. The English long-form voices Daniel, Gregory, and Ruth are also available in a conversational NTTS variant.

|     | Language            | Language code | Name/ID                       | Gender                  |
| --- | ------------------- | ------------- | ----------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **English (US)**    | en-US         | Danielle Gregory Ruth Patrick | Female Male Female Male |
| 2   | **Spanish (Spain)** | es-ES         | Alba Raúl                     | Female Male             | ## Feature and region compatibility Amazon Polly long-form voices are available in the following regions: <br>• US East (N. Virginia): us-east-1 <br>• Other regions not available **The Amazon Polly Long-form engine supports the following features:** <br>• Real-time and asynchronous speech synthesis operations. <br>• All [speech marks](speechmarks.md "speechmarks.md"). <br>• Many (but not all) SSML tags are supported by Amazon Polly. For more information about NTTS-supported SSML tags, see [Supported SSML tags](supportedtags.md "supportedtags.md") <br>• As with standard voices, you can choose from various sampling rates to optimize the bandwidth and audio quality for your application. Valid sampling rates for standard, long-form, and neural voices are: 8 kHz, 16 kHz, 22kHz, or 24 kHz. The default for standard voices is 22 kHz. The default for long-form and neural voices is 24 kHz. Amazon Polly supports MP3, OGG (Vorbis), and raw PCM audio stream formats. ###### Note Long-form voices cost is specified on the [Amazon Polly pricing information page](https://aws.amazon.com/polly/pricing/ "https://aws.amazon.com/polly/pricing/"). |
