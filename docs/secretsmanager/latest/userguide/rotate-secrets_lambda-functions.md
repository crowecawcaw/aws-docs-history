# Lambda rotation functions

In [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md"), an AWS Lambda function rotates the secret. AWS Secrets Manager
uses [staging labels](whats-in-a-secret.md "whats-in-a-secret.md") to identify secret
versions during rotation.

If AWS Secrets Manager doesn't provide a [rotation function template](reference_available-rotation-templates.md "reference_available-rotation-templates.md") for your
secret type, you can create a custom rotation function. Follow these guidelines when writing
your rotation function:

###### Best practices for custom rotation functions

- Use the [generic rotation template](reference_available-rotation-templates.md#OTHER_rotation_templates "reference_available-rotation-templates.md#OTHER_rotation_templates") as a
  starting point.
- Be cautious with debugging or logging statements. They can write information to Amazon
  CloudWatch Logs. Ensure logs don't contain sensitive information.

For log statement examples, see the [AWS Secrets Manager rotation function
templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md") source code.

- For security, AWS Secrets Manager only allows a Lambda rotation function to rotate the
  secret directly. The rotation function can't call another Lambda function to rotate the
  secret.
- For debugging guidance, see [Testing and debugging serverless applications](../../../serverless-application-model/latest/developerguide/serverless-test-and-debug.md "../../../serverless-application-model/latest/developerguide/serverless-test-and-debug.md").
- If you use external binaries and libraries, for example to connect to a resource, you're
  responsible for patching and updating them.
- Package your rotation function and any dependencies in a ZIP file, such as
  `my-function.zip`.

###### Warning

Setting the provisioned concurrency parameter to a value lower than 10 can cause
throttling due to insufficient execution threads for the Lambda function. For more
information, see [Understanding
reserved concurrency and provisioned concurrency](../../../lambda/latest/dg/lambda-concurrency.md#reserved-and-provisioned "../../../lambda/latest/dg/lambda-concurrency.md#reserved-and-provisioned") in the AWS Lambda
AWS Lambda Developer Guide.

## Four steps in a rotation

function

###### Topics

- [createSecret: Create a new version of the secret](#w2aac21c11c29c11b5 "#w2aac21c11c29c11b5")
- [setSecret: Change the credentials in the database or service](#w2aac21c11c29c11b7 "#w2aac21c11c29c11b7")
- [testSecret: Test the new secret version](#w2aac21c11c29c11b9 "#w2aac21c11c29c11b9")
- [finishSecret: Finish the rotation](#w2aac21c11c29c11c11 "#w2aac21c11c29c11c11")

### `createSecret`: Create a new version of the secret

The method `createSecret` first checks if a secret exists by calling [`get_secret_value`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_secret_value") with the passed-in `ClientRequestToken`.
If there's no secret, it creates a new secret with [`create_secret`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.create_secret "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.create_secret") and the token as the `VersionId`. Then it
generates a new secret value with [`get_random_password`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.get_random_password"). Next it calls [`put_secret_value`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.put_secret_value") to store it with the staging label
`AWSPENDING`. Storing the new secret value in `AWSPENDING` helps
ensure idempotency. If rotation fails for any reason, you can refer to that secret value in
subsequent calls. See [How
do I make my Lambda function idempotent](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/ "https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-idempotent/").

###### Tips for writing your own rotation function

- Ensure the new secret value only includes characters that are valid for the database
  or service. Exclude characters by using the `ExcludeCharacters` parameter.
- As you test your function, use the AWS CLI to see version stages: call [`describe-secret`](../../../cli/latest/reference/secretsmanager/describe-secret.md "../../../cli/latest/reference/secretsmanager/describe-secret.md") and look at
  `VersionIdsToStages`.
- For Amazon RDS MySQL, in alternating users rotation, Secrets Manager creates a cloned user with a
  name no longer than 16 characters. You can modify the rotation function to allow longer
  usernames. MySQL version 5.7 and higher supports usernames up to 32 characters, however
  Secrets Manager appends "\_clone" (six characters) to the end of the username, so you must keep the
  username to a maximum of 26 characters.

### **setSecret**: Change the credentials in the database or service

The method `setSecret` changes the credential in the database or service to
match the new secret value in the `AWSPENDING` version of the secret.

###### Tips for writing your own rotation function

- If you pass statements to a service that interprets statements, like a database, use
  query parameterization. For more information, see [Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html "https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html") on the _OWASP web
  site_.
- The rotation function is a privileged deputy that has the authorization to access
  and modify customer credentials in both the Secrets Manager secret and the target resource. To
  prevent a potential [confused deputy attack](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), you need
  to make sure that an attacker cannot use the function to access other resources. Before
  you update the credential:
  - Check that the credential in the `AWSCURRENT` version of the secret is valid. If
    the `AWSCURRENT` credential isn't valid, abandon the rotation attempt.
  - Check that the `AWSCURRENT` and `AWSPENDING` secret values are for the same
    resource. For a username and password, check that the `AWSCURRENT` and `AWSPENDING`
    usernames are the same.
  - Check that the destination service resource is the same. For a database, check
    that the `AWSCURRENT` and `AWSPENDING` host names are the same.

- In rare cases, you might want to customize an existing rotation function for a
  database. For example, with alternating users rotation, Secrets Manager creates the cloned user by
  copying the [runtime
  configuration parameters](https://www.postgresql.org/docs/8.0/runtime-config.html "https://www.postgresql.org/docs/8.0/runtime-config.html") of the first user. If you want to include more
  attributes, or change which ones are granted to the cloned user, you need to update the
  code in the `set_secret` function.

### **testSecret**: Test the new secret version

Next, the Lambda rotation function tests the `AWSPENDING` version of the secret by using
it to access the database or service. Rotation functions based on [Rotation function
templates](reference_available-rotation-templates.md "reference_available-rotation-templates.md") test the new secret by using
read access.

### **finishSecret**: Finish the rotation

Finally, the Lambda rotation function moves the label `AWSCURRENT` from the previous
secret version to this version, which also removes the `AWSPENDING` label in the same API
call. Secrets Manager adds the `AWSPREVIOUS` staging label to the previous version, so that you retain
the last known good version of the secret.

The method **finish_secret** uses [`update_secret_version_stage`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/secretsmanager.html#SecretsManager.Client.update_secret_version_stage") to move the staging label `AWSCURRENT`
from the previous secret version to the new secret version. Secrets Manager automatically adds the
`AWSPREVIOUS` staging label to the previous version, so that you retain the last known good
version of the secret.

###### Tips for writing your own rotation function

- Don't remove `AWSPENDING` before this point, and don't remove it by using a
  separate API call, because that can indicate to Secrets Manager that the rotation did not complete
  successfully. Secrets Manager adds the `AWSPREVIOUS` staging label to the previous version, so
  that you retain the last known good version of the secret.

When rotation is successful, the `AWSPENDING` staging label might be attached to the same
version as the `AWSCURRENT` version, or it might not be attached to any version. If the
`AWSPENDING` staging label is present but not attached to the same version as `AWSCURRENT`,
then any later invocation of rotation assumes that a previous rotation request is still in
progress and returns an error. When rotation is unsuccessful, the `AWSPENDING` staging label
might be attached to an empty secret version. For more information, see [Troubleshoot rotation](troubleshoot_rotation.md "troubleshoot_rotation.md").
