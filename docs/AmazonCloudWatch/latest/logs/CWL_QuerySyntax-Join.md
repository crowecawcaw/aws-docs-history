

# join
<a name="CWL_QuerySyntax-Join"></a>

Combines log events from a source log group with events from another log group or query result based on a matching field.

Use the `join` command to correlate related log events across different sources like log groups using keys common across them such as matching request identifiers or transaction IDs.

**Syntax**  


```
join type=<join_type> left=<left_alias> right=<right_alias> 
    where <left_alias>.<field>=<right_alias>.<field> 
    (SOURCE <right_log_group>)
```

**Parameters**  

+ `<right_log_group>` – The secondary data source to join with.
+ `<left_alias>` and `<right_alias>` – Aliases to distinguish fields from the left (primary) and right (secondary) data sources.
+ `where <field>` – Specifies the field used as the join key. The field must exist in both data sources.
+ `type=<join_type>` (optional) – Specifies the join type. Valid values are:
  + `inner` (default) – Returns only matching records
  + `left` – Returns all records from the primary data source and matching records from the secondary data source

**Examples**  


**Example 1: Correlate API Gateway requests with Lambda execution logs**  
This example shows how to join API Gateway access logs with Lambda function logs to correlate incoming requests with their backend processing. This is useful for troubleshooting end-to-end request flows and identifying which Lambda invocations correspond to specific API requests.  

```
filter status >= 500
| join type=inner left=api right=lambda 
    where api.requestId=lambda.requestId 
    (SOURCE '/aws/lambda/my-function')
| fields api.requestId, api.status, api.latency, lambda.duration, lambda.memoryUsed
| sort api.latency desc
```
This query:  

1. Queries API Gateway access logs and filters for server errors (status >= 500)

1. Joins with Lambda function logs using the `requestId` field that appears in both log sources

1. Uses aliases (`api` and `lambda`) to distinguish fields from each source

1. Returns combined information showing API latency alongside Lambda execution duration and memory usage

1. Sorts results by API latency to identify the slowest requests

**Example 2: Track distributed transactions across microservices**  
When debugging issues in a microservices architecture, you often need to trace a transaction across multiple services. This example shows how to join logs from two different services using a common transaction ID.  

```
filter eventType = "ORDER_CREATED"
| join type=left left=order right=payment 
    where order.transactionId=payment.transactionId 
    (SOURCE '/aws/lambda/payment-service')
| filter payment.eventType = "PAYMENT_PROCESSED" or !ispresent(payment.eventType)
| fields order.transactionId, order.orderId, order.customerId, 
    payment.paymentStatus, payment.amount
| filter payment.paymentStatus != "SUCCESS" or !ispresent(payment.paymentStatus)
```
This query:  

1. Starts with order creation events from the order service

1. Uses a `left join` to include all orders, even those without matching payment records

1. Joins with payment processing events using the shared `transactionId` field

1. Filters the final results to show only orders with failed payments or missing payment records
The left join is important here because it ensures you see orders that were created but never had a corresponding payment event, which could indicate a system failure.

**Behavior**  

+ The primary data source (left side) is processed first.
+ The secondary data source is evaluated and matched using the specified join key.
+ Matching is performed using equality comparison on the join field.
+ For left joins, unmatched records from the primary data source are retained with null values for secondary fields.

**Notes and limitations**  

+ Only equality (=) conditions are supported.
+ Only one join command is supported per query.
+ Join keys must exist in both data sources and be of compatible types.
+ Queries using join may scan more data and incur higher costs.
+ The number of unique key values in the secondary data source is limited to 50,000 to ensure query performance.
+ Subqueries on right side of join are not supported.

**Related commands**  

+ [fields](CWL_QuerySyntax-Fields.md)
+ [filter](CWL_QuerySyntax-Filter.md)
+ [parse](CWL_QuerySyntax-Parse.md)
+ [stats](CWL_QuerySyntax-Stats.md)
+ [sort](CWL_QuerySyntax-Sort.md)
+ [limit](CWL_QuerySyntax-Limit.md)