

# subqueries
<a name="CWL_QuerySyntax-Subqueries"></a>

A subquery is a nested Logs Insights query that can be used as an input to another query. Subqueries can be used to derive intermediate result sets that are then consumed by subsequent commands.

**Syntax**  


**Subquery in filter**  


```
filter <field> in (
    <subquery>
)
```

**Parameters**  

+ `<subquery>` – A valid Logs Insights query that returns a result set. The subquery must produce fields referenced by the outer query.

**Examples**  


**Example 1: Find requests that encountered errors in downstream services**  
This example shows how to use a subquery to identify requests in your main service that resulted in errors in a downstream service. This is useful for troubleshooting cascading failures in distributed systems.  

```
filter requestId in (
    SOURCE '/aws/lambda/database-service'
    | filter errorType = "DatabaseConnectionTimeout"
    | fields requestId
)
| fields @timestamp, requestId, endpoint, userId, responseTime
| sort @timestamp desc
```
This query:  

1. The subquery finds all `requestId` values from the database service that experienced connection timeouts

1. The outer query filters your main service's logs to show only requests that match those error-prone request IDs

1. Results show the full context of requests that failed downstream, including which endpoints and users were affected
This pattern helps you understand the upstream impact of downstream failures.

**Example 2: Identify frequently failing requests for targeted investigation**  
This example demonstrates using a subquery with aggregation to find requests that fail repeatedly, which often indicates systematic issues rather than transient errors.  

```
filter requestId in (
    SOURCE '/aws/lambda/payment-processor'
    | filter status = "FAILED"
    | stats count(*) as failureCount by requestId
    | filter failureCount > 3
    | fields requestId
)
| fields @timestamp, requestId, customerId, amount, failureReason
| sort @timestamp asc
```
This query:  

1. The subquery aggregates failed payment attempts and identifies request IDs that failed more than 3 times

1. The outer query retrieves all log events for those problematic request IDs

1. Results are sorted chronologically to show the progression of retry attempts
This helps distinguish between transient failures (single occurrence) and persistent issues (multiple failures) that require deeper investigation.

**Behavior**  

+ Subqueries are executed independently of the outer query.
+ Results are materialized before being consumed by the outer query.
+ Only fields explicitly selected in the subquery are available to the outer query.

**Notes and limitations**  

+ Subqueries must return fields referenced by the outer query.
+ Nested subqueries are not supported.
+ Subqueries may increase query execution time and cost.
+ Correlated subqueries are not supported.
+ Inner query execution is limited to 30 seconds.

**Related commands**  

+ [fields](CWL_QuerySyntax-Fields.md)
+ [filter](CWL_QuerySyntax-Filter.md)
+ [parse](CWL_QuerySyntax-Parse.md)
+ [stats](CWL_QuerySyntax-Stats.md)
+ [sort](CWL_QuerySyntax-Sort.md)
+ [limit](CWL_QuerySyntax-Limit.md)