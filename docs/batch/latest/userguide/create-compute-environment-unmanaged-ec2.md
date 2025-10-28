# Tutorial: Create an unmanaged

compute environment using Amazon EC2 resources

Complete the following steps to create an unmanaged compute environment using Amazon Elastic Compute Cloud
(Amazon EC2) resources.

######

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the AWS Region to use.
3. On the **Compute Environments** page, choose
   **Create**.
4. Configure the environment.
   1. For **Compute environment configuration**, choose
      **Amazon Elastic Compute Cloud (Amazon EC2)**.
   2. For **Orchestration type**, choose
      **Unmanaged**.

5. For **Name**, specify a unique name for your compute environment. The
   name can be up to 128 characters in length. It can contain uppercase and lowercase
   letters, numbers, hyphens (-), and underscores (\_).
6. For **Service role**, choose a role that lets the AWS Batch service
   make calls to the required AWS API operations on your behalf.

###### Note

You can't use `AWSServiceRoleForBatch` for unmanaged compute
environments. 7. For **Maximum vCPUs**, choose the maximum number of vCPUs that your
compute environment can scale out to, regardless of job queue demand. 8. (Optional) Expand **Tags**. To add a tag, choose **Add
tag**. Then, enter a **Key** name and optional
**Value**. Choose **Add tag**. For more information,
see [Tag your AWS Batch resources](using-tags.md "using-tags.md"). 9. Choose **Next page**. 10. For **Review**, review the configuration steps. If you
need to make changes, choose **Edit**. When you're finished,
choose **Create compute environment**.
