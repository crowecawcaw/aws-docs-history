# Crawler scheduler API

The Crawler scheduler API describes AWS Glue crawler data
types, along with the API for creating, deleting, updating, and listing crawlers.

## Data types

- [Schedule structure](#aws-glue-api-crawler-scheduler-Schedule "#aws-glue-api-crawler-scheduler-Schedule")

## Schedule structure

A scheduling object using a `cron` statement to schedule
an event.

###### Fields

- `ScheduleExpression` – UTF-8 string.

A `cron` expression used to specify the schedule (see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

- `State` – UTF-8 string (valid values: `SCHEDULED` | `NOT_SCHEDULED` | `TRANSITIONING`).

The state of the schedule.

## Operations

- [UpdateCrawlerSchedule action (Python: update_crawler_schedule)](#aws-glue-api-crawler-scheduler-UpdateCrawlerSchedule "#aws-glue-api-crawler-scheduler-UpdateCrawlerSchedule")
- [StartCrawlerSchedule action (Python: start_crawler_schedule)](#aws-glue-api-crawler-scheduler-StartCrawlerSchedule "#aws-glue-api-crawler-scheduler-StartCrawlerSchedule")
- [StopCrawlerSchedule action (Python: stop_crawler_schedule)](#aws-glue-api-crawler-scheduler-StopCrawlerSchedule "#aws-glue-api-crawler-scheduler-StopCrawlerSchedule")

## UpdateCrawlerSchedule action (Python: update_crawler_schedule)

Updates the schedule of a crawler using a `cron` expression.

###### Request

- `CrawlerName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the crawler whose schedule to update.

- `Schedule` – UTF-8 string.

The updated `cron` expression used to specify the schedule
(see [Time-Based
Schedules for Jobs and Crawlers](monitor-data-warehouse-schedule.md "monitor-data-warehouse-schedule.md"). For example, to run something every
day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `InvalidInputException`
- `VersionMismatchException`
- `SchedulerTransitioningException`
- `OperationTimeoutException`

## StartCrawlerSchedule action (Python: start_crawler_schedule)

Changes the schedule state of the specified crawler to `SCHEDULED`,
unless the crawler is already running or the schedule state is already `SCHEDULED`.

###### Request

- `CrawlerName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the crawler to schedule.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `SchedulerRunningException`
- `SchedulerTransitioningException`
- `NoScheduleException`
- `OperationTimeoutException`

## StopCrawlerSchedule action (Python: stop_crawler_schedule)

Sets the schedule state of the specified crawler to `NOT_SCHEDULED`,
but does not stop the crawler if it is already running.

###### Request

- `CrawlerName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the crawler whose schedule state to set.

###### Response

- _No Response parameters._

###### Errors

- `EntityNotFoundException`
- `SchedulerNotRunningException`
- `SchedulerTransitioningException`
- `OperationTimeoutException`
