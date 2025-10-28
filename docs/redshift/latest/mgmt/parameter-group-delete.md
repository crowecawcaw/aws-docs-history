Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Deleting a parameter group

You can delete a parameter group if you no longer need it and it is not associated
with any clusters. You can only delete custom parameter groups.

###### To delete a parameter group

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Workload management** to display the
   **Workload management** page.
3. For **Parameter groups,** choose the parameter group that you
   want to modify.

###### Note

You can't delete the default parameter group. 4. Choose **Delete** and confirm that you want to delete the
parameter group.
