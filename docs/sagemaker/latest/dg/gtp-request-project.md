# Request a Project

Requesting a new Amazon SageMaker Ground Truth Plus project initiates the engagement with the
SageMaker Ground Truth Plus team who works to understand your requirements and deliver a high-quality,
labeled dataset that is tailored to your use case. In the project request, you
can provide details about your labeling task, such as the task type, dataset size,
and any sensitive data. You also need to specify an AWS IAM role with permissions
for SageMaker Ground Truth Plus to access your data and perform the labeling job. The following page shows
you how to create a new project request using the SageMaker AI console.

To request a project, do the following:

1. Under the Ground Truth tab of Amazon SageMaker AI, choose **Plus**.
2. On the **SageMaker Ground Truth Plus** page, choose **Request project**.
3. A page titled **Request a project** opens. The page includes fields for
   **General information** and **Project overview**. Enter the following information
   1. Under **General information**, enter your **First name**,
      **Last name** and **Business email address**.
      An AWS expert uses this information for contacting you to discuss the project after you submit the request.
   2. Under **Project overview**, enter your **Project name** and **Project description**.
      Choose the **Task type** based on your data and use case.
      You can also indicate if your data contains personally identifiable information (PII).
   3. Create or select an IAM role that grants SageMaker Ground Truth Plus permissions to perform a labeling job by choosing one of the options below.
      1. You can **Create an IAM role** that provides access to any S3 bucket you specify.
      2. You can **Enter a custom IAM role ARN**.
      3. You can choose an existing role.
      4. If you use an existing role or a custom IAM role ARN, make sure you have the following IAM role and trust policy.

      IAM role

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement": [
       {
       "Effect": "Allow",
       "Action": [
       "s3:GetObject",
       "s3:GetBucketLocation",
       "s3:ListBucket",
       "s3:PutObject"
       ],
       "Resource": [
       "arn:aws:s3:::`your-bucket-name`",
       "arn:aws:s3:::`your-bucket-name`/*"
       ]
       }
       ]
      }`

      ```

      Trust policy

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement": [
       {
       "Effect": "Allow",
       "Principal": {
       "Service": "sagemaker-ground-truth-plus.amazonaws.com"
       },
       "Action": "sts:AssumeRole"
       }
       ]
      }`

      ```

4. Choose **Request a project**.
   Once you create a project, you can find it on the **SageMaker Ground Truth Plus** page,
   under the Projects section. The project status should be **Review in-progress**

###### Note

You cannot have more than 5 projects with the **Review in progress** status.
