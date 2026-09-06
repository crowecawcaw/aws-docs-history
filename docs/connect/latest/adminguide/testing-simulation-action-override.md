

# Override system behavior actions
<a name="testing-simulation-action-override"></a>

Override System Behavior actions provide a powerful way to control how specific resources in your contact flow operate during test execution. When you override a resource, you're temporarily changing its behavior for testing purposes without modifying your actual contact flow configuration.

## How resource overrides work
<a name="testing-simulation-action-override-how"></a>

When you configure an override for a resource (such as a Lambda function, queue, Lex bot, or hours of operation), the override applies only once to that specific resource. This means the next time that particular resource is invoked during your test, it will use your override configuration. After that single use, the override is consumed, and subsequent invocations will behave normally—unless you've configured additional overrides.

**Important**  
Only one active override per specific resource is allowed at any given time. If you configure multiple overrides for the same resource in sequence, they work like a "queue" (first in, first out). The least recent configured override takes precedence, but later overrides remain available and will activate in sequential order as each override is consumed.

This single-use behavior gives you maximum flexibility to override resources at different points in your test flow, allowing you to test various scenarios with the same resource behaving differently at different points in time. However, the best practice is to override your resources when you observe them to simplify your test configuration logic.

## Simple example: Testing different Lambda responses
<a name="testing-simulation-action-override-example"></a>

Let's walk through a practical example to illustrate how this works.

Scenario: Your contact flow calls a specific Lambda function twice, once to validate a customer's account status and again later to retrieve their order history. You want to test how your flow handles different responses from each call.

Test Configuration:
+ **First Interaction Group** – Observe: Test started
  + Action: Override Lambda function "ValidateAccount" with mock response returning "Active"
+ **Second Interaction Group** – Observe: Lambda function "ValidateAccount" starts
  + Action: Override Lambda function "ValidateAccount" with mock response returning "Suspended"
  + The first override (returning "Active") is used because it was configured least recently within the interaction group
  + Your flow receives "Active" status.
+ **Third Interaction Group** – Observe: Lambda function "ValidateAccount" starts again
  + The most recent override (returning "Suspended") is now used
  + Your flow receives "Suspended" status.

What happens: Even though you configured two overrides for the same Lambda function, each override is consumed only once, in sequential order of configuration. With sequential overrides, you can test how your flow handles different responses from the same resource at different points in the test.

![Test case designer showing three interaction groups with Lambda function overrides configured in sequence.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-override-example.png)


## Override resources and actions supported
<a name="testing-simulation-action-override-resources"></a>

### Lambda function override
<a name="testing-simulation-action-override-lambda"></a>

Controls how Lambda function calls behave during your test. You can redirect to a different Lambda function or provide mock responses.

**Substitute Resource:** Redirects Lambda invocations to use a different function, useful when you want to use a test version of your Lambda function.

Configuration options:
+ **Action** – Select "Mock Resource Behavior"
+ **Resource Type** – Lambda function
+ **Target resource** – Select from dropdown or enter the ARN of the Lambda function you want to override
+ **Option** – Choose "Substitute Resource"
+ **Substitute resource** – Select from dropdown or provide the ARN of the replacement Lambda function

**Mock Response:** Provides predefined responses without actually calling any Lambda function, use for isolated testing.

Configuration options for Success Response:
+ **Option** – Choose "Mock Response"
+ **Response** – Select "Success"
+ **Delay** – Specify how many seconds to wait before returning the response
+ **Raw JSON** (optional) – Enter the data that should be returned (in JSON format)

Configuration options for Error Response:
+ **Option** – Choose "Mock Response"
+ **Response** – Select "Error"
+ **Delay** – Specify how many seconds to wait before returning the response

![Action block configuration showing Lambda function override with mock response options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-override-lambda.png)


### Hours of operation override
<a name="testing-simulation-action-override-hours"></a>

Modifies how hours of operation checks behave, allowing you to test both in-hours and out-of-hours scenarios regardless of the actual time.

**Substitute Resource:** Redirects to a different hours of operation resource.

Configuration options:
+ **Action** – Select "Mock Resource Behavior"
+ **Resource Type** – Hours of operation
+ **Target resource** – Select from dropdown or enter the ARN of the Hours of operation you want to override
+ **Option** – Choose "Substitute Resource"
+ **Substitute resource** – Select from dropdown or provide the ARN of the replacement hours of operation resource

**Mock Response:** Returns a predefined result without checking actual hours.

Configuration options for Response:
+ **Option** – Choose "Mock Response"
+ **Response** – Choose either "InHours" or "OutOfHours" or "Error"

![Action block configuration showing Hours of operation override with mock response options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-override-hours.png)


### Lex bot override
<a name="testing-simulation-action-override-lex"></a>

Controls Lex bot interactions during testing, allowing you to use test bots.

**Substitute Resource:** Redirects to a different Lex bot.

Configuration options:
+ **Action** – Select "Mock Resource Behavior"
+ **Resource Type** – Lex bot
+ **Target resource** – Select from dropdown or enter the ARN and Alias of the Lex bot you want to override
+ **Option** – Choose "Substitute Resource"
+ **Substitute resource** – Select from dropdown or provide the ARN and Alias of the replacement Lex bot resource

**Mock Response:** Provides predefined bot responses without invoking the actual bot.

Configuration options for Response:
+ **Option** – Choose "Mock Response"
+ **Response** – Choose either "Success" or "Error" or "Time limit exceeded"
+ **Delay** – Specify how many seconds to wait before returning the response
+ **Raw JSON** (optional) – Enter the data that should be returned (in JSON format)

![Action block configuration showing Lex bot override with mock response options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-override-lex.png)


**Lex V2 bot intent resolution might differ during simulation**  
During simulation, Text/Utterance input sends customer utterances to the Lex V2 bot as text. On a real voice call, the bot uses a voice-optimized path. This path might produce different confidence scores for the same words. As a result, the bot might return `FallbackIntent` during simulation for utterances that resolve correctly on a real call.  
To get deterministic results, use the **Mock Response** option. This bypasses the live Lex invocation and provides consistent test outcomes.

### Queue override
<a name="testing-simulation-action-override-queue"></a>

Modifies queue transfer behavior for testing different queue scenarios or transfer failures.

**Substitute Resource:** Redirects transfers to a different queue.

Configuration options:
+ **Action** – Select "Mock Resource Behavior"
+ **Resource Type** – Queue
+ **Target resource** – Select from dropdown or enter the ARN of the Queue you want to override
+ **Option** – Choose "Substitute Resource"
+ **Substitute resource** – Select from dropdown or provide the ARN of the replacement Queue resource

**Mock Response:** Simulates transfer failures for error path testing.

Configuration options:
+ **Option** – Choose "Mock Response"
+ **Response** – Choose either "Queue at capacity" or "Error"

![Action block configuration showing Queue override with mock response options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/test-action-override-queue.png)
