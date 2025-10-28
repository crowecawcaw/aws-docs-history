# Examples for using ABAC with DynamoDB tables and indexes

The following examples depict some use cases to implement attribute-based conditions using tags.

###### Topics

- [Example 1: Allow an action using aws:ResourceTag](#abac-allow-example-resource-tag "#abac-allow-example-resource-tag")
- [Example 2: Allow an action using aws:RequestTag](#abac-allow-example-request-tag "#abac-allow-example-request-tag")
- [Example 3: Deny an action using aws:TagKeys](#abac-deny-example-tag-key "#abac-deny-example-tag-key")

## Example 1: Allow an action using aws:ResourceTag

Using the `aws:ResourceTag/tag-key` condition key, you can compare the tag key-value pair that's specified in an IAM policy with the key-value pair that's attached in a DynamoDB table. For example, you can allow a specific action, such as [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md"), if the tag conditions match in an IAM policy and a table. To do this, perform the following steps:

Using the AWS CLI

1. Create a table. The following example uses the [create-table](../../../cli/latest/reference/dynamodb/create-table.md "../../../cli/latest/reference/dynamodb/create-table.md") AWS CLI command to create a table named `myMusicTable`.

```
aws dynamodb create-table \
  --table-name myMusicTable \
  --attribute-definitions AttributeName=id,AttributeType=S \
  --key-schema AttributeName=id,KeyType=HASH \
  --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
  --region `us-east-1`
```

2. Add a tag to this table. The following [tag-resource](../../../cli/latest/reference/dynamodb/tag-resource.md "../../../cli/latest/reference/dynamodb/tag-resource.md") AWS CLI command example adds the tag key-value pair `Title: ProductManager` to the `myMusicTable`.

```
aws dynamodb tag-resource --region `us-east-1` --resource-arn arn:aws:dynamodb:`us-east-1`:`123456789012`:table/myMusicTable --tags Key=Title,Value=ProductManager
```

3. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role which has the [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dynamodb:PutItem",
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Title": "ProductManager"
 }
 }
 }
 ]
}`

```

This policy allows the `PutItem` action on the table when the tag key and value attached to the table matches with the tags specified in the policy. 4. Assume the role with the policies described in Step 3. 5. Use the [put-item](../../../cli/latest/reference/dynamodb/put-item.md "../../../cli/latest/reference/dynamodb/put-item.md") AWS CLI command to put an item to the `myMusicTable`.

```
aws dynamodb put-item \
    --table-name myMusicTable --region us-east-1 \
    --item '{
        "id": {"S": "2023"},
        "title": {"S": "Happy Day"},
        "info": {"M": {
            "rating": {"N": "9"},
            "Artists": {"L": [{"S": "Acme Band"}, {"S": "No One You Know"}]},
            "release_date": {"S": "2023-07-21"}
        }}
    }'
```

6. Scan the table to verify if the item was added to the table.

```
aws dynamodb scan --table-name myMusicTable  --region `us-east-1`
```

Using the AWS SDK for Java 2.x

1. Create a table. The following example uses the [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") API to create a table named `myMusicTable`.

```
DynamoDbClient dynamoDB = DynamoDbClient.builder().region(region).build();
CreateTableRequest createTableRequest = CreateTableRequest.builder()
    .attributeDefinitions(
        Arrays.asList(
            AttributeDefinition.builder()
            .attributeName("id")
            .attributeType(ScalarAttributeType.S)
            .build()
        )
    )
    .keySchema(
        Arrays.asList(
            KeySchemaElement.builder()
            .attributeName("id")
            .keyType(KeyType.HASH)
            .build()
        )
    )
    .provisionedThroughput(ProvisionedThroughput.builder()
        .readCapacityUnits(5L)
        .writeCapacityUnits(5L)
        .build()
    )
    .tableName("myMusicTable")
    .build();

CreateTableResponse createTableResponse = dynamoDB.createTable(createTableRequest);
String tableArn = createTableResponse.tableDescription().tableArn();
String tableName = createTableResponse.tableDescription().tableName();
```

2. Add a tag to this table. The [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") API in the following example adds the tag key-value pair `Title: ProductManager` to the `myMusicTable`.

```
TagResourceRequest tagResourceRequest = TagResourceRequest.builder()
    .resourceArn(tableArn)
    .tags(
        Arrays.asList(
            Tag.builder()
            .key("Title")
            .value("ProductManager")
            .build()
        )
    )
    .build();
dynamoDB.tagResource(tagResourceRequest);
```

3. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role which has the [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dynamodb:PutItem",
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Title": "ProductManager"
 }
 }
 }
 ]
}`

```

This policy allows the `PutItem` action on the table when the tag key and value attached to the table matches with the tags specified in the policy. 4. Assume the role with the policies described in Step 3. 5. Use the [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md") API to put an item to the `myMusicTable`.

```
HashMap<String, AttributeValue> info = new HashMap<>();
info.put("rating", AttributeValue.builder().s("9").build());
info.put("artists", AttributeValue.builder().ss(List.of("Acme Band","No One You Know").build());
info.put("release_date", AttributeValue.builder().s("2023-07-21").build());

HashMap<String, AttributeValue> itemValues = new HashMap<>();
itemValues.put("id", AttributeValue.builder().s("2023").build());
itemValues.put("title", AttributeValue.builder().s("Happy Day").build());
itemValues.put("info", AttributeValue.builder().m(info).build());


PutItemRequest putItemRequest = PutItemRequest.builder()
                .tableName(tableName)
                .item(itemValues)
                .build();
dynamoDB.putItem(putItemRequest);
```

6. Scan the table to verify if the item was added to the table.

```
ScanRequest scanRequest = ScanRequest.builder()
                .tableName(tableName)
                .build();

ScanResponse scanResponse = dynamoDB.scan(scanRequest);
```

Using the AWS SDK for Python (Boto3)

1. Create a table. The following example uses the [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") API to create a table named `myMusicTable`.

```
create_table_response = ddb_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    TableName='myMusicTable',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)

table_arn = create_table_response['TableDescription']['TableArn']
```

2. Add a tag to this table. The [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") API in the following example adds the tag key-value pair `Title: ProductManager` to the `myMusicTable`.

```
tag_resouce_response = ddb_client.tag_resource(
    ResourceArn=table_arn,
    Tags=[
        {
            'Key': 'Title',
            'Value': 'ProductManager'
        },
    ]
)
```

3. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role which has the [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "dynamodb:PutItem",
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/Title": "ProductManager"
 }
 }
 }
 ]
 }`

```

This policy allows the `PutItem` action on the table when the tag key and value attached to the table matches with the tags specified in the policy. 4. Assume the role with the policies described in Step 3. 5. Use the [PutItem](../APIReference/API_PutItem.md "../APIReference/API_PutItem.md") API to put an item to the `myMusicTable`.

```
put_item_response = client.put_item(
    TableName = 'myMusicTable'
    Item = {
        'id': '2023',
        'title': 'Happy Day',
        'info': {
            'rating': '9',
            'artists': ['Acme Band','No One You Know'],
            'release_date': '2023-07-21'
        }
    }
)
```

6. Scan the table to verify if the item was added to the table.

```
scan_response = client.scan(
    TableName='myMusicTable'
)
```

###### Without ABAC

If ABAC isn't enabled for your AWS account, the tag conditions in the IAM policy and the DynamoDB table aren’t matched. Consequently, the `PutItem` action returns an `AccessDeniedException` because of the effect of the `AmazonDynamoDBReadOnlyAccess` policy.

```
An error occurred (AccessDeniedException) when calling the PutItem operation: User: arn:aws:sts::123456789012:assumed-role/DynamoDBReadOnlyAccess/Alice is not authorized to perform: dynamodb:PutItem on resource: arn:aws:dynamodb:us-east-1:123456789012:table/myMusicTable because no identity-based policy allows the dynamodb:PutItem action.
```

###### With ABAC

If ABAC is enabled for your AWS account, the `put-item` action completes successfully and adds a new item to your table. This is because the inline policy on the table allows the `PutItem` action if the tag conditions in the IAM policy and the table match.

## Example 2: Allow an action using aws:RequestTag

Using the [aws:RequestTag/tag-key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag") condition key, you can compare the tag key-value pair that's passed in your request with the tag pair that's specified in the IAM policy. For example, you can allow a specific action, such as `CreateTable`, using the `aws:RequestTag` if the tag conditions don't match. To do this, perform the following steps:

Using the AWS CLI

1. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role which has the [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/ReadOnlyAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:TagResource"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Owner": "John"
 }
 }
 }
 ]
}`

```

2. Create a table that contains the tag key-value pair of `"Owner": "John"`.

```
aws dynamodb create-table \
--attribute-definitions AttributeName=ID,AttributeType=S \
--key-schema AttributeName=ID,KeyType=HASH  \
--provisioned-throughput ReadCapacityUnits=1000,WriteCapacityUnits=500 \
--region `us-east-1` \
--tags Key=Owner,Value=John \
--table-name myMusicTable
```

Using the AWS SDK for Python (Boto3)

1. Create an [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") and add it to a role which has the [AmazonDynamoDBReadOnlyAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBReadOnlyAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:TagResource"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/Owner": "John"
 }
 }
 }
 ]
}`

```

2. Create a table that contains the tag key-value pair of `"Owner": "John"`.

```
ddb_client = boto3.client('dynamodb')

create_table_response = ddb_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    TableName='myMusicTable',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 1000,
        'WriteCapacityUnits': 500
    },
    Tags=[
        {
            'Key': 'Owner',
            'Value': 'John'
        },
    ],
)
```

###### Without ABAC

If ABAC isn't enabled for your AWS account, the tag conditions in the inline policy and the DynamoDB table aren’t matched. Consequently, the `CreateTable` request fails and your table isn’t created.

```
An error occurred (AccessDeniedException) when calling the CreateTable operation: User: arn:aws:sts::123456789012:assumed-role/Admin/John is not authorized to perform: dynamodb:CreateTable on resource: arn:aws:dynamodb:us-east-1:123456789012:table/myMusicTable because no identity-based policy allows the dynamodb:CreateTable action.
```

###### With ABAC

If ABAC is enabled for your AWS account, your table creation request completes successfully. Because the tag key-value pair of `"Owner": "John"` is present in the `CreateTable` request, the inline policy allows the user `John` to perform the `CreateTable` action.

## Example 3: Deny an action using aws:TagKeys

Using the [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys") condition key, you can compare the tag keys in a request with the keys that are specified in the IAM policy. For example, you can deny a specific action, such as `CreateTable`, using `aws:TagKeys` if a specific tag key is _not_ present in the request. To do this, perform the following steps:

Using the AWS CLI

1. Add a [customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") to a role which has the [AmazonDynamoDBFullAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:TagResource"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*",
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
}`

```

2. Assume the role to which the policy was attached, and create a table with the tag key `Title`.

```
aws dynamodb create-table \
--attribute-definitions AttributeName=ID,AttributeType=S \
--key-schema AttributeName=ID,KeyType=HASH  \
--provisioned-throughput ReadCapacityUnits=1000,WriteCapacityUnits=500 \
--region `us-east-1` \
--tags Key=Title,Value=ProductManager \
--table-name myMusicTable
```

Using the AWS SDK for Python (Boto3)

1. Add a [customer managed policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") to a role which has the [AmazonDynamoDBFullAccess](../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonDynamoDBFullAccess.md") AWS managed policy attached to it, as shown in the following example.

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "dynamodb:CreateTable",
 "dynamodb:TagResource"
 ],
 "Resource": "arn:aws:dynamodb:*:*:table/*",
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
}`

```

2. Assume the role to which the policy was attached, and create a table with the tag key `Title`.

```
ddb_client = boto3.client('dynamodb')

create_table_response = ddb_client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    TableName='myMusicTable',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
        ProvisionedThroughput={
        'ReadCapacityUnits': 1000,
        'WriteCapacityUnits': 500
    },
    Tags=[
        {
            'Key': 'Title',
            'Value': 'ProductManager'
        },
    ],
)



```

###### Without ABAC

If ABAC isn't enabled for your AWS account, DynamoDB doesn’t send the tag keys in the `create-table` command to IAM. The `Null` condition ensures that the condition evaluates to `false` if there are no tag keys in the request. Because the `Deny` policy doesn't match, the `create-table` command completes successfully.

###### With ABAC

If ABAC is enabled for your AWS account, the tag keys passed in the `create-table` command are passed to IAM. The tag key `Title` is evaluated against the condition-based tag key, `CostCenter`, present in the `Deny` policy. The tag key `Title` doesn't match the tag key present in the `Deny` policy because of the `StringNotEquals` operator. Therefore, the `CreateTable` action fails and your table isn’t created. Running the `create-table` command returns an `AccessDeniedException`.

```
An error occurred (AccessDeniedException) when calling the CreateTable operation: User: arn:aws:sts::123456789012:assumed-role/DynamoFullAccessRole/ProductManager is not authorized to perform: dynamodb:CreateTable on resource: arn:aws:dynamodb:us-east-1:123456789012:table/myMusicTable with an explicit deny in an identity-based policy.
```
