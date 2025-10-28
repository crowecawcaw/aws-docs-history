# Connect to source code in Amazon S3

You can connect AWS Transform to source code in Amazon S3 as an alternative to [connecting a source code repo](dotnet-creating-repo-connector.md "dotnet-creating-repo-connector.md").

## S3 bucket organization

Original source code and transformed code are stored in a common S3 bucket, organized as shown below. You must set up your S3 bucket in the same region as your AWS Transform job. Upload your source code to the bucket as a zip file. The zip file must contain a top level folder for each repository.

During transformation, AWS Transform creates a transform-output folder, and stores the transformation results in that folder. Transformation creates a zip file named _transformed-code.zip_ containing the transformed code. This includes a code differences report file name diff.txt that highlights file changes at a project level.

```

<customer-bucket>/
├── source-code.zip
         ├── repo 1
         ├── repo 2
         ├── ......
         ├── repo n
└── transform-output/
      ├── transformed-code.zip

```

## Adding a new S3 Connector

To create a new S3 source code repository connector:

1. In the AWS console, create an S3 bucket.
2. Upload your source code as a zip file to the S3 bucket.
3. In the AWS Transform web app, start a .NET transformation job. In the **Connect a source code repository** step, select **Connect your source code in S3 bucket** and choose **Save**.
4. On the next page, enter your S3 bucket details and choose **Submit**.
   1. Connector name
   2. AWS Account ID
   3. S3 Bucket Arn
   4. S3 Bucket Encryption Key (optional)

5. Approve the connector:
   1. On the next page, copy the verification link.
   2. Have an approver browse to the link to reach the AWS Transform connector creation request page.
   3. Choose to create a new role or use an existing role.
   4. After reviewing the request, choose **Save** and **Approve** to approve it.

6. Specify the S3 zip file location:
   1. In the AWS Transform web app, wait for status to show **Approved**.
   2. On the **Specify asset location** page, enter an S3 URL for the code zip file in the format `s3://bucket-name/zip-file-name` and choose **Send to AWS Transform**.
   3. The job proceeds to the **Discovery** step to continue the transformation.

## Deleting an S3 Connector

To delete an existing S3 connector:

1. In the AWS Transform web app, select **Manage connectors** at the top right.
2. In the **Manage connectors** window, select the connector.
3. Choose **Delete**.
