

# Tagging for access control in Amazon SQS

The following is an example of using tags for access control in Amazon SQS. The IAM policy restricts an IAM user to all Amazon SQS actions for all queues that include a resource tag with the key environment and the value production. For more information, see [Attribute-based access control with tags and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging_abac.html). 

------
#### [ JSON ]

****  

```json
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowAccessForProd",
      "Effect": "Allow",
      "Action": "sqs:*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/environment": "prod"
        }
      }
    }
  ]
}
```

------