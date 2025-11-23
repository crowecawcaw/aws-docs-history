# How Amazon SageMaker AI uses AWS Secrets Manager

SageMaker AI is a fully managed machine learning service. With SageMaker AI, data scientists and
developers can quickly and easily build and train machine learning models, and then
directly deploy them into a production-ready hosted environment. It provides an
integrated Jupyter authoring notebook instance for easy access to your data sources for
exploration and analysis, so you don't have to manage servers.

You can associate Git repositories with your Jupyter notebook instances to save your
notebooks in a source control environment that persists even if you stop or delete your
notebook instance. You can manage your private repositories credentials using Secrets Manager. For
more information, see [Associate Git Repositories with Amazon
SageMaker Notebook Instances](../../../sagemaker/latest/dg/nbi-git-repo.md "../../../sagemaker/latest/dg/nbi-git-repo.md") in the
_Amazon SageMaker AI Developer Guide_.

To import data from Databricks, Data Wrangler stores your JDBC URL in Secrets Manager. For more
information, see [Import
data from Databricks (JDBC)](../../../sagemaker/latest/dg/data-wrangler-import.md#data-wrangler-databricks "../../../sagemaker/latest/dg/data-wrangler-import.md#data-wrangler-databricks").

To import data from Snowflake, Data Wrangler stores your credentials in a Secrets Manager
secret. For more information, see [Import
data from Snowflake](../../../sagemaker/latest/dg/data-wrangler-import.md#data-wrangler-snowflake "../../../sagemaker/latest/dg/data-wrangler-import.md#data-wrangler-snowflake").
