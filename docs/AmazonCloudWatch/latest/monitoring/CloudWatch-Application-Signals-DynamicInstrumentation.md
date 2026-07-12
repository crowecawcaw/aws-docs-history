# Debug applications with Dynamic Instrumentation

With Dynamic Instrumentation, you can capture runtime state from a live application
without restarting or redeploying. Runtime state includes variable values, method arguments,
return values, and stack traces. You define instrumentation configurations that specify where
in your code to capture data, and the running agent instruments the application at runtime.

## Concepts

Breakpoint
Temporary instrumentation that auto-expires. The default expiration is 24 hours,
configurable from 5 minutes to 24 hours. Use breakpoints for debugging and investigation.

Probe
Permanent instrumentation that persists until explicitly deleted. Use probes for
ongoing observability.

Snapshot
A point-in-time capture of program state including local variables, arguments,
return value, exceptions, and stack trace. Dynamic Instrumentation emits snapshots as
log records to CloudWatch Logs.

Location
The code location where instrumentation is applied. Required fields differ by
language.

## Supported languages

- Java
- Python
- JavaScript or TypeScript

## Prerequisites

To use Dynamic Instrumentation, update your instrumentation components to the latest
version based on your deployment type:

- **Amazon EKS customers** — Update the Amazon CloudWatch
  Observability EKS add-on to the latest version. The add-on includes the ADOT SDK
  and CloudWatch Agent. For more information, see
  [Install the CloudWatch Observability EKS add-on](install-CloudWatch-Observability-EKS-addon.md "install-CloudWatch-Observability-EKS-addon.md").
- **All other customers** — Update both of the
  following components:

  - The AWS Distro for OpenTelemetry (ADOT) instrumentation SDK
    for your language (Java, Python, or Node.js).
  - The CloudWatch Agent to the latest version.

The following conditions must also be met:

- CloudWatch Application Signals must be enabled for your application.
- Set the environment variable `OTEL_AWS_DYNAMIC_INSTRUMENTATION_ENABLED=true`
  on your application.
- Set the environment variable `OTEL_SERVICE_NAME` to your service name.
- Set the environment variable
  `OTEL_RESOURCE_ATTRIBUTES=deployment.environment.name=`my_deployment_env_name``.
  For existing Application Signals users, the value must match the Environment name for
  your service as it appears in the Application Signals console.
- The CloudWatch Agent must be running with the Application Signals configuration.
- Dynamic Instrumentation is not supported in Lambda environments.

## Add dynamic instrumentation to your application

After you instrument your application (see [Prerequisites](#Application-Signals-DI-Prerequisites "#Application-Signals-DI-Prerequisites")),
you create an instrumentation _configuration_ that specifies which part of your
code you want to introduce dynamic telemetry to. Each configuration defines two things:

1. **Where in the code to monitor** — The code location
   where the breakpoint or probe is applied.
2. **What data to capture** — The runtime state captured
   when the breakpoint or probe is executed.

###### Note

By default, Dynamic Instrumentation captures only limited data. To maximize the value
of this feature, consider expanding the capture configuration using the options described in
[Capture limits](#Application-Signals-DI-Limits "#Application-Signals-DI-Limits").

You can create configurations using the AWS CLI or SDK, or by using the Model Context
Protocol (MCP) server with an AI coding assistant in your IDE.

### Create configurations using the CLI or SDK

Use the AWS CLI or AWS SDK to create instrumentation configurations programmatically.

#### Specify the code location

The location defines where in your code the instrumentation is applied. The required fields
differ by language:

| Language                 | Required Fields                                             | Optional Fields                                                                                                                                                    |
| ------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Java                     | `CodeUnit` (package), `ClassName`, `MethodName`, `FilePath` | `LineNumber`                                                                                                                                                       |
| Python                   | `CodeUnit` (module), `MethodName`, `FilePath`               | `LineNumber`, `ClassName`                                                                                                                                          |
| JavaScript or TypeScript | `FilePath`, `LineNumber`                                    | None. Only line-level breakpoints are supported. Probes and function-level<br>breakpoints are not supported. TypeScript is supported when you provide source maps. |

#### Configure what data to capture

The capture configuration controls what runtime state is collected when the instrumentation
fires. Available options:

- `CaptureArguments` — List of method argument names to capture.
- `CaptureReturn` — Capture the return value (boolean).
- `CaptureStackTrace` — Capture the stack trace (boolean).
- `CaptureLocals` — List of local variable names to capture.
- `CaptureLimits` — Control capture depth and size (see
  [Capture limits](#Application-Signals-DI-Limits "#Application-Signals-DI-Limits")).

#### Configuration parameters

Key parameters when creating a configuration:

- `instrumentation-type` — `BREAKPOINT` or `PROBE`
- `service` — The service name as reported by Application Signals
- `environment` — The environment name
- `signal-type` — `SNAPSHOT`
- `location` — Code location fields (see above)
- `capture-configuration` — Capture options (see above)

#### Example

The following example creates a breakpoint on a Java method:

```
aws application-signals create-instrumentation-configuration \
    --instrumentation-type BREAKPOINT \
    --service "my-service" \
    --environment "production" \
    --signal-type SNAPSHOT \
    --location '{
        "CodeLocation": {
            "Language": "Java",
            "CodeUnit": "com.example.service",
            "ClassName": "OrderController",
            "MethodName": "processOrder",
            "FilePath": "OrderController.java"
        }
    }' \
    --capture-configuration '{
        "CodeCapture": {
            "CaptureArguments": ["orderId", "user"],
            "CaptureReturn": true,
            "CaptureStackTrace": true,
            "CaptureLimits": {
                "MaxHits": 100,
                "MaxStringLength": 255,
                "MaxCollectionWidth": 20,
                "MaxObjectDepth": 3,
                "MaxFieldsPerObject": 20,
                "MaxStackFrames": 20
            }
        }
    }'
```

### Create configurations using the MCP server

The recommended approach to using Dynamic Instrumentation is through the CloudWatch
Application Signals MCP (Model Context Protocol) server. The MCP enables AI coding
assistants and agents in your IDE to create, manage, and query Dynamic Instrumentation
configurations directly from your development environment.

Using the MCP, your AI assistant can:

- Create breakpoints and probes at specific code locations without
  leaving your editor.
- Query captured snapshots to inspect runtime variable values and
  call paths.
- Automatically correlate snapshot data with the code you are
  working on to suggest fixes.
- Manage the lifecycle of instrumentation configurations (view status,
  delete expired breakpoints).

For setup and usage instructions, see the
[Application Signals MCP server](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server "https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server")
on the GitHub website.

## Data storage

When a breakpoint or probe fires, Dynamic Instrumentation creates a log group in
CloudWatch Logs with the prefix
`/aws/application-signals/`service-name`` (where
`service-name` is the value of your
`OTEL_SERVICE_NAME` environment variable) and writes captured snapshots
as log records to that log group.

If the log group does not already exist, Dynamic Instrumentation creates it
automatically the first time a snapshot is emitted. You are billed for log ingestion
and storage at standard CloudWatch Logs rates.

## View and manage configurations

In the CloudWatch console, navigate to the service detail page and choose the
**Instrumentation** tab.

- Toggle between **Breakpoints** and
  **Probes** to view configurations by type.
- View configuration details including description, capture configuration, location,
  ARN, and expiration time.
- View status history to track transitions: Ready to Active to Error/Disabled.
- Delete configurations that are no longer needed.

## Understand status

Each instrumentation configuration has a status that indicates its current state.

| Status   | Description                                                           |
| -------- | --------------------------------------------------------------------- |
| READY    | The agent received the configuration.                                 |
| ACTIVE   | The agent applied the instrumentation to the running application.     |
| ERROR    | The instrumentation failed to apply. See the error cause for details. |
| DISABLED | The instrumentation expired, or you removed it.                       |

When an instrumentation enters the ERROR state, the following causes might be reported:

| Error Cause           | Description                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------- |
| FILE\_NOT\_FOUND      | The specified file path does not exist in the application.                                                     |
| METHOD\_NOT\_FOUND    | The specified method does not exist in the target class or module.                                             |
| LINE\_NOT\_EXECUTABLE | The specified line number does not correspond to an executable statement.                                      |
| OVERLOADED\_METHODS   | Multiple methods match the specified name. Provide additional location details to identify the correct method. |
| LANGUAGE\_MISMATCH    | The location fields do not match the language of the running application.                                      |
| RUNTIME\_ERROR        | An unexpected error occurred while applying the instrumentation.                                               |

## Capture limits

Capture limits control the size and depth of captured data. Configure these values in the
`capture-limits` field of the capture configuration.

| Limit              | Default | Range  | Description                                               |
| ------------------ | ------- | ------ | --------------------------------------------------------- |
| maxStringLength    | 255     | 1–255  | Maximum characters captured per string value.             |
| maxCollectionWidth | 20      | 1–20   | Maximum elements captured per collection or array.        |
| maxObjectDepth     | 3       | 1–5    | Maximum depth for nested object traversal.                |
| maxFieldsPerObject | 20      | 1–20   | Maximum fields captured per object.                       |
| maxStackFrames     | 20      | 1–20   | Maximum stack frames captured.                            |
| maxHits            | 100     | 1–1000 | Maximum captures before auto-disabling. Breakpoints only. |

Each instrumentation point is rate-limited to 5 captures per second.
