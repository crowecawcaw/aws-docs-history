# RAIRC03-BP03 Measure veracity of outputs

Assess your system's tendency to generate factually accurate
information while avoiding the specific types of hallucinations,
misinformation, or fabricated content your risk assessment
identified as problematic for your use case. Implement automated
fact-checking and human expert evaluations. Measure the specific
aspects of truthfulness your risk assessment prioritized such as
factual accuracy, groundedness to source material, or consistency
across interactions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Identify metrics for potential hallucination, omission, and
   misemphasis harms that you identified in your risk assessment
   (RAIBR02).
2. Plan expert human evaluations where domain specialists review
   sample outputs for factual accuracy and appropriateness within
   their area of expertise. Have subject matter experts evaluate
   claims in their field to catch subtle inaccuracies that
   automated tools might miss. Human experts can assess context,
   nuance, and domain-specific accuracy that automated systems
   often overlook.
3. Measure groundedness, i.e. the degree to which your system's
   outputs can be traced back to reliable source material when
   sources are available. Check if claims in generated content
   align with the source documents and whether citations are
   accurate and relevant. Groundedness testing blocks your system
   from making claims that aren't supported by its reference
   materials.
4. Measure consistency by asking your system the same questions
   multiple times and across different phrasings to see if
   answers remain factually consistent. Also test related
   questions to see if responses contradict each other across
   different interactions. Consistency testing reveals when your
   system generates conflicting information about the same
   topics.

## Resources

**Related documents**

- [NIST
  AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE "https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation

**Related tools:**

- [Amazon
  Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
- [Improve
  accuracy by adding Automated Reasoning checks in Amazon
  Bedrock Guardrails](../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md "../../../bedrock/latest/userguide/guardrails-automated-reasoning-checks.md")
