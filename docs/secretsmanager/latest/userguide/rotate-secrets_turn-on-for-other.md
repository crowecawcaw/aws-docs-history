# Set up automatic rotation for

non-database AWS Secrets Manager secrets

This tutorial describes how to set up [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md") for
non-database secrets. Rotation is the process of periodically updating a secret. When you
rotate a secret, you update the credentials in both the secret and the database or service
that the secret is for.

For database secrets, see [Automatic rotation for database secrets (console)](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md").

###### Warning

To turn on automatic rotation, you must have permission to create an IAM execution role for the Lambda rotation function
and attach a permission policy to it. You need both `iam:CreateRole` and
`iam:AttachRolePolicy` permissions. Granting these permissions allows an identity to grant
themselves any permissions.

###### Steps:

- [Step 1: Create a generic
  rotation function](#rotate-secrets_turn-on-for-other_create "#rotate-secrets_turn-on-for-other_create")
- [Step 2: Write the rotation
  function code](#rotate-secrets_turn-on-for-other_write "#rotate-secrets_turn-on-for-other_write")
- [Step 3: Configure the
  secret for rotation](#rotate-secrets_turn-on-for-other_configure "#rotate-secrets_turn-on-for-other_configure")
- [Step 4: Allow the rotation
  function to access Secrets Manager and your database or service](#rotate-secrets_turn-on-for-other_perms "#rotate-secrets_turn-on-for-other_perms")
- [Step 5: Allow Secrets Manager to invoke
  the rotation function](#rotate-secrets_turn-on-for-other_perms2 "#rotate-secrets_turn-on-for-other_perms2")
- [Step 6: Set up network access for the rotation function](#rotate-secrets_turn-on-for-other_network "#rotate-secrets_turn-on-for-other_network")
- [Next steps](#rotate-secrets_turn-on-for-other_stepnext "#rotate-secrets_turn-on-for-other_stepnext")

## Step 1: Create a generic

rotation function

To begin, create a Lambda rotation function. It will not have the code in it to rotate
your secret, so you'll write that in a later step. For information about how a rotation
function works, see [Lambda rotation functions](rotate-secrets_lambda-functions.md "rotate-secrets_lambda-functions.md").

In supported Regions, you can use AWS Serverless Application Repository to create the function from a template. For a
list of supported Regions, see [AWS Serverless Application Repository FAQs](https://aws.amazon.com/serverless/serverlessrepo/faqs/ "https://aws.amazon.com/serverless/serverlessrepo/faqs/"). In other Regions, you
create the function from scratch and copy the template code into the function.

###### To create a generic rotation function

1. To determine whether AWS Serverless Application Repository is supported in your Region, see [AWS Serverless Application Repository
   endpoints and quotas](../../../general/latest/gr/serverlessrepo.md "../../../general/latest/gr/serverlessrepo.md") in the _AWS General
   Reference_.
2. Do one of the following:
   - If AWS Serverless Application Repository is supported in your Region:
     1. In the Lambda console, choose **Applications**
        and then choose **Create application**.
     2. On the **Create application** page, choose
        the **Serverless application** tab.
     3. In the search box under **Public
        applications**, enter
        `SecretsManagerRotationTemplate`.
     4. Select **Show apps that create custom IAM roles or
        resource policies**.
     5. Choose the **SecretsManagerRotationTemplate**
        tile.
     6. On the **Review, configure and deploy** page,
        in the **Application settings** tile, fill in
        the required fields.
        - For **endpoint**, enter the endpoint
          for your Region, including
          `https://`. For a list of
          endpoints, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").
        - To put the Lambda function in a VPC, include
          **vpcSecurityGroupIds** and
          **vpcSubnetIds**.

     7. Choose **Deploy**.

   - If AWS Serverless Application Repository isn't supported in your Region:
     1. In the Lambda console, choose **Functions** and then choose **Create function**.
     2. On the **Create function** page, do the following:
        1. Choose **Author from scratch**.
        2. For **Function name**, enter a name for your rotation function.
        3. For **Runtime**, choose **Python 3.10**.
        4. Choose **Create function**.

## Step 2: Write the rotation

function code

In this step, you write the code that updates the secret and the service or database
that the secret is for. For information about what a rotation function does, including
tips on writing your own rotation function, see [Lambda rotation functions](rotate-secrets_lambda-functions.md "rotate-secrets_lambda-functions.md"). You can also use the [Rotation function
templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md") as reference.

## Step 3: Configure the

secret for rotation

In this step, you set a rotation schedule for your secret and connect the rotation
function to the secret.

###### To configure rotation and create an empty rotation function

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On the **Secrets** page, choose your secret.
3. On the **Secret details** page, in the **Rotation
   configuration** section, choose **Edit rotation**. In
   the **Edit rotation configuration** dialog box, do the
   following:
   1. Turn on **Automatic rotation**.
   2. Under **Rotation schedule**, enter your schedule in UTC
      time zone in either the **Schedule expression builder**
      or as a **Schedule expression**. Secrets Manager stores your schedule as a
      `rate()` or `cron()`
      expression. The rotation window automatically starts at midnight
      unless you specify a **Start time**. You can rotate a secret as often as every four hours. For more
      information, see [Rotation schedules](rotate-secrets_schedule.md "rotate-secrets_schedule.md").
   3. (Optional) For **Window duration**, choose the length of
      the window during which you want Secrets Manager to rotate your secret, for example
      `3h` for a three hour window. The window must not
      extend into the next rotation window. If you don't specify **Window
      duration**, for a rotation schedule in hours, the
      window automatically closes after one hour. For a rotation schedule in days, the
      window automatically closes at the end of the day.
   4. (Optional) Choose **Rotate immediately when the secret is
      stored** to rotate your secret when you save your
      changes. If you clear the checkbox, then the first rotation will
      begin on the schedule you set.
   5. Under **Rotation function**, choose the Lambda
      function you created in Step 1.
   6. Choose **Save**.

## Step 4: Allow the rotation

function to access Secrets Manager and your database or service

The Lambda rotation function needs permission to access the secret in Secrets Manager, and it
needs permission to access your database or service. In this step, you grant these
permissions to the Lambda execution role. If the secret is encrypted with a KMS key other than the AWS managed key
`aws/secretsmanager`, then you need to grant the Lambda execution role permission to use the key. You can use the [SecretARN encryption context](security-encryption.md#security-encryption-encryption-context "security-encryption.md#security-encryption-encryption-context") to limit the use of the decrypt function, so the rotation function role only has access to decrypt the secret it is responsible for rotating. For policy examples,
see [Permissions for
rotation](rotating-secrets-required-permissions-function.md "rotating-secrets-required-permissions-function.md").

For instructions, see [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in
the _AWS Lambda Developer Guide_.

## Step 5: Allow Secrets Manager to invoke

the rotation function

To allow Secrets Manager to invoke the rotation function on the rotation schedule you set up,
you need to grant `lambda:InvokeFunction` permission to the Secrets Manager service
principal in the resource policy of the Lambda function.

In the resource policy for your rotation function, we recommend that you include the context key [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") to help prevent
Lambda from being used as a [confused
deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). For some AWS services, to avoid the confused deputy scenario, AWS recommends
that you use both the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn")
and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount")
global condition keys. However, if you include the `aws:SourceArn` condition in your
rotation function policy, the rotation function can only be used to rotate the secret specified by
that ARN. We recommend that you include only the context key `aws:SourceAccount` so that you
can use the rotation function for multiple secrets.

To attach a resource policy to a Lambda function, see [Using resource-based policies
for Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md").

The following policy allows Secrets Manager to invoke a Lambda function.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "default",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "secretsmanager.amazonaws.com"
 },
 "Action": "lambda:InvokeFunction",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`123456789012`"
 }
 },
 "Resource": "arn:aws:lambda:`us-east-1`:`123456789012`:function:`function-name`"
 }
 ]
}`

```

## Step 6: Set up network access for the rotation function

In this step, you allow the rotation function to connect to both Secrets Manager and the service or database the secret is for. The rotation function must have access to both to be able to rotate the secret. See [Network access for AWS Lambda rotation function](rotation-function-network-access.md "rotation-function-network-access.md").

## Next steps

When you configured rotation in Step 3, you set a schedule for rotating the secret. If
rotation fails when it is scheduled, Secrets Manager will attempt the rotation multiple times. You
can also start a rotation immediately by following the instructions in [Rotate a secret immediately](rotate-secrets_now.md "rotate-secrets_now.md").

If rotation fails, see [Troubleshoot rotation](troubleshoot_rotation.md "troubleshoot_rotation.md").
