# EUCOPS12-BP01 Deploy alerting mechanisms that quickly identify

anomalous metrics

AWS EUC services provide access to desktops and applications which can be highly
variable in their resource requirements over time. Weekly, monthly, quarterly, and year-end
activities can cause spikes in resource consumption that might result in unnecessary alerts
and a degraded user experience.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

The design and pilot phases of an AWS EUC project should identify resource
requirements for each application set over a typical business cycle. Identify the peak
activity levels to verify that the compute instance types selected for both Amazon WorkSpaces and
WorkSpaces Applications can deliver performance that maintains a good user experience and improves
productivity.

Third party tools from vendors such as ControlUp, Nuvens, LiquidWare, Lakeside
Software, and Aternity can be used to collect resource usage trends and build baselines
for key applications. Some of these can be found on the AWS Marketplace.

AWS and the AWS Partner Network offer many services and automation capabilities you can use
to automatically and elastically scale backend application services or to provide
increased compute capabilities during periods of heavy utilization**.**
