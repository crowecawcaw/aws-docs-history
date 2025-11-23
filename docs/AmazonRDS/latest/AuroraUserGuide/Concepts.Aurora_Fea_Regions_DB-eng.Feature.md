# Supported Regions and Aurora DB engines for Blue/Green

Deployments

A blue/green deployment copies a production database environment in a separate,
synchronized staging environment. By using Amazon RDS Blue/Green Deployments, you can make
changes to the database in the staging environment without affecting the production
environment. For example, you can upgrade the major or minor DB engine version, change
database parameters, or make schema changes in the staging environment. When you are
ready, you can promote the staging environment to be the new production database
environment. For more information, see [Using Amazon Aurora Blue/Green Deployments
for database updates](blue-green-deployments.md "blue-green-deployments.md").

## Blue/Green Deployments with Aurora MySQL

The Blue/Green Deployments feature is available for all versions of Aurora MySQL in
all AWS Regions, including Aurora MySQL clusters configured as Aurora Global Database.

## Blue/Green Deployments with Aurora PostgreSQL

The following Regions and engine versions are available for
Blue/Green Deployments with Aurora PostgreSQL, including Aurora PostgreSQL clusters configured as Aurora Global Database.

| Region          | Aurora PostgreSQL 17    | Aurora PostgreSQL 16    | Aurora PostgreSQL 15    | Aurora PostgreSQL 14    | Aurora PostgreSQL 13     | Aurora PostgreSQL 12     | Aurora PostgreSQL 11     |
| --------------- | ----------------------- | ----------------------- | ----------------------- | ----------------------- | ------------------------ | ------------------------ | ------------------------ |
| All AWS Regions | Version 17.4 and higher | Version 16.1 and higher | Version 15.4 and higher | Version 14.9 and higher | Version 13.12 and higher | Version 12.16 and higher | Version 11.21 and higher |
