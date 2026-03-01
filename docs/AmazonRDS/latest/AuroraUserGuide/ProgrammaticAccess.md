# Programmatic access to Amazon Aurora

Amazon RDS provides you with the following tools to manage your Amazon Aurora
resources programmatically.

**AWS Command Line Interface (AWS CLI)**

You can create and manage your Amazon Aurora resources by
using the AWS CLI in a command-line shell. The AWS CLI provides direct access to the
APIs for AWS services, such as Amazon RDS. For syntax and examples for the commands
for Amazon RDS, see [rds](../../../cli/latest/reference/rds.md "../../../cli/latest/reference/rds.md") in the _AWS CLI Command
Reference_.

**AWS CloudFormation**

With this AWS Infrastructure as Code (IaC) tool, you can create templates
that describe all of the Amazon Aurora resources that you want, and AWS CloudFormation
provisions and configures those resources for you. For more information, see
[Creating Amazon Aurora resources with AWS CloudFormation](creating-resources-with-cloudformation.md "creating-resources-with-cloudformation.md").

**AWS software development kits (SDKs)**

AWS provides SDKs for many popular technologies and programming languages.
They make it easier for you to call AWS services from within your applications
in that language or technology. For more information about these SDKs, see
[Tools for developing and
managing applications on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

**Amazon RDS API**

This API is the protocol-level interface for Amazon RDS. When using this API, you
must format every HTTPS request correctly and add a valid digital signature to
every request. For more information, see [Amazon RDS API reference](ProgrammingGuide.md "ProgrammingGuide.md").

**Console-to-Code**

With this tool, you can generate code for actions that you perform in the
Amazon RDS console, and use that code in other tools such as AWS CloudFormation. For more
information, see [Use Console-to-Code to generate code for your Amazon Aurora console actions](Using_C2C.md "Using_C2C.md").

**RDS Data API**

RDS Data API (Data API) provides programmatic access to the data in your
Amazon Aurora Serverless databases. With Data API, you can use a secure HTTP
endpoint to run your SQL statements without managing connections. For more
information, see [Using the Amazon RDS Data API](data-api.md "data-api.md").
