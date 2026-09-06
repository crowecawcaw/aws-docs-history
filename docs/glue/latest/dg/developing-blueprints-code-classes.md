

# AWS Glue blueprint classes reference
<a name="developing-blueprints-code-classes"></a>

The libraries for AWS Glue blueprints define three classes that you use in your workflow layout script: `Job`, `Crawler`, and `Workflow`.

**Topics**
+ [Job class](#developing-blueprints-code-jobclass)
+ [Crawler class](#developing-blueprints-code-crawlerclass)
+ [Workflow class](#developing-blueprints-code-workflowclass)
+ [Class methods](#developing-blueprints-code-methods)

## Job class
<a name="developing-blueprints-code-jobclass"></a>

The `Job` class represents an AWS Glue ETL job.

**Mandatory constructor arguments**  
The following are mandatory constructor arguments for the `Job` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| Name | str | Name to assign to the job. AWS Glue adds a randomly generated suffix to the name to distinguish the job from those created by other blueprint runs. | 
| Role | str | Amazon Resource Name (ARN) of the role that the job should assume while executing. | 
| Command | dict | Job command, as specified in the [JobCommand structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-JobCommand) in the API documentation.  | 

**Optional constructor arguments**  
The following are optional constructor arguments for the `Job` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| DependsOn | dict | List of workflow entities that the job depends on. For more information, see [Using the DependsOn argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on). | 
| WaitForDependencies | str | Indicates whether the job should wait until all entities on which it depends complete before executing or until any completes. For more information, see [Using the WaitForDependencies argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies). Omit if the job depends on only one entity. | 
| (Job properties) | - | Any of the job properties listed in [Job structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job) in the AWS Glue API documentation (except CreatedOn and LastModifiedOn). | 

## Crawler class
<a name="developing-blueprints-code-crawlerclass"></a>

The `Crawler` class represents an AWS Glue crawler.

**Mandatory constructor arguments**  
The following are mandatory constructor arguments for the `Crawler` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| Name | str | Name to assign to the crawler. AWS Glue adds a randomly generated suffix to the name to distinguish the crawler from those created by other blueprint runs. | 
| Role | str | ARN of the role that the crawler should assume while running. | 
| Targets | dict | Collection of targets to crawl. Targets class constructor arguments are defined in the [CrawlerTargets structure](aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-CrawlerTargets) in the API documentation. All Targets constructor arguments are optional, but you must pass at least one.  | 

**Optional constructor arguments**  
The following are optional constructor arguments for the `Crawler` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| DependsOn | dict | List of workflow entities that the crawler depends on. For more information, see [Using the DependsOn argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on). | 
| WaitForDependencies | str | Indicates whether the crawler should wait until all entities on which it depends complete before running or until any completes. For more information, see [Using the WaitForDependencies argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies). Omit if the crawler depends on only one entity. | 
| (Crawler properties) | - | Any of the crawler properties listed in [Crawler structure](aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-Crawler) in the AWS Glue API documentation, with the following exceptions:+  `State` <br />+  `CrawlElapsedTime` <br />+  `CreationTime` <br />+  `LastUpdated` <br />+  `LastCrawl` <br />+  `Version`  | 

## Workflow class
<a name="developing-blueprints-code-workflowclass"></a>

The `Workflow` class represents an AWS Glue workflow. The workflow layout script returns a `Workflow` object. AWS Glue creates a workflow based on this object.

**Mandatory constructor arguments**  
The following are mandatory constructor arguments for the `Workflow` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| Name | str | Name to assign to the workflow. | 
| Entities | Entities | A collection of entities (jobs and crawlers) to include in the workflow. The Entities class constructor accepts a Jobs argument, which is a list of Job objects, and a Crawlers argument, which is a list of Crawler objects. | 

**Optional constructor arguments**  
The following are optional constructor arguments for the `Workflow` class.


| Argument name | Type | Description | 
| --- | --- | --- | 
| Description | str | See [Workflow structure](aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow). | 
| DefaultRunProperties | dict | See [Workflow structure](aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow). | 
| OnSchedule | str | A cron expression. | 

## Class methods
<a name="developing-blueprints-code-methods"></a>

All three classes include the following methods.

**validate()**  
Validates the properties of the object and if errors are found, outputs a message and exits. Generates no output if there are no errors. For the `Workflow` class, calls itself on every entity in the workflow.

**to\_json()**  
Serializes the object to JSON. Also calls `validate()`. For the `Workflow` class, the JSON object includes job and crawler lists, and a list of triggers generated by the job and crawler dependency specifications.