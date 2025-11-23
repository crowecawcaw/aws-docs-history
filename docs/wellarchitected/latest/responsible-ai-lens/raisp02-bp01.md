# RAISP02-BP01 Design the core AI system to directly address your

release criteria

Build your system with your release criteria in mind from the
beginning, choosing components and designing processes that directly
support the performance targets you need to hit. Think of your
release criteria as the blueprint for your system design where every
design decision should move you closer to meeting those specific
goals. Set up regular check-ins during development to see how you
are tracking against your targets and be ready to adjust your
approach if you spot gaps early. Make sure your candidate testing
and validation closely mirror the way you will measure success at
release time, so there are no surprises when it is time to release.
This approach assists you to build exactly what you need to pass
your release criteria, rather than creating a system that performs
well on general metrics but falls short on the specific measures
that matter for your use case.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Define alignment goals that support the release criteria.
2. Define the architecture of the AI system to enhance alignment
   with release criteria (including determining which methods
   will be used to address criteria in model training, setting
   bounds on free parameters, putting in place uncertainty
   estimation and output validation procedures).
3. Develop training protocol with safety checkpoints and consider
   techniques like fine-tuning and constitutional training.
4. Establish a validation framework, including safety-focused
   testing, alignment validation, adversarial and stress testing
   and integration tests that mirror how the success of the AI
   system will be measured once it is released.

## Resources

**Related documents:**

- [Retrieve
  Anything To Augment Large Language Models](https://arxiv.org/abs/2310.07554 "https://arxiv.org/abs/2310.07554")
- [Constitutional
  AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073 "https://arxiv.org/abs/2212.08073")
- [ISO/IEC
  42001:2023 Information technology — Artificial intelligence —
  Management system](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related tools:**

- [Customize
  models in Amazon Bedrock with your own data using fine-tuning
  and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/ "https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/")
