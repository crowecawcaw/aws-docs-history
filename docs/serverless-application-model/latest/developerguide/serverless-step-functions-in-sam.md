# Orchestrating AWS SAM resources with

AWS Step Functions

You can use [AWS Step Functions](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md") to orchestrate AWS Lambda functions
and other AWS resources to form complex and robust workflows. Step Functions to tell your application
when and under what conditions your AWS resources, like AWS Lambda functions, are used.
This simplifies the process of forming complex and robust workflows. Using
[AWS::Serverless::StateMachine](sam-resource-statemachine.md "sam-resource-statemachine.md"),
you define the individual steps in your workflow, associate resources in each step, and
then sequence these steps together. You also add transitions and conditions where they are needed.
This simplifies the process of making a complex and robust workflow.

###### Note

To manage AWS SAM templates that contain Step Functions state machines, you must use version 0.52.0
or later of the AWS SAM CLI. To check which version you have, execute the command `sam
 --version`.

Step Functions is based on the concepts of [tasks](../../../step-functions/latest/dg/amazon-states-language-task-state.md "../../../step-functions/latest/dg/amazon-states-language-task-state.md") and [state machines](../../../step-functions/latest/dg/concepts-states.md "../../../step-functions/latest/dg/concepts-states.md"). You define state machines
using the JSON-based [Amazon States Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md"). The [Step Functions console](https://console.aws.amazon.com/states/home?region=us-east-1#/ "https://console.aws.amazon.com/states/home?region=us-east-1#/") displays a graphical view of your state machine's structure so you can
visually check your state machine's logic and monitor executions.

With Step Functions support in AWS Serverless Application Model (AWS SAM), you can do the following:

- Define state machines, either directly within an AWS SAM template or in a separate file
- Create state machine execution roles through AWS SAM policy templates, inline policies, or
  managed policies
- Trigger state machine executions with API Gateway or Amazon EventBridge events, on a schedule within an
  AWS SAM template, or by calling APIs directly
- Use available [AWS SAM Policy
  Templates](serverless-policy-templates.md "serverless-policy-templates.md") for common Step Functions development patterns.

## Example

The following example snippet from a AWS SAM template file defines a Step Functions state machine in
a definition file. Note that the `my_state_machine.asl.json` file must be written
in [Amazon States
Language](../../../step-functions/latest/dg/concepts-amazon-states-language.md "../../../step-functions/latest/dg/concepts-amazon-states-language.md").

```
AWSTemplateFormatVersion: "2010-09-09"
Transform: AWS::Serverless-2016-10-31
Description: Sample SAM template with Step Functions State Machine

Resources:
  MyStateMachine:
    Type: AWS::Serverless::StateMachine
    Properties:
      DefinitionUri: statemachine/my_state_machine.asl.json
      ...
```

To download a sample AWS SAM application that includes a Step Functions state machine, see [Create a Step Functions State Machine Using
AWS SAM](../../../step-functions/latest/dg/tutorial-state-machine-using-sam.md "../../../step-functions/latest/dg/tutorial-state-machine-using-sam.md") in the _AWS Step Functions Developer Guide_.

## More information

To learn more about Step Functions and using it with AWS SAM, see the following:

- [How AWS Step Functions
  works](../../../step-functions/latest/dg/how-step-functions-works.md "../../../step-functions/latest/dg/how-step-functions-works.md")
- [AWS Step Functions and AWS Serverless Application Model](../../../step-functions/latest/dg/concepts-sam-sfn.md "../../../step-functions/latest/dg/concepts-sam-sfn.md")
- [Tutorial: Create a
  Step Functions State Machine Using AWS SAM](../../../step-functions/latest/dg/tutorial-state-machine-using-sam.md "../../../step-functions/latest/dg/tutorial-state-machine-using-sam.md")
- [AWS SAM Specification:
  AWS::Serverless::StateMachine](sam-resource-statemachine.md "sam-resource-statemachine.md")
