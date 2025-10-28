# Using machine learning and generative AI in Amazon SageMaker Unified Studio

###### Note

Powered by Amazon Bedrock: AWS implements automated abuse detection. Because the
AI recommendations for descriptions functionality in Amazon SageMaker Unified Studio is built on Amazon
Bedrock, users inherit the controls implemented in Amazon Bedrock to enforce safety,
security, and the responsible use of AI.

In the current release of Amazon SageMaker Unified Studio, you can use the AI recommendations for names
& descriptions functionality to automate data discovery and cataloging. Support for
generative AI in Amazon SageMaker Unified Studio creates business names and descriptions for assets and
columns. You can use these names and descriptions to add business context for your data
and recommend analysis for datasets, which can help boost data discovery results.

Powered by Amazon Bedrock's large language models, the AI recommendations for data
asset names & descriptions in Amazon SageMaker Unified Studio help you to ensure that your data is
comprehensible and easily discoverable. The AI recommendations also suggest the most
pertinent analytical applications for datasets. By reducing manual documentation tasks
and advising on appropriate data usage, auto-generated names and descriptions can help
you to enhance the trustworthiness of your data and minimize overlooking valuable data
to accelerate informed decision making.

## Supported Regions

In the current Amazon SageMaker Unified Studio release, the AI recommendations for names and
descriptions feature is supported in the following regions:

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (London)
- South America (Sao Paulo)
- Europe (Ireland)
- Asia Pacific (Singapore)
- US East (Ohio)
- Asia Pacific (Seoul)

Amazon SageMaker Unified Studio supports Business Description Generation in the following
regions.

- Asia Pacific (Mumbai)
- Europe (Paris)

Amazon SageMaker Unified Studio supports Business Name Generation in the following regions.

- Europe (Stockholm)

###### Bedrock Cross Region Inference

Amazon SageMaker Unified Studio leverages Amazon Bedrock's Cross Region inference endpoint to serve
recommendations for the US East (Ohio) region. All other regions use in-region
endpoint.

## Steps to use GenAI

The following procedure describes how to generate AI recommendations for names and
descriptions in Amazon SageMaker Unified Studio:

- Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
  using your SSO or AWS credentials.
- Choose the project that contains the asset for which you want to generate
  AI recommendations for descriptions.

### Generating Business

Descriptions and Summaries

- Navigate to the **Data** tab for the project.
- From **Project catalog**, choose
  **Assets** and chose the asset for which you want
  to generate AI recommendations for descriptions.
- On the asset's details page, in the **Business
  metadata** tab, choose **Generate
  descriptions**.

### Generating Business Names

- Navigate to the **Data** tab for the project.
- In the left navigation pane, choose **Data sources**,
  and then choose datasource for which you want to enable business name
  generation.
- Go to the **details** tab and enable the
  **AUTOMATED BUSINESS NAME GENERATION**
  configuration.
- BusinessNames can also be generated programmatically when creating an
  asset by enabling the businessNameGeneration flag under
  predictionConfiguration in the [CreateAsset API](../../../datazone/latest/APIReference/API_CreateAsset.md "../../../datazone/latest/APIReference/API_CreateAsset.md") payload.

### Accepting/Rejecting

Predictions

- Once the descriptions are generated, you can either edit, accept, or
  reject them.
- Green icons are displayed next to each automatically generated
  metadata description for the data asset. In the **Business
  metadata** tab, you can choose the green icon next to the
  automatically generated **Summary**, and then choose
  **Edit**, **Accept**, or
  **Reject** to address the generated
  description.
- You can also choose **Accept all** or
  **Reject all** options that are displayed at the
  top of the page when the **Business metadata** tab is
  selected, and thus perform the selected action on all automatically
  generated descriptions.
- Or you can choose the **Schema** tab, and then
  address automatically generated descriptions individually by choosing
  the green icon for one column description at a time and then choosing
  **Accept** or **Reject**.
- In the **Schema** tab, you can also choose
  **Accept all** or **Reject all**
  and thus perform the selected action on all automatically generated
  descriptions.

To publish the asset to the catalog with the generated descriptions, choose
**Publish asset**, and then confirm this action by choosing
**Publish asset** again in the **Publish
asset** pop up window.

###### Note

If you don't accept or reject the generated descriptions for an asset, and
then you publish this asset, this unreviewed automatically generated
metadata is not included in the published data asset.

## Support for custom relational asset

types

Amazon SageMaker Unified Studio supports genAI capabilities for custom asset types. Previously this
feature was only supported for the managed AWS Glue and Amazon Redshift asset
types.

In order to enable this feature, create your own asset type definition and attach
`RelationalTableFormType` as one of the forms. Amazon SageMaker Unified Studio
automatically detects the presence of such forms and enables GenAI capabilities for
these assets. The overall experience remains the same for generating business names
(via predictionConfiguration in the CreateAsset API) and businessDescription (via
Generate Description button click on the asset details page).

For more information about creating custom asset types see [Create custom asset types in Amazon SageMaker Unified Studio](create-asset-types.md "create-asset-types.md").

## Quotas

Amazon SageMaker Unified Studio supports different quotas for business name generation and business
description generation. You can reach out to the AWS support team for an increase
in these quotas.

- BusinessDescriptionGeneration: 10K invocations/month
- BusinessNameGeneration: 50K invocations/month
