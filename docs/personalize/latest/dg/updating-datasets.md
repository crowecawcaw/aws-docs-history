# Updating data in datasets after training

As your catalog grows, import additional training data into your datasets. This helps maintain and improve the relevance of Amazon Personalize recommendations.
You can import more data with bulk or individual data import operations.

- With individual imports, Amazon Personalize appends the new records to the dataset. To update an individual item,
  user, or action, you can import a record with the same ID but with the modified attributes. You can import up to
  10 records per individual import operation.

For more information on importing records individually, see [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md"). For information about recording real-time events, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md").

- With bulk imports, you add to or replace bulk data by [creating another import
  job](bulk-data-import-step.md "bulk-data-import-step.md"). By default, a dataset import job replaces any existing data in the dataset that you imported in bulk. You
  can instead append the new records to existing data by changing the job's [import
  mode](bulk-data-import-step.md#bulk-import-modes "bulk-data-import-step.md#bulk-import-modes").

To append data to an Item interactions dataset or Action interactions dataset with a dataset import job, you must have at
minimum 1000 new item interaction or action interaction records. Within 20 minutes of
completing a bulk import, Amazon Personalize updates any filters you created in the dataset group with your new bulk data. This update
allows Amazon Personalize to use the most recent data when filtering recommendations for your users.
After you create an Items or Users dataset, you can replace its schema with a new or existing one. You might replace a dataset's
schema if your data structure changed after you created the dataset. For example, you might have a new column of item metadata
that you want Amazon Personalize to consider during training. Or you might want to add a column of data to use only when filtering
recommendations. For more information, see [Replacing a dataset's schema to add new columns](updating-dataset-schema.md "updating-dataset-schema.md").

After you create a recommender or custom solution version, how new data
influences recommendations depends on its type, the method of import, and the domain use case or custom recipe you use. The following sections
explain how new data influences real-time and batch recommendations before the next training.

###### Topics

- [How new data influences real-time recommendations](how-new-data-influences-recommendations.md "how-new-data-influences-recommendations.md")
- [How new data influences batch recommendations (custom resources)](how-new-data-influences-batch-recommendations.md "how-new-data-influences-batch-recommendations.md")
