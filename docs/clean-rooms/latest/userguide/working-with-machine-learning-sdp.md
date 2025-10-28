# Creating AWS Clean Rooms ML models as a seed

data provider

After the training data provider is done creating the ML model, the seed data provider can
create and export the lookalike segment. The lookalike segment is a subset of the training
data that most closely resembles the seed data.

This is the workflow that the seed data provider must complete:

1. The seed data provider's data can be stored in an Amazon S3 bucket or it can come
   from the results of query.
2. The seed data provider opens the collaboration that they share with the
   training data provider.
3. The seed data provider creates a lookalike segment from the Clean Rooms ML tab of the
   collaboration page.
4. The seed data provider can evaluate the relevance metrics, if they were
   shared, and export the lookalike segment for use outside AWS Clean Rooms.

###### Topics

- [Creating a lookalike segment](create-ml-segment-create.md "create-ml-segment-create.md")
- [Exporting a lookalike segment](create-ml-segment-export.md "create-ml-segment-export.md")
