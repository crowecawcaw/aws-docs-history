

# External tool integration
<a name="prompting-speech-bp-tools"></a>

**Note**  
This documentation is for Amazon Nova Version 1. For the Amazon Nova 2 Speech-to-Speech prompt engineering guide, visit [Voice conversation prompts](https://docs.aws.amazon.com/nova/latest/nova2-userguide/sonic-system-prompts.html).

When [you use external tools](https://docs.aws.amazon.com/nova/latest/userguide/prompting-tools.html) with Amazon Nova Sonic, we recommend the following:
+ Design tool invocations to handle potential automatic speech recognition errors in user input.
+ Account for the fact that users can't see the tools being used.
+ Provide verbal confirmation when tools are being consulted.