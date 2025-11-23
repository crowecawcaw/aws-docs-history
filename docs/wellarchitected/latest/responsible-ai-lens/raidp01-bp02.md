# RAIDP01-BP02 Identify the datasets needed for training and

customizing your system

Identify and plan datasets needed to train your AI system to meet
your release criteria. Determine which dataset types (training,
fine-tuning, validation, calibration, and alignment) you need based
on your training approach, assess existing data to identify gaps,
then acquire or build the missing datasets through external sources,
your own collection, crowdsourcing, or synthetic generation.
Finally, plan how to combine and allocate your datasets while
keeping them separate from evaluation data and maintaining proper
representation across user groups.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Map release criteria to training data requirements by listing
   specific capabilities, behaviors, and knowledge areas your
   system should demonstrate. Identify what types of training
   examples you need for each criterion, like domain-specific
   terminology for accuracy or diverse interactions for fairness.
2. Assess existing training data and identify gaps by checking
   which model capabilities your current datasets support. Look
   for missing edge cases, underrepresented languages, or
   insufficient examples for specific behaviors your system needs
   to learn.
3. Choose between building custom datasets and using existing
   ones by weighing control against cost for each gap. Custom
   datasets provide precise control but require more Resources,
   while existing datasets are faster but may not perfectly match
   your needs.
4. Plan data combination and allocation across training phases
   including pre-training, fine-tuning, validation, calibration,
   and alignment while maintaining complete separation from
   evaluation datasets. Design systems that block
   training-evaluation overlap to protect measurement integrity.

## Resources

**Related documents:**

- [Generative
  AI lifecycle](../generative-ai-lens/generative-ai-lifecycle.md "../generative-ai-lens/generative-ai-lifecycle.md")
- [Responsible
  AI Best Practices: Promoting Responsible and Trustworthy AI
  Systems](https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-best-practices-promoting-responsible-and-trustworthy-ai-systems/ "https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-best-practices-promoting-responsible-and-trustworthy-ai-systems/")
- [AWS Generative AI Best Practices Framework v2](../../../audit-manager/latest/userguide/aws-generative-ai-best-practices.md "../../../audit-manager/latest/userguide/aws-generative-ai-best-practices.md")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.4.3 Data Resources
