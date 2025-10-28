# Viewing standard operating procedures

###### To view the implemented SOPs from applications

1. In the left navigation menu, choose **Applications**.
2. In **Applications**, open an application.
3. Choose **Standard operating procedures** tab.

In **Standard operating procedures summary** section, the
**Implemented standard operating procedures** table displays the
list of SOPs that are generated from SOP recommendations.

You can identify your SOPs by the following:

    * **SOP name** – Name of the SOP that you have defined for your
     application.
    * **SSM document** – S3 URL of the Amazon EC2 Systems Manager document that
     contains the SOP definition.
    * **Description** – Describes the objective of the SOP.
    * **Test run** – S3 URL of the document that contains the results
     of the latest test.
    * **Reference ID** – Identifier of the referenced SOP
     recommendation.
    * **Resource ID** – Identifier of the resource for which the SOP
     recommendation is implemented.

###### To view the recommended SOPs from assessments

1. In the left navigation menu, choose **Applications**.
2. Select an application from the **Applications** table.

To find an application, enter the application name in the **Find
applications** box. 3. Choose **Assessments** tab.

In **Resiliency assessments** table, you can identify your assessments
using the following information:

    * **Name** – Name of the assessment you had provided at the time of
     creation.
    * **Status** – Indicates the execution state of the assessment.
    * **Compliance status** – Indicates if the assessment is compliant with
     the resiliency policy.
    * **Resiliency drift status** – Indicates if your application has drifted
     or not from the previous successful assessment.
    * **App version** – Version of your application.
    * **Invoker** – Indicates the role that invoked the assessment.
    * **Start time** – Indicates the start time of the assessment.
    * **End time** – Indicates the end time of the assessment.
    * **ARN** – The Amazon Resource Name (ARN) of the assessment.

4. Select an assessment from the **Resiliency assessments** table.
5. Choose **Operational recommendations** tab.
6. Choose **Standard operating procedures** tab.

In the **Standard operating procedures** table, you can understand more
about the recommended SOPs using the following information:

    * **Name** – Name of the recommended SOP.
    * **Description** – Describes the objective of the SOP.
    * **State** – Indicates the current implementation state of the
     SOP. That is, **Implemented**, **Not implemented**, and
     **Excluded**.
    * **Configuration** – Indicates if there are any pending
     configuration dependencies that needs to be addressed.
    * **Type** – Indicates the type of SOP.
    * **AppComponent** – Indicates the Application Components
     (AppComponents) that are associated with this SOP. For more information about supported
     AppComponents, see [Grouping resources in an AppComponent](AppComponent.md "AppComponent.md").
    * **Reference ID** – Indicates the logical identifier of the
     AWS CloudFormation stack event in AWS CloudFormation.
    * **Recommendation ID** – Indicates the logical identifier of the
     AWS CloudFormation stack resource in AWS CloudFormation.
