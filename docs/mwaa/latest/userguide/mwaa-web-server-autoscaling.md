# Configuring Amazon MWAA webserver automatic scaling

For environments running Apache Airflow v2.2.2 and later, Amazon MWAA dynamically scales your webservers to handle fluctuating workloads,
which in turn prevents performance issues during peak loads. By automatically scaling the number of webservers based on CPU utilization and active connection count,
Amazon MWAA ensures that your Apache Airflow environment can seamlessly accommodate increased demand, whether from REST API requests, CLI usage, or more concurrent Apache Airflow
user interface users.

###### Sections

- [How webserver scaling works](#mwaa-web-server-autoscaling-how "#mwaa-web-server-autoscaling-how")
- [Using the Amazon MWAA console](#mwaa-web-server-autoscaling-console "#mwaa-web-server-autoscaling-console")

## How webserver scaling works

Amazon MWAA uses the container metric, [CPUUtilization](accessing-metrics-cw-container-queue-db.md#container-list "accessing-metrics-cw-container-queue-db.md#container-list"), and the load balancer metric, [ActiveConnectionCount](accessing-metrics-cw-container-queue-db.md#alb-list "accessing-metrics-cw-container-queue-db.md#alb-list"), to determine if scaling the webservers is required based on
the amount of traffic. If `CPUUtilization` is greater than 70 or `ActiveConnectionCount` is greater than 15, Amazon MWAA will add additional Fargate webserver containers
up to the maximum value specified by `MaxWebservers`.

As traffic decreases and the `CPUUtilization` and `ActiveConnectionCount` values reduce,
Amazon MWAA requests Fargate to scale down the webserver containers for the environment to the minimum value set by `MinimumWebservers`.

## Using the Amazon MWAA console

You can choose the number of webservers that can run on your environment concurrently on the Amazon MWAA console. By default, the minimum number of webservers is two, and the maximum number of webservers is five.

###### To configure the number of webservers

1. Open the [Environments](https://console.aws.amazon.com/mwaa/home#/environments "https://console.aws.amazon.com/mwaa/home#/environments") page on the Amazon MWAA console.
2. Choose an environment.
3. Choose **Edit**.
4. Choose **Next**.
5. On the **Environment class** pane, enter a value in **Maximum webserver count**.
6. Next, enter a value in **Minimum webserver count**.
7. Choose **Save**.

###### Note

It can take a few minutes before changes take effect on your environment.
