# Logical migration from MySQL to Amazon Aurora MySQL by using

mysqldump

Because Amazon Aurora MySQL is a MySQL-compatible database, you can use the `mysqldump` utility to copy data from
your MySQL database or the `mariadb-dump` utility to copy your data from your
MariaDB database to an existing Aurora MySQL DB cluster.

For a discussion of how to do so with MySQL or MariaDB databases that are very large, see the following topics in the _Amazon Relational Database Service User
Guide_:

- MySQL – [Importing data to an Amazon RDS for MySQL database with
  reduced downtime](../UserGuide/mysql-importing-data-reduced-downtime.md "../UserGuide/mysql-importing-data-reduced-downtime.md")
- MariaDB – [Importing data to an Amazon RDS for MariaDB database with
  reduced downtime](../UserGuide/mariadb-importing-data-reduced-downtime.md "../UserGuide/mariadb-importing-data-reduced-downtime.md")
  For MySQL or MariaDB databases that have smaller amounts of data, see the following topics in the _Amazon Relational Database Service User
  Guide_:

- MySQL – [Importing data from an external MySQL database to
  an Amazon RDS for MySQL DB instance](../UserGuide/mysql-importing-data-external-database.md "../UserGuide/mysql-importing-data-external-database.md")
- MariaDB – [Importing data from an external MariaDB database to
  an Amazon RDS for MariaDB DB instance](../UserGuide/mariadb-importing-data-external-database.md "../UserGuide/mariadb-importing-data-external-database.md")
