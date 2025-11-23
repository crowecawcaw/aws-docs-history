# RAIUC03-BP02 Identify how your expected inputs could vary in

their content

Identify the ways in which inputs to the AI system might
systematically vary under real-world conditions. For example, the
inputs to system that transcribes speech in audio recordings might
vary by background noise, physical characteristics of the voices, or
the sensitivity of the microphone. Or, inputs to chatbot could vary
by language, use of slang or jargon, or word spellings ("analyze" vs
"analyse"). Decide whether each type of variation is something the
AI system should attend to, or ignore.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Review examples of potential real-world inputs to identify the
   types of intrinsic and confounding variations. Consider how
   inputs are sourced (for example, sensor types, environmental
   conditions, and potentially pre-processed). Consider
   variations across different user segments, geographic regions,
   and time periods.
   1. _Intrinsic variation_ refers to
      differences in input data to which AI system should attend
      to succeed.
   2. _Confounding variation_ refers to
      differences in input data that an AI system should ignore
      to succeed.
   3. For example, when comparing two images of faces to
      determine if the images are of the same person, an AI
      system must look at differences in pixel intensities that
      are due to facial geometry (like the width of the nose)
      and skin albedo (including scars, tattoos, and natural
      skin coloration), but not pixel differences due to camera
      angle, facial expression, or scene lighting. The first
      variations are intrinsic and the second are confounding.

2. Consider whether data capturing intrinsic or confounding
   variations can be synthesized.
3. Identify edge cases and other out-of-distribution scenarios
   that might affect system reliability.

## Resources:

**Related documents:**

- [Responsible
  AI Practices](https://aws.amazon.com/machine-learning/responsible-ai/ "https://aws.amazon.com/machine-learning/responsible-ai/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
- [NIST
  Artificial Intelligence Risk Management Framework (NIST AI
  100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf"): MAP2.1, MAP2.2, MAP2.3
