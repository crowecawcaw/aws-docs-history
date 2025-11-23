# Create a domain

You can create a domain using the CodeArtifact console, the AWS Command Line Interface (AWS CLI), or CloudFormation. When you
create a domain, it does not contain any repositories. For more information, see
[Create a repository](create-repo.md "create-repo.md"). For more information about
managing CodeArtifact domains with CloudFormation, see [Creating CodeArtifact resources with AWS CloudFormation](cloudformation-codeartifact.md "cloudformation-codeartifact.md").

###### Topics

- [Create a domain (console)](#create-domain-console "#create-domain-console")
- [Create a domain (AWS CLI)](#create-domain-cli "#create-domain-cli")
- [Example AWS KMS key policy](#create-domain-kms-key-policy-example "#create-domain-kms-key-policy-example")

## Create a domain (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, and then choose
   **Create domain**.
3. In **Name**, enter a name for your domain.
4. Expand **Additional configuration**.
5. Use an AWS KMS key (KMS key) to encrypt all assets in your domain. You can use an
   AWS managed KMS key or a KMS key that you manage. For more information about the supported
   types of KMS keys in CodeArtifact, see [Types of AWS KMS keys supported in CodeArtifact](domain-overview.md#domain-overview-supported-kms-keys "domain-overview.md#domain-overview-supported-kms-keys").
   - Choose **AWS managed key** if you want to use the default
     AWS managed key.
   - Choose **Customer managed key** if you want to use a
     KMS key that you manage. To use a KMS key that you manage, in
     **Customer managed key ARN**, search for and choose the KMS key.
     For more information, see [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") and [Customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

6. Choose **Create domain**.

## Create a domain (AWS CLI)

To create a domain with the AWS CLI, use the `create-domain` command. You
must use an AWS KMS key (KMS key) to encrypt all assets in your domain. You can use
an AWS managed KMS key or a KMS key that you manage. If you use an AWS managed
KMS key, do not use the `--encryption-key` parameter.

For more information about the supported
types of KMS keys in CodeArtifact, see [Types of AWS KMS keys supported in CodeArtifact](domain-overview.md#domain-overview-supported-kms-keys "domain-overview.md#domain-overview-supported-kms-keys").
For more information about KMS keys, see [AWS managed key](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") and [Customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in
the _AWS Key Management Service Developer Guide_.

```
aws codeartifact create-domain --domain `my_domain`
```

JSON-formatted data appears in the output with details about your new domain.

```
{
    "domain": {
        "name": "`my_domain`",
        "owner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`us-west-2`:`111122223333`:domain/`my_domain`",
        "status": "Active",
        "encryptionKey": "arn:aws:kms:`us-west-2`:`111122223333`:key/`your-kms-key`",
        "repositoryCount": 0,
        "assetSizeBytes": 0,
        "createdTime": "2020-10-12T16:51:18.039000-04:00"
    }
}
```

If you use a KMS key that you manage, include its Amazon Resource Name (ARN) with the `--encryption-key` parameter.

```
aws codeartifact create-domain --domain `my_domain` --encryption-key `arn:aws:kms:us-west-2:111122223333:key/your-kms-key`
```

JSON-formatted data appears in the output with details about your new domain.

```
{
    "domain": {
        "name": "`my_domain`",
        "owner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`us-west-2`:`111122223333`:domain/`my_domain`",
        "status": "Active",
        "encryptionKey": "arn:aws:kms:`us-west-2`:`111122223333`:key/`your-kms-key`",
        "repositoryCount": 0,
        "assetSizeBytes": 0,
        "createdTime": "2020-10-12T16:51:18.039000-04:00"
    }
}
```

### Create a domain with tags

To create a domain with tags, add the `--tags` parameter to your `create-domain` command.

```
aws codeartifact create-domain --domain `my_domain` --tags `key=k1,value=v1 key=k2,value=v2`
```

## Example AWS KMS key policy

When you create a domain in CodeArtifact, you use a KMS key to encrypt all assets in the domain. You can choose an AWS
managed KMS key, or a customer managed key that you manage. For more information about KMS keys, see the
[AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

To use a customer managed key, your KMS key must have a key policy that grants access to CodeArtifact. A key policy is a
resource policy for an AWS KMS key and are the primary way to control access to KMS keys. Every KMS key must
have exactly one key policy. The statements in the key policy determine who has permission to use the KMS key and how
they can use it.

The following example key policy statement allows AWS CodeArtifact to create grants and view key details on
behalf of authorized users. This policy statement limits the permission to CodeArtifact acting on the specified account
ID’s behalf by using the `kms:ViaService` and `kms:CallerAccount` condition keys. It also
grants all AWS KMS permissions to the IAM root user, so the key can be managed after it is created.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "key-consolepolicy-3",
 "Statement": [
 {
 "Sid": "Allow access through AWS CodeArtifact for all principals in the account that are authorized to use CodeArtifact",
 "Effect": "Allow",
 "Principal": {
 "AWS": "*"
 },
 "Action": [
 "kms:CreateGrant",
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:CallerAccount": "111122223333",
 "kms:ViaService": "codeartifact.us-west-2.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Enable IAM User Permissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 }
 ]
}`

```
