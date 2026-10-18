

# Connect a service to the Agent Space
<a name="next-gen-devops-agent-connect"></a>

After your invoker role has the required DevOps Agent permissions, you can connect a service to your Agent Space. Connect a service by providing the Agent Space ARN in the service's DevOps Agent configuration. You can do this when you create a service or when you update an existing one.

The following command connects an existing service to an Agent Space.

```
aws resiliencehubv2 update-service \
  --service-arn {{service-arn}} \
  --dev-ops-agent-configuration '{"agentSpaceArn": "{{agent-space-arn}}"}'
```

To check the connection status, call `GetService` and inspect the `devOpsAgentConfiguration` field.

```
aws resiliencehubv2 get-service \
  --service-arn {{service-arn}} \
  --query 'service.devOpsAgentConfiguration.status'
```

To disconnect a service later, update it with an empty DevOps Agent configuration (`'{}'`). This clears the connection without affecting the Agent Space itself.