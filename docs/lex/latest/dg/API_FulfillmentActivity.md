End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# FulfillmentActivity

Describes how the intent is fulfilled after the user provides all
of the information required for the intent. You can provide a Lambda
function to process the intent, or you can return the intent information
to the client application. We recommend that you use a Lambda function so
that the relevant logic lives in the Cloud and limit the client-side code
primarily to presentation. If you need to update the logic, you only
update the Lambda function; you don't need to upgrade your client
application.

Consider the following examples:

- In a pizza ordering application, after the user provides all of
  the information for placing an order, you use a Lambda function to
  place an order with a pizzeria.
- In a gaming application, when a user says "pick up a rock,"
  this information must go back to the client application so that it can
  perform the operation and update the graphics. In this case, you want
  Amazon Lex to return the intent data to the client.

## Contents

**type**

How the intent should be fulfilled, either by running a Lambda
function or by returning the slot data to the client application.

Type: String

Valid Values: `ReturnIntent | CodeHook`

Required: Yes

**codeHook**

A description of the Lambda function that is run to fulfill the
intent.

Type: [CodeHook](API_CodeHook.md "API_CodeHook.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/FulfillmentActivity.md "../../../goto/SdkForCpp/lex-models-2017-04-19/FulfillmentActivity.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/FulfillmentActivity.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/FulfillmentActivity.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/FulfillmentActivity.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/FulfillmentActivity.md")
