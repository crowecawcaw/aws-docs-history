# Databases

## What are Lightsail managed

databases?

Lightsail managed databases are instances that are dedicated to running databases,
instead of other workloads like web servers, mail servers, etc. A managed database can
contain multiple user-created databases, and you can access it by using the same tools and
applications that you use with a stand-alone database. Lightsail maintains the security
and health of your database’s underlying infrastructure and operating system, so that you
can run a database without deep expertise in infrastructure management.

Like regular Lightsail instances, Lightsail managed databases come with a fixed
amount of memory, computing power, and SSD based storage in their plans that you can scale
up over time. Lightsail will automatically install and configure your chosen database for
you upon creation.

## What can I do with Lightsail

managed databases?

Lightsail managed databases provide an easy, low maintenance way to store your data in
the cloud. You can run managed databases either as a new database or by migrating from an
existing on-premises or hosted database to Lightsail.

They can also allow you to scale your application to accept larger amounts of traffic
and more intensive loads, by separating out your database into a dedicated instance.
Lightsail managed databases are especially useful for stateful applications – like
WordPress and most common CMSs – that need data to be kept in sync when you scale beyond a
single instance. Managed databases can be paired with a Lightsail load balancer and two or
more Lightsail instances to create a powerful, scaled application. By using Lightsail
high availability managed database plans, you can also add redundancy to your database,
helping to ensure high uptime for your application.

## What does Lightsail manage for

me?

Lightsail manages a range of maintenance activities and security for your managed
database and its underlying infrastructure. Lightsail automatically backs up your database
and allows point in time restore from the past 7 days using the database restore tool, to
help protect against data loss or component failure. Lightsail also automatically encrypts
your data at rest and in motion for increased security and stores your database password for
easy and secure connections to your database. On the maintenance side, Lightsail runs
maintenance on your database during your set maintenance window. This maintenance include
automatic upgrades to the latest minor database version and all management of the underlying
infrastructure and operating system.

## What kinds of databases and

what versions of these databases does Lightsail support?

Lightsail managed databases support the latest major versions of MySQL and PostgreSQL.
Currently, these versions are MySQL 5.7, MySQL 8.0, PostgreSQL 9, PostgreSQL 10, PostgreSQL
11, and PostgreSQL 12. Lightsail only provides the latest minor version for each major
version option.

## What managed database

plans does Lightsail offer?

Lightsail offers 6 sizes of managed databases in standard and high availability plans.
Each plan comes with a fixed amount of storage and a monthly allowance of data transfer. You
can also scale up to larger plans over time, as needed, and switch between standard and high
availability plans. High availability plans mirror the same resources as standard plans and
additionally include a standby database running in a separate Availability Zones from your
primary database for redundancy. For more
information about data transfer costs, see [What does data transfer cost?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost "amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost").

## What is a high availability plan?

Lightsail managed databases are available in standard and high availability plans.
Standard and high availability plans have identical plan resources, including memory,
storage, and data transfer allowance. High availability plans add redundancy and durability
to your database, by automatically creating standby database in a separate Availability Zone
from your primary database, synchronously replicating data to the standby database, and
providing failover to the standby database in case of infrastructure failure and during
maintenance so that you ensure uptime even when databases is being automatically
upgraded/maintained by Lightsail. Use high availability plans for running production
applications or software where high uptime is required.

## How do I scale up or down my

Lightsail managed database?

You can scale up your Lightsail managed database by taking a snapshot of it and
creating a new, larger database plan from snapshot or by creating a new, larger database
using the emergency restore feature. You can also switch from standard to high availability
plans and vice versa using either method. You cannot scale down your database. For more
information, see [Creating
a database from a snapshot in Lightsail](amazon-lightsail-creating-a-database-from-snapshot.md "amazon-lightsail-creating-a-database-from-snapshot.md").

## How can I back up my Lightsail managed

database?

Lightsail backs up your data automatically and allows restore of this data from a
specific point in time to a new database. Automatic backup is a free service for your
database but only saves the last 7 days of data. If you delete your database, all automatic
backup records are deleted and point-in-time restore is no longer possible. To retain
backups of data after deleting your database or to retain a backup for more than 7 days in
the past, use manual snapshots.

You can take manual snapshots of your Lightsail managed databases from the database
management pages. Manual snapshots contain all the data from your database and can be used
as backups for data that you want to store permanently. You can also use manual snapshots to
create a new, larger database or to switch between Standard and High Availability plans.
Manual snapshots are stored until you delete them and are billed at $0.05
USD/GB-month.

## What happens to my data if

I delete my Lightsail managed database?

If you delete your Lightsail managed database, both your database itself and all
automatic backups will be deleted. There is no way to recover this data unless you take a
manual snapshot before deleting your database. During deletion of your database, Lightsail
provides a one-click option to take a manual snapshot, if desired, to help protect against
accidental loss of data. Taking a manual snapshot before deletion is optional but highly
recommended. You can delete your manual snapshot in the future when you no longer need the
stored data.

## Can I connect my instance(s) to a Lightsail managed database running in different

AWS Regions or different Availability Zones?

You cannot use Lightsail managed databases with instances running in different
AWS Regions. You can, however, use databases across different Availability Zones from your
instance.

## How do I load data onto my Lightsail

managed database?

In order to load data onto your Lightsail managed database, you should first enable
data import mode. After enabling data import mode, you can continue to manually upload data
using your preferred database client. After you are done loading data, remember to turn off
Data import mode so that automatic backups and logging for your databases can resume. For
more information, see [Import data into your
MySQL database](amazon-lightsail-importing-data-into-your-mysql-database.md "amazon-lightsail-importing-data-into-your-mysql-database.md") and [Import data into
your PostgreSQL database](amazon-lightsail-importing-data-into-your-postgres-database.md "amazon-lightsail-importing-data-into-your-postgres-database.md").

## How do I access the data on my

Lightsail managed database?

You can connect to your database and query your data using any standard SQL client
application. We recommend MySQL Workbench for GUI based administration and querying. You can
find connection data in the database management screen for your database, including the
endpoint URL and DNS name. For more information, see [Connect to your MySQL
database](amazon-lightsail-connecting-to-your-mysql-database.md "amazon-lightsail-connecting-to-your-mysql-database.md") or [Connecting to your PostgreSQL database in Amazon Lightsail](amazon-lightsail-connecting-to-your-postgres-database.md "amazon-lightsail-connecting-to-your-postgres-database.md").

## How do

Lightsail managed databases work with my Lightsail instances?

After you create your Lightsail managed database, you can start using it with your
application immediately, using your Lightsail instances as web servers or other dedicated
workloads for your app. To connect your Lightsail instance to a database, use your
database endpoint and reference your securely stored password to configure the database as
your data store in the code of your application. You can find connection data in the
database management screens. The file name and location for your database configuration file
will vary by application. Note that you can connect many instances to one database, either
using the same tables or using different ones.

## How can I connect Lightsail

managed database to EC2 instances running in my AWS account?

You can connect your Lightsail managed database to EC2 instances by connecting over
the public internet. Note that connection to all AWS services will consume your database
data transfer allowance, and data out over the public internet to AWS services in excess
of your data transfer allowance will accrue overage charges. You cannot use VPC peering
between Lightsail managed databases and EC2 instances. For more
information about data transfer costs, see [What does data transfer cost?](amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost "amazon-lightsail-faq-data-transfer-allowance.md#data-transfer-allowance-what-does-data-transfer-cost").

## What is the difference between public and private modes for my Lightsail managed

database?

By default, your Lightsail managed database is created in private mode, which secures
it by making it accessible only by Lightsail instances. You can set your database public
mode if you need to connect to software or services over the public internet. To ensure
security of your data, we do not recommend keeping public mode enabled long-term. You can
change between public and private modes at any time from your database management
screens.

## Can I manage the ports used by

my Lightsail managed database?

No, Lightsail automatically manages your ports for security purposes, opening Port
3306 for MySQL for all Lightsail managed databases in public mode. If your database is in
private mode, your database is only open to resources running in your Lightsail account
via the internal network.

## Do Lightsail managed databases services

support IPv6?

Lightsail managed databases do not support IPv6.
