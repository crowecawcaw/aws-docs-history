# RAIRC03-BP04 Measure robustness of outputs to input variation

Measure how consistently your system performs when faced with the
specific input variations and distribution shifts that are relevant
to your use case. Prepare to test performance across the natural
variations your risk assessment determined users might provide (such
as different writing styles, dialects, image qualities, or audio
conditions relevant to your use case).

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Build controlled robustness tests that vary one input factor
   at a time while keeping the content meaning the same, using
   the input variations your RAIBR02 risk assessment found most
   likely in your deployment environment. Create paired test
   cases where you change only one thing, such as converting
   formal business language to casual speech or adjusting image
   lighting conditions. Controlled variation testing shows you
   which specific input factors cause performance drops and by
   how much.
2. Apply the same metrics you selected in RAIRC02-BP01 to measure
   performance across different input variations, comparing how
   your system performs on standard inputs versus challenging
   variations. Use controlled comparisons where you test the same
   content with only one input characteristic changed at a time,
   such as measuring accuracy on both formal and casual versions
   of the same question. This approach reveals which specific
   input factors cause performance drops and by how much.
3. Calculate performance variance and degradation across known
   input variations to quantify how much your system's
   reliability fluctuates under different conditions. Identify
   the worst-case performance drops across input types.
4. Test combinations of multiple input variations together, such
   as processing accented speech with background noise or
   analyzing low-quality images with poor lighting, since real
   users often provide challenging inputs with several issues
   simultaneously. Focus on combinations most likely to occur in
   your deployment environment based on your use case analysis.
   Combined variation testing catches failure modes that only
   emerge when multiple challenging factors interact.

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
