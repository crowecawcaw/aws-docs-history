

# Resources requiring manual cleanup before or after teardown
<a name="pre-teardown-resource-notes"></a>

## Amazon ECS clusters and services
<a name="ecs-clusters-and-services"></a>

The guidance deploys several Amazon ECS services across dedicated clusters. CloudFormation removes these services when each stack is destroyed, but you should confirm the following clusters are fully drained and deleted after teardown:
+  `cms-<stage>-simulation` — simulation service and FleetWise Edge agent tasks
+  `cms-<stage>-commands` — vehicle command dispatcher
+  `cms-<stage>-ws-fanout` — WebSocket fanout consumer
+  `cms-<stage>-oem1-connector` — OEM1 gRPC streaming connector (if deployed)

If any ECS tasks remain in a `STOPPING` or `DEPROVISIONING` state after the stack delete completes, wait up to 10 minutes for ECS to drain them. Amazon VPC and ECS resources can remain queryable for a short period after deletion — this is expected behavior.

## Amazon Bedrock agents
<a name="bedrock-agents-manual-delete"></a>

The guidance creates Amazon Bedrock agents and agent aliases via the `bedrock-agents` CDK stack. When this stack is destroyed, CloudFormation deletes the Bedrock **agent resource** it manages; however, the **AgentCore Runtime** endpoint (if deployed separately via the AgentCore SDK) is not managed by the CDK stack and is not automatically deleted.

To remove AgentCore Runtime deployments:

1. Sign in to the [Amazon Bedrock console](https://console.aws.amazon.com/bedrock/).

1. In the navigation pane, choose **AgentCore** and then **Runtimes**.

1. Locate runtimes associated with the guidance deployment (for example, runtimes prefixed with `vsa_supervisor_`).

1. Select each runtime and choose **Delete**.

**Note**  
If you deployed the AgentCore runtime using `agentcore deploy`, you can also delete it using the AgentCore CLI:  

```
agentcore delete --runtime-id <runtime-id>
```

## Amazon ECR container images
<a name="ecr-images-note"></a>

The guidance uses pre-built simulation container images published to the AWS Solutions public Amazon ECR registry. These images are shared across all deployments and are not per-customer resources — they are not deleted during uninstall.

If you built and pushed custom images to a private Amazon ECR repository, you can delete those repositories after teardown:

1. Sign in to the [Amazon ECR console](https://console.aws.amazon.com/ecr/).

1. Choose **Repositories** from the left navigation pane.

1. Locate repositories prefixed with `cms-<stage>`.

1. Select a repository and choose **Delete**.