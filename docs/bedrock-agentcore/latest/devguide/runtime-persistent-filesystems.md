# Persist session state across stop/resume with a filesystem configuration (Preview)

Agents built on Amazon Bedrock AgentCore Runtime maintain their local state during the compute lifecycle and by default, the compute associated with a session is ephemeral. Every session boots into a clean filesystem, and if the session is stopped or terminated, invoking the same session again will get a new compute and a clean filesystem. Modern agents don’t just chat — they write code, install packages, generate artifacts, and manage state through the filesystem.

AgentCore Runtime managed session storage changes this. Session storage is a fully service-managed capability where AgentCore Runtime handles all storage operations. Your agent reads and writes to a local filesystem mount and the runtime environment transparently replicates data to service storage throughout the session duration. Session storage is isolated per session — each session can only access its own storage and cannot read or write data from other sessions of the same agent runtime or sessions of different agent runtimes.

## How session storage works

When you configure session storage on an agent runtime, each session gets a persistent directory at the mount path you specify. The lifecycle works as follows:

1. **First invoke on a session** — A new isolated compute is provisioned. Your agent sees an empty directory at the mount path.
2. **Agent writes files** — All file operations (read, write, mkdir, rename) work as normal similar to a local filesystem and data is asynchronously replicated to durable storage.
3. **Session stops** — The compute is terminated. Any data not yet persisted is flushed to durable storage during graceful shutdown.
4. **Resume with same session** — A new compute is provisioned and the filesystem state is restored from durable storage. The agent can continue from where it left.

## Configure session storage

Add `filesystemConfigurations` with a `sessionStorage` entry when creating or updating an agent runtime.

###### Example

AWS CLI

1. ```
   aws bedrock-agentcore-control create-agent-runtime \
     --agent-runtime-name "coding-agent" \
     --role-arn "arn:aws:iam::111122223333:role/AgentExecutionRole" \
     --agent-runtime-artifact '{
       "containerConfiguration": {
         "containerUri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
       }
     }' \
     --filesystem-configurations '[{
       "sessionStorage": {
         "mountPath": "/mnt/workspace"
       }
     }]'
   ```

```



 AWS SDK

1. Python example using boto3 to create an AgentCore Runtime with session storage.



```

import boto3

client = boto3.client("bedrock-agentcore-control", region_name="us-west-2")

response = client.create_agent_runtime(
agentRuntimeName="coding-agent",
roleArn="arn:aws:iam::111122223333:role/AgentExecutionRole",
agentRuntimeArtifact={
"containerConfiguration": {
"containerUri": "123456789012.dkr.ecr.us-west-2.amazonaws.com/my-agent:latest"
}
},
filesystemConfigurations=[
{
"sessionStorage": {
"mountPath": "/mnt/workspace"
}
}
]
)

```



You can also add session storage to an existing agent runtime using [UpdateAgentRuntime](../../../bedrock-agentcore-control/latest/APIReference/API_UpdateAgentRuntime.md "../../../bedrock-agentcore-control/latest/APIReference/API_UpdateAgentRuntime.md") with the same `filesystemConfigurations` parameter.


## Invoke with session storage


Invoke the agent with a `runtimeSessionId` . Everything your agent writes to the configured mount path persists across stop/resume cycles.



**Example Using session storage across stop/resume cycles**




```

# First invocation — agent sets up the project

aws bedrock-agentcore invoke-agent-runtime \
 --agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-runtime/coding-agent" \
 --runtime-session-id "session-001" \
 --payload '{"prompt": "Set up the project and install dependencies in /mnt/workspace"}'

# Stop the session

aws bedrock-agentcore stop-runtime-session \
 --agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-runtime/coding-agent" \
 --runtime-session-id "session-001"

# Resume later — the project is exactly where the agent left it

aws bedrock-agentcore invoke-agent-runtime \
 --agent-runtime-arn "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-runtime/coding-agent" \
 --runtime-session-id "session-001" \
 --payload '{"prompt": "Run the tests and fix any failures"}'

```

The agent sees `/mnt/workspace` exactly as it left it. Source files, node\_modules, build artifacts, .git history — everything. No re-installing packages. No re-generating boilerplate. No warm-up before the agent can do useful work.


The session’s compute environment spun down hours ago. But the filesystem was already persisted. When you resume, a new compute environment mounts the same storage, and your agent picks up mid-thought.


###### Note

When explicitly calling `StopRuntimeSession` always wait for it to complete before resuming the session. This ensures all data is flushed to durable storage.


###### Note

The mounted path is available only at the time of agent invocation, not during initialization.


## Filesystem semantics


Session storage provides a standard Linux filesystem at your configured mount path. Standard tools and operations work without modification — `ls` , `cat` , `mkdir` , `git` , `npm` , `pip` , and `cargo` all work as expected.



**Supported operations**



Regular files, directories, and symlinks. Read, write, rename, delete, `chmod` , `chown` , `stat` , and `readdir` — standard POSIX file operations used by common development tools.



**Limits**



For session storage limits including maximum storage size, file count, and directory depth, see [Session storage limits](bedrock-agentcore-limits.md#session-storage-limits "bedrock-agentcore-limits.md#session-storage-limits").



**Unsupported operations**



The following filesystem operations are not supported:



* **Hard links** — Use symlinks instead.
* **Device files, FIFOs, or UNIX sockets** — `mknod` is not supported.
* **Extended attributes (xattr)** — Tools that depend on xattr metadata are not supported.
* **fallocate** — Sparse file preallocation is not supported.
* **File locking across sessions** — Advisory locks work within a running session but are not persisted across stop/resume. Tools that use file-based locking (such as `git` ) are unaffected.

###### Note

Permissions are stored but not enforced within the session. `chmod` and `stat` work correctly, but access checks always succeed because the agent runs as the only user in the microVM.


## Session storage lifecycle


Session data is deleted (reset to a clean state) in the following scenarios:



* The session is not invoked for **14 days.**
* The agent runtime version is updated. Invoking a session after a version update provisions a fresh filesystem.

Use [DeleteAgentRuntime](../../../bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntime.md "../../../bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntime.md") or [DeleteAgentRuntimeEndpoint](../../../bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntimeEndpoint.md "../../../bedrock-agentcore-control/latest/APIReference/API_DeleteAgentRuntimeEndpoint.md") to delete all session storage data associated with the runtime or endpoint.


## Use cases



* **Durable filesystem scratch space** — Agents write intermediate files, downloaded assets, and work-in-progress artifacts to a scratch directory that persists across session stop/resume cycles, eliminating the need to recreate temporary files after each restart.
* **Code generation and iteration** — Your agent scaffolds a project, installs dependencies, writes code, and runs tests across multiple sessions. Stop overnight, resume the next morning with the entire project directory intact.
* **Long-running analysis with checkpoints** — Process large datasets over multiple sessions. Intermediate results, temporary files, and partial outputs persist between invocations without custom checkpoint logic.

## Example: Coding agent with persistent workspace


This example shows a coding agent using Strands Agents with `FileSessionManager` for conversation history and session storage for project files. Both persist across stop/resume cycles.



**Coding agent with session storage**




```

import os

# Enable non-interactive mode for strands tools

os.environ["BYPASS_TOOL_CONSENT"] = "true"

from strands import Agent
from strands.session import FileSessionManager
from strands.models import BedrockModel
from strands_tools import file_read, file_write, shell
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()
WORKSPACE = "/mnt/workspace"

model = BedrockModel(model_id="us.anthropic.claude-sonnet-4-20250514-v1:0")
tools = [file_read, file_write, shell]

@app.entrypoint
def handle_request(payload):
session_id = payload.get("session_id", "default")

    # Persist conversation history alongside project files
    session_manager = FileSessionManager(
        session_id=session_id,
        storage_dir=f"{WORKSPACE}/.sessions"
    )

    agent = Agent(
        model=model,
        tools=tools,
        session_manager=session_manager,
        system_prompt="You are a coding assistant. Project files are in /mnt/workspace."
    )

    response = agent(payload.get("prompt"))
    return {"response": response.message["content"][0]["text"]}

if **name** == "**main**":
app.run()

```


**requirements.txt**




```

strands-agents
strands-agents-tools
bedrock-agentcore
boto3

```

Invoke the agent, stop the session, then resume. Both project files and conversation context persist.



**Invoke, stop, and resume cycle**




```

import boto3, json

client = boto3.client("bedrock-agentcore")
agent_arn = "arn:aws:bedrock-agentcore:us-west-2:111122223333:agent-runtime/coding-agent"
session_id = "project-xyz-001"

def invoke(prompt):
resp = client.invoke_agent_runtime(
agentRuntimeArn=agent_arn,
runtimeSessionId=session_id,
payload=json.dumps({"prompt": prompt, "session_id": "conv-001"}).encode()
)
return json.loads(b"".join(resp["response"]))["response"]

# First invoke: Create a simple script

invoke("Write a Python script called calculator.py with add and subtract functions.")

# Stop session — compute terminates, storage persists

client.stop_runtime_session(agentRuntimeArn=agent_arn, runtimeSessionId=session_id)

# Resume same session — new compute, but files and conversation history restored

invoke("Add a multiply function to the script you created.")

# Agent knows it created calculator.py (conversation history)

# AND finds existing file (file persistence)

```

The `FileSessionManager` stores conversation history to `/mnt/workspace/.sessions/` , enabling the agent to remember context across stop/resume cycles.


## Networking requirements


If your agent runtime uses VPC mode with session storage, the agent will need network access to sync with remote storage. Session data is stored in AgentCore S3, so your VPC must allow outbound connectivity to S3. If you are using an S3 Gateway endpoint with a custom policy, you can scope access to your regional session storage bucket as follows:



```

"Action": [
"s3:GetObject",
"s3:PutObject",
"s3:ListBucket"
],
"Resource": [
"arn:aws:s3:::acr-storage-*-region-an",
"arn:aws:s3:::acr-storage-*-region-an/*"
],
"Condition": {
"StringEquals": {
"aws:PrincipalServiceName": "bedrock-agentcore.amazonaws.com"
}
}

```

Replace `region` with your AWS Region (for example, `us-west-2` ).
```
