

# Integrating an AWS Lambda function into your Amazon Lex V2 bot
<a name="lambda"></a>

With [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions, you can extend and better control the behavior of your Amazon Lex V2 bot through custom functions that you define. Amazon Lex V2 uses one Lambda function per bot alias per language instead of one Lambda function for each intent. Before you begin, determine which fields in the [input event](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-input-format) you want to draw information from and which fields in the [response](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-response-format) you want to manipulate and return from your Lambda function

To integrate a Lambda function with your Amazon Lex V2 bot, carry out the following steps:

1. [Create a function](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach) in AWS Lambda using your programming language of choice and write up your script.

1. Make sure that the function returns a structure matching the [response format](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-response-format).

1. Deploy the Lambda function.

1. Associate the Lambda function with an Amazon Lex V2 bot alias with the [console](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-console) or [API operations](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-api).

1. Select the conversation stages at which you want to invoke your Lambda function with the [console](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-console) or [API operations](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-attach-api).

1. Build your Amazon Lex V2 bot and test that the Lambda function works as intended. [Debug](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-debug) your function with the help of Amazon CloudWatch.

**Topics**
+ [AWS Lambda input event format for Lex V2](lambda-input-format.md)
+ [AWS Lambda response format for Lex V2](lambda-response-format.md)
+ [Common structures in an AWS Lambda function for Amazon Lex V2](lambda-common-structures.md)
+ [Creating an AWS Lambda function for your Amazon Lex V2 bot](lambda-attach.md)
+ [Debugging a Lambda function using CloudWatch Logs logs](lambda-debug.md)