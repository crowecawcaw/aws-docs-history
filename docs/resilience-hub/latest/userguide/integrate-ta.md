# AWS Trusted Advisor

AWS Trusted Advisor is a centralized home of AWS best practice recommendations that
helps you to identify, prioritize, and optimize your deployment on AWS.
AWS Trusted Advisor inspects your AWS environment, and then makes recommendations
through checks when opportunities exist to save money, improve system availability
and performance, or help close security gaps. These checks are divided into multiple
categories based on their purpose. For more information about different categories
of checks in AWS Trusted Advisor, see the [AWS Support](../../../awssupport/latest/user/trusted-advisor-check-reference.md "../../../awssupport/latest/user/trusted-advisor-check-reference.md") User Guide.

AWS Trusted Advisor provides multiple high-level resiliency recommendations through
resiliency checks for each application in AWS Resilience Hub under **Fault
tolerance** category. **Fault tolerance** category
lists all the checks that tests your applications to determine their resilience and
reliability. These checks alert you when there are AppComponent failures and policy
breaches that can cause resiliency risks and affect the application availability for
business continuity. It also provides resiliency recommendations that will improve
the chances to reduce these risks under **Recommended Action**
section, which needs to be addressed in AWS Resilience Hub. For more insights about the
recommendations for each application in the AWS Trusted Advisor, we recommend you to view
the detailed recommendations provided in the AWS Resilience Hub.

AWS Trusted Advisor provides the following checks for each application in
AWS Resilience Hub:

- **AWS Resilience Hub application resilience scores**
  – Checks the resiliency score of your applications from their latest
  assessment in AWS Resilience Hub and alerts you if their resiliency scores are below
  a specific value.

**Alert criteria**

    + **Green** – Indicates that
     your application has a resiliency score of 70 and above.
    + **Yellow** – Indicates that
     your application has a resiliency score between 40 and 69.
    + **Red** – Indicates that your
     application has a resiliency score less than 40.

**Recommended action**

To improve the resiliency posture and obtain the best possible resiliency
score for your application, run an assessment with the most recently updated
version of your application resources and if applicable, implement the
suggested operational recommendations. For more information about running,
reviewing, and implementing assessments, reviewing and including/excluding
operational recommendations, and implementing the same, see the following
topics:

    + [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md")
    + [Reviewing assessments reports](review-assessment.md "review-assessment.md")
    + [Reviewing resiliency recommendations](resil-recs.md "resil-recs.md")
    + [Including or excluding operational
     recommendations](exclude-recommend.md "exclude-recommend.md")

- **AWS Resilience Hub application policy breached**
  – Checks if the AWS Resilience Hub applications meet the RTO and RPO targets
  you have set for an application and alerts you if the application do not
  meet the RTO and RPO targets.

**Alert criteria**

    + **Green** – Indicates that the
     application has a policy and the estimated workload RTO and
     estimated workload RPO meet the RTO and RPO targets.
    + **Yellow** – Indicates that
     the application has a policy and has not been assessed.
    + **Red** – Indicates that the
     application has a policy and the estimated workload RTO and
     estimated workload RPO does not meet the RTO and RPO targets.

**Recommended action**

To ensure that the estimated workload RTO and estimated workload RPO of
your application still meet the defined RTO and RPO targets, run assessments
regularly with the most recently updated version of your application
resources. In addition, if you want to ensure that the resiliency policy of
your application is not breached, we recommend you to review the assessment
report and implement the suggested resiliency recommendations. For more
information about enabling AWS Resilience Hub to run assessments on a daily basis on
your behalf, running assessments, reviewing resiliency recommendations and
implementing the same, see the following topics:

    + [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md") (To enable AWS Resilience Hub to
     run assessments on a daily basis on your behalf, complete the steps
     in **To edit drift notification settings
     of your application** procedure to select
     **Automatically assess daily** check
     box.)
    + [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md")
    + [Reviewing assessments reports](review-assessment.md "review-assessment.md")
    + [Reviewing resiliency recommendations](resil-recs.md "resil-recs.md")
    + [Including or excluding operational
     recommendations](exclude-recommend.md "exclude-recommend.md")

- **AWS Resilience Hub application assessment age**
  – Checks the last time since you had run an assessment for each of
  your applications in AWS Resilience Hub. It alerts you if you haven’t run an
  assessment for the specified number of days.

**Alert criteria**

    + **Green** – Indicates that you
     have run an assessment for your application in the last 30
     days.
    + **Yellow** – Indicates that
     you have not run an assessment for your application in the last 30
     days.

**Recommended action**

Run assessments regularly to manage and improve the resilience posture of
your applications on AWS. If you want AWS Resilience Hub to assess your application
on a daily basis on your behalf, you can enable the same by the selecting
the **Automatically assess this application daily** check
box in AWS Resilience Hub drift notification. To select **Automatically
assess this application daily** check box, complete the
**To edit drift notification of your
application** procedure in [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md").

###### Note

This check determines the assessment age of only those applications
that have been assessed at-least once in AWS Resilience Hub.

- **AWS Resilience Hub application component check**
  – Checks if an Application Component (AppComponent) in your
  application is unrecoverable. That is, if this AppComponent does not recover
  in case of a disruption event, you may experience unknown data loss and
  system downtime. If the alert criteria is set to **Red**,
  it indicates that the AppComponent is unrecoverable.

**Recommended action**

To ensure that your AppComponent is recoverable, review and implement the
resiliency recommendations, and then run a new assessment. For more
information about reviewing the resiliency recommendations, see [Reviewing resiliency recommendations](resil-recs.md "resil-recs.md").
For more information about using AWS Trusted Advisor, see the [AWS Support User Guide](../../../awssupport/latest/user/trusted-advisor.md "../../../awssupport/latest/user/trusted-advisor.md").
