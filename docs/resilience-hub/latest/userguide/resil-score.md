# Understanding resiliency scores

This section describes how AWS Resilience Hub quantifies application readiness from different
disruption scenarios.

AWS Resilience Hub provides resiliency score that represents the resiliency posture of the
application. This score reflects how closely the application follows our recommendations for
meeting the application's resiliency policy, alarms, standard operating procedures (SOPs),
and tests. Based on the type of resources the application uses, AWS Resilience Hub recommends alarms,
SOPs, and a set of tests for each disruption type.

The top resiliency score is 100 points. To achieve the best possible score or the top
score, you must implement all the recommended alarms, SOPs, and tests in your application.
For example, AWS Resilience Hub recommends one test with one alarm and one SOP. The test runs and
fires the alarm and initiates the associated SOP. If they perform successfully and if the
application meets the resiliency policy, it receives a resiliency score close to or equal to
100 points.

After running first assessment, AWS Resilience Hub provides an option to exclude operational
recommendations from your application. To understand the impact of the excluded
recommendations on the resiliency score, you must run a new assessment. However, you can
always include the excluded recommendations in your application and run a new assessment.
For more information about including and excluding alarm, SOP, and test recommendations, see
[Including or excluding operational
recommendations](exclude-recommend.md "exclude-recommend.md").
