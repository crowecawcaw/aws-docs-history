# Use a customer managed key to encrypt the cluster secret

By default, AWS PCS stores the cluster secret in AWS Secrets Manager encrypted with an
AWS managed key. AWS PCS doesn't require additional authorization to use the
AWS managed key. Alternatively, you can encrypt the cluster secret with a customer managed key. The
customer managed key must be a symmetric encryption key (`SYMMETRIC_DEFAULT`,
`ENCRYPT_DECRYPT`) in the same AWS account and AWS Region as the cluster.

The AWS managed policy `AWSPCSServiceRolePolicy` that is attached to the
AWS PCS service-linked role (`AWSServiceRoleForPCS`) grants no `kms:`
permissions. If you attach a customer managed key to the secret without
editing the key policy, the service-linked role does not have the ability to access the secret. As a result, secret
rotation and compute node operations fail. For more information about the AWS PCS service-linked role, see
[Service-linked roles for AWS PCS](service-linked-roles.md "service-linked-roles.md").

## Required key policy

Add the following statement to the customer managed key's key policy. Replace
`account-id` with your AWS account ID. This statement gives the
AWS PCS service-linked role (`AWSServiceRoleForPCS`) permission to use the
customer managed key to protect the cluster secret.

```
{
   "Sid": "Allow service-linked role use of the customer managed key",
   "Effect": "Allow",
   "Principal": {
       "AWS": [
           "arn:aws:iam::`account-id`:role/aws-service-role/pcs.amazonaws.com/AWSServiceRoleForPCS"
       ]
   },
   "Action": [
       "kms:Decrypt",
       "kms:GenerateDataKey",
       "kms:DescribeKey"
   ],
   "Resource": "*"
}
```

For more information, see:

- [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md") in the
  _AWS CLI Command Reference_
- [create-key](../../../cli/latest/reference/kms/create-key.md "../../../cli/latest/reference/kms/create-key.md") in the
  _AWS CLI Command Reference_
- [Find the key ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the
  _AWS Key Management Service Developer Guide_
- [AWS Key Management Service](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md") in the
  _AWS Key Management Service Developer Guide_
- The AWS PCS cluster secret is stored as a [managed secret](../../../secretsmanager/latest/userguide/integrating_pcs.md "../../../secretsmanager/latest/userguide/integrating_pcs.md") in AWS Secrets Manager.

## Permissions to change the encryption key

The permissions in the preceding section apply to the AWS PCS service-linked role. The
IAM principal that changes the encryption key attached to the secret needs its own permissions, which are separate
from the service-linked role. The principal needs the following permissions:

- `secretsmanager:UpdateSecret` on the cluster secret.
- `kms:Decrypt` on the outgoing key (the key that currently encrypts the
  secret).
- `kms:GenerateDataKey`, `kms:Encrypt`, and `kms:Decrypt`
  on the incoming key (the new key).

When you change the key, AWS Secrets Manager re-encrypts every stored version of the secret, including
the `AWSCURRENT` and `AWSPREVIOUS` versions.

For the procedure to attach the key, see [Attach the key and rotate the secret](#working-with_clusters_secrets_cmk-attach-and-rotate "#working-with_clusters_secrets_cmk-attach-and-rotate").

## Attach the key and rotate the secret

You attach the customer managed key to the cluster secret with the AWS Secrets Manager
`UpdateSecret` operation. AWS PCS provides no API parameter for the secret's
encryption key.

The following example attaches the customer managed key to the cluster secret. Replace the
placeholders with your values.

```
aws secretsmanager update-secret \
    --region `region` \
    --secret-id `secret-arn` \
    --kms-key-id `key-arn`
```

###### Note

The customer managed key must be a symmetric encryption key in the same AWS account and
AWS Region as the secret. You need the permissions listed in [Permissions to change the encryption key](#working-with_clusters_secrets_cmk-change-key-permissions "#working-with_clusters_secrets_cmk-change-key-permissions").

After you attach the customer managed key, proceed with rotation so that AWS PCS generates a new
cluster secret encrypted with the newly attached customer managed key. For the rotation procedure, see
[Rotate a cluster secret in AWS PCS](cluster-secret-rotation-procedure.md "cluster-secret-rotation-procedure.md").
