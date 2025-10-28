Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Create and activate an

Amazon FSx File Gateway

In this section, you can find instructions on how to create, deploy, and activate a
File Gateway in AWS Storage Gateway.

###### Topics

- [Set up an Amazon FSx File Gateway](#set-up-gateway-fsx-file "#set-up-gateway-fsx-file")
- [Connect your Amazon FSx File Gateway to
  AWS](#connect-to-amazon-fsx-file "#connect-to-amazon-fsx-file")
- [Review settings and activate your
  Amazon FSx File Gateway](#review-and-activate-fsx-file "#review-and-activate-fsx-file")
- [Configure your Amazon FSx File Gateway](#configure-gateway-fsx-file "#configure-gateway-fsx-file")

## Set up an Amazon FSx File Gateway

###### To set up a new FSx File Gateway

1. Open the AWS Management Console at [https://console.aws.amazon.com/storagegateway/home/](https://console.aws.amazon.com/storagegateway/home/ "https://console.aws.amazon.com/storagegateway/home/"), and choose the
   AWS Region where you want to create your gateway.
2. Choose **Create gateway** to open the **Set up
   gateway** page.
3. In the **Gateway settings** section, do the
   following:
   1. For **Gateway name**, enter a name for your
      gateway. After your gateway is created, you can search for this name
      to find your gateway on the list pages in the AWS Storage Gateway
      console.
   2. For **Gateway time zone**, choose the local time
      zone for the part of the world where you want to deploy your
      gateway.

4. In the **Gateway options** section, for **Gateway
   type**, choose **Amazon FSx File Gateway**.
5. In the **Platform options** section, do the
   following:
   1. For **Host platform**, choose the platform on
      which you want to deploy your gateway. Then follow the
      platform-specific instructions displayed on the Storage Gateway console page
      to set up your host platform. You can choose from the following
      options:
      - **VMware ESXi** – Download,
        deploy, and configure the gateway virtual machine using
        VMware ESXi.
      - **Microsoft Hyper-V** – Download,
        deploy, and configure the gateway virtual machine using
        Microsoft Hyper-V.
      - **Linux KVM** – Download, deploy,
        and configure the gateway virtual machine using Linux
        Kernel-based Virtual Machine (KVM).
      - **Amazon EC2** – Configure and launch
        an Amazon EC2 instance to host your gateway.
      - **Hardware appliance** – Order a
        dedicated physical hardware appliance from AWS to host
        your gateway.

   2. For **Confirm set up gateway**, select the check
      box to confirm that you performed the deployment steps for the host
      platform you chose. This step is not applicable for the
      **Hardware appliance** host platform.

6. Now that your gateway is set up, you must choose how you want it to
   connect and communicate with AWS. Choose **Next** to
   proceed.

## Connect your Amazon FSx File Gateway to

AWS

###### To connect a new FSx File Gateway to AWS

1. If you have not done so already, complete the procedure described in
   [Set up an Amazon FSx File Gateway](create-gateway-file.md#set-up-gateway-fsx-file "create-gateway-file.md#set-up-gateway-fsx-file"). When finished, choose
   **Next** to open the **Connect to
   AWS** page in the AWS Storage Gateway console.
2. In the **Endpoint options** section, for
   **Service endpoint**, choose the type of endpoint your
   gateway will use to communicate with AWS. You can choose from the
   following options:
   - **Publicly accessible** – Your gateway
     communicates with AWS over the public internet. If you select this
     option, use the
     **FIPS enabled endpoint** check box to specify
     whether the connection must comply with Federal Information
     Processing Standards (FIPS).

   ###### Note

   If you require FIPS 140-2 validated cryptographic modules when
   accessing AWS through a command line interface or an API, use
   a FIPS-compliant endpoint. For more information, see [Federal Information
   Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

   The FIPS service endpoint is available only in some AWS
   Regions. For more information, see [AWS Storage Gateway endpoints and
   quotas](../../../general/latest/gr/sg.md "../../../general/latest/gr/sg.md") in the
   _AWS General Reference_.
   - **VPC hosted** – Your gateway communicates
     with AWS through a private connection with your virtual private
     cloud (VPC), allowing you to control your network settings. If you
     select this option, you must specify an existing VPC endpoint by
     choosing its VPC endpoint ID from the dropdown list. You can also
     provide its VPC endpoint Domain Name System (DNS) name or IP
     address.

3. In the **Gateway connection options** section, for
   **Connection options**, choose how to identify your
   gateway to AWS. You can choose from the following options:
   - **IP address** – Provide the IP address of
     your gateway in the corresponding field. This IP address must be
     public or accessible from within your current network, and you must
     be able to connect to it from your web browser.

   You can obtain the gateway IP address by logging into the
   gateway's local console from your hypervisor client, or by copying
   it from your Amazon EC2 instance details page.
   - **Activation key** – Provide the
     activation key for your gateway in the corresponding field. You can
     generate an activation key using the gateway's local console. If
     your gateway's IP address is unavailable, choose this option.

4. Now that you have chosen how you want your gateway to connect to AWS,
   you must activate the gateway. Choose **Next** to
   proceed.

## Review settings and activate your

Amazon FSx File Gateway

###### To activate a new FSx File Gateway

1.  If you have not done so already, complete the procedures described in the
    following topics:

        * [Set up an Amazon FSx File Gateway](create-gateway-file.md#set-up-gateway-fsx-file "create-gateway-file.md#set-up-gateway-fsx-file")
        * [Connect your Amazon FSx File Gateway to AWS](create-gateway-file.md#connect-to-amazon-fsx-file "create-gateway-file.md#connect-to-amazon-fsx-file")

    When finished, choose **Next** to open the
    **Review and activate** page in the AWS Storage Gateway
    console.

2.  Review the initial gateway details for each section on the page.
3.  If a section contains errors, choose **Edit** to return
    to the corresponding settings page and make changes.

###### Important

You cannot modify the gateway options or connection settings after
your gateway is activated. 4. Now that you have activated your gateway, you must perform the first-time
configuration to allocate local storage disks and configure logging. Choose
**Next** to proceed.

## Configure your Amazon FSx File Gateway

###### To perform the first-time configuration on a new FSx File Gateway

1.  If you have not done so already, complete the procedures described in the
    following topics:

        * [Set up an Amazon FSx File Gateway](create-gateway-file.md#set-up-gateway-fsx-file "create-gateway-file.md#set-up-gateway-fsx-file")
        * [Connect your Amazon FSx File Gateway to AWS](create-gateway-file.md#connect-to-amazon-fsx-file "create-gateway-file.md#connect-to-amazon-fsx-file")
        * [Review settings and activate your Amazon FSx File Gateway](create-gateway-file.md#review-and-activate-fsx-file "create-gateway-file.md#review-and-activate-fsx-file")

    When finished, choose **Next** to open the
    **Configure gateway** page in the AWS Storage Gateway
    console.

2.  In the **Configure storage** section, use the dropdown
    lists to allocate at least one local disk with at least 150 gibibytes (GiB)
    capacity to **Cache**. The local disks listed in this
    section correspond to the physical storage that you provisioned on your host
    platform.
3.  In the **CloudWatch log group** section, choose how to set up
    Amazon CloudWatch Logs to monitor the health of your gateway. You can choose from the
    following options:
    - **Create a new log group** – Set up a new
      log group to monitor your gateway.
    - **Use an existing log group** – Choose an
      existing log group from the corresponding dropdown list.
    - **Deactivate logging** – Do not use
      Amazon CloudWatch Logs to monitor your gateway.

###### Note

To receive Storage Gateway health logs, the following permissions must be
present in your log group resource policy. Replace the
`highlighted section` with the specific log
group resourceArn information for your deployment.

```
"Sid": "AWSLogDeliveryWrite20150319",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "delivery.logs.amazonaws.com"
        ]
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "`arn:aws:logs:eu-west-1:1234567890:log-group:/foo/bar:log-stream:*`"
```

The "Resource" element is required only if you want the permissions to
apply explicitly to an individual log group. 4. In the **CloudWatch alarms** section, choose how to set up
Amazon CloudWatch alarms to notify you when your gateway's metrics deviate from
defined limits. You can choose from the following options:

    * **Create Storage Gateway's recommended alarms**
     – Create all recommended CloudWatch alarms automatically when the
     gateway is created. For more information on recommended alarms, see
     [Understanding CloudWatch alarms](Main_monitoring-gateways-common.md#cloudwatch-alarms "Main_monitoring-gateways-common.md#cloudwatch-alarms").


    ###### Note

    This feature requires CloudWatch policy permissions which are
     *not* automatically granted as part of
     the preconfigured Storage Gateway full access policy. Make sure your
     security policy grants the following permissions before you
     attempt to create recommended CloudWatch alarms:



    	+ `cloudwatch:PutMetricAlarm` - create
    	 alarms
    	+ `cloudwatch:DisableAlarmActions` - turn
    	 alarm actions off
    	+ `cloudwatch:EnableAlarmActions` - turn
    	 alarm actions on
    	+ `cloudwatch:DeleteAlarms` - delete
    	 alarms
    * **Create a custom alarm** – Configure a
     new CloudWatch alarm to be notified about your gateway's metrics. Choose
     **Create alarm** to define metrics and specify
     alarm actions in the Amazon CloudWatch console. For instructions, see [Using Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the *Amazon CloudWatch User Guide*.
    * **No alarm** – Do not use CloudWatch alarms to
     be notified about your gateway's metrics.

5. (Optional) In the **Tags** section, choose **Add
   new tag**, then enter a case-sensitive key-value pair to help
   you search and filter for your gateway on the list pages in the AWS Storage Gateway
   console. Repeat this step to add as many tags as you need.
6. (Optional) In the **Verify VMware High Availability
   configuration** section, if your gateway is deployed on a
   VMware host that is part of a VMware High Availability (HA) cluster, choose
   **Verify VMware HA** to test whether the HA
   configuration is working properly.

###### Note

This section appears only for gateways that are running on the VMware
host platform.

This step is not required to complete the gateway configuration
process. You can test your gateway's HA configuration at any time.
Verification takes a few minutes, and reboots the Storage Gateway virtual
machine (VM). 7. Choose **Configure** to finish creating your
gateway.

To check the status of your new gateway, search for it on the
**Gateway overview** page of the AWS Storage Gateway
console.

Now that you have created your gateway, you must attach a file system for it to
use. For instructions, see [Attach an
Amazon FSx for Windows File Server file system](attach-fsxw-filesystem.md "attach-fsxw-filesystem.md").

If you do not have an existing Amazon FSx file system to attach, you must create one.
For instructions, see [Getting started with
Amazon FSx](../../../fsx/latest/WindowsGuide/getting-started.md "../../../fsx/latest/WindowsGuide/getting-started.md").
