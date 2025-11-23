# RAISP02-BP04 Build security protections directly into the core

AI system design

Follow "secure by design" and "defense in depth" principles and
build security protections into your system from the beginning to
protect your system and maintain its intended operation. This means
incorporating safeguards like access controls, input validation and
sanitization to defend against prompt injections, and robust
techniques to mitigate attempts at jailbreaking or bypassing your
system's safety guardrails. The specific security measures you
choose should directly address the security requirements in your
release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Build input validation into your model's core processing by
   checking inputs for unwanted patterns, prompt injections, and
   attempts to manipulate system behavior. Create filters that
   detect and block unwanted patterns such as instruction
   overrides, data extraction attempts, and jailbreaking prompts
   before they reach your model.
2. Design access controls directly into your system architecture
   by requiring authentications for each interaction, limiting
   what different user types can access, and restricting
   administrative functions to authorized personnel only. Set up
   role-based permissions that block unauthorized users from
   accessing sensitive model capabilities or training data.
3. Build adversarial robustness into your model by training it to
   resist attempts to manipulate its outputs through crafted
   inputs. Include adversarial examples in your training data and
   design your model architecture to be stable when faced with
   inputs designed to cause harmful or unexpected behavior.

## Resources

**Related documents:**

- [Detect
  and filter harmful content by using Amazon Bedrock
  Guardrails](../../../bedrock/latest/userguide/guardrails.md "../../../bedrock/latest/userguide/guardrails.md")
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools**

- [Amazon
  Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/ "https://aws.amazon.com/bedrock/guardrails/")
