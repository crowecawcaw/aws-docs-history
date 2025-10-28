# Sample policies for private

subnets that access Amazon S3

For private subnets, at a minimum you must provide the ability for Amazon EMR to
access Amazon Linux repositories. This private subnet policy is a part of the VPC
endpoint policies for accessing Amazon S3.

With Amazon EMR 5.25.0 or later, to enable
one-click access to persistent Spark history server, you must allow Amazon EMR to
access the system bucket that collects Spark event logs. If you enable logging,
provide PUT permissions to the following bucket:

```
aws157-logs-${AWS::`Region`}/*
```

For more information, see [One-click
access to persistent Spark History Server](app-history-spark-UI.md "app-history-spark-UI.md").

It is up to you to determine the policy restrictions that meet your business
needs. The following example policy provides permissions to access Amazon Linux
repositories and the Amazon EMR system bucket for collecting Spark event logs. It shows a few sample resource names for the buckets.

For more information about using IAM policies with Amazon VPC endpoints, see
[Endpoint policies for Amazon S3](../../../vpc/latest/privatelink/vpc-endpoints-s3.md#vpc-endpoints-policies-s3 "../../../vpc/latest/privatelink/vpc-endpoints-s3.md#vpc-endpoints-policies-s3").

The following policy example contains sample resources in the us-east-1 region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonLinuxAMIRepositoryAccess",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject"
 ],
 "Resource": [
 "arn:aws:s3:::packages.us-east-1.amazonaws.com/*",
 "arn:aws:s3:::repo.us-east-1.amazonaws.com/*"
 ]
 },
 {
 "Sid": "EnableApplicationHistory",
 "Effect": "Allow",
 "Action": [
 "s3:Put*",
 "s3:Get*",
 "s3:Create*",
 "s3:Abort*",
 "s3:List*"
 ],
 "Resource": [
 "arn:aws:s3:::prod.us-east-1.appinfo.src/*"
 ]
 }
 ]
}`

```

The following example policy provides the permissions required to access Amazon Linux
2 repositories in the us-east-1 region.

```
{
   "Statement": [
       {
           "Sid": "AmazonLinux2AMIRepositoryAccess",
           "Effect": "Allow",
           "Principal": "*",
           "Action": "s3:GetObject",
           "Resource": [
           	"arn:aws:s3:::amazonlinux.us-east-1.amazonaws.com/*",
           	"arn:aws:s3:::amazonlinux-2-repos-us-east-1/*"
           ]
       }
   ]
}
```

The following example policy provides the permissions required to access Amazon Linux
2023 repositories in the us-east-1 region.

```
{
    "Statement": [
        {
            "Sid": "AmazonLinux2023AMIRepositoryAccess",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": [
                 "arn:aws:s3:::al2023-repos-us-east-1-de612dc2/*"
            ]
        }
    ]
 }
```

## Available regions

The following table contains a list of buckets by region, and includes both an Amazon Resource Name (ARN) for the respository and a string that represents
the ARN for the `appinfo.src`. The ARN, or Amazon Resource Name, is a string that uniquely identifies an AWS resource.

| Region                      | Repository buckets                                                                                                                                              | AppInfo bucket                                    |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| _US East (Ohio)_            | "arn:aws:s3:::packages.us-east-2.amazonaws.com/","arn:aws:s3:::repo.us-east-2.amazonaws.com/","arn:aws:s3:::repo.us-east-2.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.us-east-2.appinfo.src/\*"      |
| _US East (N. Virginia)_     | "arn:aws:s3:::packages.us-east-1.amazonaws.com/","arn:aws:s3:::repo.us-east-1.amazonaws.com/","arn:aws:s3:::repo.us-east-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.us-east-1.appinfo.src/\*"      |
| _US West (N. California)_   | "arn:aws:s3:::packages.us-west-1.amazonaws.com/","arn:aws:s3:::repo.us-west-1.amazonaws.com/","arn:aws:s3:::repo.us-west-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.us-west-1.appinfo.src/\*"      |
| _US West (Oregon)_          | "arn:aws:s3:::packages.us-west-2.amazonaws.com/","arn:aws:s3:::repo.us-west-2.amazonaws.com/","arn:aws:s3:::repo.us-west-2.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.us-west-2.appinfo.src/\*"      |
| _Africa (Cape Town)_        | "arn:aws:s3:::packages.af-south-1.amazonaws.com/","arn:aws:s3:::repo.af-south-1.amazonaws.com/","arn:aws:s3:::repo.af-south-1.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.af-south-1.appinfo.src/\*"     |
| _Africa (Cape Town)_        | "arn:aws:s3:::packages.ap-east-1.amazonaws.com/","arn:aws:s3:::repo.ap-east-1.amazonaws.com/","arn:aws:s3:::repo.ap-east-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.ap-east-1.appinfo.src/\*"      |
| _Asia Pacific (Hyderabad)_  | "arn:aws:s3:::packages.ap-south-2.amazonaws.com/","arn:aws:s3:::repo.ap-south-2.amazonaws.com/","arn:aws:s3:::repo.ap-south-2.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.ap-south-2.appinfo.src/\*"     |
| _Asia Pacific (Jakarta)_    | "arn:aws:s3:::packages.ap-southeast-3.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-3.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-3.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-southeast-3.appinfo.src/\*" |
| _Asia Pacific (Malaysia)_   | "arn:aws:s3:::packages.ap-southeast-5.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-5.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-5.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-southeast-5.appinfo.src/\*" |
| _Asia Pacific (Melbourne)_  | "arn:aws:s3:::packages.ap-southeast-4.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-4.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-4.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-south-4.appinfo.src/\*"     |
| _Asia Pacific (Mumbai)_     | "arn:aws:s3:::packages.ap-south-1.amazonaws.com/","arn:aws:s3:::repo.ap-south-1.amazonaws.com/","arn:aws:s3:::repo.ap-south-1.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.ap-south-1.appinfo.src/\*"     |
| _Asia Pacific (Osaka)_      | "arn:aws:s3:::packages.ap-northeast-3.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-3.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-3.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-northeast-3.appinfo.src/\*" |
| _Asia Pacific (Seoul)_      | "arn:aws:s3:::packages.ap-northeast-2.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-2.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-2.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-northeast-2.appinfo.src/\*" |
| _Asia Pacific (Singapore)_  | "arn:aws:s3:::packages.ap-southeast-1.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-1.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-1.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-southeast-1.appinfo.src/\*" |
| _Asia Pacific (Sydney)_     | "arn:aws:s3:::packages.ap-southeast-2.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-2.amazonaws.com/","arn:aws:s3:::repo.ap-southeast-2.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-southeast-2.appinfo.src/\*" |
| _Asia Pacific (Tokyo)_      | "arn:aws:s3:::packages.ap-northeast-1.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-1.amazonaws.com/","arn:aws:s3:::repo.ap-northeast-1.emr.amazonaws.com/\*" | "arn:aws:s3:::prod.ap-northeast-1.appinfo.src/\*" |
| _Canada (Central)_          | "arn:aws:s3:::packages.ca-central-1.amazonaws.com/","arn:aws:s3:::repo.ca-central-1.amazonaws.com/","arn:aws:s3:::repo.ca-central-1.emr.amazonaws.com/\*"       | "arn:aws:s3:::prod.ca-central-1.appinfo.src/\*"   |
| _Canada West (Calgary)_     | "arn:aws:s3:::packages.ca-west-1.amazonaws.com/","arn:aws:s3:::repo.ca-west-1.amazonaws.com/","arn:aws:s3:::repo.ca-west-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.ca-west-1.appinfo.src/\*"      |
| _Europe (Frankfurt)_        | "arn:aws:s3:::packages.eu-central-1.amazonaws.com/","arn:aws:s3:::repo.eu-central-1.amazonaws.com/","arn:aws:s3:::repo.eu-central-1.emr.amazonaws.com/\*"       | "arn:aws:s3:::prod.eu-central-1.appinfo.src/\*"   |
| _Europe (Ireland)_          | "arn:aws:s3:::packages.eu-west-1.amazonaws.com/","arn:aws:s3:::repo.eu-west-1.amazonaws.com/","arn:aws:s3:::repo.eu-west-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.eu-west-1.appinfo.src/\*"      |
| _Europe (London)_           | "arn:aws:s3:::packages.eu-west-2.amazonaws.com/","arn:aws:s3:::repo.eu-west-2.amazonaws.com/","arn:aws:s3:::repo.eu-west-2.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.eu-west-2.appinfo.src/\*"      |
| _Europe (Milan)_            | "arn:aws:s3:::packages.eu-south-1.amazonaws.com/","arn:aws:s3:::repo.eu-south-1.amazonaws.com/","arn:aws:s3:::repo.eu-south-1.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.eu-south-1.appinfo.src/\*"     |
| _Europe (Paris)_            | "arn:aws:s3:::packages.eu-west-3.amazonaws.com/","arn:aws:s3:::repo.eu-west-3.amazonaws.com/","arn:aws:s3:::repo.eu-west-3.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.eu-west-3.appinfo.src/\*"      |
| _Europe (Spain)_            | "arn:aws:s3:::packages.eu-south-2.amazonaws.com/","arn:aws:s3:::repo.eu-south-2.amazonaws.com/","arn:aws:s3:::repo.eu-south-2.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.eu-south-2.appinfo.src/\*"     |
| _Europe (Stockholm)_        | "arn:aws:s3:::packages.eu-north-1.amazonaws.com/","arn:aws:s3:::repo.eu-north-1.amazonaws.com/","arn:aws:s3:::repo.eu-north-1.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.eu-north-1.appinfo.src/\*"     |
| _Europe (Zurich)_           | "arn:aws:s3:::packages.eu-central-2.amazonaws.com/","arn:aws:s3:::repo.eu-central-2.amazonaws.com/","arn:aws:s3:::repo.eu-central-2.emr.amazonaws.com/\*"       | "arn:aws:s3:::prod.eu-central-2.appinfo.src/\*"   |
| _Israel (Tel Aviv)_         | "arn:aws:s3:::packages.il-central-1.amazonaws.com/","arn:aws:s3:::repo.il-central-1.amazonaws.com/","arn:aws:s3:::repo.il-central-1.emr.amazonaws.com/\*"       | "arn:aws:s3:::prod.il-central-1.appinfo.src/\*"   |
| _Middle East (Bahrain)_     | "arn:aws:s3:::packages.me-south-1.amazonaws.com/","arn:aws:s3:::repo.me-south-1.amazonaws.com/","arn:aws:s3:::repo.me-south-1.emr.amazonaws.com/\*"             | "arn:aws:s3:::prod.me-south-1.appinfo.src/\*"     |
| _Middle East (UAE)_         | "arn:aws:s3:::packages.me-central-1.amazonaws.com/","arn:aws:s3:::repo.me-central-1.amazonaws.com/","arn:aws:s3:::repo.me-central-1.emr.amazonaws.com/\*"       | "arn:aws:s3:::prod.me-central-1.appinfo.src/\*"   |
| _South America (São Paulo)_ | "arn:aws:s3:::packages.sa-east-1.amazonaws.com/","arn:aws:s3:::repo.sa-east-1.amazonaws.com/","arn:aws:s3:::repo.sa-east-1.emr.amazonaws.com/\*"                | "arn:aws:s3:::prod.sa-east-1.appinfo.src/\*"      |
| _AWS GovCloud (US-East)_    | "arn:aws:s3:::packages.us-gov-east-1.amazonaws.com/","arn:aws:s3:::repo.us-gov-east-1.amazonaws.com/","arn:aws:s3:::repo.us-gov-east-1.emr.amazonaws.com/\*"    | "arn:aws:s3:::prod.us-gov-east-1.appinfo.src/\*"  |
| _AWS GovCloud (US-West)_    | "arn:aws:s3:::packages.us-gov-west-1.amazonaws.com/","arn:aws:s3:::repo.us-gov-west-1.amazonaws.com/","arn:aws:s3:::repo.us-gov-west-1.emr.amazonaws.com/\*"    | "arn:aws:s3:::prod.me-south-1.appinfo.src/\*"     |
