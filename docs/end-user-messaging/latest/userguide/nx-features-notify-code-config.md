

# Notify code configurations
<a name="nx-features-notify-code-config"></a>

A notify code configuration is a reusable one-time passcode (OTP) policy and message-template set that you apply when you send verifications. It defines how a passcode is generated — the code type, length, validity period, and maximum number of attempts — and holds per-channel templates for the text, voice, and WhatsApp channels. You define the rules once and reuse the configuration across any Notify configuration; any policy field you leave blank uses the service default at send time.

The verification runtime is a two-step flow: send a passcode to a recipient, then validate the passcode the recipient submits. A caller-supplied reference identifier binds a send to its later validate. The passcode policy is captured at send time, so updating a configuration does not affect verifications that are already in progress. You can protect a configuration from deletion with deletion protection.

**Topics**
+ [Create a notify code configuration](nx-features-notify-code-config-create.md)
+ [Get a notify code configuration](nx-features-notify-code-config-get.md)
+ [List notify code configurations](nx-features-notify-code-config-list.md)
+ [Update a notify code configuration](nx-features-notify-code-config-update.md)
+ [Delete a notify code configuration](nx-features-notify-code-config-delete.md)
+ [Send a passcode](nx-features-notify-code-config-send.md)
+ [Validate a passcode](nx-features-notify-code-config-validate.md)