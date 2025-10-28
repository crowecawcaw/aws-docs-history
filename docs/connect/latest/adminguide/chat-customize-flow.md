# Customize chat flow experiences in Amazon Connect by

integrating custom participants

You can integrate other solutions, such as bots, with Amazon Connect chat to create customized chat
flow experiences.

Following is an overview of how you can customize your chat flow experience. Implement
these steps for each chat segment after the chat conversation is started. We recommend
adding an [AWS Lambda
function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block to call the APIs in your chat
flow.

###### Important

Add a [Play prompt](play.md "play.md") block before a [AWS Lambda
function](invoke-lambda-function-block.md "invoke-lambda-function-block.md") block. This is required only
when an **Invoke AWS Lambda** block is the first block in your
inbound chat flow.

1.  [Enable real-time streaming of chat
    messages](chat-message-streaming.md "chat-message-streaming.md").
2.  Call the Amazon Connect [CreateParticipant](../APIReference/API_CreateParticipant.md "../APIReference/API_CreateParticipant.md") API to add a custom participant
    (`ParticipantRole` = `CUSTOM_BOT`) to the chat
    contact.
    1. For information about how to create the SDK client for calling Amazon Connect APIs,
       see the following topics:
       - [Class AmazonConnectClientBuilder](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/connect/AmazonConnectClientBuilder.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/services/connect/AmazonConnectClientBuilder.md")
       - [Creating Service Clients](../../../sdk-for-java/v1/developer-guide/creating-clients.md "../../../sdk-for-java/v1/developer-guide/creating-clients.md")

    2. Keep the `ParticipantToken` that is obtained from [CreateParticipant](../APIReference/API_CreateParticipant.md "../APIReference/API_CreateParticipant.md") to call [CreateParticipantConnection](../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md "../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md").
       `CreateParticipantConnection` returns a
       `ConnectionToken`, which you can use to call other Amazon Connect
       Participant APIs.

    When calling [CreateParticipantConnection](../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md "../../../connect-participant/latest/APIReference/API_CreateParticipantConnection.md") to create a connection for a custom
    participant:

        * Set `ConnectParticipant` to `True` to mark
         the custom participant as connected for message streaming.
        * Pass `Type` as `CONNECTION_CREDENTIALS` to
         call the subsequent Amazon Connect Participant Service APIs.
        * `CreateParticipantConnection` should be called within
         15 seconds of calling `CreateParticipant`.

3.  After the participant is added to the contact, they can exchange messages with the
    customer by using Amazon Connect Participant Service APIs.
4.  To disconnect the participant, call the [DisconnectParticipant](../../../connect-participant/latest/APIReference/API_DisconnectParticipant.md "../../../connect-participant/latest/APIReference/API_DisconnectParticipant.md") API.

###### Note

- A custom participant cannot be added to a chat when an agent or Amazon Lex bot is
  already present on the contact.
- A custom participant will be disconnected when an agent or Amazon Lex bot joins a
  contact.
- Only one custom participant can be present on a contact.
- A custom participant is not permitted to access attachments a customer may upload.
  We recommend configuring how long a custom participant can chat with a contact:

- Set the **Timeout** property on the [Wait](wait.md "wait.md") block for the `ParticipantRole` =
  `CUSTOM_BOT`.
- If the custom bot participant is not disconnected before the timeout, then the
  contact is routed down the **Time Expired** branch. This allows you
  to decide which block to run next to resolve the customer's query.

###### Note

If a contact is routed down the **Time Expired** branch, they are not
disconnected from the contact. You must call the [DisconnectParticipant](../../../connect-participant/latest/APIReference/API_DisconnectParticipant.md "../../../connect-participant/latest/APIReference/API_DisconnectParticipant.md") API to disconnect the participant.

## Activate timers for customers who are

joined to a custom participant

You can activate timers on customers who are joined to custom participants, such as
custom bots. This enables you to detect when a customer stops responding so you can then
terminate that bot conversation, and perform the next step in the flow. By terminating
idle participants, you can reduce the number of open chats where there is a
non-responsive customer engaged with a custom participant.

Perform the following steps to integrate an Idle Participant Custom Bot Extension and
optionally set custom timer values. These steps assume that the you already use the
custom participant feature for chat.

1. Before the custom participant joins the chat, invoke the [UpdateParticipantRoleConfig](../APIReference/API_UpdateParticipantRoleConfig.md "../APIReference/API_UpdateParticipantRoleConfig.md") API for the customer.
   1. Timers activate only for the customer. Custom participants do not have idle participant or auto-disconnect timers.
   2. You can choose the method for invoking the API.
   3. Timer values configured in this step persist for the life of the chat.
      If you want different timer values for the **customer and agent interaction**, see Step 2.
   4. If your client is already set up this way, you don't need to take any
      other action to integrate your custom participant.

2. (Optional) To configure timers and timer values that are different during the
   **customer and agent interaction** than during
   the **customer and custom participant interaction**:
   - Before the agent joins the chat, invoke the [UpdateParticipantRoleConfig](../APIReference/API_UpdateParticipantRoleConfig.md "../APIReference/API_UpdateParticipantRoleConfig.md") API again with the
     configurations you want.

For more information about chat timers, see [Set up chat timeouts for chat participants](setup-chat-timeouts.md "setup-chat-timeouts.md").

### Starting timers

A timer begins for the customer after the custom participant establishes a
connection to them using the [CreateParticipantConnection](../APIReference/API_connect-participant_CreateParticipantConnection.md "../APIReference/API_connect-participant_CreateParticipantConnection.md") API.

### What happens when non-compatible

participants join a chat with a custom participant

Following is what happens when an agent or Lex bot participant joins a chat
with a custom participant, and they are non-compatible
participants:

1. The custom participant is automatically disconnected from the chat.
2. All previously active timers are terminated and new timers are created
   for the connected participants (if timers are configured).
3. Each new timer is also updated with the latest configuration (if
   needed). This effectively establishes a new "Idle session" for the new
   set of active participants on the chat.

### Interaction with the Wait block

timer

The idle timer does not impact how the [Wait](wait.md "wait.md") block works.

The **Wait** block timer that starts
when the chat contact enters a **Wait** block continues to work. If the **Wait** block timer expires, the contact
resumes the flow and is routed down the **Time Expired**
branch, regardless of whether any idle participant timers are active.

## Troubleshooting tips

- `ResourceNotFoundException`:

If you get a `ResourceNotFoundException` for the custom participant when
calling the `CreateParticipantConnection` API, check whether the
`CreateParticipantConnection` API was called within 15 seconds of
`CreateParticipant` API.

- `AccessDeniedException`:

If you get an `AccessDeniedException` error and the participant role is a CUSTOM_BOT,
it indicates the bot is trying to access attachments. The participant role of CUSTOM_BOT is not permitted to
access attachments that customers upload.
