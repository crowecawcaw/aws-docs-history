AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Create data transfer endpoints for

File Transfer

Data transfer endpoints enable connectivity with the source mainframe, and support high availability,
scalability, and streamlined management of agents. Individual agents are installed on
mainframe LPARs and can be grouped together into a data transfer endpoint. When a request is
made to transfer a dataset, one agent in the data transfer endpoint will handle that
specific transfer. To initiate data transfers, at least one agent on the data transfer
endpoint must be online.

This procedure assumes that you have completed the steps in
[Set up for AWS Mainframe Modernization](setting-up.md "setting-up.md") and [Configure
File Transfer agent on the source mainframe](tutorial-filetransfer-getting-started.md#filetransfer-configure "tutorial-filetransfer-getting-started.md#filetransfer-configure").

## Create data transfer endpoints

To create data transfer endpoints for File Transfer, follow these steps in the AWS Mainframe Modernization
console.

###### To create a data transfer endpoint

1. Open the AWS Mainframe Modernization console at [https://console.aws.amazon.com/m2/](https://console.aws.amazon.com/m2/ "https://console.aws.amazon.com/m2/").
2. In the AWS Region selector, choose the region where you want to transfer
   files from your mainframe to an Amazon S3 bucket.
3. On the **Data transfer endpoints** page, under **File Transfer**,
   choose **Create data transfer endpoint**.
4. On the **Data transfer endpoint prerequisites** page, read
   all the instructions to make sure you have completed these steps on the source
   mainframe. Once confirmed, choose **Next**.
5. On the **Configure data transfer endpoint** page, add basic
   information for your data transfer endpoint.
   1. In the basic information section, enter your data transfer endpoint
      name.

   ###### Note

   The data transfer endpoint name must match the Sysplex name,
   unless you specify a complex name in the agent configuration. 2. An optional description. 3. The KMS key used to encrypt the secret.

   ###### Note

   You must add the following resource-based policy for KMS so the
   AWS Mainframe Modernization service can read and use these keys for
   encryption/decryption:

   ```
   {
     "Sid" : "Enable AWS M2 Permissions",
     "Effect" : "Allow",
     "Principal" : {
         "Service" : "m2.amazonaws.com"
               },
      "Action" : [
          "kms:Encrypt",
          "kms:Decrypt"
                 ],
      "Resource" : "*"
   }
   ```

   4. Specify the **S3 location for intermediate data**,
      which is the intermediate S3 location where transferred datasets from
      the mainframe are stored before they are converted and transferred to
      the target Amazon S3 bucket.

   .

   ###### Note

   It's recommended that you create a new Amazon S3 bucket for your
   transfer tasks. For additional information, see [Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md"). You can also browse your existing
   Amazon S3 buckets by choosing **Browse S3**
   option. 5. After entering required fields, choose
   **Next**.

6. On the **Review and create data transfer endpoint** page,
   check if you have completed prerequisites, and review basic information. Once
   confirmed, choose **Create data transfer endpoint**.

You will be redirected to the **Data transfer endpoints overview** page where you
can see the list of all data transfer endpoints. You will also be able to see the data
transfer endpoints that are available or have failed.

You can also search data transfer endpoints by name and access additional information for each available
agent.
