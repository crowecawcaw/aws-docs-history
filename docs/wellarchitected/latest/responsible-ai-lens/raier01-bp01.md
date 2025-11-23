# RAIER01-BP01 Validate that release criteria still align with

current industry standards

At the start of a release evaluation, check that the release
criteria and associated evaluation tests are still aligned with the
current version of the AI system. Research and confirm that there
are no new and relevant benchmarks or expectations that need to be
included in the evaluation.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

1. Compare your current release criteria against the actual
   system features and capabilities you plan to release, looking
   for gaps or mismatches. If your system includes capabilities
   that were not considered when you last updated your criteria,
   consider adding appropriate evaluation tests to cover these
   new features. This includes revisiting your risk and benefit
   assessment if necessary.
2. Stay up to date with new benchmarks, evaluation methods, or
   industry standards to see if there are new ways to test your
   system against your release criteria.
3. Consider new guidelines, updated regulations, or emerging
   compliance-aligned frameworks that might affect what you need
   to test before release. Consult with your legal team to assess
   relevant regulatory considerations.
4. Cross-check your evaluation datasets and test cases to make
   sure they still match the real-world scenarios where your
   system will be used. If your intended use cases have changed
   or expanded, you may need to update your evaluation approach
   to reflect these new applications.

## Resources

**Related documents**

- [ISO/IEC
  42001:2023 A.6.2.4 AI system verification and
  validation](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")

**Related videos:**

- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best
  practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y "https://www.youtube.com/watch?v=wuVpCc5a81Y")

**Related examples:**

- [awslabs](https://github.com/awslabs "https://github.com/awslabs")/[agent-evaluation](https://github.com/awslabs/agent-evaluation "https://github.com/awslabs/agent-evaluation")
- [aws-samples](https://github.com/aws-samples "https://github.com/aws-samples")/[rag-evaluation](https://github.com/aws-samples/rag-evaluation "https://github.com/aws-samples/rag-evaluation")

**Related tools**

- [Amazon
  Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
- [Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker/ai/?trk=bba24a8e-fec0-4c35-b7c7-d2e5e6b67eeb&sc_channel=ps&ef_id=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE:G:s&s_kwcid=AL!4422!3!724106169285!e!!g!!amazon%20sagemaker%20ai!19090032234!170269930766&gad_campaignid=19090032234&gbraid=0AAAAADjHtp97_-1psrdUeBS9kWnK-_Zmt&gclid=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE "https://aws.amazon.com/sagemaker/ai/?trk=bba24a8e-fec0-4c35-b7c7-d2e5e6b67eeb&sc_channel=ps&ef_id=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE:G:s&s_kwcid=AL!4422!3!724106169285!e!!g!!amazon%20sagemaker%20ai!19090032234!170269930766&gad_campaignid=19090032234&gbraid=0AAAAADjHtp97_-1psrdUeBS9kWnK-_Zmt&gclid=CjwKCAjw2vTFBhAuEiwAFaScwgLGwsaX0LbsbBiFc16GhqyAGMIK79BPAbk_Bnl_-rlJVFq23-H2KRoCz5cQAvD_BwE")
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
