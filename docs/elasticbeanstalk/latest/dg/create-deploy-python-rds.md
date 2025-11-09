# Adding an Amazon RDS DB instance to your Python Elastic Beanstalk environment

This topic provides instructions to create an Amazon RDS using the Elastic Beanstalk console.
You can use an Amazon Relational Database Service (Amazon RDS) DB instance to store data gathered and modified by your
application. The database can be coupled to your environment and managed by Elastic Beanstalk, or it can be created as decoupled
and managed externally by another service.
In these instructions the database is coupled to your environment and managed by Elastic Beanstalk. For more information about integrating an Amazon RDS with
Elastic Beanstalk, see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

###### Sections

- [Adding a DB instance to your environment](#python-rds-create "#python-rds-create")
- [Downloading a driver](#python-rds-drivers "#python-rds-drivers")
- [Connecting to a database](#python-rds-connect "#python-rds-connect")

## Adding a DB instance to your environment

###### To add a DB instance to your environment

1. Open the [Elastic Beanstalk console](https://console.aws.amazon.com/elasticbeanstalk "https://console.aws.amazon.com/elasticbeanstalk"),
   and in the **Regions** list, select your AWS Region.
2. In the navigation pane, choose **Environments**, and then choose the name of your environment from the list.
3. In the navigation pane, choose **Configuration**.
4. In the **Database** configuration category, choose **Edit**.
5. Choose a DB engine, and enter a user name and password.
6. To save the changes choose **Apply** at the bottom of the page.

Adding a DB instance takes about 10 minutes. When the environment update is complete, the DB instance's hostname and other connection information are
available to your application through the following environment properties:

| Property name  | Description                                                                                    | Property value                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `RDS_HOSTNAME` | The hostname of the DB instance.                                                               | On the **Connectivity & security\*<br>• tab on the Amazon RDS console: **Endpoint\*\*. |
| `RDS_PORT`     | The port where the DB instance accepts connections. The default value varies among DB engines. | On the **Connectivity & security\*<br>• tab on the Amazon RDS console: **Port\*\*.     |
| `RDS_DB_NAME`  | The database name, `ebdb`.                                                                     | On the **Configuration\*<br>• tab on the Amazon RDS console: **DB Name\*\*.            |
| `RDS_USERNAME` | The username that you configured for your database.                                            | On the **Configuration\*<br>• tab on the Amazon RDS console: **Master username\*\*.    |
| `RDS_PASSWORD` | The password that you configured for your database.                                            | Not available for reference in the Amazon RDS console.                                 |

For more information about configuring a database instance coupled with an Elastic Beanstalk environment,
see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

## Downloading a driver

Add the database driver to your project's [requirements file](python-configuration-requirements.md "python-configuration-requirements.md").

###### Example requirements.txt – Django with MySQL

```
Django==2.2
`mysqlclient==2.0.3`
```

###### Common driver packages for Python

- **MySQL** – `mysqlclient`
- **PostgreSQL** – `psycopg2`
- **Oracle** – `cx_Oracle`
- **SQL Server** – `adodbapi`

For more information see
[Python DatabaseInterfaces](https://wiki.python.org/moin/DatabaseInterfaces "https://wiki.python.org/moin/DatabaseInterfaces") and
[Django 2.2 - supported databases](https://docs.djangoproject.com/en/2.2/ref/databases "https://docs.djangoproject.com/en/2.2/ref/databases").

## Connecting to a database

Elastic Beanstalk provides connection information for attached DB instances in environment properties. Use
`os.environ['`VARIABLE`']` to read the properties and configure a database connection.

###### Example Django settings file – DATABASES dictionary

```
import os

if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
```
