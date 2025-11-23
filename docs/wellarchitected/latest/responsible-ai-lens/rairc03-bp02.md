# RAIRC03-BP02 Measure fairness as unwanted bias across

stakeholder groups

Measure variations across relevant stakeholder groups based on your
specific use case and context. This evaluation may include
identifying appropriate fairness metrics that align with your use
case requirements and could examine consistency at both individual
and group levels. Technical approaches for measuring variations in
system performance may include metrics such as demographic parity,
equal outcome rates, equalized odds and equal opportunity to
understand the experience of different groups using the system.
Balance these different fairness metrics based on your use case
context, as optimizing for one type of fairness may sometimes
conflict with others.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Measure individual fairness by testing whether similar
   individuals get similar treatment regardless of their
   demographic characteristics.
2. Measure group fairness by comparing your system's performance
   across the demographic groups you identified in your risk
   assessment (RAIBR02) using metrics like accuracy, precision,
   and recall. Calculate performance differences between groups
   and compare them to your acceptable thresholds to identify
   potential biases. Group-level measurement reveals systemic
   unwanted bias that may have larger impacts (like bias across
   entire groups).
3. Test for representational fairness by analyzing whether your
   system's outputs reinforce harmful stereotypes or misrepresent
   different groups. Use existing tools like stereotype detection
   classifiers or analyze generated content for biased language
   patterns. This catches subtle bias that may not show up in
   performance metrics but still causes harm.
4. Consider testing your system on pairs of similar inputs that
   differ only in demographic attributes to see if outputs change
   inappropriately. This reveals potential bias where demographic
   factors inappropriately influence decisions.
5. Consider testing your system on intersectional groups that
   combine multiple demographic characteristics, using the same
   metrics you applied to single-group analysis. Compare results
   across these intersectional groups to identify potential bias
   that might be hidden when looking at single demographics
   alone.
6. Consider experimenting with complementary fairness metrics
   like demographic parity, equal opportunity, and equalized odds
   to get multiple perspectives on your system's fairness. For
   example, measure whether different groups receive similar
   positive prediction rates and whether the system correctly
   identifies positive cases at similar rates across groups.
   Multiple metrics reveal different types of bias since systems
   can appear fair on one measure but not on another.
7. Identify which fairness metrics conflict with each other for
   your system and make explicit decisions about which to
   prioritize based on your use case context and stakeholder
   values established in your risk characterization (RAIBR02).
   Record your reasoning for these trade-offs since optimizing
   for one type of fairness often reduces performance on others.
   Clear prioritization assists you to make consistent decisions
   when fairness measures conflict.

## Resources

**Related documents**

- [NIST
  AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE "https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
- [Common
  fairness metrics](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html "https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html")

**Related tools:**

- [Amazon
  Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/ "https://aws.amazon.com/sagemaker/ai/clarify/")
