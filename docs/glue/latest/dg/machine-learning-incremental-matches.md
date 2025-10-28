# Finding incremental matches

The Find matches feature allows you to identify duplicate or matching records in your dataset, even when the records don’t have a common unique identifier and no fields match exactly. The initial release of the Find matches transform identified matching records within a single dataset. When you add new data to the dataset, you had to merge it with the existing clean dataset and rerun matching against the complete merged dataset.

The incremental matching feature makes it simpler to match to incremental records against existing matched datasets. Suppose that you want to match prospects data with existing customer datasets. The incremental match capability provides you the flexibility to match hundreds of thousands of new prospects with an existing database of prospects and customers by merging the results into a single database or table. By matching only between the new and existing datasets, the find incremental matches optimization reduces computation time, which also reduces cost.

The usage of incremental matching is similar to Find matches as described in [Tutorial: Creating a machine learning transform with
AWS Glue](machine-learning-transform-tutorial.md "machine-learning-transform-tutorial.md"). This topic identifies only the differences with incremental matching.

For more information, see the blog post on [Incremental data matching](https://aws.amazon.com/blogs/big-data/incremental-data-matching-using-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/incremental-data-matching-using-aws-lake-formation/").

## Running an incremental matching job

For the following procedure, suppose the following:

- You have crawled the existing dataset into the table _first_records_. The _first_records_ dataset must be a matched dataset, or the output of the matched job.
- You have created and trained a Find matches transform with AWS Glue version 2.0. This is the only version of AWS Glue that supports incremental matches.
- The ETL language is Scala. Note that Python is also supported.
- The model already generated is called `demo-xform`.

1. Crawl the incremental dataset to the table _second_records_.
2. On the AWS Glue console, in the navigation pane, choose **Jobs**.
3. Choose **Add job**, and follow the steps in the wizard to create an ETL Spark job with a generated script. Choose the following property values for your transform:
   1. For **Name**, choose **demo-etl**.
   2. For **IAM role**, choose an IAM role with permission to the Amazon S3
      source data, labeling file, and [AWS Glue API operations](create-an-iam-role.md "create-an-iam-role.md").
   3. For **ETL language**, choose **Scala**.
   4. For **Script file name**, choose
      **demo-etl**. This is the file name of the Scala script.
   5. For **Data source**, choose
      **first_records**. The data source you choose must match the
      machine learning transform data source schema.
   6. For **Transform type**, choose **Find matching
      records** to create a job using a machine learning transform.
   7. Select the incremental matching option, and for **Data Source** select the table named **second_records**.
   8. For **Transform**, choose
      **demo-xform**, the machine learning transform used by the
      job.
   9. Choose **Create tables in your data target** or **Use tables in the data catalog and update your data target**.

4. Choose **Save job and edit script** to display the script editor page.
5. Choose **Run job** to start the job run.
