# AWS Resilience Hub summary

AWS Resilience Hub provides a visual summary with charts and graphs that gives you an at-a-glance
view of your application's resilience posture across multiple AWS services and resources.
This comprehensive and concise visual summary enables you to quickly identify potential
resilience gaps, prioritize actions, and track progress in enhancing your application's
ability to recover from disruptions. When you choose **Export**, and if you
are exporting the metrics for the first time, AWS Resilience Hub creates a new Amazon S3 bucket in the
Region from which you are accessing AWS Resilience Hub. This Amazon S3 bucket is created only for the
first time and will be used to save the exported metrics upon successful completion.
Additional charges apply for storing exported data in Amazon S3. For more information about these
charges, [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

The charts and graphs in the widgets help you understand the following:

- Overview of the application's overall resilience score and current operational
  state.
- Potential policy violations or deviations from best practices by highlighting
  applications that are not compliant with established policies or have drifted from
  recommended configurations. Additionally, it also highlights specific areas that
  enables you to prioritize and address them.
- Critical resources or applications that demand immediate attention.
- Recommendations for enhancing resilience practices, such as implementing alarms,
  conducting AWS Fault Injection Service (AWS FIS) experiments, and establishing standard
  operating procedures. These recommendations are tracked over time, allowing you to
  monitor the implementation progress and measure the impact on the application's
  overall resilience posture.

###### Widgets

- [Application status](#arh-summary-app-status-ug "#arh-summary-app-status-ug")
- [Top infrastructure
  recommendations by resource type](#arh-summary-infra-top-recommendation-ug "#arh-summary-infra-top-recommendation-ug")
- [Infrastructure
  recommendations](#arh-summary-infra-recommendation-ug "#arh-summary-infra-recommendation-ug")
- [Unimplemented operational
  recommendations](#arh-summary-ops-recommendation-ug "#arh-summary-ops-recommendation-ug")
- [Alarm
  recommendations](#arh-summary-alarms-overtime-recommendation-ug "#arh-summary-alarms-overtime-recommendation-ug")
- [SOP recommendations](#arh-summary-sop-overtime-recommendation-ug "#arh-summary-sop-overtime-recommendation-ug")
- [AWS FIS experiment
  recommendations](#arh-summary-fis-exp-overtime-recommendation-ug "#arh-summary-fis-exp-overtime-recommendation-ug")
- [Applications with drifts](#arh-summary-app-drifts-ug "#arh-summary-app-drifts-ug")
- [Resiliency score](#arh-summary-res-score-overtime-recommendation-ug "#arh-summary-res-score-overtime-recommendation-ug")
- [Bottom 10 applications for
  resiliency score](#arh-summary-res-score-bottom-ten-app-ug "#arh-summary-res-score-bottom-ten-app-ug")
- [Application state by policy](#arh-summary-app-state-policy-ug "#arh-summary-app-state-policy-ug")

## Application status

This widget indicates if your applications comply with the resiliency policy or not.
Choose the number adjacent to the **Application count** in the pop-up
to view all the associated applications in the **Applications** pane.
To view all the applications you have created, choose **View
applications**. For more information about managing applications in
AWS Resilience Hub, see [Viewing an AWS Resilience Hub application summary](view-app-summary.md "view-app-summary.md").

## Top infrastructure

recommendations by resource type

This widget displays the number of infrastructure recommendations for each resource
type of your AWS resources provided in the last successful assessment to improve their
resiliency posture. You can identify the details by hovering over them or by navigating
to them. To view all the applications you have created, choose **View
applications**. For more information about infrastructure recommendations,
see [Reviewing resiliency recommendations](resil-recs.md "resil-recs.md").

## Infrastructure

recommendations

This widget lists up to 10 applications that have the maximum number of infrastructure
recommendations provided in the last successful assessment to improve their resiliency
posture. To view all the applications you have created, choose **View
applications**. For more information about infrastructure recommendations,
see [Reviewing resiliency recommendations](resil-recs.md "resil-recs.md").

You can identify the details using the following:

- **Application name** – Name of the application that
  you provided while defining it in AWS Resilience Hub.
- **Count** – Indicates the number of infrastructure
  recommendations provided by AWS Resilience Hub in the last successful assessment. Choose
  the number to view all the infrastructure recommendations provided in the
  assessment report.
- **Last assessed** – Indicates the date and time when
  your application was last assessed successfully.

## Unimplemented operational

recommendations

This widget lists up to 10 applications that have the maximum number of unimplemented
operational recommendations provided in the last successful assessment to improve their
resiliency posture. To view all the applications you have created, choose **View
applications**. For more information about operational recommendations, see
[Reviewing operational recommendations](ops.md "ops.md").

You can identify the details using the following:

- **Application name** – Name of the application that
  you provided while defining it in AWS Resilience Hub.
- **Count** – Indicates
  the number of operational recommendations provided by AWS Resilience Hub in the last
  successful assessment. Choose the number to view all the unimplemented
  operational recommendations in the assessment report.
- **Last assessment time** – Indicates the date and time
  when your application was last assessed successfully.

## Alarm

recommendations

This widget lists all the Amazon CloudWatch alarm recommendations provided for improving the
resilience posture over a selected time period. The different categories
(**Implemented**, **Not implemented**, and
**Excluded**) indicate their implementation state in your
application. You can view the number of Amazon CloudWatch alarm recommendations for each category
by hovering over them or by navigating to them. To view all the applications you have
created, choose **View applications**. For more information about alarm
recommendations, see [Reviewing operational recommendations](ops.md "ops.md").

## SOP recommendations

This widget lists all the standard operating procedure (SOP) recommendations provided
for improving the resilience posture over a selected time period. The different
categories (**Implemented**, **Not implemented**, and
**Excluded**) indicate their implementation state in your
application. You can view the number of SOP recommendations for each category by
hovering over them or by navigating to them. To view all the applications you have
created, choose **View applications**. For more information about
operational recommendations, see [Reviewing operational recommendations](ops.md "ops.md").

## AWS FIS experiment

recommendations

This widget lists all the AWS FIS experiment recommendations provided for
improving the resilience posture over a selected time period. The different categories
(**Implemented**, **Not implemented**,
**Partially implemented**, and **Excluded**)
indicate their implementation state in your application. You can view the number of
AWS FIS experiment recommendations for each category by hovering over them or by
navigating to them. To view all the applications you have created, choose **View
applications**. For more information about AWS FIS experiment
recommendations, see [Managing standard operating procedures](sops.md "sops.md").

## Applications with drifts

This widget lists all your applications that have drifted from their previous
compliant state in the last successful assessment. To view all the applications you have
created, choose **View applications**. For more information about
managing applications in AWS Resilience Hub, see [Viewing an AWS Resilience Hub application summary](view-app-summary.md "view-app-summary.md").

You can identify the details using the following:

- **Application name** – Name of the application that
  you provided while defining it in AWS Resilience Hub.
- **Policy drifts** – Choose the number adjacent to the
  application name to view all the Application Components that complied with the
  policy in the previous assessment but failed to comply in the current
  assessment.
- **Resource drifts** – Choose the number below to view
  all the resources that have changed from their configuration in the latest
  import.

## Resiliency score

This widget displays the trend of the application's resiliency score over a selected
time period for up to five applications. You can view an application's resiliency score
by hovering over the line associated with the application name or by navigating to it,
and then choosing the application name to view the application summary. To view all the
applications you have created, choose **View applications**. For more
information about resilience score, see [Understanding resiliency scores](resil-score.md "resil-score.md").

## Bottom 10 applications for

resiliency score

This widget lists up to 10 applications with the lowest resiliency scores from their
most recent assessments, highlighting the applications that require immediate attention
to improve their resilience. To view all the applications you have created, choose
**View applications**. For more information about resilience score,
see [Understanding resiliency scores](resil-score.md "resil-score.md").

You can identify the details using the following:

- **Application name** – Name of the application that
  you provided while defining it in AWS Resilience Hub.
- **Resiliency score** – The overall resiliency score
  determined by AWS Resilience Hub for your application after running the
  assessment.
- **Last assessment time** – Indicates the date and time
  when your application was last assessed successfully.

## Application state by policy

This widget lists all your policies and the number of applications that have breached,
met, or yet to be assessed against them. To view all the policies you have created,
choose **View policies**. For more information about resilience score,
see [Managing resiliency policies](resiliency-policies.md "resiliency-policies.md").

You can identify the details using the following:

- **Policy name** – Indicates the policy name you
  provided while defining it in AWS Resilience Hub.
- **Type** – Indicates that the type of policy
  (**Resiliency policy**) attached to the application.
- **Policy name** – Indicates the number of applications
  that have either breached the RTO and RPO targets defined in the resiliency
  policy.
- **Apps met** – Indicates the number of applications
  that are compliant with the resiliency policy.
- **Apps not assessed** – Indicates the number of
  applications that are yet to be assessed against the resiliency policy.
- **Resiliency score** – The overall resiliency score
  determined by AWS Resilience Hub for your application after running the
  assessment.
- **Last assessment time** – Indicates the date and time
  when your application was last assessed successfully.
