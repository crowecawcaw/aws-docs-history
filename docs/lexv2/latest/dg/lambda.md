# Integrating an AWS Lambda function into your bot

With [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") functions, you can extend and
better control the behavior of your Amazon Lex V2 bot through custom functions that you define. Amazon Lex V2 uses one Lambda function
per bot alias per language instead of one Lambda function for each intent. Before you begin, determine which fields in
the [input event](lambda-input-format.md "lambda-input-format.md") you want to draw information
from and which fields in the [response](lambda-response-format.md "lambda-response-format.md") you
want to manipulate and return from your Lambda function

To integrate a Lambda function with your Amazon Lex V2 bot, carry out the following steps:

1. [Create a function](lambda-attach.md "lambda-attach.md") in AWS Lambda using your
   programming language of choice and write up your script.
2. Make sure that the function returns a structure matching
   the [response format](lambda-response-format.md "lambda-response-format.md").
3. Deploy the Lambda function.
4. Associate the Lambda function with an Amazon Lex V2 bot alias with the [console](lambda-attach-console.md "lambda-attach-console.md") or [API operations](lambda-attach-api.md "lambda-attach-api.md").
5. Select the conversation stages at which you want to invoke your Lambda function with the [console](lambda-attach-console.md "lambda-attach-console.md") or [API operations](lambda-attach-api.md "lambda-attach-api.md").
6. Build your Amazon Lex V2 bot and test that the Lambda function works as intended. [Debug](lambda-debug.md "lambda-debug.md") your function with the help of Amazon CloudWatch.

###### Topics

- [AWS Lambda input event format for Lex V2](lambda-input-format.md "lambda-input-format.md")
- [AWS Lambda response format for Lex V2](lambda-response-format.md "lambda-response-format.md")
- [Common structures in an AWS Lambda function for](lambda-common-structures.md "lambda-common-structures.md")
- [Creating an AWS Lambda function for your bot](lambda-attach.md "lambda-attach.md")
- [Debugging a Lambda function using CloudWatch Logs logs](lambda-debug.md "lambda-debug.md")
