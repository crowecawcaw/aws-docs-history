# Connect Amazon S3 Access Grants with Studio

JupyterLab notebooks

Use the following information to grant Amazon S3 Access Grants in Studio
JupyterLab notebooks.

After Amazon S3 Access Grants is set up, [add the following
permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") to your domain or user [execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role "sagemaker-roles.md#sagemaker-roles-get-execution-role").

- `us-east-1` is your
  AWS Region
- `111122223333` is your
  AWS account ID
- `S3-ACCESS-GRANT-ROLE` is your Amazon S3 Access
  Grant role

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowDataAccessAPI",
 "Effect": "Allow",
 "Action": [
 "s3:GetDataAccess"
 ],
 "Resource": [
 "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 ]
 },
 {
 "Sid": "RequiredForTIP",
 "Effect": "Allow",
 "Action": "sts:SetContext",
 "Resource": "arn:aws:iam::`111122223333`:role/`S3-ACCESS-GRANT-ROLE`"
 }
 ]
}`

```

Ensure that your Amazon S3 Access Grants role's trust policy allows the
`sts:SetContext` and `sts:AssumeRole` actions. The following is an
example policy for when you [update your role trust
policy](../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md "../../../IAM/latest/UserGuide/id_roles_update-role-trust-policy.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "access-grants.s3.amazonaws.com"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`111122223333`",
 "aws:SourceArn": "arn:aws:s3:`us-east-1`:`111122223333`:access-grants/default"
 }
 }
 }
 ]
}`

```

## Use Amazon S3 Access Grants to call

Amazon S3

The following is an example Python script showing how Amazon S3 Access Grants can be used
to call Amazon S3. This assumes you have already successfully set up trusted identity
propagation with SageMaker AI.

```
import boto3
from botocore.config import Config

def get_access_grant_credentials(account_id: str, target: str,
                                 permission: str = 'READ'):
    s3control = boto3.client('s3control')
    response = s3control.get_data_access(
        AccountId=account_id,
        Target=target,
        Permission=permission
    )
    return response['Credentials']

def create_s3_client_from_credentials(credentials) -> boto3.client:
    return boto3.client(
        's3',
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )

# Create client
credentials = get_access_grant_credentials('`111122223333`',
                                        "s3://tip-enabled-bucket/tip-enabled-path/")
s3 = create_s3_client_from_credentials(credentials)

s3.list_objects(Bucket="tip-enabled-bucket", Prefix="tip-enabled-path/")
```

If you use a path to an Amazon S3 bucket where Amazon S3 access grant is not enabled, the call
will fail.

For other programming languages, see [Managing access with Amazon S3 Access
Grants](../../../AmazonS3/latest/userguide/access-grants.md "../../../AmazonS3/latest/userguide/access-grants.md") for more information.
