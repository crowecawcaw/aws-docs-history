

# Using DynamoDB as a checkpoint store for LangGraph agents
<a name="ddb-langgraph-checkpoint"></a>

[LangGraph](https://langchain-ai.github.io/langgraph/) is a framework for building stateful, multi-actor AI applications with Large Language Models (LLMs). LangGraph agents require persistent storage to maintain conversation state, enable human-in-the-loop workflows, support fault tolerance, and provide time-travel debugging capabilities. DynamoDB's serverless architecture, single-digit millisecond latency, and automatic scaling make it an ideal checkpoint store for production LangGraph deployments on AWS.

The `langgraph-checkpoint-aws` package provides a `DynamoDBSaver` class that implements the LangGraph checkpoint interface, enabling you to persist agent state in DynamoDB with optional Amazon Simple Storage Service offloading for large checkpoints.

The same package also provides a `DynamoDBStore` class that implements the LangGraph store interface for long-term, cross-thread agent memory, with semantic search backed by DynamoDB vector indexes. For more information, see [Semantic long-term memory for LangGraph agents](ddb-langgraph-memory.md). This topic covers the checkpoint saver.

## Key features
<a name="langgraph-key-features"></a>

State persistence  
Automatically saves agent state after each step, enabling agents to resume from interruptions and recover from failures.

Time to Live-based cleanup  
Automatically expire old checkpoints using DynamoDB Time to Live to manage storage costs.

Compression  
Optionally compress checkpoint data with gzip to reduce storage costs and improve throughput.

Amazon S3 offloading  
Automatically offload large checkpoints (greater than 350 KB) to Amazon Simple Storage Service to work within DynamoDB item size limits.

Sync and async support  
Both synchronous and asynchronous APIs for flexibility in different application architectures.

## Prerequisites
<a name="langgraph-prerequisites"></a>
+ Python 3.10 or later
+ An AWS account with permissions to create DynamoDB tables (and optionally Amazon S3 buckets)
+ AWS credentials configured (see the AWS documentation for credential setup options)

## Installation
<a name="langgraph-installation"></a>

Install the checkpoint package from PyPI:

```
pip install langgraph-checkpoint-aws
```

## Basic usage
<a name="langgraph-basic-usage"></a>

The following example demonstrates how to configure DynamoDB as a checkpoint store for a LangGraph agent:

```
from langgraph.graph import StateGraph
from langgraph_checkpoint_aws import DynamoDBSaver
from typing import TypedDict

# Define your state schema
class State(TypedDict):
    input: str
    result: str

# Initialize the DynamoDB checkpoint saver
checkpointer = DynamoDBSaver(
    table_name="langgraph-checkpoints",
    region_name="us-east-1"
)

# Build your LangGraph workflow
builder = StateGraph(State)
builder.add_node("process", lambda state: {"result": "processed"})
builder.set_entry_point("process")
builder.set_finish_point("process")

# Compile the graph with the DynamoDB checkpointer
graph = builder.compile(checkpointer=checkpointer)

# Invoke the graph with a thread ID to enable state persistence
config = {"configurable": {"thread_id": "session-123"}}
result = graph.invoke({"input": "data"}, config)
```

The `thread_id` in the configuration acts as the partition key in DynamoDB, allowing you to maintain separate conversation threads and retrieve historical states for any thread.

## Production configuration
<a name="langgraph-production-config"></a>

For production deployments, you can enable Time to Live, compression, and Amazon S3 offloading. You can also use the `endpoint_url` parameter to point to a local DynamoDB instance for testing:

```
import boto3
from botocore.config import Config
from langgraph_checkpoint_aws import DynamoDBSaver

# Production configuration
session = boto3.Session(
    profile_name="production",
    region_name="us-east-1"
)

checkpointer = DynamoDBSaver(
    table_name="langgraph-checkpoints",
    session=session,
    ttl_seconds=86400 * 7,           # Expire checkpoints after 7 days
    enable_checkpoint_compression=True,  # Enable gzip compression
    boto_config=Config(
        retries={"mode": "adaptive", "max_attempts": 6},
        max_pool_connections=50
    ),
    s3_offload_config={
        "bucket_name": "my-checkpoint-bucket"
    }
)

# Local testing with DynamoDB Local
local_checkpointer = DynamoDBSaver(
    table_name="langgraph-checkpoints",
    region_name="us-east-1",
    endpoint_url="http://localhost:8000"
)
```

## DynamoDB table configuration
<a name="langgraph-table-config"></a>

The checkpoint saver requires a DynamoDB table with a composite primary key. You can create the table using the following AWS CloudFormation template:

```
AWSTemplateFormatVersion: '2010-09-09'
Description: 'DynamoDB table for LangGraph checkpoint storage'

Parameters:
  TableName:
    Type: String
    Default: langgraph-checkpoints

Resources:
  CheckpointTable:
    Type: AWS::DynamoDB::Table
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      TableName: !Ref TableName
      BillingMode: PAY_PER_REQUEST
      AttributeDefinitions:
        - AttributeName: PK
          AttributeType: S
        - AttributeName: SK
          AttributeType: S
      KeySchema:
        - AttributeName: PK
          KeyType: HASH
        - AttributeName: SK
          KeyType: RANGE
      TimeToLiveSpecification:
        AttributeName: ttl
        Enabled: true
      PointInTimeRecoverySpecification:
        PointInTimeRecoveryEnabled: true
      SSESpecification:
        SSEEnabled: true
```

Deploy the template with the AWS CLI:

```
aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name langgraph-checkpoint \
  --parameter-overrides TableName=langgraph-checkpoints
```

## Required IAM permissions
<a name="langgraph-iam-permissions"></a>

The following IAM policy provides the minimum permissions required for the DynamoDB checkpoint saver. Replace {{111122223333}} with your AWS account ID and update the Region to match your environment.

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "dynamodb:GetItem",
        "dynamodb:PutItem",
        "dynamodb:Query",
        "dynamodb:BatchGetItem",
        "dynamodb:BatchWriteItem"
      ],
      "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/langgraph-checkpoints"
    }
  ]
}
```

If you enable Amazon S3 offloading, add the following statement to the policy:

```
{
  "Effect": "Allow",
  "Action": [
    "s3:PutObject",
    "s3:GetObject",
    "s3:DeleteObject",
    "s3:PutObjectTagging"
  ],
  "Resource": "arn:aws:s3:::my-checkpoint-bucket/*"
},
{
  "Effect": "Allow",
  "Action": [
    "s3:GetBucketLifecycleConfiguration",
    "s3:PutBucketLifecycleConfiguration"
  ],
  "Resource": "arn:aws:s3:::my-checkpoint-bucket"
}
```

## Asynchronous usage
<a name="langgraph-async"></a>

For asynchronous applications, use the async methods provided by the checkpoint saver:

```
import asyncio
from langgraph.graph import StateGraph
from langgraph_checkpoint_aws import DynamoDBSaver
from typing import TypedDict

class State(TypedDict):
    input: str
    result: str

async def main():
    checkpointer = DynamoDBSaver(
        table_name="langgraph-checkpoints",
        region_name="us-east-1"
    )
    builder = StateGraph(State)
    builder.add_node("process", lambda state: {"result": "processed"})
    builder.set_entry_point("process")
    builder.set_finish_point("process")
    graph = builder.compile(checkpointer=checkpointer)

    config = {"configurable": {"thread_id": "async-session-123"}}
    result = await graph.ainvoke({"input": "data"}, config)
    return result

asyncio.run(main())
```

## Error handling
<a name="langgraph-error-handling"></a>

Common error scenarios:
+ **Table not found**: Verify the `table_name` and `region_name` match your DynamoDB table.
+ **Throttling**: If you see `ProvisionedThroughputExceededException`, consider switching to on-demand billing mode or increasing provisioned capacity.
+ **Item size exceeded**: If checkpoints exceed 350 KB, enable Amazon S3 offloading (see [Production configuration](#langgraph-production-config)).
+ **Credential errors**: Verify your AWS credentials are valid and have the [required permissions](#langgraph-iam-permissions).

## Additional resources
<a name="langgraph-additional-resources"></a>
+ [langgraph-checkpoint-aws on PyPI](https://pypi.org/project/langgraph-checkpoint-aws/)
+ [langgraph-checkpoint-aws on GitHub](https://github.com/langchain-ai/langchain-aws/tree/main/libs/langgraph-checkpoint-aws)
+ [LangGraph documentation](https://langchain-ai.github.io/langgraph/)
+ [DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
+ [Build durable AI agents with LangGraph and Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-durable-ai-agents-with-langgraph-and-amazon-dynamodb/)