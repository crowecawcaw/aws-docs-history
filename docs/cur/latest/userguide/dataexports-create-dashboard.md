

# Creating a cost and usage dashboard
<a name="dataexports-create-dashboard"></a>

You can visualize your billing and cost management data by deploying a pre-built Cost and Usage Dashboard powered by Amazon QuickSight.

**To create a cost and usage dashboard**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Data Exports**.

1. On the **Data Exports** page, choose either **Create** or the **Cost and usage dashboard** tile.

1. On the **Create** page, under **Export type**, choose **Cost and usage dashboard powered by QuickSight**.

1. For **Export name**, enter a name for your dashboard.

   Export names can have up to 128 characters and must be unique. Valid characters are a-z, A-Z, 0-9, - (hyphen), and \_ (underscore).

1. For **QuickSight dashboard settings** your QuickSight account details such as **account name**, **account ID**, **account edition**, and **authentication method** are automatically populated.

   1. If the QuickSight account details don't populate automatically, choose **Create account** to sign up if you're new to QuickSight, or log in to your QuickSight account if you're an existing QuickSight customer.

   1. Once you successfully create or log in to your QuickSight account, you'll see a success message. Close the window and return to **Data Exports**.

   1. Under **QuickSight dashboard settings**, choose **Refresh**.
**Note**  
This feature requires [Enterprise Edition](https://aws.amazon.com/quicksight/pricing/).

1. For **QuickSight namespace**, enter your [namespace](https://docs.aws.amazon.com/quicksight/latest/user/namespaces.html).

1. For **QuickSight username**, enter the details for the user who has permissions to access the QuickSight dashboard.

1. For **QuickSight region**, choose the AWS Region where you want to create the QuickSight dashboard.

1. The **Data table content settings** and **Data table delivery options** are preset and can't be edited.

1. Under **Data export storage settings**, for **S3 bucket** name, choose **Configure**.

1. In the **Configure S3 bucket** dialog box, do one of the following:
   + Select existing bucket.
   + Choose **Create a bucket**, enter an **S3 bucket name**, and then choose the **Region** where you want to create a new bucket.

1. Review the **Bucket policy**, and then choose **Create bucket**.

1. For **S3 path prefix**, enter the S3 path prefix that you want prepended to the name of your export.

1. Under **Service access**, choose a method to authorize QuickSight:
   + Create a new service role (default)
   + Use an existing service role

1. Under **Tags**, you can choose to add up to 50 tags in order to search and filter your resources or track your AWS costs.
**Note**  
Adding tags is optional.

1. Choose **Create**.

You can always return to the **Data Exports** page of the AWS Billing and Cost Management console to see when your Cost and Usage Dashboard was last updated.