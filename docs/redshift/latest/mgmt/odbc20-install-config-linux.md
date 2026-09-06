

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Using an Amazon Redshift ODBC driver on Linux
<a name="odbc20-install-config-linux"></a>

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift data warehouse. For each computer where you install the driver, there are the following minimum requirements: 
+ Root access on the machine.
+ One of the following distributions:
  + Amazon Linux 2
  + Amazon Linux 2023
  + Red Hat® Enterprise Linux® (RHEL) 8 or later
  + CentOS 8 or later
  + Debian 11 or later
+ 150 MB of available disk space.
+ unixODBC 2.2.14 or later.
+ glibc 2.26 or later.