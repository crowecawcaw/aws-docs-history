# AmazonDataZoneS3Manage-<region>-<domainId>

The AmazonDataZoneS3Manage-<region>-<domainId> is used when Amazon DataZone
calls AWS Lake Formation to register an Amazon Simple Storage Service (Amazon S3)
location. AWS Lake Formation assumes this role when accessing the data in that
location. For more information, see [Requirements for roles used to register locations](../../../lake-formation/latest/dg/registration-role.md "../../../lake-formation/latest/dg/registration-role.md").

This role has the following inline permissions policy attached.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3",
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 },
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3ListBucket",
 "Effect": "Allow",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 },
 {
 "Sid": "LakeFormationDataAccessPermissionsForS3ListAllMyBuckets",
 "Effect": "Allow",
 "Action": [
 "s3:ListAllMyBuckets"
 ],
 "Resource": "arn:aws:s3:::*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 },
 {
 "Sid": "LakeFormationExplicitDenyPermissionsForS3",
 "Effect": "Deny",
 "Action": [
 "s3:PutObject",
 "s3:GetObject",
 "s3:DeleteObject"
 ],
 "Resource": [
 "arn:aws:s3:::[[BucketNames]]/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 },
 {
 "Sid": "LakeFormationExplicitDenyPermissionsForS3ListBucket",
 "Effect": "Deny",
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::[[BucketNames]]"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "{{accountId}}"
 }
 }
 }
 ]
}`

```

The AmazonDataZoneS3Manage-<region>-<domainId> has the following trust
policy attached:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TrustLakeFormationForDataLocationRegistration",
 "Effect": "Allow",
 "Principal": {
 "Service": "lakeformation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{source_account_id}}"
 }
 }
 }
 ]
}`

```
