# AlexaSkill

The object describing an `AlexaSkill` event source type.

## Syntax

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML

```
  SkillId: `String`

```

## Properties

`SkillId`

The Alexa Skill ID for your Alexa Skill. For more information about Skill ID see [Configure the trigger for a Lambda function](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#configuring-the-alexa-skills-kit-trigger "https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#configuring-the-alexa-skills-kit-trigger") in the Alexa Skills Kit documentation.

_Type_: String

_Required_: No

_CloudFormation compatibility_: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples

### AlexaSkillTrigger

Alexa Skill Event Example

#### YAML

```
AlexaSkillEvent:
  Type: AlexaSkill

```
