# Visual ETL

Data engineers, analysts, and scientists use visual ETL features to create extract,
transform, and load (ETL) flows using an intuitive visual interface. With visual ETL, analytics
users can discover, prepare, move, and integrate data from multiple sources. This simplifies the
process of data manipulation and integration so that you can prepare data for analysis and
reporting.

Visual ETL in Amazon SageMaker Unified Studio provides a drag-and-drop interface for building ETL flows and
authoring flows with Amazon Q. You can connect to data sources, apply transformations, and define
target destinations without writing complex code.

You can use Visual ETL to implement solutions such as:

- Data integration from multiple sources
- Data cleansing and normalization
- Creating data warehouses or data lakes
- Preparing data for machine learning models
- Automating regular data processing tasks
  Authoring flows with Visual ETL utilizes AWS Glue interactive sessions Version
  5.0.

Amazon SageMaker Unified Studio supports Visual ETL in two domain types:

- **IAM-based domains** - New domain type where customers log
  into Amazon SageMaker Unified Studio using federated roles and existing IAM permissions apply when using
  Amazon SageMaker Unified Studio IAM-based domains. Provides access to a new Amazon SageMaker Unified Studio interface.
- **Identity Center-based domains** - Original Amazon SageMaker Unified Studio
  interface and user experience that continues to be supported and maintained.
  While workflows are similar across both domain types, the steps to complete actions differ
  between the two interfaces. Choose the appropriate section below based on your domain
  type.

###### Topics

- [Supported connectors for Visual ETL](connectors-visual-etl.md "connectors-visual-etl.md")
- [Supported transforms for
  Visual ETL](visual-etl-supported-transforms.md "visual-etl-supported-transforms.md")
- [Visual ETL for IAM-based domains](visual-etl-iam-domains.md "visual-etl-iam-domains.md")
- [Visual ETL for Identity Center-based
  domains](visual-etl-identity-center-domains.md "visual-etl-identity-center-domains.md")
