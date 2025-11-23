# RAIUC03-BP01 Identify the expected input and outputs for the AI

system

Imagine the AI system solving the use case as a box containing an
unknown mechanism. Describe the inputs to the AI system. Stay at a
high level, focusing, for example, on whether inputs might contain
spoken English text and images, but not on the specific audio or
image filetypes. Consider what information is present in the input
signal, and whether that information is enough to infer the desired
outputs. Consider whether the inputs and outputs differ from how the
use case is currently solved.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Define your AI system's inputs at a high level by describing
   the types of information that will flow into your system, such
   as text in multiple languages, images, audio recordings, or
   structured data like user preferences or transaction
   histories. Focus on the content and meaning rather than
   technical formats. For example, you could define inputs as
   _customer support conversations_ rather
   than _MP3 audio files_.
2. Specify what your AI system should produce as outputs,
   describing the type of information it will generate. This
   might include text responses, classification labels,
   recommendations, generated content, or structured data that
   downstream systems can use to take actions.
3. Analyze whether your inputs contain enough information to
   reliably produce your desired outputs by thinking through the
   logical connection between what you're giving the system and
   what you expect it to produce. If you want your system to
   diagnose medical conditions but only provide it with basic
   symptoms, consider whether that's sufficient or if you need
   additional input like medical history or test results.
4. Compare your AI system's inputs and outputs to how the problem
   is solved today without AI, identifying what's different and
   what stays the same. For example, if human customer service
   agents currently handle inquiries using phone calls and
   internal knowledge bases, but your AI will work with chat
   messages and documentation, note these differences and
   consider their implications.

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.2 AI system requirements and
  specification
- [NIST
  Artificial Intelligence Risk Management Framework (NIST AI
  100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf"): MAP2.1, MAP2.2

**Related tools:**

- [Improve
  accuracy by adding Automated Reasoning checks in Amazon
  Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md "../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md")
- [Use
  contextual grounding check to filter hallucinations in
  responses](../../../bedrock/latest/userguide/guardrails-contextual-grounding-check.md "../../../bedrock/latest/userguide/guardrails-contextual-grounding-check.md")
