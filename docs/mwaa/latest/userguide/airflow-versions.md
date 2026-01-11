# Apache Airflow versions on Amazon Managed Workflows for Apache Airflow

This topic describes the Apache Airflow versions Amazon Managed Workflows for Apache Airflow supports, and best-practices for upgrading to the latest version.

###### Topics

- [About Amazon MWAA versions](#airflow-versions-image "#airflow-versions-image")
- [Latest version](#airflow-versions-latest "#airflow-versions-latest")
- [Apache Airflow versions](#airflow-versions-official "#airflow-versions-official")
- [Apache Airflow components](#airflow-versions-components "#airflow-versions-components")
- [Upgrading the Apache Airflow version](#airflow-versions-upgrade "#airflow-versions-upgrade")
- [Downgrading the Apache Airflow version](#airflow-versions-downgrade "#airflow-versions-downgrade")
- [Apache Airflow deprecated versions](#airflow-versions-deprecation "#airflow-versions-deprecation")
- [Apache Airflow version support and FAQ](#airflow-versions-support "#airflow-versions-support")

## About Amazon MWAA versions

Amazon MWAA builds container images that bundle Apache Airflow releases with other common binaries and Python libraries. The image uses the Apache Airflow base install for the version you specify. When you create an environment, you specify an image version to use. Once an environment is created, it keeps using the specified image version until you upgrade it to a later version.

## Latest version

Amazon MWAA supports more than one Apache Airflow version. If you don't specify an image version when you create an environment, Amazon MWAA creates an environment using the latest supported version of Apache Airflow.

## Apache Airflow versions

The following Apache Airflow versions are supported on Amazon Managed Workflows for Apache Airflow.

###### Note

- Effective December 30, 2025, Amazon MWAA will end support for Apache Airflow versions v2.4.3, v2.5.1,
  and v2.6.3. For more information, refer to [Apache Airflow version support and FAQ](#airflow-versions-support "#airflow-versions-support").
- Beginning with Apache Airflow v2.2.2, Amazon MWAA supports installing Python requirements, provider
  packages, and custom plugins directly on the Apache Airflow webserver.
- Beginning with Apache Airflow v2.7.2, your requirements file must include a `--constraint` statement. If you don't provide a constraint, Amazon MWAA will specify
  one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you're using.

For more information about setting up constraints in your requirements file, refer to
[Installing Python dependencies](working-dags-dependencies.md#working-dags-dependencies-syntax-create "working-dags-dependencies.md#working-dags-dependencies-syntax-create").

| Apache Airflow version                                                                                                   | Apache Airflow release date                                                                                                                                                                                                  | Amazon MWAA availability date | Apache Airflow constraints                                                                                                                                                                                      | Python version                                                                       |
| ------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| [v2.11.0](https://airflow.apache.org/docs/apache-airflow/2.11.0 "https://airflow.apache.org/docs/apache-airflow/2.11.0") | [May 20, 2025](https://airflow.apache.org/docs/apache-airflow/2.11.0/release_notes.html#airflow-2-11-0-2022-05-20 "https://airflow.apache.org/docs/apache-airflow/2.11.0/release_notes.html#airflow-2-11-0-2022-05-20")      | January 7, 2026               | [v2.11.0 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.11.0/constraints-3.12.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.11.0/constraints-3.12.txt") | [Python 3.12](https://peps.python.org/pep-0693/ "https://peps.python.org/pep-0693/") |
| [v3.0.6](https://airflow.apache.org/docs/apache-airflow/3.0.6 "https://airflow.apache.org/docs/apache-airflow/3.0.6")    | [August 29, 2025](https://airflow.apache.org/docs/apache-airflow/3.0.6/release_notes.html#airflow-3-0-6-2025-08-29 "https://airflow.apache.org/docs/apache-airflow/3.0.6/release_notes.html#airflow-3-0-6-2025-08-29")       | October 1, 2025               | [v3.0.6 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt "https://raw.githubusercontent.com/apache/airflow/constraints-3.0.6/constraints-3.12.txt")    | [Python 3.12](https://peps.python.org/pep-0693/ "https://peps.python.org/pep-0693/") |
| [v2.10.3](https://airflow.apache.org/docs/apache-airflow/2.10.3 "https://airflow.apache.org/docs/apache-airflow/2.10.3") | [November 4, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.3/release_notes.html#airflow-2-10-3-2024-11-04 "https://airflow.apache.org/docs/apache-airflow/2.10.3/release_notes.html#airflow-2-10-3-2024-11-04")  | December 18, 2024             | [v2.10.3 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.3/constraints-3.11.txt") | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.10.1](https://airflow.apache.org/docs/apache-airflow/2.10.1 "https://airflow.apache.org/docs/apache-airflow/2.10.1") | [September 5, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-10-1-2024-09-05 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-10-1-2024-09-05") | September 26, 2024            | [v2.10.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.1/constraints-3.11.txt") | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.9.2](https://airflow.apache.org/docs/apache-airflow/2.9.2 "https://airflow.apache.org/docs/apache-airflow/2.9.2")    | [June 10, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-9-2-2024-06-10 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-9-2-2024-06-10")       | July 9, 2024                  | [v2.9.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.9.2/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.8.1](https://airflow.apache.org/docs/apache-airflow/2.8.1 "https://airflow.apache.org/docs/apache-airflow/2.8.1")    | [January 19, 2024](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-8-1-2024-01-19 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-8-1-2024-01-19")    | February 23, 2024             | [v2.8.1 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.8.1/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |
| [v2.7.2](https://airflow.apache.org/docs/apache-airflow/2.7.2 "https://airflow.apache.org/docs/apache-airflow/2.7.2")    | [October 12, 2023](https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-7-2-2023-10-12 "https://airflow.apache.org/docs/apache-airflow/2.10.1/release_notes.html#airflow-2-7-2-2023-10-12")    | November 6, 2023              | [v2.7.2 constraints file](https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt")    | [Python 3.11](https://peps.python.org/pep-0664/ "https://peps.python.org/pep-0664/") |

For more information about migrating your self-managed Apache Airflow deployments, or migrating an existing Amazon MWAA environment, including instructions for backing up your metadata database, refer to the [Amazon MWAA Migration Guide](../migrationguide/index.md "../migrationguide/index.md").

## Apache Airflow components

This section describes the number of Apache Airflow schedulers and workers available for each Apache Airflow version on Amazon MWAA, and provides a list of key Apache Airflow features, indicating the version
that supports each feature.

### Schedulers

Schedulers for Apache Airflow v2 and later:

| Scheduler (default) | Scheduler (min) | Scheduler (max) |
| ------------------- | --------------- | --------------- |
| 2                   | 2               | 5               |

### Workers

Workers for Apache Airflow v2 and later:

| Workers (default) | Workers (min) | Workers (max) |
| ----------------- | ------------- | ------------- |
| 10                | 1             | 25            |

## Upgrading the Apache Airflow version

Amazon MWAA supports minor version upgrades. This means you can upgrade your environment from version `x.**1**.z` to `x.**2**.z`, but not to a new major version, for example, from `**1**.y.z` to `**2**.y.z`.

For more information, and detailed instructions on updating your workflow resources, and upgrading the environment to a new version, refer to [Changing the Apache Airflow version](upgrading-environment.md "upgrading-environment.md").

## Downgrading the Apache Airflow version

Amazon MWAA supports minor version downgrades to an earlier version that is still supported at the time of downgrade. This means you can downgrade your environment from version `x.**2**.z` to `x.**1**.z`, but not to a previous major version, for example, from `**2**.y.z` to `**1**.y.z`.

For more information, and detailed instructions on updating your workflow resources, and upgrading the environment to a new version, refer to [Changing the Apache Airflow version](upgrading-environment.md "upgrading-environment.md").

## Apache Airflow deprecated versions

The following table lists the deprecated versions of Apache Airflow in Amazon MWAA, along with initial release and end-of-support dates for each version. For more information about migrating to a newer version, refer to the [Amazon MWAA Migration Guide](../migrationguide/about-mwaa-migration.md "../migrationguide/about-mwaa-migration.md").

| Apache Airflow version | Apache Airflow release date | Amazon MWAA availability date | Amazon MWAA end-of-support date |
| ---------------------- | --------------------------- | ----------------------------- | ------------------------------- |
| v1.10.12               | August 25, 2020             | November 24, 2020             | February 21, 2024               |
| v2.0.2                 | April 19, 2021              | May 25, 2021                  | April 29, 2024                  |
| v2.2.2                 | November 15, 2021           | January 27,2022               | June 27, 2024                   |
| v2.4.3                 | November 14, 2022           | January 05, 2023              | December 30, 2025               |
| v2.5.1                 | January 20, 2023            | April 11, 2023                | December 30, 2025               |
| v2.6.3                 | July 10, 2023               | August 09, 2023               | December 30, 2025               |

## Apache Airflow version support and FAQ

In accordance with the Apache Airflow community [release process and version policy](https://airflow.apache.org/docs/apache-airflow/stable/release-process.html "https://airflow.apache.org/docs/apache-airflow/stable/release-process.html"), Amazon MWAA is committed to supporting at least three minor versions of Apache Airflow at any given time. We will announce the end of support date of a given Apache Airflow minor version at least 180 days before the end of support date.

### Frequently asked questions

###### Q: How long does Amazon MWAA support an Apache Airflow version?

A: Amazon MWAA supports an Apache Airflow patch version for a minimum of 12 months after first being available.

###### Q: Am I notified when support is ending for an Apache Airflow version on Amazon MWAA?

A: Yes. If any Amazon MWAA environments in your account run the version nearing the end of support, Amazon MWAA sends out a notice through the AWS Health Dashboard with the end of support date.

###### Q: What happens on the end of support date?

A: On the end of support date, you can no longer use a deprecated version to create new Amazon MWAA environments. You can continue to access your existing Amazon MWAA environments that run the associated, deprecated version of Apache Airflow at your own risk. To upgrade to a newer version of Apache Airflow on Amazon MWAA, refer to the [Amazon MWAA Migration Guide](../migrationguide/index.md "../migrationguide/index.md").

###### Important

You are responsible for keeping your Amazon MWAA versions current. AWS urges all customers to upgrade their Amazon MWAA environments to the latest version to benefit from the most current security, privacy, and availability safeguards. If you operate your environment on an unsupported version or software past the deprecation date, referred to as the _legacy version_, you face a greater likelihood of security, privacy, and operational risks, including downtime events. By operating your Amazon MWAA environment on a legacy version, you confirm that you understand and knowingly assume these risks, and you agree to complete your upgrade to the latest version as soon as possible. Continued operation of your environment on a legacy version is subject to the agreement governing your use of the AWS services.

Legacy versions are not considered generally available, and AWS no longer provides support for the legacy version. As a result, AWS might place limits on the access to or use of any legacy version at any time, if AWS determines that the legacy version poses a security or liability risk, or a risk of harm, to the services, AWS, its Affiliates, or any other third party. Your decision to continue running Your workloads on a legacy version might result in Your content becoming unavailable, corrupted, or unrecoverable. Environments running on a legacy version are subject to Service Level Agreement (SLA) exceptions.

Environments, and related software, running on a legacy version might contain bugs, errors, defects, and harmful components. Accordingly, and notwithstanding any information to the contrary in the agreement, or the terms of service, AWS provides the legacy version _as is_.

For more information about AWS's shared responsibility model, refer to [Shared responsibility](../../../wellarchitected/latest/security-pillar/shared-responsibility.md "../../../wellarchitected/latest/security-pillar/shared-responsibility.md") in the
_AWS Well-Architected Framework_.
