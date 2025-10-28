# Reviewing assessments reports

You find assessment reports in the **Assessments** view of your
application.

###### To find an assessment report

1. In the left navigation menu, choose **Applications**.
2. In **Applications**, open an application.
3. In **Assessments** tab, choose an assessment report from the
   **Resiliency assessments** section.
   When you open the report, you see the following:

- An overall overview of the assessment report
- Recommendations to improve resiliency.
- Recommendations to set up alarms, SOPs, and tests
- How to create and manage tags to search and filter your AWS resources

## Assessment report

This section provides an overview of the assessment report. AWS Resilience Hub lists each
disruption type and the associated Application Component. It also lists your actual
RTO and RPO policies and determines whether the Application Component can achieve
the policy goals.

**Overview**

Shows the name of the application, the name of the resiliency policy, and the
creation date of the report.

**Detected resource drifts**

This section lists all the resources that were added or removed after they were
included in the latest version of the published application. Choose
**Reimport input sources** to reimport all the input sources
(which contains drifted resources) in the **Input sources** tab.
Choose **Publish and assess** to include the updated resources in
the application and receive an accurate resiliency assessment.

You can identify the drifted input sources using the following:

- **Logical ID** – Indicates the logical ID of the
  resource. A logical ID is a name used to identify resources in your
  AWS CloudFormation stack, Terraform state file, myApplications application, or AWS Resource Groups.
- **Change** – Indicates if an input resource was
  **Added** or **Removed**.
- **Source name** – Indicates the resource name.
  Choose a source name to view its details in the respective application. For
  manually added input sources, the link will not be available. For example,
  if you choose the source name that is imported from an AWS CloudFormation stack, you
  will be redirected to the stack details page on the AWS CloudFormation.
- **Resource type** – Indicates the resource
  type.
- **Account** – Indicates the AWS account that
  owns the physical resource.
- **Region** – Indicates the AWS
  Region where the resource is located.

**RTO**

Shows a graphical representation of whether the application is estimated to meet
resiliency policy's objectives. This is based on the amount of time that an
application can be down without causing significant damage to the organization. The
assessment provides an estimated workload RTO.

**RPO**

Shows a graphical representation of whether the application is estimated to meet
resiliency policy's objectives. This is based on the amount of time that data can be
lost before a significant harm to the business occurs. The assessment provides an
estimated workload RPO.

**Details**

Provides detailed descriptions of each disruption type using **All
results** and **Application compliance drifts** tabs.
**All results** tab shows all the disruptions including
compliance drifts, and **Application compliance drifts** tab
displays only compliance drifts. Disruption type includes
**Application**, cloud infrastructure
(**Infrastructure** and **Availability
Zone**), and **Region**, and provides the following
information about it:

- **AppComponent**

The resources that comprise the application. For example, your application
might have a database or compute component.

- **Estimated RTO**

Indicates whether your policy configuration aligns with your policy
requirement. We provide two values, our **Estimated RTO**
and your **Targeted RTO**. For example, if you see
**2h** value under **Targeted RTO**
and **40m** under **Estimated Workload
RTO**, it indicates that we provide an estimated workload RTO
of 40 minutes, while the current RTO of your application is two hours. We
base our estimated workload RTO calculation on the configuration, not the
policy. As a result, a multi-Availability Zone database will have the same
estimated workload RTO for Availability Zone failure, no matter which policy
you select.

- **RTO drift**

Indicates the duration by which your application has drifted from the
estimated workload RTO of the previous successful assessment. We provide two
values, our **Estimated RTO** and **RTO
drift**. For example, if you see **2h** value
under **Estimated RTO** and **40m** under
**RTO drift**, it indicates that your application
drifts from the estimated workload RTO of the previous successful assessment
by 40 minutes.

- **Estimated RPO**

Shows the actual **Estimated Workload RPO** policy that
AWS Resilience Hub estimates, based on the **Targeted RPO** policy
that you set for each Application Component. For example, you might have set
the RPO target in your resiliency policy for Availability Zone failures to
one hour. The estimated result might be calculated near to zero. This
assumes that Amazon Aurora, where we commit every transaction, is successful in
four out of six nodes, spanning multiple Availability Zones. It might be
five minutes for point-in-time restore.

The only RTO and RPO target that you can opt not to supply is Region. For
some applications, it is useful to plan for recovery when there is a crucial
dependency on an AWS service, which might become unavailable in the entire
Region.

If you choose this option, such as setting RTO or RPO targets for the
Region, you’ll receive an estimated recovery time and operational
recommendations for such failures.

- **RPO drift**

Indicates the duration by which your application has drifted from the
estimated workload RPO of the previous successful assessment. We provide two
values, our **Estimated RPO** and **RPO
drift**. For example, if you see **2h** value
under **Estimated RPO** and **40m** under
**RPO drift**, it indicates that your application
drifts from the estimated workload RPO of the previous successful assessment
by 40 minutes.
