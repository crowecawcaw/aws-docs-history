On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Replacing your dataset

Replacing your dataset allows you to change the data without re-creating the project from
the beginning.

You may want to do this after [reviewing the ingestion of your dataset](understanding-ingestion-validation.md "understanding-ingestion-validation.md"), and addressing problems with the job, files, or sensors.

###### Note

If you want to change your schema, then you must start over with a new project.

The **Replace dataset** page is similar to the **Ingest dataset** page that
you visited earlier in the workflow. The main difference is that the **Replace
dataset** page does not ask you for information about how you named your .csv
files. When you replace a dataset, Lookout for Equipment re-uses the schema detection information that you
entered before.

To replace your dataset:

- From the **Dataset details** screen, choose **Replace dataset**.
- On the **Replace dataset** page, indicate the location of your data on Amazon S3
  and choose your IAM role.
- Choose **Start ingestion**.
  After the procedure above, you'll [review your dataset ingestion](understanding-ingestion-validation.md "understanding-ingestion-validation.md") once again.
