# Initiating, creating, and running AWS FIS

experiments

AWS Resilience Hub simplifies AWS FIS experiments by integrating with AWS FIS experiments. It
provides tailored recommendations and allows initiating AWS FIS experiments with
pre-populated templates mapped to your Application Components (AppComponents), enabling
efficient resilience testing.

###### To initiate an AWS FIS experiment from

Operational recommendations

1. Open the AWS Resilience Hub console.
2. In the navigation pane, choose **Applications**.
3. From the list of applications, choose the application you want to create a
   test for.
4. Choose **Assessments** tab.
5. Select an assessment from the **Resiliency assessments**
   table. If you don't have an assessment, complete the procedure in [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md") and then return to this step.
6. Choose **Operational recommendations** tab.
7. Choose the right arrow before **Fault injection
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
     recommended for your application. Choose the action name to view all the
     recommended AppComponents on the **AWS FIS experiment
     details** page. When the **State** is set
     to **Not trackable**, it indicates that the AWS FIS
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

8. Select an AWS FIS action for which you want to initiate an experiment.

In the AWS FIS experiment recommendation section, you can understand more about
the experiments you need implement on the AppComponents using the following
information:

    * **Name** – Name of the AppComponent in which
     the resources are grouped into.
    * **State** – Indicates the current
     implementation state of the AWS FIS action. That is,
     **Implemented**, **Partially
     implemented**, **Not implemented**, and
     **Excluded**.


    ###### Note

    AWS FIS scenario is a console-only feature with multiple predefined
     actions. Hence, AWS Resilience Hub cannot track it and it will set the
     **State** to **Not
     trackable**.
    * **Target selection** – Indicates how the
     resources will be included in the experiment when you choose
     **Initiate experiment**. If AWS Resilience Hub doesn't
     automatically determine target resources, hover over the respective
     **Target selection** field for guidance on adding
     them.
    * **Resources** – Indicates the number of
     resources grouped under the AppComponent. Choose the number to view
     these resources in the **Resources** dialog box. You
     can identify the resources using the following:




    	+ **Logical ID** – Indicates the logical
    	 ID of the resource. A logical ID is a name used to identify
    	 resources in your AWS CloudFormation, Terraform state file,
    	 myApplications application, AWS Resource Groups resource, or Amazon Elastic Kubernetes Service
    	 cluster.
    	+ **Physical ID** – Indicates the actual
    	 assigned identifier for the resource, such as an Amazon EC2 instance
    	 ID or an Amazon S3 bucket name.
    	+ **Type** – Indicates the type of
    	 resource.
    	+ **Region** – Indicates the AWS
    	 Region in which the resource is located.

9. Select an AppComponent and choose **Include** or
   **Exclude** to include or exclude the AppComponent in the
   AWS FIS experiment, respectively.
10. Choose **Initiate experiment**.

AWS Resilience Hub will redirect you to **Specify template details**
page in the AWS FIS console, opening it in a new tab. 11. To create an experiment template, complete the steps in [To create an experiment template using the console](../../../fis/latest/userguide/create-template.md "../../../fis/latest/userguide/create-template.md").

Additionally, after you enter the template details and choose
**Next** in the **Specify template
details** page of the AWS FIS console by following the steps in
[To create an experiment template using the console](../../../fis/latest/userguide/create-template.md "../../../fis/latest/userguide/create-template.md"), AWS Resilience Hub
automatically tries to map **Actions** and
**Targets** for your resource types in the
**Actions and targets** page. However, to improve the
coverage, you can manually add actions and targets by choosing **Add
action** and **Add target**, respectively, and
complete the rest of the procedure to create your experiment.

## Running AWS FIS experiments

After creating an experiment in AWS FIS console, follow the steps in [Start an experiment from a template](../../../fis/latest/userguide/start-experiment-from-template.md "../../../fis/latest/userguide/start-experiment-from-template.md") to run an experiment in AWS FIS
console. If you want AWS Resilience Hub to detect the latest experiments you have run in
AWS FIS, you must run a new assessment. For more information about running
assessments, see [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md").
