End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Call Center Agent Assistant

In this tutorial, you use Amazon Lex with Amazon Kendra to build an agent assist bot that assists
customer support agents and publish it as a web application. Amazon Kendra is an enterprise search
service that uses machine learning to search through documents to find answers. For more
information about Amazon Kendra, see [the _Amazon Kendra Developer
Guide_](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md").

Amazon Lex bots are widely used in call centers as the first point of contact for customers. A
bot is often capable of resolving customer questions. When a bot can't answer a question, it
transfers the conversation to a customer support employee.

In this tutorial, we create an Amazon Lex bot that agents use to answer customer queries in
real time. By reading the answers that the bot provides, the agent is spared from looking up
answers manually.

The bot and web application that you create in this tutorial helps agents respond to
customers efficiently and accurately by quickly providing the right resources. The following
diagram shows how the web application works.

![Customer talking to a support agent. Amazon Lex keeps track of the conversation and calls the Kendra Search Intent if the customer asks a question, which then searches an index of documents stored in Amazon S3. Amazon Kendra finds the answer and returns it to Amazon Lex, which then displays the answer to the agent.](images/agent-tutorial.png)
As the diagram shows, the Amazon Kendra index of documents is stored in an Amazon Simple Storage Service (Amazon S3)
bucket. If you don't already have an S3 bucket, you can set one up when you create the Amazon Kendra
index. In addition to Amazon S3, you will use Amazon Cognito for this tutorial. Amazon Cognito manages permissions
for deploying the bot as a web application.

In this tutorial, you create an Amazon Kendra index that provides answers to customer
questions, create the bot and add intents that allow it to suggest answers based on the
conversation with the customer, set up Amazon Cognito to manage access permissions, and deploy the
bot as a web application.

**Estimated time:** 75 minutes

**Estimated cost:** $2.50 per hour for an Amazon Kendra index and
$0.75 for 1000 Amazon Lex requests. Your Amazon Kendra index continues to run after you are finished with
this exercise. Be sure to delete it to avoid unnecessary costs.

**Note:** Make sure that you choose the same AWS Region for
all the services used in this tutorial.

###### Topics

- [Step 1: Create an Amazon Kendra Index](agent-step-1.md "agent-step-1.md")
- [Step 2: Create an Amazon Lex Bot](agent-step-2.md "agent-step-2.md")
- [Step 3: Add a Custom and Built-in Intent](agent-step-3.md "agent-step-3.md")
- [Step 4: Set up Amazon Cognito](agent-step-4.md "agent-step-4.md")
- [Step 5: Deploy Your Bot as a Web Application](agent-step-5.md "agent-step-5.md")
- [Step 6: Use the Bot](agent-step-6.md "agent-step-6.md")
