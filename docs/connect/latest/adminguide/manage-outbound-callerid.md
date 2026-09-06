

# Manage caller ID for outbound calls
<a name="manage-outbound-callerid"></a>

When agents transfer calls or initiate outbound calls, your instance configuration determines which caller ID displays to the recipient. The following sections explain where caller ID comes from in each scenario and how to set the number you want to display to recipients.

You can only use phone numbers that you've claimed or ported to your Connect Customer instance as your outbound caller ID. In some cases, you can request approval to use an external number. For more information, see [Set up outbound caller ID](queues-callerid.md).

**Topics**
+ [Where caller ID comes from](#callerid-transfer-sources)
+ [Set caller ID for direct outbound calls and callbacks](#callerid-direct-outbound)
+ [Set caller ID for transfers](#callerid-transfers-active)
+ [Set caller ID for redirected calls](#callerid-redirected-calls)
+ [All caller ID configuration points](#callerid-config-reference)

## Where caller ID comes from
<a name="callerid-transfer-sources"></a>

The following table describes where the caller ID originates for each call scenario and whether you can override it with an outbound whisper flow. An outbound whisper flow runs before the recipient answers a call. You can use a [Call phone number](call-phone-number.md) block in this flow to set the caller ID before Connect Customer places the call.


| Scenario | Where the caller ID comes from | Can you override it with a whisper flow? | 
| --- | --- | --- | 
| Direct outbound (agent not on a call) | Outbound queue in the agent's [routing profile](routing-profiles.md) | Yes | 
| Queued callback | Queue associated with the callback | Yes | 
| Transfer through Quick Connect (agent on active call) | Inbound queue that serviced the original call | No | 
| Flow-based transfer ([Transfer to phone number](transfer-to-phone-number.md) block) | Caller ID set explicitly in the block | N/A — you set it directly | 

**Important**  
For transfers through Quick Connect, the caller ID comes from the *inbound* queue that serviced the original call, not the outbound queue or routing profile. If transfers display an unexpected number, check the caller ID that you configured on your inbound queues.

## Set caller ID for direct outbound calls and callbacks
<a name="callerid-direct-outbound"></a>

For direct outbound calls (when the agent is not on an active call) and queued callbacks, you can set the caller ID on the queue or override it with an outbound whisper flow.

### To set caller ID on the queue
<a name="callerid-direct-queue"></a>

1. In the navigation pane, choose **Routing**, **Queues**.

1. Choose the queue to edit.

1. For **Outbound caller ID number**, choose the number you want to display to recipients.

1. Choose **Save**.

### To override caller ID with an outbound whisper flow
<a name="callerid-direct-whisper"></a>

An outbound whisper flow overrides the queue setting for direct outbound calls and callbacks.

1. Create an outbound whisper flow with a [Call phone number](call-phone-number.md) block.

1. In the block, set the caller ID to the number you want displayed to recipients (static or dynamic through contact attributes).

1. Attach the whisper flow to the queue.

The whisper flow caller ID takes priority over the queue setting.

**Note**  
If you haven't configured a caller ID on the queue and haven't attached a whisper flow, direct outbound calls fail with an Invalid outbound configuration error. Either the queue or the whisper flow must supply a caller ID.

## Set caller ID for transfers
<a name="callerid-transfers-active"></a>

For transfers while an agent is on an active call, you can set the caller ID on the inbound queue or use a flow-based transfer for per-destination control.

### To set caller ID on the inbound queue
<a name="callerid-transfer-queue"></a>

Setting the caller ID on the queue is the simplest approach. Every transfer from the queue displays the same number to recipients.

1. In the navigation pane, choose **Routing**, **Queues**.

1. Choose each inbound queue where agents initiate transfers.

1. For **Outbound caller ID number**, choose the number you want to display to transfer recipients.

1. Choose **Save**.

Connect Customer requires a valid caller ID on all outbound calls. Configure caller ID on every queue to ensure reliable delivery.

### To use transfer to queue for per-destination control
<a name="callerid-transfer-flow"></a>

When you need different caller IDs for different transfer destinations, use a transfer-to-queue approach. Create a dedicated queue with a transfer to queue flow that contains a [Transfer to phone number](transfer-to-phone-number.md) block. The block sets the caller ID explicitly for each destination.

1. Create a transfer to queue flow. Add a [Transfer to phone number](transfer-to-phone-number.md) block.

1. In the block, set the **Caller ID number to display** to the number you want the recipient to see.

1. Set the destination phone number.

1. Save and publish the flow.

1. Create a dedicated queue for this transfer destination.

1. Create a *Queue*-type Quick Connect that routes to this queue and uses the transfer to queue flow you created.

When the agent selects this Quick Connect during an active call, Connect Customer routes the call to the dedicated queue, runs the transfer to queue flow, and the [Transfer to phone number](transfer-to-phone-number.md) block places the external call with the caller ID you configured. The caller ID set in the flow block takes priority regardless of what is configured on the queue.

**Important**  
Outbound whisper flows do not control caller ID for transfers that agents initiate through Quick Connect while on an active call. To control caller ID per destination, use the transfer-to-queue approach described in this section.

## Set caller ID for redirected calls
<a name="callerid-redirected-calls"></a>

When you redirect an inbound call to an external number, you must configure a valid caller ID from your instance for the outbound leg. Connect Customer requires a valid caller ID on all outbound calls — you cannot pass through the inbound caller's number because you haven't claimed or ported it to your instance. Configure a caller ID from your instance to ensure reliable delivery.

To set a valid caller ID on redirected calls, do one of the following:
+ Set a valid **Outbound caller ID number** on the queue that handles the redirection.
+ Use a [Transfer to phone number](transfer-to-phone-number.md) block with an explicit caller ID.

## All caller ID configuration points
<a name="callerid-config-reference"></a>

The following table summarizes every location where you can configure caller ID and when each setting applies.


| Configuration point | Location | When it applies | 
| --- | --- | --- | 
| Queue outbound caller ID | Routing, Queues, edit the queue | Baseline for all scenarios | 
| [Call phone number](call-phone-number.md) block (whisper flow) | Outbound whisper flow | Overrides queue on direct outbound calls and callbacks | 
| [Transfer to phone number](transfer-to-phone-number.md) block | Contact flow | Sets caller ID explicitly on flow-based transfers | 
| sourcePhoneNumber (API) | [StartOutboundVoiceContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundVoiceContact.html) API | Overrides queue on API-initiated calls | 
| Dynamic attribute | Set contact attributes and [Call phone number](call-phone-number.md) block | Dynamic override in flows | 