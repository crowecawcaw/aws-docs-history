# Monitor external key stores

AWS KMS collects metrics for each interaction with an external key store and publishes them
in your CloudWatch account. These metrics are used to generate the graphs in the monitoring
section of the detail page for each external key store. The following topic details how to
use the graphs to identify and troubleshoot operational and configuration issues impacting
your external key store. We recommend using the CloudWatch metrics to set alarms that notify you
when your external key store isn't performing as expected. For more information, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

###### Topics

- [Viewing the graphs](#xks-monitoring-navigate "#xks-monitoring-navigate")
- [Interpreting the graphs](#interpreting-graphs "#interpreting-graphs")

## Viewing the graphs

You can view the graphs at different levels of detail. By default, each graph uses a
three hour time range and five minute aggregation [period](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchPeriods "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchPeriods"). You
can adjust the graph view within the console, but your changes will revert to the
default settings when the external key store detail page is closed or the browser is
refreshed. For help with Amazon CloudWatch terminology, see [Amazon CloudWatch concepts](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md").

### View data point details

The data in each graph is collected by [AWS KMS metrics](monitoring-cloudwatch.md#kms-metrics "monitoring-cloudwatch.md#kms-metrics").
To view more information about a specific data point, pause the mouse over the data
point on the line graph. This will display a pop-up with more information about the
metric that the graph was derived from. Each list item displays the [dimension](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#Dimension") value
recorded at that data point. The pop-up displays a null value
(**–**) if there is no metric data available for the
dimension value at that data point. Some graphs record multiple dimensions and
values for a single data point. Other graphs, like the [reliability graph](#reliability-graph "#reliability-graph"), use the data collected by
the metric to calculate a unique value. Each list item is associated with a
different line graph color.

### Modify the time range

To modify the [time
range](../../../AmazonCloudWatch/latest/monitoring/modify_graph_date_time.md "../../../AmazonCloudWatch/latest/monitoring/modify_graph_date_time.md"), select one of the predefined time ranges in the upper right
corner of the monitoring section. The predefined time ranges span from 1 hour to 1
week (**1h**, **3h**,
**12h**, **1d**,
**3d**, or **1w**).
This adjusts the time range for all graphs. If you want to view one specific graph
in a different time range, or if you want to set a custom time range, enlarge the
graph or view it in the Amazon CloudWatch console.

### Zoom in on graphs

You can use the [mini-map zoom
feature](../../../AmazonCloudWatch/latest/monitoring/zoom-graph.md "../../../AmazonCloudWatch/latest/monitoring/zoom-graph.md") to focus on sections of line graphs and stacked portions of the
graphs without changing between zoomed-in and zoomed-out views. For example, you can
use the mini-map zoom feature to focus on a peak in a graph, so that you can compare
the spike against other graphs in the monitoring section from the same timeline.

1. Choose and drag on the area of the graph that you want to focus on, and
   then release the drag.
2. To reset the zoom, choose the **Reset zoom** icon, which
   looks like a magnifying glass with a minus (-) symbol inside.

### Enlarge a graph

To enlarge a graph, select the menu icon in the upper right corner of an
individual graph and choose **Enlarge**. You can also select the
enlarge icon that appears next to the menu icon when you hover over a graph.

Enlarging a graph enables you to further modify the view of a graph by specifying
a different period, custom time range, or refresh interval. These changes will
revert to the default settings when you close the enlarged view.

Modify the period

1. Choose the **Period options** menu. By
   default, this menu displays the value: **5
   minutes**.
2. Choose a period, the predefined periods span from 1 second to
   30 days.

For example, you can choose a one-minute view, which can be
useful when troubleshooting. Or, choose a less detailed,
one-hour view. That can be useful when viewing a broader time
range (for example, 3 days) so that you can see trends over
time. For more information, see [Periods](../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchPeriods "../../../AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.md#CloudWatchPeriods") in the
_Amazon CloudWatch User Guide_.

Modify the time range or time zone

1. Select one of the predefined time ranges, which span from 1
   hour to 1 week (**1h**, **3h**, **12h**, **1d**,
   **3d**, or **1w**). Alternatively, you can choose
   **Custom** to set your own time
   range.
2. Choose **Custom**
   1. _Time range:_ select the
      **Absolute** tab in the upper left
      corner of the box. Use the calendar picker or text field
      boxes to specify a time range.
   2. _Time zone:_ choose the dropdown in
      the upper right corner of the box. You can change the
      time zone to **UTC** or **Local
      time zone**.

3. After you specify a time range, choose
   **Apply**.

Modify how often the data in your graph is refreshed

1. Choose the **Refresh options** menu in the
   upper-right corner.
2. Choose a refresh interval (**Off**, **10
   Seconds**, **1 Minute**,
   **2 Minutes**, **5 Minutes**, or **15 Minutes**).

### View graphs in the Amazon CloudWatch console

The graphs in the monitoring section are derived from predefined metrics that
AWS KMS publishes to Amazon CloudWatch. You can open them within the CloudWatch console and save them
to CloudWatch dashboards. If you have multiple external key stores, you can open their
respective graphs in CloudWatch and save them to a single dashboard to compare their
health and usage.

###### Add to CloudWatch dashboard

Select **Add to dashboard** in the upper right corner to add
all of the graphs to an Amazon CloudWatch dashboard. You can either select an existing
dashboard or create a new one. For information on using this dashboard to create
customized views of the graphs and alarms, see [Using Amazon CloudWatch
dashboards](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md") in the _Amazon CloudWatch User Guide_.

###### View in CloudWatch metrics

Select the menu icon in the upper right corner of an individual graph and
choose **View in metrics** to view this graph in the Amazon CloudWatch
console. From the CloudWatch console, you can add this single graph to a dashboard and
modify time ranges, periods, and refresh intervals. For more information see,
[Graphing metrics](../../../AmazonCloudWatch/latest/monitoring/graph_metrics.md "../../../AmazonCloudWatch/latest/monitoring/graph_metrics.md") in the
_Amazon CloudWatch User Guide_.

## Interpreting the graphs

AWS KMS provides several graphs to monitor the health of your external key store within
the AWS KMS console. These graphs are automatically configured and derived from [AWS KMS
metrics](monitoring-cloudwatch.md#kms-metrics "monitoring-cloudwatch.md#kms-metrics").

The graph data is collected as part of the calls you make to your external key store
and external keys. You might see data populating graphs during a time range that you did
not make any calls, this data comes from the periodic `GetHealthStatus` calls
that AWS KMS makes on your behalf to check the status of your external key store proxy and
external key manager. If your graphs display the message **No data
available**, then there were no calls recorded during that time range or
your external key store is in a [DISCONNECTED](xks-connect-disconnect.md#xks-connection-state "xks-connect-disconnect.md#xks-connection-state") state. You might be able to identify the time
your external key store disconnected by [adjusting your
view](#graph-time-range "#graph-time-range") to a broader time range.

###### Topics

- [Total requests](#total-requests-graph "#total-requests-graph")
- [Reliability](#reliability-graph "#reliability-graph")
- [Latency](#latency-graph "#latency-graph")
- [Top 5 exceptions](#top-5-exceptions-graph "#top-5-exceptions-graph")
- [Certificate days to expire](#cert-expire-graph "#cert-expire-graph")

### Total requests

The total number of AWS KMS requests being received for a specific external key
store during a given time range. Use this graph to determine if you are at risk of
throttling.

AWS KMS recommends that your external key manager be able to handle up to 1800
requests for cryptographic operations per second. If you approach 540,000 calls in a
five-minute period, you are at risk of throttling.

You can monitor the number of requests for cryptographic operations on KMS keys
in your external key store that AWS KMS throttles with the [ExternalKeyStoreThrottle](monitoring-cloudwatch.md#metric-throttling "monitoring-cloudwatch.md#metric-throttling") metric.

If you are getting very frequent `KMSInvalidStateException` errors with
a message that explains that the request was rejected "due to a very high request
rate," it might indicate that your external key manager or external key store proxy
cannot keep pace with the current request rate. If possible, lower your request
rate. You might also consider requesting a decrease in your custom key store request
quota value. Decreasing this quota value might increase throttling, but it indicates
that AWS KMS is rejecting excess requests quickly before they are sent to your
external key store proxy or external key manager. To request a quota decrease,
please visit [AWS Support Center](https://console.aws.amazon.com/support/home "https://console.aws.amazon.com/support/home")
and create a case.

The total requests graph is derived from the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors")
metric, which collects data on both the successful and unsuccessful responses that
AWS KMS receives from your external key store proxy. When you [view a specific data point](#graph-data-point "#graph-data-point"), the pop-up
displays the value of the `CustomKeyStoreId` dimension alongside the
total number of AWS KMS requests recorded at that data point. The
`CustomKeyStoreId` will always be the same.

### Reliability

The percentage of AWS KMS requests for which the external key store proxy returned
either a successful response or a non-retryable error. Use this graph to evaluate
the operational health of your external key store proxy.

When the graph displays a value less than 100%, it indicates cases where the proxy
either did not respond or responded with a retryable error. This can indicate
problems with the network, slowness of the external key store proxy or external key
manager, or implementation bugs.

If the request includes a bad credential and your proxy responds with an
`AuthenticationFailedException`, the graph will still indicate 100%
reliability because the proxy identified an incorrect value in the [external key store proxy API request](keystore-external.md#concept-proxy-apis "keystore-external.md#concept-proxy-apis"), and
therefore the failure is expected. If the percentage of your reliability graph is
100%, then your external key store proxy is responding as expected. If the graph
displays a value less than 100%, then the proxy either responded with a retryable
error or timed out. For example, if the proxy responds with a
`ThrottlingException` due to a very high request rate, it will
display a lower reliability percentage because the proxy was unable to identify a
specific problem in the request that caused it to fail. This is because retryable
errors are likely transient problems that can be resolved by retrying the
request.

The following error responses will lower the reliability percentage. You can use
the [Top 5 exceptions](#top-5-exceptions-graph "#top-5-exceptions-graph")
graph and the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric to further monitor how
frequently your proxy returns each retryable error.

- `InternalException`
- `DependencyTimeoutException`
- `ThrottlingException`
- `XksProxyUnreachableException`

The reliability graph is derived from the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric, which collects data on both
the successful and unsuccessful responses that AWS KMS receives from your external key
store proxy. The reliability percentage will only lower if the response has an
`ErrorType` value of `Retryable`. When you [view a specific data point](#graph-data-point "#graph-data-point"), the pop-up
displays the value of the `CustomKeyStoreId` dimension alongside the
reliability percentage for AWS KMS requests recorded at that data point. The
`CustomKeyStoreId` will always be the same.

We recommend using the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric to create a CloudWatch alarm that
notifies you of potential networking problems by alerting you when more than five
retryable errors are recorded in a one minute period. For more information, see
[Create an alarm for retryable
errors](xks-alarms.md#retryable-errors-alarm "xks-alarms.md#retryable-errors-alarm").

### Latency

The number of milliseconds it takes for an external key store proxy to respond to
an AWS KMS request. Use this graph to evaluate the performance of your external key
store proxy and external key manager.

AWS KMS expects the external key store proxy to respond to each request within 250
milliseconds. In the case of network timeouts, AWS KMS will retry the request once. If
the proxy fails a second time, the recorded latency is the combined timeout limit
for both request attempts and the graph will display approximately 500 milliseconds.
In all other cases where the proxy doesn't respond within the 250 millisecond
timeout limit, the recorded latency is 250 milliseconds. If the proxy is frequently
timing out on encryption and decryption operations, consult your external proxy
administrator. For help troubleshooting latency problems, see [Latency and timeout errors](xks-troubleshooting.md#fix-xks-latency "xks-troubleshooting.md#fix-xks-latency").

Slow responses might also indicate that your external key manager cannot handle
the current request traffic. AWS KMS recommends that your external key manager be able
to handle up to 1800 requests for cryptographic operations per second. If your
external key manager cannot handle the 1800 requests per second rate, consider
requesting a decrease in your [request quota for
KMS keys in a custom key store](requests-per-second.md#rps-key-stores "requests-per-second.md#rps-key-stores"). Requests for cryptographic operations
using the KMS keys in your external key store will fail fast with a [throttling exception](throttling.md "throttling.md"), rather than being processed
and later rejected by your external key store proxy or external key manager.

The latency graph is derived from the [XksProxyLatency](monitoring-cloudwatch.md#metric-xks-proxy-latency "monitoring-cloudwatch.md#metric-xks-proxy-latency") metric. When you [view a specific data point](#graph-data-point "#graph-data-point"), the pop-up
displays the corresponding `KmsOperation` and `XksOperation`
dimension values alongside the average latency recorded for the operations at that
data point. The list items are ordered from highest latency to lowest.

We recommend using the [XksProxyLatency](monitoring-cloudwatch.md#metric-xks-proxy-latency "monitoring-cloudwatch.md#metric-xks-proxy-latency") metric to create a CloudWatch alarm that
notifies you when your latency is approaching the timeout limit. For more
information, see [Create an alarm for response
timeout](xks-alarms.md#latency-alarm "xks-alarms.md#latency-alarm").

### Top 5 exceptions

The top five exceptions for failed cryptographic and management operations during
a given time range. Use this graph to track the most frequent errors, so you can
prioritize your engineering effort.

This count includes exceptions that AWS KMS received from the external key store
proxy and the `XksProxyUnreachableException` that AWS KMS returns
internally when it cannot establish communication with the external key store
proxy.

High rates of retryable errors might indicate networking errors, while high rates
of non-retryable errors might indicate a problem with the configuration of your
external key store. For example, a spike in
`AuthenticationFailedExceptions` indicates a discrepancy between the
authentication credentials configured in AWS KMS and the external key store proxy. To
view your external key store configuration, see [View external key stores](view-xks-keystore.md "view-xks-keystore.md"). To edit your external key store settings,
see [Edit external key store properties](update-xks-keystore.md "update-xks-keystore.md").

The exceptions that AWS KMS receives from the external key store proxy are different
from the exceptions that AWS KMS returns when an operation fails. AWS KMS cryptographic
operations return an `KMSInvalidStateException` for all failures related
to the external configuration or connection state of the external key store. To
identify the problem, use the accompanying error message text.

The following table shows the exceptions that can appear in the top 5 exceptions
graph and the corresponding exceptions that AWS KMS returns to you.

| Error type    | Exception displayed in the graph                                                                                                                                                                                                                                         | Exception that AWS KMS returned to you                                                                                                                                                                                                                                                                               |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Non-retryable | **`AccessDeniedException`**<br>For troubleshooting help, see [Proxy authorization issues](xks-troubleshooting.md#fix-xks-authorization "xks-troubleshooting.md#fix-xks-authorization").                                                                                  | **`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                                                                                                                                               |
| Non-retryable | **`AuthenticationFailedException`**<br>For troubleshooting help, see [Authentication credential errors](xks-troubleshooting.md#fix-xks-credentials "xks-troubleshooting.md#fix-xks-credentials").                                                                        | **`XksProxyIncorrectAuthenticationCredentialException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore`<br>operations.**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations. |
| Retryable     | **`DependencyTimeoutException`**<br>For troubleshooting help, see [Latency and timeout errors](xks-troubleshooting.md#fix-xks-latency "xks-troubleshooting.md#fix-xks-latency").                                                                                         | **`XksProxyUriUnreachableException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                   |
| Retryable     | **`InternalException`**<br>The external key store proxy rejected the request because it<br>cannot communicate with the external key manager. Verify that<br>the external key store proxy configuration is correct and that<br>the external key manager is available.     | **`XksProxyInvalidResponseException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                  |
| Non-retryable | **`InvalidCiphertextException`**<br>For troubleshooting help, see [Decryption errors](xks-troubleshooting.md#fix-xks-decrypt "xks-troubleshooting.md#fix-xks-decrypt").                                                                                                  | \*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                                                                                                                                                                                                                                      |
| Non-retryable | **`InvalidKeyUsageException`**<br>For troubleshooting help, see [Cryptographic operation errors for the<br>external key](xks-troubleshooting.md#fix-external-key-crypto "xks-troubleshooting.md#fix-external-key-crypto").                                               | **`XksKeyInvalidConfigurationException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                                                                                                                                               |
| Non-retryable | **`InvalidStateException`**<br>For troubleshooting help, see [Cryptographic operation errors for the<br>external key](xks-troubleshooting.md#fix-external-key-crypto "xks-troubleshooting.md#fix-external-key-crypto").                                                  | **`XksKeyInvalidConfigurationException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                                                                                                                                               |
| Non-retryable | **`InvalidUriPathException`**<br>For troubleshooting help, see [General configuration errors](xks-troubleshooting.md#fix-xks-gen-configuration "xks-troubleshooting.md#fix-xks-gen-configuration").                                                                      | **`XksProxyInvalidConfigurationException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.             |
| Non-retryable | **`KeyNotFoundException`**<br>For troubleshooting help, see [External key errors](xks-troubleshooting.md#fix-external-key "xks-troubleshooting.md#fix-external-key").                                                                                                    | **`XksKeyNotFoundException`\*<br>• in response<br>to `CreateKey` operations.<br>**`KMSInvalidStateException`\*<br>• in<br>response to cryptographic operations.                                                                                                                                                      |
| Retryable     | **`ThrottlingException`**<br>The external key store proxy rejected the request due to a<br>very high request rate. Reduce the frequency of your calls using<br>KMS keys in this external key store.                                                                      | **`XksProxyUriUnreachableException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                   |
| Non-retryable | **`UnsupportedOperationException`**<br>For troubleshooting help, see [Cryptographic operation errors for the<br>external key](xks-troubleshooting.md#fix-external-key-crypto "xks-troubleshooting.md#fix-external-key-crypto").                                          | **`XksKeyInvalidResponseException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                                                                                                                                                    |
| Non-retryable | **`ValidationException`**<br>For troubleshooting help, see [Proxy issues](xks-troubleshooting.md#fix-xks-proxy "xks-troubleshooting.md#fix-xks-proxy").                                                                                                                  | **`XksProxyInvalidResponseException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                  |
| Retryable     | **`XksProxyUnreachableException`**<br>If you see this error repeatedly, verify that your external<br>key store proxy is active and is connected to the network, and<br>that its URI path and endpoint URI or VPC service name are<br>correct in your external key store. | **`XksProxyUriUnreachableException`**<br>in response to `CreateCustomKeyStore` and<br>`UpdateCustomKeyStore` operations.<br>**`CustomKeyStoreInvalidStateException`**<br>in response to `CreateKey` operations.<br>\*_`KMSInvalidStateException`_<br>• in<br>response to cryptographic operations.                   |

The top 5 exceptions graph is derived from the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors")
metric. When you [view a specific data point](#graph-data-point "#graph-data-point"),
the pop-up displays the value of the `ExceptionName` dimension alongside
the number of times that the exception was recorded at that data point. The five
list items are ordered from most frequent exception to least.

We recommend using the [XksProxyErrors](monitoring-cloudwatch.md#metric-xks-proxy-errors "monitoring-cloudwatch.md#metric-xks-proxy-errors") metric to create a CloudWatch alarm that
notifies you of potential configuration problems by alerting you when more than five
non-retryable errors are recorded in a one minute period. For more information, see
[Create an alarm for
non-retryable errors](xks-alarms.md#nonretryable-errors-alarm "xks-alarms.md#nonretryable-errors-alarm").

### Certificate days to expire

The number of days until the TLS certificate for your external key store proxy
endpoint (`XksProxyUriEndpoint`) expires. Use this graph to monitor
upcoming expiration of your TLS certificate.

When the certificate expires, AWS KMS cannot communicate with the external key store
proxy. All data protected by KMS keys in your external key store becomes
inaccessible until you renew the certificate.

The certificate days to expire graph is derived from the [XksProxyCertificateDaysToExpire](monitoring-cloudwatch.md#metric-xks-proxy-certificate-days-to-expire "monitoring-cloudwatch.md#metric-xks-proxy-certificate-days-to-expire") metric. We
strongly recommend using this metric to create a CloudWatch alarm that notifies you about
the upcoming expiration. Certificate expiration might prevent you from accessing
your encrypted resources. Set the alarm to give your organization time to renew the
certificate before it expires. For more information, see [Create an alarm for certificate
expiration](xks-alarms.md#cert-expire-alarm "xks-alarms.md#cert-expire-alarm").
