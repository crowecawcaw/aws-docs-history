# Adding a trusted account in AWS DRS

To add a trusted account, take the following steps:

1. Click **Add trusted accounts and create roles**.
2. Click **Add new trusted account**.
3. Enter an account ID and choose the relevant role or roles. There are 3 available
   options: Staging role, Network role, and Failback and in-AWS right-sizing roles.
4. Click **Add trusted accounts and roles**. A success
   message will appear at the top of the screen.

###### Note

Up to 10 accounts can be added in a single batch and up to 100 accounts for a single AWS
DRS account.

## Creating the Staging role

The **Staging role** is required to utilize various
AWS Elastic Disaster Recovery capabilities, including the multi-account feature. To automatically create the
role and the attached required policies, simply create it for a specific account via the
**Trusted accounts** page.

This action will create the DRSStagingAccountRole role which includes the
AWSElasticDisasterRecoveryStagingAccountPolicy_v2 policy and the following trust policy
permissions:

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
 "Action": [
 "sts:AssumeRole",
 "sts:SetSourceIdentity"
 ],
 "Condition": {
 "StringLike": {
 "sts:SourceIdentity": "{{target_account}}",
 "aws:SourceAccount": "{{target_account}}"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:drs:*:*:source-server/*"
 }
 }
 }
 ]
 }`

```

## Creating the Network role

The **Network role** is required to utilize various
AWS Elastic Disaster Recovery capabilities, including the network replication feature. To automatically create
the role and the attached required policies, simply create it for a specific account via the
**Trusted accounts** page.

This action will create the DRSSourceNetworkRole role which includes the
AWSElasticDisasterRecoverySourceNetworkPolicy policy and the following trust policy
permissions:

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

## Creating the Failback and in-AWS

right-sizing roles

The **Failback and in-AWS right-sizing roles** are required
to utilize various AWS Elastic Disaster Recovery capabilities, including cross account failback and in-AWS
features. Each Trusted AWS Account will need a set of these IAM roles for functionality. You
can automatically create these roles, and their attached policies, via the **Trusted accounts** section of the AWS Elastic Disaster Recovery console. The roles
required are:

1. **DRSCrossAccountReplicationRole**
2. **DRSCrossAccountAgentRole**
3. **DRSCrossAccountAgentAuthorizedRole**

If you intend to create these roles manually, please ensure they are placed in the
`service-role` path, with the Role name ending in an underscore and the trusted
Account ID, as specified below:

```
arn:aws:iam::`account-id`:role/service-role/DRSCrossAccountReplicationRole`_trustedAccountID`
```

### DRSCrossAccountReplicationRole

The **DRSCrossAccountReplicationRole** contains the
following trust policy. If you plan to use the policy as a template, replace the
`account-id` the Trusted AWS Account ID.

The **DRSCrossAccountReplicationRole** has the AWS
Managed Policy **AWSElasticDisasterRecoveryCrossAccountReplicationPolicy** attached.

### DRSCrossAccountAgentRole

The **DRSCrossAccountAgentRole** contains the following
trust policy. If you plan to use the policy as a template, replace the
`trustedAccount` with the Trusted AWS Account ID, and replace
`sourceAccount` with the source AWS Account ID.

The **DRSCrossAccountAgentRole** has the AWS Managed
Policy **AWSElasticDisasterRecoveryEc2InstancePolicy**
attached.

### DRSCrossAccountAgentAuthorizedRole

The **DRSCrossAccountAgentAuthorizedRole** contains the
following trust policy. If you plan to use the policy as a template, replace the
`account-id` with the Trusted AWS Account ID.

The **DRSCrossAccountReplicationRole** has the following
inline policy attached. If you plan to use the policy as a template, replace the
`trustedAccount` with the Trusted AWS Account ID, and replace
`sourceAccount` with the source AWS Account ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sts:AssumeRole",
 "sts:TagSession"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/service-role/DRSCrossAccountAgentRole_`sourceAccount`",
 "Effect": "Allow"
 },
 {
 "Condition": {
 "StringLike": {
 "sts:SourceIdentity": "i-*"
 }
 },
 "Action": [
 "sts:SetSourceIdentity"
 ],
 "Resource": "arn:aws:iam::`111122223333`:role/service-role/DRSCrossAccountAgentRole_`sourceAccount`",
 "Effect": "Allow"
 }
 ]
}`

```
