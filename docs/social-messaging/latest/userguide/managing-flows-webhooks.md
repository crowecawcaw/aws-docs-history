

# Receiving Flow responses and status changes
<a name="managing-flows-webhooks"></a>

When a user completes a Flow or when a Flow's status changes, AWS End User Messaging Social delivers webhook notifications through your existing configured event destination. No additional setup or new event types are required — Flow events are delivered automatically to the same event destination you use for messages and delivery receipts. You must have an event destination enabled to receive these notifications. For more information, see [Add a message and event destination to AWS End User Messaging Social](managing-event-destinations-add.md).

## Flow response messages
<a name="managing-flows-webhooks-response"></a>

When a user completes a Flow, you receive an inbound message with the type `interactive` and the subtype `nfm_reply`. The `response_json` field contains the data submitted by the user as a JSON string.

The following example shows a Flow response webhook payload:

```
{
    "messages": [
        {
            "from": "14085551234",
            "id": "wamid.XXX",
            "timestamp": "1234567890",
            "type": "interactive",
            "interactive": {
                "type": "nfm_reply",
                "nfm_reply": {
                    "response_json": "{\"name\":\"John Doe\",\"email\":\"john@example.com\",\"phone\":\"+14085551234\"}",
                    "body": "Sent",
                    "name": "flow"
                }
            }
        }
    ]
}
```

The `response_json` contains key-value pairs corresponding to the form field names defined in your Flow JSON and the values entered by the user. Parse this JSON string to extract the submitted data.

## Flow status change notifications
<a name="managing-flows-webhooks-status"></a>

When Meta changes a Flow's status (for example, from PUBLISHED to BLOCKED), you receive a notification through your event destination. The following example shows a status change payload:

```
{
    "entry": [
        {
            "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
            "changes": [
                {
                    "value": {
                        "event": "FLOW_STATUS_CHANGE",
                        "flow_id": "{FLOW_ID}",
                        "old_status": "PUBLISHED",
                        "new_status": "BLOCKED",
                        "reason": "Policy violation detected"
                    },
                    "field": "flows"
                }
            ]
        }
    ]
}
```

Monitor these status change events to detect when Meta blocks or throttles your Flows so you can take corrective action.

## Flow version expiry warnings
<a name="managing-flows-webhooks-expiry"></a>

Meta sends a warning webhook when the Flow JSON version used by your Flow is approaching its end-of-life date. When a version expires, you cannot send the Flow until you update to a newer version.

```
{
    "entry": [
        {
            "id": "WHATSAPP_BUSINESS_ACCOUNT_ID",
            "changes": [
                {
                    "value": {
                        "event": "FLOW_VERSION_EXPIRY_WARNING",
                        "flow_id": "{FLOW_ID}",
                        "warning": "Your current Flow version will freeze in 21 days. You won't be able to send the Flow after it expires. Please migrate to the recommended version as soon as possible."
                    },
                    "field": "flows"
                }
            ]
        }
    ]
}
```

When you receive this warning, update your Flow JSON to use the recommended version (currently 7.3) by calling `UpdateWhatsAppFlowAssets` with the updated JSON, then re-publish the Flow.