# Call simulation concepts

The traditional contact center testing and simulation approaches rely on technical
step IDs and transitions that are inconsistent with natural human interaction patterns,
creating a disconnect in validation processes. Connect's call simulation capabilities
use an event-driven trigger response model that mirrors natural cause-and-effect
reasoning patterns used by QA engineers and business testers. This approach removes the
need to know every interaction that are programmed in order to test and validate the
experience. Each test case is constructed as a sequence of observations paired with
actions. Dependencies between observations are handled as transitions, creating a
logical flow that matches human reasoning while maintaining technical precision. The
following terms are used in the test case configuration:

Observations

Observations represent each complete interaction that includes one
observed event expected from the system and many actions to validate or
simulate system behaviors.

Events
Events represent expected behaviors that would come from the system, such as a prompt, a bot message, or a Lambda call.

Actions
Actions represent what the testing framework should do in response to an event, such as sending DTMF, responding with text, asserting attribute values or ending the test.

Actors

Actors represent roles to be played in the testing framework. When
observing events, actors can be the system or agent, such as a play prompt
coming from the system or an agent accepting the call. When simulating
actions, actors can be the customer, system, or agent, such as simulating a
customer input DTMF or utterance, or simulating a system response from a
Lambda function.

## Interaction groups

Use interaction groups to create simulated interactions with the call center. Each interaction group has three defined steps, described as the following blocks:

Observe

This block is mandatory and is used to validate the expected interaction from the system with a matching type (Contains and Similarity match).

Check

This block is optional and is used to validate metadata such as user
defined attributes, system attributes, and segment attributes. You can
validate more than one attribute in the check block.

Actions

This block is optional and is used to override actions, override
resources, send instructions, or test control actions. You can use
override resources such as Lambda, Lex, Queue, or Hours of Operation
with alternative resources or override actions with response values from
related actions. You can validate the contact experience without
invoking external resources to speed up test execution and prevent real
data manipulation, such as preventing replaying a Lambda block that
charges a credit card in production environment. You can use send
instructions to simulate input to be sent to the contact center
experience, such as text/utterance, DTMF tone, or .wav file for
pre-recorded audio. Additionally, users can use test control action
types to log data and end the test case execution at any point. Overall,
you can simulate multiple types of actions in the action block
configuration.
