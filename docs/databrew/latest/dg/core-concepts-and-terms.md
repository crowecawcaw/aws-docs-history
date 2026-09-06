

# Core concepts and terms in AWS Glue DataBrew
<a name="core-concepts-and-terms"></a>

Following, you can find an overview of the core concepts and terminology in AWS Glue DataBrew. After you read this section, see [Getting started with AWS Glue DataBrew](getting-started.md), which walks you through the process of creating projects and connecting datasets and running jobs.

**Topics**
+ [Project](#projects-concept)
+ [Dataset](#datasets-concept)
+ [Recipe](#recipes-concept)
+ [Job](#jobs-concept)
+ [Data lineage](#data-lineage-concept)
+ [Data profile](#data-profile-concept)

## Project
<a name="projects-concept"></a>

The interactive data preparation workspace in DataBrew is called a *project*. Using a data project, you manage a collection of related items: data, transformations, and scheduled processes. As part of creating a project, you choose or create a dataset to work on. Next, you create a *recipe*, which is a set of instructions or steps that you want DataBrew to act on. These actions transform your raw data into a form that is ready to be consumed by your data pipeline.

## Dataset
<a name="datasets-concept"></a>

Dataset simply means a set of data—rows or records that are divided into columns or fields. When you create a DataBrew project, you connect to or upload data that you want to transform or prepare. DataBrew can work with data from any source, imported from formatted files, and it connects directly to a growing list of data stores. 

For DataBrew, a *dataset* is a read-only connection to your data. DataBrew collects a set of descriptive metadata to refer to the data. No actual data can be altered or stored by DataBrew. For simplicity, we use dataset to refer to both the actual dataset and the metadata DataBrew uses. 

## Recipe
<a name="recipes-concept"></a>

In DataBrew, a *recipe* is a set of instructions or steps for data that you want DataBrew to act on. A recipe can contain many steps, and each step can contain many actions. You use the transformation tools on the toolbar to set up all the changes that you want to make to your data. Later, when you're ready to see the finished product of your recipe, you assign this job to DataBrew and schedule it. DataBrew stores the instructions about the data transformation, but it doesn't store any of your actual data. You can download and reuse recipes in other projects. You can also publish multiple versions of a recipe.

## Job
<a name="jobs-concept"></a>

DataBrew takes on the job of transforming your data by running the instructions that you set up when you made a recipe. The process of running these instructions is called a *job.* A job can put your data recipes into action according to a preset schedule. But you aren't confined to a schedule. You can also run jobs on demand. If you want to profile some data, you don't need a recipe. In that case, you can just set up a profile job to create a data profile. 

## Data lineage
<a name="data-lineage-concept"></a>

DataBrew tracks your data in a visual interface to determine its origin, called a *data lineage*. This view shows you how the data flows through different entities from where it originally came. You can see its origin, other entities it was influenced by, what happened to it over time, and where it was stored. 

## Data profile
<a name="data-profile-concept"></a>

When you profile your data, DataBrew creates a report called a *data profile*. This summary tells you about the existing shape of your data, including the context of the content, the structure of the data, and its relationships. You can make a data profile for any dataset by running a data profile job. 