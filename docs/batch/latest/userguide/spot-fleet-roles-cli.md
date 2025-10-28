# Tutorial: Create Amazon EC2 spot fleet roles with the AWS CLI

###### To create the **AmazonEC2SpotFleetTaggingRole** IAM role for your Spot Fleet compute

environments

1. Run the following command with the AWS CLI.

```
`$` `aws iam create-role --role-name AmazonEC2SpotFleetTaggingRole \
 --assume-role-policy-document '{
 "Version": "2012-10-17",
 "Statement":[
 {
 "Sid":"",
 "Effect":"Allow",
 "Principal": {
 "Service":"spotfleet.amazonaws.com"
 },
 "Action":"sts:AssumeRole"
 }
 ]
 }'`
```

2. To attach the **AmazonEC2SpotFleetTaggingRole** managed IAM policy to
   your **AmazonEC2SpotFleetTaggingRole** role, run the following command with
   the AWS CLI.

```
`$` `aws iam attach-role-policy \
 --policy-arn \
 arn:aws:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole \
 --role-name \
 AmazonEC2SpotFleetTaggingRole`
```

###### To create the `AWSServiceRoleForEC2Spot` IAM service-linked role for Amazon EC2

Spot

###### Note

If the `AWSServiceRoleForEC2Spot` IAM service-linked role already exists, you
see an error message that resembles the following.

```
An error occurred (InvalidInput) when calling the CreateServiceLinkedRole operation:
Service role name `AWSServiceRoleForEC2Spot` has been taken in this account, please try a different suffix.
```

- Run the following command with the AWS CLI.

```
`$` `aws iam create-service-linked-role --aws-service-name spot.amazonaws.com`
```

###### To create the `AWSServiceRoleForEC2SpotFleet` IAM service-linked role for Amazon EC2 Spot

Fleet

###### Note

If the `AWSServiceRoleForEC2SpotFleet` IAM service-linked role already
exists, you see an error message that resembles the following.

```
An error occurred (InvalidInput) when calling the CreateServiceLinkedRole operation:
Service role name `AWSServiceRoleForEC2SpotFleet` has been taken in this account, please try a different suffix.
```

- Run the following command with the AWS CLI.

```
`$` `aws iam create-service-linked-role --aws-service-name spotfleet.amazonaws.com`
```
