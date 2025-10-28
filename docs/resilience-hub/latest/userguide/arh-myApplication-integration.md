# AWS Resilience Hub and myApplications

The **Resiliency** widget in the myApplications dashboard streamlines the process of assessing and monitoring the application resilience.
It enables you to quickly evaluate the resilience of your applications defined in myApplications without the need to manually recreate them in the AWS Resilience Hub console.
This integrated approach combines the application management capabilities of myApplications with the resilience assessment features of AWS Resilience Hub,
allowing you to leverage the strengths of both platforms. By bringing together application definitions and resilience assessment capabilities,
the **Resiliency** widget simplifies the workflow, enabling you to access relevant information and take actions to enhance resilience from a centralized location.
When an application is assessed from the **Resiliency** widget, AWS Resilience Hub performs the following:

- Creates the selected application in AWS Resilience Hub.
- Automatically discovers and maps the resources associated with the model.
- Creates and assigns a new resiliency policy with pre-defined values for recovery time
  objective (RTO) and recovery point objective (RPO). That is four hours for RTO and one hour for
  RPO. After you generate an assessment, you can modify the resiliency policy or assign a
  different policy from the AWS Resilience Hub console. For more information about updating resiliency
  policy and attaching a different policy, see [Managing resiliency policies](resiliency-policies.md "resiliency-policies.md").
- Assesses the application's resilience against RTO and RPO defined in the resiliency policy
  to identify the areas that require improvements in the application architecture. The failure
  scenarios include Availability Zone failures, Regional outages, and other potential
  disruptions.
- Continuously monitors the application's resources and configuration changes after the
  initial assessment, providing alerts or updates if any changes impact the application's
  resilience.

###### Note

Before starting assessments, we recommend you to evaluate the potential costs involved in
running assessments using AWS Resilience Hub. For detailed pricing information, see the [AWS Resilience Hub pricing](https://aws.amazon.com/resilience-hub/pricing/ "https://aws.amazon.com/resilience-hub/pricing/").

After assessing your application, you can access the full capability of AWS Resilience Hub from the widget by choosing Go to AWS Resilience Hub to view the application details in the AWS Resilience Hub console.
The process for including applications from myApplications into AWS Resilience Hub is governed by the following rules and constraints:

- You can associate only one myApplications application to an application in AWS Resilience Hub. That
  is, you can associate a myApplications application to an AWS Resilience Hub application either by
  running an assessment from **Resiliency** widget in the myApplications dashboard, or by completing
  the [Using myApplications applications](discover-structure.md#myApplications-steps "discover-structure.md#myApplications-steps") procedure while describing the application in AWS Resilience Hub
  console.
- You can only include, assess, and view myApplications applications that reside within the
  same AWS Region and AWS account boundaries as your myApplications environment. Applications
  created in different AWS Regions or under separate AWS accounts will not be visible or
  accessible through this widget.
- You can only add, remove, and update resources from the myApplications dashboard. When you
  modify the application resources from the myApplications dashboard, you must reimport the
  AWS Resilience Hub to view the resource changes in AWS Resilience Hub.

## Learn more

For more information about managing applications and resources in the myApplications dashboard, see the following topics in AWS Console Home documentation:

- [What is myApplications on AWS?](../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md "../../../awsconsolehelpdocs/latest/gsg/aws-myApplications.md")
- [Creating your first application in myApplications](../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md "../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md")
- [Managing resources](../../../awsconsolehelpdocs/latest/gsg/myApp-manage-resources.md "../../../awsconsolehelpdocs/latest/gsg/myApp-manage-resources.md")
- [Resiliency Widget](../../../awsconsolehelpdocs/latest/gsg/myApp-app-dash.md#myApp-reshub.html "../../../awsconsolehelpdocs/latest/gsg/myApp-app-dash.md#myApp-reshub.html")

For more information about describing applications and running assessments in AWS Resilience Hub, see the following topics:

- [To run a resiliency assessment for an existing
  myApplications application from
  Resiliency widget for the first time](run-assessment-resiliency-widget.md#run-res-widget-new "run-assessment-resiliency-widget.md#run-res-widget-new")
- [To rerun a resiliency assessment for an existing
  myApplications application from
  Resiliency widget](run-assessment-resiliency-widget.md#rerun-res-widget "run-assessment-resiliency-widget.md#rerun-res-widget")
- [Reviewing assessment summary in
  Resiliency widget](review-assessment-resliency-widget.md "review-assessment-resliency-widget.md")
