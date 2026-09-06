

# Data import
<a name="canvas-importing-data"></a>

Amazon SageMaker Canvas supports importing tabular, image, and document data. You can import datasets from your local machine, Amazon services such as Amazon S3 and Amazon Redshift, and external data sources. When importing datasets from Amazon S3, you can bring a dataset of any size. Use the datasets that you import to build models and make predictions for other datasets.

Each use case for which you can build a custom model accepts different types of input. For example, if you want to build a single-label image classification model, then you should import image data. For more information about the different model types and the data they accept, see [How custom models work](canvas-build-model.md). You can import data and build custom models in SageMaker Canvas for the following data types:
+ **Tabular** (CSV, Parquet, or tables)
  + Categorical – Use categorical data to build custom categorical prediction models for 2 and 3\+ category prediction.
  + Numeric – Use numeric data to build custom numeric prediction models.
  + Text – Use text data to build custom multi-category text prediction models.
  + Timeseries – Use timeseries data to build custom time series forecasting models.
+ **Image** (JPG or PNG) – Use image data to build custom single-label image prediction models.
+ **Document** (PDF, JPG, PNG, TIFF) – Document data is only supported for SageMaker Canvas Ready-to-use models. To learn more about Ready-to-use models that can make predictions for document data, see [Ready-to-use models](canvas-ready-to-use-models.md).

You can import data into Canvas from the following data sources:
+ Local files on your computer
+ Amazon S3 buckets
+ Amazon Redshift provisioned clusters (not Amazon Redshift Serverless)
+ AWS Glue Data Catalog through Amazon Athena
+ Amazon Aurora
+ Amazon Relational Database Service (Amazon RDS)
+ Salesforce Data Cloud
+ Snowflake
+ Databricks, SQLServer, MariaDB, and other popular databases through JDBC connectors
+ Over 40 external SaaS platforms, such as SAP OData

For a full list of data sources from which you can import, see the following table:


| Source | Type | Supported data types | 
| --- | --- | --- | 
| Local file upload | Local | Tabular, Image, Document | 
| Amazon Aurora | Amazon internal | Tabular | 
| Amazon S3 bucket | Amazon internal | Tabular, Image, Document | 
| Amazon RDS | Amazon internal | Tabular | 
| Amazon Redshift provisioned clusters (not Redshift Serverless) | Amazon internal | Tabular | 
| AWS Glue Data Catalog (through Amazon Athena) | Amazon internal | Tabular | 
| [Databricks](https://www.databricks.com/) | External | Tabular | 
| Snowflake | External | Tabular | 
| [Salesforce Data Cloud](https://www.salesforce.com/products/genie/overview/) | External | Tabular | 
| SQLServer | External | Tabular | 
| MySQL | External | Tabular | 
| PostgreSQL | External | Tabular | 
| MariaDB | External | Tabular | 
| [Amplitude](https://docs.aws.amazon.com/appflow/latest/userguide/amplitude.html) | External SaaS platform | Tabular | 
| [CircleCI](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-circleci.html) | External SaaS platform | Tabular | 
| [DocuSign Monitor](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-docusign-monitor.html) | External SaaS platform | Tabular | 
| [Domo](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-domo.html) | External SaaS platform | Tabular | 
| [Datadog](https://docs.aws.amazon.com/appflow/latest/userguide/datadog.html) | External SaaS platform | Tabular | 
| [Dynatrace](https://docs.aws.amazon.com/appflow/latest/userguide/dynatrace.html) | External SaaS platform | Tabular | 
| [Facebook Ads](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-facebook-ads.html) | External SaaS platform | Tabular | 
| [Facebook Page Insights](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-facebook-page-insights.html) | External SaaS platform | Tabular | 
| [Google Ads](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-google-ads.html) | External SaaS platform | Tabular | 
| [Google Analytics 4](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-google-analytics-4.html) | External SaaS platform | Tabular | 
| [Google Search Console](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-google-search-console.html) | External SaaS platform | Tabular | 
| [GitHub](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-github.html) | External SaaS platform | Tabular | 
| [GitLab](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-gitlab.html) | External SaaS platform | Tabular | 
| [Infor Nexus](https://docs.aws.amazon.com/appflow/latest/userguide/infor-nexus.html) | External SaaS platform | Tabular | 
| [Instagram Ads](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-instagram-ads.html) | External SaaS platform | Tabular | 
| [Jira Cloud](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-jira-cloud.html) | External SaaS platform | Tabular | 
| [LinkedIn Ads](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-linkedin-ads.html) | External SaaS platform | Tabular | 
| [LinkedIn Ads](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-linkedin-ads.html) | External SaaS platform | Tabular | 
| [Mailchimp](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-mailchimp.html) | External SaaS platform | Tabular | 
| [Marketo](https://docs.aws.amazon.com/appflow/latest/userguide/marketo.html) | External SaaS platform | Tabular | 
| [Microsoft Teams](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-microsoft-teams.html) | External SaaS platform | Tabular | 
| [Mixpanel](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-mixpanel.html) | External SaaS platform | Tabular | 
| [Okta](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-okta.html) | External SaaS platform | Tabular | 
| [Salesforce](https://docs.aws.amazon.com/appflow/latest/userguide/salesforce.html) | External SaaS platform | Tabular | 
| [Salesforce Marketing Cloud](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-salesforce-marketing-cloud.html) | External SaaS platform | Tabular | 
| [Salesforce Pardot](https://docs.aws.amazon.com/appflow/latest/userguide/pardot.html) | External SaaS platform | Tabular | 
| [SAP OData](https://docs.aws.amazon.com/appflow/latest/userguide/sapodata.html) | External SaaS platform | Tabular | 
| [SendGrid](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-sendgrid.html) | External SaaS platform | Tabular | 
| [ServiceNow](https://docs.aws.amazon.com/appflow/latest/userguide/servicenow.html) | External SaaS platform | Tabular | 
| [Singular](https://docs.aws.amazon.com/appflow/latest/userguide/singular.html) | External SaaS platform | Tabular | 
| [Slack](https://docs.aws.amazon.com/appflow/latest/userguide/slack.html) | External SaaS platform | Tabular | 
| [Stripe](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-stripe.html) | External SaaS platform | Tabular | 
| [Trend Micro](https://docs.aws.amazon.com/appflow/latest/userguide/trend-micro.html) | External SaaS platform | Tabular | 
| [Typeform](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-typeform.html) | External SaaS platform | Tabular | 
| [Veeva](https://docs.aws.amazon.com/appflow/latest/userguide/veeva.html) | External SaaS platform | Tabular | 
| [Zendesk](https://docs.aws.amazon.com/appflow/latest/userguide/zendesk.html) | External SaaS platform | Tabular | 
| [Zendesk Chat](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-zendesk-chat.html) | External SaaS platform | Tabular | 
| [Zendesk Sell](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-zendesk-sell.html) | External SaaS platform | Tabular | 
| [Zendesk Sunshine](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-zendesk-sunshine.html) | External SaaS platform | Tabular | 
| [Zoom Meetings](https://docs.aws.amazon.com/appflow/latest/userguide/connectors-zoom.html) | External SaaS platform | Tabular | 

For instructions on how to import data and information regarding input data requirements, such as the maximum file size for images, see [Create a dataset](canvas-import-dataset.md).

Canvas also provides several sample datasets in your application to help you get started. To learn more about the SageMaker AI-provided sample datasets you can experiment with, see [Use sample datasets](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-sample-datasets.html).

After you import a dataset into Canvas, you can update the dataset at any time. You can do a manual update or you can set up a schedule for automatic dataset updates. For more information, see [Update a dataset](canvas-update-dataset.md).

For more information specific to each dataset type, see the following sections:

**Tabular**

To import data from an external data source (such as a Snowflake database or a SaaS platform), you must authenticate and connect to the data source in the Canvas application. For more information, see [Connect to data sources](canvas-connecting-external.md).

If you want to import datasets larger than 5 GB from Amazon S3 into Canvas, you can achieve faster sampling by using Amazon Athena to query and sample the data from Amazon S3.

After creating datasets in Canvas, you can prepare and transform your data using the data preparation functionality of Data Wrangler. You can use Data Wrangler to handle missing values, transform your features, join multiple datasets into a single dataset, and more. For more information, see [Data preparation](canvas-data-prep.md).

**Tip**  
As long as your data is arranged into tables, you can join datasets from various sources, such as Amazon Redshift, Amazon Athena, or Snowflake.

**Image**

For information about how to edit an image dataset and perform tasks such as assigning or reassigning labels, adding images, or deleting images, see [Edit an image dataset](canvas-edit-image.md).