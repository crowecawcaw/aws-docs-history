# Compute

On a project's **Compute** page in Amazon SageMaker Unified Studio, you can view compute
information and add compute resources such as Amazon Redshift and Amazon EMR
Serverless clusters to your project. Amazon SageMaker Unified Studio supports different kinds of compute
resources:

- **Data warehouse**: This includes
  Amazon Redshift Serverless workgroups and Amazon Redshift provisioned
  clusters. Workgroups are a collection of compute resources that you can use to run data
  warehousing queries and engineering notebooks without managing underlying infrastructure.
  Clusters are scalable compute environments that enable the processing and analysis of large
  datasets. For more information, see [Amazon Redshift compute connections in Amazon SageMaker Unified Studio](compute-redshift.md "compute-redshift.md").
- **Data processing**: This includes connections to Amazon EMR on EC2
  clusters, Amazon EMR on EKS virtual clusters, Amazon EMR Serverless
  applications, and
  Glue ETL computes. For more information, see
  the following
  links:
  - [Amazon EMR on EC2 connections in Amazon SageMaker Unified Studio](managing-emr-on-ec2.md "managing-emr-on-ec2.md")
  - [Amazon EMR on EKS in Amazon SageMaker Unified Studio](managing-emr-on-eks.md "managing-emr-on-eks.md")
  - [EMR Serverless compute connections in Amazon SageMaker Unified Studio](adding-deleting-emr-serverless.md "adding-deleting-emr-serverless.md")
  - [Glue ETL in Amazon SageMaker Unified Studio](compute-glue-etl.md "compute-glue-etl.md")

- **HyperPod clusters**: In Amazon SageMaker Unified Studio,
  you can launch machine learning workloads on Amazon SageMaker AI HyperPod clusters.
  For more information, see [HyperPod clusters](sagemaker-hyperpods.md "sagemaker-hyperpods.md").
- **Spaces**: Spaces are used to manage the storage and resource
  needs of applications running on JupyterLab. On the **Spaces** tab of the
  **Compute** page, you can view information about your JupyterLab
  environment in Amazon SageMaker Unified Studio, such as the EBS volume and the status of the
  IDE. For more information about spaces, see [IDE spaces in Amazon SageMaker Unified Studio](ide-spaces.md "ide-spaces.md").
- **MLflow tracking servers**: MLflow tracking servers make it
  possible to use MLflow in Amazon SageMaker Unified Studio to create, manage, analyze, and compare machine learning
  experiments. For more information, see [Track experiments using MLflow](sagemaker-experiments.md "sagemaker-experiments.md").
- **Workflow environments**: Use a workflow environment to share
  scheduled workflows with other project
  members. For more
  information, see [Create a workflow environment](create-workflow-environment.md "create-workflow-environment.md").

###### Note

Adding a serverless or cluster compute connection adds the compute resource to the project space, so all project members can access it.
