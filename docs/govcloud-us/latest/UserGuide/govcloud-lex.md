# Amazon Lex in AWS GovCloud (US)

This service is currently available in AWS GovCloud (US-West) only.

Amazon Lex is an AWS service for building conversational interfaces for applications using voice and text. With Amazon Lex, the same conversational engine that powers Amazon Alexa is now available to any developer, enabling you to build sophisticated, natural language chatbots into your new and existing applications. Amazon Lex provides the deep functionality and flexibility of natural language understanding (NLU) and automatic speech recognition (ASR) so you can build highly engaging user experiences with lifelike, conversational interactions, and create new categories of products.

## How Amazon Lex differs for AWS GovCloud (US)

- Amazon Lex V2 and Amazon Lex V1 are available in AWS GovCloud (US).
- Amazon Lex does not support channels, which enable bots to integrate with messaging platforms such as Facebook, Slack, and Twilio.
- The Amazon Lex console does not show utterances or missed utterances. The GetUtterancesView API action is not supported.
- The supported languages include only en-US and es-US.
- Amazon Lex does not support conversation logs, which store interactions to help you review the bot’s performance and troubleshoot.
- In AWS GovCloud (US) Regions, AWS DOES NOT use or store AI Content processed by this AI Service to develop and improve that Service or technologies of AWS or its affiliates. Opt-out policies are not currently applicable to these Regions.

## Documentation for Amazon Lex

[Amazon Lex documentation](../../../lex/latest/dg/what-is.md "../../../lex/latest/dg/what-is.md").

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- The following customer-defined metadata may leave the AWS GovCloud (US) Regions only when the customer asks AWS to investigate a reported issue:
  - Bot definitions
  - Intent definitions
  - Slot definitions
  - Session attributes that customers use for the Get customer input block in the Amazon Connect console, such as `x-amz-lex:start-silence-threshold-ms` or `x-amz-lex:end-silence-threshold-ms`. For all session attributes, see [Contact block: Get customer input](../../../connect/latest/adminguide/get-customer-input.md "../../../connect/latest/adminguide/get-customer-input.md") in the Amazon Connect Administrator Guide.
