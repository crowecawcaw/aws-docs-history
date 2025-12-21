# Editing default values for query results

settings

###### Note

The **Results destination in
Amazon S3** can't be within the same S3 bucket as any data source.

As a member who can receive results, you can edit the default values for query results
settings in the AWS Clean Rooms console.

###### To edit the default values for query results settings

1.  Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home") with your AWS account (if you haven't yet done so).
2.  In the left navigation pane, choose **Collaborations**.
3.  Choose the collaboration that has **Your member abilities** status of
    **Receive results**.
4.  On the **Analysis** tab, under **Results settings
    defaults**, choose **Edit**.
5.  On the **Edit results settings defaults** page, modify any of the
    following, as needed:
    1. Under **Query results**, modify the **Results destination
       in Amazon S3**, the **Result format**, or the **Result
       files**.
    2. (Optional) For **Service access**, if you want to deliver queries
       that take up to 24 hours to your S3 destination, select the **Add a service
       role to support queries that take up to 24 hours to complete**
       checkbox.

    Large queries that take up to 24 hours to complete will be delivered to your S3
    destination.

    If you don't select the checkbox, only queries that complete within 12 hours will
    be delivered to your S3 location.

        1. Specify the **Service access** permissions by selecting
         either **Create and use a new service role** or **Use an
         existing service role**.



        Create and use a new service role


        	* AWS Clean Rooms creates a service role with the required policy for this
        	 table.
        	* The default **Service role name** is
        	 `cleanrooms-query-receiver-<timestamp>`
        	* You must have permissions to create roles and attach
        	 policies.

        Use an existing service role


        	1. Choose an **Existing service role name** from the
        	 dropdown list.


        	The list of roles are displayed if you have permissions to list
        	 roles.


        	If you don't have permissions to list roles, you can enter the
        	 Amazon Resource Name (ARN) of the role that you want to use.
        	2. View the service role by choosing the **View in
        	 IAM** external link.


        	If there are no existing service roles, the option to **Use
        	 an existing service role** is unavailable.


        	By default, AWS Clean Rooms doesn't attempt to update the existing role policy
        	 to add necessary permissions.


        ###### Note



        	* AWS Clean Rooms requires permissions to query according to the analysis rules.
        	 For more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
        	* If the role doesn’t have sufficient permissions for AWS Clean Rooms, you
        	 receive an error message stating that the role doesn't have sufficient
        	 permissions for AWS Clean Rooms. The role policy must be added before
        	 proceeding.
        	* If you can’t modify the role policy, you receive an error message
        	 stating that AWS Clean Rooms couldn't find the policy for the service role.

6.  Choose **Save changes**.
7.  The updated **Query results settings** appear on the collaboration
    detail page.
