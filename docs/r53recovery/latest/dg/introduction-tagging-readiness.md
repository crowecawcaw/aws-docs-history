#

Tagging for readiness check in Amazon Application Recovery Controller (ARC)

Tags are words or phrases (meta data) that you use to identify and organize your AWS resources. You can add multiple
tags to each resource, and each tag includes a key and a value that you define. For example, the key might be environment
and the value might be production. You can search and filter your resources based on the tags you add.

You can tag the following resources in readiness check in ARC:

- Resource sets
- Readiness checks
  Tagging in ARC is available only through the API, for example, by using the AWS CLI.

The following are examples of tagging in readiness check by using the AWS CLI.

`aws route53-recovery-readiness --region us-west-2 create-resource-set --resource-set-name dynamodb_resource_set --resource-set-type AWS::DynamoDB::Table 
 --resources ReadinessScopes=arn:aws:aws-recovery-readiness::111122223333:cell/PDXCell,ResourceArn=arn:aws:dynamodb:us-west-2:111122223333:table/PDX_Table
 ReadinessScopes=arn:aws:aws-recovery-readiness::111122223333:cell/IADCell,ResourceArn=arn:aws:dynamodb:us-east-1:111122223333:table/IAD_Table 
 --tags Stage=Prod`

`aws route53-recovery-readiness --region us-west-2 create-readiness-check --readiness-check-name dynamodb_readiness_check --resource-set-name dynamodb_resource_set 
 --tags Stage=Prod`

For more information, see
[TagResource](../../../recovery-readiness/latest/api/tags-resource-arn.md "../../../recovery-readiness/latest/api/tags-resource-arn.md") in the
_Recovery Readiness API Reference Guide_ for Amazon Application Recovery Controller (ARC).
