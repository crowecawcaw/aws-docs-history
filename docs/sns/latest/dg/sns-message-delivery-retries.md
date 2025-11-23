# Amazon SNS message delivery retries

Amazon SNS defines a _delivery policy_ for each delivery protocol. The
delivery policy defines how Amazon SNS retries the delivery of messages when server-side errors
occur (when the system that hosts the subscribed endpoint becomes unavailable). When the
delivery policy is exhausted, Amazon SNS stops retrying the delivery and discards the
message—unless a dead-letter queue is attached to the subscription. For more
information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md").

## Delivery protocols and

policies

###### Note

- With the exception of HTTP/S, you can't change Amazon SNS-defined delivery
  policies. Only HTTP/S supports custom policies. See [Creating an HTTP/S delivery policy](#creating-delivery-policy "#creating-delivery-policy").
- Amazon SNS applies jittering to delivery retries. For more information, see the
  [Exponential Backoff and Jitter](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/ "https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/") post on the _AWS
  Architecture Blog_.
- **The total policy retry time for an HTTP/S endpoint
  cannot be greater than 3,600 seconds. This is a hard limit and cannot be
  increased**.

| Endpoint type              | Delivery protocols | Immediate retry (no delay) phase | Pre-backoff phase         | Backoff phase                                                                      | Post-backoff phase                       | Total attempts              |
| -------------------------- | ------------------ | -------------------------------- | ------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------- | --------------------------- |
| AWS managed endpoints      | ¹                  | 3 times, without delay           | 2 times, 1 second apart   | 10 times, with exponential backoff, from 1 second to 20<br>seconds                 | 100,000 times, 20 seconds apart          | 100,015 times, over 23 days |
| AWS Lambda                 |
| Amazon SQS                 |
| Customer managed endpoints | SMTP               | 0 times, without delay           | 2 times, 10 seconds apart | 10 times, with exponential backoff, from 10 seconds to<br>600 seconds (10 minutes) | 38 times, 600 seconds (10 minutes) apart | 50 attempts, over 6 hours   |
| SMS                        |
| Mobile push                |

¹ For throttling errors with the Firehose protocol, Amazon SNS uses the same delivery
policy as for customer managed endpoints.

## Delivery policy stages

The following diagram shows the phases of a delivery policy.

![An x y axis diagram displaying Time as the x value and Initial Delivery Attempt as the y value. The delivery policy begins with the Immediate Retry Phase on the y axis, followed on the x axis by the Pre-Backoff Phase, the Backoff Phase, and the Post-Backoff Phase.](images/sns-delivery-policy-phases.png)

Each delivery policy is comprised of four phases.

1. **Immediate retry phase (no delay)** –
   This phase occurs immediately after the initial delivery attempt. There is no
   delay between retries in this phase.
2. **Pre-backoff phase** – This phase follows
   the Immediate Retry Phase. Amazon SNS uses this phase to attempt a set of retries
   before applying a backoff function. This phase specifies the number of retries
   and the amount of delay between them.
3. **Backoff phase** – This phase controls
   the delay between retries by using the retry-backoff function. This phase sets a
   minimum delay, a maximum delay, and a retry-backoff function that defines how
   quickly the delay increases from the minimum to the maximum delay. The backoff
   function can be arithmetic, exponential, geometric, or linear.
4. **Post-backoff phase** – This phase
   follows the backoff phase. It specifies a number of retries and the amount of
   delay between them. This is the final phase.

## Creating an HTTP/S delivery policy

You can define how Amazon SNS retries message delivery to HTTP/S endpoints using a delivery
policy with four phases: _no-delay_, _pre-backoff_, _backoff_,
and _post-backoff_. This policy allows you to override
the default retry settings and customize them to match the capacity of your HTTP
server.

You can define your HTTP/S delivery policy as a JSON object at either the **topic** or **subscription**
level:

- **Topic-level policy** – Applies to all
  HTTP/S subscriptions linked to the topic. Use the [`CreateTopic`](../api/API_CreateTopic.md "../api/API_CreateTopic.md")
  or [`SetTopicAttributes`](../api/API_SetTopicAttributes.md "../api/API_SetTopicAttributes.md") API action to set this
  policy.
- **Subscription-level policy** – Applies
  only to a specific subscription. Use the [`Subscribe`](../api/API_Subscribe.md "../api/API_Subscribe.md") or
  [`SetSubscriptionAttributes`](../api/API_SetSubscriptionAttributes.md "../api/API_SetSubscriptionAttributes.md") API action to set this
  policy.

Alternatively, you can also use the [AWS::SNS::Subscription](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sns-subscription.md") resource in your CloudFormation templates.

You should customize your delivery policy based on your HTTP/S server's
capacity:

- **Single server for all subscriptions** –
  If all HTTP/S subscriptions in a topic use the same server, set the delivery
  policy as a topic attribute to ensure consistency across all
  subscriptions.
- **Different servers for subscriptions** –
  If subscriptions target different servers, create a unique delivery policy for
  each subscription, tailored to the capacity of the specific server.

You can also set the `Content-Type` header in the request policy to specify
the media type of the notification. By default, Amazon SNS sends all the notifications to
HTTP/S endpoints with content type set to `text/plain; charset=UTF-8`.
However, you can override this default using the [headerContentType](#header-content-type "#header-content-type") field in the request policy.

The following JSON object defines a delivery policy with retries structured in four
phases:

1. **No-delay phase** – Retry 3 times
   immediately.
2. **Pre-backoff phase** – Retry 2 times with
   a 1 second interval.
3. **Backoff phase** – Retry 10 times with
   exponential delays ranging from 1 to 60 seconds.
4. **Post-backoff phase** – Retry 35 times
   with a fixed 60-second interval.

Amazon SNS makes a total of **50 attempts** to deliver a
message before discarding it. To retain messages that can't be delivered after all
retries, configure your subscription to move undeliverable messages to a dead-letter
queue (DLQ). For more information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md").

Amazon SNS considers all 5XX errors and 429 (too many requests sent) errors as retryable. These errors are subject to the delivery policy. All other errors are considered as permanent failures and retries will not be attempted.

###### Note

This delivery policy uses the `maxReceivesPerSecond` property to
throttle delivery traffic to an average of 10 messages per second per subscription.
While this mechanism helps prevent your HTTP/S endpoint from being overwhelmed by
high traffic, it's designed to maintain an average delivery rate and doesn't enforce
a strict cap. Occasional delivery traffic spikes above the specified limit may
occur, especially if your publishing rate is significantly higher than the
throttling limit.

When the publishing (inbound) traffic exceeds the delivery (outbound) rate, it can
result in a message backlog and higher delivery latency. To avoid such issues,
ensure the `maxReceivesPerSecond` value aligns with your HTTP/S server's
capacity and workload requirements.

The following delivery policy example overrides the default content type for HTTP/S
notification to `application/json`.

```
{
    "healthyRetryPolicy": {
        "minDelayTarget": 1,
        "maxDelayTarget": 60,
        "numRetries": 50,
        "numNoDelayRetries": 3,
        "numMinDelayRetries": 2,
        "numMaxDelayRetries": 35,
        "backoffFunction": "exponential"
    },
    "throttlePolicy": {
        "maxReceivesPerSecond": 10
    },
    "requestPolicy": {
        "headerContentType": "application/json"
    }
}
```

The delivery policy is composed of a **retry policy**,
**throttle policy** and a **request
policy**. In total, there are **9 attributes** in
a delivery policy.

| Policy                 | Description                                                                                          | Constraint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `minDelayTarget`       | The minimum delay for a retry.\*_Unit:_<br>• Seconds                                                 | 1 to maximum delay**Default:**<br>20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `maxDelayTarget`       | The maximum delay for a retry.\*_Unit:_<br>• Seconds                                                 | Minimum delay to 3,600**Default:**<br>20                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `numRetries`           | The total number of retries, including immediate, pre-backoff, backoff,<br>and post-backoff retries. | 0 to 100\*_Default:_<br>• 3                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `numNoDelayRetries`    | The number of retries to be done immediately, with no delay between<br>them.                         | 0 or greater**Default:**<br>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `numMinDelayRetries`   | The number of retries in the pre-backoff phase, with the specified<br>minimum delay between them.    | 0 or greater**Default:**<br>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `numMaxDelayRetries`   | The number of retries in the post-backoff phase, with the maximum delay<br>between them.             | 0 or greater**Default:**<br>0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `backoffFunction`      | The model for backoff between retries.                                                               | One of four options:<br>• arithmetic<br>• exponential<br>• geometric<br>• linear<br>\*_Default:_<br>• linear                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `maxReceivesPerSecond` | The maximum average number of message deliveries per second, per<br>subscription.                    | 1 or greater\*_Default:_<br>• No throttling<br>(no limit on delivery rate)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `headerContentType`    | The content type of the notification being sent to HTTP/S<br>endpoints.                              | If the request policy is not defined, the content type defaults to<br>`text/plain; charset=UTF-8`.<br>When the raw message delivery is disabled for a subscription<br>(default), or when the delivery policy is defined on the topic-level,<br>the supported header content types are `application/json` and<br>`text/plain`.<br>When the raw message delivery is enabled for a subscription, the<br>following content types are supported:<br>• text/css<br>• text/csv<br>• text/html<br>• text/plain<br>• text/xml<br>• application/atom+xml<br>• application/json<br>• application/octet-stream<br>• application/soap+xml<br>• application/x-www-form-urlencoded<br>• application/xhtml+xml<br>• application/xml |

Amazon SNS uses the following formula to calculate the number of retries in the backoff
phase:

```
numRetries - numNoDelayRetries - numMinDelayRetries - numMaxDelayRetries
```

You can control the frequency of retries during the backoff phase using three
parameters:

- **`minDelayTarget`** – Sets the
  delay for the first retry attempt in the backoff phase.
- **`maxDelayTarget`** – Sets the
  delay for the final retry attempt in the backoff phase.
- **`backoffFunction`** – Determines
  the algorithm Amazon SNS uses to calculate the delays for all retry attempts between the
  first and last retries. You can choose from four available retry-backoff
  functions.
  The following diagram illustrates how different retry backoff functions affect the delays
  between retries during the backoff phase. The delivery policy used for this example includes
  the following settings: **10 total retries**, a **minimum delay of 5 seconds**, and a **maximum
  delay of 260 seconds**.

- The **vertical axis** shows the delay (in seconds)
  for each retry attempt.
- The **horizontal axis** represents the retry
  sequence, ranging from the first to the tenth attempt.

![The diagram shows how retry delays progress over 10 attempts based on four backoff functions: exponential, arithmetic, linear, and geometric. Each colored line represents a function's delay pattern: Exponential: Increases rapidly, reaching the maximum delay the quickest, Linear: Increases steadily with each retry, Arithmetic and Geometric: Show moderate increases, steeper than linear but less rapid than exponential. All lines start near the minimum delay of 5 seconds and approach the maximum delay of 260 seconds by the tenth retry.](images/backoff-graph.png)
