# Sample utterances

You create sample utterances that are variations of phrases that you expect users to use to initiate an intent. For example, for a `BookFlight` intent, you might include utterances such as the following:

1. I want to book a flight
2. help me get a flight.
3. plane tickets, please!
4. flight from {`DepartureCity`} to {`DestinationCity`}
   You should provide 10 or more sample utterances. Give samples that represent a wide range of sentence structures and words that users may utter. Consider incomplete sentences as well, such as in examples 3 and 4 above. You can also use slots that you have defined for the intent in a sample utterance by wrapping curly braces around the slot name, as in {`DepartureCity`} in example 4. If you include slot names in a sample utterance, Amazon Lex V2 fills the slots of the intent with the values that the user provides in the utterance.

A variety of sample utterances helps Amazon Lex V2 generalize to effectively recognize that the user wants to initiate the intent.

You can add sample utterances in the intent editor, visual conversation builder, or with the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") API operations. You can also generate sample utterances automatically by taking advantage of Amazon Bedrock's generative AI capabilities. For more information, see [Use utterance generation to generate sample utterances for intent recognition](utterance-generation.md "utterance-generation.md").

###### Use the Intent editor or Visual conversation builder

1. In the Intent editor, navigate to the **Sample utterances** section. In the Visual conversation builder, find the **Sample utterances** section in the **Start** block.
2. In the box with the transparent text `I want to book a flight`, type a sample utterance. Select **Add utterance** to add the utterance.
3. View the sample utterances you have added in either **Preview** or **Plain text** mode. In **Plain text**, each line is a separate utterance. In **Preview mode**, hover over an utterance to reveal the following options:
   - Select the text box to edit the utterance.
   - Select the x button on the right of the text box to delete the utterance.
   - Drag the button on the left of the text box to change the order of sample utterances.

4. Use the search bar at the top to search through your sample utterances and the dropdown menu next to it to sort by the order you added the utterances or in alphabetical order.

###### Use an API operation

1. Create a new intent with the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") operation or update an existing one with the [UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation.
2. The API request includes a `sampleUtterances` field, which maps to an array of [SampleUtterance](../APIReference/API_SampleUtterance.md "../APIReference/API_SampleUtterance.md") objects.
3. For each sample utterance that you want to add, append a `SampleUtterance` object to the array. Add the sample utterance as the value of the `utterance` field.
4. To edit and delete sample utterances, send an `UpdateIntent` request. The list of utterances you provide in the `sampleUtterances` field replaces the existing utterances.

###### Important

Any field that you leave blank in the `UpdateIntent` request will cause existing configurations in the intent to be deleted. Use the [DescribeIntent](../APIReference/API_DescribeIntent.md "../APIReference/API_DescribeIntent.md") operation to return the bot configuration and copy any configurations that you do not want to be deleted into the `UpdateIntent` request.
