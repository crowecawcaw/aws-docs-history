# IAM roles and trust policy for your integrations

In order for your integrations to work, you will need to add the following two IAM
roles as part of your configuration.

###### Note

IAM roles and trust policy are not required for using browser extensions.

###### Topics

- [IAM role for allowing the integration to call Amazon Q Business on your end user's behalf](#amazon-q-business-integrations-iam-allow-integration-access "#amazon-q-business-integrations-iam-allow-integration-access")
- [IAM role for allowing Amazon Q Business to monitor the resources that the integration creates in your account](#amazon-q-business-integrations-iam-allow-qbusiness-monitor "#amazon-q-business-integrations-iam-allow-qbusiness-monitor")
- [IAM trust policy for your integrations](#amazon-q-business-integrations-iam-trust-policy "#amazon-q-business-integrations-iam-trust-policy")

## IAM role for allowing the integration to call Amazon Q Business on your end user's behalf

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessConversationPermissions",
 "Effect": "Allow",
 "Action": [
 "qbusiness:Chat",
 "qbusiness:ChatSync",
 "qbusiness:PutFeedback",
 "qbusiness:DeleteConversation",
 "qbusiness:ListAttachments",
 "qbusiness:DeleteAttachment"
 ],
 "Resource": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 },
 {
 "Sid": "QBusinessKMSDecryptPermissions",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/[[key_id]]"
 ],
 "Condition": {
 "StringLike": {
 "kms:ViaService": [
 "qbusiness.us-east-1.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "QBusinessSetContextPermissions",
 "Effect": "Allow",
 "Action": [
 "sts:SetContext"
 ],
 "Resource": [
 "arn:aws:sts::*:self"
 ],
 "Condition": {
 "StringLike": {
 "aws:CalledViaLast": [
 "qbusiness.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

## IAM role for allowing Amazon Q Business to monitor the resources that the integration creates in your account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessIdCInstanceReadOnlyPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:ListApplications"
 ],
 "Resource": "arn:aws:sso:::instance/`idc-instance-id`"
 },
 {
 "Sid": "QBusinessIdCInstanceApplicationReadOnlyPermissions",
 "Effect": "Allow",
 "Action": [
 "sso:ListApplicationAccessScopes",
 "sso:GetApplicationAssignmentConfiguration",
 "sso:GetApplicationGrant",
 "sso:GetApplicationAuthenticationMethod"
 ],
 "Resource": "arn:aws:sso::111122223333:application/`idc-instance-id`/*"
 }
 ]
}`

```

## IAM trust policy for your integrations

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "QBusinessTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "integrations.qbusiness.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/`application-id`"
 }
 }
 }
 ]
}`

```
