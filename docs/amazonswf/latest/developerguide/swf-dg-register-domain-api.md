# Registering a Domain with Amazon SWF

Your workflow and activity types and the workflow execution itself are all scoped to a
_domain_. Domains isolate a set of types, executions, and task lists from others within the same
account.

You can register a domain by using the AWS Management Console or by using the `RegisterDomain` action in the Amazon SWF API. The following example uses the API.

```
https://swf.us-east-1.amazonaws.com
RegisterDomain
{
  "name" : "867530901",
  "description" : "music",
  "workflowExecutionRetentionPeriodInDays" : "60"
}
```

The parameters are specified in JavaScript Object Notation (JSON) format. Here, the retention period is set to
60 days. During the retention period, all information about the workflow execution is available through visibility
operations using either the AWS Management Console or the Amazon SWF API.

After registering the domain, you should register the workflow type and the activity types used by the
workflow. You need to register the domain first because a registered domain name is part of the required information
for registering workflow and activity types.

## See Also

`RegisterDomain` in
the _Amazon Simple Workflow Service API Reference_
