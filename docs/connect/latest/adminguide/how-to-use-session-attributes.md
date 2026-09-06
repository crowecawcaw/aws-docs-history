

# How flow blocks use Amazon Lex session attributes
<a name="how-to-use-session-attributes"></a>

When a customer starts a conversation with your bot, Amazon Lex creates a *session*. With *session attributes*, also known as *Lex attributes*, you can pass information between the bot and Connect Customer during the session. For a list of Amazon Lex attributes that you can use, see [Amazon Lex contact attributes](connect-attrib-list.md#attribs-lex-table).

## Life cycle of session attributes
<a name="session-attribute-lifecycle"></a>

Each conversation contains one set of session attributes. In cases where an AWS Lambda function is invoked to do some processing, Amazon Lex runs the attributes in the following order:
+ Service defaults: These attributes are only used if no attributes are defined.
+ Session attributes provided by Connect Customer: These attributes are defined in the [Get customer input](get-customer-input.md) block.
+ Session attributes provided by Lambda override everything prior: When an AWS Lambda function is invoked and it does some processing, it overrides any session attributes set in the [Get customer input](get-customer-input.md) block.

Let's say a customer utters that they want **a car**. That's the first session attribute to go through processing. When asked what kind of car, they say **luxury car**. This second utterance overrides any Lambda processing that took place on the first utterance. 

For an example of how to create a Lambda function that processes session attributes, see [Step 1: Create a Lambda Function](https://docs.aws.amazon.com/lex/latest/dg/gs2-prepare.html) in the *Amazon Lex Developer Guide*. For information about Amazon Lex V2, see [Setting session attributes](https://docs.aws.amazon.com/lexv2/latest/dg/context-mgmt-session-attribs.html). 

For the structure of the event data that Amazon Lex provides to a Lambda function, see [Lambda Function Input Event and Response Format](https://docs.aws.amazon.com/lex/latest/dg/lambda-input-response-format.html) in the *Amazon Lex Developer Guide*. For information about Amazon Lex V2, see [Interpreting the input event format](https://docs.aws.amazon.com/lexv2/latest/dg/lambda-input-format.html).

## Flow blocks that support Lex session attributes
<a name="blocks-support-lex-session-attributes"></a>

You can use Lex session attributes in the following flow blocks when a Lex bot is called:
+  [Change routing priority / age](change-routing-priority.md) 
+  [Check contact attributes](check-contact-attributes.md) 
+  [Get customer input](get-customer-input.md) 
+  [AWS Lambda function](invoke-lambda-function-block.md) 
+  [Loop](loop.md) 
+  [Set callback number](set-callback-number.md) 
+  [Set contact attributes](set-contact-attributes.md) 
+  [Set customer queue flow](set-customer-queue-flow.md) 
+  [Set disconnect flow](set-disconnect-flow.md) 
+  [Set hold flow](set-hold-flow.md) 
+  [Set logging behavior](set-logging-behavior.md) 
+  [Set whisper flow](set-whisper-flow.md) 
+  [Set working queue](set-working-queue.md) 
+  [Transfer to flow](transfer-to-flow.md) 
+  [Transfer to phone number](transfer-to-phone-number.md) 
+  [Wait](wait.md) 

### More information
<a name="more-info-attributes"></a>

For more information about using Amazon Lex session attributes, see [Managing Conversation Context](https://docs.aws.amazon.com/lex/latest/dg/context-mgmt.html) in the *Amazon Amazon Lex V1 Developer Guide*.