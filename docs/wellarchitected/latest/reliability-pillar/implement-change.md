# Implement change

Controlled changes are necessary to deploy new functionality and to ensure that the
workloads and the operating environment are running known, properly patched software. If these
changes are uncontrolled, then it makes it difficult to predict the effect of these changes,
or to address issues that arise because of them.

**Additional deployment patterns to minimize risk**

[Feature flags (also
known as feature toggles)](https://martinfowler.com/articles/feature-toggles.html "https://martinfowler.com/articles/feature-toggles.html") are configuration options on an application. You can
deploy the software with a feature turned off, so that your customers don’t see the feature.
You can then turn on the feature, as you’d do for a canary deployment, or you can set the
change pace to 100% to see the effect. If the deployment has problems, you can simply turn
the feature back off without rolling back.

[Fault isolated zonal deployment](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/ "https://aws.amazon.com/builders-library/static-stability-using-availability-zones/"): One of the most important rules AWS has
established for its own deployments is to avoid touching multiple Availability Zones within
a Region at the same time. This is critical to ensuring that Availability Zones are
independent for purposes of our availability calculations. We recommend that you use similar
considerations in your deployments.

**Operational Readiness Reviews (ORRs)**

AWS finds it useful to perform operational readiness reviews that evaluate the
completeness of the testing, ability to monitor, and importantly, the ability to audit the
application's performance to its SLAs and provide data in the event of an interruption or
other operational anomaly. A formal ORR is conducted prior to initial production
deployment. AWS will repeat ORRs periodically (once per year, or before critical
performance periods) to ensure that there has not been drift from operational
expectations. For more information on operational readiness, see the [Operational Excellence
pillar](../operational-excellence-pillar/welcome.md "../operational-excellence-pillar/welcome.md") of the [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/ "https://aws.amazon.com/architecture/well-architected/").

###### Best practices

- [REL08-BP01 Use runbooks for standard activities such as
  deployment](rel_tracking_change_management_planned_changemgmt.md "rel_tracking_change_management_planned_changemgmt.md")
- [REL08-BP02 Integrate functional testing as part of your
  deployment](rel_tracking_change_management_functional_testing.md "rel_tracking_change_management_functional_testing.md")
- [REL08-BP03 Integrate resiliency testing as part of your
  deployment](rel_tracking_change_management_resiliency_testing.md "rel_tracking_change_management_resiliency_testing.md")
- [REL08-BP04 Deploy using immutable infrastructure](rel_tracking_change_management_immutable_infrastructure.md "rel_tracking_change_management_immutable_infrastructure.md")
- [REL08-BP05 Deploy changes with automation](rel_tracking_change_management_automated_changemgmt.md "rel_tracking_change_management_automated_changemgmt.md")
