# Data preparation

###### Note

Previously, Amazon SageMaker Data Wrangler was part of the SageMaker Studio Classic experience. Now, if you update to using
the new Studio experience, you must use SageMaker Canvas to access Data Wrangler and receive the latest feature updates.
If you have been using Data Wrangler in Studio Classic until now and want to migrate to Data Wrangler in Canvas,
you might have to grant additional permissions so that you can create and use a Canvas
application. For more information, see [(Optional) Migrate from Data Wrangler in
Studio Classic to SageMaker Canvas](studio-updated-migrate-ui.md#studio-updated-migrate-dw "studio-updated-migrate-ui.md#studio-updated-migrate-dw").

To learn how to migrate your data flows from Data Wrangler in Studio Classic, see
[(Optional) Migrate data from
Studio Classic to Studio](studio-updated-migrate-data.md "studio-updated-migrate-data.md").

Use Amazon SageMaker Data Wrangler in Amazon SageMaker Canvas to prepare, featurize and analyze your data. You can integrate a Data Wrangler data preparation flow
into your machine learning (ML) workflows to simplify and streamline data pre-processing and
feature engineering using little to no coding. You can also add your own Python scripts and
transformations to customize workflows.

- **Data Flow** – Create a data flow to define a
  series of ML data prep steps. You can use a flow to combine datasets from different
  data sources, identify the number and types of transformations you want to apply to
  datasets, and define a data prep workflow that can be integrated into an ML
  pipeline.
- **Transform** – Clean and transform your
  dataset using standard _transforms_ like string,
  vector, and numeric data formatting tools. Featurize your data using transforms like
  text and date/time embedding and categorical encoding.
- **Generate Data Insights** – Automatically verify data quality and detect abnormalities in your data with Data Wrangler Data Quality and Insights Report.
- **Analyze** – Analyze features in your dataset
  at any point in your flow. Data Wrangler includes built-in data visualization tools like
  scatter plots and histograms, as well as data analysis tools like target leakage
  analysis and quick modeling to understand feature correlation.
- **Export** – Export your data preparation workflow to a different location. The following are example locations:
  - Amazon Simple Storage Service (Amazon S3) bucket
  - Amazon SageMaker Feature Store – Store the features and their data in a centralized store.

- **Automate data preparation** – Create machine learning workflows from your data flow.
  - Amazon SageMaker Pipelines – Build workflows that manage your SageMaker AI data preparation, model training, and model deployment jobs.
  - Serial inference pipeline – Create a serial inference pipeline from your data flow. Use it to make predictions on new data.
  - Python script – Store the data and their transformations in a Python script for your custom workflows.
