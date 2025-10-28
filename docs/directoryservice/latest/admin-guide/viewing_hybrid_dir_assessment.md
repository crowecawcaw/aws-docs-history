# Viewing directory assessments

You can view directory assessments in the AWS Management Console to review assessment results and manage your
assessment reports.

###### To view a directory assessment

1. Open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. On the **Directories** page, under the **Trial hybrid
   directory assessments** section, choose the assessment you want to
   view. This opens the assessment details page.
3. On the assessment details page, you can choose:
   - **Download** to download the directory assessment report as a CSV
     file.
   - **Delete** to delete the directory assessment report.
   - **Create assessment** to create a new directory assessment.

4. From the assessment details page, you can view the following
   information:
   1. Assessment information, such as the assessment ID, status, whether it
      was created by the customer or system, and when it was last
      updated.
   2. Self-managed AD details such as the DNS name, VPC, and subnets.
   3. AWS Systems Manager managed node information, such as IP address, assessment
      status, and the number of passed and failed assessment tests.
   4. Assessment status for domain controllers. You can also review
      assessment test details by choosing the domain controllers. Error codes
      appear in the **Status** column for failed assessment
      tests.
