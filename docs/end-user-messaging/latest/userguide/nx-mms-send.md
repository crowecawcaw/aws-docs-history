

# Send a message
<a name="nx-mms-send"></a>

You send an MMS message with the `SendMediaMessage` operation, referencing media that you store in Amazon S3. How the service selects an origination identity depends on what you specify in the request. You can send through a phone pool (recommended), directly from a single origination identity, or at the account level.

**Important**  
MMS capabilities are only available in some countries. To confirm that your origination identity is MMS capable, check the phone number status. For country availability, see [Country support](nx-mms-scale-country-support.md).

## API operations
<a name="nx-mms-send-operations"></a>

Use the following API operation to send MMS messages.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendMediaMessage` | Sends an MMS message with media stored in Amazon S3, or a text-only message. | All outbound MMS. | 

## Types of send
<a name="nx-mms-send-types"></a>

AWS End User Messaging supports three ways to send an MMS message. Each one determines how the service selects the origination identity for your message.


**Types of send**  

| Type | How it works | When to use | 
| --- | --- | --- | 
| Pool-based (recommended) | Specify a pool ID as the origination identity. The service selects the best identity from the pool. | All use cases. Managed selection and compliance-safe routing. | 
| Direct | Specify a single origination identity, such as a phone number. | You want to send from one specific identity. | 
| Account-level | Omit the origination identity. The service selects from the identities in your account. | Simple single-use-case setups. Not recommended when the account has numbers for multiple use cases. | 

For full detail and code examples, see [Outbound messaging](nx-mms-send-outbound.md).

## In this section
<a name="nx-mms-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-mms-send-outbound.md) | Send MMS messages with the pool-based, direct, and account-level sending patterns, including the media storage requirements and a code example. | 

**Inbound messaging**



|  |  | 
| --- |--- |
| [Inbound messaging](nx-mms-send-inbound.md) | Understand inbound behavior for MMS numbers, which receive responses as inbound SMS. | 