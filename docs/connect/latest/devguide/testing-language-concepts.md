

# Connect Customer Testing language concepts
<a name="testing-language-concepts"></a>

The following terms are used in the Testing language.

## Observations
<a name="testing-language-concepts-observations"></a>

Observations represent each complete interaction that includes one observed event expected from the system and many actions to validate or simulate system behaviors.

## Events
<a name="testing-language-concepts-events"></a>

Events represent expected behaviors that would come from the system, such as a prompt, a bot message, or a Lambda call.

## Actions
<a name="testing-language-concepts-actions"></a>

Actions represent what the testing framework should do in response to an event, such as sending DTMF, responding with text, asserting attribute values, or ending the test.

## Actors
<a name="testing-language-concepts-actors"></a>

Actors represent roles to be played in the testing framework. When observing events, actors can be the system or agent, such as a play prompt coming from the system or an agent accepting the call. When simulating actions, actors can be the customer, system, or agent, such as simulating a customer input DTMF or utterance, or simulating a system response from a Lambda function.