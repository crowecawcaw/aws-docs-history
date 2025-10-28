# Specify sensitive data with Systems Manager Parameter Store

With AWS Batch, you can inject sensitive data into your containers by storing your sensitive data in AWS Systems Manager
Parameter Store parameters and then referencing them in your container definition.

###### Topics

- [Considerations when you specify sensitive data using Systems Manager
  Parameter Store](#secrets--parameterstore-considerations "#secrets--parameterstore-considerations")
- [Required IAM permissions for AWS Batch secrets](#secrets-iam-parameters "#secrets-iam-parameters")
- [Inject sensitive data as an environment variable](#secrets-envvar-parameters "#secrets-envvar-parameters")
- [Inject sensitive data in a log configuration](#secrets-logconfig-parameters "#secrets-logconfig-parameters")
- [Create an AWS Systems Manager Parameter Store parameter](#secrets-create-parameter "#secrets-create-parameter")

## Considerations when you specify sensitive data using Systems Manager

Parameter Store

The following should be considered when specifying sensitive data for containers using Systems Manager Parameter Store
parameters.

- This feature requires that your container instance have version 1.23.0 or later of the container agent.
  However, we recommend using the latest container agent version. For information about checking your agent version
  and updating to the latest version, see [Updating the Amazon ECS container agent](../../../AmazonECS/latest/developerguide/ecs-agent-update.md "../../../AmazonECS/latest/developerguide/ecs-agent-update.md") in the
  _Amazon Elastic Container Service Developer Guide_.
- Sensitive data is injected into the container for your job when the container is initially started. If the
  secret or Parameter Store parameter is subsequently updated or rotated, the container doesn't receive the updated
  value automatically. You must launch a new job to force the launch of a fresh job with updated secrets.

## Required IAM permissions for AWS Batch secrets

To use this feature, you must have the execution role and reference it in your job definition. This allows the
Amazon ECS container agent to pull the necessary AWS Systems Manager resources. For more information, see [AWS Batch IAM execution role](execution-IAM-role.md "execution-IAM-role.md").

To provide access to the AWS Systems Manager Parameter Store parameters that you create, manually add the following
permissions as an inline policy to the execution role. For more information, see [Adding and Removing IAM Policies](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the
_IAM User Guide_.

- `ssm:GetParameters`—Required if you're referencing a Systems Manager Parameter Store parameter in a
  task definition.
- `secretsmanager:GetSecretValue`—Required if you're referencing a Secrets Manager secret either
  directly or if your Systems Manager Parameter Store parameter is referencing a Secrets Manager secret in a task definition.
- `kms:Decrypt`—Required only if your secret uses a custom KMS key and not the default key.
  The ARN for your custom key should be added as a resource.

The following example inline policy adds the required permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetParameters",
 "secretsmanager:GetSecretValue",
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:ssm:`us-east-2`:`999999999999`:parameter/`<parameter_name>`",
 "arn:aws:secretsmanager:`us-east-2`:`999999999999`:secret:`<secret_name>`",
 "arn:aws:kms:`us-east-2`:`999999999999`:key/`<key_id>`"
 ]
 }
 ]
}`

```

## Inject sensitive data as an environment variable

Within your container definition, specify `secrets` with the name of the environment variable to set
in the container and the full ARN of the Systems Manager Parameter Store parameter containing the sensitive data to present to
the container.

The following is a snippet of a task definition showing the format when referencing an Systems Manager Parameter Store
parameter. If the Systems Manager Parameter Store parameter exists in the same Region as the task that you're launching, then
you can use either the full ARN or name of the parameter. If the parameter exists in a different Region, then the
full ARN must be specified.

```
{
  "containerProperties": [{
    "secrets": [{
      "name": "`environment_variable_name`",
      "valueFrom": "arn:aws:ssm:`region`:`aws_account_id`:parameter/`parameter_name`"
    }]
  }]
}
```

## Inject sensitive data in a log configuration

Within your container definition, when specifying a `logConfiguration` you can specify
`secretOptions` with the name of the log driver option to set in the container and the full ARN of the
Systems Manager Parameter Store parameter containing the sensitive data to present to the container.

###### Important

If the Systems Manager Parameter Store parameter exists in the same Region as the task you're launching, then you can use
either the full ARN or name of the parameter. If the parameter exists in a different Region, then the full ARN must
be specified.

The following is a snippet of a task definition showing the format when referencing an Systems Manager Parameter Store
parameter.

```
{
  "containerProperties": [{
    "logConfiguration": [{
      "logDriver": "`fluentd`",
      "options": {
        "tag": "`fluentd demo`"
      },
      "secretOptions": [{
        "name": "`fluentd-address`",
        "valueFrom": "arn:aws:ssm:`region`:`aws_account_id`:parameter/`parameter_name`"
      }]
    }]
  }]
}
```

## Create an AWS Systems Manager Parameter Store parameter

You can use the AWS Systems Manager console to create a Systems Manager Parameter Store parameter for your sensitive data. For more
information, see [Walkthrough: Create and Use a Parameter in
a Command (Console)](../../../systems-manager/latest/userguide/sysman-paramstore-console.md "../../../systems-manager/latest/userguide/sysman-paramstore-console.md") in the _AWS Systems Manager User Guide_.

###### To create a Parameter Store parameter

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**, **Create
   parameter**.
3. For **Name**, type a hierarchy and a parameter name. For example, type
   `test/database_password`.
4. For **Description**, type an optional description.
5. For **Type**, choose **String**, **StringList**, or
   **SecureString**.

###### Note

    * If you choose **SecureString**, the **KMS Key ID** field appears. If you
     don't provide a KMS key ID, a KMS key ARN, an alias name, or an alias ARN, then the system uses
     `alias/aws/ssm`. This is the default KMS key for Systems Manager. To avoid using this key, choose a custom
     key. For more information, see [Use Secure String
     Parameters](../../../systems-manager/latest/userguide/sysman-paramstore-about.md "../../../systems-manager/latest/userguide/sysman-paramstore-about.md") in the *AWS Systems Manager User Guide*.
    * When you create a secure string parameter in the console by using the `key-id` parameter with
     either a custom KMS key alias name or an alias ARN, you must specify the prefix `alias/` before the
     alias. The following is an ARN example:



    ```
    arn:aws:kms:us-east-2:123456789012:alias/`MyAliasName`
    ```

    The following is an alias name example:



    ```
    alias/`MyAliasName`
    ```

6. For **Value**, type a value. For example, `MyFirstParameter`. If you chose
   **SecureString**, the value is masked exactly as you entered it.
7. Choose **Create parameter**.
