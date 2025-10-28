# EUCPERF08-BP04 Monitor

operating system metrics

Operating systems can add significant variations in performance to your Workload
depending on the compute, storage, and memory resources required. Test with all operating
systems that are intended to be supported by your deployment.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Monitor the performance of instances delivering end user services.

- Use operating system metrics such as Windows Performance Counters for detailed
  insight into instance performance.
- [Use
  the EUC Toolkit to manage Amazon AppStream 2.0 and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/").
- For ongoing monitoring and analysis, consider using the [Amazon Kinesis Agent for Windows](../../../kinesis-agent-windows/latest/userguide/what-is-kinesis-agent-windows.md "../../../kinesis-agent-windows/latest/userguide/what-is-kinesis-agent-windows.md") to monitor Windows Performance Counters for
  performance trend analysis of key system metrics.
