# Set up automatic rotation using the AWS CLI

This tutorial describes how to set up [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md") by using the AWS CLI. When you rotate a secret, you update the
credentials in both the secret and the database or service that the secret is for.

You can also set up rotation using the console. For database secrets, see [Automatic rotation for database secrets (console)](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md"). For all other types of secrets, see [Automatic rotation for
non-database secrets (console)](rotate-secrets_turn-on-for-other.md "rotate-secrets_turn-on-for-other.md").

To set up rotation using the AWS CLI, if you are rotating a database secret, you first need to choose a rotation strategy. If you choose the alternating users strategy, you must store a separate secret with credentials for a database superuser. Next, you write the rotation function code. Secrets Manager provides templates you can base your function on. Then you create a Lambda function with your code and set permissions for both the Lambda function and the Lambda execution role. The next step is to make sure that the Lambda function can access both Secrets Manager and your database or service through the network. Finally, you configure the secret for rotation.

###### Steps:

- [Prerequisite for database secrets: Choose a
  rotation strategy](#rotate-secrets_turn-on-cli_step1 "#rotate-secrets_turn-on-cli_step1")
- [Step 1: Write the rotation function
  code](#rotate-secrets_turn-on-cli_write "#rotate-secrets_turn-on-cli_write")
- [Step 2: Create the Lambda function](#w21aac21b9c25c15 "#w21aac21b9c25c15")
- [Step 3: Set up network access](#w21aac21b9c25c17 "#w21aac21b9c25c17")
- [Step 4: Configure the secret for rotation](#w21aac21b9c25c19 "#w21aac21b9c25c19")
- [Next steps](#w21aac21b9c25c21 "#w21aac21b9c25c21")

## Prerequisite for database secrets: Choose a

rotation strategy

For information about the strategies offered by Secrets Manager, see [Lambda function rotation strategies](rotation-strategy.md "rotation-strategy.md").

### Option 1: Single user strategy

If you choose the _single user strategy_, you can continue with Step

1.

### Option 2: Alternating users strategy

If you choose the _alternating users strategy_, you must:

- [Create a secret](create_secret.md#create_secret_cli "create_secret.md#create_secret_cli") and store database
  superuser credentials in it. You need a secret with superuser credentials because
  alternating users rotation clones the first user, and most users do not have that
  permission.
- Add the ARN of the superuser secret to the original secret. For more information,
  see [JSON structure of AWS Secrets Manager secrets](reference_secret_json_structure.md "reference_secret_json_structure.md") .

Note that Amazon RDS Proxy does not support the alternating users strategy.

## Step 1: Write the rotation function

code

To rotate a secret, you need a rotation function. A rotation function is a Lambda function that Secrets Manager calls to rotate your secret. For more information, see [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md"). In this step, you write the code that updates the secret and the service or database that the secret is for.

Secrets Manager provides templates for Amazon RDS, Amazon Aurora, Amazon Redshift, and Amazon DocumentDB database secrets in [Rotation function
templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md").

###### To write the rotation function code

1. Do one of the following:
   - Check the list of [rotation function templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md"). If there is one that matches your service and rotation strategy, copy the code.
   - For other types of secrets, you write your own rotation function. For instructions, see [Lambda rotation functions](rotate-secrets_lambda-functions.md "rotate-secrets_lambda-functions.md").

2. Save the file in a ZIP file `my-function.zip` along with any required dependencies.

## Step 2: Create the Lambda function

In this step, you create the Lambda function using the ZIP file you created in Step 1. You also set the [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md"), which is the role that Lambda assumes when the function is invoked.

###### To create a Lambda rotation function and execution role

1. Create a trust policy for the Lambda execution role and save it as a JSON file. For examples and more information, see [Lambda rotation function
   execution role permissions for AWS Secrets Manager](rotating-secrets-required-permissions-function.md "rotating-secrets-required-permissions-function.md"). The policy must:
   - Allow the role to call Secrets Manager operations on the secret.
   - Allow the role to call the service that the secret is for, for example, to create a new password.

2. Create the Lambda execution role and apply the trust policy you created in the previous step by calling [`iam create-role`](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md").

```
aws iam create-role \
    --role-name `rotation-lambda-role` \
    --assume-role-policy-document file://`trust-policy.json`
```

3. Create the Lambda function from the ZIP file by calling [`lambda create-function`](../../../cli/latest/reference/lambda/create-function.md "../../../cli/latest/reference/lambda/create-function.md").

```
aws lambda create-function \
  --function-name my-rotation-function \
  --runtime python3.7 \
  --zip-file fileb://`my-function.zip` \
  --handler .handler \
  --role arn:aws:iam::`123456789012`:role/service-role/`rotation-lambda-role`
```

4. Set a resource policy on the Lambda function to allow Secrets Manager to invoke it by calling [`lambda add-permission`](../../../cli/latest/reference/lambda/add-permission.md "../../../cli/latest/reference/lambda/add-permission.md").

```
aws lambda add-permission \
  --function-name `my-rotation-function` \
  --action lambda:InvokeFunction \
  --statement-id SecretsManager \
  --principal secretsmanager.amazonaws.com \
  --source-account `123456789012`
```

## Step 3: Set up network access

For more information, see [Network access for AWS Lambda rotation function](rotation-function-network-access.md "rotation-function-network-access.md").

## Step 4: Configure the secret for rotation

To turn on automatic rotation for your secret, call [`rotate-secret`](../../../cli/latest/reference/secretsmanager/rotate-secret.md "../../../cli/latest/reference/secretsmanager/rotate-secret.md"). You can set a rotation schedule
with a `cron()` or `rate()` schedule expression, and you can
set a rotation window duration. For more information, see [Rotation schedules](rotate-secrets_schedule.md "rotate-secrets_schedule.md").

```
aws secretsmanager rotate-secret \
    --secret-id MySecret \
    --rotation-lambda-arn arn:aws:lambda:`Region`:`123456789012`:function:`my-rotation-function` \
    --rotation-rules "{\"ScheduleExpression\": \"`cron(0 16 1,15 * ? *)`\", \"Duration\": \"`2h`\"}"
```

## Next steps

See [Troubleshoot AWS Secrets Manager rotation](troubleshoot_rotation.md "troubleshoot_rotation.md").
