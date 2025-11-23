# Notebooks

## Overview

Notebooks in Amazon SageMaker Unified Studio provide an interactive environment for data analysis,
exploration, engineering, and machine learning workflows. You can run SQL, Python, and natural
language queries to discover, transform, analyze, visualize, and share insights on data at
scale.

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

SageMaker notebooks are only available in IAM-based domains.

## Key capabilities

1. Execute Python, Spark, and SQL code in interactive cells
2. Integrate with Amazon Athena for Apache Spark for distributed processing
3. Connect to multiple data sources including Amazon Simple Storage Service, Amazon S3 Tables, AWS Glue Data
   Catalog, Amazon Athena, and Amazon Redshift. List of supported sources can be found [here](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported").
4. Work with Apache Iceberg REST Catalogs located anywhere to read/write Iceberg tables
   using Iceberg REST APIs in Python/SQL.
5. Visualize data with interactive tables and charts
6. Auto code completion, formatting, linting supported in Cell editor
7. Use AI assistance for code generation and error diagnosis
8. Manage compute environments with configurable instance types
9. Export notebooks in multiple formats including Jupyter, and Python files
10. Install and manage Python packages

## Roles and permissions

To use notebooks in Amazon SageMaker Unified Studio, you need:

1. Access to an Amazon SageMaker Unified Studio domain
2. Appropriate IAM permissions to access data sources
3. Project membership with notebook creation permissions
