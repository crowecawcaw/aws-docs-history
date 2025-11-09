# Get started with Amazon Bedrock AgentCore

Build and deploy a production-ready AI agent in minutes with runtime hosting, memory, secure code
execution, and observability. This guide shows you how to use [AgentCore Runtime](agents-tools-runtime.md "agents-tools-runtime.md"), [Memory](memory.md "memory.md"), [Code Interpreter](code-interpreter-tool.md "code-interpreter-tool.md"), and [Observability](observability.md "observability.md") features.

###### Note

The agent is built using Strands SDK. Strands is a powerful SDK that takes a model-driven approach
to building and running AI agents. Learn more about [Strands](https://strandsagents.com/latest/ "https://strandsagents.com/latest/").

For AgentCore Gateway and Identity features, see the [Gateway quickstart](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/gateway/quickstart.md "https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/gateway/quickstart.md") and [Identity quickstart](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/identity/quickstart.md "https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/identity/quickstart.md").

###### Topics

- [Prerequisites](#agentcore-get-started-prerequisites "#agentcore-get-started-prerequisites")
- [Step 1: Create the agent](#agentcore-get-started-create-agent "#agentcore-get-started-create-agent")
- [Step 2: Configure and deploy the
  agent](#agentcore-get-started-configure-deploy "#agentcore-get-started-configure-deploy")
- [Step 3: Monitor the deployment](#agentcore-get-started-monitor-deployment "#agentcore-get-started-monitor-deployment")
- [Step 4: Test Memory and Code
  Interpreter](#agentcore-get-started-test-memory-code "#agentcore-get-started-test-memory-code")
- [Step 5: View traces and logs](#agentcore-get-started-view-traces-logs "#agentcore-get-started-view-traces-logs")
- [Clean up](#agentcore-get-started-clean-up "#agentcore-get-started-clean-up")
- [Troubleshooting](#agentcore-get-started-troubleshooting "#agentcore-get-started-troubleshooting")
- [Summary](#agentcore-get-started-summary "#agentcore-get-started-summary")

## Prerequisites

Before you start, make sure you have:

- **AWS permissions**. AWS root users or users with
  privileged roles (such as the **AdministratorAccess** role) can skip this
  step. Others will need to attach the [AmazonBedrockAgentCoreFullAccess](../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md "../../../aws-managed-policy/latest/reference/BedrockAgentCoreFullAccess.md") managed policy and the
  AgentCore starter toolkit policy described in [Use the starter toolkit](runtime-permissions.md#runtime-permissions-starter-toolkit "runtime-permissions.md#runtime-permissions-starter-toolkit").

###### Note

For this tutorial, you only need to add the AmazonBedrockAgentCoreFullAccess and
starter toolkit policies; there's no need to create an execution role as described in
[Execution role for running an agent in
AgentCore Runtime](runtime-permissions.md#runtime-permissions-execution "runtime-permissions.md#runtime-permissions-execution") because it will be created
automatically.

- **AWS CLI version 2.0 or later**. Configure the AWS CLI using
  `aws configure`. For more information, see the [AWS Command Line Interface User Guide for Version 2](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- **Python 3.10 or newer**
- **AgentCore starter toolkit**. For installation
  instructions, see the following section.

###### AWS Region consistency

Make sure you're using the _same AWS Region_ for:

- The default Region you selected when you ran `aws
configure`.
- The Region where you've enabled Amazon Bedrock model access.
  All resources created during the agent deployment will use this Region.

### Install the

AgentCore starter toolkit

Install the AgentCore starter toolkit:

```
# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install required packages (version 0.1.21 or later)
pip install "bedrock-agentcore-starter-toolkit>=0.1.21" strands-agents strands-agents-tools boto3
```

## Step 1: Create the agent

Create `agentcore_starter_strands.py`:

```
"""
Strands Agent sample with AgentCore
"""
import os
from strands import Agent
from strands_tools.code_interpreter import AgentCoreCodeInterpreter
from bedrock_agentcore.memory.integrations.strands.config import AgentCoreMemoryConfig, RetrievalConfig
from bedrock_agentcore.memory.integrations.strands.session_manager import AgentCoreMemorySessionManager
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

MEMORY_ID = os.getenv("BEDROCK_AGENTCORE_MEMORY_ID")
REGION = os.getenv("AWS_REGION")
MODEL_ID = "us.anthropic.claude-3-7-sonnet-20250219-v1:0"

@app.entrypoint
def invoke(payload, context):
    actor_id = "quickstart-user"

    # Get runtime session ID for isolation
    session_id = getattr(context, 'session_id', None)

    # Configure memory if available
    session_manager = None
    if MEMORY_ID:
        memory_config = AgentCoreMemoryConfig(
            memory_id=MEMORY_ID,
            session_id=session_id or 'default',
            actor_id=actor_id,
            retrieval_config={
                f"/users/{actor_id}/facts": RetrievalConfig(top_k=3, relevance_score=0.5),
                f"/users/{actor_id}/preferences": RetrievalConfig(top_k=3, relevance_score=0.5)
            }
        )
        session_manager = AgentCoreMemorySessionManager(memory_config, REGION)

    # Create Code Interpreter with runtime session binding
    code_interpreter = AgentCoreCodeInterpreter(
        region=REGION,
        session_name=session_id,
        auto_create=True
    )

    agent = Agent(
        model=MODEL_ID,
        session_manager=session_manager,
        system_prompt="""You are a helpful assistant with code execution capabilities. Use tools when appropriate.
Response format when using code:
1. Brief explanation of your approach
2. Code block showing the executed code
3. Results and analysis
""",
        tools=[code_interpreter.code_interpreter]
    )

    result = agent(payload.get("prompt", ""))
    return {"response": result.message.get('content', [{}])[0].get('text', str(result))}

if __name__ == "__main__":
    app.run()
```

Create `requirements.txt`:

```
strands-agents
bedrock-agentcore
strands-agents-tools
```

## Step 2: Configure and deploy the

agent

In this step, you'll use the AgentCore CLI to configure and deploy your agent.

### Configure the agent

Configure the agent with memory and execution settings:

**For this tutorial**: When prompted for the execution role,
press Enter to auto-create a new role with all required permissions for the Runtime, Memory,
Code Interpreter, and Observability features. When prompted for long-term memory, type
`yes`.

```
agentcore configure -e agentcore_starter_strands.py

#Interactive prompts you'll see:

# 1. Execution Role: Press Enter to auto-create or provide existing role ARN/name
# 2. ECR Repository: Press Enter to auto-create or provide existing ECR URI
# 3. Requirements File: Confirm the detected requirements.txt file or specify a different path
# 4. OAuth Configuration: Configure OAuth authorizer? (yes/no) - Type `no` for this tutorial
# 5. Request Header Allowlist: Configure request header allowlist? (yes/no) - Type `no` for this tutorial
# 6. Memory Configuration:
#    - If existing memories found: Choose from list or press Enter to create new
#    - If creating new: Enable long-term memory extraction? (yes/no) - Type `yes` for this tutorial
#    - Note: Short-term memory is always enabled by default
#    - Type `s` to skip memory setup
```

###### Note

If the memory configuration prompts do not appear during `agentcore
 configure`, refer to the [Troubleshooting](#agentcore-get-started-troubleshooting "#agentcore-get-started-troubleshooting") section (**Memory
configuration not appearing**) for instructions on how to check whether the
correct toolkit version is installed.

### Deploy to AgentCore

Launch your agent to the AgentCore runtime environment:

```
agentcore launch

# This performs:
#   1. Memory resource provisioning (STM + LTM strategies)
#   2. Docker container build with dependencies
#   3. ECR repository push
#   4. AgentCore Runtime deployment with X-Ray tracing enabled
#   5. CloudWatch Transaction Search configuration (automatic)
#   6. Endpoint activation with trace collection
```

Expected output:

During launch, you'll see the memory creation progress with elapsed time indicators. Memory
provisioning may take 2-5 minutes to activate:

```
Creating memory resource for agent: agentcore_starter_strands
⏳ Creating memory resource (this may take 30-180 seconds)...
Created memory: agentcore_starter_strands_mem-abc123
Waiting for memory agentcore_starter_strands_mem-abc123 to return to ACTIVE state...
⏳ Memory: CREATING (61s elapsed)
⏳ Memory: CREATING (92s elapsed)
⏳ Memory: CREATING (123s elapsed)
✅ Memory is ACTIVE (took 159s)
✅ Memory created and active: agentcore_starter_strands_mem-abc123
Observability is enabled, configuring Transaction Search...
✅ Transaction Search configured: resource_policy, trace_destination, indexing_rule
🔍 GenAI Observability Dashboard:
   https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#gen-ai-observability/agent-core
✅ Container deployed to Bedrock AgentCore
Agent ARN: arn:aws:bedrock-agentcore:us-west-2:123456789:runtime/starter_agent-xyz
```

If the deployment encounters errors or behaves unexpectedly, check your
configuration:

```
cat .bedrock_agentcore.yaml  # Review deployed configuration
agentcore status              # Verify resource provisioning status
```

## Step 3: Monitor the deployment

Check the agent's deployment status:

```
agentcore status

# Shows:
#   Memory ID: bedrock_agentcore_memory_ci_agent_memory-abc123
#   Memory Type: STM+LTM (3 strategies) (when active with strategies)
#   Memory Type: STM only (if configured without LTM)
#   Observability: Enabled
```

## Step 4: Test Memory and Code

Interpreter

In this section, you'll test your agent's memory capabilities and code execution
features.

### Test short-term memory

Test short-term memory within a single session:

```
# Store information (session IDs must be 33+ characters)
agentcore invoke '{"prompt": "Remember that my favorite agent platform is AgentCore"}'

# Retrieve within same session
agentcore invoke '{"prompt": "What is my favorite agent platform?"}'

# Expected response:
# "Your favorite agent platform is AgentCore."
```

### Test long-term memory – cross-session

persistence

Long-term memory (LTM) lets information persist across different sessions. This requires
waiting for long-term memory to be extracted before starting a new session.

Test long-term memory by starting a session:

```
# Session 1: Store facts
agentcore invoke '{"prompt": "My email is user@example.com and I am an AgentCore user"}'
```

After invoking the agent, AgentCore runs in the background to perform an extraction. Wait
for the extraction to finish. This typically takes 10-30 seconds. If you do not see any facts,
wait a few more seconds.

Start another session:

```
sleep 20
# Session 2: Different runtime session retrieves the facts extracted from initial session
SESSION_ID=$(python -c "import uuid; print(uuid.uuid4())")
agentcore invoke '{"prompt": "Tell me about myself?"}' --session-id $SESSION_ID

# Expected response:
# "Your email address is user@example.com."
# "You appear to be a user of AgentCore, which seems to be your favorite agent platform."
```

### Test Code Interpreter

Test AgentCore Code Interpreter:

```
# Store data
agentcore invoke '{"prompt": "My dataset has values: 23, 45, 67, 89, 12, 34, 56."}'

# Create visualization
agentcore invoke '{"prompt": "Create a text-based bar chart visualization showing the distribution of values in my dataset with proper labels"}'

# Expected: Agent generates matplotlib code to create a bar chart
```

## Step 5: View traces and logs

In this section, you'll use observability features to monitor your agent's performance.

### Access the Amazon CloudWatch dashboard

Navigate to the GenAI Observability dashboard to view end-to-end request traces including
agent execution tracking, memory retrieval operations, code interpreter executions, agent
reasoning steps, and latency breakdown by component. The dashboard provides a service map view
showing agent runtime connections to Memory and Code Interpreter services with request flow
visualization and latency metrics, as well as detailed X-Ray traces for debugging and
performance analysis.

```
# Get the dashboard URL from status
agentcore status

# Navigate to the URL shown, or go directly to:
# https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#gen-ai-observability/agent-core
# Note: Replace the Region
```

### View AgentCore Runtime logs

Access detailed AgentCore Runtime logs for debugging and monitoring:

```
# The correct log paths are shown in the invoke or status output
agentcore status

# You'll see log paths like:
# aws logs tail /aws/bedrock-agentcore/runtimes/AGENT_ID-DEFAULT --log-stream-name-prefix "YYYY/MM/DD/[runtime-logs]" --follow

# Copy this command from the output to view logs
# For example:
aws logs tail /aws/bedrock-agentcore/runtimes/AGENT_ID-DEFAULT --log-stream-name-prefix "YYYY/MM/DD/[runtime-logs]" --follow

# For recent logs, use the --since option as shown in the output:
aws logs tail /aws/bedrock-agentcore/runtimes/AGENT_ID-DEFAULT --log-stream-name-prefix "YYYY/MM/DD/[runtime-logs]" --since 1h
```

## Clean up

Remove all resources created during this tutorial:

```
agentcore destroy

# Removes:
#   - AgentCore Runtime endpoint and agent
#   - AgentCore Memory resources (short- and long-term memory)
#   - Amazon ECR repository and images
#   - IAM roles (if auto-created)
#   - CloudWatch log groups (optional)
```

## Troubleshooting

This section describes common issues and solutions when using the
AgentCore starter toolkit.

**Memory option not showing during `agentcore
 configure`**

This issue typically occurs when using an outdated version of the
AgentCore starter toolkit. Make sure you have version 0.1.21 or later installed:

```
# Step 1: Verify current state
which python   # Should show .venv/bin/python
which agentcore  # Currently showing global path

# Step 2: Deactivate and reactivate venv to reset PATH
deactivate
source .venv/bin/activate

# Step 3: Check if that fixed it
which agentcore
# If NOW showing .venv/bin/agentcore -> RESOLVED, skip to Step 7
# If STILL showing global path -> continue to Step 4

# Step 4: Force local venv to take precedence in PATH
export PATH="$(pwd)/.venv/bin:$PATH"

# Step 5: Check again
which agentcore
# If NOW showing .venv/bin/agentcore -> RESOLVED, skip to Step 7
# If STILL showing global path -> continue to Step 6

# Step 6: Reinstall in local venv with forced precedence
pip install --force-reinstall --no-cache-dir "bedrock-agentcore-starter-toolkit>=0.1.21"

# Step 7: Final verification
which agentcore  # Must show: /path/to/your-project/.venv/bin/agentcore
pip show bedrock-agentcore-starter-toolkit  # Verify version >= 0.1.21
agentcore --version  # Double check it's working

# Step 8: Try configure again
agentcore configure -e agentcore_starter_strands.py

#If Step 6 still doesn't work, the nuclear option:
cd ..
mkdir fresh-agentcore-project && cd fresh-agentcore-project
python3 -m venv .venv
source .venv/bin/activate
pip install --no-cache-dir "bedrock-agentcore-starter-toolkit>=0.1.21" strands-agents boto3
# Copy your agent code here, then reconfigure
```

**Additional checks**

- Make sure you're running `agentcore configure` from within the
  activated virtual environment.
- If you're using an IDE (VSCode, PyCharm), restart the IDE after
  reinstalling.
- Verify no system-wide agentcore installation conflicts: `pip list |
 grep bedrock-agentcore`.
  If you need to change your AWS Region configuration:

1. Clean up resources in the incorrect Region:

```
agentcore destroy

# This removes:
#   - AgentCore Runtime endpoint and agent
#   - AgentCore Memory resources (short- and long-term memory)
#   - Amazon ECR repository and images
#   - IAM roles (if auto-created)
#   - CloudWatch log groups (optional)
```

2. Verify your AWS CLI is configured for the correct Region:

```
aws configure get region
# Or reconfigure for the correct region:
aws configure set region `your-desired-region`
```

3. Make sure Amazon Bedrock model access is enabled in the target Region. To check, go to the
   AWS Management Console, choose the Amazon Bedrock service, and then choose **Model
   access**)
4. Copy your agent code and `requirements.txt` to the new
   folder, then return to [Step 2: Configure and deploy the
   agent](#agentcore-get-started-configure-deploy "#agentcore-get-started-configure-deploy") and complete the
   steps.
   **Cross-session memory not working**

- Verify that long-term memory is active (not "provisioning")
- Wait 15-30 seconds after storing facts for extraction
- Check extraction logs for completion
  **No traces appearing**

- Verify observability was enabled during `agentcore configure`
- Check IAM permissions include CloudWatch and X-Ray access
- Wait 30-60 seconds for traces to appear in CloudWatch
- Traces are viewable at: AWS Management Console → CloudWatch → Service Map or X-Ray → Traces
  **Missing memory logs**

- Check log group exists:
  `/aws/vendedlogs/bedrock-agentcore/memory/APPLICATION_LOGS/`memory-id``
- Verify that the IAM role has CloudWatch Logs permissions

## Summary

You've deployed a production agent with:

- **AgentCore Runtime** for managed container orchestration.
- **AgentCore Memory** with short-term memory for immediate context
  and long-term memory for cross-session persistence.
- **AgentCore Code Interpreter** for secure Python execution with
  data visualization capabilities.
- **AWS X-Ray Tracing** automatically configured for
  distributed tracing.
- **CloudWatch integration** for logs and metrics with Transaction
  Search enabled.

All services are automatically instrumented with X-Ray tracing, providing complete visibility
into agent behavior, memory operations, and tool executions through the CloudWatch dashboard.
