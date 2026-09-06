

# Select a From email address
<a name="agent-select-from-email"></a>

When agents reply to or initiate emails, they can select which From (system) email address to use. This is helpful when agents support multiple brands, departments, or business units within the same contact center.

See [Create email addresses](create-email-address1.md) if you do not have email addresses created in your Amazon Connect instance.

## Selecting a From address when replying to inbound emails
<a name="agent-select-from-email-reply"></a>

When an agent replies to an inbound email contact:

1. The **From** address defaults to the original email address that received the customer's email.

1. The agent sees a label indicating **Original email address that received this email contact**.

1. The agent can change to a different address if needed by selecting from the **From** dropdown.

The available email addresses come from the queue that received the contact. The list is ordered as follows:

1. The original email address that received the inbound email (labeled as **Original email address that received this email contact**)

1. The default email address configured on the queue

1. The remaining additional email addresses configured on the queue

![The From address dropdown when replying to an inbound email.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-from-selector-reply.png)


## Selecting a From address when initiating outbound emails
<a name="agent-select-from-email-initiate"></a>

When an agent initiates a new outbound email contact:

1. The **From** address defaults to the default email address configured on the agent's default outbound queue (specified in their routing profile).

1. The agent can change to a different address by selecting from the **From** dropdown.

The available email addresses come from the default outbound queue configured in the agent's routing profile. The list is ordered as follows:

1. The default email address configured on the default outbound queue

1. The remaining additional email addresses configured on the default outbound queue

![The From address dropdown when initiating an outbound email.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-from-selector-initiate.png)


## Using the From address selector
<a name="agent-select-from-email-using"></a>

To select a From email address:

1. Choose the **From** dropdown to see all available email addresses.

1. Use the search box to quickly find the right address.

1. Review the information displayed for each address:
   + Friendly sender name (if configured)
   + Email address
   + Description (if configured)

   For example: `Support Team <support@example.com> - For customer support inquiries`

1. Select the appropriate address for your use case.

![The From address selector showing the search box, and email addresses displayed with friendly sender names.](http://docs.aws.amazon.com/connect/latest/adminguide/images/email-from-selector-search.png)


**Note**  
The list of available email addresses respects your security permissions. If [tag-based access control (TBAC)]() is configured, you only see email addresses that match your assigned tags.

## Example use cases
<a name="agent-select-from-email-examples"></a>

The following examples show when agents might need to select a different From email address:
+ **Multi-brand support**: An agent handles contacts for both an insurance division and a retail division. When sending a follow-up email, the agent selects the appropriate brand email address.
+ **BPO scenario**: A BPO agent supporting multiple client brands receives a call from AnyCompany Brand. When initiating a follow-up email, the agent selects the AnyCompany Brand email address.
+ **Blended agents**: An agent on a voice call needs to send follow-up instructions by email. The agent initiates an outbound email and selects the correct department email address.
+ **Email routing correction**: An agent receives an email that was sent to sales@example.com but should have gone to support@example.com. The agent selects support@example.com as the From address when replying.