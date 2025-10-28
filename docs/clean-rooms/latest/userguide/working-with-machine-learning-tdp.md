# Create AWS Clean Rooms ML models as a training

data provider

A _lookalike model_ is a model of a training data provider's data that
allows a seed data provider to create a lookalike segment of training data provider's data
that most closely resembles their seed data. To create a lookalike model that can be used in
a collaboration, you must import your training data, create a lookalike model, configure
that lookalike model, and then associate it to a collaboration.

Working with lookalike models requires that two parties, a training data provider and a
seed data provider, work sequentially in AWS Clean Rooms to bring their data into a collaboration.
This is the workflow that the training data provider must complete first:

1. The training data provider's data must be stored in a AWS Glue data catalog table of
   user-item interactions. At a minimum, the training data must contain a user ID
   column, interaction ID column, and a timestamp column.
2. The training data provider registers the training data with AWS Clean Rooms.
3. The training data provider creates a lookalike model that can be shared with
   multiple seed data providers. The lookalike model is a deep neural network that can
   take up to 24 hours to train. It isn't automatically retrained and we recommend that
   you retrain the model weekly.
4. The training data provider configures the lookalike model, including whether to
   share relevance metrics and the Amazon S3 location of the output segments. The training
   data provider can create multiple configured lookalike models from a single
   lookalike model.
5. The training data provider associates the configured audience model to a
   collaboration that's shared with a seed data provider.
   After the training data provider is done creating the ML model, the [seed data provider can create and export the
   lookalike segment](working-with-machine-learning-sdp.md "working-with-machine-learning-sdp.md").

###### Topics

- [Importing training data](create-ml-model-training-data.md "create-ml-model-training-data.md")
- [Creating a lookalike model](create-ml-model-create-model.md "create-ml-model-create-model.md")
- [Configuring a lookalike model](create-ml-model-configure-model.md "create-ml-model-configure-model.md")
- [Associating a configured lookalike
  model](create-ml-model-associate-model.md "create-ml-model-associate-model.md")
- [Updating a configured lookalike
  model](update-ml-model-configured-model.md "update-ml-model-configured-model.md")
