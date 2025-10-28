# Improved memory

management in Aurora PostgreSQL

Aurora PostgreSQL now includes advanced memory management capabilities to optimize
database performance and resilience under varying workloads. These improvements help
Aurora PostgreSQL maintain consistent availability and responsiveness, even during periods
of high memory demand.

This feature is available and enabled by default in the following Aurora PostgreSQL
versions for provisioned instances:

- 15.3 and all higher minor versions
- 14.8 and higher minor versions
- 13.11 and higher minor versions
- 12.15 and higher minor versions
- 11.20 and higher minor versions
  This feature is available and enabled by default in the following Aurora PostgreSQL for
  Aurora Serverless instances:

- 16.3 and all higher minor versions
- 15.7 and all higher minor versions
- 14.12 and higher minor versions
- 13.15 and higher minor versions
  When customer workloads use up all available free memory, the operating system may
  restart the database to protect resources, leading to temporary unavailability. The new
  memory management improvements in Aurora PostgreSQL proactively cancel certain transactions
  when the system experiences high memory pressure, helping to maintain database
  stability.

The key features of improved memory management is as follows:

- Cancelling database transactions that request more memory when the system is
  approaching critical memory pressure.
- The system is said to be under critical memory pressure, when it exhausts all
  the physical memory and is about to exhaust the swap. In these circumstances,
  any transaction that requests memory will be cancelled in an effort to
  immediately reduce memory pressure in the DB instance.
- Essential PostgreSQL launchers and background workers such as autovacuum
  workers are always protected.

## Handling memory management parameters

###### To turn on memory management

This feature is turned on by default. An error message is displayed when a
transaction is cancelled due to insufficient memory as shown in the following
example:

```
ERROR: out of memory Detail: Failed on request of size 16777216.
```

###### To turn off memory management

To turn off this feature, connect to the Aurora PostgreSQL DB cluster with psql
and use the SET statement for the parameter values as mentioned below.

###### Note

We recommend that you keep memory management enabled. This helps prevent
potential out-of-memory errors that may lead to workload-induced database
restarts due to memory exhaustion.

The following table shows how to turn off the memory management feature for the
different Aurora PostgreSQL versions:

| Aurora PostgreSQL versions                                       | Parameter                      | Default | Command to turn off memory management at session level |
| ---------------------------------------------------------------- | ------------------------------ | ------- | ------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 11.20, 11.21, 12.15, 12.16, 13.11, 13.12, 14.8, 14.9, 15.3, 15.4 | `rds.memory_allocation_guard`  | `false` | `SET rds.memory_allocation_guard = true;`              |
| 12.17, 13.13, 14.10, 15.5, and higher versions                   | `rds.enable_memory_management` | `true`  | `SET rds.enable_memory_management = false;`            | ###### Note The `rds.memory_allocation_guard` parameter has been deprecated in Aurora PostgreSQL 12.17, 13.13, 14.10, 15.5, and higher versions. Setting the values of these parameters in the DB cluster parameter group prevents the queries from being canceled. For more information about DB cluster parameter group, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). ## Limitation <br>• This feature is not supported in db.t3.medium instance class. |
