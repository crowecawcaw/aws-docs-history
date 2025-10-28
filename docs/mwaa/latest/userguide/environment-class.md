# Configuring the Amazon MWAA environment class

The environment class you choose for your Amazon MWAA environment determines the size of the AWS-managed AWS Fargate containers where the
[Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html "https://airflow.apache.org/docs/apache-airflow/stable/executor/celery.html") runs, and the AWS-managed Amazon Aurora PostgreSQL
metadata database where the Apache Airflow schedulers creates task instances. This topic describes each Amazon MWAA environment class, and how to update the environment
class on the Amazon MWAA console.

###### Sections

- [Environment capabilities](#environment-class-sizes "#environment-class-sizes")
- [Apache Airflow schedulers](#environment-class-schedulers "#environment-class-schedulers")

## Environment capabilities

The following section contains the default concurrent Apache Airflow tasks, Random Access Memory (RAM), and the virtual centralized processing units (vCPUs)
for each environment class. The concurrent tasks listed assume that task concurrency does not exceed the Apache Airflow worker capacity in the environment.

In the following table, DAG capacity refers to DAG definitions, not executions, and assumes that your DAGs are
[dynamic](https://airflow.apache.org/docs/apache-airflow/2.6.3/concepts/dags.html?highlight=dynamic%20dag#dynamic-dags "https://airflow.apache.org/docs/apache-airflow/2.6.3/concepts/dags.html?highlight=dynamic%20dag#dynamic-dags") in a single Python file and written with [Apache Airflow best practices](https://airflow.apache.org/docs/apache-airflow/2.6.3/best-practices.html?highlight=best%20practices "https://airflow.apache.org/docs/apache-airflow/2.6.3/best-practices.html?highlight=best%20practices").

Task executions depend on how many are scheduled simultaneously, and assumes that the
number of DAG runs set to start at the same time doesn't exceed the default [`max_dagruns_per_loop_to_schedule`](https://airflow.apache.org/docs/apache-airflow/2.6.3/configurations-ref.html#config-scheduler-max-dagruns-per-loop-to-schedule "https://airflow.apache.org/docs/apache-airflow/2.6.3/configurations-ref.html#config-scheduler-max-dagruns-per-loop-to-schedule"), as well as the size and number of workers as
detailed in this topic.

mw1.micro

- Up to 25 DAG capacity
- 3 concurrent tasks (by default)
- Components:
  - Webserver: 1 vCPU, 3GB RAM
  - Worker and scheduler: 1 vCPU, 3GB RAM
  - Database: 2 vCPU, 4GB RAM

  ###### Note

  mw1.micro does not support auto-scaling.

mw1.small

- Up to 50 DAG capacity
- 5 concurrent tasks (by default)
- Components:
  - Webservers: 1 vCPU, 2GB RAM each
  - Workers: 1 vCPU, 2GB RAM each
  - Schedulers: 1 vCPU, 2GB RAM each
  - Database: 2 vCPU, 4GB RAM

mw1.medium

- Up to 250 DAG capacity
- 10 concurrent tasks (by default)
- Components:
  - Webservers: 1 vCPU 2GB RAM each
  - Workers: 2 vCPU 4GB RAM each
  - Schedulers: 2 vCPU 4GB RAM each
  - Database: 2 vCPU 8GB RAM

mw1.large

- Up to 1000 DAG capacity
- 20 concurrent tasks (by default)
- Components:
  - Webservers: 2 vCPU 4GB RAM each
  - Workers: 4 vCPU 8GB RAM each
  - Schedulers: 4 vCPU 8GB RAM each
  - Database: 2 vCPU 8GB RAM

mw1.xlarge

- Up to 2000 DAG capacity
- 40 concurrent tasks (by default)
- Components:
  - Webservers: 4 vCPU 12GB RAM each
  - Workers: 8 vCPU 24GB RAM each
  - Schedulers: 8 vCPU 24GB RAM each
  - Database: 4 vCPU 32GB RAM

mw1.2xlarge

- Up to 4000 DAG capacity
- 80 concurrent tasks (by default)
- Componenets:
  - Webservers: 8 vCPU 24GB RAM each
  - Workers: 16 vCPU 48GB RAM each
  - Schedulers: 16 vCPU 48GB RAM each
  - Database: 8 vCPU 64GB RAM

You can use `celery.worker_autoscale` to increase tasks per worker. For more information, refer to the [Example high performance use case](mwaa-autoscaling.md#mwaa-autoscaling-high-volume "mwaa-autoscaling.md#mwaa-autoscaling-high-volume").

## Apache Airflow schedulers

The following section contains the Apache Airflow scheduler options available on the Amazon MWAA, and how the number of schedulers affects the number
of triggerers.

In Apache Airflow, a [triggerer](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html "https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/deferring.html") manages tasks which it defers until certain conditions specified using a
trigger have been met. In Amazon MWAA the triggerer runs alongside the
scheduler on the same Fargate task. Increasing the scheduler count correspondingly increases
the number of available triggerers, optimizing how the environment manages deferred tasks.
This ensures efficient handling of tasks, promptly scheduling them to run when conditions are
satisfied.

Apache Airflow v3

- **v3** - For environments larger than
  mw1.micro, accepts values from `2` to `5`. Defaults to
  `2` for all environment sizes except mw1.micro, which defaults to
  `1`.

Apache Airflow v2

- **v2** - For environments larger than
  mw1.micro, accepts values from `2` to `5`. Defaults to
  `2` for all environment sizes except mw1.micro, which defaults to
  `1`.
