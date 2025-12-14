# GAMEPERF03-BP03 Optimize resource utilization of GameLift

containers

To optimize resource utilization of GameLift containers, design
your container fleet effectively and set precise resource limits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Key guidelines include:

- **Container group design:**
  Organize your software into container groups. The primary
  container should bundle your game server application and the
  Amazon GameLift Agent. Use sidecar containers for additional
  software to manage dependencies and set container-specific
  limits for memory and CPU usage.
- **Set resource limits:** For
  each container group, determine the required memory and CPU
  resources. Set optional limits for individual containers to
  verify they have reserved resources but can also exceed these
  limits if additional resources are available. This helps
  prevent resource contention and potential container failures.
- **Daemon container group:**
  Consider using a daemon container group for background or
  monitoring processes that do not need to scale with the
  primary container group. This verifies that essential
  background tasks are handled efficiently without impacting the
  primary game server processes.

### Implementation steps

- Design container groups with a primary container for the
  game server and GameLift Agent, and sidecars for managing
  dependencies, with specific memory and CPU limits.
- Set resource limits for each container group to reserve
  required resources while allowing controlled resource usage
  to avoid contention.
- Use a daemon container group for background or monitoring
  tasks, making sure they operate efficiently without
  affecting primary game server processes.
