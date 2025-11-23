# RAISP03-BP04 Implement output filtering to detect and block

hallucinations

Build filtering mechanisms that automatically detect and block
factually incorrect outputs, hallucinations, and misleading
information before they reach users. These filters act as a final
check to catch inaccuracies that your core AI system might generate.
Use both automated reasoning checks and fact verification systems to
validate outputs against known facts and logical consistency before
delivery.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Identify the specific types of veracity issues your system
   needs to filter based on your release criteria. Define what
   counts as hallucinations, factual errors, and misleading
   information for your use case.

For example, determine whether you need to catch mathematical
errors, fabricated citations, invented statistics, or false
historical claims.

1. Design your filtering strategy by deciding which verification
   methods to use and how they will work together. Plan whether
   you need automated reasoning checks, external fact
   verification, confidence scoring, or human review processes.
   Create a filtering architecture that can handle your expected
   output volume and response time requirements.
2. Implement your filtering mechanisms starting with automated
   reasoning checks that validate logical consistency,
   mathematical accuracy, and basic factual relationships. Add
   fact checking connections to reliable knowledge sources and
   databases. Build hallucination detection systems that can
   identify fabricated information patterns your system commonly
   generates.
3. Test your complete filtering system using known examples of
   your system's typical errors and hallucinations. Measure how
   effectively your filters catch different types of inaccuracies
   without blocking too many accurate outputs. Adjust detection
   thresholds and add new filtering rules based on what you
   discover during testing.

## Resources

**Related tools:**

- [Improve
  accuracy by adding Automated Reasoning checks in Amazon
  Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md "../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md")
- [Amazon
  Bedrock: Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/")
- [Amazon Comprehend Features](https://aws.amazon.com/comprehend/features/ "https://aws.amazon.com/comprehend/features/")
- [Amazon Kendra](https://aws.amazon.com/kendra/ "https://aws.amazon.com/kendra/")
- [Amazon
  Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
