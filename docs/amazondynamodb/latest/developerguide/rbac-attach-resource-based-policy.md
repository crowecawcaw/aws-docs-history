# Attach a policy to an DynamoDB existing table

You can attach a resource-based policy to an existing table or modify an existing policy
by using the DynamoDB console, [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") API, the AWS CLI, AWS SDK, or an [CloudFormation template](rbac-create-table.md#rbac-create-table-cfn "rbac-create-table.md#rbac-create-table-cfn").

The following IAM policy example uses the `put-resource-policy` AWS CLI
command to attach a resource-based policy to an existing table. This example allows the
user `John` to perform the [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md"), [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md"), [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md"), and
[UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") API
actions on an existing table named `MusicCollection`.

Remember to replace the `italicized` text with your resource-specific information.

```
aws dynamodb put-resource-policy \
    --resource-arn arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection` \
    --policy \
        "{
            \"Version\": \"2012-10-17\",
            \"Statement\": [
              {
                    \"Effect\": \"Allow\",
                    \"Principal\": {
                        \"AWS\": \"arn:aws:iam::`111122223333`:user/`John`\"
                    },
                    \"Action\": [
                        \"dynamodb:GetItem\",
                        \"dynamodb:PutItem\",
                        \"dynamodb:UpdateItem\",
                        \"dynamodb:UpdateTable\"
                    ],
                    \"Resource\": \"arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`\"
                }
            ]
        }"
```

To conditionally update an existing resource-based policy of a table, you can use the
optional `expected-revision-id` parameter. The following example will only
update the policy if it exists in DynamoDB and its current revision ID matches the provided
`expected-revision-id` parameter.

```
aws dynamodb put-resource-policy \
    --resource-arn arn:aws:dynamodb:us-west-2:123456789012:table/`MusicCollection` \
    --expected-revision-id 1709841168699 \
    --policy \
        "{
            \"Version\": \"2012-10-17\",
            \"Statement\": [
              {
                    \"Effect\": \"Allow\",
                    \"Principal\": {
                        \"AWS\": \"arn:aws:iam::111122223333:user/`John`\"
                    },
                    \"Action\": [
                        \"dynamodb:GetItem\",
                        \"dynamodb:UpdateItem\",
                        \"dynamodb:UpdateTable\"
                    ],
                    \"Resource\": \"arn:aws:dynamodb:us-west-2:123456789012:table/`MusicCollection`\"
                }
            ]
        }"
```

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. From the dashboard, choose an existing table.
3. Navigate to the **Permissions** tab, and choose **Create
   table policy**.
4. In the resource-based policy editor, add the policy you would like to attach and
   choose **Create policy**.

The following IAM policy example allows the user
`John` to perform the [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md"), [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md"), [UpdateItem](../APIReference/API_UpdateItem.md "../APIReference/API_UpdateItem.md"), and
[UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md")
API actions on an existing table named
`MusicCollection`.

Remember to replace the `italicized` text with your resource-specific information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`username`"
 },
 "Action": [
 "dynamodb:GetItem",
 "dynamodb:PutItem",
 "dynamodb:UpdateItem",
 "dynamodb:UpdateTable"
 ],
 "Resource": "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`MusicCollection`"
 }
 ]
}`

```

The following IAM policy example uses the `putResourcePolicy` method to
attach a resource-based policy to an existing table. This policy allows a user to perform
the [GetItem](../APIReference/API_GetItem.md "../APIReference/API_GetItem.md") API action on an existing table.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.services.dynamodb.model.DynamoDbException;
import software.amazon.awssdk.services.dynamodb.model.PutResourcePolicyRequest;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * Get started with the AWS SDK for Java 2.x
 */
public class PutResourcePolicy {

    public static void main(String[] args) {
        final String usage = """

                Usage:
                    <tableArn> <allowedAWSPrincipal>

                Where:
                    tableArn - The Amazon DynamoDB table ARN to attach the policy to. For example, arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`.
                    allowedAWSPrincipal - Allowed AWS principal ARN that the example policy will give access to. For example, arn:aws:iam::`123456789012`:user/`John`.
                """;

        if (args.length != 2) {
            System.out.println(usage);
            System.exit(1);
        }

        String tableArn = args[0];
        String allowedAWSPrincipal = args[1];
        System.out.println("Attaching a resource-based policy to the Amazon DynamoDB table with ARN " +
                tableArn);
        Region region = Region.US_WEST_2;
        DynamoDbClient ddb = DynamoDbClient.builder()
                .region(region)
                .build();

        String result = putResourcePolicy(ddb, tableArn, allowedAWSPrincipal);
        System.out.println("Revision ID for the attached policy is " + result);
        ddb.close();
    }

    public static String putResourcePolicy(DynamoDbClient ddb, String tableArn, String allowedAWSPrincipal) {
        String policy = generatePolicy(tableArn, allowedAWSPrincipal);
        PutResourcePolicyRequest request = PutResourcePolicyRequest.builder()
                .policy(policy)
                .resourceArn(tableArn)
                .build();

        try {
            return ddb.putResourcePolicy(request).revisionId();
        } catch (DynamoDbException e) {
            System.err.println(e.getMessage());
            System.exit(1);
        }

        return "";
    }

    private static String generatePolicy(String tableArn, String allowedAWSPrincipal) {
        return "{\n" +
                "    \"Version\": \"2012-10-17\",\n" +,
                "    \"Statement\": [\n" +
                "        {\n" +
                "            \"Effect\": \"Allow\",\n" +
                "            \"Principal\": {\"AWS\":\"" + allowedAWSPrincipal + "\"},\n" +
                "            \"Action\": [\n" +
                "                \"dynamodb:GetItem\"\n" +
                "            ],\n" +
                "            \"Resource\": \"" + tableArn + "\"\n" +
                "        }\n" +
                "    ]\n" +
                "}";
    }
}
```
