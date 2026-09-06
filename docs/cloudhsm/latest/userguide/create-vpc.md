

# Create a virtual private cloud (VPC) for AWS CloudHSM
<a name="create-vpc"></a>

You need a virtual private cloud (VPC) for your cluster in AWS CloudHSM. If you don't already have one, follow the steps in this topic to create a VPC.

**Note**  
Following these steps will result in the creation of public and private subnets.

**To create a VPC**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. On the navigation bar, use the region selector to choose one of the [AWS Regions where AWS CloudHSM is currently supported](https://docs.aws.amazon.com/general/latest/gr/rande.html#cloudhsm_region).

1. Select the **Create VPC** button.

1. For **Resources to create**, choose **VPC and more**.

1. For **Name tag auto-generation**, type an identifiable name such as **CloudHSM**. 

1. For **IPv6 CIDR block**, select **Amazon-provided IPv6 CIDR block** to use IPv6 connectivity for your HSMs and have AWS allocate an IPv6 CIDR block for your cluster. This setting supports the dual-stack Network Type. Keep the default setting if you don't need IPv6 connectivity.

1. Leave all other options set to their defaults.

1. Choose **Create VPC**.

1. After the VPC is created, select **View VPC** to view the VPC you just created.