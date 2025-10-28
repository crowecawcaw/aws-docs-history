# Remove AWS Control Tower Roles and

Policies

These procedures walk you through how to clean up the roles and policies that AWS Control Tower
created when your landing zone was set up, or later.

###### To delete the IAM Identity Center AWSServiceCatalogEndUserAccess role

1. Open the AWS IAM Identity Center console at [https://console.aws.amazon.com/singlesignon/](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Change your AWS Region to your home Region, which is the Region where you initially set
   up AWS Control Tower.
3. From the left navigation menu, choose **AWS accounts**.
4. Choose your management account link.
5. Choose the dropdown for **Permission sets**, select
   **AWSServiceCatalogEndUserAccess**, and then choose
   **Remove**.
6. Choose **AWS accounts** from the left panel.
7. Open the **Permission sets** tab.
8. Select **AWSServiceCatalogEndUserAccess** and delete it.

###### To delete IAM roles

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the left navigation menu, choose **Roles**.
3. From the table, search for roles with the name
   **AWSControlTower**.
4. For each role in the table, do the following:
   1. Choose the check box for the role.
   2. Choose **Delete role**.
   3. In the dialog box that opens, review the information to make sure it's accurate, and
      then choose **Yes, delete**.

###### To delete IAM policies

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. From the left navigation menu, choose **Policies**.
3. From the table, search for policies with the name
   **AWSControlTower**.
4. For each policy in the table, do the following:
   1. Choose the check box for the policy.
   2. Choose **Policy actions**, and **Delete** from the
      dropdown menu.
   3. In the dialog box that opens, review the information to make sure it's accurate, and
      then choose **Delete**.
