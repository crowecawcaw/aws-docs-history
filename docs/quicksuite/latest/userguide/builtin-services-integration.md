# AWS service action connectors

With AWS service action connectors in Amazon Quick Suite, you can create action connectors
that interact directly with AWS services like Amazon Bedrock, Amazon Textract, and
Amazon Comprehend. These connectors enable automated workflows that leverage AWS AI and
machine learning capabilities.

## What you can do

AWS service action connectors enable you to integrate powerful AWS capabilities
into your automated workflows. For example, you can use Amazon Bedrock to
generate content with foundation models, Amazon Textract to extract text and data from
documents, or Amazon Comprehend to analyze sentiment and extract insights from
text. These action connectors allow you to build sophisticated automation workflows that
combine multiple AWS services for document processing, content generation, and data
analysis—all while maintaining security through IAM role-based authentication.

###### Note

AWS services action connectors can only be used with Amazon Quick Automate because they
require an IAM identity for authentication. These connectors are created through the
admin console and provide direct access to AWS service APIs.

## Supported AWS services

Amazon Quick Suite supports the following AWS services for action connectors:

- **Amazon Bedrock Agent** - Invoke Bedrock agents for complex AI workflows.
- **Amazon Bedrock Runtime** - Access foundation models for text generation and conversation.
- **Amazon Bedrock Data Automation** - Automate data processing workflows with AI.
- **Amazon Comprehend** - Analyze text for sentiment, entities, and key phrases.
- **Amazon Comprehend Medical** - Extract medical information from healthcare text.
- **Amazon Textract** - Extract text and data from documents and images.
- **Amazon S3** - Manage objects and buckets in S3.

## Before you begin

Before you set up an AWS service action connectors, make sure you have the
following:

- AWS account with access to the desired AWS services.
- IAM role with appropriate permissions for the AWS services you want to use.
- Amazon Quick Suite Admin access to create action connectors.
- Amazon Quick Automate access to use the action connectors in workflows.

## Prepare IAM role and permissions

Before setting up the action connectors in Amazon Quick Suite, prepare your IAM role with
the necessary permissions for the AWS services you want to use.

### Required IAM permissions

Configure your IAM role with the appropriate permissions based on the AWS
services you plan to use. Make sure your IAM role includes a trust policy that
allows Amazon Quick Suite to assume the role for executing actions.

### IAM Role for Resource Access

First, you will need to create an IAM role that will be used by Amazon Quick Suite to call the AWS service needed in your Amazon Quick Automate workflow.

1. Login to the AWS Console of the AWS account where the Amazon Quick Suite subscription resides.
2. Open IAM and create a new IAM role.
3. Give it all the permissions for the AWS service you want to invoke via action connectors. For example, you can assign a managed policy like `AmazonS3FullAccess` if you need to invoke Amazon S3.
4. In the trust relationship, give the assume role permission to `quicksight.amazonaws.com`. This allows Amazon Quick Suite to assume this role and call Amazon S3/Amazon Textract/etc on your behalf.
5. Once the Customer Role is created, take a note of the IAM role ARN.

Example trust policy:

###### Note

For pre-prod stages, you will also have to include `"quicksight-test.amazonaws.com"` in the `"Service"` array.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "quicksight.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

## Create AWS services action

connector

After preparing your IAM role and permissions, follow these steps to create your AWS
services action connector:

1. In the Amazon Quick Suite console, choose the user icon in the upper right corner.
2. From the dropdown menu, select **Manage Quick Suite**. This takes you to the Admin console.
3. In the left navigation panel, select **AWS actions**.
4. Choose **New Action**.
5. Choose one of the supported AWS services:
   - Bedrock Agent
   - Bedrock Runtime
   - Bedrock Data Automation
   - Comprehend
   - Comprehend Medical
   - Textract
   - Amazon S3

6. Select **Next**.
7. Review all of the supported actions in the list for your selected service.
8. Select **Next**.
9. Customize the connection details:
   - **Name** - Enter a descriptive name for your action connector.
   - **Description** - Describe the purpose of this action connector.
   - **Role ARN** - Enter the ARN of the IAM role that provides the proper permissions for the AWS service.

10. Select **Next**.
11. Add users you want to share the action connector with.
12. Select **Next** to finish creating the action connector.

After creating the action connector, it becomes available for use in Amazon Quick Automate workflows. The connector will be found in Actions tab under integration.

## Use action connectors in workflows

After setting up your AWS services action connector, you can use it in Amazon Quick Automate
workflows.

### Access in Amazon Quick Automate

To use your AWS action connector in Amazon Quick Automate:

1. Open Amazon Quick Automate and go to Projects.
2. Click Manage groups and select your group.
3. In the Assets sections, click **Add** → **Actions**.
4. Select the Action you created earlier and Add to the automation group.
5. Go to the automation in the group and your action will be available for use.
6. In the Actions panel, look for your AWS service action connector.
7. Drag the desired action into your workflow.
8. Configure the action parameters as needed for your use case.
9. Test and save your workflow.

### Manage existing connectors

You can modify your existing AWS action connectors:

1. In the Admin console, choose **AWS actions**.
2. Select your action connector from the list.
3. Choose the actions menu, then choose **Edit**.
4. Update your configuration settings as needed and choose **Save**.

###### Note

AWS services action connectors use IAM role-based authentication and can only
be used within Amazon Quick Automate workflows. Make sure your IAM role has the minimum
required permissions for the AWS services you plan to use.
