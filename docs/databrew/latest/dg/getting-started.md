# Step 5: Create a data profile

When you work with on a project, DataBrew displays statistics such as the number of rows
in the sample and the distribution of unique values in each column. These statistics,
and many more, represent a _profile_ of the
sample.

To request a data profile, create and run a profile job.

###### To profile a dataset

1. On the navigation pane, choose **Jobs**.
2. On the **Profile jobs** tab, choose **Create
   job**.
3. For **Job name**, enter
   `chess-data-profile`.
4. For **Job type**, choose **Create a profile
   job**.
5. On the **Job input** pane, do the following:
   - For **Run on**, choose
     **Dataset**.
   - Choose **Select a dataset** to view a list of
     available datasets, and choose `chess-games`.

6. On the **Job output settings** pane, do the following:
   - For **File type**, choose **JSON**
     (JavaScript Object Notation).
   - Choose **S3 location** to view a list of available
     Amazon S3 buckets, and choose the bucket to use. Then choose
     **Browse**. In the list of folders, choose
     `databrew-output`, and chose
     **Select**.

7. On the **Access permissions** pane, choose
   `AwsGlueDataBrewDataAccessRole`. This is a service linked role that
   lets DataBrew access your Amazon S3 buckets on your behalf.
8. Choose **Create and run job**. DataBrew creates a job with your
   settings, and then runs it.
9. On the **Job run history** pane, wait for the job status to
   change from `Running` to `Succeeded`.
10. To view the profile, choose **VIEW
    PROFILE**:

![Icon of a person silhouette with "VIEW PROFILE" text underneath.](images/view-profile-button.png)

The **DATASETS** window is shown. Take some time
to explore the following tabs:

    * Dataset preview
    * Profile overview
    * Column statistics
    * Data lineage statistics
