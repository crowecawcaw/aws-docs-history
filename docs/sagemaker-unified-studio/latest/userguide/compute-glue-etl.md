# Glue ETL in Amazon SageMaker Unified Studio

AWS Glue ETL compute resources power Visual ETL flows in your Amazon SageMaker Unified Studio project.
You can use Glue ETL serverless compute resources to run Visual ETL flows
and JupyterLab notebooks without managing underlying infrastructure.
This is especially useful for analytics, machine learning, and application development.

You can view information about your AWS Glue ETL compute resources on the
**Data processing** tab of the **Compute** page in your project.
These resources are used when you create and run Visual ETL flows in Amazon SageMaker Unified Studio.

By default, when you create a project in Amazon SageMaker Unified Studio two Glue ETL compute connections are created.
The Glue ETL connection with permission mode set to compatibility is called `project.spark.compatibility`,
and the Glue ETL connection with permission mode set to fine-grained is called `project.spark.fineGrained`.
You can choose which compute option to use when you use tools such as Visual ETL and JupyterLab in Amazon SageMaker Unified Studio.
For more information about compatibility and fine-grained permission modes, see [Configuring permission mode for Glue ETL in Amazon SageMaker Unified Studio](compute-permissions-mode-glue.md "compute-permissions-mode-glue.md").

###### Note

Amazon SageMaker Unified Studio automatically creates Glue ETL compute resources during project creation.
You cannot create, edit, or delete these instances.
By default, Glue ETL uses AWS Glue 5.0 with G.1X (1 Data Processing Unit / Hour) worker types.
