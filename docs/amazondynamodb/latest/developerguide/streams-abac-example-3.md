

# Example 3: Deny stream access unless a specific tag is present
<a name="streams-abac-example-3"></a>

Using the `aws:TagKeys` condition key, you can deny tagging a stream unless a required tag key is included in the request.

## Using the AWS CLI
<a name="streams-abac-example-3-cli"></a>

1. Add a customer managed policy to a role which has DynamoDB access, as shown in the following example.

   ```
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Deny",
         "Action": [
           "dynamodb:TagResource"
         ],
         "Resource": "arn:aws:dynamodb:*:*:table/*/stream/*",
         "Condition": {
           "Null": {
             "aws:TagKeys": "false"
           },
           "ForAllValues:StringNotEquals": {
             "aws:TagKeys": "CostCenter"
           }
         }
       }
     ]
   }
   ```

1. Assume the role and attempt to tag a stream with a tag key that is not `CostCenter`.

   ```
   aws dynamodb tag-resource \
     --resource-arn arn:aws:dynamodb:us-east-1:123456789012:table/myMusicTable/stream/2024-01-01T00:00:00.000 \
     --tags Key=Department,Value=Engineering
   ```

## Behavior with and without Streams ABAC
<a name="streams-abac-example-3-behavior"></a>

Without Streams ABAC  
If Streams ABAC isn't enabled for your AWS account, DynamoDB doesn't send the tag keys in the request to IAM. The `Null` condition ensures that the condition evaluates to false if there are no tag keys in the request. Because the Deny policy doesn't match, the `tag-resource` command completes successfully.

With Streams ABAC  
If Streams ABAC is enabled for your AWS account, the tag key `Department` is evaluated against the condition-based tag key `CostCenter` present in the Deny policy. The tag key `Department` doesn't match the tag key present in the Deny policy because of the `StringNotEquals` operator. Therefore, the `TagResource` action fails and returns an `AccessDeniedException`.