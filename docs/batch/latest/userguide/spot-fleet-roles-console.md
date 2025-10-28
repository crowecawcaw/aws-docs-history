# Tutorial: Create Amazon EC2 spot fleet roles in the

AWS Management Console

###### To create the `AmazonEC2SpotFleetTaggingRole` IAM service-linked role for

Amazon EC2 Spot Fleet

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. For **Access Management**, choose **Roles**,
3. For **Roles**, choose **Create role**.
4. From **Select trusted entity** for **Trusted entity
   type**, choose **AWS service**.
5. For **Use cases for other AWS services**, choose
   **EC2** and then choose **EC2 - Spot Fleet Tagging**.
6. Choose **Next**.
7. From **Permissions policies** for **Policy name**,
   verify `AmazonEC2SpotFleetTaggingRole`.
8. Choose **Next**.
9. For **Name, review, and create**:
   1. For **Role name**, enter a name to identify the role.
   2. For **Description**, enter a short explanation for the policy.
   3. (Optional) For **Step 1: Select trusted entities**, choose
      **Edit** to modify the code.
   4. (Optional) For **Step 2: Add permissions**, choose
      **Edit** to modify the code.
   5. (Optional) For **Add tags**, choose **Add tag** to
      add tags to the resource.
   6. Choose **Create role**.

###### Note

In the past, there were two managed policies for the Amazon EC2 Spot Fleet role.

- **AmazonEC2SpotFleetRole**: This is the original managed policy for the
  Spot Fleet role. However, we no longer recommend that you use it with AWS Batch. This policy
  doesn't support Spot Instance tagging in compute environments, which is required to use the
  `AWSServiceRoleForBatch` service-linked role. If you previously created a Spot
  Fleet role with this policy, apply the new recommended policy to that role. For more
  information, see [Spot Instances not tagged on creation](spot-instance-no-tag.md "spot-instance-no-tag.md").
- **AmazonEC2SpotFleetTaggingRole**: This role provides all of the
  necessary permissions to tag Amazon EC2 Spot Instances. Use this role to allow Spot Instance
  tagging on your AWS Batch compute environments.
