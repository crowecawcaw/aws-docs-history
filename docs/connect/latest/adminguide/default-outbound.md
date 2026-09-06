

# Default outbound flow in Connect Customer: "This call is not being recorded"
<a name="default-outbound"></a>

**Important**  
Before using the **Send message** block in an outbound flow, see [Important information about using the Send message block in outbound flows](send-message.md#send-message-outboundflow-important) for recommended safeguards you should implement.

This flow is an outbound whisper that manages what the customer experiences as part of an outbound call, before being connected with an agent. 

1. It starts with an optional **Set recording behavior** block. Then a prompt plays the following message: 

   *This call is not being recorded.*

1. The flow ends.

1. The customer remains in the system (on the call) after the flows ends. 

When thinking about how to design an outbound flow, keep in mind how an outbound flow works: 
+ Before the call is made, all the blocks before the first **Play prompt** are run. 
+ After the customer picks up, the first **Play prompt** and all the blocks after it are run. 

For instructions about how to override and change a default flow, see [Change a default flow in your Connect Customer contact center](change-default-contact-flow.md).

**Tip**  
Wondering if a default flow has been changed? Use [flow version control](flow-version-control.md) to view the original version of the flow. 