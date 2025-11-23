# RAIRC03-BP05 Measure privacy protection

Measure how well your system protects each type of confidential or
personal information that your risk assessment identified as at
risk. This may include detecting privacy leaks, unauthorized data
access patterns, or inappropriate data retention issues your risk
assessment determined to be most likely or impactful. Assess private
data identification and redaction capabilities for the data types
that your risk assessment prioritized and consult with your legal
team on the specific privacy regulations relevant to your use case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Build privacy attack tests that target the vulnerabilities
   your RAIBR02 risk assessment found, using both automated tools
   such as
   [Promptfoo](https://github.com/promptfoo/promptfoo "https://github.com/promptfoo/promptfoo")
   and manual testing to check for membership inference, data
   extraction, and prompt injections. Create standard test cases
   with clear success measures and document your testing methods
   so you can repeat them across different system versions.
2. Set up automated detection tests that check your system's
   ability to find and remove the types of confidential and
   personal information that your risk assessment prioritized.
   Build testing pipelines that measure how accurately your
   system detects these data types.

## Resources

**Related documents:**

- [NIST
  AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE "https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE")
- [NIST
  Privacy Engineering Program](https://www.nist.gov/privacy-engineering "https://www.nist.gov/privacy-engineering")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
- [Remove
  PII from conversations by using sensitive information
  filters](../../../bedrock/latest/userguide/guardrails-sensitive-filters.md "../../../bedrock/latest/userguide/guardrails-sensitive-filters.md")

**Related tools:**

- [Promptfoo](https://github.com/promptfoo/promptfoo "https://github.com/promptfoo/promptfoo")
- [Presidio:
  Data Protection and De-identification SDK](https://microsoft.github.io/presidio/ "https://microsoft.github.io/presidio/")
