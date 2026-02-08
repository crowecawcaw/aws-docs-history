# MSFTPERF04-BP01 Use historical data to evaluate

performance

Effective assessment of Microsoft workload performance requires
comprehensive data collection across key system components: compute,
memory, storage, and networking. This approach aligns with the
Well-Architected Framework's Performance Excellence guidelines,
specifically the best practice PERF02-BP03, which focuses on
gathering compute-related metrics. By monitoring these critical
areas, organizations can identify suboptimal performance and
implement timely corrective measures. This holistic monitoring
strategy enables proactive management of Microsoft workloads,
ensuring they meet performance expectations and allowing for swift
intervention when performance falls below desired thresholds.

**Desired outcome:** Establish
comprehensive performance data collection and analysis capabilities
for Microsoft workloads that enable data-driven optimization
decisions, proactive issue identification, and continuous
performance improvement through historical trend analysis and
performance pattern recognition.

**Common anti-patterns:**

- Collecting performance data without systematic analysis or
  historical comparison, missing opportunities to identify
  performance trends and optimization opportunities over time.
- Monitoring only basic system metrics without collecting
  Microsoft-specific performance indicators, limiting visibility
  into application-level performance issues and optimization
  potential.
- Implementing reactive performance monitoring that only triggers
  during incidents, rather than proactive analysis that can
  prevent performance degradation before it impacts users.

**Benefits of establishing this best
practice:**

- Data-driven optimization decisions through comprehensive
  historical performance analysis that identifies trends,
  patterns, and optimization opportunities across Microsoft
  workload components.
- Proactive issue identification and prevention through continuous
  monitoring and analysis that can detect performance degradation
  before it impacts business operations.
- Improved capacity planning and resource allocation through
  historical data analysis that enables accurate forecasting of
  future performance and scaling requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing comprehensive performance data collection and
analysis requires establishing systematic monitoring across all
Microsoft workload components and creating processes for regular
performance evaluation and optimization.

### Implementation steps

1. Identify key performance metrics for Microsoft workload
   components including compute, memory, storage, and network
   performance indicators.
2. Configure comprehensive monitoring using Amazon CloudWatch,
   Performance Counters, and application-specific monitoring
   tools to collect historical performance data.
3. Establish data retention policies that maintain sufficient
   historical data for trend analysis and performance
   comparison over time.
4. Implement automated data analysis and reporting processes
   that regularly evaluate performance trends and identify
   optimization opportunities.
5. Create performance dashboards and visualization tools that
   enable easy analysis of historical performance data and
   trend identification.
6. Establish regular performance review processes that analyze
   historical data to identify patterns, anomalies, and
   optimization opportunities.
7. Document performance baselines and thresholds based on
   historical analysis to enable effective anomaly detection
   and alerting.
8. Integrate historical performance analysis into capacity
   planning and architectural decision-making processes for
   continuous improvement.

## Resources

**Related documents:**

- [Monitoring
  Windows services with Amazon CloudWatch](https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/ "https://aws.amazon.com/blogs/mt/monitoring-windows-services-with-amazon-cloudwatch-2/")
- [How
  do I use the CloudWatch agent on a Windows Server to view
  metrics for Performance Monitor?](https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows "https://repost.aws/knowledge-center/cloudwatch-performance-monitor-windows")
- [How
  to monitor Windows and Linux servers and get internal
  performance metrics](https://aws.amazon.com/blogs/compute/how-to-monitor-windows-and-linux-servers-and-get-internal-performance-metrics/ "https://aws.amazon.com/blogs/compute/how-to-monitor-windows-and-linux-servers-and-get-internal-performance-metrics/")
- [Run
  ADOTCollector on AWS Windows Ec2 Host](https://aws-otel.github.io/docs/setup/build-collector-on-windows "https://aws-otel.github.io/docs/setup/build-collector-on-windows")

**Related tools:**

- [Amazon CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md")
- [OpenTelemetry](https://opentelemetry.io/ "https://opentelemetry.io/")
