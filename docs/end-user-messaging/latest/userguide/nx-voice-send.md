

# Send a message
<a name="nx-voice-send"></a>

You place a voice call with the `SendVoiceMessage` operation. The service uses Amazon Polly to convert text to speech, or plays an audio file that you supply, to the destination phone number. How the service selects an origination identity depends on what you specify in the request. You can send through a phone pool (recommended), directly from a single origination identity, or at the account level.

## API operations
<a name="nx-voice-send-operations"></a>

Use the following API operation to place voice calls.


**API operations**  

| Operation | Description | Use for | 
| --- | --- | --- | 
| `SendVoiceMessage` | Places a voice call that plays text-to-speech or audio you supply. | All outbound voice. | 

## Types of send
<a name="nx-voice-send-types"></a>

AWS End User Messaging supports three ways to place a voice call. Each one determines how the service selects the origination identity for your call.


**Types of send**  

| Type | How it works | When to use | 
| --- | --- | --- | 
| Pool-based (recommended) | Specify a pool ID as the origination identity. The service selects the best identity from the pool. | All use cases. Managed selection and compliance-safe routing. | 
| Direct | Specify a single origination identity, such as a phone number. | You want to send from one specific identity. | 
| Account-level | Omit the origination identity. The service selects from the identities in your account. | Simple single-use-case setups. Not recommended when the account has numbers for multiple use cases. | 

For full detail and code examples, see [Outbound messaging](nx-voice-send-outbound.md).

## In this section
<a name="nx-voice-send-in-section"></a>

**Outbound messaging**



|  |  | 
| --- |--- |
| [Outbound messaging](nx-voice-send-outbound.md) | Place voice calls with the pool-based, direct, and account-level sending patterns, using text-to-speech or audio, including a code example. | 