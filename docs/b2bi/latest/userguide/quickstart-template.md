# Configure AWS B2B Data Interchange using an CloudFormation template

We provide a basic stack that you can use to quickly configure all the resources you need to work with AWS B2B Data Interchange.

###### To configure B2B Data Interchange objects from a CloudFormation template

1. Download the template from the GitHub repository here:
   [AWS B2B Data Interchange
   basic template](https://github.com/aws-samples/aws-b2b-data-interchange-toolkit/blob/main/templates/aws-b2bi-basic.template.yaml "https://github.com/aws-samples/aws-b2b-data-interchange-toolkit/blob/main/templates/aws-b2bi-basic.template.yaml")
2. Open the CloudFormation console at [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
3. In the left navigation pane, choose **Stacks**.
4. Choose **Create stack**, and then choose **With new
   resources (standard)**.
5. On the **Create stack** page, do the following.
   1. In the **Prerequisite - Prepare template** section, select
      **Choose an existing template**.
   2. In the **Specify template** section, choose **Upload a template file**.
   3. Navigate to your saved template file, and select it.
   4. Choose **Next**.

6. On the **Specify stack details** page, name your stack, and change the names of the listed parameters as appropriate for your configuration.
7. Choose **Next**. On the **Configure stack
   options** page, optionally add tags and an IAM role. Then choose **Next** again.
8. On the **Review and create** page review the details for the stack that you're creating, and then choose
   **Submit**.
   You can view the progress of your stack being creating in the CloudFormation console.
