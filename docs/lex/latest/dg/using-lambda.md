End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Using Lambda Functions

You can create AWS Lambda functions to use as code hooks for your
Amazon Lex bot. You can identify Lambda functions to perform
initialization and validation, fulfillment, or both in your intent
configuration.

We recommend that you use a Lambda function as a code hook for your
bot. Without a Lambda function, your bot returns the intent information
to the client application for fulfillment.

###### Topics

- [Lambda Function Input
  Event and Response Format](lambda-input-response-format.md "lambda-input-response-format.md")
- [Amazon Lex and AWS Lambda
  Blueprints](lex-lambda-blueprints.md "lex-lambda-blueprints.md")
