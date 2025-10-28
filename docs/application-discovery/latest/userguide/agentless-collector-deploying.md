AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Deploying

Application Discovery Service Agentless Collector

To deploy Application Discovery Service Agentless Collector, you must first create an IAM user and
download the collector. This page walks you through the steps to take to deploy a
collector.

## Create an IAM user for

Agentless Collector

To use Agentless Collector, in the AWS account that you used in [Sign in to the Migration Hub console and
choose a home Region](setting-up.md#setting-up-choose-home-region "setting-up.md#setting-up-choose-home-region"), you must create an AWS Identity and Access Management
(IAM) user. Then, set up this IAM user to use the following AWS managed policy
[AWSApplicationDiscoveryAgentlessCollectorAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSApplicationDiscoveryAgentlessCollectorAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSApplicationDiscoveryAgentlessCollectorAccess"). You attach this IAM
policy when you create the IAM user.

To use the database and analytics data collection module, create two customer
managed IAM policies. These policies provide access your Amazon S3 bucket and the AWS DMS
API. For more information, see [Create a customer
managed policy](../../../IAM/latest/UserGuide/tutorial_managed-policies.md "../../../IAM/latest/UserGuide/tutorial_managed-policies.md") in the _IAM User Guide_.

- Use the following JSON code to create the
  `DMSCollectorPolicy` policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect": "Allow",
 "Action": [
 "dms:DescribeFleetAdvisorCollectors",
 "dms:ModifyFleetAdvisorCollectorStatuses",
 "dms:UploadFileMetadataList"
 ],
 "Resource": "*"
 }]
}`

```

- Use the following JSON code to create the
  `FleetAdvisorS3Policy` policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject*",
 "s3:GetBucket*",
 "s3:List*",
 "s3:DeleteObject*",
 "s3:PutObject*"
 ],
 "Resource": [
 "arn:aws:s3:::`bucket_name`",
 "arn:aws:s3:::`bucket_name`/*"
 ]
 }
 ]
}`

```

In the preceding example, replace
`bucket_name` with the name of
the Amazon S3 bucket that you created in the prerequisites step.

We recommend that you create a non-administrative IAM user to use with
Agentless Collector. When creating non-administrative IAM users, follow
the security best practice [Grant Least
Privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege"), granting users minimum permissions.

###### To create a non-administrator IAM user to use with

Agentless Collector

1. In AWS Management Console, navigate to the IAM console, using the AWS account that
   you used to set the home Region in [Sign in to the Migration Hub console and
   choose a home Region](setting-up.md#setting-up-choose-home-region "setting-up.md#setting-up-choose-home-region").
2. Create a non-administrator IAM user by following the instructions for
   creating a user with the console as described in [Creating an IAM user in your
   AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the _IAM User Guide_.

While following the instructions in the
_IAM User Guide_:

    * When on the step about selecting the type of access, select
     **Programmatic access**. Note, while not
     recommended, only select **AWS Management Console
     access** if you plan to use the same IAM user
     credentials for accessing the AWS console.
    * When on the step about the **Set permission**
     page, choose the option to **Attach existing policies to
     user directly**. Then select the
     `AWSApplicationDiscoveryAgentlessCollectorAccess`
     AWS managed policy from the list of policies.


    Next, select the `DMSCollectorPolicy` and
     `FleetAdvisorS3Policy` customer managed IAM
     policies.
    * When on the step about viewing the user's access keys (access key
     IDs and secret access keys), follow the guidance in the
     **Important** note about saving the user's new
     access key ID and secret access key in a safe and secure place.
     You'll need these access keys in [Configuring
     Agentless Collector](agentless-collector-gs-configure.md "agentless-collector-gs-configure.md").


    It's an AWS security best practice to rotate access keys. For
     information about rotating keys, see  [Rotate access keys regularly for use cases that require
     long-term credentials](../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials "../../../IAM/latest/UserGuide/best-practices.md#rotate-credentials") in the
     *IAM User Guide.*

## Download the

Agentless Collector

To set up the Application Discovery Service Agentless Collector (Agentless Collector), you
must download and deploy the Agentless Collector Open Virtualization
Archive (OVA) file. The Agentless Collector is a virtual appliance that you
install in your on-premises VMware environment. This step describes how to download
the collector OVA file and the next step describes how to deploy it.

###### To download the collector OVA file and verify its checksum

1. Sign in to vCenter as a VMware administrator and switch to the directory
   where you want to download the Agentless Collector OVA file.
2. Download the OVA file from the following URL:

[Agentless Collector OVA](https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova "https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova") 3. Depending on which hashing algorithm you use in your system environment,
download either the [MD5](https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova.md5 "https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova.md5") or [SHA256](https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova.sha256 "https://s3.us-west-2.amazonaws.com/aws.agentless.discovery.collector.bundle/releases/latest/ApplicationDiscoveryServiceAgentlessCollector.ova.sha256") to get the file containing the checksum value. Use the
downloaded value to verify the
`ApplicationDiscoveryServiceAgentlessCollector` file
downloaded in the preceding step. 4. Depending on your variation of Linux, run the version appropriate MD5
command or SHA256 command to verify that the cryptographic signature of the
`ApplicationDiscoveryServiceAgentlessCollector.ova`
file matches the value in the respective MD5/SHA256 file that you
downloaded.

```
$ md5sum ApplicationDiscoveryServiceAgentlessCollector.ova
```

```
$ sha256sum ApplicationDiscoveryServiceAgentlessCollector.ova
```

## Deploy

Agentless Collector

Application Discovery Service Agentless Collector (Agentless Collector) is a virtual
appliance that you install in your on-premises VMware environment. This section
describes how to deploy the Open Virtualization Archive (OVA) file that you
downloaded in your VMware environment.

**Agentless Collector virtual machine
specifications**

Agentless Collector version 2

- **Operating System** –
  Amazon Linux 2023
- **RAM** – 16 GB
- **CPU** – 4 cores
- **VMware requirements** –
  See [VMware host requirements for running AL2023 on
  VMware](../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements "../../../linux/al2023/ug/vmware-supported-configurations.md#vmware-host-requirements")

Agentless Collector version 1

- **Operating System** –
  Amazon Linux 2
- **RAM** – 16 GB
- **CPU** – 4 cores

The following procedure steps you through deploying the
Agentless Collector OVA file in your VMware environment.

###### To deploy Agentless Collector

1.  Sign in to vCenter as a VMware administrator.
2.  Use one of the following ways to install the OVA file:
    - Use the UI: Choose **File**, choose
      **Deploy OVF Template**, select the collector
      OVA file you downloaded in the previous section, and then complete
      the wizard. Ensure the proxy settings in the server management
      dashboard are configured correctly.
    - Use the command line: To install the collector OVA file from the
      command line, download and use the VMware Open Virtualization Format
      Tool (ovftool). To download ovftool, select a release from the
      [OVF
      Tool Documentation](https://www.vmware.com/support/developer/ovf/ "https://www.vmware.com/support/developer/ovf/") page.

    The following is an example of using the ovftool command line tool
    to install the collector OVA file.

    ```
    ovftool --acceptAllEulas --name=`AgentlessCollector` --datastore=`datastore1` -dm=thin `ApplicationDiscoveryServiceAgentlessCollector.ova` 'vi://`username:password@vcenterurl/Datacenter/host/esxi/`'
    ```

    ###### The following describe the

    `replaceable` values in the
    example

        + The name is the name that you want to use for your
         Agentless Collector VM.
        + The datastore is the name of the datastore in your
         vCenter.
        + The OVA file name is the name of the downloaded collector
         OVA file.
        + The username/password are your vCenter credentials.
        + The vcenterurl is the URL of your vCenter.
        + The vi path is the path to your VMware ESXi host.

3.  Locate the deployed Agentless Collector in your vCenter.
    Right-click the VM, and then choose **Power**,
    **Power On**.
4.  After a few minutes, the IP address of the collector displays in vCenter.
    You use this IP address to connect to the collector.
