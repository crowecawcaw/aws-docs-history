# Viewing AWS FIS experiments

In AWS Resilience Hub, view the AWS FIS experiments that you set up to measure the resiliency of
your AWS resources and the amount of time it takes to recover from application,
infrastructure, availability zone, and AWS Region incidents.

To view the list of active AWS FIS experiments from the dashboard, choose
**Dashboard** from the left navigation menu.

In the **Implemented experiments** table, you can identify the AWS FIS
experiments using the following information:

- **Experiment ID** – Identifier of the AWS FIS
  experiment.
- **Action** – Indicates the AWS FIS action associated
  with the AWS FIS experiment. Additionally, if there are more than one action, it
  highlights the number of AWS FIS actions associated with the AWS FIS experiment. You
  can identify the details by hovering over them or by navigating to them.
- **Experiment template ID** – Identifier of the AWS FIS
  experiment template that was used to create the AWS FIS experiment.

###### To view the list of implemented AWS FIS

experiments from applications

1. In the left navigation menu, choose **Applications**.
2. Select an application from the **Applications** table.

To find an application, enter the application name in the **Find
applications** box. 3. Choose **Fault injection experiments**.

In the **Implemented experiments** table, you can identify
the AWS FIS experiments implemented in your application using the following
information:

    * **Experiment ID** – Identifier of the AWS FIS
     experiment.
    * **Action** – Indicates the AWS FIS action
     associated with the AWS FIS experiment. Additionally, if there are more
     than one action, it highlights the number of AWS FIS actions associated
     with the AWS FIS experiment. You can identify the details by hovering over
     them or by navigating to them.
    * **Experiment template ID** – Identifier of the
     AWS FIS experiment template that was used to create the AWS FIS
     experiment.

###### To view the recommended AWS FIS experiments from assessments

1. In the left navigation menu, choose **Applications**.
2. Select an application from the **Applications** table.

To find an application, enter the application name in the **Find
applications** box. 3. Choose **Assessments** tab.

In the **Assessments** table, you can identify your
assessments using the following information:

    * **Name** – Name of the assessment you had provided at
     the time of creation.
    * **Status** – Indicates the execution state of the
     assessment.
    * **Compliance status** – Indicates if the assessment
     is compliant with the resiliency policy.
    * **Resiliency** – Indicates if your application has
     drifted from the RTO and RPO targets defined in the attached resiliency
     policy or not from the previous successful assessment.
    * **App version** – Version of your application that
     was assessed.
    * **Invoker** – Indicates the role that invoked the
     assessment.
    * **Start time** – Indicates the start time of the
     assessment.
    * **End time** – Indicates the end time of the
     assessment.
    * **ARN** – The Amazon Resource Name (ARN) of the
     assessment.

4. Select an assessment from the **Assessments** table.
5. Choose **Operational recommendations**.
6. Choose the right arrow before **Fault injection
   experiments**.

This section lists all the AWS FIS experiments recommended by AWS Resilience Hub for your
application to stress-test and improve its resilience. Based on your
implementation, the AWS FIS experiments are categorized into the following
states:

    * **Implemented** – Indicates that the
     experiments recommended by AWS Resilience Hub are implemented in your
     application. Choose the number below to view all the implemented
     experiments in the **Experiments** table.
    * **Partially implemented** – Indicates that the
     experiments recommended by AWS Resilience Hub are partially implemented in your
     application. Choose the number below to view all the partially
     implemented experiments in the **Experiments**
     table.
    * **Not implemented** – Indicates that the
     experiments recommended by AWS Resilience Hub are unimplemented in your
     application. Choose the number below to view all the unimplemented
     experiments in the **Experiments** table.
    * **Excluded** – Indicates that the experiments
     recommended by AWS Resilience Hub are excluded from your application. Choose the
     number below to view all the excluded experiments in the
     **Experiments** table. For more information about
     including and excluding recommended experiments, see [Including or excluding operational recommendations](exclude-recommend.md "exclude-recommend.md").

**Experiments** table lists all the implemented AWS FIS
experiments that impact the resiliency score of your application. You can
identify the AWS FIS experiments using the following information:

    * **Action name** – Indicates the AWS FIS action
     recommended for your application. When the **State** is
     set to **Not trackable**, it indicates that the AWS FIS
     experiment is a scenario. Choose the scenario name to view its details
     on the **Scenario library** page in the AWS FIS
     console.
    * **State** – Indicates the current
     implementation state of the AWS FIS experiment. That is,
     **Implemented**, **Partially
     implemented**, **Not implemented**, and
     **Excluded**.


    ###### Note

    AWS FIS scenario is a console-only feature with multiple predefined
     actions. Hence, AWS Resilience Hub cannot track it and it will set the
     **State** to **Not
     trackable**.
    * **Description** – Describes the objective of
     the AWS FIS action.
