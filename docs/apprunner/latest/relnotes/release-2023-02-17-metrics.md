

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds new service level metrics for CPU, memory, and concurrency on February 17, 2023
<a name="release-2023-02-17-metrics"></a>

AWS App Runner adds new service level metrics for CPU utilization, memory utilization, and concurrent requests.

**Release date:** February 17, 2023

## Changes
<a name="release-2023-02-17-metrics.changes"></a>

AWS App Runner now provides service level metrics for *CPU utilization*, *memory utilization*, and the total number of *concurrent requests* in the App Runner console and the Amazon CloudWatch. 

Earlier, App Runner only displayed metrics for CPU and memory utilization at the instance level. Now with App Runner support to display these metrics at the service level, you can gauge CPU and memory usage related to your service. Use the new service level concurrency metrics in conjunction with CPU and memory utilization metrics to derive data to set your auto-scaling configuration for improved service efficiency. Use these metrics to improve performance of your service by making better decisions when defining compute configuration (*CPU and Memory*) and auto-scaling configuration (*concurrency*). For more information, see [Viewing App Runner service metrics reported to CloudWatch](https://docs.aws.amazon.com/apprunner/latest/dg/monitor-cw.html) in the *AWS App Runner Developer Guide*.