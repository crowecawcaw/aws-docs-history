

# Understanding Flow status
<a name="managing-flows-status"></a>

Each WhatsApp Flow has a status that represents its lifecycle state. The status determines what actions you can take on the Flow.


**Flow status values**  

| Status | Description | Allowed actions | 
| --- | --- | --- | 
| DRAFT | Initial state when a Flow is created. The Flow can be edited and tested but cannot be sent to users. | Update, update assets, publish, delete, preview | 
| PUBLISHED | The Flow is available for use in template messages and can be sent to users. Published Flows cannot be edited directly. | Deprecate, preview. To edit, update assets (which reverts to DRAFT). | 
| DEPRECATED | The Flow is no longer recommended for use. This is an irreversible state. | None (terminal state) | 
| BLOCKED | Meta has blocked the Flow due to integrity or policy violations. | Contact Meta support | 
| THROTTLED | Meta has temporarily throttled the Flow. | Wait for throttling to be lifted | 

**Important**  
Publishing and deprecating a Flow are irreversible operations. Once a Flow is published, you cannot revert it to DRAFT directly. However, updating a published Flow's assets (JSON definition) will revert it to DRAFT status, requiring you to re-publish.

Meta sends a webhook notification each time a Flow's status changes. You receive these notifications through your configured event destination. For more information, see [Receiving Flow responses and status changes](managing-flows-webhooks.md).