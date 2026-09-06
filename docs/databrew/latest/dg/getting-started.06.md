

# Step 6: Transform the dataset
<a name="getting-started.06"></a>

Until now, you tested your recipe on only a sample of the dataset. Now it's time to transform the entire dataset by creating a DataBrew recipe job. 

When the job runs, DataBrew applies your recipe to all of the data in the dataset, and writes the transformed data to an Amazon S3 bucket. The transformed data is separate from the original dataset. DataBrew doesn't alter the source data.

Before you proceed, ensure that you have an Amazon S3 bucket in your account that you can write to. In that bucket, create a folder to capture the job output from DataBrew. To do these steps, use the following procedure.

**To create an S3 bucket and folder to capture job output**

1. Sign in to the AWS Management Console and open the Amazon S3 console at [https://console.aws.amazon.com/databrew/](https://console.aws.amazon.com/s3/).

   If you already have an Amazon S3 bucket available, and you have write permissions for it, skip the next step.

1. If you don't have an Amazon S3 bucket, choose **Create bucket**. For **Bucket name**, enter a unique name for your new bucket. Choose **Create bucket**. 

1. From the list of buckets, choose the one that you want to use.

1. Choose **Create folder**. 

1. For **Folder name**, enter `databrew-output`, and choose **Create folder**.

After you create an Amazon S3 bucket and folder to contain the job, run your job by using the following procedure.

**To create and run a recipe job**

1. On the navigation pane, choose **Jobs**.

1. On the **Recipe jobs** tab, choose **Create job**.

1. For **Job name**, enter `chess-winner-summary`.

1. For **Job type**, choose **Create a recipe job**.

1. On the **Job input** pane, do the following:
   + For **Run on**, choose **Dataset**.
   + Choose **Select a dataset** to view a list of available datasets, and choose `chess-games`.
   + Choose **Select a recipe** to view a list of available recipes, and choose `chess-project-recipe`.

1. On the **Job output settings** pane, do the following:
   + **File type** – chose **CSV** (comma-separated values).
   + **S3 location **- choose this field to view a list of available Amazon S3 buckets, and choose the bucket to use. Then choose **Browse**. In the list of folders, choose `databrew-output`, and choose **Select**.

1. On the **Access permissions** pane, choose `AwsGlueDataBrewDataAccessRole`. This service-linked role lets DataBrew access your Amazon S3 buckets on your behalf. 

1. Choose **Create and run job**. DataBrew creates a job with your settings, and then runs it.

1. On the **Job run history** pane, wait for the job status to change from `Running` to `Succeeded`.

1. Choose **Output** to access the Amazon S3 console. Choose your S3 bucket, and then choose the` databrew-output` folder to access the job output.

1. (Optional) Choose **Download** to download the file and view its contents.