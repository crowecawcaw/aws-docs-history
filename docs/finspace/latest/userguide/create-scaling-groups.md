

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Creating a Managed kdb scaling group
<a name="create-scaling-groups"></a>

**To create a scaling group**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. In the left pane, under **Managed kdb Insights**, choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose **Kdb scaling groups** tab.

1. Choose **Create kdb scaling group**.

1. On the **Create kdb scaling group** page, enter a unique name for the scaling group details.

1. Choose a **Host Type** based on the available throughput and size.

1. Choose the availability zone that you want to associate with the scaling group. Currently, you can choose only single availability zone.

1. (Optional) Add a new tag to assign it to your scaling group. For more information, see [AWS tags](https://docs.aws.amazon.com/finspace/latest/userguide/create-an-amazon-finspace-environment.html#aws-tags). 
**Note**  
You can only add up to 50 tags to your user.

1. Choose **Create kdb scaling group**. The scaling group creation process starts and the kdb environment details page opens where you can see the status of creation under the **Kdb scaling groups** tab.