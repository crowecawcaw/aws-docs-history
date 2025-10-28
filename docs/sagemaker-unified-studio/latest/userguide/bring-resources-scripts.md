# Bringing existing resources into Amazon SageMaker Unified Studio

You can bring in existing resources to your Amazon SageMaker Unified Studio project
by using the **Data** and **Compute** pages in your project,
or by using scripts provided in GitHub.

Examples of resources you can bring into Amazon SageMaker Unified Studio are listed below.

## AWS Glue Data Catalogs

- A GitHub script for bringing this resource into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-gdc-assets "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-gdc-assets").

## Amazon S3 data

To bring your existing Amazon S3 data and use it in Amazon SageMaker Unified Studio,
follow the guide in the link below. This guide explains how you can configure permissions
and customize role assignments for Amazon SageMaker Unified Studio to
access your Amazon S3 data from a project.

- A GitHub script for bringing this resource into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-role "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-role").
- To add Amazon S3 connections using the Amazon SageMaker Unified Studio interface, see [Amazon S3 data in Amazon SageMaker Unified Studio](data-s3.md "data-s3.md").

## Amazon Athena workgroups and saved queries

- A GitHub script for bringing this resource into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/athena").

## Amazon EMR on EC2 clusters

- A GitHub script for bringing this resource into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/emr "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/emr").
- To bring in existing clusters using the Amazon SageMaker Unified Studio interface, see [Adding an existing Amazon EMR on EC2 cluster in Amazon SageMaker Unified Studio](adding-existing-emr-on-ec2-clusters.md "adding-existing-emr-on-ec2-clusters.md").

## Amazon Redshift clusters and Amazon Redshift Serverless workgroups

- To bring in existing Amazon Redshift clusters and workgroups using the Amazon SageMaker Unified Studio
  interface, see [Connecting to an existing Amazon Redshift resource](adding-a-existing-compute-connection.md "adding-a-existing-compute-connection.md").

## Amazon SageMaker AI resources

- Amazon SageMaker Studio users can bring their existing SageMaker AI domains, user profiles, and spaces into Amazon SageMaker Unified Studio.
  This integration also supports additional SageMaker AI resources such as training jobs, machine learning pipelines, models, inference endpoints, and more.
  A package of GitHub scripts for bringing Amazon SageMaker AI resources into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/sagemaker-ai "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/sagemaker-ai").

## AWS IAM roles

Use the utility script in GitHub to configure permissions and customize role assignments for Amazon SageMaker Unified Studio.

- A GitHub script for bringing this resource into Amazon SageMaker Unified Studio can be found
  [here](https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-role "https://github.com/aws/Unified-Studio-for-Amazon-Sagemaker/tree/main/migration/bring-your-own-role").

###### Note

Review the prerequisites carefully before proceeding to execute the script. Ensure that you save your work and that you do not have any running tasks or processes such as reconfiguring a JupyterLab space or creating a new compute resource.
These processes might get interrupted or cause the script to fail.
