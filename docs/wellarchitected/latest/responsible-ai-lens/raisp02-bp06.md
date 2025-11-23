# RAISP02-BP06 Enable users to customize core AI system

behaviors

Design your system so users can adjust how it works to better fit
their particular requirements and preferences, while keeping those
adjustments within appropriate boundaries for your use case. This
means incorporating features like adjustable output styles, user
preference settings, or options that let users guide how the system
interprets and responds to their requests.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. When adding guardrails to your system, build adjustable
   controls that let users determine how strictly content gets
   filtered. Set up multi-level filtering from low to high for
   different content types and create user roles where
   administrators set baseline policies while end users can
   adjust settings within safe limits. Include feedback systems
   to track how well these guardrail controls work and improve
   them over time.
2. Design interfaces for adjusting output content, style and
   tone. Allow users to adjust inference parameters like
   Temperature, Top P, and Top K for text generation to balance
   between creative and focused outputs. These parameters control
   the output by influencing the token selection process.
   Temperature determines randomness of token selection, with
   higher values producing more creative text and lower values
   resulting in more focused output. Top P (Nucleus Sampling)
   samples tokens whose cumulative probability sums to a given
   threshold, dynamically adjusting the option pool. Top K
   restricts the model's choice to a fixed number of
   highest-probability tokens. Similarly, provide ways to the
   user to adjust response length, format options, and output
   style.
3. Design structured prompting frameworks to enhance user control
   over AI system behavior and outputs. Create system-level
   prompt templates that allow administrators to define AI
   personality, tone, and response boundaries, while enabling end
   users to customize task-specific instructions within safe
   limits. Build prompt libraries with preset configurations for
   common use cases (for example, professional communication,
   creative writing, technical analysis) that users can select
   and modify. Include prompt validation mechanisms to assist
   user-provided prompts align with safety guidelines while
   maintaining the desired level of control over AI responses.
   Design prompt management interfaces that assist users to
   understand prompt effectiveness through clear feedback and
   iterative refinement options.
4. Design tracking mechanisms for control adjustments, system
   responses, user interactions and performance impacts.
5. Create feedback mechanisms that enable users to refine AI
   behavior over time. This assists to maintain relevance and
   reliability of the AI system based on user input and
   preferences.
6. Develop role-based customization options, allowing different
   levels of AI feature access and customization based on user
   roles and business requirements.

## Resources

**Related documents:**

- [Prompt
  templates and examples for Amazon Bedrock text models](../../../bedrock/latest/userguide/prompt-templates-and-examples.md "../../../bedrock/latest/userguide/prompt-templates-and-examples.md")
- [Detect
  and filter harmful content by using Amazon Bedrock
  Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md")
- [Influence
  response generation with inference parameters](../../../bedrock/latest/userguide/inference-parameters.md "../../../bedrock/latest/userguide/inference-parameters.md")
- [ISO/IEC
  42001:2023 Information technology — Artificial intelligence —
  Management system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
