# Apache Airflow provider packages installed on Amazon MWAA environments

This page lists the Apache Airflow provider packages installed by Amazon MWAA for all supported Apache Airflow environments. For more information about these packages, refer to the [Apache Airflow reference for package extras](https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html "https://airflow.apache.org/docs/apache-airflow/stable/extra-packages-ref.html").

###### Note

To ensure that compatibility with CloudWatch logging is not overridden by other Python library installations, Amazon MWAA installs [Watchtower version 2.0.1](https://pypi.org/project/watchtower/2.0.1/ "https://pypi.org/project/watchtower/2.0.1/") after performing `pip3 install -r requirements.txt`.

###### Topics

- [Constraints file](#connections-packages-constraints "#connections-packages-constraints")
- [Version-specific provider packages](#connections-packages-table "#connections-packages-table")

## Constraints file

Beginning with Apache Airflow v2.7.2, your requirements file must include a `--constraint` statement. If you don't provide a constraint, Amazon MWAA will specify one for you to ensure the packages listed in your requirements are compatible with the version of Apache Airflow you're using.

Apache Airflow constraints files specify the provider versions available at the time of an Apache Airflow release. In many cases, however, newer providers are compatible with that version of Apache Airflow. Because you must use constraints, to specify a newer version of a provider package, you can modify the constraints file for a specific provider version:

1. Download the version-specific constraints file from GitHub, for example
   [https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt](https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt "https://raw.githubusercontent.com/apache/airflow/constraints-2.7.2/constraints-3.11.txt") (replace '2.7.2' with the version you want to use).
2. Save the modified constraints file to the Amazon S3 dags folder of your Amazon MWAA environment, for example, as `constraints-3.11-updated.txt`.
3. Specify your requirements as listed in the following.

```
--constraint "/usr/local/airflow/dags/constraints-3.11-updated.txt"
apache-airflow-providers-amazon==``version-number``
```

###### Note

If you are using a private webserver, we recommend that you [package the required libraries as WHL files](best-practices-dependencies.md#best-practices-dependencies-python-wheels "best-practices-dependencies.md#best-practices-dependencies-python-wheels") by using [aws-mwaa-docker-images](https://github.com/aws/amazon-mwaa-docker-images "https://github.com/aws/amazon-mwaa-docker-images").

## Version-specific provider packages

Installing provider packages you can use to access a connection type in the Apache Airflow UI. It also means you don't need to specify these packages as a Python dependency in your `requirements.txt` file. This page lists the Apache Airflow provider packages installed by Amazon MWAA for all supported Apache Airflow environments.

###### Note

For Apache Airflow v2 and later, Amazon MWAA installs [Watchtower version 2.0.1](https://pypi.org/project/watchtower/2.0.1/ "https://pypi.org/project/watchtower/2.0.1/") after performing `pip3 install -r requirements.txt`, to ensure compatibility with CloudWatch logging is not overridden by other Python library installations.

You can specify the latest supported version of `apache-airflow-providers-amazon` to upgrade this provider.

**Supported Apache Airflow versions:**

v3.0.6

| Connection type     | Package                                                                                                                                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==9.9.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.9.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.9.0/index.html")    |
| Postgres Connection | [apache-airflow-providers-postgres==6.2.1](https://airflow.apache.org/docs/apache-airflow-providers-postgres/6.2.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/6.2.1/index.html")           |
| FTP Connection      | [apache-airflow-providers-ftp==3.13.1](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.13.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.13.1/index.html")                       |
| Fab Connection      | [apache-airflow-providers-fab==2.3.0](https://airflow.apache.org/docs/apache-airflow-providers-fab/2.3.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-fab/2.3.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.12.1](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.12.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.12.1/index.html")              |
| HTTP Connection     | [apache-airflow-providers-http==5.3.2](https://airflow.apache.org/docs/apache-airflow-providers-http/5.3.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/5.3.2/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.9.1](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.9.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.9.1/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.27.3](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.27.3/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.27.3/index.html")  |
| SQLite Connection   | [apache-airflow-providers-sqlite==4.1.1](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/4.1.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/4.1.1/index.html")                 | v2.10.3 |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==9.0.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.0.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/9.0.0/index.html")    |
| Postgres Connection | [apache-airflow-providers-postgres==5.13.1](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.13.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.13.1/index.html")        |
| FTP Connection      | [apache-airflow-providers-ftp==3.11.1](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.11.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.11.1/index.html")                       |
| Fab Connection      | [apache-airflow-providers-fab==1.5.0](https://airflow.apache.org/docs/apache-airflow-providers-fab/1.5.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-fab/1.5.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.8.3](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.8.3/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.8.3/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.13.2](https://airflow.apache.org/docs/apache-airflow-providers-http/4.13.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.13.2/index.html")                    |
| IMAP Connection     | [apache-airflow-providers-imap==3.7.0](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.7.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.7.0/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.19.0](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.19.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.19.0/index.html")  |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.9.0](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.9.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.9.0/index.html")                 |
| SMTP Connection     | [apache-airflow-providers-smtp==1.8.0](https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.8.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.8.0/index.html")                       | v2.10.1 |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==8.28.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/2.28.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/2.28.0/index.html") |
| Postgres Connection | [apache-airflow-providers-postgres==5.12.0](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.12.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.12.0/index.html")        |
| FTP Connection      | [apache-airflow-providers-ftp==3.11.0](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.11.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.11.0/index.html")                       |
| Fab Connection      | [apache-airflow-providers-fab==1.3.0](https://airflow.apache.org/docs/apache-airflow-providers-fab/1.3.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-fab/1.3.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.8.1](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.8.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.8.1/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.13.0](https://airflow.apache.org/docs/apache-airflow-providers-http/4.13.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.13.0/index.html")                    |
| IMAP Connection     | [apache-airflow-providers-imap==3.7.0](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.7.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.7.0/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.16.0](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.16.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.16.0/index.html")  |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.9.0](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.9.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.9.0/index.html")                 |
| SMTP Connection     | [apache-airflow-providers-smtp==1.8.0](https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.8.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.8.0/index.html")                       | v2.9.2  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==8.24.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.24.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.24.0/index.html") |
| Postgres Connection | [apache-airflow-providers-postgres==5.11.1](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.11.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.11.1/index.html")        |
| FTP Connection      | [apache-airflow-providers-ftp==3.9.1](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.9.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.9.1/index.html")                          |
| Fab Connection      | [apache-airflow-providers-fab==1.1.1](https://airflow.apache.org/docs/apache-airflow-providers-fab/1.1.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-fab/1.1.1/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.7.2](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.7.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.7.2/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.11.1](https://airflow.apache.org/docs/apache-airflow-providers-http/4.11.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.11.1/index.html")                    |
| IMAP Connection     | [apache-airflow-providers-imap==3.6.1](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.6.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.6.1/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.14.0](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.14.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.14.0/index.html")  |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.8.1](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.8.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.8.1/index.html")                 |
| SMTP Connection     | [apache-airflow-providers-smtp==1.7.1](https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.7.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-smtp/1.7.1/index.html")                       | v2.8.1  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==8.16.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.16.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.16.0/index.html") |
| Postgres Connection | [apache-airflow-providers-postgres==5.10.0](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.10.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.10.0/index.html")        |
| FTP Connection      | [apache-airflow-providers-ftp==3.7.0](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.7.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.7.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.5.1](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.5.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.5.1/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.8.0](https://airflow.apache.org/docs/apache-airflow-providers-http/4.8.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.8.0/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.5.0](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.5.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.5.0/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.10.0](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.10.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.10.0/index.html")  |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.7.0](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.7.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.7.0/index.html")                 | v2.7.2  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==8.7.1](https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.7.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.7.1/index.html")    |
| Postgres Connection | [apache-airflow-providers-postgres==5.6.1](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.6.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.6.1/index.html")           |
| FTP Connection      | [apache-airflow-providers-ftp==3.5.2](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.5.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.5.2/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.3.4](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.3.4/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.3.4/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.5.2](https://airflow.apache.org/docs/apache-airflow-providers-http/4.5.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.5.2/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.3.2](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.3.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.3.2/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.7.2](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.7.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.7.2/index.html")     |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.4.3](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.4.3/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.4.3/index.html")                 | v2.6.3  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon[aiobotocore]==8.2.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.2.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/8.2.0/index.html")    |
| Postgres Connection | [apache-airflow-providers-postgres==5.5.1](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.5.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.5.1/index.html")           |
| FTP Connection      | [apache-airflow-providers-ftp==3.4.2](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.4.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.4.2/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.2.1](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.2.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.2.1/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.4.2](https://airflow.apache.org/docs/apache-airflow-providers-http/4.4.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.4.2/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.2.2](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.2.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.2.2/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.5.2](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.5.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.5.2/index.html")     |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.4.2](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.4.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.4.2/index.html")                 | v2.5.1  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon==7.1.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/7.1.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/7.1.0/index.html")                 |
| Postgres Connection | [apache-airflow-providers-postgres==5.4.0](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.4.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.4.0/index.html")           |
| FTP Connection      | [apache-airflow-providers-ftp==3.3.0](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.3.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.3.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.1.0](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.1.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.1.0/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.1.1](https://airflow.apache.org/docs/apache-airflow-providers-http/4.4.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.4.1/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.1.1](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.1.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.1.1/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.3.3](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.3.3/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.3.3/index.html")     |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.3.1](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.3.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.3.1/index.html")                 | v2.4.3  |
| Connection type     | Package                                                                                                                                                                                                                       |
| ---                 | ---                                                                                                                                                                                                                           |
| AWS Connection      | [apache-airflow-providers-amazon==6.0.0](https://airflow.apache.org/docs/apache-airflow-providers-amazon/6.0.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-amazon/6.0.0/index.html")                 |
| Postgres Connection | [apache-airflow-providers-postgres==5.2.2](https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.2.2/index.html "https://airflow.apache.org/docs/apache-airflow-providers-postgres/5.2.2/index.html")           |
| FTP Connection      | [apache-airflow-providers-ftp==3.1.0](https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.1.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-ftp/3.1.0/index.html")                          |
| Celery Connection   | [apache-airflow-providers-celery==3.0.0](https://airflow.apache.org/docs/apache-airflow-providers-celery/3.0.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-celery/3.0.0/index.html")                 |
| HTTP Connection     | [apache-airflow-providers-http==4.0.0](https://airflow.apache.org/docs/apache-airflow-providers-http/4.0.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-http/4.0.0/index.html")                       |
| IMAP Connection     | [apache-airflow-providers-imap==3.0.0](https://airflow.apache.org/docs/apache-airflow-providers-imap/3.0.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-imap/3.0.0/index.html")                       |
| Common SQL          | [apache-airflow-providers-common-sql==1.2.0](https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.2.0/index.html "https://airflow.apache.org/docs/apache-airflow-providers-common-sql/1.2.0/index.html")     |
| SQLite Connection   | [apache-airflow-providers-sqlite==3.2.1](https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.2.1/index.html "https://airflow.apache.org/docs/apache-airflow-providers-sqlite/3.2.1/index.html")                 |
