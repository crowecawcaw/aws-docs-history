# Sample Lambda integration flow in

Amazon Connect

###### Note

This topic explains a sample flow that is included with Amazon Connect. For information
about locating the sample flows in your instance, see [Sample flows in Amazon Connect](contact-flow-samples.md "contact-flow-samples.md").

Type: Flow (inbound)

This flow shows you how to invoke a Lambda function and do a data dip, that is,
retrieve information about the customer. The data dip uses the caller's phone number to
look up the US state they are calling from. If the customer is using chat, it returns a
fun fact. Here's how it works:

1. A prompt tells the customer that a data dip is being performed.
2. The [AWS Lambda
   function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block triggers
   **sampleLambdaFlowFunction**. This sample Lambda function
   determines the location of the phone number. The function times out in 4
   seconds. If it times out, it plays a prompt that says "Sorry, we failed to find
   the state for your phone number's area code."
3. In the first **Check contact attributes** block, it checks
   the channel the customer is using: voice, chat, task. If chat, it returns a fun
   fact.
4. If voice, the second **Check contact attributes** block is
   triggered. It checks the match conditions of **State**, which
   is an external attribute. It uses an external contact attribute because it's
   getting data by using a process that's external to Amazon Connect
5. A prompt tells you that it's returning you back to **Sample inbound
   flow**, and then starts the **Transfer flow**
   block.
6. If the transfer fails, it plays a prompt and then disconnects the contact.
   For more information about using attributes, see [Store a value from a Lambda functions as a contact
   attribute in Amazon Connect](attribs-with-lambda.md "attribs-with-lambda.md").
