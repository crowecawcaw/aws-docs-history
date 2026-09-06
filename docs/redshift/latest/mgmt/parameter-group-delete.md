

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Deleting a parameter group
<a name="parameter-group-delete"></a>

You can delete a parameter group if you no longer need it and it is not associated with any clusters. You can only delete custom parameter groups.

**To delete a parameter group**

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Configurations**, then choose **Workload management** to display the **Workload management** page. 

1. For **Parameter groups,** choose the parameter group that you want to modify.
**Note**  
You can't delete the default parameter group.

1. Choose **Delete** and confirm that you want to delete the parameter group. 