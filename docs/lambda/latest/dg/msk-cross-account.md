# Creating cross-account event source mappings in Lambda

You can use [multi-VPC private
connectivity](../../../msk/latest/developerguide/aws-access-mult-vpc.md "../../../msk/latest/developerguide/aws-access-mult-vpc.md") to connect a Lambda function to a provisioned MSK cluster in a different AWS account.
Multi-VPC connectivity uses AWS PrivateLink, which keeps all traffic within the AWS network.

###### Note

You can't create cross-account event source mappings for serverless MSK clusters.

To create a cross-account event source mapping, you must first [configure multi-VPC
connectivity for the MSK cluster](../../../msk/latest/developerguide/aws-access-mult-vpc.md#mvpc-cluster-owner-action-turn-on "../../../msk/latest/developerguide/aws-access-mult-vpc.md#mvpc-cluster-owner-action-turn-on"). When you create the event source mapping, use the managed VPC connection
ARN instead of the cluster ARN, as shown in the following examples. The [CreateEventSourceMapping](../api/API_CreateEventSourceMapping.md "../api/API_CreateEventSourceMapping.md") operation
also differs depending on which authentication type the MSK cluster uses.

###### Example — Create cross-account event source mapping for cluster that uses IAM authentication

When the cluster uses [IAM role-based authentication](msk-cluster-auth.md#msk-iam-auth "msk-cluster-auth.md#msk-iam-auth"),
you don't need a [SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object. Example:

```
aws lambda create-event-source-mapping \
  --event-source-arn arn:aws:kafka:`us-east-1:111122223333`:vpc-connection/`444455556666/my-cluster-name/51jn98b4-0a61-46cc-b0a6-61g9a3d797d5-7` \
  --topics AWSKafkaTopic \
  --starting-position LATEST \
  --function-name my-kafka-function
```

###### Example — Create cross-account event source mapping for cluster that uses SASL/SCRAM authentication

If the cluster uses [SASL/SCRAM authentication](msk-cluster-auth.md#msk-sasl-scram "msk-cluster-auth.md#msk-sasl-scram"),
you must include a [SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object that specifies `SASL_SCRAM_512_AUTH`
and a Secrets Manager secret ARN.

There are two ways to use secrets for cross-account Amazon MSK event source mappings with SASL/SCRAM authentication:

- Create a secret in the Lambda function account and sync it with the cluster secret.
  [Create a rotation](../../../secretsmanager/latest/userguide/rotating-secrets.md "../../../secretsmanager/latest/userguide/rotating-secrets.md")
  to keep the two secrets in sync. This option allows you to control the secret from the function account.
- Use the secret that's associated with the MSK cluster. This secret must allow cross-account
  access to the Lambda function account. For more information, see [Permissions to AWS Secrets Manager
  secrets for users in a different account](../../../secretsmanager/latest/userguide/auth-and-access_examples_cross.md "../../../secretsmanager/latest/userguide/auth-and-access_examples_cross.md").

```
`aws lambda create-event-source-mapping \
 --event-source-arn arn:aws:kafka:`us-east-1:111122223333`:vpc-connection/`444455556666/my-cluster-name/51jn98b4-0a61-46cc-b0a6-61g9a3d797d5-7` \
 --topics AWSKafkaTopic \
 --starting-position LATEST \
 --function-name my-kafka-function \
 --source-access-configurations `'[{"Type": "SASL_SCRAM_512_AUTH","URI": "arn:aws:secretsmanager:us-east-1:444455556666:secret:my-secret"}]'``
```

###### Example — Create cross-account event source mapping for cluster that uses mTLS authentication

If the cluster uses [mTLS authentication](msk-cluster-auth.md#msk-mtls "msk-cluster-auth.md#msk-mtls"),
you must include a [SourceAccessConfiguration](../api/API_SourceAccessConfiguration.md "../api/API_SourceAccessConfiguration.md") object that specifies `CLIENT_CERTIFICATE_TLS_AUTH`
and a Secrets Manager secret ARN. The secret can be stored in the cluster account or the Lambda function account.

```
`aws lambda create-event-source-mapping \
 --event-source-arn arn:aws:kafka:`us-east-1:111122223333`:vpc-connection/`444455556666/my-cluster-name/51jn98b4-0a61-46cc-b0a6-61g9a3d797d5-7` \
 --topics AWSKafkaTopic \
 --starting-position LATEST \
 --function-name my-kafka-function \
 --source-access-configurations `'[{"Type": "CLIENT_CERTIFICATE_TLS_AUTH","URI": "arn:aws:secretsmanager:us-east-1:444455556666:secret:my-secret"}]'``
```
