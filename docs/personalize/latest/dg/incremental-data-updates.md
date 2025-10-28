# Importing individual records into an Amazon Personalize dataset

After you have complete [Creating a schema and a dataset](data-prep-creating-datasets.md "data-prep-creating-datasets.md"), you can import individual
records, including item interactions, users,
items, actions, or action interactions into an existing dataset. Importing data individually allows you to
add small batches of records to your Amazon Personalize datasets as your catalog
grows. You can import up to 10 records per individual
import operation.

If you import an item, user, or action with the same ID as a record that's already in your dataset, Amazon Personalize replaces it
with the new record. If you record two item interaction or action interaction
events with exactly the same timestamp and identical properties, Amazon Personalize keeps only one of the events.

If you use Apache Kafka, you can use the _Kafka connector for Amazon Personalize_ to stream data in real time to Amazon Personalize.
For information see [Kafka Connector for Amazon Personalize](https://github.com/aws/personalize-kafka-connector/blob/main/README.md "https://github.com/aws/personalize-kafka-connector/blob/main/README.md") in the _personalize-kafka-connector_ Github repository.

If you have a large amount of historical records, we recommend that you
first import data in bulk and then import data individually as necessary.
See [Importing bulk data into Amazon Personalize with a
dataset import job](bulk-data-import-step.md "bulk-data-import-step.md").

**Filter updates for individual record
imports**

Amazon Personalize updates any filters you created in the dataset group with your
new interaction, item, and user data within 20 minutes from the last
individual import. This update allows your campaigns to use your most recent
data when filtering recommendations for your users.

If you already created a recommender or deployed a custom solution version with a campaign, how
new individual records influence recommendations depends on the domain use case or recipe that you use. For more information, see [Updating data in datasets after training](updating-datasets.md "updating-datasets.md").

###### Topics

- [Importing interactions
  individually](importing-interactions.md "importing-interactions.md")
- [Importing users individually](importing-users.md "importing-users.md")
- [Importing items individually](importing-items.md "importing-items.md")
- [Importing actions individually](importing-actions.md "importing-actions.md")
