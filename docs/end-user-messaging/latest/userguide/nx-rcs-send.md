

# Send a message
<a name="nx-rcs-send"></a>

AWS End User Messaging uses the same `SendTextMessage` API operation for both RCS and SMS delivery. How the service routes your message depends on the origination identity that you specify in the request. To send rich RCS content such as rich cards, carousels, media files, and interactive suggestions, use the `SendRcsMessage` operation instead. You can send through a phone pool (recommended), directly through an AWS RCS Agent ARN, or at the account level.

## API operations
<a name="nx-rcs-send-operations"></a>

Use the following API operations to send RCS messages.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendTextMessage` | Sends a message that the service routes to RCS or SMS based on the origination identity. | Standard text, with SMS fallback. | 
| `SendRcsMessage` | Sends rich RCS content such as rich cards, carousels, media, and interactive suggestions. | Rich RCS experiences. | 

## Types of send
<a name="nx-rcs-send-types"></a>

AWS End User Messaging supports three ways to send a message. Each one determines how the service selects an origination identity and whether automatic SMS fallback is available.


**Types of send**  

| Type | How it works | When to use | 
| --- | --- | --- | 
| Pool-based (recommended) | Specify a pool ID as the origination identity. The service selects the best identity from the pool and provides automatic SMS fallback. | All use cases. Managed selection and compliance-safe routing with automatic SMS fallback. | 
| Direct | Specify an AWS RCS Agent ARN. The message is sent via RCS only, with no SMS fallback. | RCS-or-nothing use cases, or when you manage fallback yourself. | 
| Account-level | Omit the origination identity. The service selects from the identities in your account. | Simple single-use-case setups. Not recommended when the account has numbers for multiple use cases. | 

For full detail and code examples, see [Outbound messaging](nx-rcs-send-outbound.md).

## In this section
<a name="nx-rcs-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-rcs-send-outbound.md) | Send RCS messages with the pool-based, direct, and account-level sending patterns, including code examples. | 

**Inbound messaging**



|  |  | 
| --- |--- |
| [Inbound messaging](nx-rcs-send-inbound.md) | Test and receive inbound (two-way) RCS messages from your customers. | 