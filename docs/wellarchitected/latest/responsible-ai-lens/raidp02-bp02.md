# RAIDP02-BP02 Set dataset quality requirements based on your

release criteria

Work backwards from your release criteria to define the quality
standards for each dataset, then select metrics and thresholds to
measure when your data meets those standards. Think of this as
creating data readiness criteria just like your system release
criteria. Data quality means different things depending on how
you'll use the data and what your release criteria need. For
example, it could mean label accuracy, representation across user
groups, diversity of examples, or completeness of coverage.

For each dataset, pick specific quality metrics that align with your
release criteria and set minimum thresholds that should be met
before using that data. Different datasets need different quality
bars. For example, evaluation sets require higher quality standards
than training sets.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Work backwards from each release criterion to determine the
   quality standards means for your datasets by asking,
   "What quality level does my data need to reach for me to
   trust this measurement?" Define what quality means for
   each use case, whether that's label accuracy for fairness
   testing, completeness for harm detection, or consistency for
   robustness evaluation.
2. Pick specific quality metrics that align with how you'll use
   each dataset by choosing measurements like missing value
   rates, label agreement scores, noise levels, or coverage
   percentages. Make sure your metrics connect to your release
   criteria instead of just measuring generic data health that
   might not matter for your specific goals.
3. Set minimum quality thresholds that must be met before you can
   use each dataset by deciding on specific numbers like label
   accuracy above 95%, missing values below 2%, or representation
   coverage across demographic groups. Document these thresholds
   as clear pass or fail criteria that your team can check
   against.
4. Set high quality standards for your evaluation data since
   evaluation quality directly affects your confidence in release
   decisions and noise in this data could lead to inaccurate test
   results.
5. Build data readiness checks that validate your quality
   thresholds before using a dataset by setting up both automated
   validation for quantitative metrics and manual reviews for
   qualitative standards. Treat these like deployment gates that
   block you from using data that doesn't meet your quality
   criteria.

## Resources

**Related documents:**

- [Amazon
  Responsible AI Best Practices](https://aws.amazon.com/machine-learning/responsible-ai/ "https://aws.amazon.com/machine-learning/responsible-ai/")
- [Data
  Quality Assessment Guidelines](../../../sagemaker/latest/dg/model-monitor-data-quality.md "../../../sagemaker/latest/dg/model-monitor-data-quality.md")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.7.4 Quality of data for AI systems
