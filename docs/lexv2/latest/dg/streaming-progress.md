# Configuring fulfillment progress

updates for your Lex V2 bot

When the fulfillment Lambda function for an intent is called, the bot
doesn't send a response until the function completes. If the Lambda
function takes more than a few seconds to complete, the user may think
that the bot is unresponsive. To address this, you can configure your
bot to send updates to the user while the fulfillment Lambda function is
running so that the user knows that the bot is still working on their
request.

When you add fulfillment updates to an intent, the bot responds at the
start of fulfillment and periodically while fulfillment is in progress.
When you configure the start response, you can specify a delay before
the bot sends the response. With this, you can support cases where the
fulfillment doesn't finish relatively quickly. When you configure an
update response, you specify the frequency that you want the updates
sent. You also configure a timeout to limit the time that the
fulfillment function has to run.

You can also add post-fulfillment responses to a bot. This enables the
bot to send a different response depending on whether fulfillment
succeeds, fails, or times out.

Fulfillment updates are used only when interacting with a bot using
the [StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md") operation. You can
use the post-fulfillment update when interacting with the bot using the
[StartConversation](../APIReference/API_runtime_StartConversation.md "../APIReference/API_runtime_StartConversation.md"),
[RecognizeText](../APIReference/API_runtime_RecognizeText.md "../APIReference/API_runtime_RecognizeText.md"), and
[RecognizeUtterance](../APIReference/API_runtime_RecognizeUtterance.md "../APIReference/API_runtime_RecognizeUtterance.md") operations

## Fulfillment updates

Fulfillment updates are sent while your Lambda function is
fulfilling an intent. When you turn on fulfillment updates, you
provide a start response that is sent at the beginning of
fulfillment and an update response that is sent periodically while
fulfillment is in progress.

When you specify an update response, you also specify a timeout
that determines how long the fulfillment function can run. You can
specify a timeout length of up to 15 minutes (900 seconds).

If you turn off fulfillment updates by setting `active`
to false in the console or using the [CreateIntent](../APIReference/API_CreateIntent.md "../APIReference/API_CreateIntent.md") or
[UpdateIntent](../APIReference/API_UpdateIntent.md "../APIReference/API_UpdateIntent.md") operation, the timeout
specified for the fulfillment updates isn't used and the default
timeout of 30 seconds is used instead.

If the fulfillment function times out, Amazon Lex V2 does one of three
things:

- Post-fulfillment response is configured and active –
  returns the timeout response.
- Post-fulfillment response is configured and not active
  – returns an exception.
- Post-fulfillment response isn't configured – returns
  an exception.

### Start response

Amazon Lex V2 returns the start response when the Lambda fulfillment
function is called during a streaming conversation. It typically
tells the user that fulfilling the intent takes some time and
that they should wait. The start response isn't returned when
you use the `RecognizeText` or
`RecognizeUtterance` operations.

You can specify up to five response messages. Amazon Lex V2 chooses
one of the messages to play to the user.

You can configure a delay between when the Lambda function is
called and when the start response is returned. The start
response isn't returned if the Lambda function completes its work
before the delay is complete.

You can use the `active` toggle in the console or
the [FulfillmentUpdatesSpecification](../APIReference/API_FulfillmentUpdatesSpecification.md "../APIReference/API_FulfillmentUpdatesSpecification.md")
structure to turn the start response on and off. When
`active` is false, the start response isn't
played.

### Update response

Amazon Lex returns the update response periodically during a
streaming conversation while the Lambda fulfillment function is
running. The update response isn't played when you use the
`RecognizeText` or
`RecognizeUtterance` operations. You can
configure how often the update response plays. For example, you
can play an update response every 30 seconds while the
fulfillment function runs to let the user know that the process
is running and that they should continue to wait.

You can specify up to five update messages. Amazon Lex V2 chooses a
message to play to the user. Using multiple messages keeps the
updates from being repetitive.

If the user provides input via voice, DTMF, or text while the
fulfillment Lambda function is running, Amazon Lex V2 returns the update
response to the user.

If the Lambda function completes its work before the first
update period ends, the update response isn't returned.

You can use the `active` toggle in the console or
the [FulfillmentUpdatesSpecification](../APIReference/API_FulfillmentUpdatesSpecification.md "../APIReference/API_FulfillmentUpdatesSpecification.md")
structure to turn the update response on and off. When
`active` is false, the update response isn't
returned.

## Post-fulfillment

response

Amazon Lex V2 returns a post-fulfillment response when the fulfillment
function ends. A post-fulfillment response can be used when
fulfilling any intent, not just when streaming conversations. The
post-fulfillment response lets the user know that the function is
complete and the result.

You can use the `active` toggle in the console or the
[PostFulfillmentStatusSpecification](../APIReference/API_PostFulfillmentStatusSpecification.md "../APIReference/API_PostFulfillmentStatusSpecification.md")
structure to turn the post-fulfillment response on and off. When
`active` is false, the response is not played.

There are three types of post-fulfillment responses:

- **Success** – returned when the fulfillment Lambda
  function completes its work successfully. If
  post-fulfillment responses aren't active. Amazon Lex V2 takes the
  next configured action.
- **Timeout** – returned if the Lambda function doesn't
  complete its work before the configured timeout period
  elapses. If post-fulfillment responses aren't active, Amazon Lex V2
  returns an exception.
- **Failure** – returned when the Lambda function returns
  the status `Failed` in the response or when
  Amazon Lex V2 encounters an error while fulfilling the intent. If
  post-fulfillment responses aren't active, Amazon Lex V2 returns an
  exception.

You can specify up to five messages for each type. Amazon Lex V2 chooses
one of the messages to play to the user.

Unlike fulfillment start and fulfillment update responses, post-fulfillment responses are played back for both streaming and non-streaming conversations.

You also have the option to override these messages by configuring the Lambda function
to return a post-fulfillment message.

###### Note

If the intent has a closing response, it is returned
after the post-fulfillment response.

### Post-fulfillment example for Lex V2

To better understand the post-fulfillment response, let's take, as an example, a `BookTrip` bot, created to help plan a trip, with a `BookFlight` intent, configured with a fulfillment Lambda function that reserves the customer's flight with an airline. Once the slots for `BookFlight` have been elicited, Amazon Lex V2 invokes the fulfillment Lambda function. During this fulfillment process one of the following three results can happen:

- **Success** – The flight is successfully booked.
- **Timeout** – The booking process takes longer than the configured fulfillment Lambda execution time (for example, if the airline cannot be contacted within the allotted time).
- **Failure** – The booking fails for another reason.

You can leverage the post-fulfillment response to provide a more meaningful response to your customers in each of these situations. Examples for each situation are as follows:

- **Success response** – "We were able to successfully book your ticket and have sent you a confirmation email. Please feel free to reach out to us using the contact information provided in that email if you have any questions."
- **Timeout response** – "Due to heavy traffic on our systems, booking your ticket is taking longer than expected. We have your request in our queue and have sent you an email with the reference number corresponding to this request. Once we book the ticket, we will send you a confirmation of the reservation. Please feel free to reach out to us using the contact information provided in that email if you have any questions."

###### Note

If you do not configure a timeout message, throws a 4XX error corresponding to the use case.

- **Failure response** – "Unfortunately, we were unable to book your ticket. We have sent an email with details regarding the issue we encountered while booking your reservation."
