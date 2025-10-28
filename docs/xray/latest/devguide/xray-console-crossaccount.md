# Cross-account tracing

AWS X-Ray supports _cross-account observability_, enabling you to monitor and troubleshoot
applications that span multiple accounts within an AWS Region. You can seamlessly search, visualize, and analyze
your metrics, logs, and traces in any of the linked accounts as if you were operating in a single account. This
provides a complete view of requests that travel across multiple accounts. You can view cross-account traces in the
X-Ray trace map and traces pages within the [CloudWatch
console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").

The shared observability
data can include any of the following types of telemetry:

- Metrics in Amazon CloudWatch
- Log groups in Amazon CloudWatch Logs
- Traces in AWS X-Ray
- Applications in Amazon CloudWatch Application Insights

## Configure cross-account observability

To turn on cross-account observability, set up one or more AWS _monitoring_ accounts and
link them with multiple _source_ accounts. A monitoring account is a central AWS account that
can view and interact with observability data that's generated from source accounts. A source account is an
individual AWS account that generates observability data for the resources that it contains.

Source accounts share their observability data with monitoring accounts. Traces are copied from each source
account to up to five monitoring accounts. Copies of traces from source accounts to the first monitoring account
are free. Copies of traces sent to additional monitoring accounts are charged to each source account, based on
standard pricing. For more information, see [AWS X-Ray pricing](https://aws.amazon.com/xray/pricing/ "https://aws.amazon.com/xray/pricing/")
and [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

To create links between monitoring accounts and source accounts, use the CloudWatch console or the new Observability
Access Manager commands in the AWS CLI and API. For more information, see [CloudWatch cross-account observability](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.md").

###### Note

X-Ray traces are billed to the AWS account where they're received. If a [sampled](xray-concepts.md#xray-concepts-sampling "xray-concepts.md#xray-concepts-sampling") request spans services across more than one AWS account,
each account records a separate trace, and all traces share the same trace ID. To learn more about cross-account
observability pricing, see [AWS X-Ray pricing](https://aws.amazon.com/xray/pricing/ "https://aws.amazon.com/xray/pricing/") and [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Viewing cross-account traces

Cross-account traces are displayed in the monitoring account. Each source account displays only local traces
for that specific account. The following sections assume that you're signed in to the monitoring account and have
opened the Amazon CloudWatch console. On both the trace map and traces pages, a monitoring account badge is displayed in
the upper-right corner.

![Monitoring account badge](images/crossaccount-monitoring-account.png)

### Trace map

In the CloudWatch console, choose **Trace Map** under **X-Ray traces** from
the left navigation pane. By default, the trace map displays nodes for all source accounts that send traces to
the monitoring account, and nodes for the monitoring account itself. On the trace map, choose
**Filters** from the upper left to filter the trace map using the
**Accounts** drop-down. After an account filter is applied, service nodes from accounts that
don't match the current filter are grayed out.

![Filtered trace map](images/crossaccount-servicemap-account-filter.png)

When you choose a service node, the node details pane includes the service's account ID and label.

![Node detail pane](images/crossaccount-servicemap-node-detail.png)

In the upper-right corner of the trace map, choose **List view** to see a list of service
nodes. The list of service nodes includes services from the monitoring account and all configured source
accounts. Filter the list of nodes by **Account label** or **Account id** by
choosing them from the **Nodes** filter.

![Filtered service list](images/crossaccount-servicelist-account-filter.png)

### Traces

View trace details for traces that span multiple accounts by opening the CloudWatch console
from the monitoring account, and choosing **Traces** under **X-Ray
traces** in the left navigation pane. You can also open this page by choosing a
node in the X-Ray **Trace Map**, and then choosing **View
traces** from the node details pane.

The **Traces** page supports querying by account ID. To get started, [enter a query](xray-console-filters.md "xray-console-filters.md") that includes one or more account IDs. The following
example queries for traces that have passed through account ID Xor
_Y_:

```
service(id(account.id:"`X`")) OR service(id(account.id:"`Y`"))
```

![Query traces by account](images/crossaccount-traces-query-by-account.png)

Refine your query by **Account**. Select one or more accounts from the list, and choose
**Add to query**.

![Refine trace query by account](images/crossaccount-traces-refine-by-account.png)

### Trace details

View details for a trace by choosing it from the **Traces** list at the bottom of the
**Traces** page. The **Trace details** displays, including a trace details map with
service nodes from across all accounts that the trace passed through. Choose a specific service node to see its
corresponding account.

The **Segments timeline** section displays the account details for each segment in the
timeline.

![Segments timeline](images/crossaccount-traces-segment-timeline.png)
