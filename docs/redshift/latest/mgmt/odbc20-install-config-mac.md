

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Using an Amazon Redshift ODBC driver on Apple macOS
<a name="odbc20-install-config-mac"></a>

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift data warehouse. For each computer where you install the driver, these are the following minimum requirements: 
+ Root access on the machine. 
+ Apple macOS System Requirements:
  + A 64-bit version of Apple macOS version 11.7 or higher (such as Apple macOS Big Sur, Monterey, Ventura or later) is required. The Redshift ODBC driver only supports 64-bit client applications.
  + 150 MB of available disk space.
  + The driver supports applications built with iODBC 3.52.9\+ or unixODBC 2.3.7\+.