**End of support notice**: On February
20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will
no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more
information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/ "https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/"). **Note:** This does not impact the
availability of the [Amazon Chime SDK
service](https://aws.amazon.com/chime/chime-sdk/ "https://aws.amazon.com/chime/chime-sdk/").

# Creating webhooks for Amazon Chime

Webhooks allow web applications to communicate with each other in real time. Typically, webhooks send notifications when an action occurs. For example, say you run an online shopping site.
Webhooks can notify you when a customer adds items to a shopping cart, pays for an order, or sends a comment. Webhooks don't need as much programming as traditional applications, and they don't
use as much processing power. Without a webhook, a program has to to poll for data frequently in order to get it in real time. With a webhook, the sending application posts the data immediately.

Incoming webhooks that you create can programmatically send messages to Amazon Chime chat rooms.
For example, a webhook can notify a customer service team about the creation of a new
high-priority ticket, and add a link to the ticket in the chat room.

Webhooks messages can be formatted with markdown and can include emojis. HTTP links and
email addresses render as active links. Messages can also include @All and @Present
annotations to alert all members and present members of a chat room, respectively. To
directly @mention a chat room participant, use their alias or full email address. For
example, @`alias` or @`alias@domain.com`.

Webhooks can only be part of a chat room and can't be shared. Amazon Chime chat room administrators can add up to 10 webhooks for each chat room.

After you create a webhook, you can integrate it with an Amazon Chime chat room, as shown in the
following procedure.

###### To integrate a webhook with a chat room

1.  Get the webhook URL from the chat room administrator. For more information,
    see [Adding webhooks to a chat room](../ug/chat-webhooks.md "../ug/chat-webhooks.md") in the _Amazon Chime User Guide_.
2.  Use the webhook URL in the script or application that you created to send messages
    to the chat room:

        1. The URL accepts an HTTP POST request.
        2. Amazon Chime webhooks accept a JSON payload with a single key
         **Content**. The following is a sample curl command
         with a sample payload:



        ```
        curl -X POST "<Insert your webhook URL here>" -H "Content-Type:application/json" --data '{"Content":"Message Body emoji test: :) :+1: link test: http://sample.com email test: marymajor@example.com All member callout: @All All Present member callout: @Present"}'
        ```

        The following is a sample PowerShell command for Windows users:



        ```
        Invoke-WebRequest -Uri '<Insert your webhook URL here>' -Method 'Post' -ContentType 'application/JSON' -Body '{"Content":"Message Body emoji test: :) :+1: link test: http://sample.com email test: marymajor@example.com All member callout: @All All Present member callout: @Present"}'
        ```

    After the external program sends the HTTP POST to the webhook URL, the server
    validates that the webhook is valid and has an assigned chat room. The webhook appears in the chat room roster with a webhook icon next to its name. Chat room messages sent by the webhook appear in the
    chat room under the webhook name followed by **(Webhook)**.

###### Note

CORS is not currently enabled for webhooks.

## Troubleshooting webhook errors

The following is a list of webhook-related errors:

- The incoming webhook rate limit for each webhook is 1 TPS per chat room.
  Throttling results in an HTTP 429 error.
- Messages posted by a webhook must be 4 KB or less. A bigger message payload
  results in an HTTP 413 error.
- Messages posted by a webhook with @All and @Present annotations work only
  for chat rooms with 50 or fewer members. More than 50 members results in an
  HTTP 400 error.
- If the webhook URL is regenerated, using the old URL results in an HTTP
  404 error.
- If the webhook in a room is deleted, using the old URL results in an HTTP
  404 error.
- Invalid webhook URLs result in HTTP 403 errors.
- If the service is unavailable, the user receives an HTTP 503 error in the
  response.
