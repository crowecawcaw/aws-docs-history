# Get a secure string value from

Systems Manager Parameter Store

In CloudFormation, you can use sensitive data like passwords or license keys without
exposing them directly in your templates by storing the sensitive data as a "secure
string" in AWS Systems Manager Parameter Store. For an introduction to Parameter Store, see [AWS Systems Manager Parameter
Store](../../../systems-manager/latest/userguide/systems-manager-parameter-store.md "../../../systems-manager/latest/userguide/systems-manager-parameter-store.md") in the _AWS Systems Manager User Guide_.

To use a Parameter Store secure string within your template, you use a
`ssm-secure` dynamic reference. CloudFormation never stores the actual secure
string value. Instead, it only stores the literal dynamic reference, which contains the
plaintext parameter name of the secure string.

During stack creation or updates, CloudFormation accesses the secure string value as
needed, without exposing the actual value. Secure strings can only be used for resource
properties that support the `ssm-secure` dynamic reference pattern. For more
information, see [Resources that
support dynamic parameter patterns for secure strings](#template-parameters-dynamic-patterns-resources "#template-parameters-dynamic-patterns-resources").

CloudFormation doesn't return the actual parameter value for secure strings in any API
calls. It only returns the literal dynamic reference. When comparing changes using
change sets, CloudFormation only compares the literal dynamic reference string. It doesn't
resolve and compare the actual secure string values.

When using `ssm-secure` dynamic references, there are a few important
things to keep in mind:

- CloudFormation can't access Parameter Store values from other
  AWS accounts.
- CloudFormation doesn't support using Systems Manager parameter labels or public parameters
  in dynamic references.
- In the `cn-north-1` and `cn-northwest-1` regions, secure
  strings aren't supported by Systems Manager.
- Dynamic references for secure values, such as `ssm-secure`, aren't
  currently supported in custom resources.
- If CloudFormation needs to roll back a stack update, and the previously specified
  version of a secure string parameter is no longer available, the rollback
  operation will fail. In such cases, you have two options:
  - Use `CONTINUE_UPDATE_ROLLBACK` to skip the resource.
  - Recreate the secure string parameter in the Systems Manager Parameter Store, and
    update it until the parameter version reaches the version used in the
    template. Then, use `CONTINUE_UPDATE_ROLLBACK` without
    skipping the resource.

## Resources that

support dynamic parameter patterns for secure strings

Resources that support the `ssm-secure` dynamic reference pattern
include:

| Resource                                                                                                                                                                          | Property type                                                                                                                                                                                                                                       | Properties           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| [AWS::DirectoryService::MicrosoftAD](../TemplateReference/aws-resource-directoryservice-microsoftad.md "../TemplateReference/aws-resource-directoryservice-microsoftad.md")       |                                                                                                                                                                                                                                                     | `Password`           |
| [AWS::DirectoryService::SimpleAD](../TemplateReference/aws-resource-directoryservice-simplead.md "../TemplateReference/aws-resource-directoryservice-simplead.md")                |                                                                                                                                                                                                                                                     | `Password`           |
| [AWS::ElastiCache::ReplicationGroup](../TemplateReference/aws-resource-elasticache-replicationgroup.md "../TemplateReference/aws-resource-elasticache-replicationgroup.md")       |                                                                                                                                                                                                                                                     | `AuthToken`          |
| [AWS::IAM::User](../TemplateReference/aws-resource-iam-user.md "../TemplateReference/aws-resource-iam-user.md")                                                                   | [LoginProfile](../TemplateReference/aws-properties-iam-user-loginprofile.md "../TemplateReference/aws-properties-iam-user-loginprofile.md")                                                                                                         | `Password`           |
| [AWS::KinesisFirehose::DeliveryStream](../TemplateReference/aws-resource-kinesisfirehose-deliverystream.md "../TemplateReference/aws-resource-kinesisfirehose-deliverystream.md") | [RedshiftDestinationConfiguration](../TemplateReference/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.md "../TemplateReference/aws-properties-kinesisfirehose-deliverystream-redshiftdestinationconfiguration.md") | `Password`           |
| [AWS::OpsWorks::App](../TemplateReference/aws-resource-opsworks-app.md "../TemplateReference/aws-resource-opsworks-app.md")                                                       | [Source](../TemplateReference/aws-properties-opsworks-app-source.md "../TemplateReference/aws-properties-opsworks-app-source.md")                                                                                                                   | `Password`           |
| [AWS::OpsWorks::Stack](../TemplateReference/aws-resource-opsworks-stack.md "../TemplateReference/aws-resource-opsworks-stack.md")                                                 | [CustomCookbooksSource](../TemplateReference/aws-properties-opsworks-stack-source.md "../TemplateReference/aws-properties-opsworks-stack-source.md")                                                                                                | `Password`           |
| [AWS::OpsWorks::Stack](../TemplateReference/aws-resource-opsworks-stack.md "../TemplateReference/aws-resource-opsworks-stack.md")                                                 | [RdsDbInstances](../TemplateReference/aws-properties-opsworks-stack-rdsdbinstance.md "../TemplateReference/aws-properties-opsworks-stack-rdsdbinstance.md")                                                                                         | `DbPassword`         |
| [AWS::RDS::DBCluster](../TemplateReference/aws-resource-rds-dbcluster.md "../TemplateReference/aws-resource-rds-dbcluster.md")                                                    |                                                                                                                                                                                                                                                     | `MasterUserPassword` |
| [AWS::RDS::DBInstance](../TemplateReference/aws-resource-rds-dbinstance.md "../TemplateReference/aws-resource-rds-dbinstance.md")                                                 |                                                                                                                                                                                                                                                     | `MasterUserPassword` |
| [AWS::Redshift::Cluster](../TemplateReference/aws-resource-redshift-cluster.md "../TemplateReference/aws-resource-redshift-cluster.md")                                           |                                                                                                                                                                                                                                                     | `MasterUserPassword` |

## Reference pattern

To reference a secure string value from Systems Manager Parameter Store in your CloudFormation
template, use the following `ssm-secure` reference pattern.

```
{{resolve:ssm-secure:`parameter-name`:`version`}}
```

Your reference must adhere to the following regular expression pattern for
parameter-name and version:

```
{{resolve:ssm-secure:[a-zA-Z0-9_.\-/]+(:\d+)?}}
```

`parameter-name`

The name of the parameter in the Parameter Store. The parameter name
is case-sensitive.

Required.

`version`

An integer that specifies the version of the parameter to use. If you
don't specify the exact version, CloudFormation uses the latest version of
the parameter whenever you create or update the stack. For more
information, see [Working with
parameter versions](../../../systems-manager/latest/userguide/sysman-paramstore-versions.md "../../../systems-manager/latest/userguide/sysman-paramstore-versions.md") in the
_AWS Systems Manager User Guide_.

Optional.

## Example

The following example uses an `ssm-secure` dynamic reference to set the
password for an IAM user to a secure string stored in Parameter Store. As
specified, CloudFormation will use version `10` of
the `IAMUserPassword` parameter for stack and
change set operations.

### JSON

```
  "MyIAMUser": {
    "Type": "AWS::IAM::User",
    "Properties": {
      "UserName": "MyUserName",
      "LoginProfile": {
        "Password": "{{resolve:ssm-secure:`IAMUserPassword:10`}}"
      }
    }
  }
```

### YAML

```
  MyIAMUser:
    Type: AWS::IAM::User
    Properties:
      UserName: 'MyUserName'
      LoginProfile:
        Password: '{{resolve:ssm-secure:`IAMUserPassword:10`}}'
```
