# Transferring to or from S3 compatible storage on

Snowball Edge

With AWS DataSync, you can transfer objects between [Amazon S3 compatible storage
on an AWS Snowball Edge](../../../snowball/latest/developer-guide/s3compatible-on-snow.md "../../../snowball/latest/developer-guide/s3compatible-on-snow.md") device or cluster and any of the following AWS
storage services:

- [Amazon S3](../../../s3/index.md "../../../s3/index.md")
- [Amazon Elastic File System (Amazon EFS)](../../../efs/latest/ug/whatisefs.md "../../../efs/latest/ug/whatisefs.md")
- [Amazon FSx for Windows File Server](../../../fsx/latest/WindowsGuide/what-is.md "../../../fsx/latest/WindowsGuide/what-is.md")
- [Amazon FSx for Lustre](../../../fsx/latest/LustreGuide/what-is.md "../../../fsx/latest/LustreGuide/what-is.md")
- [Amazon FSx for OpenZFS](../../../fsx/latest/OpenZFSGuide/what-is-fsx.md "../../../fsx/latest/OpenZFSGuide/what-is-fsx.md")
- [Amazon FSx for NetApp ONTAP](../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/what-is-fsx-ontap.md")

## Prerequisites

Before you get started, make sure that you've done the following:

- Created an AWS storage resource in the AWS Region where you plan to
  transfer data to or from. For example, this could be an S3 bucket or Amazon EFS file
  system in US East (N. Virginia).
- Established a wide-area network (WAN) connection for traffic into and out of
  your on-premises storage environment. For example, you can establish this kind
  of connection with [AWS Direct Connect](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md").

When you [create your DataSync
agent](#create-agent-s3-compatible-storage "#create-agent-s3-compatible-storage"), you'll configure this WAN connection so that DataSync can
transfer data between your Amazon S3 compatible storage that's on-premises and your
storage resource in AWS.

- Downloaded and installed the [Snowball Edge client](https://aws.amazon.com/snowball/resources/ "https://aws.amazon.com/snowball/resources/").

## Providing DataSync access to S3

compatible storage

To access your Amazon S3 compatible storage bucket, DataSync needs the following:

- User credentials on your Snowball Edge device or cluster that can access the
  bucket that you're transferring data to or from.
- An HTTPS certificate that allows DataSync to verify the authenticity of the
  connection between the DataSync agent and the `s3api` endpoint on your
  device or cluster.

###### Topics

- [Getting
  the user credentials to access your S3 bucket](#get-credentials-snowballedge "#get-credentials-snowballedge")
- [Getting a certificate for the
  s3api endpoint connection](#get-certificate-snowballedge "#get-certificate-snowballedge")

### Getting

the user credentials to access your S3 bucket

DataSync needs the access key and secret key for a user who can access the bucket
that you're working with on your Snowball Edge device or cluster.

###### To get the user credentials to access your bucket

1. Open a terminal and run the Snowball Edge client.

For more information about running the Snowball Edge client, see [Using the
Snowball Edge client](../../../snowball/latest/developer-guide/using-client.md "../../../snowball/latest/developer-guide/using-client.md") in the _AWS Snowball Edge Developer Guide_. 2. To get the access keys associated with your device or cluster, run the
following `snowballEdge` command:

```
snowballEdge list-access-keys
```

3. In the output, locate the access key for the bucket that DataSync will work
   with (for example, `AKIAIOSFODNN7EXAMPLE`).
4. To get the secret access key, run the following `snowballEdge`
   command. Replace
   `access-key-for-datasync` with the
   access key that you located in the prior step.

```
snowballEdge get-secret-access-key --access-key-id `access-key-for-datasync`
```

The output includes the access key's corresponding secret key (for
example, `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`). 5. Save the access key and secret key somewhere that you can remember.

You will need these keys when you're [configuring the DataSync
source location](#s3-compatible-storage-source-location "#s3-compatible-storage-source-location") for your transfer.

### Getting a certificate for the

`s3api` endpoint connection

You need an HTTPS certificate that can verify the authenticity of the connection
between your DataSync agent and an `s3api` endpoint on your Snowball Edge
device or cluster.

###### To get a certificate for the `s3api` endpoint connection

1. In the Snowball Edge client, run the following
   `list-certificates` command:

```
snowballEdge list-certificates
```

In the output, take note of the `CertificateArn` value. This is
the certificate's Amazon Resource Name (ARN). You need the ARN to get the
certificate's contents. 2. Run the following `get-certificate` command that specifies the
certificate ARN that you just retrieved:

```
snowballEdge get-certificate --certificate-arn arn:aws:snowball-device:::certificate/`78EXAMPLE516EXAMPLEf538EXAMPLEa7`
```

3. Copy the output, including the `BEGIN CERTIFICATE` and
   `END CERTIFICATE` lines, and save it as a
   `.pem` file.

**Example of `get-certificate`
output:**

```
-----BEGIN CERTIFICATE-----
`Certificate`
-----END CERTIFICATE-----
```

You specify this `.pem` file when [creating the DataSync source
location](#s3-compatible-storage-source-location "#s3-compatible-storage-source-location") for your transfer.

## Creating a DataSync agent in your

on-premises storage environment

During a transfer, DataSync uses an [agent](how-datasync-transfer-works.md#sync-agents "how-datasync-transfer-works.md#sync-agents") to read from
or write to the Amazon S3 compatible storage on your Snowball Edge device or cluster.

This agent must be deployed in your on-premises storage environment where it can
connect to your device or cluster through your network. For example, you can run the
agent on a VMware ESXi hypervisor that has local network access to your cluster.

###### To create a DataSync agent in your on-premises storage environment

1. Make sure that the [DataSync agent can run on
   your hypervisor](agent-requirements.md#hosts-requirements "agent-requirements.md#hosts-requirements") and that you [allocate the agent enough
   virtual machine (VM) resources](agent-requirements.md#agent-tranfer-resource-requirements "agent-requirements.md#agent-tranfer-resource-requirements").
2. Deploy the agent in your on-premises environment.

For instructions, see one of the following topics, depending on the type of
hypervisor that you're deploying the agent on:

    * [Deploy your agent on
     VMware](deploy-agents.md#create-vmw-agent "deploy-agents.md#create-vmw-agent")
    * [Deploy your agent on Linux
     Kernel-based Machine (KVM)](deploy-agents.md#create-kvm-agent "deploy-agents.md#create-kvm-agent")
    * [Deploy your agent on Microsoft
     Hyper-V](deploy-agents.md#create-hyper-v-agent "deploy-agents.md#create-hyper-v-agent")
    * [Deploy your agent on
     Amazon EC2](deploy-agents.md#ec2-deploy-agent "deploy-agents.md#ec2-deploy-agent")


    ###### Warning

    We don't recommend deploying an agent on Amazon EC2 agent to access
     on-premises storage because of increased network latency.

3. Configure your network to allow the following traffic between the agent and
   your Amazon S3 compatible storage:

| From           | To                                                                                                                                              | Protocol and port |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DataSync agent | A virtual network interface (VNI) for an `s3api` endpoint on your device or cluster. If you have a cluster, it can be any `s3api` endpoint VNI. | TCP 443 (HTTPS)   | If you need to find a VNI on your device or cluster, see [describing your virtual network interfaces](../../../snowball/latest/developer-guide/using-ec2-edge-client.md#ec2-edge-describe-vnic "../../../snowball/latest/developer-guide/using-ec2-edge-client.md#ec2-edge-describe-vnic") on Snowball Edge. 4. [Choose a service endpoint](choose-service-endpoint.md "choose-service-endpoint.md") that the agent uses to communicate with the DataSync service. 5. [Activate your agent](activate-agent.md "activate-agent.md"). ## Configuring the source location for your transfer After you create your agent, you can configure the source location for your DataSync transfer. ###### Note The following instructions assume that you're transferring from Amazon S3 compatible storage, but you can also use this location for a transfer destination. ###### To configure the source location by using the DataSync console 1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/ "https://console.aws.amazon.com/datasync/"). 2. In the left navigation pane, expand **Data transfer**. Choose **Tasks**, and then choose **Create task**. 3. On the **Configure source location** page, choose **Create a new location**. 4. For **Location type**, choose **Object storage**. 5. For **Agents**, choose the DataSync agent that you created in your on-premises storage environment. 6. For **Server**, enter the VNI for the `s3api` endpoint that's used by your Amazon S3 compatible storage. If you have a Snowball Edge cluster instead of a single device, you can specify any of the cluster's `s3api` endpoint VNIs. 7. For **Bucket name**, enter the name of the Amazon S3 compatible storage bucket that you're transferring objects from. 8. For **Folder**, enter an object prefix. DataSync only transfers objects with this prefix. 9. To configure the DataSync connection to the Snowball Edge device or cluster, expand **Additional settings** and do the following: 1. For **Server protocol**, choose **HTTPS**. 2. For **Server port**, enter `443`. 3. For **Certificate**, choose the certificate file for the [s3api endpoint connection](#get-certificate-snowballedge "#get-certificate-snowballedge"). 10. Select **Requires credentials**, and enter the **Access key** and **Secret key** to [access the Amazon S3 compatible storage bucket](#get-credentials-snowballedge "#get-credentials-snowballedge") on your Snowball Edge device or cluster. 11. Choose **Next**. ## Configuring the destination location for your transfer Your transfer's destination location must be in the same AWS Region and AWS account where you created your agent. **Before you begin**: Make sure you've [configured the source location](#s3-compatible-storage-source-location "#s3-compatible-storage-source-location") for your transfer. ###### To configure the destination location for your transfer by using the DataSync console 1. On the **Configure destination location** page, choose **Create a new location** or **Choose an existing location** for the AWS storage resource where you're transferring objects to. If you're creating a new location, see one of the following topics: <br>• [Amazon S3](create-s3-location.md "create-s3-location.md") <br>• [Amazon EFS](create-efs-location.md "create-efs-location.md") <br>• [FSx for Windows File Server](create-fsx-location.md "create-fsx-location.md") <br>• [FSx for Lustre](create-lustre-location.md "create-lustre-location.md") <br>• [FSx for OpenZFS](create-openzfs-location.md "create-openzfs-location.md") <br>• [FSx for ONTAP](create-ontap-location.md "create-ontap-location.md") 2. When you're done configuring the destination location, choose **Next**. ## Configuring your transfer settings With DataSync, you can specify a transfer schedule, customize how your data integrity is verified, and specify whether you want to transfer only a subset of objects, among other options. **Before you begin**: Make sure you've [configured the destination location](#s3-compatible-storage-destination-location "#s3-compatible-storage-destination-location") for your transfer. ###### To configure your transfer settings by using the DataSync console 1. On the **Configure settings** page, change the transfer settings or use the defaults. For more information about these settings, see [Choosing what AWS DataSync transfers](task-options.md "task-options.md"). 2. Choose **Next**. 3. Review your transfer details, and then choose **Create task**. ## Starting your transfer After you create your transfer task, you're ready to start moving data. For instructions on starting a task by using the DataSync console or AWS CLI, see [Starting your task](run-task.md#starting-task "run-task.md#starting-task"). ## Limitations <br>• If your source storage system uses the NFS protocol (such as Amazon EFS), DataSync can't transfer files with hard links to a Snowball Edge device. <br>• DataSync can’t transfer objects that are longer than 1,024 bytes from a Snowball Edge device to an S3 bucket. For more information, see the _[Amazon S3 User Guide](../../../AmazonS3/latest/userguide/object-keys.md "../../../AmazonS3/latest/userguide/object-keys.md")_. |
