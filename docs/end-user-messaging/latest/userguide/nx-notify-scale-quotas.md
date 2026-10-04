

# Quotas
<a name="nx-notify-scale-quotas"></a>

The following quotas and limits apply to Notify. For the full cross-channel quota tables and how to request increases, see [Quotas](nx-features-quotas.md).


**Notify quotas and limits**  

<table>
<thead>
  <tr><th>Limit</th><th>Basic tier</th><th>Advanced tier</th></tr>
</thead>
<tbody>
  <tr><td>Messages per day per configuration</td><td>200</td><td>Unlimited</td></tr>
  <tr><td>TPS per configuration</td><td>1</td><td>25</td></tr>
  <tr><td>Supported countries</td><td>30 pre-approved</td><td>All supported</td></tr>
  <tr><td>Notify configurations per account</td><td colspan="2">25 (adjustable)</td></tr>
  <tr><td>Messages to a single destination number per day, per configuration and per account</td><td colspan="2">10</td></tr>
</tbody>
</table>


Send API rate limits are 1 request per second on the Basic tier and 25 requests per second on the Advanced tier. Management actions such as `CreateNotifyConfiguration`, `UpdateNotifyConfiguration`, `DescribeNotifyTemplates`, and `ListNotifyCountries` are limited to 1 request per second. To request an increase, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/), navigate to AWS End User Messaging SMS, select the quota, and choose **Request quota increase**.