

# System role adaptation
<a name="prompting-speech-bp-sysrole"></a>

**Note**  
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

Amazon Nova text models benefit from [clear role definitions](https://docs.aws.amazon.com/nova/latest/userguide/prompting-system-role.html). For Amazon Nova Sonic applications, consider the following:
+ Define roles that sound natural when speaking (such as, "friendly advisor" rather than "information retrieval system").
+ Use role descriptions that emphasize conversational attributes (warm, patient, concise) rather than text-oriented attributes (detailed, comprehensive, systematic).
+ Consider how the chosen voice might influence the perceived personality. Test the voices to chose the best voice for your use case. Review the [System prompt authoring guidelines and examples](prompting-speech-speech.md) section for techniques on how to indirectly influence the model's natural prosody.