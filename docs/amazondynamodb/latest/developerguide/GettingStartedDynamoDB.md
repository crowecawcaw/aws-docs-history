# Getting started with DynamoDB

You’ll learn how to connect to, create, and manage DynamoDB tables in the following
sections.

Before you begin, you should familiarize yourself with the basic concepts in Amazon DynamoDB.
You can get a quick overview in [What is Amazon DynamoDB?](Introduction.md "Introduction.md")
and a more in-depth look in [Core components of Amazon DynamoDB](HowItWorks.md "HowItWorks.md"). Then, continue on to [Prerequisites](#GettingStarted.SettingUp.DynamoWebService "#GettingStarted.SettingUp.DynamoWebService").

###### Note

When you sign up for AWS, you can get started with DynamoDB using the [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/"). If you have not already
exceeded the free tier benefits for Amazon DynamoDB, it won't cost you anything to complete
the examples in this section. Otherwise, you'll incur the standard DynamoDB usage fees from
the time that you create the tables until you delete the tables.

If you don't want to sign up for a free tier account, you can set up [DynamoDB local (downloadable version)](DynamoDBLocal.md "DynamoDBLocal.md") on your computer.
The downloadable version lets you develop and test applications locally without signing
up for an AWS account or accessing the DynamoDB web service.

###### Topics

- [Amazon DynamoDB resources for first-time users](dynamodb-resources-first-time-users.md "dynamodb-resources-first-time-users.md")
- [Accessing DynamoDB](AccessingDynamoDB.md "AccessingDynamoDB.md")
- [Prerequisites](#GettingStarted.SettingUp.DynamoWebService "#GettingStarted.SettingUp.DynamoWebService")
- [Setting up DynamoDB](SettingUp.md "SettingUp.md")
- [Step 1: Create a table in DynamoDB](getting-started-step-1.md "getting-started-step-1.md")
- [Step 2: Write data to a DynamoDB table](getting-started-step-2.md "getting-started-step-2.md")
- [Step 3: Read data from a DynamoDB table](getting-started-step-3.md "getting-started-step-3.md")
- [Step 4: Update data in a DynamoDB table](getting-started-step-4.md "getting-started-step-4.md")
- [Step 5: Query data in a DynamoDB table](getting-started-step-5.md "getting-started-step-5.md")
- [Step 6: (Optional) Delete your DynamoDB table to clean up resources](getting-started-step-6.md "getting-started-step-6.md")
- [Continue learning about DynamoDB](getting-started-NextSteps.md "getting-started-NextSteps.md")
- [Generate infrastructure code for Amazon DynamoDB using Console-to-Code](console-to-code.md "console-to-code.md")

## Prerequisites

Before starting the Amazon DynamoDB tutorial, learn about the ways you can access DynamoDB in
[Accessing DynamoDB](AccessingDynamoDB.md "AccessingDynamoDB.md"). Then, set up
DynamoDB through either the web service or the locally downloaded version in [Setting up DynamoDB](SettingUp.md "SettingUp.md"). After
that, continue on to [Step 1: Create a table in DynamoDB](getting-started-step-1.md "getting-started-step-1.md").

###### Note

- If you plan to interact with DynamoDB only through the AWS Management Console, you don't
  need an AWS access key. Complete the steps in [Signing up for AWS](SettingUp.md#SettingUp.DynamoWebService.SignUpForAWS "SettingUp.md#SettingUp.DynamoWebService.SignUpForAWS"), and then continue on to [Step 1: Create a table in DynamoDB](getting-started-step-1.md "getting-started-step-1.md").
- If you don't want to sign up for a free tier account, you can set up
  [DynamoDB local
  (downloadable version)](DynamoDBLocal.md "DynamoDBLocal.md"). Then continue on to [Step 1: Create a table in DynamoDB](getting-started-step-1.md "getting-started-step-1.md").
- There are differences when working with CLI commands in terminals on Linux
  and Windows. The following guide presents commands formatted for Linux
  terminals (this includes macOS), and commands formatted for Windows CMD.
  Choose the command that best fits the terminal application you are using.
