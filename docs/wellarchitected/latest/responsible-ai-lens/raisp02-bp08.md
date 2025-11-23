# RAISP02-BP08 Consider core AI system designs that improve

factual accuracy

Design your system to produce more accurate information by
incorporating techniques that distinguish facts from speculation,
reduce hallucinations, and acknowledge uncertainty. This means
connecting to authoritative knowledge sources through retrieval
methods with source attribution (for example, RAG), employing
alignment approaches like constitutional training and reinforcement
learning from human feedback (RLHF) to block hallucinations, and
incorporating automated reasoning capabilities like chain of thought
reasoning for self-reflection along with uncertainty and confidence
measurements that assist the system to recognize when it is not
confident about information.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Design and implement knowledge grounding strategy using RAG
   architecture or parametric knowledge, verifying clear version
   control of knowledge bases and rigorous source validation
   process.
2. Create training objectives that explicitly reward factual
   accuracy and penalize hallucinations, incorporating
   self-critique methods and negative examples while using tools
   like Constitutional AI or RLHF.
3. Build uncertainty quantification into model behavior through
   calibrated confidence scores and explicit knowledge
   boundaries, training the system to acknowledge limitations
   rather than generate plausible but unverified responses.
4. Establish continuous feedback loops to identify and correct
   factual errors, implementing regular validation cycles against
   authoritative sources and domain-specific accuracy metrics.
5. Use output validation to check that your system's responses
   are accurate and relevant. This is used to detect when your
   system makes up information by comparing responses against
   trusted sources and using logical checks to verify facts are
   correct. For example, Amazon Bedrock Guardrails provide
   capabilities for detecting hallucinations in model responses
   using contextual grounding checks. Automated Reasoning checks
   in Amazon Bedrock Guardrails assists to block factual errors
   from hallucinations using logically accurate and verifiable
   reasoning that explains why responses are correct. Automated
   Reasoning assists to mitigate hallucinations using sound
   mathematical techniques to validate/correct, and logically
   explain the information generated leading to outputs that
   align with known facts and are not based on fabricated or
   inconsistent data.

## Resources

**Related documents:**

- [Minimize
  AI hallucinations and deliver up to 99% verification accuracy
  with Automated Reasoning checks: Now available](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/ "https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/")
- Build responsible AI applications with Amazon Bedrock
  Guardrails
- [ISO/IEC
  42001:2023 A.6.1.2 Objectives for responsible development of
  AI system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Amazon
  Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/ "https://aws.amazon.com/bedrock/guardrails/")
