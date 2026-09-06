

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Using an Amazon Redshift ODBC driver on Microsoft Windows
<a name="odbc20-install-config-win"></a>

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift data warehouse. For each computer where you install the driver, there are the following minimum requirements: 
+ Administrator rights on the machine. 
+ The machine meets the following system requirements:
  + One of the following operating systems:
    + Windows 10 or 8.1.
    + Windows Server 2025, 2022, 2019, 2016, or 2012.
  + 100 MB of available disk space.
  + Visual C\+\+ Redistributable for Visual Studio 2015 for 64-bit Windows installed. You can download the installation package at [ Download Visual C\+\+ Redistributable for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022) on the Microsoft website.