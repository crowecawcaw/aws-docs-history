

# Create a Spot Instance request
<a name="spot-requests"></a>

To use Spot Instances, you create a Spot Instance request that includes the desired number of instances, the instance type, and the Availability Zone. If capacity is available, Amazon EC2 fulfills your request immediately. Otherwise, Amazon EC2 waits until your request can be fulfilled or until you cancel the request.

You can use the [launch instance wizard](ec2-launch-instance-wizard.md) in the Amazon EC2 console or the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command to request a Spot Instance in the same way that you can launch an On-Demand Instance. This method is only recommended for the following reasons:
+ You're already using the [launch instance wizard](ec2-launch-instance-wizard.md) or [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command to launch On-Demand Instances, and you simply want to change to launching Spot Instances by changing a single parameter.
+ You do not need multiple instances with different instance types.

This method is generally not recommended for launching Spot Instances because you can't specify multiple instance types, and you can't launch Spot Instances and On-Demand Instances in the same request. For the preferred methods for launching Spot Instances, which include launching a *fleet* that includes Spot Instances and On-Demand Instances with multiple instance types, see [Which is the best Spot request method to use?](spot-best-practices.md#which-spot-request-method-to-use)

If you request multiple Spot Instances at one time, Amazon EC2 creates separate Spot Instance requests so that you can track the status of each request separately. For more information about tracking Spot Instance requests, see [Get the status of a Spot Instance request](spot-request-status.md).

------
#### [ Console ]<a name="create-spot-instance-request-console-procedure"></a>

**To create a Spot Instance request**

Steps 1–9 are the same steps you'd use to launch an On-Demand Instance. At Step 10, you configure the Spot Instance request.

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation bar at the top of the screen, select a Region.

1. From the Amazon EC2 console dashboard, choose **Launch instance**.

1. (Optional) Under **Name and tags**, you can name your instance, and tag the Spot Instance request, the instance, the volumes, and the elastic graphics. For information about tags, see [Tag your Amazon EC2 resources](Using_Tags.md).

   1. For **Name**, enter a descriptive name for your instance.

      The instance name is a tag, where the key is **Name**, and the value is the name that you specify. If you don't specify a name, the instance can be identified by its ID, which is automatically generated when you launch the instance.

   1. To tag the Spot Instance request, the instance, the volumes, and the elastic graphics, choose **Add additional tags**. Choose **Add tag**, and then enter a key and value, and select the resource type to tag. Choose **Add tag** again for each additional tag to add.

1. Under **Application and OS Images (Amazon Machine Image)**, choose the operating system (OS) for your instance, and then select an AMI. For more information, see [Application and OS Images (Amazon Machine Image)](ec2-instance-launch-parameters.md#liw-ami).

1. Under **Instance type**, select the instance type that meets your requirements for the hardware configuration and size of your instance. For more information, see [Instance type](ec2-instance-launch-parameters.md#liw-instance-type).

1. Under **Key pair (login)**, choose an existing key pair, or choose **Create new key pair** to create a new one. For more information, see [Amazon EC2 key pairs and Amazon EC2 instances](ec2-key-pairs.md).
**Important**  
If you choose the **Proceed without key pair (Not recommended)** option, you won't be able to connect to the instance unless you choose an AMI that is configured to allow users another way to log in.

1. Under **Network settings**, use the default settings, or choose **Edit** to configure the network settings as necessary.

   Security groups form part of the network settings, and define firewall rules for your instance. These rules specify which incoming network traffic is delivered to your instance.

   For more information, see [Network settings](ec2-instance-launch-parameters.md#liw-network-settings).

1. The AMI you selected includes one or more volumes of storage, including the root device volume. Under **Configure storage**, you can specify additional volumes to attach to the instance by choosing **Add new volume**. For more information, see [Configure storage](ec2-instance-launch-parameters.md#liw-storage).

1. Under **Advanced details**, configure the Spot Instance request as follows:

   1. Under **Purchasing option**, select the **Request Spot Instances** checkbox.

   1. You can either keep the default configuration for the Spot Instance request, or choose **Customize** (at the right) to specify custom settings for your Spot Instance request.

      When you choose **Customize**, the following fields appear.

      1. **Maximum price**: You can request Spot Instances at the Spot price, capped at the On-Demand price, or you can specify the maximum amount you're willing to pay.
**Warning**  
If you specify a maximum price, your instances will be interrupted more frequently than if you choose **No maximum price**.  
If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in a failed launch.
         + **No maximum price**: Your Spot Instance will launch at the current Spot price. The price will never exceed the On-Demand price. (Recommended)
         + **Set your maximum price (per instance/hour)**: You can specify the maximum amount you're willing pay.
           + If you specify a maximum price that is less than the current Spot price, your Spot Instance will not launch.
           + If you specify a maximum price that is more than the current Spot price, your Spot Instance will launch and be charged at the current Spot price. After your Spot Instance is running, if the Spot price rises above your maximum price, Amazon EC2 interrupts your Spot Instance.
           + Regardless of the maximum price you specify, you will always be charged the current Spot price.

           To review Spot price trends, see [View Spot Instance pricing history](using-spot-instances-history.md).

      1. **Request type**: The Spot Instance request type that you choose determines what happens if your Spot Instance is interrupted.
         + **One-time**: Amazon EC2 places a one-time request for your Spot Instance. If your Spot Instance is interrupted, the request is not resubmitted.
         + **Persistent request**: Amazon EC2 places a persistent request for your Spot Instance. If your Spot Instance is interrupted, the request is resubmitted to replenish the interrupted Spot Instance.

         If you do not specify a value, the default is a one-time request.

      1. **Valid to**: The expiration date of a *persistent* Spot Instance request.

         This field is not supported for one-time requests. A *one-time* request remains active until all the instances in the request launch or you cancel the request. 
         + **No request expiry date**: The request remains active until you cancel it.
         + **Set your request expiry date**: The persistent request remains active until the date that you specify, or until you cancel it.

      1. **Interruption behavior**: The behavior that you choose determines what happens when a Spot Instance is interrupted.
         + For persistent requests, valid values are **Stop** and **Hibernate**. When an instance is stopped, charges for EBS volume storage apply.
**Note**  
Spot Instances now use the same hibernation functionality as On-Demand Instances. To enable hibernation, you can either choose **Hibernate** here, or you can choose **Enable** from the **Stop - Hibernate behavior** field, which appears lower down in the launch instance wizard. For the hibernation prerequisites, see [Prerequisites for EC2 instance hibernation](hibernating-prerequisites.md).
         + For one-time requests, only **Terminate** is valid.

         If you do not specify a value, the default is **Terminate**, which is not valid for a persistent Spot Instance request. If you keep the default and try to launch a persistent Spot Instance request, you'll get an error.

         For more information, see [Behavior of Spot Instance interruptions](interruption-behavior.md).

1. On the **Summary** panel, for **Number of instances**, enter the number of instances to launch.
**Note**  
Amazon EC2 creates a separate request for each Spot Instance.

1. On the **Summary** panel, review the details of your instance, and make any necessary changes. After you submit your Spot Instance request, you can't change the parameters of the request. You can navigate directly to a section in the launch instance wizard by choosing its link in the **Summary** panel. For more information, see [Summary](ec2-instance-launch-parameters.md#liw-summary).

1. When you're ready to launch your instance, choose **Launch instance**. 

   If the instance fails to launch or the state immediately goes to `terminated` instead of `running`, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md).

------
#### [ AWS CLI ]

**To create a Spot Instance request using run-instances**  
Use the [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command and specify the Spot Instance options in the `--instance-market-options` parameter as follows.

```
--instance-market-options file://{{spot-options.json}}
```

The following is the data structure to specify in the JSON file. You can also specify `ValidUntil` and `InstanceInterruptionBehavior`. If you do not specify a field in the data structure, the default value is used.

The following example creates a `persistent` request.

```
{
  "MarketType": "spot",
  "SpotOptions": {
    "SpotInstanceType": "{{persistent}}"
  }
}
```

**To create a Spot Instance request using request-spot-instances**

**Note**  
We strongly discourage using the [request-spot-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-instances.html) command to request a Spot Instance because it is a legacy API with no planned investment. For more information, see [Which is the best Spot request method to use?](spot-best-practices.md#which-spot-request-method-to-use)

Use the [request-spot-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-instances.html) command to create a one-time request.

```
aws ec2 request-spot-instances \
    --instance-count {{5}} \
    --type "one-time" \
    --launch-specification file://{{specification.json}}
```

Use the [request-spot-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-instances.html) command to create a persistent request.

```
aws ec2 request-spot-instances \
    --instance-count {{5}} \
    --type "persistent" \
    --launch-specification file://{{specification.json}}
```

For example launch specification files to use with these commands, see [Spot Instance request example launch specifications](spot-request-examples.md). If you download a launch specification file from the Spot Requests console, you must use the [request-spot-fleet](https://docs.aws.amazon.com/cli/latest/reference/ec2/request-spot-fleet.html) command instead (the Spot Requests console specifies a Spot Instance request using a Spot Fleet).

------
#### [ PowerShell ]

**To create a Spot Instance request**  
Use the [New-EC2Instance](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Instance.html) cmdlet and specify the Spot Instance options using the `-InstanceMarketOption` parameter.

```
-InstanceMarketOptions $marketOptions
```

Create the data structure for the Spot Instance options as follows.

```
$spotOptions = New-Object Amazon.EC2.Model.SpotMarketOptions
$spotOptions.SpotInstanceType="persistent"
$marketOptions = New-Object Amazon.EC2.Model.InstanceMarketOptionsRequest
$marketOptions.MarketType = "spot"
$marketOptions.SpotOptions = $spotOptions
```

------