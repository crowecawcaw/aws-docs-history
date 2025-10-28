# Troubleshoot AWS Secrets Manager rotation

For many services, Secrets Manager uses a Lambda function to rotate secrets. For more information, see
[Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md"). The Lambda rotation function interacts with the
database or service the secret is for as well as Secrets Manager. When rotation doesn't work the way you
expect, you should first check the CloudWatch logs.

###### Note

Some services can manage secrets for you, including managing automatic rotation. For more
information, see [Managed rotation for AWS Secrets Manager secrets](rotate-secrets_managed.md "rotate-secrets_managed.md").

###### Topics

- [How to troubleshoot secret rotation
  failures in AWS Lambda functions](#troubleshooting-secret-rotation-failures "#troubleshooting-secret-rotation-failures")
- [No activity after "Found credentials in
  environment variables"](#troubleshoot_rotation_timing-out "#troubleshoot_rotation_timing-out")
- [No activity after "createSecret"](#troubleshoot_rotation_createSecret "#troubleshoot_rotation_createSecret")
- [Error: "Access to KMS is not allowed"](#troubleshoot_rotation_kms-key "#troubleshoot_rotation_kms-key")
- [Error: "Key is missing from secret
  JSON"](#tshoot-lambda-mismatched-secretvalue "#tshoot-lambda-mismatched-secretvalue")
- [Error: "setSecret: Unable to log into
  database"](#troubleshoot_rotation_setSecret "#troubleshoot_rotation_setSecret")
- [Error: "Unable to import module 'lambda_function'"](#tshoot-python-version "#tshoot-python-version")
- [Upgrade an existing rotation function from
  Python 3.7 to 3.9](#troubleshoot_rotation_python39 "#troubleshoot_rotation_python39")
- [Upgrade an existing rotation function from
  Python 3.9 to 3.10](#troubleshoot_rotation_python_310 "#troubleshoot_rotation_python_310")
- [AWS Lambda secret rotation with
  PutSecretValue failed](#troubleshoot_rotation_putsecretvalue "#troubleshoot_rotation_putsecretvalue")
- [Error: "Error when executing lambda
  <arn> during <a
  rotation> step"](#concurrency-related-failures "#concurrency-related-failures")

## How to troubleshoot secret rotation

failures in AWS Lambda functions

If you're experiencing secret rotation failures with your Lambda functions, use the
following steps to troubleshoot and resolve the issue.

### Possible causes

- Insufficient concurrent executions for the Lambda function
- Race conditions due to multiple API calls during rotation
- Incorrect Lambda function logic
- Networking issues between the Lambda function and the database

### General troubleshooting steps

1. Analyze CloudWatch logs:
   - Look for specific error messages or unexpected behavior in the Lambda function
     logs
   - Verify that all rotation steps (**CreateSecret**,
     **SetSecret**, **TestSecret**,
     **FinishSecret**) are being attempted

2. Review API calls during rotation:
   - Avoid making mutating API calls on the secret during Lambda rotation
   - Ensure there's no race condition between **RotateSecret** and
     **PutSecretValue** calls

3. Verify Lambda function logic:
   - Confirm you're using the latest AWS sample code for secret rotation
   - If using custom code, review it for proper handling of all rotation steps

4. Check network configuration:
   - Verify security group rules allow the Lambda function to access the
     database
   - Ensure proper VPC endpoint or public endpoint access for Secrets Manager

5. Test secret versions:
   - Verify that the AWSCURRENT version of the secret allows database access
   - Check if AWSPREVIOUS or AWSPENDING versions are valid

6. Clear pending rotations:
   - If rotation consistently fails, clear the AWSPENDING staging label and retry
     rotation

7. Check Lambda concurrency settings:
   - Verify that concurrency settings are appropriate for your workload
   - If you suspect concurrency issues, see the "Troubleshooting concurrency-related
     rotation failures" section

## No activity after "Found credentials in

environment variables"

If there is no activity after "Found credentials in environment variables", and the task
duration is long, for example the default Lambda timeout of 30000ms, then the Lambda function
may be timing out while trying to reach the Secrets Manager endpoint.

Your Lambda rotation function must be able to access a Secrets Manager endpoint. If your
Lambda function can access the internet, then you can use a public endpoint. To find an
endpoint, see [AWS Secrets Manager endpoints](asm_access.md#endpoints "asm_access.md#endpoints").

If your Lambda function runs in a VPC that doesn't have internet access, we
recommend you configure Secrets Manager service private endpoints within your VPC. Your VPC can
then intercept requests addressed to the public regional endpoint and redirect them to
the private endpoint. For more information, see [VPC endpoints
(AWS PrivateLink)](vpc-endpoint-overview.md "vpc-endpoint-overview.md").

Alternatively, you can enable your Lambda function to access a Secrets Manager public endpoint
by adding a [NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md") or an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md") to your VPC, which allows traffic from your VPC to reach the
public endpoint. This exposes your VPC to more risk because an IP address for the
gateway can be attacked from the public Internet.

## No activity after "createSecret"

The following are issues that can cause rotation to stop after createSecret:

**The VPC Network ACLs do not allow HTTPS traffic in and out.**

For more information, see [Control traffic to subnets using
Network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") in the _Amazon VPC User Guide_.

**Lambda function timeout configuration is too short to perform the task.**

For more information, see [Configuring Lambda function
options](../../../lambda/latest/dg/configuration-function-common.md "../../../lambda/latest/dg/configuration-function-common.md") in the _AWS Lambda Developer Guide_.

**The Secrets Manager VPC endpoint does not allow the VPC CIDRs on ingress in the assigned
security groups.**

For more information, see [Control traffic to resources using
security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") in the _Amazon VPC User Guide_.

**The Secrets Manager VPC endpoint policy does not allow Lambda to use the VPC endpoint.**

For more information, see [Using an AWS Secrets Manager VPC endpoint](vpc-endpoint-overview.md "vpc-endpoint-overview.md").

**The secret uses alternating users rotation, the superuser secret is managed by Amazon RDS,
and the Lambda function can't access the RDS API.**

For [alternating users rotation](rotation-strategy.md#rotating-secrets-two-users "rotation-strategy.md#rotating-secrets-two-users")
where the superuser secret is [managed by another
AWS service](service-linked-secrets.md "service-linked-secrets.md"), the Lambda rotation function must be able to call the service
endpoint to get the database connection information. We recommend that you configure a
VPC endpoint for the database service. For more information, see:

- [Amazon RDS API and
  interface VPC endpoints](../../../AmazonRDS/latest/UserGuide/vpc-interface-endpoints.md "../../../AmazonRDS/latest/UserGuide/vpc-interface-endpoints.md") in the _Amazon RDS User
  Guide_.
- [Working with
  VPC endpoints](../../../redshift/latest/mgmt/enhanced-vpc-working-with-endpoints.md "../../../redshift/latest/mgmt/enhanced-vpc-working-with-endpoints.md") in the _Amazon Redshift Management Guide_.

## Error: "Access to KMS is not allowed"

If you see `ClientError: An error occurred (AccessDeniedException) when calling the
 GetSecretValue operation: Access to KMS is not allowed`, the rotation function does
not have permission to decrypt the secret using the KMS key that was used to encrypt the
secret. There might be a condition in the permissions policy that limits the encryption
context to a specific secret. For information about the required permission, see [Policy
statement for customer managed key](rotating-secrets-required-permissions-function.md#rotating-secrets-required-permissions-function-cust-key-example "rotating-secrets-required-permissions-function.md#rotating-secrets-required-permissions-function-cust-key-example").

## Error: "Key is missing from secret

JSON"

A Lambda rotation function requires the secret value to be in a specific JSON structure. If
you see this error, then the JSON might be missing a key that the rotation function tried to
access. For information about the JSON structure for each type of secret, see [JSON structure of AWS Secrets Manager secrets](reference_secret_json_structure.md "reference_secret_json_structure.md") .

## Error: "setSecret: Unable to log into

database"

The following are issues that can cause this error:

**The rotation function can't access the database.**

If the task duration is long, for example over 5000ms, then the Lambda rotation
function might not be able to access the database over the network.

If your database or service is running on an Amazon EC2 instance in a VPC, we recommend
that you configure your Lambda function to run in the same VPC. Then the rotation
function can communicate directly with your service. For more information, see [Configuring VPC access](../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring "../../../lambda/latest/dg/configuration-vpc.md#vpc-configuring").

To allow the Lambda function to access the database or service, you must make
sure that the security groups attached to your Lambda rotation function allow
outbound connections to the database or service. You must also make sure that
the security groups attached to your database or service allow inbound
connections from the Lambda rotation function.

**The credentials in the secret are incorrect.**

If the task duration is short, then the Lambda rotation function might not be able to
authenticate with the credentials in the secret. Check the credentials by logging in
manually with the information in the `AWSCURRENT` and
`AWSPREVIOUS` versions of the secret using the AWS CLI command [`get-secret-value`](../../../cli/latest/reference/secretsmanager/get-secret-value.md "../../../cli/latest/reference/secretsmanager/get-secret-value.md").

**The database uses `scram-sha-256` to encrypt passwords.**

If your database is Aurora PostgreSQL version 13 or later and uses
`scram-sha-256` to encrypt passwords, but the rotation function uses
`libpq` version 9 or older which does not support
`scram-sha-256`, then the rotation function can't connect to the database.

###### To determine which database users use `scram-sha-256`

encryption

- See _Checking for users with non-SCRAM passwords_ in the blog
  [SCRAM Authentication in RDS for PostgreSQL 13](https://aws.amazon.com/blogs/database/scram-authentication-in-rds-for-postgresql-13/ "https://aws.amazon.com/blogs/database/scram-authentication-in-rds-for-postgresql-13/").

###### To determine which version of `libpq` your rotation function

uses

1. On a Linux-based computer, on the Lambda console, navigate to your rotation
   function and download the deployment bundle. Uncompress the zip file into a work
   directory.
2. At a command line, in the work directory, run:

`readelf -a libpq.so.5 | grep RUNPATH` 3. If you see the string `PostgreSQL-9.4.x`,
or any major version less than 10, then the rotation function doesn't support
`scram-sha-256`.

    * Output for a rotation function that doesn't support
     `scram-sha-256`:


    `0x000000000000001d (RUNPATH) Library runpath:
     [/local/p4clients/pkgbuild-*a1b2c*/workspace/build/PostgreSQL/`PostgreSQL-9.4.x`_client_only.*123456*.0/AL2_x86_64/DEV.STD.PTHREAD/build/private/tmp/brazil-path/build.libfarm/lib:/local/p4clients/pkgbuild-*a1b2c*/workspace/src/PostgreSQL/build/private/install/lib]`
    * Output for a rotation function that supports
     `scram-sha-256`:


    `0x000000000000001d (RUNPATH) Library runpath:
     [/local/p4clients/pkgbuild-*a1b2c*/workspace/build/PostgreSQL/`PostgreSQL-10.x`_client_only.*123456*.0/AL2_x86_64/DEV.STD.PTHREAD/build/private/tmp/brazil-path/build.libfarm/lib:/local/p4clients/pkgbuild-*a1b2c*/workspace/src/PostgreSQL/build/private/install/lib]`
    * Output for a rotation function that supports
     `scram-sha-256`:


    `0x000000000000001d (RUNPATH) Library runpath:
     [/local/p4clients/pkgbuild- a1b2c
     /workspace/build/PostgreSQL/PostgreSQL-14.x_client_only. 123456
     .0/AL2_x86_64/DEV.STD.PTHREAD/build/private/tmp/brazil-path/build.libfarm/lib:/local/p4clients/pkgbuild-
     a1b2c /workspace/src/PostgreSQL/build/private/install/lib]`
    * Output for a rotation function that supports
     `scram-sha-256`:


    `0x000000000000001d (RUNPATH) Library runpath:
     [/local/p4clients/pkgbuild- a1b2c/workspace/build/PostgreSQL/PostgreSQL-
     14.x_client_only.123456.0/AL2_x86_64/DEV.STD.PTHREAD/build/private/tmp/brazil-
     path/build.libfarm/lib:/local/p4clients/pkgbuild-
     a1b2c/workspace/src/PostgreSQL/build/private/install/lib]`

###### Note

If you set up automatic secret rotation before December 30, 2021, your rotation
function bundled an earlier version of `libpq` that doesn't support
`scram-sha-256`. To support `scram-sha-256`, you need to [recreate your rotation function](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md").

**The database requires SSL/TLS access.**

If your database requires an SSL/TLS connection, but the rotation function uses an
unencrypted connection, then the rotation function can't connect to the database.
Rotation functions for Amazon RDS (except Oracle and Db2) and Amazon DocumentDB automatically use
Secure Socket Layer (SSL) or Transport Layer Security (TLS) to connect to your database,
if it is available. Otherwise they use an unencrypted connection.

###### Note

If you set up automatic secret rotation before December 20, 2021, your rotation
function might be based on an earlier template that did not support SSL/TLS. To
support connections that use SSL/TLS, you need to [recreate your rotation function](rotate-secrets_turn-on-for-db.md "rotate-secrets_turn-on-for-db.md").

###### To determine when your rotation function was created

1. In the Secrets Manager console [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/"), open your secret. In the
   **Rotation configuration** section, under **Lambda
   rotation function**, you see the **Lambda function ARN**,
   for example,
   `arn:aws:lambda:`aws-region`:`123456789012`:function:`SecretsManagerMyRotationFunction`. Copy the function name from the end of the ARN, in this example `SecretsManagerMyRotationFunction``.
2. In the AWS Lambda console [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/"), under
   **Functions**, paste your Lambda function name in the search box,
   choose Enter, and then choose the Lambda function.
3. In the function details page, on the **Configuration** tab,
   under **Tags**, copy the value next to the key
   **aws:cloudformation:stack-name**.
4. In the AWS CloudFormation console [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/"), under
   **Stacks**, paste the key value in the search box, and then
   choose Enter.
5. The list of stacks filters so that only the stack that created the Lambda
   rotation function appears. In the **Created date** column, view the
   date the stack was created. This is the date the Lambda rotation function was
   created.

## Error: "Unable to import module 'lambda_function'"

You might receive this error if you're running an earlier Lambda function that was
automatically upgraded from Python 3.7 to a newer version of Python. To resolve the error, you
can change the Lambda function version back to Python 3.7, and then [Upgrade an existing rotation function from
Python 3.7 to 3.9](#troubleshoot_rotation_python39 "#troubleshoot_rotation_python39"). For more information, see [Why did my Secrets Manager
Lambda function rotation fail with a “pg module not found“ error?](https://repost.aws/knowledge-center/secrets-manager-lambda-rotation "https://repost.aws/knowledge-center/secrets-manager-lambda-rotation") in _AWS
re:Post_.

## Upgrade an existing rotation function from

Python 3.7 to 3.9

Some rotation functions created before November 2022 used Python 3.7. The AWS SDK for
Python stopped supporting Python 3.7 in December 2023. For more information, see [Python support policy updates for AWS SDKs and Tools](https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/ "https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/"). To switch to a new rotation
function that uses Python 3.9, you can add a runtime property to an existing rotation function
or recreate the rotation function.

###### To find which Lambda rotation functions use Python 3.7

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the list of **Functions**, filter for
   `SecretsManager`.
3. In the filtered list of functions, under **Runtime**, look for Python
   3.7.

###### To upgrade to Python 3.9:

- [Option 1: Recreate the rotation function using
  AWS CloudFormation](#update-python-opt-1 "#update-python-opt-1")
- [Option 2: Update the runtime for the existing rotation
  function using AWS CloudFormation](#update-python-opt-2 "#update-python-opt-2")
- [Option 3: For AWS CDK users, upgrade the CDK
  library](#update-python-opt-3 "#update-python-opt-3")

### Option 1: Recreate the rotation function using

AWS CloudFormation

When you use the Secrets Manager console to turn on rotation, Secrets Manager uses AWS CloudFormation to create the
necessary resources, including the Lambda rotation function. If you used the console to turn
on rotation, or you created the rotation function using a AWS CloudFormation stack, you can use the same
AWS CloudFormation stack to recreate the rotation function with a new name. The new function uses the
more recent version of Python.

###### To find the AWS CloudFormation stack that created the rotation function

- On the Lambda function details page, on the **Configuration** tab, choose **Tags**. View the ARN next to **aws:cloudformation:stack-id**.

The stack name is embedded in the ARN, as shown in the following example.

    + ARN: `arn:aws:cloudformation:us-west-2:408736277230:stack/`SecretsManagerRDSMySQLRotationSingleUser5c2-SecretRotationScheduleHostedRotationLambda`-3CUDHZMDMBO8/79fc9050-2eef-11ed-80f0-021fb13c0537`
    + Stack name: `SecretsManagerRDSMySQLRotationSingleUser5c2-SecretRotationScheduleHostedRotationLambda`

###### To recreate a rotation function (AWS CloudFormation)

1. In AWS CloudFormation, search for the stack by name, and then choose **Update**.

If a dialog box appears recommending you update the root stack, choose **Go
to root stack**, and then choose **Update**. 2. On the **Update stack** page, under **Prepare
template**, choose **Edit in Application Composer**, and
then under **Edit template in Application Composer**, choose the button
**Edit in Application Composer**. 3. In Application Composer, do the following:

    1. In the template code, in
     `SecretRotationScheduleHostedRotationLambda`, replace the value for
     `"functionName": "SecretsManagerTestRotationRDS"` with a new function
     name, for example in JSON, ``"functionName":
     "SecretsManagerTestRotationRDSupdated"``
    2. Choose **Update template**.
    3. In the **Continue to AWS CloudFormation** dialog box, choose
     **Confirm and continue to AWS CloudFormation**.

4. Continue through the AWS CloudFormation stack workflow and then choose
   **Submit**.

### Option 2: Update the runtime for the existing rotation

function using AWS CloudFormation

When you use the Secrets Manager console to turn on rotation, Secrets Manager uses AWS CloudFormation to create the
necessary resources, including the Lambda rotation function. If you used the console to turn
on rotation, or you created the rotation function using a AWS CloudFormation stack, you can use the same
AWS CloudFormation stack to update the runtime for the rotation function.

###### To find the AWS CloudFormation stack that created the rotation function

- On the Lambda function details page, on the **Configuration** tab, choose **Tags**. View the ARN next to **aws:cloudformation:stack-id**.

The stack name is embedded in the ARN, as shown in the following example.

    + ARN: `arn:aws:cloudformation:us-west-2:408736277230:stack/`SecretsManagerRDSMySQLRotationSingleUser5c2-SecretRotationScheduleHostedRotationLambda`-3CUDHZMDMBO8/79fc9050-2eef-11ed-80f0-021fb13c0537`
    + Stack name: `SecretsManagerRDSMySQLRotationSingleUser5c2-SecretRotationScheduleHostedRotationLambda`

###### To update the runtime for a rotation function (AWS CloudFormation)

1. In AWS CloudFormation, search for the stack by name, and then choose **Update**.

If a dialog box appears recommending you update the root stack, choose **Go
to root stack**, and then choose **Update**. 2. On the **Update stack** page, under **Prepare
template**, choose **Edit in Application Composer**, and
then under **Edit template in Application Composer**, choose the button
**Edit in Application Composer**. 3. In Application Composer, do the following:

    1. In the template JSON, for the
     `SecretRotationScheduleHostedRotationLambda`, under
     `Properties`, under `Parameters`, add `"runtime":
     "python3.9"`.
    2. Choose **Update template**.
    3. In the **Continue to AWS CloudFormation** dialog box, choose
     **Confirm and continue to AWS CloudFormation**.

4. Continue through the AWS CloudFormation stack workflow and then choose
   **Submit**.

### Option 3: For AWS CDK users, upgrade the CDK

library

If you used the AWS CDK prior to version v2.94.0 to set up rotation for your secret, you
can update the Lambda function by upgrading to v2.94.0 or later. For more information, see
the [AWS Cloud Development Kit (AWS CDK) v2 Developer
Guide](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md").

## Upgrade an existing rotation function from

Python 3.9 to 3.10

Secrets Manager is transitioning from Python 3.9 to 3.10 for Lambda rotation functions. To switch to
a new rotation function that uses Python 3.10, you'll need to follow the upgrade path
based on your deployment method. Use the following procedures to upgrade both the Python
version and the underlying dependencies.

###### To find which Lambda rotation functions use Python 3.9

1. Sign in to the AWS Management Console and open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. In the list of **Functions**, filter for
   `SecretsManager`.
3. In the filtered list of functions, under **Runtime**, look for
   `Python 3.9`.

### Update paths by deployment method

The Lambda rotation functions identified in this list can be deployed through Secrets Manager
console, AWS Serverless Application Repository apps, or AWS CloudFormation transforms. Each of these deployment strategies have a
distinct update path.

Use one of the following procedures to update your Lambda rotation functions, depending
on how your function was deployed.

AWS Secrets Manager console-deployed functions
A new Lambda function must be deployed through AWS Secrets Manager console as you cannot
manually update dependencies for existing Lambda functions.

Use the following procedure to upgrade AWS Secrets Manager console-deployed
functions.

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/ "https://console.aws.amazon.com/secretsmanager/").
2. Under **AWS Secrets Manager**, select **Secrets**.
   Select the secret that uses the Lambda function you want to update.
3. Navigate to the **Rotations** tab and select the
   **Update rotation configurations** option.
4. Under **Rotation functions**, choose **Create a new
   function**, and enter a new name for the Lambda rotation
   function.
   1. (Optional) Once the update is complete, you can test the updated Lambda
      function to confirm it works as expected. Under the
      **Rotation** tab, select **Rotate Secret
      Immediately** to initiate an immediate rotation.
   2. (Optional) You can view your function logs and the Python version used at
      runtime in Amazon CloudWatch. For more information, see [Viewing CloudWatch Logs for Lambda functions](../../../lambda/latest/dg/monitoring-cloudwatchlogs-view.md#monitoring-cloudwatchlogs-console "../../../lambda/latest/dg/monitoring-cloudwatchlogs-view.md#monitoring-cloudwatchlogs-console") in the _AWS Lambda
      Developer Guide_.

5. Once the new rotation function is set up, you can delete the old rotation
   function.

AWS Serverless Application Repository deployments
The following procedure shows how to upgrade AWS Serverless Application Repository deployments. The Lambda
functions deployed through AWS Serverless Application Repository have a banner stating `This function
 belongs to an application. Click here to manage it.` which includes
a link to the Lambda application to which the function belongs.

###### Important

AWS Serverless Application Repository availability is AWS Region dependent.

Use the following procedure to update AWS Serverless Application Repository deployed functions.

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Navigate to the **Configurations** tab of the Lambda function
   that needs to be updated.
   1. You'll need the following information about your function when updating
      the deployed AWS Serverless Application Repository application. You can find this information in the Lambda
      console.
      - **Lambda application's name**
        - The Lambda application name can be found by using the link in the
          banner. For example, the banner states the following
          `serverlessrepo-`SecretsManagerRedshiftRotationSingleUser``.
The name in this example is
`SecretsManagerRedshiftRotationSingleUser`.

      - **Lambda rotation function name**
      - **Secrets Manager endpoint**
        - The endpoint can be found under the
          **Configurations** and the **Environment
          variables** tabs assigned to the
          **SECRETS_MANAGER_ENDPOINT** variable.

3. To upgrade Python, you must update the semantic version of the serverless
   application. See [Updating Applications](../../../serverlessrepo/latest/devguide/serverlessrepo-how-to-consume-new-version.md#update-applications "../../../serverlessrepo/latest/devguide/serverlessrepo-how-to-consume-new-version.md#update-applications") in the _AWS Serverless Application Repository Developer
   Guide_.

Custom Lambda rotation functions
If you created custom Lambda rotation functions, you’ll need to upgrade each
package dependencies and runtimes for these functions. For more information, see
[Upgrade Lambda function runtime to latest version](https://repost.aws/knowledge-center/lambda-upgrade-function-runtime "https://repost.aws/knowledge-center/lambda-upgrade-function-runtime").

AWS::SecretsManager-2024-09-16 transform macro
If the Lambda function is deployed through this transform, [updating the stacks using existing template](../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md "../../../AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.md") will allow you to use the
updated Lambda runtime.

Use the following procedure to update AWS CloudFormation stack using existing template.

1. Open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the **Stacks** page, select the stack that you want to
   update.
3. Choose **Update** on the stack details pane.
4. For **Choose a template update method**, select
   **Direct update**.
5. On the **Specify template** page, select **Use
   existing template**.
6. Keep all other options at their default values, and then choose
   **Update stack**.

If you experience issues updating the stack, see [Determine the cause of a stack failure](../../../AWSCloudFormation/latest/UserGuide/determine-root-cause-for-stack-failures.md "../../../AWSCloudFormation/latest/UserGuide/determine-root-cause-for-stack-failures.md") in the _AWS CloudFormation User
Guide_.

AWS::SecretsManager-2020-07-23 transform macro
We recommend you migrate to the newer transform version if you're using
`AWS::SecretsManager-2020-07-23`. See [Introducing an enhanced version of the AWS Secrets Manager transform:
AWS::SecretsManager-2024-09-16](https://aws.amazon.com/blogs/security/introducing-an-enhanced-version-of-the-aws-secrets-manager-transform-awssecretsmanager-2024-09-16/ "https://aws.amazon.com/blogs/security/introducing-an-enhanced-version-of-the-aws-secrets-manager-transform-awssecretsmanager-2024-09-16/") in the _AWS Security
Blog_ for more information. If you continue to use
`AWS::SecretsManager-2020-07-23`, you can experience a mismatch error
between your runtime version and the Lambda function code artifacts. For more
information, see [AWS::SecretsManager::RotationSchedule HostedRotationLambda](../../../AWSCloudFormation/latest/TemplateReference/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md#cfn-secretsmanager-rotationschedule-hostedrotationlambda-runtime "../../../AWSCloudFormation/latest/TemplateReference/aws-properties-secretsmanager-rotationschedule-hostedrotationlambda.md#cfn-secretsmanager-rotationschedule-hostedrotationlambda-runtime") in the
_AWS CloudFormation Template Reference_.

If you experience issues updating the stack, [Determine the cause of a stack failure](../../../AWSCloudFormation/latest/UserGuide/determine-root-cause-for-stack-failures.md "../../../AWSCloudFormation/latest/UserGuide/determine-root-cause-for-stack-failures.md") in the _AWS CloudFormation User
Guide_.

###### Verify Python upgrade

To verify the Python upgrade, open the Lambda console ([https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/")) and access
the **Function** page. Select the function you updated. Under
**Code source** section, review the files included in the directory and
ensure the Python .so file is version `3.10`.

## AWS Lambda secret rotation with

`PutSecretValue` failed

If you use an assumed role or a cross-account rotation with Secrets Manager and you find a
**RotationFailed** event in CloudTrail with the message: **`Pending secret
 version `VERSION_ID`for Secret`SECRET_ARN` was not created by Lambda`LAMBDA_ARN.`Remove the
`AWSPENDING` staging label and restart rotation`**, then you need to
update your Lambda function to use the `RotationToken` parameter.

## Update Lambda rotation function to include

`RotationToken`

1. Download the Lambda function code
   - Open the Lambda console
   - In the navigation pane, choose **Functions**
   - Select your Lambda secret rotation function for **Function
     name**
   - For **Download**, choose one of **Function code
     .zip**, **AWS SAM file**,
     **Both**
   - Choose **OK** to save the function on your local
     machine.

2. Edit `Lambda_handler`

Include the rotation_token parameter in the create_secret step for cross-account
rotation:

```

def lambda_handler(event, context):
    """Secrets Manager Rotation Template

    This is a template for creating an AWS Secrets Manager rotation lambda

    Args:
        event (dict): Lambda dictionary of event parameters. These keys must include the following:
            - SecretId: The secret ARN or identifier
            - ClientRequestToken: The ClientRequestToken of the secret version
            - Step: The rotation step (one of createSecret, setSecret, testSecret, or finishSecret)
            - RotationToken: the rotation token to put as parameter for PutSecretValue call

        context (LambdaContext): The Lambda runtime information

    Raises:
        ResourceNotFoundException: If the secret with the specified arn and stage does not exist

        ValueError: If the secret is not properly configured for rotation

        KeyError: If the event parameters do not contain the expected keys

    """
    arn = event['SecretId']
    token = event['ClientRequestToken']
    step = event['Step']
    # Add the rotation token
    rotation_token = event['RotationToken']

    # Setup the client
    service_client = boto3.client('secretsmanager', endpoint_url=os.environ['SECRETS_MANAGER_ENDPOINT'])

    # Make sure the version is staged correctly
    metadata = service_client.describe_secret(SecretId=arn)
    if not metadata['RotationEnabled']:
        logger.error("Secret %s is not enabled for rotation" % arn)
        raise ValueError("Secret %s is not enabled for rotation" % arn)
    versions = metadata['VersionIdsToStages']
    if token not in versions:
        logger.error("Secret version %s has no stage for rotation of secret %s." % (token, arn))
        raise ValueError("Secret version %s has no stage for rotation of secret %s." % (token, arn))
    if "AWSCURRENT" in versions[token]:
        logger.info("Secret version %s already set as AWSCURRENT for secret %s." % (token, arn))
        return
    elif "AWSPENDING" not in versions[token]:
        logger.error("Secret version %s not set as AWSPENDING for rotation of secret %s." % (token, arn))
        raise ValueError("Secret version %s not set as AWSPENDING for rotation of secret %s." % (token, arn))
    # Use rotation_token
    if step == "createSecret":
        create_secret(service_client, arn, token, rotation_token)

    elif step == "setSecret":
        set_secret(service_client, arn, token)

    elif step == "testSecret":
        test_secret(service_client, arn, token)

    elif step == "finishSecret":
        finish_secret(service_client, arn, token)

    else:
        raise ValueError("Invalid step parameter")

```

3. Edit `create_secret` code

Revise the `create_secret` function to accept and use the
`rotation_token` parameter:

```

# Add rotation_token to the function
def create_secret(service_client, arn, token, rotation_token):
"""Create the secret

This method first checks for the existence of a secret for the passed in token. If one does not exist, it will generate a
new secret and put it with the passed in token.

Args:
service_client (client): The secrets manager service client

arn (string): The secret ARN or other identifier

token (string): The ClientRequestToken associated with the secret version

rotation_token (string): the rotation token to put as parameter for PutSecretValue call

Raises:
ResourceNotFoundException: If the secret with the specified arn and stage does not exist

"""
# Make sure the current secret exists
service_client.get_secret_value(SecretId=arn, VersionStage="AWSCURRENT")

# Now try to get the secret version, if that fails, put a new secret
try:
service_client.get_secret_value(SecretId=arn, VersionId=token, VersionStage="AWSPENDING")
logger.info("createSecret: Successfully retrieved secret for %s." % arn)
except service_client.exceptions.ResourceNotFoundException:
# Get exclude characters from environment variable
exclude_characters = os.environ['EXCLUDE_CHARACTERS'] if 'EXCLUDE_CHARACTERS' in os.environ else '/@"\'\\'
# Generate a random password
passwd = service_client.get_random_password(ExcludeCharacters=exclude_characters)

# Put the secret, using rotation_token
service_client.put_secret_value(SecretId=arn, ClientRequestToken=token, SecretString=passwd['RandomPassword'], VersionStages=['AWSPENDING'], RotationToken=rotation_token)
logger.info("createSecret: Successfully put secret for ARN %s and version %s." % (arn, token))

```

4. Upload the updated Lambda function code

After updating your Lambda function code, [upload it to rotate your secret](../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-update "../../../lambda/latest/dg/configuration-function-zip.md#configuration-function-update").

## Error: "Error when executing lambda

`<arn>` during `<a
 rotation>` step"

If you're experiencing intermittent secret rotation failures with your Lambda function
getting stuck in a loop of sets, for example between **CreateSecret** and
**SetSecret**, the issue may be related to concurrency settings.

### Concurrency troubleshooting

steps

###### Warning

Setting the provisioned concurrency parameter to a value lower than 10 can cause
throttling due to insufficient execution threads for the Lambda function. For more
information, see [Understanding
reserved concurrency and provisioned concurrency](../../../lambda/latest/dg/lambda-concurrency.md#reserved-and-provisioned "../../../lambda/latest/dg/lambda-concurrency.md#reserved-and-provisioned") in the AWS Lambda
AWS Lambda Developer Guide.

1. Check and adjust Lambda concurrency settings:
   - Verify that `reserved_concurrent_executions` is not set too low (for
     example, 1)
   - If using reserved concurrency, set it to at least 10
   - Consider using unreserved concurrency for more flexibility

2. For provisioned concurrency:
   - Don't set the provisioned concurrency parameter explicitly (for example, in
     Terraform).
   - If you must set it, use a value of at least 10.
   - Test thoroughly to make sure the chosen value works for your use case.

3. Monitor and adjust concurrency:
   - Calculate concurrency using this formula: Concurrency = (average requests per
     second) \* (average request duration in seconds). For more information, see [Estimating reserved concurrency](../../../lambda/latest/dg/configuration-concurrency.md#estimating-reserved-concurrency "../../../lambda/latest/dg/configuration-concurrency.md#estimating-reserved-concurrency").
   - Observe and record values during rotations to determine the appropriate
     concurrency settings.
   - Be careful when setting low concurrency values. They can cause throttling if
     there aren't enough available execution threads.

For more information on configuring Lambda concurrency, see [Configuring reserved
concurrency](../../../lambda/latest/dg/configuration-concurrency.md "../../../lambda/latest/dg/configuration-concurrency.md") and [Configuring provisioned
concurrency](../../../lambda/latest/dg/provisioned-concurrency.md "../../../lambda/latest/dg/provisioned-concurrency.md") in the AWS Lambda Developer Guide.
