# Providing your own custom scripts

Scripts perform the extract, transform, and load (ETL) work in AWS Glue. A script is
created when you automatically generate the source code logic for a job. You can either edit
this generated script, or you can provide your own custom script.

###### To provide your own custom script in AWS Glue, follow these general steps:

1. Sign in to the AWS Management Console and open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
2. Choose the **ETL Jobs** tab, and then view the **Create job**
   section. Choose a **script editor** option.
3. Under **This job runs**, choose one of the following:
   - **Create a new script with boilerplate code**
   - **Upload and edit an existing script**

4. On the **Job details** page, choose the **IAM role** that is
   required for your custom script to run. For more information, see [Identity and access management for AWS Glue](security-iam.md "security-iam.md").
5. Choose any connections that your script references. These objects are needed to
   connect to the necessary JDBC data stores.

An elastic network interface is a virtual network interface that you can attach to
an instance in a virtual private cloud (VPC). Choose the elastic network interface
that is required to connect to the data store that's used in the script. 6. Provide additional configuration, including parameters, specific to your job type. For more
information about configuration for your job type, see the [Building visual ETL jobs](author-job-glue.md "author-job-glue.md")
section. 7. On the **Script** tab, paste or write your custom script.
Use the content in this section to guide the process of writing your custom script.

For more information about adding jobs in AWS Glue, see [Building visual ETL jobs](author-job-glue.md "author-job-glue.md").

For step-by-step guidance, see the **Add job** tutorial in the AWS Glue
console.
