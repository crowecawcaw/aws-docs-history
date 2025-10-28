# Testing and debugging Step Functions state machines

Step Functions provides the following ways to test and debug state machines:

## Test with Test State in console and API

In the Step Functions console, you can test an individual state with **Test State**. You provide the state definition and inputs in the console, then Step Functions runs the state and shows the outputs, all without creating a state machine.

Or, you can use the [TestState](../apireference/API_TestState.md "../apireference/API_TestState.md") API to test an individual state. You provide the definition of a single state, and the API will execute the state and report results, also without creating an actual state machine.

See [Testing with TestState](test-state-isolation.md "test-state-isolation.md")
through the [TestState API](../apireference/API_TestState.md "../apireference/API_TestState.md") to
test your states.

## Data flow simulator (unsupported)

Data flow simulator is a console tool that was built to test JSONPath syntax. The data
flow simulator is **unsupported**.

See [Testing with TestState](test-state-isolation.md "test-state-isolation.md")
through the [TestState API](../apireference/API_TestState.md "../apireference/API_TestState.md") to
test your states.

## Step Functions Local (unsupported)

With AWS Step Functions Local, a downloadable version of Step Functions, you can test applications with
Step Functions running in your own development environment.

Step Functions Local does **not** provide feature parity. For
example, there is no support for optimized service integrations, cross-account access, or distributed map.

###### Step Functions Local is unsupported

Step Functions Local does **not** provide feature parity and is **unsupported**.

You might consider third party solutions that emulate Step Functions for testing
purposes.
