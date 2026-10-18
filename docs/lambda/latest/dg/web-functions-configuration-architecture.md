

# Instruction set architecture
<a name="web-functions-configuration-architecture"></a>

Web Functions run exclusively on the **Arm64** architecture, powered by AWS Graviton processors. Unlike Lambda Event Functions, you cannot choose the instruction set: there is no architecture setting to configure.

Each Web Function execution environment uses 2 Arm64 vCPUs. A per-Region quota limits the Arm64 vCPU capacity of your account. For the quota, see [Lambda Web Functions](gettingstarted-limits.md#web-functions-quotas). For the usage metrics that show your consumption against it, see [Regional usage and throttling metrics](web-functions-monitoring-metrics.md#web-functions-monitoring-metrics-usage).

Build native dependencies for Linux on arm64 (aarch64). Pure Node.js or JavaScript code needs no change. Any dependency with native binaries must provide a Linux arm64 build. Build the dependency on a Linux arm64 machine or in a Linux arm64 container, or cross-compile it for Linux arm64. For an example that installs dependencies in an Arm64 container, see [Test the deployment package](web-functions-testing.md#web-functions-testing-package).