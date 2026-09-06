

# Publishing, deprecating, and previewing WhatsApp Flows
<a name="managing-flows-publish"></a>

## Publishing a Flow
<a name="managing-flows-publish-flow"></a>

Publishing a Flow makes it available for use in template messages. Before you can publish a Flow, it must meet the following requirements:
+ The Flow must be in DRAFT status.
+ The Flow must have a valid Flow JSON definition with no validation errors.
+ The Flow JSON must pass Meta's validation checks.

**Important**  
Publishing a Flow is irreversible. Once published, a Flow cannot be reverted to DRAFT directly. If you need to edit a published Flow, update its assets using `UpdateWhatsAppFlowAssets`, which reverts the Flow to DRAFT status. You must then re-publish the Flow.

To publish a Flow using the API:

```
aws socialmessaging publish-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

If the Flow has validation errors, the publish operation fails. Use `GetWhatsAppFlow` to view validation errors and fix them before retrying.

## Deprecating a Flow
<a name="managing-flows-deprecate-flow"></a>

Deprecating a Flow marks it as no longer recommended for use. Only Flows in PUBLISHED status can be deprecated.

**Important**  
Deprecating a Flow is irreversible. Deprecated Flows cannot be reverted to PUBLISHED or DRAFT status.

To deprecate a Flow using the API:

```
aws socialmessaging deprecate-whatsapp-flow \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

## Previewing a Flow
<a name="managing-flows-preview"></a>

You can generate a web preview URL to test a Flow before publishing. Preview URLs expire after 30 days and can be shared with stakeholders for review. The preview URL opens a simulation of the Flow as it would appear to users in WhatsApp.

To generate a preview URL using the API:

```
aws socialmessaging get-whatsapp-flow-preview \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}}
```

The response includes the preview URL and its expiration timestamp:

```
{
    "flowId": "{FLOW_ID}",
    "preview": {
        "previewUrl": "https://business.facebook.com/wa/manage/flows/{FLOW_ID}/preview/?token=...",
        "expiresAt": "2026-07-01T23:46:55+0000"
    }
}
```

To force generation of a new preview URL (for example, if the previous URL was shared and you want a fresh URL with a new expiration), use the `--invalidate` parameter:

```
aws socialmessaging get-whatsapp-flow-preview \
    --id {{{WABA_ID}}} \
    --flow-id {{{FLOW_ID}}} \
    --invalidate
```