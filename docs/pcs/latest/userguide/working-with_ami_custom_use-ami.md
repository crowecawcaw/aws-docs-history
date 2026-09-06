

# Step 6 – Use the custom AMI with an AWS PCS compute node group
<a name="working-with_ami_custom_use-ami"></a>

You can use your custom AMI with a new or existing AWS PCS compute node group. 

**Important**  
AWS PCS currently requires a kernel with IPv4 support for local node communication, even when you use AWS PCS in an IPv6-only network.

------
#### [ New compute node group ]

**To use the custom AMI**

1.  Open the [AWS PCS console](https://console.aws.amazon.com/pcs). 

1.  In the navigation pane, choose **Clusters**. 

1.  Choose the cluster where you will use the custom AMI, then select **Compute node groups**. 

1.  Create a new compute node group. For more information, see [Creating a compute node group in AWS PCS](working-with_cng_create.md). Under **AMI ID**, search for the name or ID of the custom AMI you want to use. Finish configuring the compute node group, then choose **Create compute node group**. 

1. (Optional) Confirm the AMI supports instance launches. Launch an instance in the compute node group. You can do this by configuring the compute node group to have a single static instance, or you can submit a job to a queue that uses the compute node group.

   1.  Check the Amazon EC2 console until an instance appears tagged with the new compute node group ID. For more information on this, see [Finding compute node group instances in AWS PCS](working-with_compute-instances.md).. 

   1.  When you see an instance launch and complete its bootstrap process, confirm it is using the expected AMI. To do this, select the instance, then inspect **AMI ID** under **Details**. It should match the AMI you configured in the compute node group settings. 

   1.  (Optional) Update the compute node group scaling configuration to your preferred values. 

------
#### [ Existing compute node group ]

**To use the custom AMI**

1.  Open the [AWS PCS console](https://console.aws.amazon.com/pcs). 

1.  In the navigation pane, choose **Clusters**. 

1.  Choose the cluster where you will use the custom AMI, then select **Compute node groups**. 

1. Select the node group you wish to configure and choose **Edit**. Under **AMI ID**, search for the name or ID of the custom AMI you want to use. Finish configuring the compute node group, then choose **Update**. New instances launched in the compute node group will use the updated AMI ID. Existing instances will continue to use the old AMI until AWS PCS replaces them. For more information, see [Updating an AWS PCS compute node group](working-with_cng_update.md).

1. (Optional) Confirm the AMI supports instance launches. Launch an instance in the compute node group. You can do this by configuring the compute node group to have a single static instance, or you can submit a job to a queue that uses the compute node group.

   1.  Check the Amazon EC2 console until an instance appears tagged with the new compute node group ID. For more information on this, see [Finding compute node group instances in AWS PCS](working-with_compute-instances.md).. 

   1.  When you see an instance launch and complete its bootstrap process, confirm it is using the expected AMI. To do this, select the instance, then inspect **AMI ID** under **Details**. It should match the AMI you configured in the compute node group settings. 

   1.  (Optional) Update the compute node group scaling configuration to your preferred values. 

------