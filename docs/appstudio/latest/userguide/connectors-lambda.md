

# Connect to AWS Lambda
<a name="connectors-lambda"></a>

To connect App Studio with Lambda to enable builders to access and use Lambda resources in applications, you must perform the following steps:

1. [Step 1: Create and configure Lambda functions](#connectors-lambda-create-resources)

1. [Step 2: Create an IAM role to give App Studio access to Lambda resources](#connectors-lambda-iam-role)

1. [Step 3: Create Lambda connector](#connectors-lambda-create-connector)

## Step 1: Create and configure Lambda functions
<a name="connectors-lambda-create-resources"></a>

If you don't have existing Lambda functions, you must first create them. To learn more about creating Lambda functions, see the [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/).

## Step 2: Create an IAM role to give App Studio access to Lambda resources
<a name="connectors-lambda-iam-role"></a>

To use Lambda resources with App Studio, administrators must create an IAM role to give App Studio permissions to access the resources. The IAM role controls the resources or operations applications can access from Lambda.

We recommend creating at least one IAM role per service and policy.

**To create an IAM role to give App Studio access to Lambda resources**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam) with a user that has permissions to create IAM roles. We recommend using the administrative user created in [Sign up for an AWS account](setting-up-first-time-admin.md#sign-up-for-aws).

1. In the navigation pane of the console, choose **Roles** and then choose **Create role**.

1. In **Trusted entity type**, choose **Custom trust policy**.

1. Replace the default policy with the following policy to allow App Studio applications to assume this role in your account.

   You must replace the following placeholders in the policy. The values to be used can be found in App Studio, in the **Account settings** page.
   + Replace {{111122223333}} with the AWS account number of the account used to set up the App Studio instance, listed as **AWS account ID** in the account settings in your App Studio instance.
   + Replace {{11111111-2222-3333-4444-555555555555}} with your App Studio instance ID, listed as **Instance ID** in the account settings in your App Studio instance.

------
#### [ JSON ]

****  

   ```
   { 
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           { 
               "Effect": "Allow",
               "Principal": { 
                   "AWS": "arn:aws:iam::{{111122223333}}:root"
               }, 
               "Action": "sts:AssumeRole",
               "Condition": {
                   "StringEquals": {
                           "aws:PrincipalTag/IsAppStudioAccessRole": "true",
                           "sts:ExternalId": "{{11111111-2222-3333-4444-555555555555}}"
                   }
               }
           } 
       ]
   }
   ```

------

   Choose **Next**.

1. In **Add permissions**, search for and select the policies that grant the appropriate permissions for the role. Choosing the **\+** next to a policy will expand the policy to show the permissions granted by it and choosing the checkbox selects the policy. For Lambda, you may consider adding the `AWSLambdaRole` policy, which grants permissions to invoke Lambda functions.

   For more information about using IAM policies with Lambda, including a list of managed policies and their descriptions, see [Identity and Access Management for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-iam.html) in the *AWS Lambda Developer Guide*.

   Choose **Next**.

1. On the **Name, review, and create** page, provide a **Role name** and **Description**.

1. In **Step 3: Add tags**, choose **Add new tag** to add the following tag to provide App Studio access:
   + **Key: **`IsAppStudioDataAccessRole`
   + **Value: **`true`

1. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you will need it when [creating the Lambda connector in App Studio](#connectors-lambda-create-connector).

## Step 3: Create Lambda connector
<a name="connectors-lambda-create-connector"></a>

Now that you have your Lambda resources and IAM policy and role configured, use that information to create the connector in App Studio that builders can use to connect their apps to Lambda.

**Note**  
You must have the Admin role in App Studio to create connectors.

**To create a connector for Lambda**

1. Navigate to App Studio.

1. In the left-side navigation pane, choose **Connectors** in the **Manage** section. You will be taken to a page displaying a list of existing connectors with some details about each.

1. Choose **\+ Create connector**.

1. Choose **Other AWS Services** from the list of connector types.

1. Configure your connector by filling out the following fields:
   + **Name:** Enter a name for your Lambda connector.
   + **Description:** Enter a description for your Lambda connector.
   + **IAM role:** Enter the Amazon Resource Name (ARN) from the IAM role created in [Step 2: Create an IAM role to give App Studio access to Lambda resources](#connectors-lambda-iam-role). For more information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
   + **Service:** Choose **Lambda**.
   + **Region:** Choose the AWS Region where your Lambda resources are located.

1. Choose **Create**.

1. The newly created connector will appear in the **Connectors** list.