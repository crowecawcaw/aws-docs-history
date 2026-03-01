# Building third-party services in the Amazon Connect Agent Workspace

## What is a third-party (3P) service?

third-party (3P) services are headless applications that customers can build and
integrate into Amazon Connect agent workspace. Services begin running when the
agent workspace loads and remain active throughout the agent workspace session. They can perform
various background tasks and enhance the agent experience, such as:

- Listening to contact events: Services can monitor events like contact
  connection, disconnection, or entering After Contact Work (ACW) state.
- Launching applications: Services can automatically open specific applications
  based on certain triggers or conditions.
- Implementing custom authentication flows: Services can ensure users complete
  necessary authentication processes for third-party applications as soon as the
  agent workspace starts.

## Why use a third-party service?

third-party services allow you to implement background processes and automate tasks
throughout the agent workspace session. They provide powerful capabilities for
establishing contact event listeners, enabling custom authentication flows, and managing
other agent workspace-wide functionality.

## Common use cases for 3P services

These are common use cases for third-party services:

- Automatically launch specific applications when an agent enters After Contact
  Work (ACW).
- Ensure critical applications are always running by automatically launching
  them during agent workspace startup.
- Control application visibility by automatically bringing specific apps into
  focus based on contact events or other triggers.
- Implement custom contact handling logic to determine what happens when agents
  accept or leave contacts.
- Manage authentication flows that need to run when the agent workspace loads.

## Understanding when to use each option

### When to use a third-party application

Choose a third-party application when you need:

- Features that can be opened and closed during the agent's workflow
- Functionality that needs to be visible and directly interactive for the
  agent

### When to use a third-party service

Choose a third-party service when you need:

- To implement agent workspace-wide event listeners and handlers
- Automatic background processes that should run throughout the agent workspace
  session
- To automate tasks that don't require direct agent interaction
- To control the behavior and state of other applications in the
  agent workspace
