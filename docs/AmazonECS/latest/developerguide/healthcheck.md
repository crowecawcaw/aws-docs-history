# Determine Amazon ECS task health using container health

checks

When you create a task definition, you can configure a health check for your containers.
Health checks are commands that run locally on a container and validate application health
and availability.

The Amazon ECS container agent only monitors and reports on the health checks that are
specified in the task definition. Amazon ECS doesn't monitor Docker health checks that are
embedded in a container image but aren't specified in the container definition. Health check
parameters that are specified in a container definition override any Docker health checks
that exist in the container image.

When a health check is defined in a task definition, the container runs the health check
process inside the container, and then evaluate the exit code to determine the application
health.

The health check consists the following parameters:

- Command – The command that the container runs to determine if it's healthy.
  The string array can start with `CMD` to run the command arguments
  directly, or `CMD-SHELL` to run the command with the container's default
  shell. Use `CMD-SHELL` when you need shell features like pipes,
  redirects, command chaining, or environment variable expansion. For example,
  `CMD-SHELL` allows you to use commands like
  `curl -f http://localhost/ || exit 1` where the shell interprets
  the `||` operator. Use `CMD` for simple commands that
  don't require shell interpretation.
- Interval – The period of time (in seconds) between each health check.
- Timeout – The period of time (in seconds) to wait for a health check to
  succeed before it's considered a failure.
- Retries – The number of times to retry a failed health check before the
  container is considered unhealthy.
- Start period – The optional grace period to provide containers time to
  bootstrap in before failed health checks count towards the maximum number of
  retries.

If a health check succeeds within the `startPeriod`, then the container is considered healthy and any subsequent failures count toward the maximum number of retries.
For information about how to specify a health check in a task definition, see [Health check](task_definition_parameters.md#container_definition_healthcheck "task_definition_parameters.md#container_definition_healthcheck").

The following describes the possible health status values for a container:

- `HEALTHY`–The container health check has passed
  successfully.
- `UNHEALTHY`–The container health check has failed.
- `UNKNOWN`–The container health check is being evaluated, there's
  no container health check defined, or Amazon ECS doesn't have the health status of the
  container.
  The health check commands run on the container. Therefore you must include the commands in
  the container image.

The health check connects to the application through the container's loopback interface at
`localhost` or `127.0.0.1`. An exit code of `0`
indicates success, and non-zero exit code indicates failure.

Consider the following when using container health checks:

- Container health checks require version 1.17.0 or greater of the Amazon ECS container
  agent.
- Container health checks are supported for Fargate tasks if you're
  using Linux platform version `1.1.0` or greater or Windows platform
  version `1.1.0` or greater

## How Amazon ECS determines task health

Containers that are essential and have health check command in the task definition are
the only ones considered to determine the task health.

The following rules are evaluated in order:

1. If the status of one essential container is `UNHEALTHY`, then the
   task status is `UNHEALTHY`.
2. If the status of one essential container is `UNKNOWN`, then the task
   status is `UNKNOWN`.
3. If the status of all essential containers are `HEALTHY`, then the
   task status is `HEALTHY`.

Consider the following task health example with 2 essential containers.

| Container 1 health | Container 2 health | Task health |
| ------------------ | ------------------ | ----------- |
| `UNHEALTHY`        | `UNKNOWN`          | `UNHEALTHY` |
| `UNHEALTHY`        | `HEALTHY`          | `UNHEALTHY` |
| `HEALTHY`          | `UNKNOWN`          | `UNKNOWN`   |
| `HEALTHY`          | `HEALTHY`          | `HEALTHY`   |

Consider the following task health example with 3 containers.

| Container 1 health | Container 2 health | Container 3 health | Task health |
| ------------------ | ------------------ | ------------------ | ----------- |
| `UNHEALTHY`        | `UNKNOWN`          | `UNKNOWN`          | `UNHEALTHY` |
| `UNHEALTHY`        | `UNKNOWN`          | `HEALTHY`          | `UNHEALTHY` |
| `UNHEALTHY`        | `HEALTHY`          | `HEALTHY`          | `UNHEALTHY` |
| `HEALTHY`          | `UNKNOWN`          | `HEALTHY`          | `UNKNOWN`   |
| `HEALTHY`          | `UNKNOWN`          | `UNKNOWN`          | `UNKNOWN`   |
| `HEALTHY`          | `HEALTHY`          | `HEALTHY`          | `HEALTHY`   |

## How health checks are affected by agent

disconnects

If the Amazon ECS container agent becomes disconnected from the Amazon ECS service, this won't
cause a container to transition to an `UNHEALTHY` status. This is by design,
to ensure that containers remain running during agent restarts or temporary
unavailability. The health check status is the "last heard from" response from the Amazon ECS
agent, so if the container was considered `HEALTHY` prior to the disconnect,
that status will remain until the agent reconnects and another health check occurs.
There are no assumptions made about the status of the container health checks.
