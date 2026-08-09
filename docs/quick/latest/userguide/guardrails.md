# AI guardrails in Amazon Quick

Amazon Quick takes a defense-in-depth approach to help keep chat interactions safe and
responsible in the Amazon Quick web experience. Multiple safety layers work together,
each addressing different risks at different points in an interaction. No single layer is
designed to catch every risk on its own.

Usage of Amazon Quick AI features is subject to the [AWS Responsible AI
Policy](https://aws.amazon.com/ai/responsible-ai/policy/ "https://aws.amazon.com/ai/responsible-ai/policy/") on the AWS website.

The following topics describe how these controls work and how to configure
them.

###### Topics

- [How AI safety controls work together](#guardrails-how-controls-work-together "#guardrails-how-controls-work-together")
- [Blocked words and phrases](#guardrails-blocked-phrases "#guardrails-blocked-phrases")

## How AI safety controls work together

Amazon Quick uses the following controls together:

- **Built-in safety screening** – Amazon
  Bedrock Guardrails and Quick safeguards screen user requests for
  harmful content. This includes hate speech, insults, sexual content, violence,
  and misconduct. These checks also assess user requests for prompt attacks.
- **Prompt-level safety instructions** –
  Quick instructs the model to promote responsible behavior, resist
  attempts to override safety settings, and avoid exposing internal system
  information.
- **Access and permission controls** –
  Identity, data-access, and action-permission controls limit what data and
  operations are available during an interaction. These limits match the
  signed-in person's permissions. For more information about identity and
  permissions, see [Identity and access management in Quick](identity.md "identity.md") and [Custom permissions](custom-permissions.md "custom-permissions.md").
- **Administrator-configured controls** –
  You can set up blocked words and phrases for chat interactions in
  the Amazon Quick web experience.

These controls help reduce risk. However, they do not replace your responsibility to
configure access, permissions, agents, flows, and data sources for your use
case.

## Blocked words and phrases

You can block up to 50 words or phrases in chat interactions in the
Amazon Quick web experience. This applies to chat agents and flows. Each entry can
contain up to 36 characters. Quick checks both user requests and generated
responses for these phrases. Quick doesn't block any words or phrases by
default.

### Add blocked words and phrases

Use the following procedure to add blocked words and phrases for chat agents and
flows in the Amazon Quick web experience.

###### To add blocked words and phrases

1. Sign in to Quick and choose **Manage
   Quick**.
2. From the navigation pane, choose **Customization**, and
   then choose **Chat agent customization**.
3. In **Chat agent customization**, under
   **Guardrails and safety controls**, choose
   **Add** to add blocked words and phrases. You can add up to
   50 words and phrases. Each entry can contain up to 36 characters.

### Edit blocked words and phrases

Use the following procedure to add or remove blocked words and phrases for chat
agents and flows in the Amazon Quick web experience.

###### To edit blocked words and phrases

1. Sign in to Quick and choose **Manage
   Quick**.
2. From the navigation pane, choose **Customization**, and
   then choose **Chat agent customization**.
3. In **Chat agent customization**, under
   **Guardrails and safety controls**, choose
   **Remove** to remove existing entries, or choose
   **Add** to add entries. You can add up to 50 words and
   phrases. Each entry can contain up to 36 characters.
