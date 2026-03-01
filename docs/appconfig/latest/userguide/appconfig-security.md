# Security in AWS AppConfig

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a
data center and network architecture that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security _of_ the
cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is
  responsible for protecting the infrastructure that runs AWS services in the
  AWS Cloud. AWS also provides you with services that you can use securely.
  Third-party auditors regularly test and verify the effectiveness of our security as
  part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance
  programs that apply to AWS Systems Manager, see [AWS Services in Scope
  by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility
  is determined by the AWS service that you use. You are also responsible for other
  factors including the sensitivity of your data, your company’s requirements, and
  applicable laws and regulations.
  AWS AppConfig is a tool in AWS Systems Manager. To understand how to apply the shared responsibility model
  when using AWS AppConfig, see [Security in
  AWS Systems Manager](../../../systems-manager/latest/userguide/security.md "../../../systems-manager/latest/userguide/security.md"). That section describes how to configure Systems Manager to meet the security
  and compliance objectives for AWS AppConfig.

## Implement least privilege access

As a security best practice, grant the minimum required permissions that identities
require to perform specific actions on specific resources under specific conditions.
AWS AppConfig Agent offers two features that enable the agent to access the filesystem of an
instance or container: _backup_ and _write to
disk_. If you enable these features, verify that only the AWS AppConfig Agent has
permissions to write to the designated configuration files on the filesystem. Also
verify that only the processes required to read from these configuration files have the
ability to do so. Implementing least privilege access is fundamental in reducing
security risk and the impact that could result from errors or malicious intent.

For more information about implementing least privilege access, see [SEC03-BP02 Grant least privilege access](../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md "../../../wellarchitected/latest/framework/sec_permissions_least_privileges.md") in the
_AWS Well-Architected Tool User Guide_. For more information about the AWS AppConfig Agent
features mentioned in this section, see [Using a manifest to enable additional retrieval features](appconfig-agent-how-to-use-additional-features.md "appconfig-agent-how-to-use-additional-features.md").

## Data encryption at rest for AWS AppConfig

AWS AppConfig provides encryption by default to protect customer data at rest using
AWS owned keys.

**AWS owned keys** — AWS AppConfig uses these keys by default
to automatically encrypt data deployed by the service and hosted in the AWS AppConfig data
store. You can't view, manage, or use AWS owned keys, or audit their use. However, you
don't have to take any action or change any programs to protect the keys that encrypt
your data. For more information, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
in the _AWS Key Management Service Developer Guide_.

While you can't disable this layer of encryption or select an alternate encryption
type, you can specify a customer managed key to be used when you save configuration data hosted in
the AWS AppConfig data store and when you deploy your configuration data.

**Customer managed keys** — AWS AppConfig supports the use of a
symmetric customer managed key that you create, own, and manage to add a second layer of
encryption over the existing AWS owned key. Because you have full control of this
layer of encryption, you can perform such tasks as:

- Establishing and maintaining key policies and grants
- Establishing and maintaining IAM policies
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion

For more information, see [Customer managed
key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

**AWS AppConfig supports customer managed keys**

AWS AppConfig offers support for customer managed key encryption for configuration data. For
configuration versions saved to the AWS AppConfig hosted data store, customers can set a
`KmsKeyIdentifier` on the corresponding configuration profile. Each time
a new version of configuration data is created using the
`CreateHostedConfigurationVersion` API operation, AWS AppConfig generates an
AWS KMS data key from the `KmsKeyIdentifier` to encrypt the data before storing
it. When the data is later accessed, either during the
`GetHostedConfigurationVersion` or `StartDeployment` API
operations, AWS AppConfig decrypts the configuration data using information about the generated
data key.

AWS AppConfig also offers support for customer managed key encryption for deployed configuration data.
To encrypt configuration data, customers can provide a `KmsKeyIdentifier` to
their deployment. AWS AppConfig generates the AWS KMS data key with this
`KmsKeyIdentifier` to encrypt data on the `StartDeployment`
API operation.

**AWS AppConfig encryption access**

When creating a customer managed key, use the following key policy to ensure that the key can be
used.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow use of the key",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`role_name`"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

To encrypt hosted configuration data with a customer managed key, the identity calling
`CreateHostedConfigurationVersion` needs the following policy statement
which can be assigned to a user, group, or role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:GenerateDataKey",
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-ID`"
 }
 ]
}`

```

If you are using a Secrets Manager secret or any other configuration data encrypted with a
customer managed key, your `retrievalRoleArn` will need `kms:Decrypt` to
decrypt and retrieve the data.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-ID`"
 }
 ]
}`

```

When calling the AWS AppConfig [StartDeployment](../../2019-10-09/APIReference/API_appconfigdata_StartDeployment.md "../../2019-10-09/APIReference/API_appconfigdata_StartDeployment.md") API operation, the identity calling
`StartDeployment` needs the following IAM policy which can be assigned
to a user, group, or role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "kms:GenerateDataKey*"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-ID`"
 }
 ]
}`

```

When calling the AWS AppConfig [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md") API operation, the identity calling
`GetLatestConfiguration` needs the following policy which can be assigned
to a user, group, or role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-ID`"
 }
 ]
}`

```

**Encryption context**

An [encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is an optional set of key-value pairs that contain additional
contextual information about the data.

AWS KMS uses the encryption context as additional authenticated data to support
authenticated encryption. When you include an encryption context in a request to encrypt
data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you
include the same encryption context in the request.

**AWS AppConfig encryption context**: AWS AppConfig uses an encryption
context in all AWS KMS cryptographic operations for encrypted hosted configuration data
and deployments. The context contains a key corresponding to the type of data and a
value that identifies the specific data item.

**Monitoring your encryption keys for AWS**

When you use an AWS KMS customer managed keys with AWS AppConfig, you can use AWS CloudTrail or Amazon CloudWatch Logs to
track requests that AWS AppConfig sends to AWS KMS.

The following example is a CloudTrail event for `Decrypt` to monitor AWS KMS
operations called by AWS AppConfig to access data encrypted by your customer managed key:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AWSService",
        "invokedBy": "appconfig.amazonaws.com"
    },
    "eventTime": "2023-01-03T02:22:28z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "`Region`",
    "sourceIPAddress": "172.12.34.56",
    "userAgent": "ExampleDesktop/1.0 (V1; OS)",
    "requestParameters": {
        "encryptionContext": {
            "aws:appconfig:deployment:arn": "arn:aws:appconfig:`Region`:`account_ID`:application/`application_ID`/environment/`environment_ID`/deployment/`deployment_ID`"
        },
        "keyId": "arn:aws:kms:`Region`:`account_ID`:key/`key_ID`",
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT"
    },
    "responseElements": null,
    "requestID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "eventID": "ff000af-00eb-00ce-0e00-ea000fb0fba0SAMPLE",
    "readOnly": true,
    "resources": [
        {
            "accountId": "`account_ID`",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:`Region`:`account_ID`:`key_ID`"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "`account_ID`",
    "sharedEventID": "dc129381-1d94-49bd-b522-f56a3482d088"
}
```

## Access AWS AppConfig using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS AppConfig. You can access AWS AppConfig as if it were in your VPC, without the use of an
internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your
VPC don't need public IP addresses to access AWS AppConfig.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network
interface in each subnet that you enable for the interface endpoint. These are
requester-managed network interfaces that serve as the entry point for traffic destined
for AWS AppConfig.

For more information, see [Access
AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

### Considerations for AWS AppConfig

Before you set up an interface endpoint for AWS AppConfig, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the
_AWS PrivateLink Guide_.

AWS AppConfig supports making calls to the [`appconfig`](../../2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md "../../2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md") and [`appconfigdata`](../../2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md "../../2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md") services through the interface
endpoint.

### Create an interface endpoint for AWS AppConfig

You can create an interface endpoint for AWS AppConfig using either the Amazon VPC console
or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

Create an interface endpoint for AWS AppConfig using the following service
names:

```
com.amazonaws.`region`.appconfig
```

```
com.amazonaws.`region`.appconfigdata
```

If you enable private DNS for the interface endpoint, you can make API requests to
AWS AppConfig using its default Regional DNS name. For example,
`appconfig.us-east-1.amazonaws.com` and
`appconfigdata.us-east-1.amazonaws.com`.

### Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface
endpoint. The default endpoint policy allows full access to AWS AppConfig through the
interface endpoint. To control the access allowed to AWS AppConfig from your VPC, attach
a custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services
using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for AWS AppConfig actions

The following is an example of a custom endpoint policy. When you attach this
policy to your interface endpoint, it grants access to the listed AWS AppConfig
actions for all principals on all resources.

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "`appconfig`:`CreateApplication`",
            "`appconfig`:`CreateEnvironment`",
            "`appconfig`:`CreateConfigurationProfile`",
            "`appconfig`:`StartDeployment`",
            "`appconfig`:`GetLatestConfiguration`"
            "`appconfig`:`StartConfigurationSession`"
         ],
         "Resource":"*"
      }
   ]
}
```

## Secrets Manager key rotation

This section describes important security information about AWS AppConfig integration with
Secrets Manager. For information about Secrets Manager, see [What is AWS Secrets Manager?](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md") in the
_AWS Secrets Manager User Guide_.

### Setting up automatic rotation of Secrets Manager secrets deployed by AWS AppConfig

_Rotation_ is the process of periodically updating a secret
stored in Secrets Manager. When you rotate a secret, you update the credentials in both the
secret and the database or service. You can configure automatic secrets rotation in
Secrets Manager by using an AWS Lambda function to update the secret and the database. For more
information, see [Rotate AWS Secrets Manager
secrets](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md") in the _AWS Secrets Manager User Guide_.

To enable key rotation of Secrets Manager secrets deployed by AWS AppConfig, update your rotation
Lambda function and deploy the rotated secret.

###### Note

Deploy your AWS AppConfig configuration profile after your secret has been rotated
and fully updated to the new version. You can determine if the secret rotated
because the status of `VersionStage` changes from
`AWSPENDING` to `AWSCURRENT`. Secret rotation
completion occurs within the Secrets Manager Rotation Templates `finish_secret`
function.

Here is an example function that starts an AWS AppConfig deployment after a secret is
rotated.

```
import time
import boto3
client = boto3.client('appconfig')

def finish_secret(service_client, arn, new_version):
    """Finish the rotation by marking the pending secret as current
    This method finishes the secret rotation by staging the secret staged AWSPENDING with the AWSCURRENT stage.
    Args:
        service_client (client): The secrets manager service client
        arn (string): The secret ARN or other identifier
        new_version (string): The new version to be associated with the secret
    """
    # First describe the secret to get the current version
    metadata = service_client.describe_secret(SecretId=arn)
    current_version = None
    for version in metadata["VersionIdsToStages"]:
        if "AWSCURRENT" in metadata["VersionIdsToStages"][version]:
            if version == new_version:
                # The correct version is already marked as current, return
                logger.info("finishSecret: Version %s already marked as AWSCURRENT for %s" % (version, arn))
                return
            current_version = version
            break

    # Finalize by staging the secret version current
    service_client.update_secret_version_stage(SecretId=arn, VersionStage="AWSCURRENT", MoveToVersionId=new_version, RemoveFromVersionId=current_version)

    # Deploy rotated secret
    response = client.start_deployment(
            ApplicationId='TestApp',
            EnvironmentId='TestEnvironment',
            DeploymentStrategyId='TestStrategy',
            ConfigurationProfileId='ConfigurationProfileId',
            ConfigurationVersion=new_version,
            KmsKeyIdentifier=key,
            Description='Deploy secret rotated at ' + str(time.time())
        )

    logger.info("finishSecret: Successfully set AWSCURRENT stage to version %s for secret %s." % (new_version, arn))
```
