# Best practices for the Amazon Nova Sonic system prompt

When crafting your system prompt for Amazon Nova Sonic, you should understand that speech-based interactions differ from text-based ones. While many [prompting best practices for Amazon Nova understanding models](prompting.md "prompting.md") apply to Amazon Nova Sonic, they must be adapted for the unique dynamics of spoken conversation. For instance, a user's typed response is a reliable source of input. However, a corresponding speech interaction may be limited in context and require a back-and-forth interaction to ask for more information before moving the conversation forward. Additionally, prompts that cater to long form outputs might result in a bad experience for users due to time spent listening to find the correct answer.

As outlined in the [Amazon Nova prompting guidance](prompting.md "prompting.md"), _prompt engineering_ optimizes input to improve model output quality. For Amazon Nova Sonic, these principles must be tailored for conversational speech patterns.

Consider the following details when writing your system prompts:

###### Clarity and precision

Instructions that are clear in text may need to be reformulated for speech contexts. Ensure your prompts seek confirmation of understanding before taking action through tools to prevent mishaps.

| Task                                                               | Traditional prompt                                                                                                                                                   | Speech-optimized prompt                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First, verify a user's identity information and reservation number | `Verify the user's identity by requesting their username, email address, and reservation number. Validate that the reservation number follows the format XXX-YYYYY.` | `When asking for verification, request one piece of information at a time. First ask for their name, then wait for their response and confirm it. Next, ask for their email and repeat it back for verification. Finally, ask for their booking code, listening for the three parts separated by dashes (XXX-YYYYY). After collecting the booking code, read it back character by character to confirm accuracy before proceeding.` |

###### Conversational flow

Prioritize natural dialogue flow over formal instructional structures.

| Task                                   | Traditional prompt                                                                                                                                                           | Speech-optimized prompt                                                                                                                                                                                                                                                                           |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Troubleshoot Wi-Fi connectivity issues | `Provide step-by-step instructions for troubleshooting Wi-Fi connectivity issues. Include diagnostic steps, common error codes, and resolutions for each potential problem.` | `Guide the customer through Wi-Fi troubleshooting as a conversation. Start by asking what they've already tried, then suggest one simple step at a time. After each step, pause to check if it is clear before moving on to the next solution. Use everyday language instead of technical terms.` |

###### Memory constraints

Remember that spoken interactions have different memory dynamics compared to text. For example, listeners can't "refer back" to previous text as easily when it's spoken.

| Task                    | Traditional prompt                                                                                                                                                                       | Speech-optimized prompt                                                                                                                                                                                                                                                                 |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Explain a return policy | `Reference sections 1.3, 2.7, and 4.2 from the attached document when answering the user's questions about regulatory compliance. Include specific paragraph numbers in your citations.` | `When explaining our return policy, focus on one key point at a time. First cover the 30-day window, then shipping requirements, and finally condition standards. Summarize all three points together at the end to reinforce the main requirements without overwhelming the customer.` |

###### Topics

- [Voice-specific prompting techniques](prompting-speech-voice-language.md "prompting-speech-voice-language.md")
- [Speech-friendly content techniques](prompting-speech-bp-speech.md "prompting-speech-bp-speech.md")
- [System role adaptation](prompting-speech-bp-sysrole.md "prompting-speech-bp-sysrole.md")
- [Chain-of-thought for speech](prompting-speech-bp-reasoning.md "prompting-speech-bp-reasoning.md")
- [External tool integration](prompting-speech-bp-tools.md "prompting-speech-bp-tools.md")
- [Prompt techniques to avoid](prompting-speech-bp-avoid.md "prompting-speech-bp-avoid.md")
