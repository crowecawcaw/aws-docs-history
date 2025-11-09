# AWS Glue blueprint classes

reference

The libraries for AWS Glue blueprints define three classes that you use in your workflow
layout script: `Job`, `Crawler`, and `Workflow`.

###### Topics

- [Job class](#developing-blueprints-code-jobclass "#developing-blueprints-code-jobclass")
- [Crawler class](#developing-blueprints-code-crawlerclass "#developing-blueprints-code-crawlerclass")
- [Workflow class](#developing-blueprints-code-workflowclass "#developing-blueprints-code-workflowclass")
- [Class methods](#developing-blueprints-code-methods "#developing-blueprints-code-methods")

## Job class

The `Job` class represents an AWS Glue ETL job.

###### Mandatory constructor arguments

The following are mandatory constructor arguments for the `Job` class.

| Argument name | Type   | Description                                                                                                                                                                                              |
| ------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`        | `str`  | Name to assign to the job. AWS Glue adds a randomly generated suffix to the name to<br>distinguish the job from those created by other blueprint runs.                                                   |
| `Role`        | `str`  | Amazon Resource Name (ARN) of the role that the job should assume while<br>executing.                                                                                                                    |
| `Command`     | `dict` | Job command, as specified in the [JobCommand structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-JobCommand "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-JobCommand") in the API documentation. |

###### Optional constructor arguments

The following are optional constructor arguments for the `Job` class.

| Argument name         | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DependsOn`           | `dict` | List of workflow entities that the job depends on. For more information, see<br>[Using the DependsOn<br>argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on "developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on").                                                                                                                                                                        |
| `WaitForDependencies` | `str`  | Indicates whether the job should wait until *all<br>• entities on<br>which it depends complete before executing or until *any\*<br>completes. For more information, see [Using the<br>WaitForDependencies argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies "developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies"). Omit if the job<br>depends on only one entity. |
| (Job properties)      | -      | Any of the job properties listed in [Job structure](aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job "aws-glue-api-jobs-job.md#aws-glue-api-jobs-job-Job")<br>in the AWS Glue API documentation (except `CreatedOn` and<br>`LastModifiedOn`).                                                                                                                                                                                                                  |

## Crawler class

The `Crawler` class represents an AWS Glue crawler.

###### Mandatory constructor arguments

The following are mandatory constructor arguments for the `Crawler`
class.

| Argument name | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Name`        | `str`  | Name to assign to the crawler. AWS Glue adds a randomly generated suffix to the<br>name to distinguish the crawler from those created by other blueprint runs.                                                                                                                                                                                                                                          |
| `Role`        | `str`  | ARN of the role that the crawler should assume while running.                                                                                                                                                                                                                                                                                                                                           |
| `Targets`     | `dict` | Collection of targets to crawl. `Targets` class constructor<br>arguments are defined in the [CrawlerTargets structure](aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-CrawlerTargets "aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-CrawlerTargets") in the API documentation.<br>All `Targets` constructor arguments are optional, but you must pass at<br>least one. |

###### Optional constructor arguments

The following are optional constructor arguments for the `Crawler`
class.

| Argument name         | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DependsOn`           | `dict` | List of workflow entities that the crawler depends on. For more information,<br>see [Using the DependsOn<br>argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on "developing-blueprints-code-layout.md#developing-blueprints-code-layout-depends-on").                                                                                                                                                                          |
| `WaitForDependencies` | `str`  | Indicates whether the crawler should wait until _all_<br>entities on which it depends complete before running or until<br>\*any<br>• completes. For more information, see [Using the<br>WaitForDependencies argument](developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies "developing-blueprints-code-layout.md#developing-blueprints-code-layout-wait-for-dependencies"). Omit if the<br>crawler depends on only one entity. |
| (Crawler properties)  | -      | Any of the crawler properties listed in [Crawler structure](aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-Crawler "aws-glue-api-crawler-crawling.md#aws-glue-api-crawler-crawling-Crawler") in the AWS Glue API documentation,<br>with the following exceptions:<br>• `State`<br>• `CrawlElapsedTime`<br>• `CreationTime`<br>• `LastUpdated`<br>• `LastCrawl`<br>• `Version`                                                                          |

## Workflow class

The `Workflow` class represents an AWS Glue workflow. The workflow layout script
returns a `Workflow` object. AWS Glue creates a workflow based on this
object.

###### Mandatory constructor arguments

The following are mandatory constructor arguments for the `Workflow`
class.

| Argument name | Type       | Description                                                                                                                                                                                                                                      |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Name`        | `str`      | Name to assign to the workflow.                                                                                                                                                                                                                  |
| `Entities`    | `Entities` | A collection of entities (jobs and crawlers) to include in the workflow. The<br>`Entities` class constructor accepts a `Jobs` argument,<br>which is a list of `Job` objects, and a `Crawlers` argument,<br>which is a list of `Crawler` objects. |

###### Optional constructor arguments

The following are optional constructor arguments for the `Workflow`
class.

| Argument name          | Type   | Description                                                                                                                                  |
| ---------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `Description`          | `str`  | See [Workflow structure](aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow "aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow"). |
| `DefaultRunProperties` | `dict` | See [Workflow structure](aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow "aws-glue-api-workflow.md#aws-glue-api-workflow-Workflow"). |
| `OnSchedule`           | `str`  | A `cron` expression.                                                                                                                         |

## Class methods

All three classes include the following methods.

**validate()**

Validates the properties of the object and if errors are found, outputs a message
and exits. Generates no output if there are no errors. For the `Workflow`
class, calls itself on every entity in the workflow.

**to_json()**

Serializes the object to JSON. Also calls `validate()`. For the
`Workflow` class, the JSON object includes job and crawler lists, and a
list of triggers generated by the job and crawler dependency specifications.
