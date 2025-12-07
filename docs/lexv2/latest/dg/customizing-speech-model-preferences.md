# Configuring speech recognition model preferences

Amazon Lex V2 provides different speech recognition models that you can choose from to optimize the accuracy and performance of your bot's speech recognition capabilities. You can configure speech model preferences to select the most appropriate model for your use case.

## Speech recognition model types

Amazon Lex V2 supports the following speech recognition models:

Standard model

The standard speech recognition model provides reliable speech recognition performance for general use cases. This model offers consistent accuracy across a wide range of audio conditions and is suitable for most conversational AI applications.

Neural model

The neural speech recognition model provides enhanced accuracy and better handling of natural speech patterns, accents, and background noise. This model uses advanced neural network architectures to improve recognition performance, especially in challenging audio environments.

Deepgram

Deepgram provides a public speech-to-test (STT) API for users that create an account and an API key. See [https://deepgram.com/](https://deepgram.com/ "https://deepgram.com/") for information about their public offerings.

## Configuring speech model preferences

You can configure speech model preferences when creating or updating a bot locale. The speech model preference setting determines which recognition model Amazon Lex V2 uses to process audio input for your bot.

To configure speech model preferences:

1. In the Amazon Lex V2 console, navigate to your bot and select the locale you want to configure.
2. In the bot locale settings, locate the **Speech recognition settings** section.
3. For **Speech model preference**, choose one of the following options:
   - **Standard** - Use the standard speech recognition model for reliable performance across general use cases.
   - **Neural** - Use the neural speech recognition model for enhanced accuracy and better handling of natural speech patterns.
   - **Deepgram** - Use Deepgram's Listen API for speech recognition. For setup instructions, see [Setting up Deepgram speech model preference](customizing-speech-deepgram-setup.md "customizing-speech-deepgram-setup.md").

4. Save your changes to apply the speech model preference to your bot locale.

###### Note

If you don't specify a speech model preference, Amazon Lex V2 uses the standard model by default.

## Choosing the right speech model

Consider the following factors when choosing a speech recognition model for your bot:

- **Audio quality** - If your bot will process audio with background noise, varying audio quality, or challenging acoustic conditions, the neural model may provide better accuracy.
- **Speaker diversity** - If your bot will interact with users who have diverse accents or speech patterns, the neural model's enhanced natural language processing capabilities may improve recognition performance.
- **Performance requirements** - The standard model provides consistent performance and may be sufficient for applications with controlled audio environments and clear speech input.

You can test both models with your specific use case to determine which provides the best balance of accuracy and performance for your application.
