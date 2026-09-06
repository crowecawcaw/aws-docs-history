

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# IAM role for an Amazon Kendra retriever
<a name="kendra-retriever-iam-role"></a>

When you use an Amazon Kendra index as a retriever, you must provide Amazon Q Business with an IAM role with permissions to access Amazon Kendra. You must also provide a trust policy that allows Amazon Q to assume the role. The following are the policies that must be provided.

**To allow Amazon Q to access your Amazon Kendra index, use the following policy:**

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "KendraRetrieveAccess",
            "Effect": "Allow",
            "Action": [
                "kendra:Retrieve",
                "kendra:DescribeIndex"
            ],
            "Resource": "arn:aws:kendra:us-east-1:111122223333:index/{{example-index-id}}"
        }
    ]
}
```

------

**To allow Amazon Q to assume a role, use the following trust policy:**

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AmazonQKendraAccessPermission",
            "Effect": "Allow",
            "Principal": {
                "Service": "qbusiness.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "111122223333"
                },
                "ArnEquals": {
                    "aws:SourceArn": "arn:aws:qbusiness:us-east-1:111122223333:application/{{application-id}}"
                }
            }
        }
    ]
}
```

------