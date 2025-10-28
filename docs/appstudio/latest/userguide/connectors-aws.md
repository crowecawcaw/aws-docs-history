# Connect to AWS services using the Other AWS services connector

While App Studio offers some connectors that are specific to certain AWS services, you can also connect to other AWS services
using the **Other AWS services** connector.

###### Note

It is recommended to use the connector specific to the AWS service if it is available.

To connect App Studio with AWS services to enable builders to access and use the service's resources in applications, you must perform
the following steps:

1. [Create an IAM role to give App Studio access to AWS resources](#connectors-aws-iam-role "#connectors-aws-iam-role")
2. [Create an Other AWS services connector](#connectors-aws-create-connector "#connectors-aws-create-connector")

## Create an IAM role to give App Studio access to AWS resources

To use AWS services and resources with App Studio, administrators must create an IAM role to give App Studio
permissions to access the resources. The IAM role controls the scope of resources that builders can access and what operations can
be called against the resources. We recommend creating at least one IAM role per service and policy.

###### To create an IAM role to give App Studio access to AWS resources

1. Sign in to the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam") with a user that has permissions to create IAM roles. We recommend
   using the administrative user created in
   [Create an administrative user for managing AWS resources](setting-up-first-time-admin.md#setting-up-create-admin-user "setting-up-first-time-admin.md#setting-up-create-admin-user").
2. In the navigation pane of the console, choose **Roles** and then choose **Create role**.
3. In **Trusted entity type**, choose **Custom trust policy**.
4. Replace the default policy with the following policy to allow App Studio applications to assume this role in your account.

You must replace the following placeholders in the policy. The values to be used can be found in App Studio, in the **Account settings** page.

    * Replace `111122223333` with the AWS account number of the account used to set up the App Studio instance, listed as
     **AWS account ID** in the account settings in your App Studio instance.
    * Replace `11111111-2222-3333-4444-555555555555` with your App Studio instance ID, listed as **Instance ID**
     in the account settings in your App Studio instance.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/IsAppStudioAccessRole": "true",
 "sts:ExternalId": "`11111111-2222-3333-4444-555555555555`"
 }
 }
 }
 ]
}`

```

Choose **Next**. 5. In **Add permissions**, search and select the policies that grant the appropriate permissions for the role. Choosing the
**+** next to a policy will expand the policy to show the permissions granted by it and choosing the checkbox selects the policy.
For more information about IAM, see the
[IAM User Guide](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md").

Choose **Next**. 6. In **Role details**, provide a name and description. 7. In **Step 3: Add tags**,
choose **Add new tag** to add the following tag to provide App Studio access:

    * **Key:** `IsAppStudioDataAccessRole`
    * **Value:** `true`

8. Choose **Create role** and make note of the generated Amazon Resource Name (ARN), you
   will need it when [creating
   the Other AWS services connector in App Studio](#connectors-aws-create-connector "#connectors-aws-create-connector").

## Create an **Other AWS services** connector

Now that you have your IAM role configured, use that information to create the connector in App Studio that builders
can use to connect their apps to the service and resources.

###### Note

You must have the Admin role in App Studio to create connectors.

###### To connect to AWS services using the **Other AWS services** connector

1. Navigate to App Studio.
2. In the left-side navigation pane, choose **Connectors** in the **Manage** section.
3. Choose **+ Create connector**.
4. Choose **Other AWS services** in the **AWS connectors** section of the supported services list.
5. Configure your AWS service connector by filling out the following fields:
   - **Name:** Provide a name for your connector.
   - **Description:** Provide a description for your connector.
   - **IAM role:** Enter the Amazon Resource Name (ARN) from
     the IAM role that was created in [Create an IAM role to give App Studio access to AWS resources](#connectors-aws-iam-role "#connectors-aws-iam-role").
   - **Service:** Select the AWS service you want to connect to App Studio.
   - **Region:** Select the AWS Region where your AWS resources are located.

6. Choose **Create**. The newly created connector will appear in the connectors list.
