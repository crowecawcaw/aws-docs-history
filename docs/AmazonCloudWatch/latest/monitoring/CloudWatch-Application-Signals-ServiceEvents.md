

# Monitor service events
<a name="CloudWatch-Application-Signals-ServiceEvents"></a>

Service Events provides automated deep observability for services monitored with CloudWatch Application Signals. It captures error metrics, function-level performance data, incident snapshots (when requests exceed latency thresholds or throw exceptions), and deployment events — without additional code changes.

## How service events works
<a name="Application-Signals-ServiceEvents-HowItWorks"></a>

Service Events collects the following types of signals from your instrumented services:
+ **Error metrics** — Per-exception-type error counts and rates for each operation, enabling you to identify which exceptions are most frequent and trending.
+ **Function-call metrics** — Invocation count, duration, and error rates for individual functions within your application code.
+ **Incident snapshots** — Detailed captures triggered when a request exceeds a latency threshold or throws an exception, including stack traces, call trees, caller details, and operation context.
+ **Deployment events** — Markers emitted at application startup and every 24 hours that correlate code deployments with changes in service behavior. The application emits deployment events automatically. Providing deployment metadata (git commit, deployment ID) enriches these events with additional context.

Service Events is automatically enabled when you enable CloudWatch Application Signals for your service. Error metrics and exception tracking are active immediately. Function-call metrics require additional configuration — you must configure packages to instrument before function-call data is collected (see [Enable function instrumentation](#Application-Signals-ServiceEvents-Configure-Function)). Service Events can be disabled by setting `OTEL_AWS_SERVICE_EVENTS_ENABLED=false`. Data flows from the ADOT SDK to the CloudWatch agent. The agent publishes events to CloudWatch Logs (`/aws/service-events/{{service-name}}` log groups) and CloudWatch Metrics.

Supported languages: Java, Python, and Node.js.

**Note**  
Service Events is automatically disabled in Lambda environments.

## Data storage
<a name="Application-Signals-ServiceEvents-DataStorage"></a>

Service Events stores data in CloudWatch Logs. CloudWatch publishes service event data to a log group with the prefix `/aws/application-signals/{{service-name}}`, where {{service-name}} is the value of your `OTEL_SERVICE_NAME` environment variable. One log group is created per service.

You are billed for log ingestion and storage at standard CloudWatch Logs rates.

## View errors in the console
<a name="Application-Signals-ServiceEvents-Errors"></a>

In the CloudWatch console, navigate to **Application Signals**, choose your service, and then choose the **Errors** tab. This tab shows exception metrics for your service.

The tab displays:
+ An exception count chart showing error trends over time. Use this to detect which exception types have changed in frequency recently.
+ A table listing each exception type, the operation where it occurred, the occurrence count, and the change compared to the previous period.

Select an exception to drill down into details including the stack trace, exception message, and a link to the associated trace.

Errors are grouped by operation, exception type, and top stack frames. Only the most recent representative of each group is shown.

**Note**  
To view error data, at least one `/aws/service-events/{{service-name}}` log group must exist in your account. If no log groups exist, the Errors tab displays an onboarding prompt.

## View service events in logs
<a name="Application-Signals-ServiceEvents-Logs"></a>

Service Events data is stored in CloudWatch Logs under log groups with the prefix `/aws/service-events/{{service-name}}`. You can query this data directly using CloudWatch Logs Insights to build custom views, create dashboards, or investigate specific incidents.

To query service events:

1. Open the CloudWatch console and navigate to **Logs Insights**.

1. Select the log group `/aws/service-events/{{service-name}}` for your service.

1. Enter a query to filter and analyze the service events data.

## Service events in the CloudWatch Application Signals MCP (Model Context Protocol) server
<a name="Application-Signals-ServiceEvents-MCP"></a>

Service events data is accessible through the CloudWatch Application Signals MCP (Model Context Protocol) server, enabling AI coding assistants and agents to query your service's runtime behavior directly.

**Troubleshooting**
+ Automatically correlate errors in your code with production incident snapshots, including full stack traces and affected endpoints.
+ Use incident context (exception types, call paths, trace IDs) to suggest targeted fixes without requiring you to manually navigate dashboards.
+ Retrieve deployment events to determine whether a recent release introduced a regression.

**Performance improvement**
+ Query function-level performance data to identify bottlenecks when investigating latency issues.
+ Compare function call durations across deployments to pinpoint performance regressions.

For setup and usage instructions, see the [Application Signals MCP server](https://awslabs.github.io/mcp/servers/cloudwatch-applicationsignals-mcp-server) on the GitHub website.

## Configure service events
<a name="Application-Signals-ServiceEvents-Configure"></a>

### Prerequisites
<a name="Application-Signals-ServiceEvents-Configure-Prerequisites"></a>

To use service events, make sure you have the minimum required versions of the following components:

1. **Update the ADOT SDK** — Update the AWS Distro for OpenTelemetry (ADOT) instrumentation SDK to the latest version for your language (Java, Python, or Node.js).

1. **Update the Amazon EKS add-on (if applicable)** — If you use the CloudWatch Observability Amazon EKS add-on to instrument your applications, update to the latest version of the add-on.

1. **Update the CloudWatch Agent** — Update to version `1.300069.0` or later of the CloudWatch agent.

If you use Amazon EKS, see [Enable your applications on Amazon EKS clusters](CloudWatch-Application-Signals-Enable-EKS.md) for add-on setup instructions.

### Features enabled by default
<a name="Application-Signals-ServiceEvents-Configure-Defaults"></a>

If you use CloudWatch Application Signals, the following service events signals are **enabled by default** with no additional configuration required:
+ Incident snapshots (triggered on exceptions and latency threshold breaches)
+ Error metrics (per-exception-type error counts per operation)
+ Deployment events (always emitted; enriched when you provide deployment metadata)
+ Function instrumentation (enabled by default, but produces no metrics until you configure packages to instrument)

The following features are **opt-in** and require setting environment variables to produce data:
+ Function-level metrics (requires configuring `OTEL_AWS_SERVICE_EVENTS_PACKAGES_INCLUDE`)
+ Custom endpoint filtering
+ Per-endpoint latency thresholds

### General settings
<a name="Application-Signals-ServiceEvents-Configure-General"></a>


| Environment variable | Default | Description | 
| --- | --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_ENABLED | Follows CloudWatch Application Signals | Toggle for Service Events. Service Events is automatically enabled when CloudWatch Application Signals is enabled. Set to false to explicitly disable. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_SAMPLING\_MODE | always | Controls function-call data sampling strategy. Values: always (record all function calls), auto (let the SDK decide based on load), never (disable function-call recording). Only applies when function instrumentation packages are configured. | 

### Enable function instrumentation
<a name="Application-Signals-ServiceEvents-Configure-Function"></a>

Function instrumentation is enabled by default, but it produces no metrics until you configure which packages to instrument. Provide a package allow list to start collecting per-function telemetry:


| Environment variable | Default | Description | 
| --- | --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_FUNCTION\_INSTRUMENT\_ENABLED | true | Enables or disables function-level instrumentation. Set to false to disable entirely. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_PACKAGES\_INCLUDE | None (required for metrics) | Comma-separated list of package prefixes to instrument. No wildcard needed. For example: Java uses com.myapp, Python uses myapp, Node.js uses src/myapp. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_PACKAGES\_EXCLUDE | None | Comma-separated list of sub-packages to exclude from instrumentation. Exclude always takes precedence over include. For example, include com.myapp and exclude com.myapp.models to instrument your application code but skip data model classes. | 

### Endpoint filtering
<a name="Application-Signals-ServiceEvents-Configure-Endpoint"></a>

Endpoint filtering controls which endpoints generate endpoint error metrics and incident snapshots. These settings do not affect function instrumentation.


| Environment variable | Default | Description | 
| --- | --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_ENDPOINT\_INCLUDE\_PATTERNS | All endpoints | Comma-separated glob patterns of endpoints to include. Matched against METHOD /route. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_ENDPOINT\_EXCLUDE\_PATTERNS | None | Comma-separated glob patterns of endpoints to exclude. Exclude takes precedence when an endpoint matches both. | 

### Latency thresholds
<a name="Application-Signals-ServiceEvents-Configure-Latency"></a>

Use the following environment variables to configure latency thresholds for incident snapshot triggers.


| Environment variable | Default | Description | 
| --- | --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_INCIDENT\_SNAPSHOT\_DURATION\_THRESHOLD\_MS | 5000 | Global latency threshold in milliseconds. Requests exceeding this duration trigger an incident snapshot. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_LATENCY\_THRESHOLDS | None | Per-endpoint latency thresholds that override the global default. Format: METHOD /route:ms (for example, GET /health:200,POST /checkout:8000). | 

### Rate limiting
<a name="Application-Signals-ServiceEvents-Configure-RateLimit"></a>

Use the following environment variables to control the rate at which service events data is collected and reported.


| Environment variable | Default | Description | 
| --- | --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_INCIDENT\_SNAPSHOT\_MAX\_PER\_MINUTE | 100 | Maximum number of incident snapshots captured per minute. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_INCIDENT\_SNAPSHOT\_MAX\_SAME\_ERROR | 1 | Maximum number of snapshots for the same error per capture window. | 

## Configure deployment events
<a name="Application-Signals-ServiceEvents-DeploymentEvents"></a>

Deployment events are always emitted at application startup and every 24 hours. Providing deployment metadata enriches these events so you can correlate incidents and performance changes with specific code deployments.

Set the following environment variables on your application containers or processes to provide deployment metadata:


| Environment variable | Description | 
| --- | --- | 
| OTEL\_AWS\_SERVICE\_EVENTS\_GIT\_COMMIT\_SHA | Git commit SHA of the deployed code. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_GIT\_REPO\_URL | URL of the Git repository. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_DEPLOYMENT\_ID | Unique identifier for the deployment (for example, a CI/CD pipeline run ID). | 
| OTEL\_AWS\_SERVICE\_EVENTS\_DEPLOYMENT\_TIMESTAMP | ISO 8601 timestamp of the deployment. | 
| OTEL\_AWS\_SERVICE\_EVENTS\_DEPLOYMENT\_URL | URL of the deployment build or pipeline run. | 

### Configure deployment events with GitHub Actions
<a name="Application-Signals-ServiceEvents-DeploymentEvents-GitHub"></a>

In your GitHub Actions workflow, use the built-in environment variables to populate deployment metadata. Add the following to your deployment step or container environment:

```
env:
  OTEL_AWS_SERVICE_EVENTS_GIT_COMMIT_SHA: ${{ github.sha }}
  OTEL_AWS_SERVICE_EVENTS_GIT_REPO_URL: ${{ github.server_url }}/${{ github.repository }}
  OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_ID: ${{ github.run_id }}
  OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_TIMESTAMP: $(date -u +%Y-%m-%dT%H:%M:%SZ)
  OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_URL: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

If you deploy container images, pass these values as environment variables in your task definition or pod spec. You can bake them into the image at build time or inject them at deploy time through your deployment configuration.

### Configure deployment events with GitLab CI/CD
<a name="Application-Signals-ServiceEvents-DeploymentEvents-GitLab"></a>

In your GitLab CI/CD pipeline, use the predefined CI/CD variables to populate deployment metadata. Add the following to your deployment job:

```
deploy:
  variables:
    OTEL_AWS_SERVICE_EVENTS_GIT_COMMIT_SHA: $CI_COMMIT_SHA
    OTEL_AWS_SERVICE_EVENTS_GIT_REPO_URL: $CI_PROJECT_URL
    OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_ID: $CI_PIPELINE_ID
    OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_TIMESTAMP: $(date -u +%Y-%m-%dT%H:%M:%SZ)
    OTEL_AWS_SERVICE_EVENTS_DEPLOYMENT_URL: $CI_PIPELINE_URL
```

Pass these variables to your application containers at deploy time through your container orchestration platform (for example, as environment variables in your Amazon ECS task definition or Kubernetes deployment manifest).