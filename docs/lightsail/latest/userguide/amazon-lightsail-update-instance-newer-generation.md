

# Update Lightsail instances to run on newer-generation hardware
<a name="amazon-lightsail-update-instance-newer-generation"></a>

You can update an eligible Amazon Lightsail instance to run on newer-generation hardware when you start it. The instance keeps its name, private IP address, attached disks, and data, and moves to the equivalent bundle at the same price. For more information about instance states, see [Start, stop, or reboot your Lightsail instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md).

You can also move to newer-generation hardware by creating a new instance from a snapshot. For more information, see [Create an instance from a snapshot](lightsail-how-to-create-instance-from-snapshot.md).

**Note**  
The default public IP address for your instance changes when you update your instance. When you attach a static IP address to your instance, it stays the same. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

## Check whether your instance uses previous-generation hardware
<a name="check-instance-generation"></a>

Your instance uses previous-generation hardware if it's on a general purpose bundle whose ID ends in `_1_{{x}}` or `_2_{{x}}`, such as `micro_2_0`. Bundles that end in `_2_3` in Europe (Stockholm) (eu-north-1) already use newer-generation hardware.

To check your instance in the Lightsail console, open the instance's management page. If the instance uses previous-generation hardware, **Update your instance** appears below the instance name. To check using the AWS CLI, type the following command. For more information, see [Configure the AWS CLI to work with Lightsail](lightsail-how-to-set-up-and-configure-aws-cli.md).

```
aws lightsail get-instance --instance-name {{Wordpress-1}} --query instance.bundleId
```

If your instance's blueprint doesn't support newer-generation hardware, you can't update the instance.

**Note**  
Some `_1_{{x}}` bundles have a smaller disk than the equivalent newer-generation bundle. For example, `micro_1_0` has 30 GB and `micro_3_0` has 40 GB. The updated instance keeps its original disk size. To get the larger disk, create a new instance from a snapshot instead.

## Update an instance when you start it
<a name="update-instance-newer-generation"></a>

The instance must be in the `Stopped` state.

Before you update, create a snapshot of the instance so that you can recover it if needed. For more information, see [Create a snapshot of your instance](lightsail-how-to-create-a-snapshot-of-your-instance.md).

**Important**  
After the updated instance is running, verify you have access to the instance and everything is working properly. Keep the snapshot that you created before the update in case you need to go back to it. When you no longer need the snapshot, delete it. Snapshots incur a monthly storage fee until you delete them. For more information, see [Delete snapshots](amazon-lightsail-deleting-snapshots.md).

You can update an instance when you start it using the Amazon Lightsail console or the AWS Command Line Interface (AWS CLI).

### Update an instance using the Lightsail console
<a name="update-instance-newer-generation-console"></a>

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. Choose the **Instances** tab, and then choose the name of the instance to open its management page.

1. Make sure your instance is fully stopped. The instance must be in the `Stopped` state. Stopping an instance can take a few minutes to complete. For more information, see [Stop a running instance](lightsail-how-to-start-stop-or-restart-your-instance-virtual-private-server.md#lightsail-instance-stop).
**Note**  
Rarely, an instance can get stuck in the `Stopping` state. If this happens, see [Force stop stuck Lightsail instances](amazon-lightsail-force-stop-instance.md).

1. Choose **Start**.

1. In the **Update recommended to start instance** dialog, keep the **Update to newer-generation hardware** check box selected, and then choose **Start**.

   The dialog lists your **Current plan** and the **New plan** so that you can compare them. Each plan shows its memory, vCPUs, storage, and monthly price. The new plan has the same memory and price as your current plan. The number of vCPUs is the same or higher. For example, a plan with 1 GB of memory, 1 vCPU, and 40 GB of storage is updated to a plan with 1 GB of memory, 2 vCPUs, and 40 GB of storage at the same price. Your instance runs on newer-generation hardware after it starts.  
![The Update recommended to start instance dialog, comparing the current plan and the new plan.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-update-instance-newer-generation-start-modal.png)

### Update an instance using the AWS CLI
<a name="update-instance-newer-generation-cli"></a>

1. Before you begin, you need to install the AWS CLI. To learn more, see [Installing the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). Be sure to [configure the AWS CLI](lightsail-how-to-set-up-and-configure-aws-cli.md) after you install it.

1. Type the following command to update the instance.

   ```
   aws lightsail start-instance --instance-name {{Wordpress-1}} --attribute-updates bundleId=auto
   ```

   The `auto` value updates the instance to the equivalent newer-generation bundle. If the instance isn't eligible, the command returns an error that explains why.

## Revert an instance to its original bundle
<a name="revert-instance-original-bundle"></a>

You can use the AWS CLI to revert an updated instance to its original previous-generation bundle. You can revert only to the instance's original bundle ID. The instance must be in the `Stopped` state.

1. Stop the instance, and wait for it to reach the `Stopped` state.

1. Type the following command to revert the instance to its original bundle.

   ```
   aws lightsail start-instance --instance-name {{Wordpress-1}} --attribute-updates bundleId={{micro_2_0}}
   ```

   Replace {{micro\_2\_0}} with the original bundle ID of your instance.