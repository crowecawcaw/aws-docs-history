

# Launch a Mac instance using the AWS Management Console or the AWS CLI
<a name="mac-instance-launch"></a>

EC2 Mac instances require a [Dedicated Host](dedicated-hosts-overview.md). You first need to allocate a host to your account, and then launch the instance onto the host.

You can launch a Mac instance using the AWS Management Console or the AWS CLI. 

## Launch a Mac instance using the console
<a name="mac-instance-launch-console"></a>

**To launch a Mac instance onto a Dedicated Host**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Allocate the Dedicated Host, as follows:

   1. In the navigation pane, choose **Dedicated Hosts**.

   1. Choose **Allocate Dedicated Host** and then do the following:

      1. For **Instance family**, choose a **Mac** Instance family. If the instance family doesn’t appear in the list, it’s not supported in the currently selected Region.

      1. For **Instance type**, choose the instance type based on the selected instance family chosen.

      1. For **Availability Zone**, choose the Availability Zone for the Dedicated Host.

      1. For **Quantity**, keep **1**.

      1. Choose **Allocate**.

1. Launch the instance on the host, as follows:

   1. Select the Dedicated Host that you created and then do the following:

      1. Choose **Actions**, **Launch instance(s) onto host**.

      1. Under **Application and OS Images (Amazon Machine Image)**, select a macOS AMI.

      1. Under **Instance type**, select the Mac instance type.

      1. Under **Advanced details**, verify that **Tenancy**, **Tenancy host by**, and **Tenancy host ID** are preconfigured based on the Dedicated Host you created. Update **Tenancy affinity** as needed.

      1. Complete the wizard, specifying EBS volumes, security groups, and key pairs as needed.

      1. In the **Summary** panel, choose **Launch instance**.

   1. A confirmation page lets you know that your instance is launching. Choose **View all instances** to close the confirmation page and return to the console. The initial state of an instance is `pending`. The instance is ready when its state changes to `running` and it passes status checks.

## Launch a Mac instance using the AWS CLI
<a name="mac-instance-launch-cli"></a>

**Allocate the Dedicated Host**

Use the following [allocate-hosts](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-hosts.html) command to allocate a Dedicated Host for your Mac instance, replacing the `instance-type` with a valid mac instance type, and the `region` and `availability-zone` with the appropriate ones for your environment. 

```
aws ec2 allocate-hosts --region {{us-east-1}} --instance-type {{mac1.metal}} --availability-zone {{us-east-1b}} --auto-placement "on" --quantity 1
```

**Launch the instance on the host**

Use the following [run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) command to launch a Mac instance, again replacing the `instance-type` with a valid mac instance type, and the `region` and `availability-zone` with the ones used previously.

```
aws ec2 run-instances --region {{us-east-1}} --instance-type {{mac1.metal}} --placement Tenancy=host --image-id {{ami_id}} --key-name {{my-key-pair}}
```

The initial state of an instance is `pending`. The instance is ready when its state changes to `running` and it passes status checks. Use the following [describe-instance-status](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instance-status.html) command to display status information for your instance.

```
aws ec2 describe-instance-status --instance-ids {{i-017f8354e2dc69c4f}}
```

The following is example output for an instance that is running and has passed status checks.

```
{
    "InstanceStatuses": [
        {
            "AvailabilityZone": "us-east-1b",
            "InstanceId": "i-017f8354e2dc69c4f",
            "InstanceState": {
                "Code": 16,
                "Name": "running"
            },
            "InstanceStatus": {
                "Details": [
                    {
                        "Name": "reachability",
                        "Status": "passed"
                    }
                ],
                "Status": "ok"
            },
            "SystemStatus": {
                "Details": [
                    {
                        "Name": "reachability",
                        "Status": "passed"
                    }
                ],
                "Status": "ok"
            }
        }
    ]
}
```