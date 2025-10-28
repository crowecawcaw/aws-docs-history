# Sample

Conformance Pack Template for Creating Process Checks

```
################################################################################
#
#  Conformance Pack template for process check
#
################################################################################
Resources:
  AWSConfigProcessCheck:
    Properties:
      ConfigRuleName: RuleName
      Description: Description of Rule
      Source:
        Owner: AWS
        SourceIdentifier: AWS_CONFIG_PROCESS_CHECK
    Type: AWS::Config::ConfigRule
```

See two sample templates, the [Operational Best
Practices for CIS AWS Foundations Benchmark v1.4 Level 1](operational-best-practices-for-cis_aws_benchmark_level_1.md "operational-best-practices-for-cis_aws_benchmark_level_1.md") template
and the [Operational Best
Practices for CIS AWS Foundations Benchmark v1.4 Level 2](operational-best-practices-for-cis_aws_benchmark_level_2.md "operational-best-practices-for-cis_aws_benchmark_level_2.md")
template.
