# How the data flow UI works

To help you navigate your data flow, Data Wrangler has the following tabs in the top navigation pane:

- **Data flow** – This tab provides you with a visual view of your
  data flow step where you can add or remove transforms, and export data.
- **Data** – This tab gives you a preview of your data so that you
  can check the results of your transforms. You can also see an ordered list of your data flow steps
  and edit or reorder the steps.

###### Note

In this tab, you can only preview data visualizations (such as the distribution of values per column)
for Amazon S3 data sources. Visualizations for other data sources, such as Amazon Athena, aren't supported.

- **Analyses** – In this tab, you can see separate sub-tabs for each
  analysis you create. For example, if you create a histogram and a Data Quality and Insights (DQI) report,
  Canvas creates a tab for each.
  When you import a dataset, the original dataset appears on the data flow and is named
  **Source**. SageMaker Canvas automatically infers
  the types of each column in your dataset and creates a new dataframe named
  **Data types**. You can select this frame to update the inferred
  data types.

The datasets, transformations, and analyses that you use in the data flow are
represented as _steps_. Each time you add a transform
step, you create a new dataframe. When multiple transform steps (other than
**Join** or **Concatenate**) are added to the same
dataset, they are stacked.

Under the **Combine data** option,
**Join** and **Concatenate** create standalone steps
that contain the new joined or concatenated dataset.
