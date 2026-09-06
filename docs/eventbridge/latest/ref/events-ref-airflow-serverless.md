

# Amazon MWAA Serverless events
<a name="events-ref-airflow-serverless"></a>

MWAA Serverless sends service events directly to EventBridge.

## MWAA Serverless service events
<a name="events-ref-airflow-serverless-events"></a>

MWAA Serverless sends the following events directly to EventBridge: 
+ MWAA Serverless Workflow Run Started
+ MWAA Serverless Workflow Run Queued
+ MWAA Serverless Workflow Run Running
+ MWAA Serverless Workflow Run Succeeded
+ MWAA Serverless Workflow Run Failed
+ MWAA Serverless Workflow Run Stopped
+ MWAA Serverless Workflow Run Timeout
+ MWAA Serverless Task Queued
+ MWAA Serverless Task Scheduled
+ MWAA Serverless Task Upstream Failed
+ MWAA Serverless Task Running
+ MWAA Serverless Task Succeeded
+ MWAA Serverless Task Failed
+ MWAA Serverless Task Up For Retry
+ MWAA Serverless Task Timeout

*Delivery type*: [ Durable ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.airflow-serverless

```
{
  "source": ["aws.airflow-serverless"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.airflow-serverless"],
  "detail-type": ["{{MWAA Serverless Workflow Run State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.