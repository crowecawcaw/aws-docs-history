# Use isolated sessions for agents

Amazon Bedrock AgentCore Runtime lets you isolate each user session and safely reuse context across
multiple invocations in a user session. Session isolation is critical for AI agent workloads
due to their unique operational characteristics:

- **Complete execution environment separation**: Each
  user session in AgentCore Runtime receives its own dedicated microVM with isolated Compute,
  memory, and filesystem resources. This prevents one user's agent from accessing
  another user's data. After session completion, the entire microVM is terminated and
  memory is sanitized to remove all session data, eliminating cross-session
  contamination risks.
- **Stateful reasoning processes**: Unlike stateless
  functions, AI agents maintain complex contextual state throughout their execution
  cycle, beyond simple message history for multi-turn conversations. AgentCore Runtime preserves
  this state securely within a session while ensuring complete isolation between
  different users, enabling personalized agent experiences without compromising data
  boundaries.
- **Privileged tool operations**: AI agents perform
  privileged operations on users' behalf through integrated tools accessing various
  resources. AgentCore Runtime's isolation model ensures these tool operations maintain proper
  security contexts and prevents credential sharing or permission escalation between
  different user sessions.
- **Deterministic security for non-deterministic
  processes**: AI agent behavior can be non-deterministic due to the
  probabilistic nature of foundation models. AgentCore Runtime provides consistent,
  deterministic isolation boundaries regardless of agent execution patterns,
  delivering the predictable security properties required for enterprise
  deployments.

###### Note

AgentCore does not enforce session-to-user mappings - your client backend should
maintain the relationship between users and their session IDs.
Additionally, your client backend should implement logic for user to session
lifecycle management like maximum number of sessions per user.

## Understanding ephemeral context

While AgentCore provides strong session isolation, these sessions are
ephemeral in nature. Any data stored in memory or written to disk persists only for the
session duration. This includes conversation history, user preferences, intermediate
calculation results, and any other state information your agent maintains.

For data that needs to be retained beyond the session lifetime (such as user
conversation history, learned preferences, or important insights), you should use
AgentCore Memory. This service provides purpose-built persistent storage designed
specifically for agent workloads, with both short-term and long-term memory
capabilities.

## Extended conversations and multi-step

workflows

Unlike traditional serverless functions that terminate after each request,
AgentCore supports ephemeral, isolated compute sessions lasting up to 8 hours.
This simplifies building multi-step agentic workflows as you can make multiple calls to
the same environment, with each invocation building upon the context established by
previous interactions.

## AgentCore Runtime session lifecycle

###### Session creation

A new session is created on the first invoke with a unique runtimeSessionId
provided by your application. AgentCore Runtime provisions a dedicated
execution environment (microVM) for each session. Context is preserved between
invocations to the same session.

###### Session states

Sessions can be in one of the following states:

- **Active**: Either processing a sync request or
  doing background tasks. Sync invocation activity is automatically tracked based
  on invocations to a runtime session. Background tasks are communicated by the
  agent code by responding with "HealthyBusy" status in pings.
- **Idle**: When not processing any requests or
  background tasks. The session has completed processing but remains available for
  future invocations.
- **Terminated**: Execution environment provisioned
  for the session is terminated. This can be due to inactivity (of 15 minutes),
  reaching max duration (8 hours) or if it's deemed unhealthy based on health
  checks. Subsequent invokes to a terminated runtimeSessionId will provision a new
  execution environment.

## How to use sessions

To use sessions effectively:

- Generate a unique session ID for each user or conversation with at least 33 characters
- Pass the same session ID for all related invocations
- Use different session IDs for different users or conversations

###### Example Using sessions for a conversation

```

# First message in a conversation

response1 = agent_core_client.InvokeAgentRuntime(
   agentRuntimeArn=agent_arn,
   runtimeSessionId="user-123456-conversation-12345678", # or uuid.uuid4()
   payload=json.dumps({"prompt": "Tell me about AWS"}).encode()
)

# Follow-up message in the same conversation reuses the runtimeSessionId.

response2 = agent_core_client.InvokeAgentRuntime(
   agentRuntimeArn=agent_arn,
   runtimeSessionId="user-123456-conversation-12345678", # or uuid.uuid4()
   payload=json.dumps({"prompt": "How does it compare to other cloud providers"}).encode()
)

```

By using the same runtimeSessionId for related invocations, you ensure that context is
maintained across the conversation, allowing your agent to provide coherent responses
that build on previous interactions.
