# Best practices and

recommendations

## Service creation

management

- Keep onCreate operations lightweight to ensure a reasonable loading time
  for Agents
  - Use Promise timeouts for any external API calls during
    initialization to ensure fail-fast behavior

- Handle service errors gracefully
  - Any uncaught error encountered during service initialization will
    be considered as a service failure, which will prevent agents from
    accessing the workspace

## Authentication

- Prompt for Authentication during agent workspace startup with a third-party
  service
  - Begin authentication process without blocking service
    execution
  - Centralize authentication prompting in your service to avoid
    redundant implementations in your third-party applications

- Implement visual authentication interfaces (e.g., pop-ups) for agent
  interaction
- Set appropriate authentication timeouts to prevent infinite retry
  loops
- Ensure applications share the same origin as the third-party
  service

## Service

coordination

- Consolidate interdependent behaviors within a single service
  - For example, any applications launched on the startup of the
    agent workspace should be done by one service to ensure a consistent
    launch order for agents
