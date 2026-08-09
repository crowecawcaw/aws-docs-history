# Get started with Instances using the AWS CLI or SDK

This tutorial walks through hosting an agent on the **Instances** compute type with the AWS Command Line Interface (AWS CLI) and SDKs. You first create a [capacity provider](runtime-instances-how-it-works.md#runtime-instances-capacity-provider "runtime-instances-how-it-works.md#runtime-instances-capacity-provider") that defines the Amazon Elastic Compute Cloud (Amazon EC2) infrastructure, then create an agent runtime that uses it, and finally invoke the agent.

For the prerequisites, see [Get started with Instances](runtime-instances-getting-started.md "runtime-instances-getting-started.md").

###### Note

Parameter names in these examples follow the AgentCore control plane model. For the authoritative request and response shapes, see the [Amazon Bedrock AgentCore Control API Reference](../../../bedrock-agentcore-control/latest/APIReference/Welcome.md "../../../bedrock-agentcore-control/latest/APIReference/Welcome.md").

## Step 1: Create a capacity provider

Use the `CreateCapacityProvider` operation to define your EC2 infrastructure. The request takes a `permissionsConfiguration` (the IAM role AgentCore uses to operate the capacity provider) and a `computeConfiguration` that describes the EC2 instances through a launch template. The following example creates a Linux capacity provider with a single allowed instance type and a persistent EBS volume.

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore-control create-capacity-provider \
--name "my_capacity_provider" \
--permissions-configuration '{
"capacityProviderOperatorRoleArn": "arn:aws:iam::111122223333:role/AgentCoreCapacityProviderOperatorRole"
}' \
--compute-configuration '{
"ec2Configuration": {
"launchTemplateSource": {
"launchParameters": {
"operatingSystem": "LINUX_X86_64",
"instanceRequirements": {
"allowedInstanceTypes": ["m5.large"]
}
}
},
"vpcConfiguration": {
"subnets": ["subnet-0123456789abcdef0"],
"securityGroups": ["sg-0123456789abcdef0"]
},
"volumes": [
{ "ebsConfiguration": { "name": "scratch", "sizeGiB": 50, "volumeType": "gp3" } }
]
}
}'

```



 AWS SDK

1. Python example using boto3 to create a capacity provider.



```

import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client.create_capacity_provider(
name="my_capacity_provider",
permissionsConfiguration={
"capacityProviderOperatorRoleArn": "arn:aws:iam::111122223333:role/AgentCoreCapacityProviderOperatorRole"
},
computeConfiguration={
"ec2Configuration": {
"launchTemplateSource": {
"launchParameters": {
"operatingSystem": "LINUX_X86_64",
"instanceRequirements": {
"allowedInstanceTypes": ["m5.large"],
},
}
},
"vpcConfiguration": {
"subnets": ["subnet-0123456789abcdef0"],
"securityGroups": ["sg-0123456789abcdef0"],
},
"volumes": [
{"ebsConfiguration": {"name": "scratch", "sizeGiB": 50, "volumeType": "gp3"}}
],
}
},
)

print(f"Capacity provider ARN: {response['capacityProviderArn']}")

````



To run GPU workloads, include a supported GPU instance type in `allowedInstanceTypes`. AgentCore provisions the GPU drivers on the instance, so standard container images work without bundling drivers. The supported families are `g4dn`, `g5`, `g6`, `g6e`, `gr6`, `g6f`, `gr6f`, `g7e`, and `inf2`. If you include an accelerator instance type from an unsupported family, the request fails with a `ValidationException`. For more information, see [Use GPU instance types](runtime-instances-how-it-works.md#runtime-instances-gpu "runtime-instances-how-it-works.md#runtime-instances-gpu").


Poll `GetCapacityProvider` until the status is `ACTIVE` before associating the capacity provider with a runtime.


## Step 2: Create an agent runtime on the capacity provider


Create an agent runtime with a `capacityProviderConfiguration` that references your capacity provider. To mount a volume defined on the capacity provider into the agent’s filesystem, add a `capacityProviderVolume` entry to `filesystemConfigurations` that references the volume by name. Mount paths must be under `/mnt` with a single subdirectory (for example, `/mnt/scratch`).


###### Example



 AWS CLI

1. ```
aws bedrock-agentcore-control create-agent-runtime \
  --agent-runtime-name "my_instances_agent" \
  --role-arn "arn:aws:iam::111122223333:role/AgentRuntimeRole" \
  --agent-runtime-artifact '{
    "containerConfiguration": {
      "containerUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
    }
  }' \
  --capacity-provider-configuration '{
    "capacityProviderArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:capacity-provider/my_capacity_provider-a1b2c3d4e5"
  }' \
  --filesystem-configurations '[
    {
      "capacityProviderVolume": { "volumeName": "scratch", "mountPath": "/mnt/scratch" }
    }
  ]'
````

AWS SDK

1. Python example using boto3 to create an agent runtime on Instances.

```
import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client.create_agent_runtime(
    agentRuntimeName="my_instances_agent",
    roleArn="arn:aws:iam::111122223333:role/AgentRuntimeRole",
    agentRuntimeArtifact={
        "containerConfiguration": {
            "containerUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
        }
    },
    capacityProviderConfiguration={
        "capacityProviderArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:capacity-provider/my_capacity_provider-a1b2c3d4e5",
    },
    filesystemConfigurations=[
        {
            "capacityProviderVolume": {"volumeName": "scratch", "mountPath": "/mnt/scratch"}
        }
    ],
)

print(f"Agent runtime ARN: {response['agentRuntimeArn']}")
```

## Step 3: Invoke the agent

Invoke the runtime the same way you would a microVM-backed runtime. Reuse the same `runtimeSessionId` across invocations to keep the session on the same instance. This lets your agent access data from previous invocations. To co-locate collaborating agents, use the same `runtimeSessionId` across multiple runtimes that share a capacity provider.

```
import boto3
import json

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.invoke_agent_runtime(
    agentRuntimeArn="arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/my_instances_agent-suffix",
    runtimeSessionId="project-xyz-0000000000000000000000000000",  # 33+ chars; reuse to keep the session
    payload=json.dumps({"prompt": "Analyze the sales data and summarize the key trends."}).encode(),
    qualifier="DEFAULT",
)

print("Agent response:", json.loads(response["response"].read()))
```

The first invocation for a new session provisions an EC2 instance in your account and launches the agent, so expect additional latency. Subsequent invocations to the same session reuse the running instance.

## Co-locate multiple agents on one instance

When two agent runtimes reference the **same** capacity provider and you invoke them with the **same**
`runtimeSessionId`, both agents run on the same EC2 instance. There, they can share the volume configured in their filesystem configuration. Agents collaborate by reading and writing files on that shared volume — each agent is invoked independently and does not otherwise share state. For example, a test runner can write results to the volume, and a code analyzer invoked on the same session can then read them. For the boundary between agents on a shared instance, see [Security model and permissions for Runtime Instances](runtime-instances-security.md "runtime-instances-security.md").

```
import boto3
import json

client = boto3.client("bedrock-agentcore", region_name="us-west-2")
session_id = "collab-session-000000000000000000000"

# Agent A — created on capacity provider "my_capacity_provider"
client.invoke_agent_runtime(
    agentRuntimeArn="arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/test-runner-suffix",
    runtimeSessionId=session_id,
    payload=json.dumps({"prompt": "Run the test suite for project ABC"}).encode(),
    qualifier="DEFAULT",
)

# Agent B — a different runtime that shares the SAME capacity provider and session ID,
# so it runs on the same instance as Agent A and can read the files Agent A wrote to the shared volume.
client.invoke_agent_runtime(
    agentRuntimeArn="arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/code-analyzer-suffix",
    runtimeSessionId=session_id,
    payload=json.dumps({"prompt": "Analyze the code for project ABC"}).encode(),
    qualifier="DEFAULT",
)
```

Each agent runs with its own IAM credentials derived from its runtime’s execution role, so you can grant the collaborating agents different permissions although they share the same instance. However, because agents on the same instance are not isolated from each other, any agent can potentially read another agent’s credentials. Co-locate only agents that are mutually trusted. For more information, see [Security model and permissions for Runtime Instances](runtime-instances-security.md "runtime-instances-security.md").

## Clean up: stop and delete sessions

###### Warning

To avoid ongoing charges for the Amazon EC2 instances and Amazon EBS volumes provisioned in your account, delete the sessions and capacity providers you no longer need when you finish this tutorial.

A session can host multiple agent runtimes on the same instance, so AgentCore provides two distinct operations:

- **Stop an agent runtime in a session** – `StopRuntimeSession` stops a single agent runtime within a session, identified by the runtime ARN and the session ID. Other agent runtimes that share the same session and instance are unaffected.
- **Delete a session** – `DeleteCapacityProviderSession` deletes the entire session and deprovisions the EC2 resources created in your account (instance, network interface, and any persistent EBS volumes), so you stop incurring infrastructure and storage costs.

To stop a specific agent runtime on a session, call the [StopRuntimeSession](../APIReference/API_StopRuntimeSession.md "../APIReference/API_StopRuntimeSession.md") operation with the runtime ARN and the session ID.

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore stop-runtime-session \
--agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/my_instances_agent-suffix" \
--runtime-session-id "project-xyz-0000000000000000000000000000"

```



 AWS SDK

1. Python example using boto3 to stop a runtime session.



```

import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

client.stop_runtime_session(
agentRuntimeArn="arn:aws:bedrock-agentcore:us-west-2:111122223333:runtime/my_instances_agent-suffix",
runtimeSessionId="project-xyz-0000000000000000000000000000",
)

````



To delete a session and deprovision all of its resources — including any persistent EBS volumes — call `DeleteCapacityProviderSession` with the capacity provider ID and the session ID. The operation is idempotent and asynchronous: it returns immediately while AgentCore terminates the instance and deletes the volumes in the background.


###### Example



 AWS CLI

1. ```
aws bedrock-agentcore delete-capacity-provider-session \
  --capacity-provider-id "my_capacity_provider-a1b2c3d4e5" \
  --session-id "project-xyz-0000000000000000000000000000"
````

AWS SDK

1. Python example using boto3 to delete a capacity provider session.

```
import boto3

client = boto3.client("bedrock-agentcore", region_name="us-west-2")

response = client.delete_capacity_provider_session(
    capacityProviderId="my_capacity_provider-a1b2c3d4e5",
    sessionId="project-xyz-0000000000000000000000000000",
)

print("Session status:", response["status"])
```

## Delete a capacity provider

When you no longer need a capacity provider, delete it with the `DeleteCapacityProvider` operation. Before you can delete a capacity provider, you must remove all references to it by deleting the associated versions, endpoints, or runtimes from each runtime’s detail page. If references remain, the delete request fails with a `ValidationException`. Deleting a capacity provider stops and deletes all of its associated sessions and their persistent storage. The operation is asynchronous; identify the capacity provider by its ID.

###### Example

AWS CLI

1. ```

   ```

aws bedrock-agentcore-control delete-capacity-provider \
--capacity-provider-id "my_capacity_provider-a1b2c3d4e5"

```



 AWS SDK

1. Python example using boto3 to delete a capacity provider.



```

import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

client.delete_capacity_provider(
capacityProviderId="my_capacity_provider-a1b2c3d4e5",
)

```

```
