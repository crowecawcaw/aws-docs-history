Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Creating a parameter group

If you want to set parameter values that are different from the default parameter
group, you can create your own parameter group,

###### To create a parameter group

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Configurations**, then
   choose **Workload management** to display the
   **Workload management** page.
3. Choose **Create** to display the **Create parameter
   group** window.
4. Enter a value for **Parameter group name** and
   **Description**.
5. Choose **Create** to create the parameter group.
