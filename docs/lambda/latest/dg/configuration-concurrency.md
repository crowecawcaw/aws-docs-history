

# Configuring reserved concurrency for an Event Function
<a name="configuration-concurrency"></a>

In Lambda, [concurrency](lambda-concurrency.md) is the number of in-flight requests that your Event Function is currently handling. There are two types of concurrency controls available:
+ Reserved concurrency – This sets both the maximum and minimum number of concurrent instances allocated to your Event Function. When an Event Function has reserved concurrency, no other Event Function can use that concurrency. Reserved concurrency is useful for ensuring that your most critical functions always have enough concurrency to handle incoming requests. Additionally, reserved concurrency can be used for limiting concurrency to prevent overwhelming downstream resources, like database connections. Reserved concurrency acts as both a lower and upper bound - it reserves the specified capacity exclusively for your function while also preventing it from scaling beyond that limit. Configuring reserved concurrency for a function incurs no additional charges.
+ Provisioned concurrency – This is the number of pre-initialized execution environments allocated to your Event Function. These execution environments are ready to respond immediately to incoming function requests. Provisioned concurrency is useful for reducing cold start latencies for functions and designed to make functions available with double-digit millisecond response times. Generally, interactive workloads benefit the most from the feature. Those are applications with users initiating requests, such as web and mobile applications, and are the most sensitive to latency. Asynchronous workloads, such as data processing pipelines, are often less latency sensitive and so do not usually need provisioned concurrency. Configuring provisioned concurrency incurs additional charges to your AWS account.

This topic details how to manage and configure reserved concurrency. For a conceptual overview of these two types of concurrency controls, see [Reserved concurrency and provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html#reserved-and-provisioned). For information on configuring provisioned concurrency, see [Configuring provisioned concurrency for an Event Function](provisioned-concurrency.md).

**Note**  
Lambda Event Functions linked to an Amazon MQ event source mapping have a default maximum concurrency. For Apache Active MQ, the maximum number of concurrent instances is 5. For Rabbit MQ, the maximum number of concurrent instances is 1. Setting reserved or provisioned concurrency for your Event Function doesn't change these limits. To request an increase in the default maximum concurrency when using Amazon MQ, contact Support.

**Topics**
+ [Configuring reserved concurrency](#configuring-concurrency-reserved)
+ [Accurately estimating required reserved concurrency for an Event Function](#estimating-reserved-concurrency)

## Configuring reserved concurrency
<a name="configuring-concurrency-reserved"></a>

You can configure reserved concurrency settings for a Lambda Event Function using the Lambda console or the Lambda API.

**To reserve concurrency for an Event Function (console)**

1. Open the [Event Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the Event Function you want to reserve concurrency for.

1. Choose **Configuration** and then choose **Concurrency**.

1. Under **Concurrency**, choose **Edit**. 

1. Choose **Reserve concurrency**. Enter the amount of concurrency to reserve for the Event Function.

1. Choose **Save**.

You can reserve up to the **Unreserved account concurrency** value minus 100. The remaining 100 units of concurrency are for Event Functions that aren't using reserved concurrency. For example, if your account has a concurrency limit of 1,000, you cannot reserve all 1,000 units of concurrency to a single Event Function.

![An error occurs if you try to reserve too much concurrency.](https://docs.aws.amazon.com/lambda/latest/dg/images/concurrency-reserve-over-limit.png)


Reserving concurrency for an Event Function impacts the concurrency pool that's available to other Event Functions. For example, if you reserve 100 units of concurrency for `function-a`, other Event Functions in your account must share the remaining 900 units of concurrency, even if `function-a` doesn't use all 100 reserved concurrency units.

To intentionally throttle an Event Function, set its reserved concurrency to 0. This stops your Event Function from processing any events until you remove the limit.

To configure reserved concurrency with the Lambda API, use the following API operations.
+ [PutFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_PutFunctionConcurrency.html)
+ [GetFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_GetFunctionConcurrency.html)
+ [DeleteFunctionConcurrency](https://docs.aws.amazon.com/lambda/latest/api/API_DeleteFunctionConcurrency.html)

For example, to configure reserved concurrency with the AWS Command Line Interface (CLI), use the `put-function-concurrency` command. The following command reserves 100 concurrency units for an Event Function named `my-function`:

```
aws lambda put-function-concurrency --function-name my-function \
    --reserved-concurrent-executions 100
```

You should see output that looks like the following:

```
{
    "ReservedConcurrentExecutions": 100
}
```

## Accurately estimating required reserved concurrency for an Event Function
<a name="estimating-reserved-concurrency"></a>

If your Event Function is currently serving traffic, you can easily view its concurrency metrics using [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html). Specifically, the `ConcurrentExecutions` metric shows you the number of concurrent invocations for each Event Function in your account.

![Graph showing concurrency for an Event Function over time.](https://docs.aws.amazon.com/lambda/latest/dg/images/concurrency-concurrent-executions-metrics.png)


The previous graph suggests that this Event Function serves an average of 5 to 10 concurrent requests at any given time, and peaks at 20 requests on a typical day. Suppose that there are many other Event Functions in your account. ** If this Event Function is critical to your application and you don't want to drop any requests**, use a number greater than or equal to 20 as your reserved concurrency setting.

Alternatively, recall that you can also [ calculate concurrency](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html#calculating-concurrency) using the following formula:

```
Concurrency = (average requests per second) * (average request duration in seconds)
```

Multiplying average requests per second with the average request duration in seconds gives you a rough estimate of how much concurrency you need to reserve. You can estimate average requests per second using the `Invocation` metric, and the average request duration in seconds using the `Duration` metric. See [Using CloudWatch metrics with Lambda](monitoring-metrics.md) for more details.

You should also be familiar with your upstream and downstream throughput constraints. While Lambda Event Functions scale seamlessly with load, upstream and downstream dependencies might not have the same throughput capabilities. If you need to limit how high your Event Function can scale, configure reserved concurrency on your Event Function.