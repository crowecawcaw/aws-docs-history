

# Querying from an OpenSearch cluster with Fine-grained access control (FGAC) enabled
<a name="full-text-search-fgac"></a>

If you have enabled [fine-grained access control](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) on your OpenSearch cluster, you need to [enable IAM authentication](iam-auth-enable.md) in your Neptune database as well.

The IAM entity (User or Role) used for connecting to the Neptune database should have permissions both for Neptune and the OpenSearch cluster. This means that your user or role must have an OpenSearch Service policy like this attached:

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowFullTextSearchAccess",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::{{111122223333}}:root"
      },
      "Action": "es:*",
      "Resource": "arn:aws:es:{{us-east-1}}:{{111122223333}}:domain/{{domain-name}}/*"
    }
  ]
}
```

------

See [Creating custom IAM policy statements to access data in Amazon Neptune](iam-data-access-policies.md) for more information.