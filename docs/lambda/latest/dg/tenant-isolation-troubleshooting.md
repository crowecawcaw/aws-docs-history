# Troubleshooting tenant isolation for Lambda functions

This page addresses common issues that occur when using tenant isolation for
AWS Lambda.

## InvalidParameterValueException

**Error :** Tenant ID configuration not specified or
passed to a function when tenant isolation is not enabled.

### Common causes

This error occurs when invoking a tenant-isolated function without a tenant ID, or
invoking a non-tenant-isolated function with a tenant ID.

### Resolution

Add a tenant ID if the function has tenant isolation enabled, or remove the tenant
ID if the function doesn't have tenant isolation enabled.

## TooManyRequestsException

**Error:** Rate exceeded

### Common causes

In addition to rate limiting based on [maximum concurrent executions](gettingstarted-limits.md#compute-and-storage "gettingstarted-limits.md#compute-and-storage") and [function scaling rate](scaling-behavior.md "scaling-behavior.md"), Lambda limits the maximum number of tenant-aware execution environments (active or idle) that can exist at a time to 2,500 for every 1,000 concurrent executions of your function.

### Resolution

To fix this issue, you can either lower the rate at which invocation requests with unique tenant identifiers are made, [implement retries with backoff and jitter](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/ "https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/"), or [request a function concurrency limit increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md").
