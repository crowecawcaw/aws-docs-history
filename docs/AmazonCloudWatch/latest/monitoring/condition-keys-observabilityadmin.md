# Condition keys for CloudWatch

Observability Admin

You can use IAM policies to control access to Amazon CloudWatch Observability Admin
resources and actions by using condition keys.

Observability Admin has the following condition keys:

| Condition Key                   | Description   | Type                                                                      |
| ------------------------------- | ------------- | ------------------------------------------------------------------------- |
| CentralizationSourceRegions     | ArrayOfString | Filters access by the source Regions that are passed in<br>the request    |
| CentralizationDestinationRegion | String        | Filters access by the destination Region that is passed in<br>the request |
| CentralizationBackupRegion      | String        | Filters access by the backup Region that is passed in the<br>request      |

## CentralizationSourceRegions

Filters access by the backup region specified for centralization
rules.

- _Availability_ – This key is available for the
  following resource types: organization-centralization-rule
- _Value type_ – String

###### Example JSON policy with observabilityadmin:CentralizationBackupRegion

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-1"
 }
 }
 }
 ]
}`

```

## CentralizationDestinationRegion

Filters access by the destination region specified for centralization
rules.

- _Availability_ – This key is available for the
  following resource types: organization-centralization-rule
- _Value type_ – String

###### Example JSON policy with observabilityadmin:CentralizationDestinationRegion

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": "us-east-1"
 }
 }
 }
 ]
}`

```

## CentralizationBackupRegion

Filters access by the source regions specified for centralization
rules.

- _Availability_ – This key is available for the
  following resource types: organization-centralization-rule
- _Value type_ – List of strings

###### Example JSON policy with observabilityadmin:CentralizationSourceRegions

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "cloudwatch:PutMetricData",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": ["us-east-1", "us-east-1"]
 }
 }
 }
 ]
}`

```
