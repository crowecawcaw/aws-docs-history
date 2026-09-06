

# Transforming data
<a name="dw-transform-data"></a>

 To transform data in Data Wrangler, you add a **Transform** step to your data flow. Data Wrangler includes over 300 transforms that you can use to prepare your data, including a **Map columns for Amazon Personalize** transform. And you can use the general Data Wrangler transforms to fix issues such as outliers, type issues, and missing values. 

After you finish transforming your data, you can analyze it with Data Wrangler. Or, if you are finished preparing your data in Data Wrangler, you can process it and import it into Amazon Personalize. For information about analyzing data, see [Generating visualizations and data insights](dw-analyze-data.md). For information about processing and importing data, see [Processing data and importing it into Amazon Personalize](dw-export-data.md).

**Topics**
+ [Mapping columns for Amazon Personalize](#dw-personalize-transform)
+ [General Data Wrangler transforms](#dw-general-transform)

## Mapping columns for Amazon Personalize
<a name="dw-personalize-transform"></a>

 To transform your data so it meets Amazon Personalize requirements, you add the **Map columns for Amazon Personalize** transform and map your columns to the required and optional fields for Amazon Personalize.

**To use the Map columns for Amazon Personalize transform**

1.  Choose **\+** for your latest transform and choose **Add transform**. If you haven't added a transform, choose the **\+** for the **Data types** transform. Data Wrangler adds this transform automatically to your flow. 

1.  Choose **Add step**. 

1.  Choose **Transforms for Amazon Personalize**. The **Map columns for Amazon Personalize** transform is selected by default. 

1. Use the transform fields to map your data to required Amazon Personalize attributes.

   1. Choose the dataset type that matches your data (Interactions, Items, or Users). 

   1. Choose your domain (ECOMMERCE, VIDEO\_ON\_DEMAND, or custom). The domain you choose must match the domain you specified when you created your dataset group.

   1. Choose the columns that match the required and optional fields for Amazon Personalize. For example, for the item\_ID column, choose the column in your data that stores the unique identification information for each of your items. 

      Each column field is filtered by data type. Only the columns in your data that meet Amazon Personalize data type requirements are available. If your data is not of the required type, you can use the [Parse Value as Type](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-cast-type) Data Wrangler transform to convert it.

## General Data Wrangler transforms
<a name="dw-general-transform"></a>

 The following general Data Wrangler transforms can help you prepare data for Amazon Personalize: 
+ Data type conversion: If your field is not listed as a possible option in the **Map columns for Amazon Personalize** transform, you might need to convert its data type. The Data Wrangler transform [Parse Value as Type](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-cast-type) can help you convert your data. Or you can use the **Data types** transform that Data Wrangler adds by default when you create a flow. To use this transform, you choose the data type from the **Type** drop-down lists, choose **Preview** and then choose **Update**.

   For information on required data types for fields, see the section for your domain and dataset type in [Creating schema JSON files for Amazon Personalize schemas](how-it-works-dataset-schema.md). 
+ Handling missing values and outliers: If you generate missing value or outlier insights, you can use the Data Wrangler transforms [Handle Outliers](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-handle-outlier) and [Handle Missing Values](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-handle-missing) to resolve these issues. 
+  Custom transformations: With Data Wrangler, you can create your own transformations with Python (User-Defined Function), PySpark, pandas, or PySpark (SQL). You might use a custom transform to perform tasks such as dropping duplicate columns or grouping by columns. For more information, see [Custom Transforms](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html#data-wrangler-transform-custom) in the *Amazon SageMaker AI Developer Guide*. 