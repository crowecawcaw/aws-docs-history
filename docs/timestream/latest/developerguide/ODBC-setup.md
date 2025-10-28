For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Setting up the Timestream for LiveAnalytics ODBC driver

## Set up access to Timestream for LiveAnalytics in your AWS account

If you haven't already set up your AWS account to work with Timestream for LiveAnalytics, follow the
insructions in [Accessing Timestream for LiveAnalytics](accessing.md "accessing.md").

## Install the ODBC driver on your system

Download the appropriate Timestream ODBC driver installer for your system from the
[ODBC GitHub
repository](https://github.com/awslabs/amazon-timestream-odbc-driver/releases "https://github.com/awslabs/amazon-timestream-odbc-driver/releases"), and follow the installation instructions that apply to your system:.

- [Windows installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-installation-guide.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-installation-guide.md")
- [MacOS installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-installation-guide.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-installation-guide.md")
- [Linux installation guide](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-installation-guide.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-installation-guide.md")

## Set up a data source name (DSN) for the ODBC driver

Follow the instructions in the DSN configuration guide for your system:

- [Windows DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-dsn-configuration.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/windows-dsn-configuration.md")
- [MacOS DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-dsn-configuration.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/macOS-dsn-configuration.md")
- [Linux DSN configuration](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-dsn-configuration.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/linux-dsn-configuration.md")

## Set up your business intelligence (BI) application to work with the ODBC driver

Here are instructions for setting several common BI applications to work with the ODBC driver:

- [Setting up Microsoft Power BI.](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-power-bi.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-power-bi.md")
- [Setting up Microsoft Excel](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-excel.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/microsoft-excel.md")
- [Setting up Tableau](https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/tableau.md "https://github.com/awslabs/amazon-timestream-odbc-driver/blob/main/docs/markdown/setup/tableau.md")

For other applications
