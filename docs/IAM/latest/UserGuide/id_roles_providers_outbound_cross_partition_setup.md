

# Setting up cross-partition identity federation
<a name="id_roles_providers_outbound_cross_partition_setup"></a>

Cross-partition identity federation works as a two-step exchange: your workload calls `sts:GetWebIdentityToken` to obtain a JWT from AWS STS in the source partition, then exchanges that token for temporary credentials from AWS STS in the destination partition by calling `sts:AssumeRoleWithWebIdentity`.

Establishing this flow involves a one-time setup phase and a runtime phase that repeats each time the workload needs credentials in the destination partition. This page explains how to configure the source and destination accounts.

**Setup phase**

1. In the source partition, enable outbound identity federation for your account. For instructions, see [Enable outbound identity federation for your account](id_roles_providers_outbound_getting_started.md#enable-outbound-federation).

1. In the source partition, create an IAM principal or choose an existing one, and grant it permission to call `sts:GetWebIdentityToken`. Use IAM policy conditions to restrict the permitted audiences, token duration, and signing algorithms. For instructions, see [Controlling access with IAM policies](id_roles_providers_outbound_policies.md).

1. In the destination partition, create an OpenID Connect (OIDC) identity provider using the source account's issuer URL. Make sure the provider's client ID list includes the audience your workload will use with `GetWebIdentityToken`. For instructions, see [Create an OpenID Connect (OIDC) identity provider in IAM](id_roles_providers_create_oidc.md).

1. In the destination partition, create an IAM role or choose an existing one for the source IAM principal to assume. Configure the role's trust policy to trust the OIDC identity provider you created and allow `sts:AssumeRoleWithWebIdentity`. For instructions, see [Who can assume a role](id_roles_providers_outbound_cross_partition_controls.md#cross-partition-destination-token-exchange).

**Runtime phase**

1. Using credentials for the IAM principal in the source partition, call [sts:GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) with the audience you configured in the destination account's OIDC identity provider.
**Note**  
For cross-partition identity federation, specify exactly one audience when calling `GetWebIdentityToken`. Tokens requested with multiple audiences can't be exchanged for temporary credentials using `AssumeRoleWithWebIdentity`.

1. AWS STS in the source partition returns a short-lived JWT that represents the source IAM principal's identity.

1. Call [sts:AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) on the AWS STS endpoint in the destination partition, passing the JWT, the ARN of the destination role you configured during setup, and a role session name (`RoleSessionName`).

1. AWS STS in the destination partition validates the JWT and evaluates the destination role's trust policy. If the request is allowed, AWS STS returns temporary credentials for that role.

1. Use the temporary credentials to access AWS resources or communicate with an AWS service in the destination partition.

The following AWS CLI example shows the runtime phase, using `us-east-1` in the `aws` partition as the source Region and `cn-north-1` in the `aws-cn` partition as the destination Region. Use credentials for the source IAM principal to call `GetWebIdentityToken`. The `AssumeRoleWithWebIdentity` call authenticates using the JWT returned by `GetWebIdentityToken` and doesn't require AWS credentials.

```
# Source partition (aws): get a short-lived JWT
TOKEN=$(aws sts get-web-identity-token \
  --region us-east-1 \
  --endpoint-url https://sts.us-east-1.amazonaws.com \
  --audience "{{your-audience}}" \
  --signing-algorithm ES384 \
  --duration-seconds 300 \
  --query WebIdentityToken --output text)

# Destination partition (aws-cn): exchange it for temporary credentials
aws sts assume-role-with-web-identity \
  --region cn-north-1 \
  --role-arn arn:aws-cn:iam::{{111122223333}}:role/DestinationWorkloadRole \
  --role-session-name cross-partition-session \
  --web-identity-token "$TOKEN" \
  --no-sign-request
```

The following example shows the same flow using the AWS SDK for Python (Boto3).

```
import boto3
from botocore import UNSIGNED
from botocore.config import Config

# Source partition (aws): get a short-lived JWT from the Regional STS endpoint
source_sts = boto3.client(
    'sts',
    region_name='us-east-1',
    endpoint_url='https://sts.us-east-1.amazonaws.com'
)
token = source_sts.get_web_identity_token(
    Audience=['{{your-audience}}'],
    SigningAlgorithm='ES384',
    DurationSeconds=300
)['WebIdentityToken']

# Destination partition (aws-cn): exchange it for temporary credentials.
# AssumeRoleWithWebIdentity doesn't require AWS credentials.
destination_sts = boto3.client(
    'sts',
    region_name='cn-north-1',
    config=Config(signature_version=UNSIGNED)
)
credentials = destination_sts.assume_role_with_web_identity(
    RoleArn='arn:aws-cn:iam::{{111122223333}}:role/DestinationWorkloadRole',
    RoleSessionName='cross-partition-session',
    WebIdentityToken=token
)['Credentials']
```