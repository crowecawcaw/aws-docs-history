# RAIDP02-BP04 Validate the quality and reliability of augmented

or synthetic datasets

Assess the quality of model-generated labels and synthetic examples
against human evaluation standards. Identify potential sources of
unwanted bias in synthetic data generation. Validate that synthetic
data maintains the statistical properties needed for your specific
datasets and doesn't exclude important edge cases. Document the
limitations of synthetic approaches and verify that synthetic
examples can effectively substitute for real data in representing
the phenomena you care about.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Test your synthetic data quality against human standards by
   reviewing samples of your generated examples and labels to see
   how realistic and accurate they are. Check whether humans can
   tell the difference between your synthetic data and real data,
   and measure how often your synthetic examples contain errors
   or unrealistic patterns that could mislead your model
   training.
2. Search for bias in your synthetic data generation by checking
   whether your generation process consistently produces unfair
   or skewed examples for certain groups. Look at whether your
   synthetic data overrepresents some demographics while
   underrepresenting others, and test whether the generation
   process amplifies existing biases from your source data or
   introduces new ones.
3. Verify that your synthetic data keeps the statistical
   properties you need by comparing distributions, correlations,
   and patterns between your synthetic and real data. Make sure
   your synthetic examples don't accidentally exclude important
   edge cases or rare scenarios that your model needs to handle,
   and check that key relationships in the data are preserved.
4. Test whether synthetic examples can substitute for real data
   by having domain experts evaluate whether your synthetic
   examples capture the key phenomena and scenarios you need to
   represent, or by training discriminator models to predict
   whether examples are real or synthetic. If your synthetic data
   is high quality, the model should struggle to tell the
   difference. Check if your synthetic data covers the same range
   of situations, edge cases, and user behaviors as your real
   data, and verify that it includes the specific patterns and
   relationships that matter for your use case.
5. Document the limitations and failure modes that you discover
   in your synthetic data so downstream users know where it might
   be unreliable. Write down what types of examples your
   synthetic data handles well versus poorly, what biases it
   contains, and when it should versus shouldn't be used as a
   substitute for real data.

## Resources

**Related documents:**

- [AWS Well-Architected Machine Learning Lens](../machine-learning-lens/welcome.md "../machine-learning-lens/welcome.md")
- [Responsible
  AI Best Practices for Synthetic Data](https://aws.amazon.com/machine-learning/responsible-ai/ "https://aws.amazon.com/machine-learning/responsible-ai/")
- [NIST
  AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework "https://www.nist.gov/itl/ai-risk-management-framework")
- [Partnership on
  AI Synthetic Media Framework](https://partnershiponai.org/ "https://partnershiponai.org/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")A.7.4 Quality of data for AI systems
