# Tutorial: Create a web server and an Amazon Aurora DB cluster

This tutorial shows you how to install an Apache web server with PHP and create a MariaDB, MySQL,
or PostgreSQL database. The web server runs on an Amazon EC2 instance using Amazon Linux 2023, and you
can choose between an Aurora MySQL or Aurora PostgreSQL DB cluster. Both
the Amazon EC2 instance and the DB cluster run in a virtual private cloud (VPC) based on the
Amazon VPC service.

###### Important

There's no charge for creating an AWS account. However, by completing this tutorial, you might incur
costs for the AWS resources you use. You can delete these resources after you complete the tutorial
if they are no longer needed.

###### Note

This tutorial works with Amazon Linux 2023 and might not work for other versions of Linux.

In the tutorial that follows, you create an EC2 instance that uses the default VPC, subnets, and
security group for your AWS account. This tutorial shows you how to create the
DB
cluster and automatically set up connectivity with the EC2 instance that you created.
The tutorial then shows you how to install the web server on the EC2 instance. You connect your
web server to your DB cluster
in the VPC using the DB cluster writer endpoint.

1. [Launch an EC2 instance to connect with your DB cluster](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md")
2. [Create an Amazon Aurora DB cluster](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md")
3. [Install a web server on your EC2 instance](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md")
   The following diagram shows the configuration when the tutorial is complete.

![Single VPC Scenario](images/con-VPC-sec-grp-aurora.png)

###### Note

After you complete the tutorial, there is a public and private subnet in each Availability Zone in
your VPC. This tutorial uses the default VPC for your AWS account and automatically sets up connectivity between your
EC2 instance and DB cluster.
If you would rather configure a new VPC for this scenario instead, complete the tasks in
[Tutorial: Create a VPC for use with a DB cluster (IPv4 only)](CHAP_Tutorials.WebServerDB.md "CHAP_Tutorials.WebServerDB.md").
