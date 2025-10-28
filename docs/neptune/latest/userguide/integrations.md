# Working with other AWS services

You can use Amazon Neptune in conjunction with many other AWS services:

###### Neptune integrations with other services

- **[AWS Glue](../../../glue/latest/dg.md "../../../glue/latest/dg.md")**   –  
  AWS Glue is a serverless data integration service that helps you perform extract,
  transform, and load (ETL) jobs on data.

Neptune provides an open-source library, [neptune-python-utilities](https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils "https://github.com/awslabs/amazon-neptune-tools/tree/master/neptune-python-utils"),
that simplifies using Python and Gremlin within a Glue job. The [Neo4j Spark Connector](https://neo4j.com/docs/spark/current/ "https://neo4j.com/docs/spark/current/") is also supported
for running Scala and openCypher Glue jobs.

- **[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ "https://aws.amazon.com/sagemaker/")**   –  
  Amazon SageMaker AI is a full-featured machine learning platform for building, training, and
  deploying high-quality machine learning models.

Neptune integrates with SageMaker AI in two primary ways:

    + Neptune provides an open-source Python package for [Jupyter
     notebooks](https://jupyter-notebook.readthedocs.io/en/stable/ "https://jupyter-notebook.readthedocs.io/en/stable/") which can be found in the [Neptune
     graph notebook project](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook") on GitHub. This package contains a set of Jupyter magics,
     tutorial notebooks, and code samples that provide in an interactive coding environment
     where you can learn about graph technology and Neptune. Neptune provides a fully
     managed environment for Jupyter notebooks hosted by SageMaker AI, and automatically links to
     the notebooks in the open-source [Neptune
     graph notebook project](https://github.com/aws/graph-notebook "https://github.com/aws/graph-notebook").
    + The Neptune ML feature makes it possible to build and train useful
     machine learning models on large graphs in hours instead of weeks. To accomplish this,
     Neptune ML uses graph neural network (GNN) technology powered by Amazon SageMaker AI and the
     [Deep Graph Library (DGL)](https://www.dgl.ai/ "https://www.dgl.ai/").

- **[AWS Lambda](../../../lambda/latest/dg.md "../../../lambda/latest/dg.md")**   –  
  AWS Lambda functions have many uses in Neptune applications.

For information about how to use Lambda functions with any of the popular
Gremlin drivers and language variants, as well as specific examples of Lambda
functions written in Java, JavaScript, and Python, see [Using AWS Lambda functions in Amazon Neptune](lambda-functions.md "lambda-functions.md").

- **[Amazon Athena](../../../athena/latest/ug.md "../../../athena/latest/ug.md")**   –  
  Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon Simple Storage Service
  and other federated data sources using standard SQL.

Neptune provides a [connector
to Athena](../../../athena/latest/ug/connectors-neptune.md "../../../athena/latest/ug/connectors-neptune.md") that enables Athena to communicate with your data stored in Neptune.

- **[AWS Database Migration Service (AWS DMS)](../../../dms/latest/userguide.md "../../../dms/latest/userguide.md")**   –  
  AWS Database Migration Service is an AWS web service you can use to migrate data from one database to another.

AWS DMS can [load data into Neptune](dms-neptune.md "dms-neptune.md") from [supported source
databases](../../../dms/latest/userguide/CHAP_Source.md "../../../dms/latest/userguide/CHAP_Source.md") quickly and securely. The source database remains fully operational
during the migration, minimizing downtime for applications that rely on it.

- **[AWS Backup](../../../aws-backup/latest/devguide.md "../../../aws-backup/latest/devguide.md")**   –  
  AWS Backup is a fully managed backup service that makes it easy to centralize and
  automate the backup of data across AWS services in the cloud as well as on premises.

AWS Backup lets you to create automated periodic snapshots of Neptune clusters
using your centralized data protection policy across the supported AWS services for
database, storage, and compute.

- **[AWS SDK for pandas](https://github.com/aws/aws-sdk-pandas "https://github.com/aws/aws-sdk-pandas")**   –  
  The AWS SDK for pandas (previously known as AWS Data Wrangler, or `awswrangler`), is
  an [AWS Professional Service](https://aws.amazon.com/professional-services "https://aws.amazon.com/professional-services")
  open-source python initiative that extends the power of the `pandas` Python data analysis
  library to AWS, connecting `DataFrames` and more than 30 AWS data-related services,
  including Neptune.

In addition to the SDK, there is also a [tutorial](https://aws-sdk-pandas.readthedocs.io/en/latest/tutorials/033%20-%20Amazon%20Neptune.html "https://aws-sdk-pandas.readthedocs.io/en/latest/tutorials/033%20-%20Amazon%20Neptune.html") about how to use it with Neptune, and several sample Neptune notebooks, namely [Fraud Ring Detection](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/00-Identifying-Fraud-Rings-Using-Social-Network-Analytics.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/00-Identifying-Fraud-Rings-Using-Social-Network-Analytics.ipynb"), [Synthetic Identity Detection](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/01-Identifying-1st-Person-Synthetic-Identity-Fraud-Using-Graph-Similarity.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/01-Identifying-1st-Person-Synthetic-Identity-Fraud-Using-Graph-Similarity.ipynb"), and [Logistics Analysis](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/02-Logistics-Analysis-using-a-Transportation-Network.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/05-Data-Science/02-Logistics-Analysis-using-a-Transportation-Network.ipynb").

- **[JDBC Driver](https://github.com/aws/amazon-neptune-jdbc-driver "https://github.com/aws/amazon-neptune-jdbc-driver")**   –  
  The Neptune JDBC driver supports openCypher, Gremlin, SQL-Gremlin, and SPARQL queries.

JDBC connectivity makes it easy to connect to Neptune with business intelligence
(BI) tools such as [Tableau](https://www.tableau.com/ "https://www.tableau.com/").
