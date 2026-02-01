Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Using an Amazon Redshift ODBC driver on Microsoft

Windows

You must install the Amazon Redshift ODBC driver on client computers accessing an Amazon Redshift
data warehouse. For each computer where you install the driver, there are the following
minimum requirements:

- Administrator rights on the machine.
- The machine meets the following system requirements:
  - One of the following operating systems:
    - Windows 10 or 8.1.
    - Windows Server 2019, 2016, or 2012.

  - 100 MB of available disk space.
  - Visual C++ Redistributable for Visual Studio 2015 for 64-bit Windows
    installed. You can download the installation package at [Download Visual C++ Redistributable for Visual Studio 2022](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022 "https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022")
    on the Microsoft website.
