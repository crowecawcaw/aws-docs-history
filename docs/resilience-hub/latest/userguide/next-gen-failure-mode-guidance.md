

# Failure mode guidance
<a name="next-gen-failure-mode-guidance"></a>

Failure mode guidance allows you to steer the agents to dial in the failure mode analysis.

**Assertions**

Assertions are statements about your application that provide context for failure mode assessments. They help the generative AI agents understand aspects of your architecture that are not visible from resource configuration alone.

Assertions can be:
+ **User-created** – You add assertions before running an assessment. Examples include "Data loss is unacceptable," "Traffic spikes are predictable," or "Typical traffic is 1,000 TPS spiking to 10,000 TPS."
+ **System-generated** – The assessment engine generates assertions during analysis that you can review, confirm, or adjust.

Assertions are categorized and serve as leverage points. By confirming or adjusting assertions, you steer the assessment toward more relevant findings. For example, if the assessment assumes your application must handle 100 TPS, but it actually needs to handle spikes of 10,000 TPS, adjusting that assertion changes the findings you receive.

**Service design files**

You can upload design files that include details about the technical design that will be provided to the AI agents to perform the failure mode analysis.