

# How assessments use assertions
<a name="next-gen-how-assertions-are-used"></a>

A failure mode assessment treats assertions as authoritative facts about your environment. Assertions take precedence over what the assessment can or cannot observe in your resource configuration. During an assessment, the next generation of Resilience Hub uses assertions to:
+ **Calibrate the analysis** – For example, an assertion about peak traffic lets the assessment evaluate whether your capacity, quotas, and scaling configuration are adequate instead of speculating about load.
+ **Complete the picture** – An assertion can describe a component that resource discovery cannot see, such as a self-managed ingress controller, a service mesh, or a third-party dependency, so that the assessment reasons about it as part of your architecture.
+ **Suppress irrelevant failure mode findings** – If an assertion states that a capability exists or that a concern does not apply to your service, the assessment does not produce failure mode findings that contradict it. For example, asserting that a third-party tool manages database backups suppresses failure mode findings about missing backup configuration.
+ **Identify service functions** – Assertions about how customers use your service help the assessment identify and describe the service functions it evaluates.

**Important**  
The assessment treats assertions as facts. An inaccurate assertion can therefore hide a real risk or produce failure mode findings that do not apply to your service. Review AI-generated assertions after your first assessment, correct anything that is wrong, and keep assertions current as your service changes.

Assertions describe facts about your environment. They do not change your resilience targets. To change the availability, recovery time, or recovery point objectives that an assessment evaluates against, update your resilience policy instead. For more information, see [Resilience policies](next-gen-resilience-policies.md).