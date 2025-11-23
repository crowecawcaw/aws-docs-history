# MLCOST03-BP02 Use no-code or low-code and code generation tools

for interactive analysis

Prepare data through data wrangler tools for interactive data
analysis and model building. The no-code/low-code, automation, and
visual capabilities improve productivity and reduce the cost for
interactive analysis. Integrate with generative AI code generation
tools.

**Desired outcome:** You will be able
to streamline your data preparation workflow using visual interfaces
with minimal coding required. By implementing no-code or low-code
tools like Amazon SageMaker AI Canvas and Data Wrangler, you reduce
time spent on data preprocessing tasks and gain improved insights
through interactive visualizations. Amazon Q integration provides
intelligent assistance for data preparation and code generation,
enabling faster iteration cycles on model development while
maintaining data quality and consistency across your machine
learning projects.

**Common anti-patterns:**

- Writing custom data preparation scripts for every analysis task.
- Using disjointed tools for data import, transformation, and
  visualization.
- Manually performing repetitive data cleaning operations.
- Creating non-reproducible data preparation workflows.

**Benefits of establishing this best
practice:**

- Reduced time and cost for data preparation and feature
  engineering.
- Improved productivity through visual interfaces and automation.
- Streamlined workflow from data import to model deployment.
- Support for code and no-code approaches to accommodate different
  skill levels.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data preparation is often cited as the most time-consuming aspect
of machine learning projects, typically consuming 60-80% of data
scientists' time. Data wrangler tools provide visual interfaces to
simplify and accelerate this process through automation and
low-code solutions.

Amazon SageMaker AI Data Wrangler offers an end-to-end solution for
data preparation that integrates directly with your machine
learning workflow. By using a visual interface, you can import
data from various sources, identify and fix data quality issues,
transform features, and generate insights—all with minimal coding
required. The tool provides transparency by generating code for
your transformations, fostering reproducibility and allowing
customization when needed.

Data wrangler tools are particularly valuable for exploratory data
analysis, where quick iteration and visualization are essential.
They allow you to rapidly identify patterns, outliers, and
relationships in your data, accelerating the feature engineering
process. With built-in data quality and insights features, you can
understand your data characteristics and address issues before
model training begins.

### Implementation steps

1. **Set up Amazon SageMaker AI Canvas or
   Studio environment**. Access SageMaker AI Canvas for a
   no-code experience or SageMaker AI Studio for more advanced
   capabilities through the AWS Management Console. Canvas
   provides a visual, drag-and-drop interface for business
   analysts and citizen data scientists, while Studio offers
   Data Wrangler for more technical users. Both environments
   support the complete machine learning workflow with varying
   levels of coding requirements.
2. **Import data from various
   sources**. Use SageMaker AI Canvas or Data Wrangler to
   connect to multiple data sources including Amazon S3, Amazon Athena, Amazon Redshift, Snowflake, and various databases.
   Canvas provides a simplified point-and-click interface for
   business users, while Data Wrangler offers more advanced
   data source connectivity options. Both tools avoid the need
   for custom connector code.
3. **Explore and visualize your
   data**. USe Data Wrangler's built-in data
   visualizations to understand distributions, correlations,
   and outliers. These visualizations assist to identify
   potential issues early and inform feature engineering
   decisions without writing complex plotting code.
4. **Use Amazon Q for generative
   AI-powered data preparation and code generation**.
   Use Amazon Q integrated within SageMaker AI Canvas and Data
   Wrangler to get natural language assistance for data
   preparation tasks, automated code generation, and
   intelligent suggestions for data transformations. Amazon Q
   can explain data patterns, suggest optimal preprocessing
   steps, and generate code snippets for custom
   transformations, significantly reducing the time needed for
   data preparation tasks. Additionally, use AI-powered
   development tools like Kiro for intelligent code generation
   and optimization of your data processing workflows.
5. **Apply transformations to prepare
   your data**. Use the visual transformation
   interface to clean and prepare data through operations like
   handling missing values, encoding categorical features,
   scaling numerical values, and feature extraction. Data
   Wrangler provides over 300 built-in transformations while
   allowing custom Python transformations when needed.
6. **Analyze data quality and generate
   insights**. Use the built-in data quality and
   insights features to detect anomalies, check for imbalanced
   data, and understand feature importance. These automated
   analyses identify potential issues before model training
   begins.
7. **Balance your datasets**.
   Address imbalanced datasets using built-in techniques like
   random oversampling, random undersampling, and synthetic
   minority oversampling (SMOTE). Data Wrangler provides visual
   controls to implement these techniques without specialized
   knowledge.
8. **Scale to larger datasets**.
   Process larger datasets by configuring instance types and
   using distributed processing capabilities. Data Wrangler
   supports processing wide datasets with thousands of columns
   and large datasets with billions of rows through appropriate
   resource allocation.
9. **Prepare time series data**.
   Use specialized time series transformations to handle
   temporal data, including resampling, lagged feature
   creation, and time-based aggregations. These operations
   simplify working with sequential data patterns.
10. **Export your data flow for
    production**. Deploy your data preparation workflow
    by exporting to various destinations including Amazon S3,
    SageMaker AI Feature Store, or directly to model building
    workflows. Data Wrangler generates Python code that can be
    integrated into production pipelines. Canvas workflows can
    also be exported to SageMaker AI notebooks for further
    customization and integration into production pipelines.
11. **Use enhanced Canvas
    capabilities**. Use SageMaker AI Canvas's improved
    natural language support and Q integration for
    conversational data analysis, enabling business users to
    perform complex data preparation tasks without technical
    expertise.
12. **Integrate with the broader machine
    learning workflow**. Connect your prepared data
    directly to SageMaker AI's model building capabilities like
    SageMaker AI Autopilot for automated model development or
    custom model training. This integration creates a seamless
    path from data to deployed models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md")
- [Get
  Started with Data Wrangler](../../../sagemaker/latest/dg/data-wrangler-getting-started.md "../../../sagemaker/latest/dg/data-wrangler-getting-started.md")
- [Prepare
  ML Data with Amazon SageMaker AI Data Wrangler](../../../sagemaker/latest/dg/data-wrangler.md "../../../sagemaker/latest/dg/data-wrangler.md")
- [What
  is Amazon Q Developer?](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md")
- [What
  is AWS Glue DataBrew?](../../../databrew/latest/dg/what-is.md "../../../databrew/latest/dg/what-is.md")
- [Create,
  store, and share features with Feature Store](../../../sagemaker/latest/dg/feature-store.md "../../../sagemaker/latest/dg/feature-store.md")
- [Accelerate
  data preparation with data quality and insights in Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/accelerate-data-preparation-with-data-quality-and-insights-in-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/accelerate-data-preparation-with-data-quality-and-insights-in-amazon-sagemaker-data-wrangler/")
- [Process
  larger and wider datasets with Amazon SageMaker AI Data
  Wrangler](https://aws.amazon.com/blogs/machine-learning/process-larger-and-wider-datasets-with-amazon-sagemaker-data-wrangler/ "https://aws.amazon.com/blogs/machine-learning/process-larger-and-wider-datasets-with-amazon-sagemaker-data-wrangler/")
- [Fuel
  Your Data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/ "https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/")

**Related examples:**

- [Prepare
  ML Data with Amazon SageMaker AI Data Wrangler](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/data-wrangler.md "https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/data-wrangler.md")
- [SageMaker AI
  Data Wrangler Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-datawrangler "https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-datawrangler")
