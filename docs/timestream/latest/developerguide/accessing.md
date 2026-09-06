

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Accessing Timestream for LiveAnalytics
<a name="accessing"></a>

You can access Timestream for LiveAnalytics using the console, CLI or the API. For information about accessing Timestream for LiveAnalytics, review the following:

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Provide Timestream for LiveAnalytics access](#getting-started.prereqs.iam-user)
+ [Using the console](console_timestream.md)
+ [Accessing Amazon Timestream for LiveAnalytics using the AWS CLI](Tools.CLI.md)
+ [Using the API](Using.API.md)
+ [Using the AWS SDKs](getting-started-sdks.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Provide Timestream for LiveAnalytics access
<a name="getting-started.prereqs.iam-user"></a>

 The permissions that are required to access Timestream for LiveAnalytics are already granted to the administrator. For other users, you should grant them Timestream for LiveAnalytics access using the following policy: 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "timestream:*",
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:Decrypt",
        "dbqms:CreateFavoriteQuery",
        "dbqms:DescribeFavoriteQueries",
        "dbqms:UpdateFavoriteQuery",
        "dbqms:DeleteFavoriteQueries",
        "dbqms:GetQueryString",
        "dbqms:CreateQueryHistory",
        "dbqms:UpdateQueryHistory",
        "dbqms:DeleteQueryHistory",
        "dbqms:DescribeQueryHistory",
        "s3:ListAllMyBuckets"
      ],
      "Resource": "*"
    }
  ]
}
```

------

**Note**  
For information about `dbqms`, see [Actions, resources, and condition keys for Database Query Metadata Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_databasequerymetadataservice.html). For information about `kms` see [Actions, resources, and condition keys for AWS Key Management Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awskeymanagementservice.html).