

# Monitor the Guidance
<a name="monitoring"></a>

This Guidance deploys 44 Amazon CloudWatch alarms covering the failure modes that stop telemetry from reaching the platform. They are created for you; they are **not** connected to a person for you.

**Important**  
Most of the alarms publish to Amazon SNS topics that have **no subscription** until you add one. An alarm with no subscriber changes state silently and reports nothing, which is indistinguishable from a healthy platform. Before treating a deployment as operational, complete [Route the alarms to a person](mon-route-alarms.md).

Counts and thresholds in this chapter were read from the synthesized staging templates. Your deployment’s counts vary with the optional stacks you enable.