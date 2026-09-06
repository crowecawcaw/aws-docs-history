

# Sample policies for private subnets that access Amazon S3
<a name="private-subnet-iampolicy"></a>

When launching an Amazon EMR cluster in a private subnet, you must provide a route to Amazon S3. By default, a gateway endpoint for Amazon S3 allows access to all buckets. You can create a VPC endpoint policy to restrict access to specific buckets; if you do, you will need to add policy statements allowing access to the specific S3 buckets required by Amazon EMR. For more information about Amazon S3 endpoints, see [Gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

It is up to you to determine the policy restrictions that meet your business needs. This page details the buckets required by Amazon EMR to successfully launch a cluster, followed by an example VPC endpoint policy granting access to those buckets.

## Required buckets
<a name="private-subnet-iampolicy-required-buckets"></a>

### Amazon Linux AMI repositories
<a name="private-subnet-iampolicy-al-repos"></a>

All Amazon EMR clusters require access to Amazon Linux repositories. The specific bucket ARNs depend on the version of Amazon Linux being used, which depends on the Amazon EMR release being used:
+ Amazon EMR 5.29.0 and earlier: AL1 repos `arn:aws:s3:::packages.{{region}}.amazonaws.com` and `arn:aws:s3:::repo.{{region}}.amazonaws.com`
+ Amazon EMR 5.30.0 through 6.15.0: AL2 repos `arn:aws:s3:::amazonlinux.{{region}}.amazonaws.com` and `arn:aws:s3:::amazonlinux-2-repos-{{region}}`
+ Amazon EMR 7.0.0 and later: AL2023 repo `arn:aws:s3:::al2023-repos-{{region}}-de612dc2`

### Amazon EMR repositories
<a name="private-subnet-iampolicy-emr-repos"></a>

Amazon EMR 5.22.0 and later require access to the EMR repository bucket `arn:aws:s3:::repo.{{region}}.emr.amazonaws.com`.

Amazon EMR 8.0.0 and later and Amazon EMR Spark 8.0.0 and later require access to the EMR instance data buckets `arn:aws:s3:::aws157-instance-data-0-prod-{{region}}` and `arn:aws:s3:::aws157-instance-data-1-prod-{{region}}`.

In the ap-southeast-2 region, these buckets are instead named `arn:aws:s3:::aws157-instance-data-bucket-0-prod-ap-southeast-2` and `arn:aws:s3:::aws157-instance-data-bucket-1-prod-ap-southeast-2`.

### Logging
<a name="private-subnet-iampolicy-logging"></a>

If you enable cluster logging, you will need PUT permissions for the bucket you specify as the log destination when creating the cluster, as well as the system logs bucket. In the us-east-1 region, the bucket ARN is `arn:aws:s3:::aws157-logs-prod`; for all other regions, the bucket ARN is `arn:aws:s3:::aws157-logs-prod-{{region}}`.

### Persistent application user interfaces
<a name="private-subnet-iampolicy-app-ui"></a>

With Amazon EMR 5.25.0 or later, to enable one-click access to persistent application user interfaces, you must allow Amazon EMR to access the system bucket that collects application logs, `arn:aws:s3:::prod.{{region}}.appinfo.src`. For more information, see [View persistent application user interfaces in Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/app-history-spark-UI.html).

## Example policy
<a name="private-subnet-iampolicy-example"></a>

The following example policy provides the permissions required to launch an Amazon EMR 8.0.0 cluster in a private subnet in the us-east-2 region, with logging and persistent application user interfaces enabled.

```
{
  "Version":"2012-10-17", 		 	 	 
  "Statement": [
    {
      "Sid": "AmazonLinux2023AMIRepositoryAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::al2023-repos-us-east-2-de612dc2/*"
      ]
    },
    {
      "Sid": "EmrRepositoryAccess",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::repo.us-east-2.emr.amazonaws.com/*",
        "arn:aws:s3:::aws157-instance-data-0-prod-us-east-2/*",
        "arn:aws:s3:::aws157-instance-data-1-prod-us-east-2/*"
      ]
    },
    {
      "Sid": "EnableClusterLogs",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:Put*"
      ],
      "Resource": [
        "arn:aws:s3:::aws157-logs-prod-us-east-2/*",
        "arn:aws:s3:::{{my-logs-bucket}}/*"
      ]
    },
    {
      "Sid": "EnableApplicationHistory",
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "s3:Put*",
        "s3:Get*",
        "s3:Create*",
        "s3:Abort*",
        "s3:List*"
      ],
      "Resource": [
        "arn:aws:s3:::prod.us-east-2.appinfo.src/*"
      ]
    }
  ]
}
```