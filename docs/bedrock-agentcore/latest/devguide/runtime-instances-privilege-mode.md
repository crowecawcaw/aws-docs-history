

# Configure the privilege mode for Runtime Instances

The privilege mode controls whether agents on the **Instances** compute type of AgentCore Runtime run with elevated privileges on their instance. Run agents with elevated privileges when their tools need full access to the operating system. For example, with elevated privileges your agents can build container images and run containers, install system packages, or change kernel settings. Before you run agents with elevated privileges, review the security implications in [Privilege mode](runtime-instances-security.md#runtime-instances-privilege-mode-security).

**Topics**
+ [Privilege modes](#runtime-instances-privilege-modes)
+ [One agent per session](#runtime-instances-privilege-mode-session-limit)
+ [Run containers in a privileged agent](#runtime-instances-privilege-mode-containers)
+ [Create an agent runtime with elevated privileges](#runtime-instances-privilege-mode-create)
+ [Change the privilege mode](#runtime-instances-privilege-mode-update)
+ [Check the privilege mode of an agent runtime](#runtime-instances-privilege-mode-verify)

## Privilege modes
<a name="runtime-instances-privilege-modes"></a>

You set the privilege mode in the `operatingSystemConfiguration` field of `capacityProviderConfiguration` on the agent runtime. This field has one member for each operating system. On Linux, you set `linux.privilegeMode` to one of the following values:

 `STANDARD`   
Your agent runs without elevated privileges. On Linux, the agent doesn’t run as root and has no Linux capabilities. A code agent runs as a dedicated, unprivileged user. A container agent runs in a user namespace. Root inside the container maps to an unprivileged user on the instance. A container agent also runs with a seccomp filter, masked `/proc` and `/sys` paths, and restricted device access. This is the default.

 `PRIVILEGED`   
Your agent runs with elevated privileges on its instance. On Linux, the agent runs as root. A code agent runs as user ID 0. A container agent runs with the same privileges as a container started with `docker run --privileged`. These privileges include all Linux capabilities, no seccomp filter, and access to all devices. Root inside the container is root on the instance.

If you omit `operatingSystemConfiguration` or `privilegeMode`, the agent runs in `STANDARD` mode. In both modes, each agent keeps its own network namespace.

Commands that you run in the session with `InvokeAgentRuntimeCommand` or `InvokeAgentRuntimeCommandShell` run with the same privileges as the agent. For more information, see [Shell execution](runtime-shell-execution.md).

## One agent per session
<a name="runtime-instances-privilege-mode-session-limit"></a>

A session that runs a privileged agent runs only that agent. A session gets its privilege mode from the first agent that runs in it, and keeps that mode for its whole lifetime. You can’t co-locate other agents with a privileged agent, even after the privileged agent stops. To run collaborating agents in one session, use `STANDARD` mode for all of them.

The privileged agent can keep using its own session. For example, you can resume the session with the same session ID after it stops.

AgentCore identifies an agent by the endpoint of its agent runtime. The following requests fail with a `ValidationException`. To run the agent, invoke it with a new session ID.


| Request | Error message | 
| --- | --- | 
| You invoke a `STANDARD` agent runtime with the session ID of a privileged agent’s session. |  `This session is a privileged session. Standard agents cannot run in it.`  | 
| You invoke a `PRIVILEGED` agent runtime with the session ID of a session that a `STANDARD` agent started. |  `This session was started in standard mode. A privileged agent must start in a new session.`  | 
| You invoke a `PRIVILEGED` agent runtime with the session ID of a session that a different privileged agent started. This includes the same agent runtime through a different endpoint. |  `This session is already used by a different privileged agent. A session can host only one privileged agent.`  | 

## Run containers in a privileged agent
<a name="runtime-instances-privilege-mode-containers"></a>

A privileged container agent can run its own container engine, such as containerd or Docker, to build container images and run containers. When your agent runs a container engine, consider the following:
+  **Storage for the container engine** – Store the container engine’s data on a volume, not on the agent container’s root file system. Container engines can’t store image layers on the root file system of a container. For example, mount a capacity provider volume at `/mnt/containers`, and set the data directory of the engine to a folder on that volume. For more information, see [Persistent storage across sessions](runtime-instances-how-it-works.md#runtime-instances-persistent-volumes).
+  **Resources** – The containers that your agent starts run inside the resource limits of the agent. Their memory counts toward the memory of the agent.

## Create an agent runtime with elevated privileges
<a name="runtime-instances-privilege-mode-create"></a>

Before you begin, you need the following:
+ A capacity provider. For more information, see [Get started with Instances](runtime-instances-getting-started.md).
+ Permission to call `bedrock-agentcore:CreateAgentRuntime`.

To create an agent runtime whose agents run with elevated privileges, complete the following steps:

1. Run `create-agent-runtime` with `linux.privilegeMode` set to `PRIVILEGED` in `operatingSystemConfiguration`. The following example uses the AWS CLI:

   ```bash
   aws bedrock-agentcore-control create-agent-runtime \
     --agent-runtime-name "my_privileged_agent" \
     --role-arn "arn:aws:iam::111122223333:role/AgentRuntimeRole" \
     --agent-runtime-artifact '{
       "containerConfiguration": {
         "containerUri": "111122223333.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
       }
     }' \
     --capacity-provider-configuration '{
       "capacityProviderArn": "arn:aws:bedrock-agentcore:us-west-2:111122223333:capacity-provider/my_capacity_provider-a1b2c3d4e5",
       "operatingSystemConfiguration": {
         "linux": {
           "privilegeMode": "PRIVILEGED"
         }
       }
     }' \
     --region us-west-2
   ```

   In the example, replace these values with your own:
   +  `my_privileged_agent` – The name of the agent runtime.
   +  `arn:aws:iam::111122223333:role/AgentRuntimeRole` – The ARN of the agent runtime execution role.
   +  `111122223333.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest` – The URI of your container image.
   +  `arn:aws:bedrock-agentcore:us-west-2:111122223333:capacity-provider/my_capacity_provider-a1b2c3d4e5` – The ARN of your capacity provider.

1. Call `get-agent-runtime` until the status of the agent runtime is `READY`.

   When the status is `READY`, the agents in your new sessions of the agent runtime run with elevated privileges.

If the request fails, check the error:
+  `ValidationException` – Specify `linux` in `operatingSystemConfiguration`, and set `privilegeMode` to `STANDARD` or `PRIVILEGED`.
+  `AccessDeniedException` – Grant your principal permission to call `bedrock-agentcore:CreateAgentRuntime`.

## Change the privilege mode
<a name="runtime-instances-privilege-mode-update"></a>

To change the privilege mode of an existing agent runtime, call `UpdateAgentRuntime` with the new `privilegeMode`. `UpdateAgentRuntime` replaces the stored capacity provider configuration. If you omit `operatingSystemConfiguration` from the update, the agent runtime returns to `STANDARD` mode. To keep the current privilege mode, include it in every update request.

A session keeps the privilege mode that it was created with. After you change the privilege mode, invoke the agent runtime with a new session ID. If you invoke a session that was created in the other mode, the request fails with a `ValidationException`. For the error messages, see [One agent per session](#runtime-instances-privilege-mode-session-limit).

## Check the privilege mode of an agent runtime
<a name="runtime-instances-privilege-mode-verify"></a>

 `GetAgentRuntime` returns the privilege mode in `capacityProviderConfiguration.operatingSystemConfiguration`. The following example returns only that field. In the example, replace `my_privileged_agent-a1b2c3d4e5` with the ID of your agent runtime:

```bash
aws bedrock-agentcore-control get-agent-runtime \
  --agent-runtime-id "my_privileged_agent-a1b2c3d4e5" \
  --query 'capacityProviderConfiguration.operatingSystemConfiguration' \
  --region us-west-2
```

The response contains the configuration that you set:

```json
{
    "linux": {
        "privilegeMode": "PRIVILEGED"
    }
}
```

If the response is empty, the agent runtime runs in `STANDARD` mode.