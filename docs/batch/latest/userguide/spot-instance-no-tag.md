# Spot Instances not tagged on creation

Spot Instance tagging for AWS Batch compute resources is supported as of October 25, 2017.
Before, the recommended IAM managed policy (`AmazonEC2SpotFleetRole`) for the Amazon EC2
Spot Fleet role didn't contain permissions to tag Spot Instances at launch. The new recommended
IAM managed policy is called `AmazonEC2SpotFleetTaggingRole`. It supports tagging
Spot Instances at launch.

To fix Spot Instance tagging on creation, follow the following procedure to apply the
current recommended IAM managed policy to your Amazon EC2 Spot Fleet role. That way, any future
Spot Instances that are created with that role have permissions to apply instance tags when
they're created.

###### To apply the current IAM managed policy to your Amazon EC2 Spot Fleet role

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Roles**, and choose your Amazon EC2 Spot Fleet role.
3. Choose **Attach policy**.
4. Select the **AmazonEC2SpotFleetTaggingRole** and choose **Attach
   policy**.
5. Choose your Amazon EC2 Spot Fleet role again to remove the previous policy.
6. Select the **x** to the right of the
   **AmazonEC2SpotFleetRole** policy, and choose
   **Detach**.
