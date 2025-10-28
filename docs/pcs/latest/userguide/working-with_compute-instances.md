# Finding compute node group instances in

AWS PCS

Each AWS PCS compute node group can launch EC2 instances with shared configurations.
You can use EC2 tags to find instances in a compute node group in the AWS Management Console or with the AWS CLI.

AWS Management Console

###### To find your compute node group instances

1. Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
2. Select the cluster.
3. Choose **Compute node groups**.
4. Find the ID for the login node group you created.
5. Navigate to the [EC2 console](https://console.aws.amazon.com/ec2/home "https://console.aws.amazon.com/ec2/home") and choose **Instances**.
6. Search for the instances with the following tag. Replace `node-group-id` with the **ID** (not the name) of your compute node group.

```
aws:pcs:compute-node-group-id=`node-group-id`
```

7. (Optional) You can change the value of **Instance state** in the search field to find instances that are being configured or that were recently terminated.
8. Find the instance ID and IP address for each instance in the list of tagged instances.

AWS CLI
To find your node group instances, use the commands that follow. Before running the
commands, make the following replacements:

- Replace `region-code` with the AWS Region of your cluster. Example: `us-east-1`
- Replace `node-group-id` with the **ID** (not the name) of your compute node group. To find the ID of a compute node group, see [Get compute node group details in
  AWS PCS](working-with_cng_get-details.md "working-with_cng_get-details.md").
- Replace `running` with other instance states such as `pending` or `terminated` to find EC2 instances in other states.

```
aws ec2 describe-instances \
     --region `region-code` --filters \
     "Name=tag:aws:pcs:compute-node-group-id,Values=`node-group-id`" \
     "Name=instance-state-name,Values=`running`" \
     --query 'Reservations[*].Instances[*].{InstanceID:InstanceId,State:State.Name,PublicIP:PublicIpAddress,PrivateIP:PrivateIpAddress}'
```

The command returns output similar to the following. The value of `PublicIP` is `null` if the instance is in a private subnet.

```
[
    [
        {
            "InstanceID": "i-0123456789abcdefa",
            "State": "running",
            "PublicIP": "18.189.32.188",
            "PrivateIP": "10.0.0.1"
        }
    ]
]

```

###### Note

If you expect `describe-instances` to return a large number of instances, you must use options for multiple pages.
For more information, see [DescribeInstances](../../../AWSEC2/latest/APIReference/API_DescribeInstances.md "../../../AWSEC2/latest/APIReference/API_DescribeInstances.md") in the _Amazon Elastic Compute Cloud API Reference_.
