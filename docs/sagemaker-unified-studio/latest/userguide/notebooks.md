# Notebooks

## Overview

Notebooks in Amazon SageMaker Unified Studio provide an interactive environment for data analysis,
exploration, engineering, and machine learning workflows. You can run SQL, Python, and natural
language queries to discover, transform, analyze, visualize, and share insights on data at
scale.

You can use notebooks in both IAM-based and IAM Identity Center-based domains.

Amazon SageMaker Unified Studio offers multiple coding experiences to meet different development preferences
and use cases. JupyterLab IDE provides a traditional Jupyter notebook environment with
extensive customization options and plugin support. Code Editor, based on [Code-OSS, Visual Studio Code - Open Source](https://github.com/microsoft/vscode#visual-studio-code---open-source-code---oss "https://github.com/microsoft/vscode#visual-studio-code---open-source-code---oss"), helps you write, test, debug, and run
your analytics and machine learning code. Code Editor extends and is fully integrated with
Amazon SageMaker Unified Studio. The new notebook experience, documented in this guide, provides a streamlined,
AI-enhanced interface optimized for data analysis workflows with built-in visualization
capabilities and seamless integration with AWS data services.

Notebooks support multiple cell types including Python code cells, SQL code cells,
markdown cells, table cells, and chart cells. Each notebook runs on a managed compute
environment that you can configure based on your processing requirements. You can use spark
code to leverage [Amazon Athena for Apache
Spark](../../../athena/latest/ug/notebooks-spark.md "../../../athena/latest/ug/notebooks-spark.md"). Athena for Spark makes it easy to interactively run data analytics and
exploration using Apache Spark without the need to plan for, configure, or manage resources.
You can transition between local Python and remote Spark workloads from a single
notebook.

The notebook interface integrates with AI assistance through SageMaker Data Agent, the AI
agent that helps generate code, diagnose errors, and provide data analysis
recommendations.

###### Note

Amazon Athena for Apache Spark doesn't support Virtual Private Cloud (VPC). If you require VPC connectivity for your workloads, use Spark on Amazon EMR or AWS Glue instead. For instructions on disabling Amazon Athena Spark, see [Network isolation](../adminguide/network-isolation.md "../adminguide/network-isolation.md") in the _Amazon SageMaker Unified Studio Admin Guide_.

For more information about configuring VPC and network isolation for your domain, see [Network isolation](../adminguide/network-isolation.md "../adminguide/network-isolation.md") in the _Amazon SageMaker Unified Studio Admin Guide_.

## Key capabilities

- Execute Python, Spark, and SQL code in interactive cells
- Integrate with Amazon Athena for Apache Spark for distributed processing
- Connect to multiple data sources including Amazon Simple Storage Service, Amazon S3 Tables, AWS Glue Data
  Catalog, Amazon Athena, and Amazon Redshift. For a complete list of supported sources, see [Supported data connections](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported").
- Work with Apache Iceberg REST Catalogs to read and write Iceberg tables by using Iceberg REST APIs in Python and SQL
- Visualize data with interactive tables and charts
- Use auto code completion, formatting, and linting in the cell editor
- Use AI assistance for code generation and error diagnosis
- Manage compute environments with configurable instance types
- Export notebooks in multiple formats including Jupyter and Python files
- Install and manage Python packages
- Run notebook kernels in your domain-level VPC configuration for network isolation

## Roles and permissions

To use notebooks in Amazon SageMaker Unified Studio, you need:

- Access to an Amazon SageMaker Unified Studio domain
- Appropriate IAM permissions to access data sources
- Project membership with notebook creation permissions
