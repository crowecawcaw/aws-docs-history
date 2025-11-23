# Building an SOP based on AWS Resilience Hub recommendations

To build an SOP based on AWS Resilience Hub recommendations, you need an AWS Resilience Hub application with a resiliency policy attached to it, and you need to have run a resiliency
assessment against that application. The resiliency assessment generates the recommendations for your SOP.

To build an SOP based on AWS Resilience Hub recommendations, you must create an CloudFormation template for
the recommended SOPs and include them in your code base.

###### Create an CloudFormation template for the SOP recommendations

1. Open the AWS Resilience Hub console.
2. In the navigation pane, choose **Applications**.
3. From the list of applications, choose the application you want to create an SOP
   for.
4. Choose **Assessments** tab.
5. Select an assessment from the **Resiliency assessments** table. If you
   don't have an assessment, complete the procedure in [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md") and then
   return to this step.
6. Under **Operational recommendations**, choose **Standard
   operating procedures**.
7. Select all the SOP recommendations you want to include.
8. Choose **Create CloudFormation template**. This can take up to a few
   minutes to create the AWS CloudFormation template.

Complete the following procedure to include the SOP recommendations in your code
base.

###### To include the AWS Resilience Hub recommendations in your code base

1. In **Operational recommendations**, choose
   **Templates**.
2. In the list of templates, choose the name of the SOP template you just created.

You can identify the SOPs that are implemented in your application using the following
information:

    * **SOP name** – Name of the SOP that you have defined for your
     application.
    * **Description** – Describes the objective of the SOP.
    * **SSM document** – Amazon S3 URL of the SSM document that
     contains the SOP definition.
    * **Test run** – Amazon S3 URL of the document that contains the
     results of the latest test.
    * **Source template** – Provides the Amazon Resource Name (ARN)
     of the AWS CloudFormation stack that contains the SOP details.

3. Under **Template details**, choose the link in **Templates S3
   Path** to open the template object in Amazon S3 console.
4. In Amazon S3 console, from **Objects** table, choose the SOP folder link.
5. To copy the Amazon S3 path, select the check box in front of the JSON file and choose
   **Copy URL**.
6. Create an AWS CloudFormation stack from AWS CloudFormation console. For more information about creating an
   AWS CloudFormation stack, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md").

While creating the AWS CloudFormation stack, you must provide the Amazon S3 path that you copied from
the previous step.
