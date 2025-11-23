# Running resiliency assessments from

Resiliency widget

For applications created in **myApplications** widget, you can now run
resiliency assessments from the **Resiliency** widget and AWS Resilience Hub
console. For more information about running resiliency assessments from AWS Resilience Hub
console, see [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md").

###### To run a resiliency assessment for an existing

**myApplications** application from
**Resiliency** widget for the first time

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Expand the left sidebar and choose **myApplications**.
3. Select the application for which you want to run assessment.

As a prerequisite, ensure that you have added the
**Resiliency** widget in your AWS Console. To add this
widget, complete the following steps.

    1. On the upper or lower right of the **Console Home**
     dashboard, choose **+Add widgets**.
    2. Choose the **drag indicator**, represented by six
     vertical dots in the upper left of the widget title bar, and then drag
     it to your **Console Home** dashboard.

4. Choose **Assess application**.
5. To select an existing IAM role that will be used for accessing resources in
   the current account, select **Use an IAM role** and then
   select an IAM role from the **Select an IAM role** dropdown
   list.

If you want to use current IAM user to discover your application resources,
choose **Use the current IAM user permissions** and select
**I understand that I must manually configure permissions to enable
the required functionality within AWS Resilience Hub** in **Use the
current IAM user to discover application resources**
section. 6. Choose **Assess**.

Alternatively, turn on **Automatically assess daily** to
enable AWS Resilience Hub to assess your application daily without any additional
costs.

AWS Resilience Hub performs the following actions:

    * Creates an application in AWS Resilience Hub and automatically discovers and
     maps the associated resources.
    * Creates and assigns a new resiliency policy with pre-defined values
     for recovery time objective (RTO) and recovery point objective (RPO).
     That is, four hours for RTO and one hour for RPO. After you generate an
     assessment, you can modify the resiliency policy or assign a different
     policy from the AWS Resilience Hub console. For more information about updating
     resiliency policy and attaching a different policy, see  [Managing resiliency policies](resiliency-policies.md "resiliency-policies.md").
    * Assesses the resilience of the application against RTO and RPO, and
     continuously monitors resources and configuration changes, and publishes
     the results.

###### Note

Before starting assessments, it is advisable to evaluate the potential
costs involved in running assessments using AWS Resilience Hub. For detailed pricing
information, see the [AWS Resilience Hub pricing](https://aws.amazon.com//resilience-hub/pricing?icmpid=docs_resiliencehub_help_panel_resiliency_policies_hp "https://aws.amazon.com//resilience-hub/pricing?icmpid=docs_resiliencehub_help_panel_resiliency_policies_hp").

###### To rerun a resiliency assessment for an existing

**myApplications** application from
**Resiliency** widget

1. Sign in to the [AWS Management
   Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. Expand the left sidebar and choose **myApplications**.
3. Select the application you want to reassess.

As a prerequisite, ensure that you have added the
**Resiliency** widget in your AWS Console. To add this
widget, complete the following steps.

    1. On the upper or lower right of the **Console Home**
     dashboard, choose **+Add widgets**.
    2. Choose the **drag indicator**, represented by six
     vertical dots in the upper left of the widget title bar, and then drag
     it to your **Console Home** dashboard.

4. Choose **Reassess** from the **Resiliency**
   widget.

Alternatively, turn on **Automatically assess daily** to
enable AWS Resilience Hub to assess your application daily without any additional
costs.
