# Adding an Amazon RDS DB instance to your PHP Elastic Beanstalk environment

This topic provides instructions to create an Amazon RDS using the Elastic Beanstalk console.
You can use an Amazon Relational Database Service (Amazon RDS) DB instance to store data gathered and modified by your
application. The database can be coupled to your environment and managed by Elastic Beanstalk, or it can be created as decoupled
and managed externally by another service.
In these instructions the database is coupled to your environment and managed by Elastic Beanstalk. For more information about integrating an Amazon RDS with
Elastic Beanstalk, see [Adding a database to your Elastic Beanstalk environment](using-features.managing.md "using-features.managing.md").

###### Sections

- [Adding a DB instance to your environment](#php-rds-create "#php-rds-create")
- [Downloading a driver](#php-rds-drivers "#php-rds-drivers")
- [Connecting to a database with a PDO or MySQLi](#php-rds-connect "#php-rds-connect")
- [Connecting to a database with Symfony](#php-rds-symfony "#php-rds-symfony")

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

To use PHP Data Objects (PDO) to connect to the database, install the driver that matches the database engine that you chose.

- **MySQL** – [`PDO_MYSQL`](http://php.net/manual/en/ref.pdo-mysql.php "http://php.net/manual/en/ref.pdo-mysql.php")
- **PostgreSQL** – [`PDO_PGSQL`](http://php.net/manual/en/ref.pdo-pgsql.php "http://php.net/manual/en/ref.pdo-pgsql.php")
- **Oracle** – [`PDO_OCI`](http://php.net/manual/en/ref.pdo-oci.php "http://php.net/manual/en/ref.pdo-oci.php")
- **SQL Server** – [`PDO_SQLSRV`](http://php.net/manual/en/ref.pdo-sqlsrv.php "http://php.net/manual/en/ref.pdo-sqlsrv.php")

For more information, see [http://php.net/manual/en/pdo.installation.php](http://php.net/manual/en/pdo.installation.php "http://php.net/manual/en/pdo.installation.php").

## Connecting to a database with a PDO or MySQLi

You can use `$_SERVER[``VARIABLE``]` to read connection information from the environment.

For a PDO, create a Data Source Name (DSN) from the host, port, and name. Pass the DSN to the [constructor for the PDO](https://php.net/manual/en/pdo.construct.php "https://php.net/manual/en/pdo.construct.php") with the database user name and password.

###### Example Connect to an RDS database with PDO - MySQL

```
<?php
$dbhost = $_SERVER['RDS_HOSTNAME'];
$dbport = $_SERVER['RDS_PORT'];
$dbname = $_SERVER['RDS_DB_NAME'];
$charset = 'utf8' ;

$dsn = "`mysql`:host={$dbhost};port={$dbport};dbname={$dbname};charset={$charset}";
$username = $_SERVER['RDS_USERNAME'];
$password = $_SERVER['RDS_PASSWORD'];

$pdo = new PDO($dsn, $username, $password);
?>
```

For other drivers, replace `mysql` with the name of your driver – `pgsql`, `oci`, or
`sqlsrv`.

For MySQLi, pass the hostname, user name, password, database name, and port to the `mysqli` constructor.

###### Example Connect to an RDS database with mysqli_connect()

```
$link = new mysqli($_SERVER['RDS_HOSTNAME'], $_SERVER['RDS_USERNAME'], $_SERVER['RDS_PASSWORD'], $_SERVER['RDS_DB_NAME'], $_SERVER['RDS_PORT']);
```

## Connecting to a database with Symfony

For Symfony version 3.2 and newer, you can use `%env(`PROPERTY_NAME`)%` to set database parameters in a
configuration file based on the environment properties set by Elastic Beanstalk.

###### Example app/config/parameters.yml

```
parameters:
    database_driver:   pdo_mysql
    database_host:     '%env(RDS_HOSTNAME)%'
    database_port:     '%env(RDS_PORT)%'
    database_name:     '%env(RDS_DB_NAME)%'
    database_user:     '%env(RDS_USERNAME)%'
    database_password: '%env(RDS_PASSWORD)%'
```

See [External Parameters (Symfony 3.4)](http://symfony.com/doc/3.4/configuration/external_parameters.html "http://symfony.com/doc/3.4/configuration/external_parameters.html") for more
information.

For earlier versions of Symfony, environment variables are only accessible if they start with `SYMFONY__`. This means that the
Elastic Beanstalk-defined environment properties are not accessible, and you must define your own environment properties to pass the connection information to
Symfony.

To connect to a database with Symfony 2, [create an environment property](create_deploy_PHP.md#php-console-properties "create_deploy_PHP.md#php-console-properties") for each parameter. Then, use
`%`property.name`%` to access the Symfony-transformed variable in a configuration file. For example, an
environment property named `SYMFONY__DATABASE__USER` is accessible as `database.user`.

```
    database_user:     "%database.user%"
```

See [External Parameters (Symfony 2.8)](http://symfony.com/doc/2.8/configuration/external_parameters.html "http://symfony.com/doc/2.8/configuration/external_parameters.html") for more
information.
