# Setting up SRT password

encryption using AWS Elemental MediaConnect

Before you can create a flow with an encrypted source or an output that uses
SRT password encryption, you must perform the following steps:

**[Step 1](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key")** – Store your SRT password as a secret
in AWS Secrets Manager.

**[Step
2](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy")** – Create an IAM policy that allows
AWS Elemental MediaConnect to read the secret that you stored in AWS Secrets Manager.

**[Step
3](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-role")** – Create an IAM role and attach the policy that
you created in step 2. Next, set up AWS Elemental MediaConnect as a trusted entity that
is allowed to assume this role and make requests on behalf of your
account.

## Step 1: Store your

encryption password in AWS Secrets Manager

To use SRT password encryption to encrypt your AWS Elemental MediaConnect content,
you must use AWS Secrets Manager to create a secret that stores the password. You must
create the secret, and the resource (source or output) that uses the secret
in the same AWS account. You can’t share secrets across accounts.

###### Note

If you use two flows to distribute video from one AWS Region to
another, you must create two secrets (one secret in each Region).

If you are creating a new SRT password to encrypt an output, we recommend
the following password policy:

- Minimum password length of 10 characters and a maximum length of
  80 characters
- Minimum of three of the following mix of character types:
  uppercase, lowercase, numbers, and `! @ # $ % ^ & * (
) _ + - = [ ] { } | '` symbols
- Not be identical to your AWS account name or email
  address

###### To store a password in Secrets Manager

1. Sign in to the AWS Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. On the **Store a new secret** page, for
   **Select secret type**, choose **Other
   type of secrets**.
3. For **Key/value pairs**, choose
   **Plaintext**.
4. Clear any text in the box and replace it with only the **value** of the SRT password.
5. For **Encryption key**, keep the default set to
   **aws/secretsmanager**.
6. Choose **Next**.
7. For **Secret name**, specify a name for your
   secret that will help you identify it later. For example,
   `2018-12-01_baseball-game-source`.
8. Choose **Next**.
9. For the **Configure automatic rotation** section,
   leave **Automatic rotation** off.
10. Choose **Next**, and then choose
    **Store**. On the next screen, select the name
    of the secret you created.

The details page for your new secret appears, showing information
such as the secret ARN. 11. Make a note of the secret ARN from Secrets Manager. You will need this
information in the next procedure.

## Step 2:

Create an IAM policy to allow AWS Elemental MediaConnect to access your
secret

In [step 1](encryption-static-key-set-up.md#encryption-static-key-set-up-store-key "encryption-static-key-set-up.md#encryption-static-key-set-up-store-key"),
you created a secret and stored it in AWS Secrets Manager. In this step, you create an
IAM policy that allows AWS Elemental MediaConnect to read the secret that you
stored.

###### To create an IAM policy that allows MediaConnect to access your

secret

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Policies**.
3. Choose **Create policy**, and then choose the
   **JSON** tab.
4. Enter a policy that uses the following format:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": [
 "arn:aws:secretsmanager:`us-west-2:111122223333`:secret:`aes256-7g8H9i`"
 ]
 }
 ]
}`

```

In the `Resource` section, each line represents the ARN
of a different secret that you created. Enter the secret ARN from
the previous procedure. Choose **Next:
Tags**. 5. Choose **Next: Review**. 6. For **Name**, enter a name for your policy such
as `SecretsManagerForMediaConnect`. 7. Choose **Create policy**.

## Step 3:

Create an IAM role with a trusted relationship

In [step
2](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy"), you created an IAM policy that allows read access to the
secret that you stored in AWS Secrets Manager. In this step, you create an IAM role
and assign the policy to that role. Then you define AWS Elemental MediaConnect as a
trusted entity that can assume the role. This allows MediaConnect to have
read access to your secret.

###### To create a role with a trusted relationship

1. In the navigation pane of the IAM console, choose
   **Roles**.
2. On the **Role** page, choose **Create
   role**.
3. On the **Create role** page, for **Select
   type of trusted entity**, choose **AWS
   service** (the default).
4. For **Choose the service that will use this
   role**, choose **EC2**.

You choose EC2 because AWS Elemental MediaConnect is not currently included
in this list. Choosing EC2 lets you create a role. In a later step,
you change this role to include MediaConnect instead of EC2. 5. Choose **Next: Permissions**. 6. For **Attach permissions policies**, enter the
name of the policy that you created in [step
2](encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy "encryption-static-key-set-up.md#encryption-static-key-set-up-create-iam-policy"), such as
`SecretsManagerForMediaConnect`. 7. For **SecretsManagerForMediaConnect**, select the
check box, and then choose **Next**. 8. For **Role name**, enter a name. We highly
recommend that you don't use the name
`MediaConnectAccessRole` because it is reserved.
Instead, use a name that includes `MediaConnect` and
describes this role's purpose, such as
`MediaConnect-ASM`. 9. For **Role description**, replace the default
text with a description that will help you remember the purpose of
this role. For example, `Allows MediaConnect to view
 secrets stored in AWS Secrets Manager.` 10. Choose **Create role**. 11. In the confirmation message that appears across the top of your
page, choose the name of the role that you just created. 12. Choose **Trust relationships**, and then choose
**Edit trust policy**. 13. For **Edit trust policy**, change
`ec2.amazonaws.com` to
`mediaconnect.amazonaws.com`.

The policy document should now look like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "mediaconnect.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

14. Choose **Update policy**.
15. On the **Summary** page, make a note of the value
    for **Role ARN**. It looks like this:
    `arn:aws:iam::111122223333:role/MediaConnectASM`.
