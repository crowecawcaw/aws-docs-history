# Troubleshooting Ruler

Using [Monitor Amazon Managed Service for Prometheus events with CloudWatch Logs](CW-logs.md "CW-logs.md"), you can troubleshoot Alert
Manager and Ruler related issues. This section contains ruler related troubleshooting
topics.

**When the log contains the following ruler failure
error**

```
{
    "workspaceId": "ws-12345c67-89c0-4d12-345b-f14db70f7a99",
    "message": {
        "log": "Evaluating rule failed, name=failure, group=canary_long_running_vl_namespace, namespace=canary_long_running_vl_namespace, err=found duplicate series for the match group {dimension1=\\\"1\\\"} on the right hand-side of the operation: [{__name__=\\\"fake_metric2\\\", dimension1=\\\"1\\\", dimension2=\\\"b\\\"}, {__name__=\\\"fake_metric2\\\", dimension1=\\\"1\\\", dimension2=\\\"a\\\"}];many-to-many matching not allowed: matching labels must be unique on one side",
        "level": "ERROR",
        "name": "failure",
        "group": "canary_long_running_vl_namespace",
        "namespace": "canary_long_running_vl_namespace"
    },
    "component": "ruler"
}

```

This means that some error occurred while executing the rule.

**Action to take**

Use the error message to troubleshoot the rule execution.
