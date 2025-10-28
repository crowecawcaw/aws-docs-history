# Running and managing resiliency assessments in

AWS Resilience Hub

When your application changes, you should run a resiliency assessment. The assessment
compares each Application Component configuration to the policy and makes alarm, SOP, and
test recommendations. These configuration recommendations can improve the speed of recovery
procedures.

Alarm recommendations help you set alarms that detect outages. SOP recommendations provide
scripts that manage common recovery processes, such as recovery from a backup. Test
recommendations offer suggestions to verify your configurations work properly. For example,
you can test whether an application recovers during automatic recovery processes, such as
automatic scaling or load balancing because of network issues. You can test whether
application alarms are triggered when resources reach their limits. You can also test how
well SOPs work under the conditions that you indicate.

###### Topics:

- [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md")
- [Reviewing assessments reports](review-assessment.md "review-assessment.md")
- [Deleting resiliency assessments](delete-assessment.md "delete-assessment.md")
