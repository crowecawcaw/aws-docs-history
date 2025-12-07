# Invoking durable Lambda functions

Durable Lambda functions can be invoked using the same methods as default Lambda functions, but with important considerations for long-running executions.
This section covers invocation patterns, execution management, and best practices for durable functions.

## Synchronous invocation limits

Synchronous invocations of durable Lambda functions are limited to 15 minutes, the same as default Lambda functions. If your durable function needs to run longer than 15 minutes, it must be invoked asynchronously.

**When to use synchronous invocation:** Use for durable functions that complete within 15 minutes and when you need immediate results, such as quick approval workflows or short data processing tasks.

## Asynchronous invocation for long-running workflows

For durable functions that may run longer than 15 minutes, use asynchronous invocation. This allows the function to continue running while your client receives an immediate acknowledgment.

TypeScript

```

import { LambdaClient, InvokeCommand } from "@aws-sdk/client-lambda";

const client = new LambdaClient({});

// Asynchronous invocation
const command = new InvokeCommand({
  FunctionName: "my-durable-function",
  InvocationType: "Event", // Asynchronous
  Payload: JSON.stringify({ orderId: "12345" })
});

await client.send(command);

```

Python

```

import boto3
import json

client = boto3.client('lambda')

# Asynchronous invocation
response = client.invoke(
    FunctionName='my-durable-function',
    InvocationType='Event',  # Asynchronous
    Payload=json.dumps({'order_id': '12345'})
)

```

## Execution management APIs

Lambda provides APIs to manage and monitor durable function executions, including listing executions, getting execution status, and stopping running executions.

TypeScript

```

// Get execution status
const statusCommand = new InvokeCommand({
  FunctionName: "my-durable-function",
  InvocationType: "RequestResponse",
  Payload: JSON.stringify({
    action: "getStatus",
    executionId: "exec-123"
  })
});

const result = await client.send(statusCommand);

```

Python

```

# Get execution status
response = client.invoke(
    FunctionName='my-durable-function',
    InvocationType='RequestResponse',
    Payload=json.dumps({
        'action': 'get_status',
        'execution_id': 'exec-123'
    })
)

```
