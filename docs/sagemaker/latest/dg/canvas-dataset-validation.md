# Data validation

Before you build your model, SageMaker Canvas checks your dataset for issues that might cause your
build to fail. If SageMaker Canvas finds any issues, then it warns you on the **Build**
page before you attempt to build a model.

You can choose **Validate data** to see a list of the issues with your
dataset. You can then use the SageMaker Canvas [Data Wrangler data preparation
features](canvas-data-prep.md "canvas-data-prep.md"), or your own tools, to fix your dataset before starting a build. If you don’t
fix the issues with your dataset, then your build fails.

If you make changes to your dataset to fix the issues, you have the option to re-validate
your dataset before attempting a build. We recommend that you re-validate your dataset before
building.

The following table shows the issues that SageMaker Canvas checks for in your dataset and how to
resolve them.

| Issue                                                      | Resolution                                                                                                                                               |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Wrong model type for your data                             | Try another model type or use a different dataset.                                                                                                       |
| Missing values in your target column                       | Replace the missing values, drop rows with missing values, or use a different<br>dataset.                                                                |
| Too many unique labels in your target column               | Verify that you've used the correct column for your target column, or use a different<br>dataset.                                                        |
| Too many non-numeric values in your target column          | Choose a different target column, select another model type, or use a different<br>dataset.                                                              |
| One or more column names contain double underscores        | Rename the columns to remove any double underscores, and try again.                                                                                      |
| None of the rows in your dataset are complete              | Replace the missing values, or use a different dataset.                                                                                                  |
| Too many unique labels for the number of rows in your data | Check that you're using the right target column, increase the number of rows in your<br>dataset, consolidate similar labels, or use a different dataset. |
