

# Collect telemetry from compiled applications using eBPF
<a name="CloudWatch-OTLP-NoCodeEbpf"></a>

You cannot instrument some applications by adding an OpenTelemetry SDK to the source. Examples include compiled binaries (such as Go, Rust, or C/C\+\+), third-party or vendor binaries whose source you do not own, and applications whose libraries an in-process agent cannot attach to. For these applications, you can use eBPF-based auto-instrumentation to generate OpenTelemetry telemetry without changing application code. You then send that telemetry to CloudWatch through the CloudWatch agent.

**Important**  
The CloudWatch agent is the OTLP receiver and exporter (the collection layer). It does not instrument your application. You pair the agent with a separate eBPF instrumentation tool that produces OTLP data. The open source OpenTelemetry project for this is [OpenTelemetry eBPF Instrumentation (OBI)](https://opentelemetry.io/docs/zero-code/obi/) on the OpenTelemetry website. eBPF attaches probes at the kernel, network, and TLS layers. As a result, it captures HTTP, HTTPS, and gRPC traffic and produces rate, errors, and duration (RED) metrics and trace spans without per-library code changes. For the languages, runtime versions, and libraries that OBI supports, see the OBI documentation. Coverage might vary by language and library, including which client and server spans it produces. Validate the specific frameworks your application uses before you rely on this approach.

## Understanding how it works
<a name="CloudWatch-OTLP-NoCodeEbpf-HowItWorks"></a>

The telemetry flows through the following pipeline.

1. eBPF auto-instrumentation generates telemetry without a code change and emits OTLP.

1. The CloudWatch agent, which is built on the OpenTelemetry Collector, receives the OTLP data. For more information, see [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md).

1. The agent forwards traces to AWS X-Ray (Transaction Search) and metrics to CloudWatch.

## Determining when to use this approach
<a name="CloudWatch-OTLP-NoCodeEbpf-WhenToUse"></a>

Consider this approach in the following cases:
+ You have compiled binaries that you cannot add an SDK to.
+ You have vendor or third-party code that you do not own.
+ You must keep an existing third-party monitoring agent in place.
+ You want RED metrics and traces without a code change or a redeploy of the application.

## Completing the prerequisites
<a name="CloudWatch-OTLP-NoCodeEbpf-Prerequisites"></a>

Before you begin, complete the following prerequisites:
+ Install CloudWatch agent version 1.300070.0 or later. Earlier versions do not support the agent's OTLP receiver. On Amazon EKS, use the CloudWatch Observability EKS add-on version 6.6.0 or later so that the agent Service exposes the OTLP ports.
+ Attach the `CloudWatchAgentServerPolicy` managed policy. The agent signs requests to the CloudWatch OTLP endpoints with its own credentials.
+ Enable Transaction Search so that spans reach the X-Ray OTLP endpoint. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md).
+ The eBPF instrumentation tool runs on Linux and requires a kernel with eBPF support and a set of Linux capabilities (such as `CAP_BPF`). The exact capabilities depend on the instrumentation tool and which features you enable, so grant the least privilege the tool documents rather than running it fully privileged. See the OBI documentation.
+ If the agent runs in a subnet without internet egress, make sure it can reach every endpoint it exports to. These endpoints are CloudWatch for metrics and X-Ray for traces (which Transaction Search uses). If you use the logs path, the agent must also reach CloudWatch Logs. In a private network, you typically provide this reachability with interface VPC endpoints (AWS PrivateLink). For the CloudWatch interface VPC endpoints, see [Using CloudWatch, CloudWatch Synthetics, and CloudWatch Network Monitoring with interface VPC endpoints](cloudwatch-and-interface-VPC.md). For the X-Ray VPC endpoint, see [Using X-Ray with interface VPC endpoints](https://docs.aws.amazon.com/xray/latest/devguide/xray-security-vpc-endpoint.html).

## Step 1: Configure the CloudWatch agent to receive OTLP data
<a name="CloudWatch-OTLP-NoCodeEbpf-Step1"></a>

Add an `opentelemetry` section to your CloudWatch agent configuration file and include the `otlp` source under `collect`. Bind the receiver to `127.0.0.1` so that the agent accepts OTLP only from the local host. In containerized deployments where producers run outside the agent's own container network—for example an Amazon ECS sidecar, or the Amazon EKS add-on's `cloudwatch-agent` Service—set the endpoints to `0.0.0.0` instead. The task, pod, or Service boundary then controls what can reach the ports.

```
{
  "opentelemetry": {
    "collect": {
      "otlp": {
        "grpc_endpoint": "127.0.0.1:4317",
        "http_endpoint": "127.0.0.1:4318"
      }
    }
  }
}
```

The agent forwards traces to X-Ray and metrics to CloudWatch automatically. For the full agent OTLP configuration, see [Amazon CloudWatch agent](CloudWatch-OTLPCloudWatchAgent.md).

**Run one OTLP receiver per host**  
Run a single OTLP receiver—the CloudWatch agent—for each host network namespace, and have every telemetry producer (your eBPF instrumentation and any OpenTelemetry SDKs) export to it. Only one process can bind the default OTLP ports (`4317` and `4318`) in a given network namespace, so a second collector that also uses the defaults fails to start. If you previously ran a separate OpenTelemetry or ADOT collector, remove it when you move collection to the agent. The eBPF instrumentation is a producer that exports OTLP, so it does not open the OTLP receiver ports. On Amazon EKS, each pod has its own network namespace, so this conflict occurs only when a pod uses host networking or a host port. If two receivers must coexist, the ports are configurable—set `grpc_endpoint` and `http_endpoint` to non-default values.

## Step 2: Point the eBPF instrumentation at the agent
<a name="CloudWatch-OTLP-NoCodeEbpf-Step2"></a>

Configure the eBPF tool's OTLP exporter to send to the local agent, using gRPC on port 4317 or HTTP on port 4318 (for example, `http://localhost:4318`). The following deployment notes apply:
+ **Amazon EC2**—Run the agent and the eBPF tool on the same instance, and export OTLP to `localhost`.
+ **Amazon EKS**—The CloudWatch Observability EKS add-on runs the agent and exposes ports 4317 and 4318 on the `cloudwatch-agent` Service. Run the eBPF instrumentation as a DaemonSet and point its exporter at that Service.

For the eBPF tool's own configuration, see the OBI documentation.

## Step 3: Verify your telemetry
<a name="CloudWatch-OTLP-NoCodeEbpf-Step3"></a>

Verify that your telemetry is arriving:
+ **Metrics**—Open the CloudWatch console, go to **Query Studio**, and run a PromQL query for your metric. OpenTelemetry metric names keep their dots in CloudWatch Query Studio, so query by the metric's OpenTelemetry name with the `__name__` matcher rather than a Prometheus-style normalized name—for example, `{__name__="http.server.request.duration"}` (the actual name depends on what your instrumentation emits).
+ **Traces and spans**—Use Transaction Search. For more information, see [Transaction Search](CloudWatch-Transaction-Search.md).

**Running alongside an existing monitoring agent**  
eBPF-based instrumentation runs out of process and does not inject into the application process. As a result, it can typically run alongside an existing in-process monitoring agent that does not instrument the same compiled runtime. Because eBPF tools require elevated privileges and some monitoring agents also use eBPF, validate resource usage and probe behavior in a test environment before you deploy to production.