# Preparing a CEV for RDS for SQL Server

## Prerequisites

Before creating a custom engine version, make sure you have completed the following prerequisites:

### Prepare SQL Server Developer Edition installation media

You must obtain the SQL Server Developer Edition installation media from Microsoft and prepare it for upload to S3.

###### To download installation media from Microsoft

1. **Option A:** Use your [Visual Studio subscription](https://visualstudio.microsoft.com/subscriptions/ "https://visualstudio.microsoft.com/subscriptions/") to download the Developer Edition ISO. Only the English version is supported.
2. **Option B: Using SQL Server Installer**
   1. Download the [SQL Server Developer Edition installer](https://download.microsoft.com/download/c/c/9/cc9c6797-383c-4b24-8920-dc057c1de9d3/SQL2022-SSEI-Dev.exe "https://download.microsoft.com/download/c/c/9/cc9c6797-383c-4b24-8920-dc057c1de9d3/SQL2022-SSEI-Dev.exe").
   2. Run the installer and choose **Download Media** to download the full ISO.
   3. Choose **English** as the preferred language.
   4. Choose **ISO** as the media type.
   5. Choose **Download**.

###### To download cumulative updates

1. Visit the [Microsoft Catalog Update](https://www.catalog.update.microsoft.com/Home.aspx "https://www.catalog.update.microsoft.com/Home.aspx") page.
2. Find a SQL Server Developer Edition supported by RDS for SQL Server, for example "SQL Server 2022 Cumulative Update".
3. Download the latest supported CU executable file and save it to your machine.
4. Example files: `SQLServer2022-KB5065865-x64.exe` (CU21 for SQL Server 2022)

###### Important

RDS for SQL Server only supports specific Cumulative Update (CU) versions. You must use the exact version listed in the table below. Do not use newer CU versions even if available from Microsoft, as they may not be compatible with RDS.

Alternatively, you can also download the required Cumulative Update (CU) file directly from the following:

The following table lists the supported SQL Server Developer Edition version and its corresponding Cumulative Update for use with RDS:

| SQL Server Version | Supported CU | KB Article                                                                                                                                                                                                                                                                                                                                                 | Download File Name                |
| ------------------ | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- |
| SQL Server 2022    | `CU21`       | [KB5065865](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate21 "https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate21")                                                                                                                                                 | `SQLServer2022-KB5065865-x64.exe` |
| SQL Server 2019    | `CU32 GDR`   | [KB5068404](https://support.microsoft.com/en-us/topic/kb5068404-description-of-the-security-update-for-sql-server-2019-cu32-november-11-2025-c203bfbf-036e-46d2-bc10-6c01200dc48a "https://support.microsoft.com/en-us/topic/kb5068404-description-of-the-security-update-for-sql-server-2019-cu32-november-11-2025-c203bfbf-036e-46d2-bc10-6c01200dc48a") | `SQLServer2019-KB5068404-x64.exe` |
