# Importing training data into Amazon Personalize datasets

After you complete [create a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"), you are ready to import your
training data into the dataset. When you import data, you can choose to import records in bulk, individually, or both.

- Bulk imports involve importing a large number of historical records at once. You can prepare bulk data yourself, and import it directly into
  Amazon Personalize from a CSV file in Amazon S3. For information about how to prepare your data, see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md").
  If you need help preparing your data, you can use SageMaker AI Data Wrangler to prepare and import your bulk item interaction,
  user, and item data. For more information, see [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](preparing-importing-with-data-wrangler.md "preparing-importing-with-data-wrangler.md").
- If you don't have bulk data, you can use individual import operations to collect data and stream events until you meet
  Amazon Personalize training requirements and the data requirements of your domain use case or recipe. For information about recording events,
  see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md"). For information about importing individual
  records, see [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md").
  After you import data into an Amazon Personalize dataset, you can [analyze it](analyzing-data.md "analyzing-data.md"), [export it to an Amazon S3 bucket](export-data.md "export-data.md"),
  [update it](updating-datasets.md "updating-datasets.md"), or [delete it](delete-dataset.md "delete-dataset.md") by deleting the dataset.

If you import an item, user, or action with the same ID as a record that's already in your dataset, Amazon Personalize replaces it
with the new record. If you record two item interaction or action interaction
events with exactly the same timestamp and identical properties, Amazon Personalize keeps only one of the events.

As your catalog grows, update your historical data with additional bulk, or individual data, import operations. For
real-time recommendations, keep your Item interactions dataset up to date with your users' behavior. You do this by recording
real-time interaction _[events](../../../glossary/latest/reference/glos-chap.md#event "../../../glossary/latest/reference/glos-chap.md#event")_ with an event tracker and the
[PutEvents](API_UBS_PutEvents.md "API_UBS_PutEvents.md") operation. For more information, see [Recording real-time events to influence recommendations](recording-events.md "recording-events.md")

After you import your data, you are ready to create domain recommenders (for Domain dataset groups) or custom resources (for
Custom dataset group) to train a model on your data. You use these resources to generate recommendations. For more
information, see [Domain recommenders in Amazon Personalize](creating-recommenders.md "creating-recommenders.md") or [Custom resources for training and deploying Amazon Personalize models](create-custom-resources.md "create-custom-resources.md").

###### Topics

- [Importing bulk data into Amazon Personalize with a
  dataset import job](bulk-data-import-step.md "bulk-data-import-step.md")
- [Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler](preparing-importing-with-data-wrangler.md "preparing-importing-with-data-wrangler.md")
- [Importing individual records into an Amazon Personalize dataset](incremental-data-updates.md "incremental-data-updates.md")
