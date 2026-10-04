

# Preparing a CEV for RDS for SQL Server
<a name="sqlserver-dev-edition.preparing"></a>

## Prerequisites
<a name="sqlserver-dev-prerequisites"></a>

Before creating a custom engine version, make sure you have completed the following prerequisites:

### Prepare SQL Server Developer Edition installation media
<a name="sqlserver-dev-prepare-media"></a>

You must obtain the SQL Server Developer Edition installation media from Microsoft and prepare it for upload to S3.

**To download installation media from Microsoft**

1. **Option A:** Use your [Visual Studio subscription](https://visualstudio.microsoft.com/subscriptions/) to download the Developer Edition ISO. Only the English version is supported.

1. **Option B: Using SQL Server Installer**

   1. Download the SQL Server Developer Edition installer for your target edition from the [Microsoft SQL Server Downloads](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) page:
      + **Developer Edition (Enterprise Edition capabilities)** – Download the **Developer** edition installer from the SQL Server 2025 section. The ISO file is named `SQLServer2025-x64-ENU-EntDev.iso`.
      + **Developer Edition (Standard Edition capabilities)** – Download the **Developer (Standard)** edition installer from the SQL Server 2025 section. The ISO file is named `SQLServer2025-x64-ENU-StdDev.iso`.

      Only the English version is supported.

   1. Run the installer and choose **Download Media** to download the full ISO.

   1. Choose **English** as the preferred language.

   1. Choose **ISO** as the media type.

   1. Choose **Download**.

**To download cumulative updates**

1. Visit the [Microsoft Catalog Update](https://www.catalog.update.microsoft.com/Home.aspx) page.

1. Find a SQL Server Developer Edition supported by RDS for SQL Server, for example "SQL Server 2025 Cumulative Update".

1. Download the latest supported CU executable file and save it to your machine.

1. Example files: `SQLServer2025-KB5104822-x64.exe` (CU8 for SQL Server 2025). See the supported versions table below for the required CU file name for each SQL Server version.

**Important**  
RDS for SQL Server only supports specific Cumulative Update (CU) versions. You must use the exact version listed in the table below. Do not use newer CU versions even if available from Microsoft, as they may not be compatible with RDS.

Alternatively, you can also download the required Cumulative Update (CU) file directly from the following:

The following table lists the supported SQL Server Developer Edition version and its corresponding Cumulative Update for use with RDS:


| SQL Server Version | Supported CU | KB Article | Download File Name | 
| --- | --- | --- | --- | 
| SQL Server 2025 (Enterprise/Standard Developer Edition) | `CU8` | [KB5104822](https://support.microsoft.com/en-us/servicing/sql/sql-server-2025/cumulative-update/kb5104822-cu8) | `SQLServer2025-KB5104822-x64.exe` | 
| SQL Server 2025 (Enterprise/Standard Developer Edition) | `CU7` | [KB5096981](https://support.microsoft.com/en-us/servicing/sql/sql-server-2025/cumulative-update/kb5096981-cu7) | `SQLServer2025-KB5096981-x64.exe` | 
| SQL Server 2025 (Enterprise/Standard Developer Edition) | `CU6` | [KB5093421](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2025/cumulativeupdate6) | `SQLServer2025-KB5093421-x64.exe` | 
| SQL Server 2025 (Enterprise/Standard Developer Edition) | `CU5` | [KB5084896](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2025/cumulativeupdate5) | `SQLServer2025-KB5084896-x64.exe` | 
| SQL Server 2022 | `CU26` | [KB5093420](https://support.microsoft.com/en-us/servicing/sql/sql-server-2022/cumulative-update/kb5093420-cu26) | `SQLServer2022-KB5093420-x64.exe` | 
| SQL Server 2022 | `CU25` | [KB5081477](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate25) | `SQLServer2022-KB5081477-x64.exe` | 
| SQL Server 2022 | `CU21` | [KB5065865](https://learn.microsoft.com/en-us/troubleshoot/sql/releases/sqlserver-2022/cumulativeupdate21) | `SQLServer2022-KB5065865-x64.exe` | 
| SQL Server 2019 | `CU32 GDR` | [KB5102335](https://support.microsoft.com/en-us/servicing/sql/sql-server-2019/general-distribution-release/kb5102335-july) | `SQLServer2019-KB5102335-x64.exe` | 
| SQL Server 2019 | `CU32 GDR` | [KB5090407](https://support.microsoft.com/en-us/servicing/sql/sql-server-2019/cumulative-update/kb5090407-description-of-the-security-update-for-sql-server-2019-cu32-may-12-2026) | `SQLServer2019-KB5090407-x64.exe` | 
| SQL Server 2019 | `CU32 GDR` | [KB5068404](https://support.microsoft.com/en-us/topic/kb5068404-description-of-the-security-update-for-sql-server-2019-cu32-november-11-2025-c203bfbf-036e-46d2-bc10-6c01200dc48a) | `SQLServer2019-KB5068404-x64.exe` | 