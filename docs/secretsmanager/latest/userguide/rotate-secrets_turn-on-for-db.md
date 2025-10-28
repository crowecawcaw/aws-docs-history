# Set up automatic rotation for Amazon RDS, Amazon Aurora, Amazon Redshift, or Amazon DocumentDB secrets

This tutorial describes how to set up [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md") for database secrets. Rotation is the process of periodically updating a secret. When you rotate a secret, you update the
credentials in both the secret and the database. In Secrets Manager, you can set up automatic rotation for your
database secrets.

To set up rotation using the console, you need to first choose a rotation strategy. Then you
configure the secret for rotation, which creates a Lambda rotation function if you don't already have one.
The console also sets permissions for the Lambda function execution role. The last step is to make sure that
the Lambda rotation function can access both Secrets Manager and your database through the network.

###### Warning

To turn on automatic rotation, you must have permission to create an IAM execution role for the Lambda rotation function
and attach a permission policy to it. You need both `iam:CreateRole` and
`iam:AttachRolePolicy` permissions. Granting these permissions allows an identity to grant
themselves any permissions.

###### Steps:

- [Step 1: Choose a rotation strategy and (optionally) create a superuser secret](#rotate-secrets_turn-on-for-db_step1 "#rotate-secrets_turn-on-for-db_step1")
- [Step 2: Configure rotation and create a rotation function](#rotate-secrets_turn-on-for-db_step2 "#rotate-secrets_turn-on-for-db_step2")
- [Step 3: (Optional) Set additional permissions conditions on the rotation function](#rotate-secrets_turn-on-for-db_step3 "#rotate-secrets_turn-on-for-db_step3")
- [Step 4: Set up network access for the rotation function](#rotate-secrets_turn-on-for-db_step4 "#rotate-secrets_turn-on-for-db_step4")
- [Next steps](#rotate-secrets_turn-on-for-db_stepnext "#rotate-secrets_turn-on-for-db_stepnext")

## Step 1: Choose a rotation strategy and (optionally) create a superuser secret

For information about the strategies offered by Secrets Manager, see [Lambda function rotation strategies](rotation-strategy.md "rotation-strategy.md").

If you choose the _alternating users strategy_, you must [Create secrets](create_secret.md "create_secret.md") and store database superuser credentials in it. You need a secret with superuser credentials because rotation clones the first user, and most users do not have that permission. Note that Amazon RDS Proxy does not support the alternating users strategy.

## Step 2: Configure rotation and create a rotation function

###### To turn on rotation for an Amazon RDS, Amazon DocumentDB, or Amazon Redshift secret

1.  Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2.  On the **Secrets** page, choose your secret.
3.  On the **Secret details** page, in the **Rotation
    configuration** section, choose **Edit rotation**.
4.  In the **Edit rotation configuration** dialog box, do the
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

    If rotation fails, for example because Steps 3 and 4 are not yet completed, Secrets Manager retries the rotation process multiple times. 5. Under **Rotation function**, do one of the following:

        * Choose **Create a new Lambda
         function** and enter a name for your new function.
         Secrets Manager adds `SecretsManager` to the beginning of the
         function name. Secrets Manager creates the function based on the appropriate
         [template](reference_available-rotation-templates.md "reference_available-rotation-templates.md") and
         sets the necessary [permissions](rotating-secrets-required-permissions-function.md "rotating-secrets-required-permissions-function.md")
         for the Lambda execution role.
        * Choose **Use an existing Lambda function** to
         reuse a rotation function you used for another secret. The rotation
         functions listed under **Recommended VPC configurations** have the
         same VPC and security group as the database, which helps the function access the database.

    6. For **Rotation strategy**,
       choose the **Single user** or **Alternating users** strategy. For more information, see [Step 1: Choose a rotation strategy and (optionally) create a superuser secret](#rotate-secrets_turn-on-for-db_step1 "#rotate-secrets_turn-on-for-db_step1").

5.  Choose **Save**.

## Step 3: (Optional) Set additional permissions conditions on the rotation function

In the resource policy for your rotation function, we recommend that you include the context key [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") to help prevent
Lambda from being used as a [confused
deputy](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"). For some AWS services, to avoid the confused deputy scenario, AWS recommends
that you use both the [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn")
and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount")
global condition keys. However, if you include the `aws:SourceArn` condition in your
rotation function policy, the rotation function can only be used to rotate the secret specified by
that ARN. We recommend that you include only the context key `aws:SourceAccount` so that you
can use the rotation function for multiple secrets.

###### To update your rotation function resource policy

1. In the Secrets Manager console, choose your secret, and then on the details page, under
   **Rotation configuration**, choose the Lambda rotation function. The Lambda console
   opens.
2. Follow the instructions at [Using
   resource-based policies for Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") to add a `aws:sourceAccount` condition.

```
"Condition": {
    "StringEquals": {
        "AWS:SourceAccount": "`123456789012`"
    }
},
```

If the secret is encrypted with a KMS key other than the AWS managed key
`aws/secretsmanager`, Secrets Manager grants the Lambda execution role permission to use the key. You can use the [SecretARN encryption context](security-encryption.md#security-encryption-encryption-context "security-encryption.md#security-encryption-encryption-context") to limit the use of the decrypt function, so the rotation function role only has access to decrypt the secret it is responsible for rotating.

###### To update your rotation function execution role

1. From the Lambda rotation function, choose **Configuration**, and then under **Execution role**, choose the **Role name**.
2. Follow the instructions at [Modifying a role permissions policy](../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy "../../../IAM/latest/UserGuide/roles-managingrole-editing-console.md#roles-modify_permissions-policy") to add a `kms:EncryptionContext:SecretARN` condition.

```
"Condition": {
    "StringEquals": {
        "kms:EncryptionContext:SecretARN": "`SecretARN`"
    }
},
```

## Step 4: Set up network access for the rotation function

For more information, see [Network access for AWS Lambda rotation function](rotation-function-network-access.md "rotation-function-network-access.md").

## Next steps

See [Troubleshoot AWS Secrets Manager rotation](troubleshoot_rotation.md "troubleshoot_rotation.md").
