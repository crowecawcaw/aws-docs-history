# Step 3: Running analysis jobs on documents in

Amazon S3

After storing the data in Amazon S3, you can begin running Amazon Comprehend analysis jobs. A _sentiment_ analysis job determines the overall mood of a
document (positive, negative, neutral, or mixed). An _entities_ analysis job extracts the names of real-world objects from a
document. These objects include people, places, titles, events, dates, quantities, products,
and organizations. In this step, you run two Amazon Comprehend analysis jobs to extract the sentiment
and entities from the sample dataset.

###### Topics

- [Prerequisites](#tutorial-reviews-analysis-prereqs "#tutorial-reviews-analysis-prereqs")
- [Analyze sentiment and entities](#tutorial-reviews-analysis-jobs "#tutorial-reviews-analysis-jobs")

## Prerequisites

Before you begin, do the following:

- Complete [Step 1: Adding documents to Amazon S3](tutorial-reviews-add-docs.md "tutorial-reviews-add-docs.md").
- (Optional) If you are using the AWS CLI, complete [Step 2: (CLI only) creating an IAM role for
  Amazon Comprehend](tutorial-reviews-create-role.md "tutorial-reviews-create-role.md") and
  have your IAM role ARN ready.

## Analyze sentiment and entities

The first job you run analyzes the sentiment of each customer review in the sample
dataset. The second job extracts the entities in each customer review. You can perform
Amazon Comprehend analysis jobs either using the Amazon Comprehend console or the AWS CLI.

###### Tip

Make sure that you are in an AWS Region that supports Amazon Comprehend. For more information,
see the [Region
table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") in the _Global Infrastructure
Guide_.

When using the Amazon Comprehend console, you create one job at a time. You need to repeat
the following steps in order to run both a sentiment and an entities analysis
job. Note that for the first job, you create an IAM role, but for the second
job, you can reuse the first job's IAM role. You can reuse the IAM role as long
as you use the same S3 bucket and folders.

###### To run sentiment and entities analysis jobs (console)

1.  Ensure that you're in the same Region in which you created your
    Amazon Simple Storage Service (Amazon S3) bucket. If you're in another Region, in the navigation
    bar, choose the AWS Region where you created your S3 bucket from the
    **Region selector**.
2.  Open the Amazon Comprehend console at [https://console.aws.amazon.com/comprehend/](https://console.aws.amazon.com/comprehend/ "https://console.aws.amazon.com/comprehend/")
3.  Choose **Launch Amazon Comprehend**.
4.  In the navigation pane, choose **Analysis
    jobs**.
5.  Choose **Create job**.
6.  In the **Job settings** section, do the
    following:
    1. For **Name**, enter
       `reviews-sentiment-analysis`.
    2. For **Analysis type**, choose
       **Sentiment**.
    3. For **Language**, choose
       **English**.
    4. Leave the **Job encryption** setting as disabled.

7.  In the **Input data** section, do the
    following:
    1. For **Data source**, choose **My
       documents**.
    2. For **S3 location**, choose **Browse
       S3** and then choose your bucket from the list of
       buckets.
    3. In your S3 bucket, for **Objects**, choose
       your `input` folder.
    4. In the `input` folder, choose the sample dataset
       `amazon-reviews.csv` and then choose
       **Choose**.
    5. For **Input format**, choose **One
       document per line**.

8.  In the **Output data** section, do the
    following:
    1. For **S3 location**, choose **Browse
       S3** and then choose your bucket from the list of
       buckets.
    2. In your S3 bucket, for **Objects**, choose
       the `output` folder and then choose
       **Choose**.
    3. Leave **Encryption** turned off.

9.  In the **Access permissions** section, do the
    following:
    1. For **IAM role**, choose **Create
       an IAM role**.
    2. For **Permissions to access**, choose
       **Input and Output S3 buckets**.
    3. For **Name suffix**, enter
       `comprehend-access-role`. This role provides
       access to your Amazon S3 bucket.

10. Choose **Create job**.
11. Repeat steps 1-10 to create an entities analysis job. Make the
    following changes:

        1. In **Job settings**, for
         **Name**, enter
         `reviews-entities-analysis`.
        2. In **Job settings**, for **Analysis
         type**, choose
         **Entities**.
        3. In **Access permissions**, choose
         **Use an existing IAM role**. For
         **Role name**, choose
         `AmazonComprehendServiceRole-comprehend-access-role`
         (this is the same role you created for the sentiment
         job).

    You use the `start-sentiment-detection-job` and the
    `start-entities-detection-job` commands to run sentiment and
    entities analysis jobs. After you run each command, the AWS CLI shows a JSON
    object with a `JobId` value that allows you to access details about
    the job, including the output S3 location.

###### To run sentiment and entities analysis jobs (AWS CLI)

1. Start a sentiment analysis job by running the following command in the
   AWS CLI. Replace
   `arn:aws:iam::123456789012:role/comprehend-access-role`
   with the IAM role ARN that you previously copied to a text editor. If
   your default AWS CLI Region differs from the Region in which you created
   your Amazon S3 bucket, include the `--region` parameter and
   replace `us-east-1` with the
   Region where your bucket resides.

```
aws comprehend start-sentiment-detection-job
--input-data-config S3Uri=s3://amzn-s3-demo-bucket/input/
--output-data-config S3Uri=s3://amzn-s3-demo-bucket/output/
--data-access-role-arn `arn:aws:iam::123456789012:role/comprehend-access-role`
--job-name reviews-sentiment-analysis
--language-code en
[--region `us-east-1`]
```

2. After you submit the job, copy the `JobId` and save it to a
   text editor. You will need the `JobId` to find the output
   files from the analysis job.
3. Start an entities analysis job by running the following
   command.

```
aws comprehend start-entities-detection-job
--input-data-config S3Uri=s3://amzn-s3-demo-bucket/input/
--output-data-config S3Uri=s3://amzn-s3-demo-bucket/output/
--data-access-role-arn `arn:aws:iam::123456789012:role/comprehend-access-role`
--job-name reviews-entities-analysis
--language-code en
[--region `us-east-1`]
```

4. After you submit the job, copy the `JobId` and save it to a
   text editor.
5. Check the status of your jobs. You can view the progress of a job by
   tracking its `JobId`.

To track the progress of your sentiment analysis job, run the
following command. Replace
`sentiment-job-id` with
the `JobId` that you copied after running your sentiment
analysis.

```
aws comprehend describe-sentiment-detection-job
--job-id `sentiment-job-id`
```

To track your entities analysis job, run the following command.
Replace `entities-job-id` with the
`JobId` that you copied after running your entities
analysis.

```
aws comprehend describe-entities-detection-job
--job-id `entities-job-id`
```

It takes several minutes for the `JobStatus` to show as
`COMPLETED`.

You have completed sentiment and entities analysis jobs. Both of the jobs should be
completed before you move on to the next step. It can take several minutes for the jobs to
finish.
