# RAIRC03-BP01 Measure safety harms and harmful outputs

Create objective definitions of safe and unsafe content for your use
case by considering both direct potential harms and contextual
inappropriateness. Identify harm categories relevant to possible
outputs of your system (for example, toxicity or violence). For
identified harm categories, select metrics and plan tests with both
quantitative (for example,
[model-based
toxicity classifiers](https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/ "https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/")) and qualitative evaluation strategies
(for example, human red-teaming). Supplement your safety evaluation
with popular open-source benchmarks (like
[ToxiGen](https://github.com/microsoft/TOXIGEN "https://github.com/microsoft/TOXIGEN")
and
[AdvBench](https://github.com/thunlp/Advbench "https://github.com/thunlp/Advbench"))
and Resources (like
[Detoxify](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify")),
and choose metric types that are appropriate for the risk of your
use case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Write clear and objective definitions of what counts as safe
   and unsafe content for your specific use case by creating
   measurable criteria and concrete examples of acceptable and
   unacceptable outputs. Include both direct harms like violence
   or toxicity and contextual problems like inappropriate tone
   for your audience, with specific thresholds and boundaries
   that evaluators can apply consistently. Objective definitions
   reduce subjective interpretation and assist evaluators apply
   consistent standards.
2. Identify the specific harm categories that your system could
   potentially produce, such as toxicity, violence,
   misinformation, or inappropriate content for your target
   users. Focus on harms that are realistic given your system's
   purpose and capabilities rather than trying to cover every
   possible risk. This targeted approach assists you to allocate
   evaluation resources effectively.
3. Choose quantitative metrics like automated toxicity
   classifiers or content filtering tools that can measure your
   identified harm categories at scale. Test popular tools like
   [Detoxify](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify")
   or [Perspective
   API](https://perspectiveapi.com/ "https://perspectiveapi.com/") on sample outputs to see how well they detect the
   types of harmful content your system might produce. Automated
   metrics give you consistent measurement across large datasets.
4. Plan qualitative evaluation methods like human red-teaming
   where experts try to get your system to produce harmful
   outputs through adversarial prompting. Have safety experts or
   domain specialists review sample outputs for harms that
   automated tools might miss. Human evaluation catches nuanced
   safety issues that automated systems may overlook.
5. Supplement your custom evaluation with open-source benchmarks
   like
   [ToxiGen](https://github.com/microsoft/TOXIGEN "https://github.com/microsoft/TOXIGEN")
   or
   [AdvBench](https://github.com/thunlp/Advbench "https://github.com/thunlp/Advbench")
   that test for common safety problems. Run these standard tests
   alongside your custom evaluation to compare your system's
   performance against known safety baselines. This provides
   additional validation and assists to identify blind spots in
   your custom evaluation approach.
6. Match your evaluation intensity to your system's risk level by
   using more thorough testing for higher-risk applications. For
   example, consider using basic automated screening for low-risk
   creative tools but adding human red-teaming for systems that
   might influence important decisions. Appropriate evaluation
   depth blocks both over-testing low-risk systems and
   under-testing higher-risk ones.

## Resources

**Related documents:**

- [NIST
  AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE "https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE")
- [Build
  a robust text-based toxicity predictor](https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/ "https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation

**Related tools:**

- [Perspective
  API](https://perspectiveapi.com/ "https://perspectiveapi.com/")
- [Detoxify](https://github.com/unitaryai/detoxify "https://github.com/unitaryai/detoxify")
- [ToxiGen](https://github.com/microsoft/TOXIGEN "https://github.com/microsoft/TOXIGEN")
- [AdvBench](https://github.com/thunlp/Advbench "https://github.com/thunlp/Advbench")
- [Bedrock
  Evaluations](https://aws.amazon.com/bedrock/evaluations/ "https://aws.amazon.com/bedrock/evaluations/")
