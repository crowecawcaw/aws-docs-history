# Response customization

settings

When you create an Amazon Q Business application, Amazon Q Business
applies its default response settings to your application. You can choose to customize
these default settings to meet your particular use case.

When configuring custom response settings, keep the following best practices in
mind:

- Keep instructions clear and specific
- Avoid contradictory directives
- Use positive instructions whenever possible
- Use negative prompts only to prevent undesirable output or biased
  responses
- Maintain consistency across related instructions
- Add relevant, diverse, and real-world scenario-based examples
- Don't include sensitive or personally identifiable information (PII)

###### Note

- Response customization settings don't overwrite any [admin controls and guardrails](guardrails.md "guardrails.md") already applied to your
  application.
- In cases where custom response settings can't be applied to a specific
  response, Amazon Q Business will apply it's default response
  settings.
- To optimize performance and accuracy, Amazon Q Business may
  pre-process custom prompts before using them to generate responses.
  When customizing responses in Amazon Q Business, you can configure the following
  settings:

###### Response customization settings

- [Identity](#identity "#identity")
- [Perspective](#perspective "#perspective")
- [Target audience](#target-audience "#target-audience")
- [Output style](#output-style "#output-style")
- [Tone](#tone "#tone")
- [Response length](#response-length "#response-length")
- [Custom instructions](#custom-instructions "#custom-instructions")

## Identity

Define the persona or identity that Amazon Q Business should adopt when
responding to users. This allows you to customize the assistant's character, role,
or representation within your organization.

When configuring identity, consider the following best practices:

- Keep character/persona descriptions consistent
- Define clear boundaries of expertise
- Specify relevant background information
- Don't create harmful or discriminatory personas
- Avoid mixing multiple conflicting identities
- Don't impersonate real individuals or protected entities

## Perspective

Choose the point of view from which Amazon Q Business generates responses,
such as first-person, second-person, or third-person perspective. This affects how
information is presented to users and can help establish the right relationship
between the assistant and users.

When configuring perspective, consider the following best practices:

- Define clear view points or approaches
- Specify professional or industry perspectives, when relevant
- Maintain ethical boundaries
- Don't request biased or discriminatory perspectives
- Avoid mixing conflicting viewpoints
- Don't ask for harmful or dangerous perspectives

## Target audience

Define the intended audience for responses, allowing Amazon Q Business to
tailor its language, terminology, and explanations appropriately. You can configure
responses for technical experts, general users, or specific custom roles within your
organization.

When configuring target audience, consider the following best practices:

- Clearly define intended audience
- Specify technical level, if relevant
- Include age-appropriate considerations
- Don't define inappropriate audiences
- Don't mix incompatible audience levels

## Output style

Specify the formatting and structural style of responses, such as bullet points,
paragraphs, step-by-step instructions, or other organizational formats that enhance
readability and comprehension.

When configuring output style, consider the following best practices:

- Specify preferred formatting clearly
- Define structure preferences
- Include any special markers or indicators needed
- Don't mix incompatible formatting styles
- Don't request harmful or inappropriate content
- Ensure your prompt instructions respect safety and security

## Tone

Control the emotional tone and communication style of responses—such as
formal, casual, technical, friendly, or professional—to align with your
organization's communication standards and user expectations.

When configuring tone, consider the following best practices:

- Specify clear mood/attitude
- Match tone to purpose and audience
- Maintain consistency
- Don't mix conflicting tones
- Don't ignore context when setting tone
- Don't request inappropriate or offensive tones

## Response length

Control whether responses are concise and brief or more detailed and
comprehensive. This setting helps ensure that users receive information at the
appropriate level of detail for their needs.

When configuring response length, consider the following best practices:

- Specify clear length preferences (brief, detailed, for example)
- Define word/character limits if needed
- Match content type (social media post, for example) to response length
  (150 words, for example)
- Don't give contradicting length requirements
- Don't request unreasonable lengths

## Custom instructions

Provide specific guidance for how Amazon Q Business should respond in
particular scenarios or to certain types of queries, enabling fine-grained control
over response generation.

When configuring custom instructions, consider the following best
practices:

- Provide clear, actionable directives
- Keep instructions focused on one aspect at a time
- Use specific examples when needed
- Avoid contradicting instructions (For example: "Be formal and
  casual")
- Don't include harmful or toxic content
- Don't add too many instructions
