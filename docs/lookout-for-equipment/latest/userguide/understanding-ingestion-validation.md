On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Reviewing data ingestion

Lookout for Equipment has [ingested your data](ingest-dataset.md#ingesting-data "ingest-dataset.md#ingesting-data"). Now it's time to make
sure everything went according to plan.

###### Note

After ingestion, a red or green status bar will appear at the top of the console
screen. Although a green status bar indicates success, there may still be issues with
specific files or sensors. It is still necessary to review the data validation
summary.

###### Topics

- [Reviewing the job](when-ingestion-jobs-fail.md "when-ingestion-jobs-fail.md")
- [Checking the files](when-files-dont-get-ingested.md "when-files-dont-get-ingested.md")
- [Evaluating sensor grades](reading-details-by-sensor.md "reading-details-by-sensor.md")

###### Next steps:

- If your entire job did not succeed, then a red bar has appeared at the top of the
  **Ingest dataset**page. In that case, it's time to [review the job](when-ingestion-jobs-fail.md "when-ingestion-jobs-fail.md").
- If the job itself succeeded, but not every file was ingested, then you'll find
  yourself on the details page for your dataset, with an error message indicating that
  there was a problem ingesting certain files. In that case, it's time to [check the files](when-files-dont-get-ingested.md "when-files-dont-get-ingested.md").
- If you did not receive any error messages regarding the ingestion job as a whole,
  or with issues with ingesting specific files, then it's time to look at your data's
  [details by sensor](reading-details-by-sensor.md "reading-details-by-sensor.md").
- If you want to make changes to your dataset based on what you've learned so far,
  and then re-ingest it, skip to [replacing your
  dataset](replacing-your-dataset.md "replacing-your-dataset.md").
