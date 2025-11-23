# Creating Amazon Lex V2 bots using templates

Amazon Lex V2 offers pre-built solutions to create experiences at scale and drive digital
engagement. The pre-built bot templates automates and
standardizes client experiences. The bot templates provide ready-to-use conversation
flows along with both training data and dialog prompts, for both
voice and chat modalities. You can expedite the delivery of bot solutions while
optimizing resources, so that you can focus on customer relationships.

You can create pre-built bots based on your business use case.
You can use the CloudFormation console to select the pre-built options for the related services,
such as Amazon S3, Amazon Connect and DynamoDB.

Currently, Amazon Lex V2 supports the following business verticals:

- Financial services
- Retail orders
- Auto insurance
- Telecommunications
- Airline services
- Additional templates will be available in the future.
  You can build a bot with the business solution template provided,
  and customize it for your business requirements.

###### Note

The templates create resources outside of Amazon Lex V2 through CloudFormation
stacks. The stack may need to be modified in other consoles such as Lambda
and DynamoDB.

**Prerequisites to build and deploy
the bot template:**

- An AWS account
- Access to the following AWS services:
  - Amazon Lex V2 to create bots
  - Lambda for the business login functions
  - DynamoDB to create the tables
  - IAM access to create policies and roles
  - AWS CloudFormation to run the stack

- IAM access and secret key credentials
- Amazon Connect instance (optional)

###### Note

The use of different AWS services incurs respective usage
costs for each service.

###### To build a bot from Amazon Lex V2 templates:

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. Select **Bot templates** from the left navigation pane.
3. Select which business vertical you want to use for your bot template. NOTE:
   There are 5 bot templates currently available. More to come soon.
4. Select **Create** for the template you want to use.
   A tab opens in CloudFormation where you can edit the parameters for the CloudFormation stack.
   All the options are already completed for the template you have chosen.
   You can also learn more about how the bot template works by selecting
   **Learn more**.
5. In the CloudFormation console, CloudFormation creates a
   default configuration for each of the values for the template you have chosen. You can
   also select your own stack name, CloudFormation parameters, Amazon DynamoDB table,
   and (optional) Amazon Connect parameters.
6. At the bottom of the window, select **Create stack**.
7. CloudFormation processes the request in the background for several minutes to
   configure your new bot. NOTE: The process automatically creates resources for a
   DynamoDB table, an Amazon Connect contact flow, and an Amazon Connect instance. You can track the
   progress in the CloudFormation console, and then navigate back to the Amazon Lex V2 console once
   the CloudFormation stack creation is completed.
8. If successfully built, a message appears and you can select
   **Go to bots list** to go to the **Bots** page,
   where you find your new bot that is ready for your testing and use.
   **Configuring your bot template**

**Lambda functions** – The bot template automatically creates
the needed Lambda functions for your deployment. If multiple bots are part of the
template solution, then multiple Lambda functions are listed in the
CloudFormation parameters. If you have existing Lambda functions to deploy with your bot,
you can enter the name of your custom Lambda function.

**Amazon DynamoDB** – The bot template automatically creates
the DynamoDB table needed to load your sample policy data. You can also enter the name
of your custom DynamoDB table. Your custom DynamoDB table should be formatted in the
same way as the default table created by the bot template deployment.

**Amazon Connect** – You can configure your Amazon Connect instance to work
with your new bot template by entering the ConnectInstanceARN and a unique
ContactFlowName. With the use of Amazon Connect, you can test your bot using an IVR system from
end-to-end.

**Troubleshooting your bot template**

- Check that you have the proper permissions to create the template that you are choosing.
  Users need CloudFormation:CreateStack permission along with permissions for the AWS
  resources that are listed within the template. A list of resources that need user
  permissions are at the bottom of the **Create template** page.
- If your bot template fails to be created, the red banner within the Amazon Lex V2 console
  provides a link to the CloudFormation stack that is responsible for creating the template.
  Within the CloudFormation console, you can view the events tab to see the specific error
  that caused the template to fail. Once you have reviewed the CloudFormation
  error, see
  [Troubleshooting CloudFormation](../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md "../../../AWSCloudFormation/latest/UserGuide/troubleshooting.md") for more information.
- Bot templates work with the sample data only. You must populate the DynamoDB table
  with your data to make the templates work with your custom data.
