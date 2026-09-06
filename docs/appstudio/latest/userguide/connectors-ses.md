

# Connect to Amazon Simple Email Service
<a name="connectors-ses"></a>

To connect App Studio with Amazon SES to enable builders to use it to send email notifications from their apps, you must perform the following steps:

1. [Step 1: Configure Amazon SES resources](#connectors-ses-create-resources)

1. [Step 2: Create an IAM policy and role with appropriate Amazon SES permissions](#connectors-ses-iam-policy-role)

1. [Step 3: Create Amazon SES connector](#connectors-ses-create-connector)

## Step 1: Configure Amazon SES resources
<a name="connectors-ses-create-resources"></a>

If you haven't, you must first configure Amazon SES to use it to send emails. To learn more about setting up Amazon SES, see [Getting started with Amazon Simple Email Service](https://docs.aws.amazon.com/ses/latest/dg/getting-started.html) in the *Amazon Simple Email Service Developer Guide*.

## Step 2: Create an IAM policy and role with appropriate Amazon SES permissions
<a name="connectors-ses-iam-policy-role"></a>

To use Amazon SES resources with App Studio, administrators must create an IAM role to give App Studio permissions to access the resources. The IAM role controls what Amazon SES functions or resources can be used in App Studio apps.

We recommend creating at least one IAM role per service and policy.

### Step 2a: Create an IAM policy with appropriate Amazon SES permissions
<a name="connectors-ses-iam-policy"></a>

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources for the application to follow best security practices.

**To create an IAM policy with appropriate Amazon SES permissions**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam) with a user that has permissions to create IAM policies. We recommend using the administrative user created in [Sign up for an AWS account](setting-up-first-time-admin.md#sign-up-for-aws).

1. In the left-side navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Type or paste in the following JSON policy document.
**Note**  
The following policies apply to all Amazon SES resources using the wildcard (`*`). For best security practices, you should replace the wildcard with the Amazon Resource Name (ARN) of the resources you want to use with App Studio.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "VisualEditor0",
               "Effect": "Allow",
               "Action": "ses:SendEmail",
               "Resource": "*"
           }
       ]
   }
   ```

------

1. Choose **Next**.

1. On the **Review and create** page, provide a **Policy name**, such as **SESForAppStudioPolicy**, and **Description** (optional).

1. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Amazon SES
<a name="connectors-ses-iam-role"></a>

Now, create an IAM role that uses the policy you previously created. App Studio will use this policy to get access to Amazon SES.

**To create an IAM role to give App Studio access to Amazon SES**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam) with a user that has permissions to create IAM roles. We recommend using the administrative user created in [Sign up for an AWS account](setting-up-first-time-admin.md#sign-up-for-aws).

1. In the left-side navigation pane, choose **Roles**

1. Choose **Create role**.

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

1. In **Add permissions**, search for and select the policy that you created in the previous step (**SESForAppStudioPolicy**). Choosing the **\+** next to a policy will expand the policy to show the permissions granted by it and choosing the checkbox selects the policy.

   Choose **Next**.

1. On the **Name, review, and create** page, provide a **Role name** and **Description**.

1. In **Step 3: Add tags**, choose **Add new tag** to add the following tag to provide App Studio access:
   + **Key: **`IsAppStudioDataAccessRole`
   + **Value: **`true`

1. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you will need it when [creating the Amazon SES connector in App Studio](#connectors-ses-create-connector).

## Step 3: Create Amazon SES connector
<a name="connectors-ses-create-connector"></a>

Now that you Amazon SES and an IAM policy and role configured, use that information to create the connector in App Studio that builders can use to use Amazon SES in their apps.

**Note**  
You must have the Admin role in App Studio to create connectors.

**To create a connector for Amazon SES**

1. Navigate to App Studio.

1. In the left-side navigation pane, choose **Connectors** in the **Manage** section. You will be taken to a page displaying a list of existing connectors with some details about each.

1. Choose **\+ Create connector**.

1. Choose **Other AWS Services** from the list of connector types.

1. Configure your connector by filling out the following fields:
   + **Name:** Enter a name for your Amazon SES connector.
   + **Description:** Enter a description for your Amazon SES connector.
   + **IAM role:** Enter the Amazon Resource Name (ARN) from the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Amazon SES](#connectors-ses-iam-role). For more information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
   + **Service:** Choose **Simple Email Service**.
   + **Region:** Choose the AWS Region where your Amazon SES resources are located.

1. Choose **Create**.

1. The newly created connector will appear in the **Connectors** list.