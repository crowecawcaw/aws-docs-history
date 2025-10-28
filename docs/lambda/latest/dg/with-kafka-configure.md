# Configuring self-managed Apache Kafka event sources for Lambda

Before you create an event source mapping for your self-managed Apache Kafka cluster, you need to ensure that your cluster and the VPC
it resides in are correctly configured. You also need to make sure that your Lambda function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md") has
the necessary IAM permissions.

Follow the instructions in the following sections to configure your self-managed Apache Kafka cluster and Lambda function. To learn how to
create the event source mapping, see [Adding a Kafka cluster as an event source](with-kafka-process.md#services-smaa-topic-add "with-kafka-process.md#services-smaa-topic-add").

###### Topics

- [Kafka cluster authentication](#smaa-authentication "#smaa-authentication")
- [API access and Lambda function permissions](#smaa-permissions "#smaa-permissions")
- [Configure network security](#services-kafka-vpc-config "#services-kafka-vpc-config")

## Kafka cluster authentication

Lambda supports several methods to authenticate with your self-managed Apache Kafka cluster. Make sure that you configure the
Kafka cluster to use one of these supported authentication methods. For more information about Kafka security, see
the [Security](http://kafka.apache.org/documentation.html#security "http://kafka.apache.org/documentation.html#security") section of the Kafka
documentation.

### SASL/SCRAM authentication

Lambda supports Simple Authentication and Security Layer/Salted Challenge Response Authentication Mechanism
(SASL/SCRAM) authentication with Transport Layer Security (TLS) encryption (`SASL_SSL`). Lambda sends the encrypted credentials to authenticate with
the cluster. Lambda doesn't support SASL/SCRAM with plaintext (`SASL_PLAINTEXT`). For more information about SASL/SCRAM authentication, see [RFC 5802](https://tools.ietf.org/html/rfc5802 "https://tools.ietf.org/html/rfc5802").

Lambda also supports SASL/PLAIN authentication. Because this mechanism uses clear text credentials, the connection to the
server must use TLS encryption to ensure that the credentials are protected.

For SASL authentication, you store the sign-in credentials as a secret in AWS Secrets Manager. For more information
about using Secrets Manager, see [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_.

###### Important

To use Secrets Manager for authentication, secrets must be stored in the same AWS region as your Lambda function.

### Mutual TLS authentication

Mutual TLS (mTLS) provides two-way authentication between the client and server. The client sends a
certificate to the server for the server to verify the client, and the server sends a certificate to the client
for the client to verify the server.

In self-managed Apache Kafka, Lambda acts as the client. You configure a client certificate (as a secret in Secrets Manager) to
authenticate Lambda with your Kafka brokers. The client certificate must be signed by a CA in the server's trust
store.

The Kafka cluster sends a server certificate to Lambda to authenticate the Kafka brokers with Lambda. The
server certificate can be a public CA certificate or a private CA/self-signed certificate. The public CA
certificate must be signed by a certificate authority (CA) that's in the Lambda trust store. For a private
CA/self-signed certificate, you configure the server root CA certificate (as a secret in Secrets Manager). Lambda uses
the root certificate to verify the Kafka brokers.

For more information about mTLS, see [Introducing mutual TLS authentication for Amazon MSK as an event source](https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-msk-as-an-event-source "https://aws.amazon.com/blogs/compute/introducing-mutual-tls-authentication-for-amazon-msk-as-an-event-source").

### Configuring the client certificate secret

The CLIENT_CERTIFICATE_TLS_AUTH secret requires a certificate field and a private key field. For an
encrypted private key, the secret requires a private key password. Both the certificate and private key must be
in PEM format.

###### Note

Lambda supports the [PBES1](https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1 "https://datatracker.ietf.org/doc/html/rfc2898/#section-6.1") (but not
PBES2) private key encryption algorithms.

The certificate field must contain a list of certificates, beginning with the client certificate, followed
by any intermediate certificates, and ending with the root certificate. Each certificate must start on a new
line with the following structure:

```
-----BEGIN CERTIFICATE-----
        <certificate contents>
-----END CERTIFICATE-----
```

Secrets Manager supports secrets up to 65,536 bytes, which is enough space for long certificate chains.

The private key must be in [PKCS #8](https://datatracker.ietf.org/doc/html/rfc5208 "https://datatracker.ietf.org/doc/html/rfc5208")
format, with the following structure:

```
-----BEGIN PRIVATE KEY-----
         <private key contents>
-----END PRIVATE KEY-----
```

For an encrypted private key, use the following structure:

```
-----BEGIN ENCRYPTED PRIVATE KEY-----
          <private key contents>
-----END ENCRYPTED PRIVATE KEY-----
```

The following example shows the contents of a secret for mTLS authentication using an encrypted private key.
For an encrypted private key, include the private key password in the secret.

```
{"privateKeyPassword":"testpassword",
"certificate":"-----BEGIN CERTIFICATE-----
MIIE5DCCAsygAwIBAgIRAPJdwaFaNRrytHBto0j5BA0wDQYJKoZIhvcNAQELBQAw
...
j0Lh4/+1HfgyE2KlmII36dg4IMzNjAFEBZiCRoPimO40s1cRqtFHXoal0QQbIlxk
cmUuiAii9R0=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFgjCCA2qgAwIBAgIQdjNZd6uFf9hbNC5RdfmHrzANBgkqhkiG9w0BAQsFADBb
...
rQoiowbbk5wXCheYSANQIfTZ6weQTgiCHCCbuuMKNVS95FkXm0vqVD/YpXKwA/no
c8PH3PSoAaRwMMgOSA2ALJvbRz8mpg==
-----END CERTIFICATE-----",
"privateKey":"-----BEGIN ENCRYPTED PRIVATE KEY-----
MIIFKzBVBgkqhkiG9w0BBQ0wSDAnBgkqhkiG9w0BBQwwGgQUiAFcK5hT/X7Kjmgp
...
QrSekqF+kWzmB6nAfSzgO9IaoAaytLvNgGTckWeUkWn/V0Ck+LdGUXzAC4RxZnoQ
zp2mwJn2NYB7AZ7+imp0azDZb+8YG2aUCiyqb6PnnA==
-----END ENCRYPTED PRIVATE KEY-----"
}
```

### Configuring the server root CA certificate secret

You create this secret if your Kafka brokers use TLS encryption with certificates signed by a private CA.
You can use TLS encryption for VPC, SASL/SCRAM, SASL/PLAIN, or mTLS authentication.

The server root CA certificate secret requires a field that contains the Kafka broker's root CA certificate
in PEM format. The following example shows the structure of the secret.

```
{"certificate":"-----BEGIN CERTIFICATE-----
MIID7zCCAtegAwIBAgIBADANBgkqhkiG9w0BAQsFADCBmDELMAkGA1UEBhMCVVMx
EDAOBgNVBAgTB0FyaXpvbmExEzARBgNVBAcTClNjb3R0c2RhbGUxJTAjBgNVBAoT
HFN0YXJmaWVsZCBUZWNobm9sb2dpZXMsIEluYy4xOzA5BgNVBAMTMlN0YXJmaWVs
ZCBTZXJ2aWNlcyBSb290IENlcnRpZmljYXRlIEF1dG...
-----END CERTIFICATE-----"
}
```

## API access and Lambda function permissions

In addition to accessing your self-managed Kafka cluster, your Lambda function needs permissions to perform
various API actions. You add these permissions to the function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md"). If your users need access to any API actions, add the required permissions to the
identity policy for the AWS Identity and Access Management (IAM) user or role.

### Required Lambda function permissions

To create and store logs in a log group in Amazon CloudWatch Logs, your Lambda function must have the following
permissions in its execution role:

- [logs:CreateLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md")
- [logs:CreateLogStream](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogStream.md")
- [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md")

### Optional Lambda function permissions

Your Lambda function might also need permissions to:

- Describe your Secrets Manager secret.
- Access your AWS Key Management Service (AWS KMS) customer managed key.
- Access your Amazon VPC.
- Send records of failed invocations to a destination.

#### Secrets Manager and AWS KMS permissions

Depending on the type of access control that you're configuring for your Kafka brokers, your Lambda function
might need permission to access your Secrets Manager secret or to decrypt your AWS KMS customer managed key. To access these
resources, your function's execution role must have the following permissions:

- [secretsmanager:GetSecretValue](../../../secretsmanager/latest/apireference/API_GetSecretValue.md "../../../secretsmanager/latest/apireference/API_GetSecretValue.md")
- [kms:Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md")

#### VPC permissions

If only users within a VPC can access your self-managed Apache Kafka cluster, your Lambda function must have permission to
access your Amazon VPC resources. These resources include your VPC, subnets, security groups, and network
interfaces. To access these resources, your function's execution role must have the following
permissions:

- [ec2:CreateNetworkInterface](../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_CreateNetworkInterface.md")
- [ec2:DescribeNetworkInterfaces](../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md "../../../AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.md")
- [ec2:DescribeVpcs](../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcs.md")
- [ec2:DeleteNetworkInterface](../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md "../../../AWSEC2/latest/APIReference/API_DeleteNetworkInterface.md")
- [ec2:DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")
- [ec2:DescribeSecurityGroups](../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md "../../../AWSEC2/latest/APIReference/API_DescribeSecurityGroups.md")

### Adding permissions to your execution role

To access other AWS services that your self-managed Apache Kafka cluster uses, Lambda uses the permissions policies that you
define in your Lambda function's [execution role](lambda-intro-execution-role.md "lambda-intro-execution-role.md").

By default, Lambda is not permitted to perform the required or optional actions for a self-managed Apache Kafka cluster. You
must create and define these actions in an [IAM trust policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md") for your execution role. This example shows how you might create a policy that allows
Lambda to access your Amazon VPC resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "ec2:CreateNetworkInterface",
 "ec2:DescribeNetworkInterfaces",
 "ec2:DescribeVpcs",
 "ec2:DeleteNetworkInterface",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource":"*"
 }
 ]
 }`

```

### Granting users access with an IAM policy

By default, users and roles don't have permission to perform [event source API operations](invocation-eventsourcemapping.md#event-source-mapping-api "invocation-eventsourcemapping.md#event-source-mapping-api"). To grant access to users in your
organization or account, you create or update an identity-based policy. For more information, see [Controlling access to AWS resources
using policies](../../../IAM/latest/UserGuide/access_controlling.md "../../../IAM/latest/UserGuide/access_controlling.md") in the _IAM User Guide_.

## Configure network security

To give Lambda full access to self-managed Apache Kafka through your event source mapping, either your cluster must use a public endpoint
(public IP address), or you must provide access to the Amazon VPC you created the cluster in.

When you use self-managed Apache Kafka with Lambda, create [AWS PrivateLink VPC endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") that provide your function
access to the resources in your Amazon VPC.

###### Note

AWS PrivateLink VPC endpoints are required for functions with event source mappings that use the default (on-demand) mode
for event pollers. If your event source mapping uses [provisioned mode](invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode "invocation-eventsourcemapping.md#invocation-eventsourcemapping-provisioned-mode"), you don't need to configure AWS PrivateLink VPC endpoints.

Create an endpoint to provide access to the following resources:

- Lambda — Create an endpoint for the Lambda service principal.
- AWS STS — Create an endpoint for the AWS STS in order for a service principal to assume a role on your behalf.
- Secrets Manager — If your cluster uses Secrets Manager to store credentials, create an endpoint for Secrets Manager.

Alternatively, configure a NAT gateway on each public subnet in the Amazon VPC. For more information,
see [Enable internet access for VPC-connected Lambda functions](configuration-vpc-internet.md "configuration-vpc-internet.md").

When you create an event source mapping for self-managed Apache Kafka, Lambda checks whether Elastic Network Interfaces (ENIs)
are already present for the subnets and security groups configured for your Amazon VPC. If Lambda finds existing ENIs, it
attempts to re-use them. Otherwise, Lambda creates new ENIs to connect to the event source and invoke your function.

###### Note

Lambda functions always run inside VPCs owned by the Lambda service. Your function's VPC configuration
does not affect the event source mapping. Only the networking configuration of the event source's determines
how Lambda connects to your event source.

Configure the security groups for the Amazon VPC containing your cluster. By default,
self-managed Apache Kafka uses the following ports: `9092`.

- Inbound rules – Allow all traffic on the default broker port for the security group associated with your event source.
  Alternatively, you can use a self-referencing security group rule to allow access from instances within the same security group.
- Outbound rules – Allow all traffic on port `443` for external destinations if your function needs to communicate with AWS services.
  Alternatively, you can also use a self-referencing security group rule to limit access to the broker if you don't need to communicate with other AWS services.
- Amazon VPC endpoint inbound rules — If you are using an Amazon VPC endpoint, the security group associated with your Amazon VPC endpoint must allow inbound traffic
  on port `443` from the cluster security group.

If your cluster uses authentication, you can also restrict the endpoint policy for the Secrets Manager endpoint.
To call the Secrets Manager API, Lambda uses your function role, not the Lambda service principal.

###### Example VPC endpoint policy — Secrets Manager endpoint

```
{
      "Statement": [
          {
              "Action": "secretsmanager:GetSecretValue",
              "Effect": "Allow",
              "Principal": {
                  "AWS": [
                      "arn:aws::iam::123456789012:role/`my-role`"
                  ]
              },
              "Resource": "arn:aws::secretsmanager:`us-west-2`:123456789012:secret:`my-secret`"
          }
      ]
  }
```

When you use Amazon VPC endpoints, AWS routes your API calls to invoke your function using the endpoint's Elastic Network Interface (ENI).
The Lambda service principal needs to call `lambda:InvokeFunction` on any roles and functions that use those ENIs.

By default, Amazon VPC endpoints have open IAM policies that allow broad access to resources. Best practice is to restrict these
policies to perform the needed actions using that endpoint. To ensure that your event source mapping is able to invoke your Lambda
function, the VPC endpoint policy must allow the Lambda service principal to call `sts:AssumeRole` and
`lambda:InvokeFunction`. Restricting your VPC endpoint policies to allow only API calls originating within your organization
prevents the event source mapping from functioning properly, so `"Resource": "*"` is required in these policies.

The following example VPC endpoint policies show how to grant the required access to the Lambda service principal for the
AWS STS and Lambda endpoints.

###### Example VPC Endpoint policy — AWS STS endpoint

```
{
      "Statement": [
          {
              "Action": "sts:AssumeRole",
              "Effect": "Allow",
              "Principal": {
                  "Service": [
                      "lambda.amazonaws.com"
                  ]
              },
              "Resource": "*"
          }
      ]
    }
```

###### Example VPC Endpoint policy — Lambda endpoint

```
{
      "Statement": [
          {
              "Action": "lambda:InvokeFunction",
              "Effect": "Allow",
              "Principal": {
                  "Service": [
                      "lambda.amazonaws.com"
                  ]
              },
              "Resource": "*"
          }
      ]
  }
```
