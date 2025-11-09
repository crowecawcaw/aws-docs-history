# Data import

Amazon SageMaker Canvas supports importing tabular, image, and document data. You can import datasets
from your local machine, Amazon services such as Amazon S3 and Amazon Redshift, and external data sources. When importing
datasets from Amazon S3, you can bring a dataset of any size. Use the datasets that you import to
build models and make predictions for other datasets.

Each use case for which you can build a custom model accepts different types of input. For example,
if you want to build a single-label image classification model, then you should import image data. For more
information about the different model types and the data they accept, see [How custom models work](canvas-build-model.md "canvas-build-model.md").
You can import data and build custom models in SageMaker Canvas for the following data types:

- **Tabular** (CSV, Parquet, or tables)
  - Categorical – Use categorical data to build custom categorical prediction models for 2 and 3+ category prediction.
  - Numeric – Use numeric data to build custom numeric prediction models.
  - Text – Use text data to build custom multi-category text prediction models.
  - Timeseries – Use timeseries data to build custom time series forecasting models.

- **Image** (JPG or PNG) – Use image data to build custom single-label image prediction models.
- **Document** (PDF, JPG, PNG, TIFF) – Document data is
  only supported for SageMaker Canvas Ready-to-use models. To learn more about Ready-to-use models that can make predictions for document data, see
  [Ready-to-use models](canvas-ready-to-use-models.md "canvas-ready-to-use-models.md").
  You can import data into Canvas from the following data sources:

- Local files on your computer
- Amazon S3 buckets
- Amazon Redshift provisioned clusters (not Amazon Redshift Serverless)
- AWS Glue Data Catalog through Amazon Athena
- Amazon Aurora
- Amazon Relational Database Service (Amazon RDS)
- Salesforce Data Cloud
- Snowflake
- Databricks, SQLServer, MariaDB, and other popular databases through JDBC
  connectors
- Over 40 external SaaS platforms, such as SAP OData
  For a full list of data sources from which you can import, see the following table:

| Source                                                                                                                                                                                | Type                   | Supported data types     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------ |
| Local file upload                                                                                                                                                                     | Local                  | Tabular, Image, Document |
| Amazon Aurora                                                                                                                                                                         | Amazon internal        | Tabular                  |
| Amazon S3 bucket                                                                                                                                                                      | Amazon internal        | Tabular, Image, Document |
| Amazon RDS                                                                                                                                                                            | Amazon internal        | Tabular                  |
| Amazon Redshift provisioned clusters (not Redshift Serverless)                                                                                                                        | Amazon internal        | Tabular                  |
| AWS Glue Data Catalog (through Amazon Athena)                                                                                                                                         | Amazon internal        | Tabular                  |
| [Databricks](https://www.databricks.com/ "https://www.databricks.com/")                                                                                                               | External               | Tabular                  |
| Snowflake                                                                                                                                                                             | External               | Tabular                  |
| [Salesforce Data Cloud](https://www.salesforce.com/products/genie/overview/ "https://www.salesforce.com/products/genie/overview/")                                                    | External               | Tabular                  |
| SQLServer                                                                                                                                                                             | External               | Tabular                  |
| MySQL                                                                                                                                                                                 | External               | Tabular                  |
| PostgreSQL                                                                                                                                                                            | External               | Tabular                  |
| MariaDB                                                                                                                                                                               | External               | Tabular                  |
| [Amplitude](../../../appflow/latest/userguide/amplitude.md "../../../appflow/latest/userguide/amplitude.md")                                                                          | External SaaS platform | Tabular                  |
| [CircleCI](../../../appflow/latest/userguide/connectors-circleci.md "../../../appflow/latest/userguide/connectors-circleci.md")                                                       | External SaaS platform | Tabular                  |
| [DocuSign Monitor](../../../appflow/latest/userguide/connectors-docusign-monitor.md "../../../appflow/latest/userguide/connectors-docusign-monitor.md")                               | External SaaS platform | Tabular                  |
| [Domo](../../../appflow/latest/userguide/connectors-domo.md "../../../appflow/latest/userguide/connectors-domo.md")                                                                   | External SaaS platform | Tabular                  |
| [Datadog](../../../appflow/latest/userguide/datadog.md "../../../appflow/latest/userguide/datadog.md")                                                                                | External SaaS platform | Tabular                  |
| [Dynatrace](../../../appflow/latest/userguide/dynatrace.md "../../../appflow/latest/userguide/dynatrace.md")                                                                          | External SaaS platform | Tabular                  |
| [Facebook Ads](../../../appflow/latest/userguide/connectors-facebook-ads.md "../../../appflow/latest/userguide/connectors-facebook-ads.md")                                           | External SaaS platform | Tabular                  |
| [Facebook Page Insights](../../../appflow/latest/userguide/connectors-facebook-page-insights.md "../../../appflow/latest/userguide/connectors-facebook-page-insights.md")             | External SaaS platform | Tabular                  |
| [Google Ads](../../../appflow/latest/userguide/connectors-google-ads.md "../../../appflow/latest/userguide/connectors-google-ads.md")                                                 | External SaaS platform | Tabular                  |
| [Google Analytics 4](../../../appflow/latest/userguide/connectors-google-analytics-4.md "../../../appflow/latest/userguide/connectors-google-analytics-4.md")                         | External SaaS platform | Tabular                  |
| [Google Search Console](../../../appflow/latest/userguide/connectors-google-search-console.md "../../../appflow/latest/userguide/connectors-google-search-console.md")                | External SaaS platform | Tabular                  |
| [GitHub](../../../appflow/latest/userguide/connectors-github.md "../../../appflow/latest/userguide/connectors-github.md")                                                             | External SaaS platform | Tabular                  |
| [GitLab](../../../appflow/latest/userguide/connectors-gitlab.md "../../../appflow/latest/userguide/connectors-gitlab.md")                                                             | External SaaS platform | Tabular                  |
| [Infor Nexus](../../../appflow/latest/userguide/infor-nexus.md "../../../appflow/latest/userguide/infor-nexus.md")                                                                    | External SaaS platform | Tabular                  |
| [Instagram Ads](../../../appflow/latest/userguide/connectors-instagram-ads.md "../../../appflow/latest/userguide/connectors-instagram-ads.md")                                        | External SaaS platform | Tabular                  |
| [Jira Cloud](../../../appflow/latest/userguide/connectors-jira-cloud.md "../../../appflow/latest/userguide/connectors-jira-cloud.md")                                                 | External SaaS platform | Tabular                  |
| [LinkedIn Ads](../../../appflow/latest/userguide/connectors-linkedin-ads.md "../../../appflow/latest/userguide/connectors-linkedin-ads.md")                                           | External SaaS platform | Tabular                  |
| [LinkedIn Ads](../../../appflow/latest/userguide/connectors-linkedin-ads.md "../../../appflow/latest/userguide/connectors-linkedin-ads.md")                                           | External SaaS platform | Tabular                  |
| [Mailchimp](../../../appflow/latest/userguide/connectors-mailchimp.md "../../../appflow/latest/userguide/connectors-mailchimp.md")                                                    | External SaaS platform | Tabular                  |
| [Marketo](../../../appflow/latest/userguide/marketo.md "../../../appflow/latest/userguide/marketo.md")                                                                                | External SaaS platform | Tabular                  |
| [Microsoft Teams](../../../appflow/latest/userguide/connectors-microsoft-teams.md "../../../appflow/latest/userguide/connectors-microsoft-teams.md")                                  | External SaaS platform | Tabular                  |
| [Mixpanel](../../../appflow/latest/userguide/connectors-mixpanel.md "../../../appflow/latest/userguide/connectors-mixpanel.md")                                                       | External SaaS platform | Tabular                  |
| [Okta](../../../appflow/latest/userguide/connectors-okta.md "../../../appflow/latest/userguide/connectors-okta.md")                                                                   | External SaaS platform | Tabular                  |
| [Salesforce](../../../appflow/latest/userguide/salesforce.md "../../../appflow/latest/userguide/salesforce.md")                                                                       | External SaaS platform | Tabular                  |
| [Salesforce Marketing Cloud](../../../appflow/latest/userguide/connectors-salesforce-marketing-cloud.md "../../../appflow/latest/userguide/connectors-salesforce-marketing-cloud.md") | External SaaS platform | Tabular                  |
| [Salesforce Pardot](../../../appflow/latest/userguide/pardot.md "../../../appflow/latest/userguide/pardot.md")                                                                        | External SaaS platform | Tabular                  |
| [SAP OData](../../../appflow/latest/userguide/sapodata.md "../../../appflow/latest/userguide/sapodata.md")                                                                            | External SaaS platform | Tabular                  |
| [SendGrid](../../../appflow/latest/userguide/connectors-sendgrid.md "../../../appflow/latest/userguide/connectors-sendgrid.md")                                                       | External SaaS platform | Tabular                  |
| [ServiceNow](../../../appflow/latest/userguide/servicenow.md "../../../appflow/latest/userguide/servicenow.md")                                                                       | External SaaS platform | Tabular                  |
| [Singular](../../../appflow/latest/userguide/singular.md "../../../appflow/latest/userguide/singular.md")                                                                             | External SaaS platform | Tabular                  |
| [Slack](../../../appflow/latest/userguide/slack.md "../../../appflow/latest/userguide/slack.md")                                                                                      | External SaaS platform | Tabular                  |
| [Stripe](../../../appflow/latest/userguide/connectors-stripe.md "../../../appflow/latest/userguide/connectors-stripe.md")                                                             | External SaaS platform | Tabular                  |
| [Trend Micro](../../../appflow/latest/userguide/trend-micro.md "../../../appflow/latest/userguide/trend-micro.md")                                                                    | External SaaS platform | Tabular                  |
| [Typeform](../../../appflow/latest/userguide/connectors-typeform.md "../../../appflow/latest/userguide/connectors-typeform.md")                                                       | External SaaS platform | Tabular                  |
| [Veeva](../../../appflow/latest/userguide/veeva.md "../../../appflow/latest/userguide/veeva.md")                                                                                      | External SaaS platform | Tabular                  |
| [Zendesk](../../../appflow/latest/userguide/zendesk.md "../../../appflow/latest/userguide/zendesk.md")                                                                                | External SaaS platform | Tabular                  |
| [Zendesk Chat](../../../appflow/latest/userguide/connectors-zendesk-chat.md "../../../appflow/latest/userguide/connectors-zendesk-chat.md")                                           | External SaaS platform | Tabular                  |
| [Zendesk Sell](../../../appflow/latest/userguide/connectors-zendesk-sell.md "../../../appflow/latest/userguide/connectors-zendesk-sell.md")                                           | External SaaS platform | Tabular                  |
| [Zendesk Sunshine](../../../appflow/latest/userguide/connectors-zendesk-sunshine.md "../../../appflow/latest/userguide/connectors-zendesk-sunshine.md")                               | External SaaS platform | Tabular                  |
| [Zoom Meetings](../../../appflow/latest/userguide/connectors-zoom.md "../../../appflow/latest/userguide/connectors-zoom.md")                                                          | External SaaS platform | Tabular                  |

For instructions on how to import data and information regarding input data requirements, such as
the maximum file size for images, see [Create a dataset](canvas-import-dataset.md "canvas-import-dataset.md").

Canvas also provides several sample datasets in your application to help you get started.
To learn more about the SageMaker AI-provided sample datasets you can experiment with, see
[Use sample datasets](canvas-sample-datasets.md "canvas-sample-datasets.md").

After you import a dataset into Canvas, you can update the dataset at any time. You can do a
manual update or you can set up a schedule for automatic dataset updates. For more information, see
[Update a dataset](canvas-update-dataset.md "canvas-update-dataset.md").

For more information specific to each dataset type, see the following sections:

**Tabular**

To import data from an external data source (such as a Snowflake database or a SaaS platform), you must
authenticate and connect to the data source in the Canvas application. For more information, see
[Connect to data sources](canvas-connecting-external.md "canvas-connecting-external.md").

If you want to import datasets larger than 5 GB from Amazon S3 into Canvas, you can achieve
faster sampling by using Amazon Athena to query and sample the data from Amazon S3.

After creating datasets in Canvas, you can prepare and transform your data using the
data preparation functionality of Data Wrangler. You can use Data Wrangler to handle missing values, transform your features,
join multiple datasets into a single dataset, and more. For more information, see
[Data preparation](canvas-data-prep.md "canvas-data-prep.md").

###### Tip

As long as your data is arranged into tables, you can join datasets from various sources, such
as Amazon Redshift, Amazon Athena, or Snowflake.

**Image**

For information about how to edit an image dataset and perform tasks such as assigning or reassigning
labels, adding images, or deleting images, see [Edit an image dataset](canvas-edit-image.md "canvas-edit-image.md").
