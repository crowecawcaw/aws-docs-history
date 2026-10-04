

# Notify configurations
<a name="nx-features-notify-config"></a>

A Notify configuration is the central resource for Notify. It defines your display name, use case, enabled channels, enabled countries, and optional settings such as a default template and an associated phone pool. You send templated SMS and voice code-verification messages against a Notify configuration without provisioning phone numbers or navigating carrier registration; AWS End User Messaging selects an appropriate identity and pre-approved template for you.

A configuration has the following properties: **Display name** (up to 15 characters, automatically reviewed for disallowed content), **Use case** (`CODE_VERIFICATION`), **Enabled channels** (`SMS`, `VOICE`, or both), **Enabled countries** (depends on your tier), an optional **Default template** and **Associated pool**, a **Tier** (`BASIC` or `ADVANCED`), **Deletion protection**, and tags. Its **Status** is `PENDING`, `ACTIVE`, `REJECTED`, or `REQUIRES_VERIFICATION`; you can send messages only when the status is `ACTIVE`.

For the guided setup walkthrough and for sending messages at scale, see the Setup Notify chapter.

**Topics**
+ [Create a Notify configuration](nx-features-notify-config-create.md)
+ [View Notify configurations](nx-features-notify-config-view.md)
+ [Update a Notify configuration](nx-features-notify-config-update.md)
+ [Delete a Notify configuration](nx-features-notify-config-delete.md)