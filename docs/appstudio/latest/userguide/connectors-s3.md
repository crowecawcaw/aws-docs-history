

# Connect to Amazon Simple Storage Service (Amazon S3)
<a name="connectors-s3"></a>

To connect App Studio with Amazon S3 to enable builders to access and use Amazon S3 resources in applications, perform the following steps:

1. [Step 1: Create and configure Amazon S3 resources](#connectors-s3-create-resources)

1. [Step 2: Create an IAM policy and role with appropriate Amazon S3 permissions](#connectors-s3-iam)

1. [Step 3: Create Amazon S3 connector](#connectors-s3-create-connector)

After you have completed the steps and created the connector with proper permissions, builders can use the connector to create apps that interact with Amazon S3 resources. For more information about interacting with Amazon S3 in App Studio apps, see [Interacting with Amazon Simple Storage Service with components and automations](automations-s3.md).

## Step 1: Create and configure Amazon S3 resources
<a name="connectors-s3-create-resources"></a>

Depending on your app's needs and your existing resources, you may need to create an Amazon S3 bucket for apps to write to and read from. For information about creating Amazon S3 resources, including buckets, see [Getting started with Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html) in the *Amazon Simple Storage Service User Guide*.

To use the [S3 upload](components-reference.md#s3-upload-component) component in your apps, you must add a cross-origin resource sharing (CORS) configuration to any Amazon S3 buckets you want to upload to. The CORS configuration gives App Studio permission to push objects to the bucket. The following procedure details how to add a CORS configuration to an Amazon S3 bucket using the console. For more information about CORS and configuring it, see [Using cross-origin resource sharing (CORS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cors.html) in the *Amazon Simple Storage Service User Guide*.

**To add a CORS configuration to an Amazon S3 bucket in the console**

1. Navigate to your bucket in the [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the **Permissions** tab.

1. In **Cross-origin resource sharing (CORS)**, choose **Edit**.

1. Add the following snippet:

   ```
   [
       {
           "AllowedHeaders": [
               "*"
           ],
           "AllowedMethods": [
               "PUT",
               "POST"
           ],
           "AllowedOrigins": [
               "*"
           ],
           "ExposeHeaders": []
       }
   ]
   ```

1. Choose **Save changes**.

## Step 2: Create an IAM policy and role with appropriate Amazon S3 permissions
<a name="connectors-s3-iam"></a>

To use Amazon S3 resources with App Studio, administrators must create an IAM policy and role to give App Studio permissions to access the resources. The IAM policy controls the scope of data that builders can use and what operations can be called against that data, such as Create, Read, Update, or Delete. The IAM policy is then attached to an IAM role that is used by App Studio.

We recommend creating at least one IAM role per service and policy. For example, if builders are creating two applications backed by different buckets in Amazon S3, an administrator should create two IAM policies and roles, one for each of the buckets.

### Step 2a: Create an IAM policy with appropriate Amazon S3 permissions
<a name="connectors-s3-iam-policy"></a>

The IAM policy that you create and use with App Studio should contain only the minimally necessary permissions on the appropriate resources for the application to follow best security practices.

**To create an IAM policy with appropriate Amazon S3 permissions**

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam) with a user that has permissions to create IAM policies. We recommend using the administrative user created in [Sign up for an AWS account](setting-up-first-time-admin.md#sign-up-for-aws).

1. In the left-side navigation pane, choose **Policies**.

1. Choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Type or paste in a JSON policy document. The following tabs contain example policies for read only and full access to Amazon S3 resources.
**Note**  
The following policies apply to all Amazon S3 resources using the wildcard (`*`). For best security practices, you should replace the wildcard with the Amazon Resource Name (ARN) of the resources, such as buckets or folders, you want to use with App Studio.

------
#### [ Read only ]

   The following policy grants read only access (get and list) to the configured Amazon S3 buckets or folders.

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
         {
            "Sid": "S3ReadOnlyForAppStudio",
            "Effect": "Allow",
            "Action": [
               "s3:GetObject",
               "s3:ListBucket"
            ],
            "Resource": "*"
         }
      ]
   }
   ```

------

------
#### [ Full access ]

   The following policy grants full access (put, get, list, and delete) to the configured Amazon S3 buckets or folders.

------
#### [ JSON ]

****  

   ```
   {
      "Version":"2012-10-17",		 	 	 
      "Statement": [
         {
            "Sid": "S3FullAccessForAppStudio",
            "Effect": "Allow",
            "Action": [
               "s3:PutObject",
               "s3:GetObject",
               "s3:ListBucket",
               "s3:DeleteObject"
            ],
            "Resource": "*"
         }
      ]
   }
   ```

------

------

1. Choose **Next**.

1. On the **Review and create** page, provide a **Policy name**, such as **AWSAppStudioS3FullAccess**, and **Description** (optional).

1. Choose **Create policy** to create the policy.

### Step 2b: Create an IAM role to give App Studio access to Amazon S3 resources
<a name="connectors-s3-iam-role"></a>

To use Amazon S3 resources with App Studio, administrators must create an IAM role to give App Studio permissions to access the resources. The IAM role controls the scope of data that builders can use and what operations can be called against that data, such as Create, Read, Update, or Delete.

We recommend creating at least one IAM role per service and policy.

**To create an IAM role to give App Studio access to Amazon S3 resources**

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

1. In **Add permissions**, search for and select the policy that you created in the previous step (**S3ReadOnlyForAppStudio** or **S3FullAccessForAppStudio**). Choosing the **\+** next to a policy will expand the policy to show the permissions granted by it and choosing the checkbox selects the policy.

   Choose **Next**.

1. On the **Name, review, and create** page, provide a **Role name** and **Description**.

1. In **Step 3: Add tags**, choose **Add new tag** to add the following tag to provide App Studio access:
   + **Key: **`IsAppStudioDataAccessRole`
   + **Value: **`true`

1. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you will need it to create the Amazon S3 connector in App Studio in the next step.

## Step 3: Create Amazon S3 connector
<a name="connectors-s3-create-connector"></a>

Now that you have your Amazon S3 resources and IAM policy and role configured, use that information to create the connector in App Studio that builders can use to connect their apps to Amazon S3.

**Note**  
You must have the Admin role in App Studio to create connectors.

**To create a connector for Amazon S3**

1. Navigate to App Studio.

1. In the left-side navigation pane, choose **Connectors** in the **Manage** section. You will be taken to a page displaying a list of existing connectors with some details about each.

1. Choose **\+ Create connector**.

1. Choose the **Amazon S3** connector.

1. Configure your connector by filling out the following fields:
   + **Name:** Enter a name for your Amazon S3 connector.
   + **Description:** Enter a description for your Amazon S3 connector.
   + **IAM role:** Enter the Amazon Resource Name (ARN) from the IAM role created in [Step 2b: Create an IAM role to give App Studio access to Amazon S3 resources](#connectors-s3-iam-role). For more information about IAM, see the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html).
   + **Region:** Choose the AWS Region where your Amazon S3 resources are located.

1. Choose **Create**.

1. The newly created connector will appear in the **Connectors** list.