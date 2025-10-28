# Handle asynchronous and long running agents with

Amazon Bedrock AgentCore Runtime

Amazon Bedrock AgentCore Runtime can handle asynchronous processing and long running agents.
Asynchronous tasks allow your agent to continue processing after responding
to the client and handle long-running operations without blocking responses. With async
processing, your agent can:

- Start a task that might take minutes or hours
- Immediately respond to the user saying "I've started working on this"
- Continue processing in the background
- Allow the user to check back later for results

## Key concepts

### Asynchronous processing model

The Amazon Bedrock AgentCore SDK supports both synchronous and asynchronous processing
through a unified API. This creates a flexible implementation pattern for both
clients and agent developers. Agent clients can work with the same API without
differentiating between synchronous and asynchronous on the client side. With the ability to
invoke the same session across invocations, agent developers can reuse context and
build upon this context incrementally without implementing complex task management
logic.

### Runtime session lifecycle

management

Agent code communicates its processing status using the "/ping" health status.
"HealthyBusy" indicates the agent is busy processing background tasks, while
"Healthy" indicates it is idle (waiting for requests). A session in idle state for
15 minutes gets automatically terminated.

## Implementing asynchronous tasks

To get started, install the `bedrock-agentcore` package:

```
pip install bedrock-agentcore
```

### API based task management

To build interactive agents that perform asynchronous tasks, you need to call
`add_async_task` when starting a task and
`complete_async_task` when the task completes. The SDK handles task
tracking and manages Ping status automatically.

```
# Start tracking a task manually
task_id = app.add_async_task("data_processing")

# Do work...

# Mark task as complete
app.complete_async_task(task_id)
```

### Asynchronous task decorator

The Amazon Bedrock AgentCore SDK helps with tracking asynchronous tasks. You can get started by
simply annotating your asynchronous functions with `@app.async_task`.

```
# Automatically track asynchronous functions:
@app.async_task
async def background_work():
    await asyncio.sleep(10)  # Status becomes "HealthyBusy"
    return "done"

@app.entrypoint
async def handler(event):
    asyncio.create_task(background_work())
    return {"status": "started"}
```

Here is how it works:

- The `@app.async_task` decorator tracks function
  execution
- When the function runs, ping status changes to "HealthyBusy"
- When the function completes, status returns to "Healthy"

### Custom ping handler

You can implement your own custom ping handler to manage the Runtime Session's
state. Your agent's health is reported through the /ping endpoint:

```
@app.ping
def custom_status():
    if system_busy():
        return PingStatus.HEALTHY_BUSY
    return PingStatus.HEALTHY
```

Status values:

- "Healthy": Ready for new work
- "HealthyBusy": Processing background task

## Complete example

First, install the required package:

```
pip install strands-agents
```

Then, create a Python file with the following code:

```
import threading
import time
from strands import Agent, tool
from bedrock_agentcore.runtime import BedrockAgentCoreApp

# Initialize app with debug mode for task management
app = BedrockAgentCoreApp()

@tool
def start_background_task(duration: int = 5) -> str:
    """Start a simple background task that runs for specified duration."""
    # Start tracking the async task
    task_id = app.add_async_task("background_processing", {"duration": duration})

    # Run task in background thread
    def background_work():
        time.sleep(duration)  # Simulate work
        app.complete_async_task(task_id)  # Mark as complete

    threading.Thread(target=background_work, daemon=True).start()
    return f"Started background task (ID: {task_id}) for {duration} seconds. Agent status is now BUSY."

# Create agent with the tool
agent = Agent(tools=[start_background_task])

@app.entrypoint
def main(payload):
    """Main entrypoint - handles user messages."""
    user_message = payload.get("prompt", "Try: start_background_task(3)")
    return {"message": agent(user_message).message}

if __name__ == "__main__":
    print("🚀 Simple Async Strands Example")
    print("Test: curl -X POST http://localhost:8080/invocations -H 'Content-Type: application/json' -d '{\"prompt\": \"start a 3 second task\"}'")
    app.run()
```

This example demonstrates:

- Creating a background task that runs asynchronously
- Tracking the task's status with `add_async_task` and
  `complete_async_task`
- Responding immediately to the user while processing continues
- Managing the agent's health status automatically
