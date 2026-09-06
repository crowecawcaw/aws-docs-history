

# Monitoring query execution plans and peak memory for Aurora PostgreSQL
<a name="AuroraPostgreSQL.Monitoring.Query.Plans"></a>

You can monitor query execution plans in your Aurora PostgreSQL DB instance to detect the execution plans contributing to current database load and to track performance statistics of execution plans over time using the `aurora_compute_plan_id` parameter. Whenever a query executes, the execution plan used by the query is assigned an identifier and the same identifier is used by subsequent executions of the same plan.

The `aurora_compute_plan_id` is turned `OFF` by default in DB parameter group from Aurora PostgreSQL versions 14.10, 15.5, and higher versions. To assign a plan identifier, set `aurora_compute_plan_id` to `ON` in the parameter group.

This plan identifier is used in several utilities that serve a different purpose.

You can monitor query peak memory usage in your DB instance to detect queries contributing to high database memory use from the following versions:
+ 16.3 and all higher versions
+ 15.7 and higher versions
+ 14.12 and higher versions

Whenever a query runs, the peak memory used by the query is tracked. Queries typically run many times; the average, minimum and maximum memory usage values across all runs can be viewed for each query.

**Topics**
+ [Accessing query execution plans and peak memory using Aurora functions](#AuroraPostgreSQL.Monitoring.Query.Plans.Functions)
+ [Parameter reference for Aurora PostgreSQL query execution plans](#AuroraPostgreSQL.Monitoring.Query.Plans.Parameters)

## Accessing query execution plans and peak memory using Aurora functions
<a name="AuroraPostgreSQL.Monitoring.Query.Plans.Functions"></a>

With `aurora_compute_plan_id`, you can access the execution plans using the following functions:
+ aurora\_stat\_activity
+ aurora\_stat\_plans

The query peak memory does not include memory that is allocated before query processing starts. Peak memory usage is tracked and reported separately for the planning and execution phases of each query.

![Understanding query peak memory.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-apg-peakmemory.png)


You can access the query peak memory statistics using the following functions:
+ aurora\_stat\_statements
+ aurora\_stat\_plans

For more information on these functions, see [Aurora PostgreSQL functions reference](Appendix.AuroraPostgreSQL.Functions.md).

## Parameter reference for Aurora PostgreSQL query execution plans
<a name="AuroraPostgreSQL.Monitoring.Query.Plans.Parameters"></a>

You can monitor the query execution plans using the below parameters in a DB parameter group. 

**Topics**
+ [aurora\_compute\_plan\_id](#aurora.compute_plan_id)
+ [aurora\_stat\_plans.minutes\_until\_recapture](#aurora.minutes_until_recapture)
+ [aurora\_stat\_plans.calls\_until\_recapture](#aurora.calls_until_recapture)
+ [aurora\_stat\_plans.with\_costs](#aurora.with_costs)
+ [aurora\_stat\_plans.with\_analyze](#aurora.with_analyze)
+ [aurora\_stat\_plans.with\_timing](#aurora.with_timing)
+ [aurora\_stat\_plans.with\_buffers](#aurora.with_buffers)
+ [aurora\_stat\_plans.with\_wal](#aurora.with_wal)
+ [aurora\_stat\_plans.with\_triggers](#aurora.with_triggers)

**Note**  
The configuration for `aurora_stat_plans.with_*` parameters takes effect only for newly captured plans.

### aurora\_compute\_plan\_id
<a name="aurora.compute_plan_id"></a>

The `aurora_compute_plan_id` is a configuration parameter that controls whether a plan identifier is assigned during query execution.



- **off**
  - **Allowed values:** 0(off) / **Description:** Set to off to prevent a plan identifier from being assigned.
  - **Allowed values:** 1(on) / **Description:** Set to on to assign a plan identifier.



### aurora\_stat\_plans.minutes\_until\_recapture
<a name="aurora.minutes_until_recapture"></a>

The number of minutes to pass before a plan is recaptured. Default is 0 which will disable recapturing a plan. When the `aurora_stat_plans.calls_until_recapture` threshold is passed, the plan will be recaptured.


| Default | Allowed values | Description | 
| --- | --- | --- | 
| 0 | 0-1073741823 | Set the number of minutes to pass before a plan is recaptured. | 

### aurora\_stat\_plans.calls\_until\_recapture
<a name="aurora.calls_until_recapture"></a>

The number of calls to a plan before it is recaptured. Default is 0 which will disable recapturing a plan after a number of calls. When the `aurora_stat_plans.minutes_until_recapture` threshold is passed, the plan will be recaptured.


| Default | Allowed values | Description | 
| --- | --- | --- | 
| 0 | 0-1073741823 | Set the number of calls before a plan is recaptured. | 

### aurora\_stat\_plans.with\_costs
<a name="aurora.with_costs"></a>

Captures an EXPLAIN plan with estimated costs. The allowed values are `on` and `off`. The default is `on`.



- **on**
  - **Allowed values:** 0(off) / **Description:** Doesn't show estimated cost and rows for each plan node.
  - **Allowed values:** 1(on) / **Description:** Shows estimated cost and rows for each plan node.



### aurora\_stat\_plans.with\_analyze
<a name="aurora.with_analyze"></a>

Controls the EXPLAIN plan with ANALYZE. This mode is only used the first time a plan is captured. The allowed values are `on` and `off`. The default is `off`.



- **off**
  - **Allowed values:** 0(off) / **Description:** Doesn't include actual run time statistics for the plan.
  - **Allowed values:** 1(on) / **Description:** Includes actual run time statistics for the plan.



### aurora\_stat\_plans.with\_timing
<a name="aurora.with_timing"></a>

Plan timing will be captured in the explain when ANALYZE is used. The default is `on`.



- **on**
  - **Allowed values:** 0(off) / **Description:** Doesn't include actual start up time and time spent in each plan node.
  - **Allowed values:** 1(on) / **Description:** Includes actual start up time and time spent in each plan node.



### aurora\_stat\_plans.with\_buffers
<a name="aurora.with_buffers"></a>

Plan buffer usage statistics will be captured in the explain when ANALYZE is used. The default is `off`.



- **off**
  - **Allowed values:** 0(off) / **Description:** Doesn't include information on buffer usage.
  - **Allowed values:** 1(on) / **Description:** Includes information on buffer usage.



### aurora\_stat\_plans.with\_wal
<a name="aurora.with_wal"></a>

Plan wal usage statistics will be captured in the explain when ANALYZE is used. The default is `off`.



- **off**
  - **Allowed values:** 0(off) / **Description:** Doesn't include information on WAL record generation.
  - **Allowed values:** 1(on) / **Description:** Includes information on WAL record generation.



### aurora\_stat\_plans.with\_triggers
<a name="aurora.with_triggers"></a>

Plan trigger execution statistics will be captured in the explain when `ANALYZE` is used. The default is `off`.



- **off**
  - **Allowed values:** 0(off) / **Description:** Doesn't include triggers execution statistics.
  - **Allowed values:** 1(on) / **Description:** Includes triggers execution statistics.

