# Privacy-enhanced synthetic dataset

generation

A _synthetic dataset_ has similar statistical
properties to the original dataset it's based on, but doesn't contain the real-world
observations present in the original dataset. By using privacy-enhanced synthetic
datasets, you can unlock new machine learning (ML) model training use cases that data
privacy concerns previously prevented. When you create an ML input channel, you can
generate synthetic data to protect sensitive information while training ML models.

When creating a template with synthetic data, you must:

- Require template output to be synthetic
- Classify output schema columns as numerical or categorical
- Customize synthetic data based on organizational needs
- Adjust privacy settings:
  - Set privacy level (epsilon)
  - Configure privacy threshold

###### Warning

Synthetic data generation protects against inferring individual attributes whether
specific individuals are present in the original dataset or learning attributes of
those individuals are present. However, it doesn't prevent literal values from the
original dataset, including personally identifiable information (PII) from appearing
in the synthetic dataset.

We recommend avoiding values in the input dataset that are associated with only
one data subject because these may re-identify a data subject. For example, if only
one user lives in a zip code, the presence of that zip code in the synthetic dataset
would confirm that user was in the original dataset. Techniques like truncating high
precision values or replacing uncommon catalogues with _other_ can be used to mitigate this risk. These transformations can
be part of the query used to create the ML input channel.

For more information about how to generate synthetic data for custom model training,
see [Creating a SQL analysis template](create-sql-analysis-template.md "create-sql-analysis-template.md").

Analysis templates with synthetic outputs can only be used to create ML input
channels. For more information, see [Creating an ML input channel in
AWS Clean Rooms ML](create-ml-input-channel.md "create-ml-input-channel.md").
