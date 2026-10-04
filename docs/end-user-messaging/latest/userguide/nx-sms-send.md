

# Send a message
<a name="nx-sms-send"></a>

You use the AWS End User Messaging API to send SMS text messages directly from your applications with the `SendTextMessage` operation. How the service selects an origination identity depends on what you specify in the request. You can send through a phone pool (recommended), directly from a single origination identity, or at the account level. You can also set up two-way SMS to receive incoming messages from your customers.

## API operations
<a name="nx-sms-send-operations"></a>

Use the following API operation to send SMS messages.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendTextMessage` | Sends an SMS text message to a destination phone number. | All outbound SMS. | 

## Types of send
<a name="nx-sms-send-types"></a>

AWS End User Messaging supports three ways to send an SMS message. Each one determines how the service selects the origination identity for your message.


**Types of send**  

| Type | How it works | When to use | 
| --- | --- | --- | 
| Pool-based (recommended) | Specify a pool ID as the origination identity. The service selects the best identity from the pool. | All use cases. Managed selection and compliance-safe routing. | 
| Direct | Specify a single origination identity, such as a phone number or sender ID. | You want to send from one specific identity. | 
| Account-level | Omit the origination identity. The service selects from the identities in your account. | Simple single-use-case setups. Not recommended when the account has numbers for multiple use cases. | 

For full detail and code examples, see [Outbound messaging](nx-sms-send-outbound.md).

## In this section
<a name="nx-sms-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-sms-send-outbound.md) | Send SMS messages with the pool-based, direct, and account-level sending patterns, including message parts and code examples. | 

**Inbound messaging**



|  |  | 
| --- |--- |
| [Inbound messaging](nx-sms-send-inbound.md) | Set up two-way SMS to receive incoming messages from your customers. | 