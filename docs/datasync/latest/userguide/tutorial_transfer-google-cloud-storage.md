# Configuring AWS DataSync transfers

with Google Cloud Storage

With AWS DataSync, you can transfer data between Google Cloud Storage and the following AWS storage services:

- Amazon S3
- Amazon EFS
- Amazon FSx for Windows File Server
- Amazon FSx for Lustre
- Amazon FSx for OpenZFS
- Amazon FSx for NetApp ONTAP
  To begin the transfer setup, create a location for your Google Cloud Storage. This
  location can serve as either your transfer source or destination. A DataSync agent is required
  only when you transfer data between Google Cloud Storage and Amazon EFS or Amazon FSx, or when using
  **Basic mode** tasks. **Enhanced mode** data transfers between Google Cloud Storage and Amazon S3 don't
  require an agent.

###### Note

For private cloud connectivity between Google Cloud Storage and AWS, use Basic mode with agents.

## Overview

DataSync uses the [Google Cloud Storage XML API](https://cloud.google.com/storage/docs/xml-api/overview "https://cloud.google.com/storage/docs/xml-api/overview") for data transfers. This API provides an Amazon S3
compatible interface for reading and writing data with Google Cloud Storage
buckets.

When you use Basic mode for transfers, you can deploy the agent in Google Cloud Storage or your Amazon VPC.

Agent in Google Cloud

1. You deploy a DataSync agent in your Google Cloud environment.
2. The agent reads your Google Cloud Storage bucket by using a
   Hash-based Message Authentication Code (HMAC) key.
3. The objects from your Google Cloud Storage bucket transfer
   securely through TLS 1.3 into the AWS Cloud by using a public
   endpoint.
4. The DataSync service writes the data to your S3 bucket.

The following diagram illustrates the transfer.

![An example DataSync transfer shows how object data transfers from a Google Cloud Storage bucket to an S3 bucket. First, the DataSync agent is deployed in your Google Cloud environment. Then, the DataSync agent reads the Google Cloud Storage bucket. The data moves securely through a public endpoint into AWS, where DataSync writes the objects to an S3 bucket in the same AWS Region where you're using DataSync.](images/diagram-transfer-google-cloud-storage-public.png)

Agent in your VPC

1. You deploy a DataSync agent in a virtual private cloud (VPC) in your
   AWS environment.
2. The agent reads your Google Cloud Storage bucket by using a
   Hash-based Message Authentication Code (HMAC) key.
3. The objects from your Google Cloud Storage bucket transfer
   securely through TLS 1.3 into the AWS Cloud by using a private VPC
   endpoint.
4. The DataSync service writes the data to your S3 bucket.

The following diagram illustrates the transfer.

![An example DataSync transfer shows how object data transfers from a Google Cloud Storage bucket to an S3 bucket. First, the DataSync agent is deployed in a VPC in AWS. Then, the DataSync agent reads the Google Cloud Storage bucket. The data moves securely through a VPC endpoint into AWS, where DataSync writes the objects to an S3 bucket in the same AWS Region as the VPC.](images/diagram-transfer-google-cloud-storage.png)

## Costs

The fees associated with this migration might include:

- Running a Google [Compute Engine](https://cloud.google.com/compute/all-pricing "https://cloud.google.com/compute/all-pricing") virtual machine (VM) instance (if you deploy your
  DataSync agent in Google Cloud)
- Running an [Amazon EC2](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") instance
  (if you deploy your DataSync agent in a VPC within AWS)
- Transferring the data by using [DataSync](https://aws.amazon.com/datasync/pricing/ "https://aws.amazon.com/datasync/pricing/"), including request charges related to [Google Cloud Storage](https://cloud.google.com/storage/pricing "https://cloud.google.com/storage/pricing")
  and [Amazon S3](create-s3-location.md#create-s3-location-s3-requests "create-s3-location.md#create-s3-location-s3-requests") (if S3 is one of
  your transfer locations)
- Transferring data out of [Google Cloud Storage](https://cloud.google.com/storage/pricing "https://cloud.google.com/storage/pricing")
- Storing data in [Amazon S3](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")

## Prerequisites

Before you begin, do the following if you haven’t already:

- [Create a
  Google Cloud Storage bucket](https://cloud.google.com/storage/docs/creating-buckets "https://cloud.google.com/storage/docs/creating-buckets") with the objects that you want to
  transfer to AWS.
- [Sign up for an
  AWS account](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
- [Create an Amazon S3
  bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") for storing your objects after they're in AWS.

## Creating an HMAC key for

your Google Cloud Storage bucket

DataSync uses an HMAC key that's associated with your Google service account to
authenticate with and read the bucket that you’re transferring data from. (For detailed
instructions on how to create HMAC keys, see the
[Google Cloud
Storage documentation](https://cloud.google.com/storage/docs/authentication/hmackeys "https://cloud.google.com/storage/docs/authentication/hmackeys").)

###### To create an HMAC key

1. Create an HMAC key for your Google service account.
2. Make sure that your Google service account has at least `Storage Object
Viewer` permissions.
3. Save your HMAC key's access ID and secret in a secure location.

You'll need these items later to configure your DataSync source location.

## Step 2: Configure your

network

Network configuration is required only when using a DataSync agent with your transfer.
The network requirements for this migration depend on where you choose to deploy your
agent.

If you want to host your DataSync agent in Google Cloud, configure your network
to [allow DataSync transfers through a public
endpoint](datasync-network.md#using-public-endpoints "datasync-network.md#using-public-endpoints").

If you want to host your agent in AWS, you need a VPC with an interface
endpoint. DataSync uses the VPC endpoint to facilitate the transfer.

###### To configure your network for a VPC endpoint

1. If you don't have one, [create
   a VPC](../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC "../../../vpc/latest/userguide/working-with-vpcs.md#Create-VPC") in the same AWS Region as your S3 bucket.
2. [Create a private
   subnet for your VPC](../../../vpc/latest/userguide/create-subnets.md "../../../vpc/latest/userguide/create-subnets.md").
3. [Create a
   VPC service endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") for DataSync.
4. Configure your network to [allow
   DataSync transfers through a VPC service endpoint](datasync-network.md#using-vpc-endpoint "datasync-network.md#using-vpc-endpoint").

To do this, modify the [security
group](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") that's associated with your VPC service
endpoint.

## Step 3: Create a DataSync

agent (optional)

A DataSync agent is only required when using **Basic** mode tasks. If
you are using **Enhanced** mode to transfer between Google Cloud
Storage (GCS) and Amazon S3, then no agent is required. If you want to use
**Basic** mode, then you need a DataSync agent that can access your
GCS bucket.

In this scenario, the DataSync agent runs in your Google Cloud
environment.

**Before you begin**: [Install the Google Cloud
CLI](https://cloud.google.com/sdk/docs/install "https://cloud.google.com/sdk/docs/install").

###### To create the agent for Google Cloud

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, choose **Agents**, then
   choose **Create agent**.
3. For **Hypervisor**, choose **VMware
   ESXi**, then choose **Download the image**
   to download a
   `.zip`
   file that contains the agent.
4. Open a terminal. Unzip the image by running the following
   command:

```
unzip AWS-DataSync-Agent-VMWare.zip
```

5. Extract the contents of the agent's `.ova` file
   beginning with `aws-datasync` by running the
   following command:

```
tar -xvf aws-datasync-2.0.1655755445.1-x86_64.xfs.gpt.ova
```

6. Import the agent's `.vmdk` file into Google Cloud
   by running the following Google Cloud CLI command:

```
gcloud compute images import aws-datasync-2-test \
   --source-file INCOMPLETE-aws-datasync-2.0.1655755445.1-x86_64.xfs.gpt-disk1.vmdk \
   --os centos-7
```

###### Note

Importing the `.vmdk` file might take up to two
hours. 7. Create and start a VM instance for the agent image that you just
imported.

The instance needs the following configurations for your agent. (For
detailed instructions on how to create an instance, see the [Google Cloud
Compute Engine documentation](https://cloud.google.com/compute/docs/instances "https://cloud.google.com/compute/docs/instances").)

    * For the machine type, choose one of the following:




    	+ **e2-standard-8** – For DataSync
    	 task executions working with up to 20 million
    	 objects.
    	+ **e2-standard-16** – For DataSync
    	 task executions working with more than 20 million
    	 objects.
    * For the boot disk settings, go to the custom images section.
     Then choose the DataSync agent image that you just imported.
    * For the service account setting, choose your Google service
     account (the same account that you used in [Step
     1](#transfer-google-cloud-storage-create-hmac-key "#transfer-google-cloud-storage-create-hmac-key")).
    * For the firewall setting, choose the option to allow
     HTTP
     (port 80) traffic.


    To activate your DataSync agent, port
     80 must be open on
     the agent. The port doesn't need to be publicly accessible. Once
     activated, DataSync closes the port.

8. After the VM instance is running, take note of its public IP
   address.

You'll need this IP address to activate the agent. 9. Go back to the DataSync console. On the **Create agent**
screen where you downloaded the agent image, do the following to
activate your agent:

    * For **Endpoint type**, choose the public
     service endpoints option (for example, **Public service
     endpoints in US East Ohio**).
    * For **Activation key**, choose
     **Automatically get the activation key from your
     agent**.
    * For **Agent address**, enter the public IP
     address of the agent VM instance that you just created.
    * Choose **Get key**.

10. Give your agent a name, and then choose **Create
    agent**.
    Your agent is online and ready to transfer data.

In this scenario, the agent runs as an Amazon EC2 instance in a VPC that's
associated with your AWS account.

**Before you begin**: [Set up the
AWS Command Line Interface (AWS CLI)](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md").

###### To create the agent for your VPC

1. Open a terminal. Make sure to configure your AWS CLI profile to use the
   account
   that's
   associated with your S3
   bucket.
2. Copy the following command. Replace
   `vpc-region` with the
   AWS Region where your VPC resides (for example,
   `us-east-1`).

```
aws ssm get-parameter --name /aws/service/datasync/ami --region `vpc-region`
```

3. Run the command. In the output, take note of the `"Value"`
   property.

This value is the DataSync Amazon Machine Image (AMI) ID of the Region
that you specified. For example, an AMI ID could look like
`ami-1234567890abcdef0`. 4. Copy the following URL. Again, replace
`vpc-region` with the
AWS Region where your VPC resides. Then, replace
`ami-id` with the AMI ID
that you noted in the previous step.

```
https://console.aws.amazon.com/ec2/v2/home?region=`vpc-region`#LaunchInstanceWizard:ami=`ami-id`
```

5. Paste the URL into a browser.

The Amazon EC2 instance launch page in the AWS Management Console displays. 6. For **Instance type**, choose one of the [recommended Amazon EC2 instances for DataSync
agents](agent-requirements.md#ec2-instance-types "agent-requirements.md#ec2-instance-types"). 7. For **Key pair**, choose an existing key pair, or
create a new one. 8. For **Network settings**, choose the VPC and subnet
where you want to deploy the agent. 9. Choose **Launch instance**. 10. Once the Amazon EC2 instance is running, [choose your VPC endpoint](choose-service-endpoint.md#datasync-in-vpc "choose-service-endpoint.md#datasync-in-vpc"). 11. [Activate your agent](activate-agent.md "activate-agent.md").

## Step 4: Create a DataSync

source location for your Google Cloud Storage bucket

To set up a DataSync location for your Google Cloud Storage bucket, you need the access
ID and secret for the HMAC key that you created in [Step 1](#transfer-google-cloud-storage-create-hmac-key "#transfer-google-cloud-storage-create-hmac-key").

###### To create the DataSync source location

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**,
   then choose **Locations** and **Create
   location**.
3. For **Location type**, choose **Object
   storage**.
4. For **Server**, enter
   `storage.googleapis.com`.
5. For **Bucket name**, enter the name of your Google Cloud
   Storage bucket.
6. For **Folder**, enter an object prefix.

DataSync only copies objects with this prefix. 7. If your transfer requires an agent, choose **Use agents**,
then choose the agent that you created in [Step 3](#transfer-google-cloud-storage-create-agent "#transfer-google-cloud-storage-create-agent"). 8. Expand **Additional settings**. For **Server
protocol**, choose **HTTPS**. For **Server
port**, choose **443**. 9. Scroll down to the **Authentication** section. Make sure that
the **Requires credentials** check box is selected, and then do
the following:

    * For **Access key**, enter your HMAC key's access
     ID.
    * For **Secret key**, either enter your HMAC key's
     secret key directly, or specify an AWS Secrets Manager secret that contains the
     key. For more information, see [Providing
     credentials for storage locations](location-credentials.md "location-credentials.md").

10. Choose **Create location**.

## Step 5: Create a

DataSync destination location for your S3 bucket

You need a DataSync location for where you want your data to end up.

###### To create the DataSync destination location

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**,
   then choose **Locations** and **Create
   location**.
3. [Create a DataSync location for the S3
   bucket](create-s3-location.md "create-s3-location.md").

If you deployed the DataSync agent in your VPC, this tutorial assumes that the S3
bucket is in the same AWS Region as your VPC and DataSync agent.

## Step 6: Create and start a

DataSync task

With your source and destinations locations configured, you can start moving your data
into AWS.

###### To create and start the DataSync task

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/").
2. In the left navigation pane, expand **Data transfer**, then choose **Tasks**, and
   then choose **Create task**.
3. On the **Configure source location** page, do the
   following:
   1. Choose **Choose an existing location**.
   2. Choose the source location that you created in [Step 4](#transfer-google-cloud-storage-create-source "#transfer-google-cloud-storage-create-source"),
      then choose **Next**.

4. On the **Configure destination location** page, do the
   following:
   1. Choose **Choose an existing location**.
   2. Choose the destination location that you created in [Step
      5](#transfer-google-cloud-storage-create-destination "#transfer-google-cloud-storage-create-destination"), then choose **Next**.

5. On the **Configure settings** page, do the following:
   1. Under **Data transfer configuration**, expand
      **Additional settings** and clear the
      **Copy object tags** check box.

   ###### Important

   Because the Google Cloud Storage XML API does not support reading
   or writing object tags, your DataSync task might fail if you try to
   copy object tags. 2. Configure any other task settings that you want, and then choose
   **Next**.

6. On the **Review** page, review your settings, and then choose
   **Create task**.
7. On the task's details page, choose **Start**, and then choose
   one of the following:
   - To run the task without modification, choose **Start with
     defaults**.
   - To modify the task before running it, choose **Start with
     overriding options**.

When your task finishes, you'll see the objects from your Google Cloud Storage bucket
in your S3 bucket.
