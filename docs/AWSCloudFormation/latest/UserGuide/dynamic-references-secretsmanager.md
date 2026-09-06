

# Get a secret or secret value from Secrets Manager
<a name="dynamic-references-secretsmanager"></a>

Secrets Manager is a service that allows you to securely store and manage secrets like database credentials, passwords, and third-party API keys. Using Secrets Manager, you can store and control access to these secrets centrally, so that you can replace hardcoded credentials in your code (including passwords), with an API call to Secrets Manager to retrieve the secret programmatically. For more information, see [What is AWS Secrets Manager?](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *AWS Secrets Manager User Guide*.

To use entire secrets or secret values that are stored in Secrets Manager within your CloudFormation templates, you use `secretsmanager` dynamic references.

## Best practices
<a name="dynamic-references-secretsmanager-best-practices"></a>

Follow these best practices when using Secrets Manager dynamic references in your CloudFormation templates:
+ **Use versionless references for your CloudFormation templates** – Store credentials in Secrets Manager and use dynamic references without specifying `version-stage` or `version-id` parameters to support proper secret rotation workflows.
+ **Leverage automatic rotation** – Use Secrets Manager's automatic rotation feature with versionless dynamic references for credential management. This ensures your credentials are regularly updated without requiring template changes. For more information, see [Rotate AWS Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html).
+ **Use versioned references sparingly** – Only specify explicit `version-stage` or `version-id` parameters for specific scenarios like testing or rollback situations.

## Considerations
<a name="dynamic-references-secretsmanager-considerations"></a>

When using `secretsmanager` dynamic references, there are important considerations to keep in mind:
+ CloudFormation doesn't track which version of a secret was used in previous deployments. Plan your secret management strategy carefully before implementing dynamic references. Use versionless references when possible to leverage automatic secret rotation. Monitor and validate resource updates when making changes to dynamic reference configurations, such as when transitioning from unversioned to versioned dynamic references, and vice versa.
+ Updating only the secret value in Secrets Manager doesn't automatically cause CloudFormation to retrieve the new value. CloudFormation retrieves the secret value only during resource creation or updates that modify the resource containing the dynamic reference. 

  For example, suppose your template includes an [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html) resource where the `MasterPassword` property is set to a Secrets Manager dynamic reference. After creating a stack from this template, you update the secret's value in Secrets Manager. However, the `MasterPassword` property retains the old password value. 

  To apply the new secret value, you'll need to modify the `AWS::RDS::DBInstance` resource in your CloudFormation template and perform a stack update. 

  To avoid this manual process in the future, consider using Secrets Manager to automatically rotate the secret. 
+ Dynamic references for secure values, such as `secretsmanager`, aren't currently supported in custom resources.
+ The `secretsmanager` dynamic reference can be used in all resource properties. Using the `secretsmanager` dynamic reference indicates that neither Secrets Manager nor CloudFormation logs should persist any resolved secret value. However, the secret value may show up in the service whose resource it's being used in. Review your usage to avoid leaking secret data.

## Permissions
<a name="dynamic-references-secretsmanager-permissions"></a>

To specify a secret stored in Secrets Manager, you must have permission to call [GetSecretValue](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html) for the secret.

## Reference pattern
<a name="dynamic-references-secretsmanager-pattern"></a>

To reference Secrets Manager secrets in your CloudFormation template, use the following `secretsmanager` reference pattern.

```
{{resolve:secretsmanager:{{secret-id}}:{{secret-string}}:{{json-key}}:{{version-stage}}:{{version-id}}}}
```

`secret-id`  
The name or ARN of the secret.  
To access a secret in your AWS account, you need only specify the secret name. To access a secret in a different AWS account, specify the complete ARN of the secret.  
Required.

`secret-string`  
The only supported value is `SecretString`. The default is `SecretString`.

`json-key`  
The key name of the key-value pair whose value you want to retrieve. If you don't specify a `json-key`, CloudFormation retrieves the entire secret text.  
This segment may not include the colon character ( `:`).

`version-stage`  
The staging label of the version of the secret to use. Secrets Manager uses staging labels to keep track of different versions during the rotation process. If you use `version-stage` then don't specify `version-id`. If you don't specify either `version-stage` or `version-id`, then the default is the `AWSCURRENT` version.  
This segment may not include the colon character ( `:`).

`version-id`  
The unique identifier of the version of the secret to use. If you specify `version-id`, then don't specify `version-stage`. If you don't specify either `version-stage` or `version-id`, then the default is the `AWSCURRENT` version.  
This segment may not include the colon character ( `:`).

## Examples
<a name="dynamic-references-secretsmanager-examples"></a>

**Topics**
+ [Retrieving user name and password values from a secret](#dynamic-references-secretsmanager-examples-user-name-and-password)
+ [Retrieving the entire SecretString](#dynamic-references-secretsmanager-examples-entire-secretstring)
+ [Retrieving a value from a specific version of a secret](#dynamic-references-secretsmanager-examples-specific-version)
+ [Retrieving secrets from another AWS account](#dynamic-references-secretsmanager-examples-secrets-from-another-account)

### Retrieving user name and password values from a secret
<a name="dynamic-references-secretsmanager-examples-user-name-and-password"></a>

The following [AWS::RDS::DBInstance](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-rds-dbinstance.html) example retrieves the user name and password values stored in the `{{MySecret}}` secret. This example shows the recommended pattern for versionless dynamic references, which automatically uses the `AWSCURRENT` version and supports Secrets Manager rotation workflows without requiring template changes.

#### JSON
<a name="dynamic-references-secretsmanager-examples-user-name-and-password.json"></a>

```
{
    "MyRDSInstance": {
        "Type": "AWS::RDS::DBInstance",
        "Properties": {
            "DBName": "MyRDSInstance",
            "AllocatedStorage": "20",
            "DBInstanceClass": "db.t2.micro",
            "Engine": "mysql",
            "MasterUsername": "{{resolve:secretsmanager:{{MySecret}}:SecretString:{{username}}}}",
            "MasterUserPassword": "{{resolve:secretsmanager:{{MySecret}}:SecretString:{{password}}}}"
        }
    }
}
```

#### YAML
<a name="dynamic-references-secretsmanager-examples-user-name-and-password.yaml"></a>

```
  MyRDSInstance:
    Type: AWS::RDS::DBInstance
    Properties:
      DBName: MyRDSInstance
      AllocatedStorage: '20'
      DBInstanceClass: db.t2.micro
      Engine: mysql
      MasterUsername: '{{resolve:secretsmanager:{{MySecret}}:SecretString:{{username}}}}'
      MasterUserPassword: '{{resolve:secretsmanager:{{MySecret}}:SecretString:{{password}}}}'
```

### Retrieving the entire SecretString
<a name="dynamic-references-secretsmanager-examples-entire-secretstring"></a>

The following dynamic reference retrieves the `SecretString` for `{{MySecret}}`.

```
{{resolve:secretsmanager:{{MySecret}}}}
```

Alternatively:

```
{{resolve:secretsmanager:{{MySecret}}::::}}
```

### Retrieving a value from a specific version of a secret
<a name="dynamic-references-secretsmanager-examples-specific-version"></a>

The following dynamic reference retrieves the `{{password}}` value for the `{{AWSPREVIOUS}}` version of `{{MySecret}}`.

```
{{resolve:secretsmanager:{{MySecret}}:SecretString:{{password}}:{{AWSPREVIOUS}}}}
```

### Retrieving secrets from another AWS account
<a name="dynamic-references-secretsmanager-examples-secrets-from-another-account"></a>

The following dynamic reference retrieves the `SecretString` for `{{MySecret}}` that's in another AWS account. You must specify the complete secret ARN to access secrets in another AWS account.

```
{{resolve:secretsmanager:{{arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret}}}}
```

The following dynamic reference retrieves the `{{password}}` value for `{{MySecret}}` that's in another AWS account. You must specify the complete secret ARN to access secrets in another AWS account.

```
{{resolve:secretsmanager:{{arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret}}:SecretString:{{password}}}}
```