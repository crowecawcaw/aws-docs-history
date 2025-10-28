After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Creating a Managed kdb volume

###### To create a Managed kdb volume

1. Sign in to the AWS Management Console and open the Amazon FinSpace console at [https://console.aws.amazon.com/finspace](https://console.aws.amazon.com/finspace/landing "https://console.aws.amazon.com/finspace/landing").
2. In the left pane, under **Managed kdb Insights**, choose **Kdb
   environments**.
3. From the kdb environments table, choose the name of the environment.
4. On the environment details page, choose **Volumes** tab.
5. Choose **Create volume**.
6. On the **Create volume** page, enter the volume details and choose
   the **Volume type**. Currently, FinSpace only supports
   **NAS_1** (network attached storage) volume type.
7. Choose the throughput from one of the following types.
   - **SSD_1000**
   - **SSD_250**
   - **HDD_12**

8. Enter the size for the network attached storage configuration. For storage type
   **SSD_1000** and **SSD_250** you can select the
   minimum size as 1200 GB or increments of 2400 GB. For storage type
   **HDD_12** you can select the minimum size as 6000 GB or increments
   of 6000 GB.
9. Choose the availability zone that you want to associate with the volume.
10. (Optional) Add a new tag to assign it to your Managed kdb volume. For more information, see
    [AWS tags](create-an-amazon-finspace-environment.md#aws-tags "create-an-amazon-finspace-environment.md#aws-tags").

###### Note

You can only add up to 50 tags to your user. 11. Choose **Create volume**. The volume creation process starts and kdb
environment details page opens where you can see the status of volume creation under the
**Volumes** tab.
