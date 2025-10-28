# Text classification for model evaluation in Amazon Bedrock

Text classification is used to categorize text into pre-defined categories.
Applications that use text classification include content recommendation, spam
detection, language identification and trend analysis on social media. Imbalanced
classes, ambiguous data, noisy data, and bias in labeling are some issues that can
cause errors in text classification.

###### Important

For text classification, there is a known system issue that prevents Cohere
models from completing the toxicity evaluation successfully.

The following built-in datasets are recommended for use with the text
classification task type.

**Women's E-Commerce Clothing Reviews**

Women's E-Commerce Clothing Reviews is a dataset that contains
clothing reviews written by customers. This dataset is used in text
classification tasks.

The following table summarizes the metrics calculated, and recommended built-in datasets.
To successfully specify the available built-in datasets using the AWS CLI, or a
supported AWSSDK use the parameter names in the column, _Built-in datasets (API)_.

| Available built-in datasets in Amazon Bedrock | Task type                                                                                                                                                                                         | Metric                                                                                                                                                                                            | Built-in datasets (console)                                           | Built-in datasets (API)                                                                                                                                                                                               | Computed metric |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| Text classification                           | Accuracy                                                                                                                                                                                          | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | `Builtin.WomensEcommerceClothingBoolQ`                                | Accuracy (Binary Accuracy from classification_accuracy_score)                                                                                                                                                         |
| Robustness                                    | [Women's Ecommerce Clothing Reviews](https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews "https://www.kaggle.com/datasets/nicapotato/womens-ecommerce-clothing-reviews") | `Builtin.WomensEcommerceClothingBoolQ`                                                                                                                                                            | classification_accuracy_score and delta_classification_accuracy_score | To learn more about how the computed metric for each built-in dataset is calculated, see [Review model evaluation job reports and metrics in Amazon Bedrock](model-evaluation-report.md "model-evaluation-report.md") |
