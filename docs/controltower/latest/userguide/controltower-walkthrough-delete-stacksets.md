# Delete StackSets and Stacks

AWS Control Tower uses StackSets and stacks to deploy AWS Config Rules related to controls in your landing zone. The
following procedures walk through how to delete these specific resources.

###### To delete CloudFormation StackSets

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the left navigation menu, choose **StackSets**.
3. For each StackSet with the prefix **AWSControlTower**, do the following.
   If you have many accounts in a StackSet, this can take some time.
   1. Choose the specific StackSet from the table in the dashboard. This opens the properties
      page for that StackSet.
   2. At the bottom of the page, in the **Stacks** table, make a record of
      the AWS account IDs for all the accounts in the table. Copy the list of all
      accounts.
   3. From **Actions**, choose **Delete stacks from
      StackSet**.
   4. On **Set deployment options**, from **Deployment
      locations**, choose **Deploy stacks in accounts**.
   5. In the text field, enter the AWS account IDs you made a record of in step 3.b,
      separated by commas. For example: `123456789012`,
      `098765431098`, and so on.
   6. From **Specify regions**, choose **Add all**, leave
      the rest of the parameters on the page set to their defaults, and choose
      **Next**.
   7. On the **Review** page, review your choices, and then choose
      **Delete stacks**.
   8. On the **StackSet properties** page, you can begin this procedure again
      for your other StackSets.

4. The process is complete when the records in the **Stacks** table of the
   different **StackSets properties** pages are empty.
5. When the records in the **Stacks** table are empty, choose
   **Delete StackSet**.

###### To delete CloudFormation stacks

1. Open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the **Stacks** dashboard, search for all of the stacks with the
   prefix **AWSControlTower**.
3. For each stack in the table, do the following:
   1. Choose the check box next to the name of the stack.
   2. From the **Actions** menu, choose **Delete
      Stack**.
   3. In the dialog box that opens, review the information to make sure it's accurate, and
      choose **Yes, Delete**.
