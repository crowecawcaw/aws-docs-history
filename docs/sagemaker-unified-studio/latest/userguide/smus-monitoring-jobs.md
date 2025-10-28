# Monitoring jobs and job runs

SageMaker Unified Studio provides comprehensive monitoring capabilities for jobs and job runs,
enabling you to track performance, costs, and run history.

## Monitoring capabilities

- **Job Status and History** - View job run status, success rates, and historical performance.
- **Resource Utilization** - Monitor compute resource consumption and optimization opportunities.
- **Cost Tracking** - Track run costs and resource usage for budgeting and optimization.
- **Logs and Metrics** - Access CloudWatch logs and Spark UI for detailed troubleshooting.
- **Data Lineage** - Track data flow and dependencies across job runs.

SageMaker Unified Studio provides aggregate job-level metrics including:

- Job success rate.
- Average resource consumption (estimated in DPU hours).
- Average runtime.

For individual job runs, detailed metrics include:

- Status (success, failure, in progress).
- Resources consumed (estimated).
- Retry attempts.
- Duration.
- Settings used for the run.

CloudWatch logs (both driver and executor logs) are automatically pulled into the output log tab,
eliminating the need to navigate to CloudWatch separately for troubleshooting.

## Job runs view

###### Note

Job run history is accessible for 90 days for your workflow and job run.

The Job runs resource list shows the jobs for the specified date range and filters.

You can filter the jobs on additional criteria, such as status, job type, and the job name. In the
filter box at the top of the table, you can enter the text to use as a filter. The table results are updated with rows that contain
matching text as you enter the text.

The Job runs resource list displays the details for the job runs. You can sort the rows in the table by choosing a column heading.
The table contains the following information:

Job name

The name of the job.

Type

The type of job environment:

AWS Glue ETL: Runs in an Apache Spark environment managed by AWS Glue.

Start time

The date and time at which this job run was started.

End time

The date and time that this job run completed.

Run status

The current state of the job run. Values can be:

STARTING

RUNNING

STOPPING

STOPPED

SUCCEEDED

WAITING

FAILED

TIMEOUT

Run time

The amount of time that the job run consumed resources.

Capacity

The number of data processing units (DPUs) that were allocated for this job run.

Instance type

The type of predefined instance that was allocated when the job ran. Values can be G.1X, G.2X, G.4X or G.8X.

DPU hours

The estimated number of DPUs used for the job run. A DPU is a relative measure of processing power. DPUs are used to determine the cost of running your job.

You can choose any job run in the list and view additional information. Choose a job run, and then do one of the following:

- Choose the Actions menu and the View job option to view the job in the visual editor.
- Choose the Actions menu and the Stop run option to stop the current run of the job.
- Choose the View CloudWatch logs button to view the job run logs for that job.
- Choose View details to view the job run details page.

## To access job monitoring

1. Navigate to the **Jobs** section in your SageMaker Unified Studio project.
2. Select the job you want to monitor.
3. View aggregate metrics including:
   - Job success rate.
   - Average run time.
   - Resource consumption.

4. Expand individual job runs to view detailed logs, metrics, and performance data.

## Viewing the details of a job run

The Run details page provides information about the job run, settings, output logs, and run parameters.

The information displayed on the job run detail page includes:

Job name

The name of the job.

Run Status

The current state of the job run. Values can be:

STARTING

RUNNING

STOPPING

STOPPED

SUCCEEDED

WAITING

FAILED

TIMEOUT

Attempt

The number of automatic retry attempts for this job run.

Start time

The date and time at which this job run was started.

End time

The date and time that this job run completed.

Duration

The amount of time spent preparing to run the job.

DPU hours consumed

The number of AWS Glue data processing units (DPUs) that were allocated for this job run.

Max capacity

The maximum capacity available to the job run.

You can also view the job run settings, which show you the compute type, engine version, instance type, capacity (DPUs), and timeout.

To view output logs and run parameters:

- In the Job runs table, choose a job run. The Output logs are visible below the Job run settings.

You can:

    + Copy log by choosing **Copy logs**.
    + Download log by choosing **Download as log file**.
    + Search the log by entering a search query. You can then filter on the results of your search and sort results.

- In the Job run details page, choose the **Run parameters** tab.
