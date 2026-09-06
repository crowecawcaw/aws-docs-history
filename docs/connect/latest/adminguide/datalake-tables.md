

# Associate tables for the Connect Customer analytics data lake
<a name="datalake-tables"></a>

 Configuration of data sharing creates a RAM invitation to the consumer account. [RAM](https://aws.amazon.com/ram/) is a service to help you securely share resources across AWS accounts. Make sure that you have the required AWS Identity and Access Management (IAM) permissions to view and accept resource share invitations. 

 For information about the suggested IAM policies for data lake administrators, see [Data lake administrator permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/permissions-reference.html#persona-dl-admin). 

1.  Open the RAM console  at [https://console.aws.amazon.com/ram/](https://console.aws.amazon.com/ram/). 

1.  Under **Shared with me** select **Resource shares**   
![Shared with me - resource shares table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/datalake-tables-1.png)

1.  Select the name of the resource share and **Accept resource share**.
**Important**  
An initial RAM request is created only for the first share.
Lake Formation optimizes subsequent shares by reusing existing accepted RAM requests when possible.
RAM requests expire after 12 hours if not accepted.
For more information about RAM requests, see [Accepting and rejecting resource share invitations](https://docs.aws.amazon.com/ram/latest/userguide/working-with-shared-invitations.html) and [Optimize AWS RAM resource shares](https://docs.aws.amazon.com/lake-formation/latest/dg/optimize-ram.html#optimize-version).   
![Shared with me - resource shares table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/datalake-tables-2.png)

1. After the resource shares have been accepted, in the consumer account navigate to the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation](https://console.aws.amazon.com/lakeformation). To configure access to the Connect Customer data lake tables, be certain the user configuring the following resources has Data lake administrator permissions in Lake Formation. For more information, see [Lake Formation personas and IAM permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/permissions-reference.html).

1. Either use an existing lake formation database or create a new database for the Connect Customer data lake tables. For more information, see [Creating a database](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-database.html). 

1.  In the AWS Lake Formation console, choose **Tables** on the left navigation menu.   
![AWS Lake Formation console.](http://docs.aws.amazon.com/connect/latest/adminguide/images/datalake-tables-3.png)

1. Select **Create table** from the upper right to [create a new Resource link](https://docs.aws.amazon.com/lake-formation/latest/dg/creating-resource-links.html).   
![AWS Lake Formation console - create table.](http://docs.aws.amazon.com/connect/latest/adminguide/images/datalake-tables-4.png)

1. In the create table dialog, select the **Resource link** radio button. **Resource link name** can be any value you wish to name the linked table. For example, for the **contact record** data type you might want to define the link name as contact\_record.

1. Specify the **Database** previously created from step 5.

1.  In the **Shared table** choose the shared table whose RAM invite was previously accepted and you wish to map to this Resource link name.  For example, select the `contact_record` shared table to map to the contact record resource link. 

1.  Information for the Shared table's database and owner ID will automatically be populated. 

1. Choose **Create**. 

1. Repeat for all data types shared to the consumer account.

1.  Open the Amazon Athena [console](https://console.aws.amazon.com/athena/home), and run a query to check if the data with the shared instance\_id is provided in the request file. For example:

    `select * from {{database_name}}.{{linked_table}} limit 10`. 

   Where:
   + {{database\_name}} is the name of the database that you created in step 5.
   + {{linked\_table}} is one of the resource link names you created in step 8.