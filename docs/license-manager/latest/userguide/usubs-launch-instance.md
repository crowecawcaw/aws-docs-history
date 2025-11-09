# Launch an instance from a license included AMI

After you have subscribed to a product, you must launch instances for your users to
connect to from the AWS Marketplace AMI that includes the product. After you launch an instance,
AWS Systems Manager attempts to join the instance to the Active Directory domain and perform additional
configuration and hardening on the resource. The configurations to make the instance
ready to use can take around 20 minutes to complete. You can confirm the resource is
ready to use from the **User association** page of the License Manager console by
checking for a **Health status** of **Active** for the
instance.

###### Important

The instances you launch must meet the required prerequisites to be in compliance.
Resources that are unable to complete the initial configuration are terminated.
For more information, see the [Prerequisites to create
user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites "user-based-subscriptions.md#usubs-prerequisites") and [Troubleshoot user-based
subscriptions in License Manager](user-based-subscriptions-troubleshoot.md "user-based-subscriptions-troubleshoot.md").

###### Launch an instance with user-based subscriptions

1. Access the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Under **Images**, choose **AMI
   Catalog**.
3. Choose **AWS Marketplace AMIs**.
4. Enter the product name into the search box and press enter. For example, you
   might search for `Visual Studio`.
5. Under **Publisher**, select **Amazon Web Services**.
6. Choose **Select** for the product that you want to launch an
   instance to provide user-based subscriptions.
7. Choose **Continue** to proceed.
8. Choose **Launch Instance with AMI**.
9. Complete the wizard while ensuring that you:
   1. Choose a Nitro based instance type that is not Graviton based.
   2. Choose a VPC and subnet from which your instance can connect to your
      AWS Managed Microsoft AD directory.
   3. Choose a security group that permits connectivity from your instance to
      your Active Directory.
   4. Expand **Advanced details** and choose an IAM role
      that allows Systems Manager functionality for your instance.

10. Choose **Launch instance**.
    When you have running instances from the AWS Marketplace AMI, you must subscribe users to the product
    and associate them with instances, which provide the product so that they can use
    it.

## Launch an instance from a specific operating system version AMI

When you launch an instance from an AMI that supports `Office LTSC Professional 
 Plus` or Microsoft Visual Studio, the launch defaults to the latest Windows operating system version of
the AMI (for example Windows Server 2025). To launch with a specific operating system version AMI,
follow these steps.

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace "https://console.aws.amazon.com/marketplace").
2. Choose **Manage subscriptions** from the navigation pane.
3. To streamline subscription results, you can search for all or part of the
   subscription name. For example, `Office LTSC Professional Plus`
   or `Visual Studio Enterprise`.
4. Select **Launch new instance** from the subscription panel.
   This opens a launch configuration page.
5. To launch an instance from an AMI that's based on an earlier version of the
   Windows OS platform, select the **full AWS Marketplace website** link,
   located under the **Software version**. This takes you to a
   configuration page where you can select from a list of versions.
6. The list shows the latest AMI versions for the supported Windows OS platforms.
   Select the Windows OS version that you want to launch from.
