

# RTB Fabric dimensions
<a name="monitoring-cloudwatch-dimensions"></a>

The following dimensions are supported for RTB Fabric metrics.


|  Dimension  |  Description  | 
| --- | --- | 
|  Link  | The unique identifier for the link between RTB gateways. | 
|  HttpStatusCode  | The HTTP status code returned by the service (for example, 200, 404, 500). Available for the `request-status-count` metric. | 
|  Statistic  | The statistical measure for latency metrics (P90, P95, P99). Available for latency metrics only. | 
|  ModuleId  | The identifier of the module that filtered the transaction. Available for the `filter-transaction` metric. | 
|  Reason  | The reason a transaction was filtered. Available for the `filter-transaction` metric. | 
|  GatewayId  | The unique identifier for the RTB gateway. Available for the `no-bid-external` and `no-bid-internal` metrics. | 