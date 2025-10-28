AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Run optimization for a private HealthOmics workflow

You can optimize runs for total cost, total run time, or a combination of both. HealthOmics provides data and tools to
help you with run optimization decisions. Run optimization doesn't apply to Ready2Run workflows, because you don't
have any control over how the service manages resource provisioning for these workflows.

The first step is to understand the current task resource usage and cost for the tasks in the run, and then
apply methods for optimizing the run cost and performance.

###### Topics

- [Run Analyzer](#workflows-run-analyzer "#workflows-run-analyzer")
- [Determine run costs](#workflows-run-costs "#workflows-run-costs")
- [Determine run time usage](#workflows-run-time "#workflows-run-time")
- [Methods to optimize runs](#run-optimize-methods "#run-optimize-methods")
- [Impact of file size variance between runs](#workflows-run-file-variance "#workflows-run-file-variance")
- [Methods to optimize resource concurrency](#run-optimize-concurrency "#run-optimize-concurrency")

## Run Analyzer

HealthOmics provides an open source tool named [Run Analyzer](https://github.com/awslabs/amazon-omics-tools?tab=readme-ov-file#omics-run-analyzer "https://github.com/awslabs/amazon-omics-tools?tab=readme-ov-file#omics-run-analyzer").
This tool extracts task-level resource usage information for a run and suggests optimization opportunities for
cost and run performance.

###### Note

Run analyzer estimates task costs and potential cost savings based on AWS list prices at the time you run the
tool. Assess the optimization recommendations and implement those that make sense for your use cases. Test the
optimizations that you adopt to make sure that they work for your run.

Run Analyzer performs the following tasks:

- Evaluates memory and compute bottlenecks.
- Identifies tasks that are over-provisioned for memory or CPU, and recommends new instance sizes that can
  reduce costs.
- Computes cost estimates for individual tasks and computes the potential cost savings if you apply the
  recommendations.
- Gives you a timeline view of tasks so you can verify the task dependencies and processing sequence. The
  timeline also helps you to identify long running tasks.
- Provides recommendations about the file-system size for the run storage.
- Shows you task provisioning times so that you can identify areas where large container loads may be slowing
  down provisioning time.
- The tool includes an input parameter (headroom) you can use to control the aggressiveness of the
  optimization recommendations.

The following sections include specific suggestions for using Run Analyzer to optimize runs.

## Determine run costs

You can use the following methods and guidelines to determine run costs:

- To view the total run costs for a billing period, follow these steps:
  1.  Open the [Billing and Cost Management](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/") console
      and choose **Bills**.
  2.  In **Charges by service**, expand **Omics**.
  3.  Expand the **region**, then view the cost of all your runs itemized by
      omics instance type, run storage type, and Ready2Run workflow.

- To generate a cost report that includes information for each run, follow these steps:
  1.  Open the [Billing and Cost Management](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/") console
      and choose **Data Exports**.
  2.  Choose **Create** to create a new data export.
  3.  Enter an **Export name** for the data export. Keep the other fields at their default
      values to create a CUR (cost and usage) report.
  4.  For **Time granularity**, select hourly or daily.
  5.  Under **Data export storage settings**, perform these configuration steps:
      1. Configure an Amazon S3 bucket for the data export.
      2. For **File versioning**, select whether to overwrite the existing export file or create a
         new file each time.The system generates the first report within the next 24 hours and generates
         subsequent reports once a day.

  6.  For more information about how to create the data export, see [Creating data exports](../../../cur/latest/userguide/dataexports-create.md "../../../cur/latest/userguide/dataexports-create.md") in the _AWS Data Exports User Guide_.

- You can tag your runs to monitor and optimize costs by category, such as by team or by project. If you use
  tags, follow these steps to view run costs by tag category:
  1.  Open the [Billing and Cost Management](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/") console
      and choose **Cost Explorer**.
  2.  In **Report parameters > Group by**, chose **Tag** as the dimension. and select
      the desired **Tag** name.

- To see resource usage for tasks, view the run manifest logs in CloudWatch. For more information, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md "monitoring-cloudwatch-logs.md").
- Use the [Run Analyzer](#workflows-run-analyzer "#workflows-run-analyzer") tool to extract
  task resource usage information for a run.

## Determine run time usage

You can use the following methods to help you investigate run time usage:

- From the **Runs** page of the console, you can view the total run time for a run.
- From the **Run details** page, you can view the following items:
  - View the total run time for a run.
  - View the run time for each task in the run.
  - Choose one of the links to view the logs in Amazon S3, or to view the run logs or run manifest logs in
    CloudWatch.

- From the **Run tasks** list, choose the **View logs** link for a task to view the task
  logs in CloudWatch.
- The response to the `listRuns` API operation includes the run start time and stop time, so you can
  calculate the total run time.
- The [Run Analyzer](#workflows-run-analyzer "#workflows-run-analyzer") tool shows task durations on a timeline view. This
  tool provides a visual representation of the task processing sequence, which you can match with the expected
  order.

## Methods to optimize runs

HealthOmics automatically provisions, manages, and optimizes resources that perform data staging (such as data
imports and data exports). HealthOmics also starts and runs the workflow engine for your workflow.
However, you can influence run start times, task
start times, and overall task run time by setting various run configurations. Your overall approach to the workflow
definition and design also impacts task run time. The following list describes factors that can affect run and task
performance:

**Run storage type**

The run storage type has an impact on run performance and run provisioning time. Dynamic run storage
provisions faster and never runs out of memory, because it scales dynamically with your run storage needs.
Dynamic run storage is also a good fit for workflows in development, where you may often start and stop a
workflow to troubleshoot issues.

Static run storage requires longer file system provisioning times, but can complete some runs faster,
typically if the runs have high task concurrency or require greater than 9.6 TiB of file system capacity.
Static run storage is well suited for long running workflows with high I/O requirements.

To help you evaluate the cost vs. performance of each run storage type for a given run, you can try A/B
testing to see which run storage type delivers better performance. Also, consider using dynamic run storage
for your development cycles, then use static run storage for production runs at scale.

For more information about run storage types [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md")

**Over-provision run static storage**

If your workflow task computation is constrained by I/O, consider over-provisioning the static run
storage. Storage cost increases with its size, but maximum throughput of the file system also increases. If
an expensive compute task is experiencing I/O bottlenecks, increasing the file system size to reduce the
task run time may reduce the overall cost.

**Reduce container image sizes**

When each task starts, HealthOmics loads the container you specified for the task. Larger containers take
longer to load. Optimize your containers to be as small as possible to improve the efficiency of launching
new tasks. If you add large datasets to your containers, consider storing the datasets in S3 and having your
workflow import the data from S3. For the maximum container sizes that HealthOmics supports, see [HealthOmics workflow fixed size quotas](fixed-quotas.md#fixed-quotas-workflows "fixed-quotas.md#fixed-quotas-workflows").

**Task size**

You can combine small, sequential tasks into a single task to save task provisioning time. Also,
HealthOmics has a one-minute minimum task duration charge, so combining tasks may reduce costs. Within the
combined task, you may be able to use Unix pipes to avoid the I/O cost of serializing and deserializing
files.

**File compression**

Avoid overly compressing workflow intermediate files. Most genomics formats use “gzip” or “block gzip”
compression. Decompressing the task input file and recompressing the task output file can consume a large
percentage of the overall task CPU usage. Some genomics applications allow you to set the compression level
when serializing outputs. By reducing the level of compression, you can reduce CPU time, although larger
files increase the time spent writing to disk. Depending on the task and the application, you can find the
optimal compression level for intermediate files that result in the shortest run time. We recommend that you
start by targeting the tasks with the largest output files. A compression level of 2 works well for several
scenarios. You can start with this level for your use-case, and compare results by trying other compression
levels.

**Thread count**

If you specify threads in your task definition, set the number of threads to the same value as the
number of requested vCPUs.

**Specify compute and memory**

If you don't specify memory or compute resources in your task, HealthOmics assigns the smallest instance type
(`omics.c.large`) as the default . Explicitly declare your memory and compute requirements if you want HealthOmics to
assign a larger instance type.

HealthOmics allocates the number of vCPUs, memory, and GPU resources that you request. For instance, if you ask
for 15vCPUs and 33GiB, HealthOmics allocates an omics.m.4xl instance (16vCPUs, 64GB) for your task, but your task
can use only 15 vCPUs and 33GiB. Therefore, we recommend that you request vCPUs and memory resources that
match an omics instance.

**Batch multiple samples into one run**

Because file system provisioning takes time at the start of the run, you can save on provisioning time
by batching multiple samples into the same run. Consider the following factors before deciding on this
approach:

- A single bad sample can cause a workflow to fail, so batching samples could increase the number of
  failed workflows. If you aren't confident that your workflow will succeed most of the time, one run per
  sample could be a better approach.
- HealthOmics allocates one run storage file system for the whole workflow. For a batch of samples, make sure to specify a
  large enough amount of run storage to process all the samples.
- There is a maximum amount of run storage per workflow, so that may constrain the number of samples
  you can add to the batch.
- The minimum run storage size is 1.2 TiB, so batching may reduce costs if the workflow uses much less
  storage than the minimum for each sample.
- Run storage can handle multiple simultaneous connections, so having multiple tasks using the same run
  storage shouldn't cause I/O bottlenecks.
- Each run has its own set of tags. If you tag workflows with information for budgeting or
  tracking, it may be better to use separate runs.
- IAM roles apply to the whole run. Each user has access to all the data for a batch of samples. Having separating workflows gives you
  the ability to use more fine-grained permissions.
- HealthOmics sets account-level quotas for maximum number of concurrent workflows and maximum number of concurrent tasks
  in a workflow. For information on how to request an increase for these quotas, see
  [HealthOmics service quotas](service-quotas.md "service-quotas.md").

**Use parameters for container images**

Parameterize your container images rather than embedding their URIs in the workflow. Wheb they are run
parameters, HealthOmics validates that the run has access to your containers before the run starts. Otherwise, the
task fails during the run, when you have incurred charges for any completed tasks. Also, because these are
parameterized inputs, HealthOmics generates a checksum in the run manifest, which improves the run
provenance.

**Use a linter**

Use a linter to find common workflow errors before you run a new workflow. For more information, see
[Workflow linters in HealthOmics](workflows-linter.md "workflows-linter.md").

**Use EventBridge to flag issues**

Use EventBridge customized alerts to catch anomalies that are specific to your business logic.

**Use sequence stores**

Consider using a sequence store for your source data to save on storage costs. For more information, see
the [Store omics data cost-effectively at any scale with HealthOmics](https://aws.amazon.com/blogs/industries/store-omics-data-cost-effectively-at-any-scale-with-aws-healthomics/ "https://aws.amazon.com/blogs/industries/store-omics-data-cost-effectively-at-any-scale-with-aws-healthomics/") blog post.

## Impact of file size variance between runs

Users often design and test runs using a small set of testing data, then encounter a wide variety of data with
significant file-size variance in production runs. Make sure you account for this variance when you optimize the
run.

The following list describes recommendations for optimization where there is significant variance in file sizes:

**Vary file sizes in your testing data**

Try to use testing data during development that has a representative amount of variance.

**Use Run Analyzer**

Use the Run Analyzer tool across a variety of samples to account for variance in data sizes.

You can use the run analyzer to understand variance between runs in your production data samples. Use
`--batch` mode in Run Analyzer to generate statistics for a batch of runs
and analyze the maximum compute resources required to handle outliers in your data sets.

For example, you can give run analyzer a full flow cell of data in batch mode to understand peak vCPU
and memory utilization for the full flow cell.

**Reduce size variance of the input datasets**

If you see high variance in sample sizes, you can bifurcate samples upstream of HealthOmics and select
different file system sizes for each batch to save on run storage costs.

In WDL, use the `size` function to bifurcate resource allocation for individual tasks for large versus
small samples. Apply this strategy to your most expensive tasks to have the most impact.

In Nextflow, use conditional resources for tiering resource allocation based on file size or file name.
For more information, see [Conditional process resources](https://nextflow-io.github.io/patterns/conditional-resources " https://nextflow-io.github.io/patterns/conditional-resources")
on the Nextflow GitHub site.

**Don't optimize too soon**

Finalize your workflow code and logic before investing in significant performance tuning efforts.
Changing your code can have significant impacts on required resources. If you optimize a run too soon in the
development process, you may over-optimize or you may need to optimize again if the workflow definition
changes later.

**Re-run the Run Analyzer tool periodically**

If you make changes to your workflow definition over time or if your sample variance changes,
periodically run the Run Analyzer tool to help you made additional optimizations.

## Methods to optimize resource concurrency

HealthOmics provides the following capabilities to help you control and manage costs when processing runs at
scale:

- Use run groups to control your costs and resource usage. You can set maximum values in the run group for
  number of concurrent runs, vCPUs, GPUs, and total run time per task. If separate teams or groups use the same
  account, you can create a separate run group for each team. You can control resource usage and costs per team and by
  configuring the run group maximum values. For more information, see [Using HealthOmics run groups](creating-run-groups.md "creating-run-groups.md").
- During development, you can configure a separate run group with lower maximum values to catch runaway
  tasks.
- Service Quotas also help to protect your account from excessive resource requests. For information about
  Service Quotas, including how to request quota value increases, see [HealthOmics service quotas](service-quotas.md "service-quotas.md")
