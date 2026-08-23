# Example 4: Tagging streams using CloudFormation

You can specify tags on DynamoDB Streams directly in your CloudFormation templates. Stream tags are defined within the `StreamSpecification` property for standard tables, and within the `ReplicaStreamSpecification` property for global tables.

## AWS::DynamoDB::Table

```
Resources:
  MyTable:
    Type: AWS::DynamoDB::Table
    Properties:
      TableName: MyTable
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
      Tags:
        - Key: TableEnv
          Value: Production
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
        Tags:
          - Key: StreamEnv
            Value: Production
          - Key: StreamTeam
            Value: Payments
```

## AWS::DynamoDB::GlobalTable

```
Resources:
  MyGlobalTable:
    Type: AWS::DynamoDB::GlobalTable
    Properties:
      TableName: MyGlobalTable
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      BillingMode: PAY_PER_REQUEST
      StreamSpecification:
        StreamViewType: NEW_AND_OLD_IMAGES
      Replicas:
        - Region: us-east-1
          Tags:
            - Key: TableEnv
              Value: Production
          ReplicaStreamSpecification:
            Tags:
              - Key: StreamEnv
                Value: Production
              - Key: StreamTeam
                Value: Payments
        - Region: eu-west-1
          Tags:
            - Key: TableEnv
              Value: Production
          ReplicaStreamSpecification:
            Tags:
              - Key: StreamEnv
                Value: Production
              - Key: StreamTeam
                Value: Payments
```

In addition to explicit stream tags, CloudFormation also propagates stack-level tags to streams. If your stack has tags configured, those tags are automatically applied to all resources in the stack, including streams.

###### Important

The IAM role used for your CloudFormation deployment must have `dynamodb:TagResource` and `dynamodb:UntagResource` permissions on stream resources (`arn:aws:dynamodb:*:*:table/*/stream/*`) to apply tags to streams. If these permissions are missing, see [CloudFormation deployments fail when tagging streams](abac-troubleshooting-streams.md#abac-troubleshooting-streams-cfn-tagging "abac-troubleshooting-streams.md#abac-troubleshooting-streams-cfn-tagging") for details.
