# RAISP02-BP10 Build safety protections into the core AI

system

Follow the safety-by-design principle and design your system from
the start to block harmful outputs and unsafe behaviors through
multiple layers of protection. Start by creating clear, objective
definitions of what constitutes safe versus unsafe behavior for your
specific use case, then incorporate safety training approaches like
model alignment techniques, constitutional training, and
reinforcement learning from human feedback (RLHF) that teach your
system to recognize and avoid harmful content while aligning with
human values and safety preferences, input sanitization techniques
that clean or modify problematic user requests before processing,
output alteration methods that modify or block unsafe responses
before they reach users, and guardrails that enforce safe
interaction boundaries throughout the system.

For example, if your release criteria include safety standards for
blocking harmful content, you might implement alignment methods to
align your model behavior with your safety criteria, use training
approaches that incorporate human feedback to reduce toxic output
generation, build input filtering that neutralizes harmful requests,
use output modification techniques that sanitize responses, or
create interaction limits that block unsafe usage patterns. The
safety techniques you choose should directly support your release
criteria, creating multiple protective layers that work together to
meet safety requirements in your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Define specific safety boundaries for your use case by
   creating clear examples of safe versus unsafe outputs that
   match your release criteria. Test these definitions with
   stakeholders to make sure your team agrees on what constitutes
   harmful behavior, then use these examples to guide your other
   safety work.
2. Build safety training into your model development process
   using techniques like constitutional AI training that teaches
   your system to follow safety principles, or RLHF approaches
   that incorporate human feedback about harmful content. Compare
   different safety training methods to see which ones work best
   for addressing the specific release criteria for your use
   case.
3. Create input sanitization filters that identify and modify
   problematic user requests before they reach your model. Build
   these filters to catch different types of harmful inputs like
   requests for dangerous information, attempts to bypass safety
   measures, or prompts designed to generate toxic content.
4. Build interaction guardrails that limit how users can interact
   with your system, like rate limits to block abuse,
   conversation boundaries that redirect harmful discussions, or
   session controls that detect and stop unsafe usage patterns.
   Test your complete safety system with red teaming exercises to
   find weaknesses and improve your protections before launch.

## Resources

**Related documents:**

- [Flag
  harmful content using Amazon Comprehend toxicity
  detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/ "https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/")
- [Thorn
  and All Tech Is Human Forge Generative AI Principles with AI
  Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/ "https://www.thorn.org/blog/generative-ai-principles/")
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Amazon
  Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/ "https://aws.amazon.com/bedrock/guardrails/")

**Related videos:**

- [AWS re:Invent 2024 - Build an AI gateway for Amazon Bedrock with
  AWS AppSync (FWM310)](https://www.youtube.com/watch?v=iW7OWwct-Ww "https://www.youtube.com/watch?v=iW7OWwct-Ww")
