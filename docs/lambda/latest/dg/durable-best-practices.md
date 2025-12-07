# Best practices for Lambda durable functions

Durable functions use a replay-based execution model that requires different patterns than traditional Lambda functions. Follow these best practices to build reliable, cost-effective workflows.

## Write deterministic code

During replay, your function runs from the beginning and must follow the same execution path as the original run. Code outside durable operations must be deterministic, producing the same results given the same inputs.

**Wrap non-deterministic operations in steps:**

- Random number generation and UUIDs
- Current time or timestamps
- External API calls and database queries
- File system operations

TypeScript

```

import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';
import { randomUUID } from 'crypto';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    // Generate transaction ID inside a step
    const transactionId = await context.step('generate-transaction-id', async () => {
      return randomUUID();
    });

    // Use the same ID throughout execution, even during replay
    const payment = await context.step('process-payment', async () => {
      return processPayment(event.amount, transactionId);
    });

    return { statusCode: 200, transactionId, payment };
  }
);

```

Python

```

from aws_durable_execution_sdk_python import durable_execution, DurableContext
import uuid

@durable_execution
def handler(event, context: DurableContext):
    # Generate transaction ID inside a step
    transaction_id = context.step(
        lambda _: str(uuid.uuid4()),
        name='generate-transaction-id'
    )

    # Use the same ID throughout execution, even during replay
    payment = context.step(
        lambda _: process_payment(event['amount'], transaction_id),
        name='process-payment'
    )

    return {'statusCode': 200, 'transactionId': transaction_id, 'payment': payment}

```

###### Important

Don't use global variables or closures to share state between steps. Pass data through return values. Global state breaks during replay because steps return cached results but global variables reset.

**Avoid closure mutations:** Variables captured in closures can lose mutations during replay. Steps return cached results, but variable updates outside the step aren't replayed.

TypeScript

```

// ❌ WRONG: Mutations lost on replay
export const handler = withDurableExecution(async (event, context) => {
  let total = 0;

  for (const item of items) {
    await context.step(async () => {
      total += item.price; // ⚠️ Mutation lost on replay!
      return saveItem(item);
    });
  }

  return { total }; // Inconsistent value!
});

// ✅ CORRECT: Accumulate with return values
export const handler = withDurableExecution(async (event, context) => {
  let total = 0;

  for (const item of items) {
    total = await context.step(async () => {
      const newTotal = total + item.price;
      await saveItem(item);
      return newTotal; // Return updated value
    });
  }

  return { total }; // Consistent!
});

// ✅ EVEN BETTER: Use map for parallel processing
export const handler = withDurableExecution(async (event, context) => {
  const results = await context.map(
    items,
    async (ctx, item) => {
      await ctx.step(async () => saveItem(item));
      return item.price;
    }
  );

  const total = results.getResults().reduce((sum, price) => sum + price, 0);
  return { total };
});

```

Python

```

# ❌ WRONG: Mutations lost on replay
@durable_execution
def handler(event, context: DurableContext):
    total = 0

    for item in items:
        context.step(
            lambda _: save_item_and_mutate(item, total),  # ⚠️ Mutation lost on replay!
            name=f'save-item-{item["id"]}'
        )

    return {'total': total}  # Inconsistent value!

# ✅ CORRECT: Accumulate with return values
@durable_execution
def handler(event, context: DurableContext):
    total = 0

    for item in items:
        total = context.step(
            lambda _: save_item_and_return_total(item, total),
            name=f'save-item-{item["id"]}'
        )

    return {'total': total}  # Consistent!

# ✅ EVEN BETTER: Use map for parallel processing
@durable_execution
def handler(event, context: DurableContext):
    def process_item(ctx, item):
        ctx.step(lambda _: save_item(item))
        return item['price']

    results = context.map(items, process_item)
    total = sum(results.get_results())

    return {'total': total}

```

## Design for idempotency

Operations may execute multiple times due to retries or replay. Non-idempotent operations cause duplicate side effects like charging customers twice or sending multiple emails.

**Use idempotency tokens:** Generate tokens inside steps and include them with external API calls to prevent duplicate operations.

TypeScript

```

import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    // Generate idempotency token once
    const idempotencyToken = await context.step('generate-idempotency-token', async () => {
      return crypto.randomUUID();
    });

    // Use token to prevent duplicate charges
    const charge = await context.step('charge-payment', async () => {
      return paymentService.charge({
        amount: event.amount,
        cardToken: event.cardToken,
        idempotencyKey: idempotencyToken
      });
    });

    return { statusCode: 200, charge };
  }
);

```

Python

```

from aws_durable_execution_sdk_python import durable_execution, DurableContext
import uuid

@durable_execution
def handler(event, context: DurableContext):
    # Generate idempotency token once
    idempotency_token = context.step(
        lambda _: str(uuid.uuid4()),
        name='generate-idempotency-token'
    )

    # Use token to prevent duplicate charges
    def charge_payment(_):
        return payment_service.charge(
            amount=event['amount'],
            card_token=event['cardToken'],
            idempotency_key=idempotency_token
        )

    charge = context.step(charge_payment, name='charge-payment')

    return {'statusCode': 200, 'charge': charge}

```

**Use at-most-once semantics:** For critical operations that must never duplicate (financial transactions, inventory deductions), configure at-most-once execution mode.

TypeScript

```

// Critical operation that must not duplicate
await context.step('deduct-inventory', async () => {
  return inventoryService.deduct(event.productId, event.quantity);
}, {
  executionMode: 'AT_MOST_ONCE_PER_RETRY'
});

```

Python

```

# Critical operation that must not duplicate
context.step(
    lambda _: inventory_service.deduct(event['productId'], event['quantity']),
    name='deduct-inventory',
    config=StepConfig(execution_mode='AT_MOST_ONCE_PER_RETRY')
)

```

**Database idempotency:** Use check-before-write patterns, conditional updates, or upsert operations to prevent duplicate records.

## Manage state efficiently

Every checkpoint saves state to persistent storage. Large state objects increase costs, slow checkpointing, and impact performance. Store only essential workflow coordination data.

**Keep state minimal:**

- Store IDs and references, not full objects
- Fetch detailed data within steps as needed
- Use Amazon S3 or DynamoDB for large data, pass references in state
- Avoid passing large payloads between steps

TypeScript

```

import { withDurableExecution, DurableContext } from '@aws/durable-execution-sdk-js';

export const handler = withDurableExecution(
  async (event: any, context: DurableContext) => {
    // Store only the order ID, not the full order object
    const orderId = event.orderId;

    // Fetch data within each step as needed
    await context.step('validate-order', async () => {
      const order = await orderService.getOrder(orderId);
      return validateOrder(order);
    });

    await context.step('process-payment', async () => {
      const order = await orderService.getOrder(orderId);
      return processPayment(order);
    });

    return { statusCode: 200, orderId };
  }
);

```

Python

```

from aws_durable_execution_sdk_python import durable_execution, DurableContext

@durable_execution
def handler(event, context: DurableContext):
    # Store only the order ID, not the full order object
    order_id = event['orderId']

    # Fetch data within each step as needed
    context.step(
        lambda _: validate_order(order_service.get_order(order_id)),
        name='validate-order'
    )

    context.step(
        lambda _: process_payment(order_service.get_order(order_id)),
        name='process-payment'
    )

    return {'statusCode': 200, 'orderId': order_id}

```

## Design effective steps

Steps are the fundamental unit of work in durable functions. Well-designed steps make workflows easier to understand, debug, and maintain.

**Step design principles:**

- **Use descriptive names** - Names like `validate-order` instead of `step1` make logs and errors easier to understand
- **Keep names static** - Don't use dynamic names with timestamps or random values. Step names must be deterministic for replay
- **Balance granularity** - Break complex operations into focused steps, but avoid excessive tiny steps that increase checkpoint overhead
- **Group related operations** - Operations that should succeed or fail together belong in the same step

## Use wait operations efficiently

Wait operations suspend execution without consuming resources or incurring costs. Use them instead of keeping Lambda running.

**Time-based waits:** Use `context.wait()` for delays instead of `setTimeout` or `sleep`.

**External callbacks:** Use `context.waitForCallback()` when waiting for external systems. Always set timeouts to prevent indefinite waits.

**Polling:** Use `context.waitForCondition()` with exponential backoff to poll external services without overwhelming them.

TypeScript

```

// Wait 24 hours without cost
await context.wait({ seconds: 86400 });

// Wait for external callback with timeout
const result = await context.waitForCallback(
  'external-job',
  async (callbackId) => {
    await externalService.submitJob({
      data: event.data,
      webhookUrl: `https://api.example.com/callbacks/${callbackId}`
    });
  },
  { timeout: { seconds: 3600 } }
);

```

Python

```

# Wait 24 hours without cost
context.wait(86400)

# Wait for external callback with timeout
result = context.wait_for_callback(
    lambda callback_id: external_service.submit_job(
        data=event['data'],
        webhook_url=f'https://api.example.com/callbacks/{callback_id}'
    ),
    name='external-job',
    config=WaitForCallbackConfig(timeout_seconds=3600)
)

```

## Additional considerations

**Error handling:** Retry transient failures like network timeouts and rate limits. Don't retry permanent failures like invalid input or authentication errors. Configure retry strategies with appropriate max attempts and backoff rates. For detailed examples, see [Error handling and retries](durable-execution-sdk-retries.md "durable-execution-sdk-retries.md").

**Performance:** Minimize checkpoint size by storing references instead of full payloads. Use `context.parallel()` and `context.map()` to execute independent operations concurrently. Batch related operations to reduce checkpoint overhead.

**Versioning:** Invoke functions with version numbers or aliases to pin executions to specific code versions. Ensure new code versions can handle state from older versions. Don't rename steps or change their behavior in ways that break replay.

**Serialization:** Use JSON-compatible types for operation inputs and results. Convert dates to ISO strings and custom objects to plain objects before passing them to durable operations.

**Monitoring:** Enable structured logging with execution IDs and step names. Set up CloudWatch alarms for error rates and execution duration. Use tracing to identify bottlenecks. For detailed guidance, see [Monitoring and debugging](durable-monitoring.md "durable-monitoring.md").

**Testing:** Test happy path, error handling, and replay behavior. Test timeout scenarios for callbacks and waits. Use local testing to reduce iteration time. For detailed guidance, see [Testing durable functions](durable-testing.md "durable-testing.md").

**Common mistakes to avoid:** Don't nest `context.step()` calls, use child contexts instead. Wrap non-deterministic operations in steps. Always set timeouts for callbacks. Balance step granularity with checkpoint overhead. Store references instead of large objects in state.

## Additional resources

- [Python SDK documentation](https://github.com/aws/aws-durable-execution-sdk-python/tree/main/docs "https://github.com/aws/aws-durable-execution-sdk-python/tree/main/docs") - Complete API reference, testing patterns, and advanced examples
- [TypeScript SDK documentation](https://github.com/aws/aws-durable-execution-sdk-js/tree/main/docs "https://github.com/aws/aws-durable-execution-sdk-js/tree/main/docs") - Complete API reference, testing patterns, and advanced examples
