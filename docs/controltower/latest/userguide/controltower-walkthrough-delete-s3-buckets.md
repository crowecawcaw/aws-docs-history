# Delete Amazon S3 Buckets in the Log

Archive Account

The following procedures guide you through how to sign in to the log archive account as an
IAM Identity Center user in the **AWSControlTowerExecution** group and then delete the Amazon S3
buckets in your log archive account.

###### To sign in to your log archive account with the right permissions

1. Open the Organizations console at [https://console.aws.amazon.com/organizations/](https://console.aws.amazon.com/organizations/ "https://console.aws.amazon.com/organizations/").
2. From the **Accounts** tab, find the **Log archive**
   account.
3. From the right pane that opens, make a record of the log archive account number.
4. From the navigation bar, choose your account name to open your account menu.
5. Choose **Switch Role**.
6. On the page that opens, provide the account number for the log archive account in
   **Account**.
7. For **Role**, enter **AWSControlTowerExecution**.
8. The **Display Name** populates with text.
9. Choose your favorite **Color**.
10. Choose **Switch Role**.

###### To delete Amazon S3 buckets

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Search for bucket names that contain **aws-controltower**.
3. For each bucket in the table, do the following:
   1. Choose the check box for the bucket in the table.
   2. Choose **Delete**.
   3. In the dialog box that opens, review the information to make sure it's accurate, enter
      the name of the bucket to confirm, and then choose **Confirm**.
