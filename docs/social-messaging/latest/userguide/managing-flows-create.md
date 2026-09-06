

# Creating and editing WhatsApp Flows
<a name="managing-flows-create"></a>

You can create a WhatsApp Flow using the AWS End User Messaging Social console or the AWS End User Messaging Social API. When you create a Flow, it is placed in DRAFT status. You can optionally provide a Flow JSON definition at creation time, or add it later using the update assets operation.

## Creating a Flow (console)
<a name="managing-flows-create-console"></a>

1. Open the AWS End User Messaging Social console at [https://console.aws.amazon.com/social-messaging/](https://console.aws.amazon.com/social-messaging/).

1. Choose **Business account**, and then choose a WABA.

1. Choose the **Flows** tab.

1. Choose **Create flow**.

1. For **Flow name**, enter a unique name for your Flow. Flow names must be unique within the WABA (maximum 200 characters).

1. For **Category**, select one or more categories that describe the business purpose of your Flow. At least one category is required. Available categories are:
   + Sign Up
   + Sign In
   + Appointment Booking
   + Lead Generation
   + Contact Us
   + Customer Support
   + Survey
   + Shopping
   + Other

1. For **Template**, choose a pre-built template to start from, or choose **Default** to start with a blank Flow. The following templates are available without an endpoint:
   + **Default** — A blank starting template
   + **Collect purchase interest** — Collect information from potential buyers
   + **Get feedback** — Gather customer feedback
   + **Send a survey** — Create a multi-question survey
   + **Customer support** — Collect support request details

1. Choose **Create**.

After you create the Flow, you can edit the Flow JSON to customize the screens and components. The Flow preview on the right side of the page shows a live preview of how your Flow will appear to users in WhatsApp.

## Creating a Flow (API)
<a name="managing-flows-create-api"></a>

Use the `CreateWhatsAppFlow` API to create a new Flow. The following example uses the AWS CLI to create a Flow with a name and category:

```
aws socialmessaging create-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-name "{{my_lead_generation_form}}" \
    --categories '["LEAD_GENERATION"]'
```

The response includes the Flow ID assigned by Meta:

```
{
    "flowId": "{FLOW_ID}",
    "validationErrors": []
}
```

You can also provide a Flow JSON definition at creation time and publish immediately:

```
aws socialmessaging create-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-name "{{appointment_booking}}" \
    --categories '["APPOINTMENT_BOOKING"]' \
    --flow-json fileb://{{flow.json}} \
    --publish
```

**Note**  
If you include `--publish`, the Flow JSON must be valid and pass Meta's validation. If there are validation errors, the Flow is created in DRAFT status and the errors are returned in the `validationErrors` field.

To clone an existing Flow within the same WABA:

```
aws socialmessaging create-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-name "{{lead_form_v2}}" \
    --categories '["LEAD_GENERATION"]' \
    --clone-flow-id {{{FLOW_ID}}}
```

## Updating a Flow
<a name="managing-flows-update"></a>

There are two types of updates you can make to a Flow:
+ **Update metadata** — Change the Flow name or categories using `UpdateWhatsAppFlow`.
+ **Update assets** — Change the Flow JSON definition using `UpdateWhatsAppFlowAssets`.

**Important**  
Updating a published Flow's assets reverts its status to DRAFT. You must re-publish the Flow for it to be available for use in messages.

The following example updates a Flow's name:

```
aws socialmessaging update-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}} \
    --flow-name "{{updated_lead_form}}"
```

The following example updates a Flow's JSON definition:

```
aws socialmessaging update-whatsapp-flow-assets \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}} \
    --flow-json fileb://{{updated_flow.json}}
```

If the Flow JSON contains validation errors, they are returned in the response. You must fix these errors before you can publish the Flow.

## Listing and viewing Flows
<a name="managing-flows-list"></a>

Use `ListWhatsAppFlows` to see all Flows for a WABA, and `GetWhatsAppFlow` to retrieve details about a specific Flow.

List all Flows:

```
aws socialmessaging list-whatsapp-flows \
    --id {{{WABA_ID}}}
```

Get details for a specific Flow:

```
aws socialmessaging get-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

The `GetWhatsAppFlow` response includes the Flow status, categories, validation errors, JSON version, preview information, and health status.

To retrieve the Flow JSON definition (assets), use `ListWhatsAppFlowAssets`:

```
aws socialmessaging list-whatsapp-flow-assets \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

The response includes a presigned download URL for the Flow JSON file. The URL expires after a short period. No additional authentication is needed to download the file from the URL.

## Deleting a Flow
<a name="managing-flows-delete"></a>

You can only delete Flows that are in DRAFT status. Published or deprecated Flows cannot be deleted.

To delete a Flow using the console, select the Flow on the **Flows** tab and choose **Delete**.

To delete a Flow using the API:

```
aws socialmessaging delete-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

**Warning**  
Deleting a Flow is permanent and cannot be undone.