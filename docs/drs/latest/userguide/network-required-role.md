# Creating the required role for Elastic Disaster Recovery

In order to replicate network configurations between different accounts, you need to go
to the source account and create the **Network role** from the
**Trusted accounts** page. This will automatically create the
role and attached the required policies.

###### Note

This is only required if your target account is different from the source account.

To create the required role, take the following steps:

1. Go to your source account.
2. Go to the **Trusted accounts** page.
3. Click **Add trusted accounts and create roles**.
4. Click **Add new trusted account**.
5. Enter the target account ID and choose **Network
   role**.
6. Click **Add trusted accounts and roles**. A success
   message will appear at the top of the screen.
   This action will create the DRSSourceNetworkRole role that is required to utilize the feature.

This role includes the AWSElasticDisasterRecoverySourceNetworkPolicy policy and the
following trust policy permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "drs.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringLike": {
 "aws:SourceAccount": "{{target_account}}"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:drs:*:*:source-network/*"
 }
 }
 }
 ]
 }`

```

After you install the agent and create the relevant role, you can start replicating your
network configurations.
