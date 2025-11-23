# RAIDP01-BP01 Identify evaluation datasets needed to measure

system performance against release criteria

Work backwards from your release criteria to identify the specific
evaluation datasets needed to test each one. Validate that each
dataset has the right characteristics for its purpose (for example,
demographic labels for fairness testing, harmful content examples
for safety testing, and sufficient sample sizes for statistical
confidence). Track mappings between datasets and criteria so you can
verify complete coverage and maintain traceability between your
release criteria and testing approach.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. For each release criterion, develop a dataset design that
   specifies the required data sources and data labels. Use your
   analysis of intrinsic and confounding variations to clarify
   the specifications. For example, safety testing may require
   harmful content examples and fairness testing may require
   demographic labels across groups.
2. Calculate required dataset sizes using statistical power
   analyses based upon the desired confidence level and interval
   for the criterion. Verify that the subgroup representation and
   sample sizes are adequate to test your release criteria with
   the required confidence you have set.
3. Consider whether one dataset can be used for multiple
   criteria. If so, verify that the statistical power offered by
   the dataset meets the needs of the most stringent release
   criterion.
4. Consider whether one criterion requires evaluation using
   multiple datasets. If your understanding of intrinsic and
   confounding variations is limited by known or unknown issues,
   your evaluation may benefit from using several independently
   sourced datasets.

## Resources

**Related documents:**

- [Statistical
  Power Analysis for the Behavioral Sciences](https://utstat.utoronto.ca/~brunner/oldclass/378f16/readings/CohenPower.pdf "https://utstat.utoronto.ca/~brunner/oldclass/378f16/readings/CohenPower.pdf")
- [Bedrock
  Model Evaluation](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
- [NIST
  AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework "https://www.nist.gov/itl/ai-risk-management-framework")
- [Datasheets
  for Datasets methodology](https://arxiv.org/abs/1803.09010 "https://arxiv.org/abs/1803.09010")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.4.3 Data Resources
