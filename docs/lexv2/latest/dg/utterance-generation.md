# Use utterance generation to generate sample utterances for intent recognition

###### Note

Before you can take advantage of the generative AI features, you must fulfill the following prerequisites

1. Navigate to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock "https://console.aws.amazon.com/bedrock") and sign up for access
   to the Anthropic Claude model you intend to use (for more information, see [Model access](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md")). For information
   about pricing for using Amazon Bedrock, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/ "https://aws.amazon.com/bedrock/pricing/").
2. Turn on the
   generative AI capabilities for your bot locale. To do so, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md "generative-features.md").
   Use utterance generation to automate the creation of sample utterances for your intent. Instead of manually inputting sample utterances, Amazon Lex V2 generates sample utterances for you based off the intent name, description, and existing sample utterances, so that you can reduce the time and effort you spend in discovering and writing your own sample utterances. After Amazon Lex V2 generates utterances, you can edit and delete the utterances. Use this tool to expedite the creation of sample utterances for the intent recognition process.

To allow utterance generation, follow the steps at [Optimize Lex V2 bot creation and performance by using generative AI](generative-features.md "generative-features.md") to activate generative AI capabilities.

To access this feature on Amazon Lex V2 console, ensure your console role has `bedrock:ListFoundationModels` and `bedrock:InvokeModel` permissions.

You can generate utterances with either the console or the API.

Console

1. Navigate to the **Sample utterances** section of any intent in your bot (in the Visual conversation builder, it is
   in the **Start** block).
2. Select the **Generate utterances** button to generate 5 sample utterances. If your intent has over 25 sample
   utterances, the **Generate utterances** button becomes disabled.
3. Generated utterances are displayed with a green banner that differentiates the generated
   utterances from the existing utterances.
4. Hover over an utterance to display the options to edit, delete, and sort the generated utterances.

API

1. Send a [GenerateBotElement](../APIReference/API_GenerateBotElement.md "../APIReference/API_GenerateBotElement.md") request,
   filling in the intent and bot ID, version, and locale for which you want to generate sample utterances.
2. The response returns a list of [SampleUtterance](../APIReference/API_SampleUtterance.md "../APIReference/API_SampleUtterance.md") objects, each of which contains a generated utterance.
3. To add the utterances to the intent, send an [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") request and add the utterances to the `sampleUtterances` field.
