# Release: App Runner adds new service level metrics for CPU, memory, and concurrency on February 17, 2023

AWS App Runner adds new service level metrics for CPU utilization, memory utilization, and concurrent requests.

**Release date:** February 17, 2023

## Changes

AWS App Runner now provides service level metrics for _CPU
utilization_, _memory utilization_, and the total number of _concurrent requests_ in the App Runner console
and the Amazon CloudWatch.

Earlier, App Runner only displayed metrics for CPU and memory utilization at the instance level. Now with App Runner support to display these metrics at the
service level, you can gauge CPU and memory usage related to your service. Use the new service level concurrency metrics in conjunction with CPU and
memory utilization metrics to derive data to set your auto-scaling configuration for improved service efficiency. Use these metrics to improve performance
of your service by making better decisions when defining compute configuration (_CPU and Memory_) and auto-scaling configuration
(_concurrency_). For more information, see [Viewing App Runner service metrics reported to
CloudWatch](../dg/monitor-cw.md "../dg/monitor-cw.md") in the _AWS App Runner Developer Guide_.
