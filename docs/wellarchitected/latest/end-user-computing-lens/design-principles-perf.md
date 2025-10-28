# Design principles

- **Minimize latency**: EUC workloads are sensitive to latency.
  For best performance, minimize the latency between end users and EUC services, as well as
  between EUC instances and dependencies.
- **Monitor performance metrics**: Use performance metrics to
  understand the behavior of both individual instances and the holistic health of your EUC
  environment. Adjust configurations to meet evolving performance requirements.
- **Consider mechanical sympathy**: Understand the design goals of
  AWS EUC services and features and align them with your workload goals. For further
  information related to mechanical sympathy, see [Consider Mechanical Sympathy](../framework/perf-dp.md "../framework/perf-dp.md").
