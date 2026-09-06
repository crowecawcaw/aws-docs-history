

# Reviewing a SQL analysis template
<a name="review-analysis-template"></a>

After a collaboration member has created a SQLanalysis template, you can review and approve it. After the analysis template and approved, it can be used in a query in AWS Clean Rooms.

**Note**  
When you bring your analysis code into a collaboration, be aware of the following:   
AWS Clean Rooms does not validate or guarantee the behavior of the analysis code.   
If you need to ensure certain behavior, review the code of your collaboration partner directly or work with a trusted third-party auditor to review it.
In the shared security model:  
You (the customer) are responsible for the security of the code running in the environment.
AWS Clean Rooms is responsible for the security of the environment, ensuring that  
only the approved code runs 
only specified configured tables are accessible 
the only output destination is the result receiver's S3 bucket.

**To review a SQL analysis template using the AWS Clean Rooms console**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with the AWS account that will function as the collaboration creator.

1. In the left navigation pane, choose **Collaborations**.

1. Choose the collaboration.

1. On the **Templates** tab, go to the **Analysis templates created by other members** section.

1. Choose the analysis template that has the **Can run status** of **No requires your review**.

1. Choose **Review**.

1. Review the analysis rule **Overview**, **Definition**, and **Parameters** (if any). 

1. Review the configured tables listed under **Tables referenced in definition**. 

   The **Status** next to each table will read **Template not allowed**.

1. Choose a table.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/clean-rooms/latest/userguide/review-analysis-template.html)

You are now ready to query the configured table using a SQL analysis template. For more information, see [Running SQL queries](running-sql-queries.md).