# Move hardcoded secrets to AWS Secrets Manager

If you have plaintext secrets in your code, we recommend that you rotate them and
store them in Secrets Manager. Moving the secret to Secrets Manager solves the problem of the secret being
visible to anyone who sees the code, because going forward, your code retrieves the secret
directly from Secrets Manager. Rotating the secret revokes the current hardcoded secret so that it is
no longer valid.

For database credential secrets, see [Move hardcoded database credentials to AWS Secrets Manager](hardcoded-db-creds.md "hardcoded-db-creds.md").

Before you begin, you need to determine who needs access to the secret. We recommend
using two IAM roles to manage permission to your secret:

- A role that manages the secrets in your organization. For more information,
  see [Secrets Manager administrator permissions](auth-and-access.md#auth-and-access_admin "auth-and-access.md#auth-and-access_admin"). You'll create and
  rotate the secret using this role.
- A role that can use the secret at runtime, for example in this tutorial you
  use `RoleToRetrieveSecretAtRuntime`. Your code assumes this
  role to retrieve the secret. In this tutorial, you grant the role only the
  permission to retrieve one secret value, and you grant permission by using the
  secret's resource policy. For other alternatives, see [Next steps](#hardcoded_step-next "#hardcoded_step-next").

###### Steps:

- [Step 1: Create the secret](#hardcoded_step-1 "#hardcoded_step-1")
- [Step 2: Update your code](#hardcoded_step-2 "#hardcoded_step-2")
- [Step 3: Update the secret](#hardcoded_step-3 "#hardcoded_step-3")
- [Next steps](#hardcoded_step-next "#hardcoded_step-next")

## Step 1: Create the secret

The first step is to copy the existing hardcoded secret into Secrets Manager. If the secret
is related to an AWS resource, store it in the same Region as the resource. Otherwise,
store it in the Region that has the lowest latency for your use case.

###### To create a secret (console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Store a new secret**.
3. On the **Choose secret type** page, do the
   following:
   1. For **Secret type**, choose **Other type
      of secret**.
   2. Enter your secret as **Key/value pairs** or in
      **Plaintext**. Some examples:

   API key
   Enter as key/value pairs:

   `ClientID` :
   `my_client_id`

   `ClientSecret` :
   `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`

   OAuth token
   Enter as plaintext:

   `AKIAI44QH8DHBEXAMPLE`

   Digital certificate
   Enter as plaintext:

   ```
   -----BEGIN CERTIFICATE-----
   *EXAMPLE*
   -----END CERTIFICATE-----
   ```

   Private key
   Enter as plaintext:

   ```
   –--- BEGIN PRIVATE KEY ----
   *EXAMPLE*
   ––-- END PRIVATE KEY –---
   ```

   3. For **Encryption key**, choose
      **aws/secretsmanager** to use the AWS managed key
      for Secrets Manager. There is no cost for using this key. You can also use your
      own customer managed key, for example to [access the secret from
      another AWS account](auth-and-access_examples_cross.md "auth-and-access_examples_cross.md"). For information about the costs of using a customer managed key, see [Pricing](intro.md#asm_pricing "intro.md#asm_pricing").
   4. Choose **Next**.

4. On the **Choose secret type** page, do the
   following:
   1. Enter a descriptive **Secret name** and
      **Description**.
   2. In **Resource permissions**, choose
      **Edit permissions**. Paste the following
      policy, which allows
      `RoleToRetrieveSecretAtRuntime` to
      retrieve the secret, and then choose
      **Save**.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "AWS": "arn:aws:iam::`111122223333`:role/`RoleToRetrieveSecretAtRuntime`"
    },
    "Action": "secretsmanager:GetSecretValue",
    "Resource": "*"
    }
    ]
   }`

   ```

   3. At the bottom of the page, choose
      **Next**.

5. On the **Configure rotation** page, keep rotation off.
   Choose **Next**.
6. On the **Review** page, review your secret details, and
   then choose **Store**.

## Step 2: Update your code

Your code must assume the IAM role
`RoleToRetrieveSecretAtRuntime` to be able to retrieve the
secret. For more information, see [Switching to an IAM
role (AWS API)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-api.md").

Next, you update your code to retrieve the secret from Secrets Manager using the sample code
provided by Secrets Manager.

###### To find the sample code

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On the **Secrets** page, choose your secret.
3. Scroll down to **Sample code**. Choose your programming
   language, and then copy the code snippet.

In your application, remove the hardcoded secret and paste the code snippet.
Depending on your code language, you might need to add a call to the function or method
in the snippet.

Test that your application works as expected with the secret in place of the
hardcoded secret.

## Step 3: Update the secret

The last step is to revoke and update the hardcoded secret. Refer to the source of
the secret to find instructions to revoke and update the secret. For example, you might
need to deactivate the current secret and generate a new secret.

###### To update the secret with the new value

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Choose **Secrets**, and then choose the secret.
3. On the **Secret details** page, scroll down and choose
   **Retrieve secret value**, and then choose
   **Edit**.
4. Update the secret and then choose **Save**.

Next, test that your application works as expected with the new secret.

## Next steps

After you remove a hardcoded secret from your code, some ideas to consider
next:

- To find hardcoded secrets in your Java and Python applications, we recommend
  [Amazon CodeGuru Reviewer](../../../codeguru/latest/reviewer-ug/welcome.md "../../../codeguru/latest/reviewer-ug/welcome.md").
- You can improve performance and reduce costs by caching secrets. For more
  information, see [Get secrets from AWS Secrets Manager](retrieving-secrets.md "retrieving-secrets.md").
- For secrets that you access from multiple Regions, consider replicating your
  secret to improve latency. For more information, see [Replicate AWS Secrets Manager secrets across Regions](replicate-secrets.md "replicate-secrets.md").
- In this tutorial, you granted
  `RoleToRetrieveSecretAtRuntime` only the permission
  to retrieve the secret value. To grant the role more permissions, for example to
  get metadata about the secret or to view a list of secrets, see [Resource-based policies](auth-and-access_resource-policies.md "auth-and-access_resource-policies.md").
- In this tutorial, you granted permission to
  `RoleToRetrieveSecretAtRuntime` by using the
  secret's resource policy. For other ways to grant permission, see [Identity-based policies](auth-and-access_iam-policies.md "auth-and-access_iam-policies.md").
