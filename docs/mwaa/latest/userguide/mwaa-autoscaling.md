# Configuring Amazon MWAA worker automatic scaling

The auto scaling mechanism automatically increases the number of Apache Airflow workers in response to running and queued tasks on your Amazon Managed Workflows for Apache Airflow environment and disposes of
extra workers when there are no more tasks queued or executing. This topic describes how you can configure auto scaling by specifying the maximum number of Apache Airflow workers
that run on your environment using the Amazon MWAA console.

###### Note

Amazon MWAA uses Apache Airflow metrics to determine when additional [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html "https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html") workers are needed,
and as required increases the number of Fargate workers up to the value specified by `max-workers`. As the additional workers complete work and work load
decreases, Amazon MWAA removes them, thus downscaling back to the value set by `min-workers`.

If workers pick up new tasks while downscaling, Amazon MWAA keeps the Fargate resource and does not remove the worker. For more information, refer to [How Amazon MWAA auto scaling works](#mwaa-autoscaling-how "#mwaa-autoscaling-how").

###### Sections

- [How worker scaling works](#mwaa-autoscaling-how "#mwaa-autoscaling-how")
- [Using the Amazon MWAA console](#mwaa-autoscaling-console "#mwaa-autoscaling-console")
- [Example high performance use case](#mwaa-autoscaling-high-volume "#mwaa-autoscaling-high-volume")
- [Troubleshooting tasks stuck in the running state](#mwaa-autoscaling-stranded "#mwaa-autoscaling-stranded")
- [What's next?](#mwaa-autoscaling-next-up "#mwaa-autoscaling-next-up")

## How worker scaling works

Amazon MWAA uses `RunningTasks` and `QueuedTasks` [metrics](access-metrics-cw.md#available-metrics-cw "access-metrics-cw.md#available-metrics-cw"), where
_(tasks running + tasks queued) / ([tasks per worker](environment-class.md#environment-class-sizes "environment-class.md#environment-class-sizes")) = (required workers)_. If the required number of workers is greater than the current number of workers,
Amazon MWAA will add Fargate worker containers to that value, up to the maximum value specified by `max-workers`.

As the workload decreases and the `RunningTasks` and `QueuedTasks` metric sum reduces, Amazon MWAA requests Fargate to scale down the workers for the environment.
Any workers which still completing work remain protected during downscaling until they complete their work. Depending on the workload, tasks might be queued while
workers downscale.

## Using the Amazon MWAA console

You can choose the maximum number of workers that can run on your environment concurrently on the Amazon MWAA console. By default, you can specify a maximum value up to 25.

###### To configure the number of workers

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Edit**.
4. Choose **Next**.
5. On the **Environment class** pane, enter a value in **Maximum worker count**.
6. Choose **Save**.

###### Note

It can take a few minutes before changes take effect on your environment.

## Example high performance use case

The following section describes the type of configurations you can use to enable high performance and parallelism on an environment.

### On-premise Apache Airflow

Typically, in an on-premise Apache Airflow platform, you configure task parallelism, auto scaling, and concurrency settings in your `airflow.cfg` file:

- `core.parallelism` – The maximum number of task instances that can run simultaneously per scheduler.
- `core.dag_concurrency` – The maximum concurrency for DAGs (not workers).
- `celery.worker_autoscale` – The maximum and minimum number of tasks that can run concurrently on any worker.

For example, if `core.parallelism` was set to `100` and `core.dag_concurrency` was set to `7`, you can only run a total of `14` tasks concurrently if you had 2 DAGs. Given, each DAG is set to run only seven tasks concurrently (in `core.dag_concurrency`), even though overall parallelism is set to `100` (in `core.parallelism`).

###### Note

`core.dag_concurrency` is not available in Apache Airflow v3.

### On an Amazon MWAA environment

On an Amazon MWAA environment, you can configure these settings directly on the Amazon MWAA console using [Using Apache Airflow configuration options on Amazon MWAA](configuring-env-variables.md "configuring-env-variables.md"), [Configuring the Amazon MWAA environment class](environment-class.md "environment-class.md"), and the **Maximum worker count** auto scaling mechanism. While `core.dag_concurrency` is not available in the drop down list as an **Apache Airflow configuration option** on the Amazon MWAA console, you can add it as a custom [Apache Airflow configuration option](configuring-env-variables.md "configuring-env-variables.md").

Let's say, when you created your environment, you chose the following settings:

1. The **mw1.small** [environment class](environment-class.md "environment-class.md") which controls the maximum number of concurrent tasks each worker can run by default and the vCPU of containers.
2. The default setting of `10` workers in **Maximum worker count**.
3. An [Apache Airflow configuration option](configuring-env-variables.md "configuring-env-variables.md") for `celery.worker_autoscale` of `5,5` tasks per worker.

This means you can run 50 concurrent tasks in your environment. Any tasks beyond 50 are queued, and wait for the running tasks to complete.

**Run more concurrent tasks**. You can modify your environment to run more tasks concurrently using the following configurations:

1. Increase the maximum number of concurrent tasks each worker can run by default and the vCPU of containers by choosing the `mw1.medium` (10 concurrent tasks by default) [environment class](environment-class.md "environment-class.md").
2. Add `celery.worker_autoscale` as an [Apache Airflow configuration option](configuring-env-variables.md "configuring-env-variables.md").
3. Increase the **Maximum worker count**. In this example, increasing maximum workers from `10` to `20` doubles the number of concurrent tasks the environment can run.

**Specify Minimum workers**. You can also specify the minimum and maximum number of Apache Airflow workers that run in your environment using the AWS Command Line Interface (AWS CLI). For example:

```
aws mwaa update-environment --max-workers 10 --min-workers 10 --name `YOUR_ENVIRONMENT_NAME`
```

To learn more, refer to the [update-environment](../../../cli/latest/reference/mwaa/update-environment.md "../../../cli/latest/reference/mwaa/update-environment.md") command in the AWS CLI.

## Troubleshooting tasks stuck in the running state

In rare cases, Apache Airflow might think there are tasks still running. To resolve this issue, you need to clear the stranded task in your Apache Airflow UI. For more information, refer to the [Troubleshooting Amazon Managed Workflows for Apache Airflow](troubleshooting.md "troubleshooting.md") troubleshooting topic.

## What's next?

- Learn more about the best practices we recommend to tune the performance of your environment in [Performance tuning for Apache Airflow on Amazon MWAA](best-practices-tuning.md "best-practices-tuning.md").
