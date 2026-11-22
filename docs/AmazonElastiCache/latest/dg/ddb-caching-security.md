

# Security in DynamoDB caching

Amazon DynamoDB caching encrypts your data, authenticates connections to the serverless cache, and authorizes access to DynamoDB table data. The following sections describe each of these security controls.

## Encryption
<a name="ddb-caching-security-encryption"></a>

Data in transit between your application, your cache, and DynamoDB is always encrypted using Transport Layer Security (TLS). For more information about in-transit encryption, see [ElastiCache in-transit encryption (TLS)](in-transit-encryption.md).

Data at rest is encrypted according to the at-rest encryption settings for the cache. For more information about data security, see [Data security in Amazon ElastiCache](encryption.md).

## Authentication
<a name="ddb-caching-security-authentication"></a>

DynamoDB caching requires IAM authentication to connect to the serverless cache. Password-based authentication is not supported. For more information, see [Authenticating with IAM in ElastiCache](auth-iam.md).

## Authorization
<a name="ddb-caching-security-authorization"></a>

When the cache needs to read from or write to DynamoDB, it authorizes the read or write using the credentials used to invoke the DynamoDB API through a [Forward Access Session](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html).

In addition to the IAM action permissions required to read and write DynamoDB table data, your principal must have the `elasticache:Connect` permission on the Amazon ElastiCache serverless cache resource. With this permission, your application can connect to the serverless cache.

The following example IAM identity policy grants an application permissions to connect to a serverless cache for DynamoDB caching and to read and write to the DynamoDB table through DynamoDB caching.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EnableDynamoDBIntegration",
            "Effect": "Allow",
            "Action": [
                "elasticache:Connect"
            ],
            "Resource": [
                "arn:aws:elasticache:{{us-east-1}}:{{123456789012}}:serverlesscache:my-ddb-cache"
            ]
        },
        {
            "Sid": "ReadAndWriteCachedTable",
            "Effect": "Allow",
            "Action": [
                "dynamodb:GetItem",
                "dynamodb:BatchGetItem",
                "dynamodb:BatchWriteItem",
                "dynamodb:DeleteItem",
                "dynamodb:UpdateItem",
                "dynamodb:PutItem",
                "dynamodb:Query",
                "dynamodb:Scan"
            ],
            "Resource": "arn:aws:dynamodb:{{us-east-1}}:{{123456789012}}:table/my-table"
        }
    ]
}
```

**Note**  
Any principal that has permissions to read from a cache with DynamoDB caching enabled can read data that was cached by other requests, even if that principal does not have permissions to access the DynamoDB source tables. ElastiCache supports Role-Based Access Control to further limit access to cached data. For more information, see [Role-Based Access Control (RBAC)](Clusters.RBAC.md). Ensure your serverless cache authorization configuration reflects your desired security posture.