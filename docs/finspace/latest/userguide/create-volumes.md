

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html). 

# Creating a Managed kdb volume
<a name="create-volumes"></a>

**To create a Managed kdb volume**

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing).

1. In the left pane, under **Managed kdb Insights**, choose **Kdb environments**.

1. From the kdb environments table, choose the name of the environment.

1. On the environment details page, choose **Volumes** tab.

1. Choose **Create volume**.

1. On the **Create volume** page, enter the volume details and choose the **Volume type**. Currently, FinSpace only supports **NAS\_1** (network attached storage) volume type.

1. Choose the throughput from one of the following types.
   + **SSD\_1000**
   + **SSD\_250**
   + **HDD\_12**

1. Enter the size for the network attached storage configuration. For storage type **SSD\_1000** and **SSD\_250** you can select the minimum size as 1200 GB or increments of 2400 GB. For storage type **HDD\_12** you can select the minimum size as 6000 GB or increments of 6000 GB.

1. Choose the availability zone that you want to associate with the volume.

1. (Optional) Add a new tag to assign it to your Managed kdb volume. For more information, see [AWS tags](https://docs.aws.amazon.com/finspace/latest/userguide/create-an-amazon-finspace-environment.html#aws-tags). 
**Note**  
You can only add up to 50 tags to your user.

1. Choose **Create volume**. The volume creation process starts and kdb environment details page opens where you can see the status of volume creation under the **Volumes** tab.