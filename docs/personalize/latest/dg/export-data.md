# Exporting the training data in a dataset to Amazon S3

After you import your data into an Amazon Personalize dataset, you can export the data to an Amazon S3 bucket. You might export data to
verify and inspect the data that Amazon Personalize uses to generate recommendations, view the item interaction events that you previously
recorded in real time, or perform offline analysis on your data.

You can choose to export only the data that you imported in bulk (imported using an Amazon Personalize dataset import job), only the
data that you imported individually (records imported using the console or the `PutEvents`, `PutUsers`,
or `PutItems` operations), or both.

###### Note

You can't export data in an Action interactions dataset or Actions dataset.

For records that match exactly _for all fields_, Amazon Personalize exports just one record. If two
records have the same ID but one or more fields are different, Amazon Personalize includes or removes the records depending on data you
choose to export:

- If you export both bulk and incremental data, Amazon Personalize exports only the newest items with the same ID (in Items dataset
  exports), and only users with the same ID (in Users dataset exports). For Item interactions datasets, Amazon Personalize exports all item
  interactions data.
- If you export incremental data only, Amazon Personalize exports all item, user, or item interaction data that you imported
  individually, including items or users with the same IDs. Only records that match exactly for all fields are
  excluded.
- If you export bulk data only, Amazon Personalize includes all item, user, or item interaction data that you imported in bulk,
  including items or users with the same IDs. Only records that match exactly for all fields are excluded.
  To export a dataset, you create a dataset export job. A _dataset export job_ is a record
  export tool that outputs the records in a dataset to one or more CSV files in an Amazon S3 bucket. The output CSV file includes a
  header row with column names that match the fields in the dataset's schema.

###### Topics

- [Dataset export job permissions requirements](export-permissions.md "export-permissions.md")
- [Creating a dataset export job in Amazon Personalize](create-dataset-export-job.md "create-dataset-export-job.md")
