# Testing and debugging durable functions

Testing and debugging durable functions locally works similarly to regular Lambda functions, with automatic support for checkpointing and replay. This guide covers common testing scenarios and troubleshooting techniques.

## Local testing workflow

When testing durable functions locally, the workflow differs from regular Lambda functions:

###### Durable function testing workflow

1. Build your application:

```
`$` `sam build`
```

2. Invoke your durable function:

```
`$` `sam local invoke MyDurableFunction --durable-execution-name test`
```

3. Check execution history if needed:

```
`$` `sam local execution history `execution-id``
```

## Common testing scenarios

### Testing checkpointing behavior

To test that your function properly checkpoints state:

```
# Example Python durable function
def handler(event, context):
    # This will create a checkpoint
    context.wait(10)  # Wait 10 seconds

    # Function resumes here after wait
    return {"message": "Function resumed after wait"}

```

When you invoke this function locally, the wait period is handled automatically.

### Testing callback scenarios

For functions that wait for external callbacks:

1. Start your durable function that waits for a callback
2. In another terminal, resolve the callback:

```
`$` `sam local callback succeed `callback-id``
```

3. Observe the function resume execution

## Troubleshooting

### Durable function not executing properly

**Problem:** The function doesn't behave as a durable function.

**Solutions:**

- Verify that `DurableConfig` is set in your SAM template
- Ensure your function code uses durable function SDK methods (e.g., `context.wait()`)
- Check that you're using a supported runtime (TypeScript, JavaScript, Python)

### Cannot retrieve execution history

**Problem:** The `local execution history` command returns no results.

**Solutions:**

- Verify the execution ID is correct
- Check that the function has been invoked at least once

### Callback commands not working

**Problem:** Callback commands don't resolve pending operations.

**Solutions:**

- Verify the callback ID is correct
- Ensure the function is actually waiting for a callback
- Verify you're using the correct callback command syntax

## Debugging tips

- **Use execution history** - Review execution history to understand the flow of your durable function
- **Test incrementally** - Start with simple wait operations before adding complex logic
- **Use verbose logging** - Enable detailed logging to trace execution flow

## Learn more

For more information about testing and debugging, see:

- [Introduction to testing with sam local invoke](using-sam-cli-local-invoke.md "using-sam-cli-local-invoke.md") - Local invoke documentation
- [sam local execution history](sam-cli-command-reference-sam-local-execution-history.md "sam-cli-command-reference-sam-local-execution-history.md") - Execution history
