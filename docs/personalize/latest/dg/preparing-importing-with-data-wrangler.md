# Preparing and importing bulk data using Amazon SageMaker AI Data Wrangler

###### Important

As you use Data Wrangler, you incur SageMaker AI costs. For a complete list of charges and prices, see the Data Wrangler
tab of [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
To avoid incurring additional fees, when you are finished, shut down your Data Wrangler instance. For more information,
see [Shut Down Data Wrangler](../../../sagemaker/latest/dg/data-wrangler-shut-down.md "../../../sagemaker/latest/dg/data-wrangler-shut-down.md").

After you create a dataset group, you can use Amazon SageMaker AI Data Wrangler (Data Wrangler) to import data from 40+ sources into an Amazon Personalize dataset. Data Wrangler
is a feature of Amazon SageMaker AI Studio Classic that provides an end-to-end solution to import, prepare, transform, and analyze data. You
can't use Data Wrangler to prepare and import data into an Actions dataset or Action interactions dataset.

When you use Data Wrangler to prepare and import data, you use a data flow. A _data flow_ defines a series of machine
learning data prep steps, starting with importing data. Each time you add a step to your flow, Data Wrangler takes an action on your
data, such as transforming it or generating a visualization.

The following are some of the steps that you can add to your flow to prepare data for Amazon Personalize:

- **Insights:** You can add Amazon Personalize specific insight steps to your flow. These insights can
  help you learn about your data and what actions you can take to improve it.
- **Visualizations:** You can add visualization steps to generate graphs such as histograms
  and scatter plots. Graphs can help you discover issues in your data, such as outliers or missing values.
- **Transformations:** You can use Amazon Personalize specific and general transformation steps to make
  sure your data meets Amazon Personalize requirements. The Amazon Personalize transformation helps you map your data columns to required columns
  depending on the Amazon Personalize dataset type.
  If you need to leave Data Wrangler before importing data into Amazon Personalize, you can return to where
  you left off by choosing the same dataset type when you [launch Data Wrangler from the
  Amazon Personalize console](dw-launch-dw-from-personalize.md "dw-launch-dw-from-personalize.md"). Or you can access Data Wrangler directly through SageMaker AI Studio Classic.

We recommend you import data from Data Wrangler into Amazon Personalize as follows. The transformation, visualization and analysis steps are
optional, repeatable, and can be completed in any order.

1. **[Set up permissions](dw-data-prep-minimum-permissions.md "dw-data-prep-minimum-permissions.md")** - Set up
   permissions for Amazon Personalize and SageMaker AI service roles. And set up permissions for your users.
2. **[Launch Data Wrangler in SageMaker AI Studio Classic from the Amazon Personalize
   console](dw-launch-dw-from-personalize.md "dw-launch-dw-from-personalize.md")** - Use the Amazon Personalize console to configure a SageMaker AI domain and launch Data Wrangler in SageMaker AI Studio Classic.
3. **[Import your data into Data Wrangler](dw-import-data.md "dw-import-data.md")** - Import data from
   40+ sources into Data Wrangler. Sources include AWS services, such as Amazon Redshift, Amazon EMR, or Amazon Athena, and 3rd parties such as
   Snowflake or DataBricks.
4. **[Transform your data](dw-transform-data.md "dw-transform-data.md")** - Use Data Wrangler
   to transform your data to meet Amazon Personalize requirements.
5. **[Visualize and analyze your data](dw-analyze-data.md "dw-analyze-data.md")** - Use Data Wrangler to
   visualize your data and analyze it through Amazon Personalize specific insights.
6. **[Process and import data into Amazon Personalize](dw-export-data.md "dw-export-data.md")** - Use a SageMaker AI Studio Classic
   Jupyter notebook to import your processed data into Amazon Personalize.

## Additional information

The following resources provide additional information about using Amazon SageMaker AI Data Wrangler and Amazon Personalize.

- For a tutorial that walks you through processing and transforming a sample dataset, see [Demo: Data Wrangler Titanic
  Dataset Walkthrough](../../../sagemaker/latest/dg/data-wrangler-getting-started.md#data-wrangler-getting-started-demo "../../../sagemaker/latest/dg/data-wrangler-getting-started.md#data-wrangler-getting-started-demo") in the _Amazon SageMaker AI Developer Guide_. This tutorial introduces the fields
  and functions of Data Wrangler.
- For information on onboarding to Amazon SageMaker AI domains, see [Quick onboard to Amazon SageMaker AI Domain](../../../sagemaker/latest/dg/onboard-quick-start.md "../../../sagemaker/latest/dg/onboard-quick-start.md") in
  the _Amazon SageMaker AI Developer Guide_.
- For information on Amazon Personalize data requirements, see [Preparing training data for Amazon Personalize](preparing-training-data.md "preparing-training-data.md").
