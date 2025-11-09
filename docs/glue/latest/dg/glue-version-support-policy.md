# AWS Glue version support policy

AWS Glue is a serverless data integration service that makes it easy to discover, prepare, and
combine data for analytics, machine learning, and application development. An _AWS Glue
job_ contains the business logic that performs the data integration work in AWS Glue.
There are three types of jobs in AWS Glue: _Spark (batch and streaming)_,
_Ray_ and _Python shell_. When you define your job, you specify the
AWS Glue version, which configures versions in the underlying Spark, Ray or Python runtime
environment. For example: an AWS Glue version 5.0 Spark job supports Spark 3.5.4 and Python
3.11.

## Support policy

AWS Glue versions are built around a combination of operating system, programming language, and software libraries that
are subject to maintenance and security updates. AWS Glue's version support policy is to end support for a version when any
major component of the version reaches the end of community long-term support (LTS) and security updates are no longer available.
AWS Glue's version support policy includes the following statuses:

**End of Support (EOS) -** When an AWS Glue version reaches EOS:

- AWS Glue will no longer apply security patches or other updates to EOS versions.
- AWS Glue jobs on EOS versions are not eligible for technical support.
- AWS Glue may not honor SLAs when jobs are run on EOS versions.

**End of Life (EOL) -** When an AWS Glue version reaches EOL:

- You can no longer create new AWS Glue jobs or interactive sessions on EOL versions.
- You can no longer start job runs on these AWS Glue versions.
- AWS Glue will stop existing job runs and interactive sessions on EOL versions.
- EOL versions will be removed from AWS Glue SDKs and APIs.

The following AWS Glue versions have reached end of support and will no longer be available after the end of life date.
Changes to a version’s support status start at midnight (Pacific time zone) on the specified date.

| **Type**             | **Glue version**                                | **End of support** | **End of life** |
| -------------------- | ----------------------------------------------- | ------------------ | --------------- |
| Spark                | Glue version 0.9 (Spark 2.2, Scala 2, Python 2) | 6/1/2022           | 4/1/2026        |
| Spark                | Glue version 1.0 (Spark 2.4, Python 2)          | 6/1/2022           | 4/1/2026        |
| Spark                | Glue version 1.0 (Spark 2.4, Scala 2, Python 3) | 9/30/2022          | 4/1/2026        |
| Spark                | Glue version 2.0 (Spark 2.4, Python 3)          | 1/31/2024          | 4/1/2026        |
| **Type**             | **Python version**                              | **End of support** | **End of life** |
| ---                  | ---                                             | ---                | ---             |
| Python shell         | Python 2 (AWS Glue Version 1.0)                 | 6/1/2022           | 4/1/2026        |
| Python shell         | PythonShell 3.6 (Glue version 1.0)              | 3/31/2026          | NA              |
| **Type**             | **Notebook version**                            | **End of support** | **End of life** |
| ---                  | ---                                             | ---                | ---             |
| Development endpoint | Zeppelin notebook                               | 9/30/2022          | NA              |

###### Note

Creating new AWS Glue Python Shell 3.6 jobs will not be allowed once end of support is reached on
March 31, 2026, but you can continue to update and run existing jobs. However, jobs running on discontinued versions are not eligible for
technical support. AWS Glue will not apply security patches or other updates to discontinued versions. AWS Glue will also not honor SLAs when
jobs are run on discontinued versions.

AWS strongly recommends that you migrate your jobs to supported versions.

For information on migrating your Spark jobs to the latest AWS Glue version, see
[Migrating AWS Glue jobs to
AWS Glue version 5.0](migrating-version-50.md "migrating-version-50.md").

For migrating your Python shell jobs to the latest AWS Glue version:

- In the console, choose `Python 3 (Glue Version 4.0)`.
- In the [CreateJob](../webapi/API_CreateJob.md "../webapi/API_CreateJob.md")/[UpdateJob](../webapi/API_UpdateJob.md "../webapi/API_UpdateJob.md") API, set the `GlueVersion` parameter to `2.0`, and the
  `PythonVersion` to `3` under the `Command` parameter. The `GlueVersion` configuration does not
  affect the behavior of Python shell jobs, so there is no advantage to incrementing `GlueVersion`.
- You need to make your job script compatible with Python 3.
