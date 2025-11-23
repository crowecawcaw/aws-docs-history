# Describing and managing AWS Resilience Hub Applications

An AWS Resilience Hub application is a collection of AWS resources that are structured to prevent
and recover AWS application disruptions.

To describe an AWS Resilience Hub application, you provide an application name, resources from one
or more CloudFormation stacks, and an appropriate resiliency policy. You can also use any existing
AWS Resilience Hub application as a template to describe your application.

After you describe an AWS Resilience Hub application, you must publish it so that you can run a
resiliency assessment on it. You can then use recommendations from the assessment to improve
resiliency by running another assessment, comparing results, and then reiterating the
process until your estimated workload RTO and estimated workload RPO meet your RTO and RPO
targets.

To view the **Applications** page, choose
**Applications** from the navigation pane. You can identify your
applications in the **Applications** page by the following:

- **Name** – The name of the application you had provided
  while defining it in AWS Resilience Hub.
- **Description** – The description of the application you
  had provided while defining it in AWS Resilience Hub.
- **Compliance status** – AWS Resilience Hub sets the application
  status as **Assessed**, **Not assessed**,
  **Policy breached**, or is **Changes
  detected**.
  - **Assessed** - AWS Resilience Hub has assessed your
    application.
  - **Not assessed** - AWS Resilience Hub has not assessed
    your application.
  - **Policy breached** - AWS Resilience Hub has
    determined your application did not meet your resiliency policy's objectives
    for Recovery Time Objective (RTO) and Recovery Point Objective (RPO). Review
    and use the recommendations provided by AWS Resilience Hub before reassessing your
    application for resiliency. For more information about recommendations, see
    [Add an application to AWS Resilience Hub](describe-applicationlication.md "describe-applicationlication.md").
  - **Changes detected** - AWS Resilience Hub has detected
    changes made to the resiliency policy associated with your application. You
    must reassess your application for AWS Resilience Hub to determine if your
    application meets your resiliency policy's objectives.

- **Scheduled assessments** – The resource type identifies
  the component resource for your application. For more information about scheduled
  assessments, see [Application resiliency](view-app-summary.md "view-app-summary.md").
  - **Active** - This indicates your application
    is automatically assessed daily by AWS Resilience Hub.
  - **Disabled** - This indicates your
    application is not automatically assessed daily by AWS Resilience Hub and you must
    manually assess your application.

- **Drift status** – Indicates if your application has
  drifted or not from the previous successful assessment and sets one of the following
  statuses:
  - **Drifted** - Indicates that the application,
    which was compliant with its resiliency policy in the previous successful
    assessment, has now breached the resiliency policy and the application is at
    risk. Additionally, it also indicates if the resources within input sources,
    which are included in the current application version, were added or
    removed.
  - **Not drifted** - Indicates that the
    application is still estimated to meet its RTO and RPO targets defined in
    the policy. Additionally, it also indicates that the resources within input
    sources, which are included in the current application version, were not
    added or removed.

- **Estimated workload RTO** – Indicates the maximum
  possible estimated workload RTO of your application. This value is the maximum
  estimated workload RTO of all the disruption types from the last successful
  assessment.
- **Estimated workload RPO** – Indicates the maximum
  possible estimated workload RPO of your application. This value is the maximum
  estimated workload RTO of all the disruption types from the last successful
  assessment.
- **Last assessment time** – Indicates the date and time
  your application was last assessed successfully.
- **Creation time** – The date and time that the application
  was created.
- **ARN** – The Amazon Resource Name (ARN) of your
  application. For more information about ARNs, see [Amazon Resource Names
  (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _AWS General Reference_.

###### Note

AWS Resilience Hub can fully assess the resiliency of cross-Region Amazon ECS resources only if you
are using Amazon ECR for the image repository.

In addition, you can also filter the applications list by using one of the following
options in the **Applications** page:

- **Find applications** – Enter your application name to
  filter the results by the name of your application.
- **Filter last assessment time by a date and time range** –
  To apply this filter, choose the calendar icon and select one of the following
  options to filter by the results that matches the time range:

      + **Relative range** – Select one of the available
       options and choose **Apply**.


      If you choose **Customised range** option, enter a
       duration in **Enter duration** box and select the
       appropriate unit of time from **Unit of time** dropdown
       list, then choose **Apply**.
      + **Absolute range** – To specify the date and time
       range, provide the start time and end time, and then choose
       **Apply**.

  The following topics show the different approaches for describing an AWS Resilience Hub application
  and how to manage them.

###### Topics

- [Viewing an AWS Resilience Hub application summary](view-app-summary.md "view-app-summary.md")
- [Editing AWS Resilience Hub application resources](application-resources.md "application-resources.md")
- [Managing Application Components](AppComponent.md "AppComponent.md")
- [Publishing a new AWS Resilience Hub application
  version](applications-publish.md "applications-publish.md")
- [Viewing all the AWS Resilience Hub application
  versions](view-application-version.md "view-application-version.md")
- [Viewing resources of AWS Resilience Hub application](view-resources.md "view-resources.md")
- [Deleting an AWS Resilience Hub application](applications-delete.md "applications-delete.md")
- [Application configuration parameters](app-config.md "app-config.md")
