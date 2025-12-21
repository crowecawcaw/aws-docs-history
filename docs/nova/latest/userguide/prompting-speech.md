# Amazon Nova Sonic prompting best practices

###### Note

This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](../nova2-userguide/sonic-system-prompts.md "../nova2-userguide/sonic-system-prompts.md").

The Amazon Nova Sonic model requires a different prompting approach than standard text-based models. When you craft prompts for speech-to-speech models, it's important to understand that the _system prompt_ steers the model's output style and lexical choice. It can't be used to change speech attributes such as accent and pitch. The model decides those speech characteristics based on the context of the conversation.

The key distinction is that the output is speech audio, instead of written text. This means you should optimize content for auditory comprehension rather than for reading comprehension. Your prompts should guide the model to generate text that will be naturally converted to speech. Focus on conversational flow and clarity when heard rather than when read.

###### Topics

- [System prompt authoring guidelines and examples](prompting-speech-speech.md "prompting-speech-speech.md")
- [Best practices for the Amazon Nova Sonic system prompt](prompting-speech-best-practices.md "prompting-speech-best-practices.md")
- [Example custom system prompts](prompting-speech-examples.md "prompting-speech-examples.md")
