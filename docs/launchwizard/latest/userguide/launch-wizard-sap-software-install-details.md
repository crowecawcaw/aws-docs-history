# Make SAP application software

available for AWS Launch Wizard to deploy SAP

This section describes steps to upload the SAP application software to Amazon S3 to make it
available for Launch Wizard to deploy SAP.

AWS Launch Wizard supports the following software versions. To install a software version, you must
provide the SAP software files to Launch Wizard by downloading them from the [SAP Support Portal](https://support.sap.com/en/index.html "https://support.sap.com/en/index.html") and then
uploading them to Amazon S3 (storage class - Standard). To access and use the files for
installation, Launch Wizard requires them to be formatted according to the Amazon S3 file path syntax
listed in the following table.

###### Note

The software versions and CD numbers listed in the following table should be used as a
reference for all of the software components required to deploy SAP, as well as for how
to format the Amazon S3 path to make the software available for Launch Wizard to deploy SAP. Launch Wizard
supports NetWeaver 7.50, NetWeaver 7.52, S/4 HANA 1909, S/4 HANA 2020, and BW/4HANA 2.0.
You can source the latest SAP software using a script or determine the latest CD numbers
of supported applications to use from SAP manually.

- For more information about running a pre-deployment configuration script to
  source the latest SAP software, refer to the [software_download](https://github.com/awslabs/aws-sap-automation/tree/main/software_download "https://github.com/awslabs/aws-sap-automation/tree/main/software_download") portion of the **aws-sap-automation** repository.
- For more information about finding the latest software from SAP, refer to
  [SAP Maintenance Planner](https://support.sap.com/en/alm/solution-manager/processes-72/maintenance-planner.html "https://support.sap.com/en/alm/solution-manager/processes-72/maintenance-planner.html") or [SAP
  Software Downloads](https://support.sap.com/en/my-support/software-downloads.html "https://support.sap.com/en/my-support/software-downloads.html").

###### Databases

- [Making software available for SAP HANA based
  applications](#nw-on-hana "#nw-on-hana")
- [Making software available for SAP ASE based
  applications](#nw-on-ase "#nw-on-ase")

## Making software available for SAP HANA based

applications

###### Note

SAP Host Agent 7.22 PL62 or a later version is recommended in a high availability
setup for SAP HANA site replication to avoid a known issue with the host
agent.

NetWeaver 7.52

| CD name              | Versions                 | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 1.0 latest version  | `SWPM20SP16_2-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1200-70007716.EXE | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | NW 7.52                  | `51051806_part1.exe`<br>`51051806_part2.rar`                                                                                                         | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.53 and later        | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_66-70006642.SAR`<br>`SAPEXEDB_66-70006641.SAR`<br>`SAPHOSTAGENT59_59-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name      | Versions   | CD number                                                                                      | Amazon S3 file path |
| ------------ | ---------- | ---------------------------------------------------------------------------------------------- | ------------------- |
| hana-20-sp05 | `51058046` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06 | `51056431` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp08 | `51058521` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

NetWeaver 7.50

| CD name              | Versions                 | CD number                                                                                                                                               | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 1.0 latest version  | `SWPM10SP42_1-20009701.SAR`                                                                                                                             | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | NW 7.50                  | `51050829_3.ZIP`                                                                                                                                        | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.53 and later        | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_700-80002572.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                    | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                      | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name      | Versions   | CD number                                                                                      | Amazon S3 file path |
| ------------ | ---------- | ---------------------------------------------------------------------------------------------- | ------------------- |
| hana-20-sp05 | `51058046` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06 | `51056431` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp08 | `51058521` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

NetWeaver 750 (JAVA)

| CD name              | Versions                | CD number                                                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 1.0 latest version | `SWPM10SP42_1-20009701.SAR`                                                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | NW 7.50                 | `51055106.ZIP`                                                                                                                                                                       | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.53 and later       | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_700-80002572.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR`<br>`SAPJVM8_89-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                     | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name      | Versions   | CD number                                                                                      | Amazon S3 file path |
| ------------ | ---------- | ---------------------------------------------------------------------------------------------- | ------------------- |
| hana-20-sp05 | `51056441` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06 | `51058046` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp08 | `51058521` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

BW/4HANA 2023

| CD name              | Versions                 | CD number                                                                                                                                              | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP19_1-80003424.SAR`                                                                                                                            | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                    | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | BW4HANA300               | `BW4HANA400_INST_EXPORT_1.zip` through<br>`BW4HANA400_INST_EXPORT_9.zip`                                                                               | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later             | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_101-70007807.SAR`<br>`SAPEXEDB_101-70007806.SAR`<br>`SAPHOSTAGENT54_54-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.22                     | `IMDB_CLIENT20_022_32-80002082.SAR`                                                                                                                    | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                     | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA Database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

BW/4HANA 2021

| CD name              | Versions                 | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP10_3-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | BW4HANA300               | `BW4HANA300_INST_EXPORT_1.zip` through<br>`BW4HANA300_INST_EXPORT_8.zip`                                                                             | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later             | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_50-80005374.SAR`<br>`SAPEXEDB_50-80005373.SAR`<br>`SAPHOSTAGENT54_54-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                     | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA Database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

BW/4HANA 2.0

| CD name              | Versions                 | CD number                                                                                                                                               | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP07_0-80003424.SAR`                                                                                                                             | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | BW4HANA 2.0              | `BW4HANA200_INST_EXPORT_1.zip` through<br>`BW4HANA200_INST_EXPORT_7.zip`                                                                                | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.77                  | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_300-80004393.SAR`<br>`SAPEXEDB_300-80004392.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                    | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                      | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA 2023

| CD name              | Versions                | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version | `SWPM20SP16_0-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 108              | `S4CORE108_INST_EXPORT_1.zip` through<br>`S4CORE108_INST_EXPORT_30.zip`                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later            | `igsexe_4-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_60-70007807.SAR`<br>`SAPEXEDB_60-70007806.SAR`<br>`SAPHOSTAGENT62_62-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                    | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                      | Versions     | CD number  | Amazon S3 file path                                                                            |
| ---------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database software` | hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA Foundations 2023

| CD name              | Versions                | CD number                                                                                                                                        | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version | `SWPM20SP16_0-80003424.SAR`                                                                                                                      | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 108              | `S4FND108_INST_EXPORT_1.zip` through<br>`S4FND108_INST_EXPORT_9.zip`                                                                             | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later            | `igsexe_4-70005417.sar``igshelper_17-10010245.sar`<br>`SAPEXE_60-70007807.SAR`<br>`SAPEXEDB_60-70007806.SAR`<br>`SAPHOSTAGENT62_62-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                    | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                               | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                      | Versions     | CD number  | Amazon S3 file path                                                                            |
| ---------------------------- | ------------ | ---------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database software` | hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA 2022

| CD name              | Versions                | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version | `SWPM20SP10_3-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 105              | `S4CORE107_INST_EXPORT_1.zip` through<br>`S4CORE107_INST_EXPORT_30.zip`                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later            | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_66-70006642.SAR`<br>`SAPEXEDB_66-70006641.SAR`<br>`SAPHOSTAGENT59_59-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                    | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA Foundations 2022

| CD name              | Versions                | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version | `SWPM20SP10_3-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 105              | `S4FND107_INST_EXPORT_1.zip` through<br>`S4FND107_INST_EXPORT_9.zip`                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later            | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_66-70006642.SAR`<br>`SAPEXEDB_66-70006641.SAR`<br>`SAPHOSTAGENT59_59-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                    | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA 2021

| CD name              | Versions                 | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP10_3-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 106               | `S4CORE106_INST_EXPORT_1.zip` through<br>`S4CORE106_INST_EXPORT_28.zip`                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later             | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_50-80005374.SAR`<br>`SAPEXEDB_50-80005373.SAR`<br>`SAPHOSTAGENT54_54-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                     | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA Foundations 2021

| CD name              | Versions                | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version | `SWPM20SP10_3-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | Latest                  | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 105              | `S4FND106_INST_EXPORT_1.zip` through<br>`S4FND106_INST_EXPORT_8.zip`                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | 785 or later            | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_66-70006642.SAR`<br>`SAPEXEDB_66-70006641.SAR`<br>`SAPHOSTAGENT59_59-80004822.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.11                    | `IMDB_CLIENT20_011_14-80002082.SAR`                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                    | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA 2020

| CD name              | Versions                 | CD number                                                                                                                                            | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP07_0-80003424.SAR`                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                  | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 105               | `S4CORE105_INST_EXPORT_1.zip` through<br>`S4CORE105_INST_EXPORT_24.zip`                                                                              | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.77                  | `igsexe_0-70005417.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_15-70005283.SAR`<br>`SAPEXEDB_15-70005282.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                   | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

S/4HANA 1909

| CD name              | Versions                 | CD number                                                                                                                                               | Amazon S3 file path                                                                                |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 2.0 latest version  | `SWPM20SP07_0-80003424.SAR`                                                                                                                             | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`                    |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`                  |
| `Exports`            | S4Core 104               | `S4CORE104_INST_EXPORT_1.zip` through<br>`S4CORE104_INST_EXPORT_25.zip`                                                                                 | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports`                 |
| `Kernel components`  | NW 7.77                  | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_300-80004393.SAR`<br>`SAPEXEDB_300-80004392.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                                                    | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.                                      | `S3://`Your SAP software bucket<`/webdisp/`                                                        |

The following HANA DB version is supported.

###### Note

\*The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                         | Versions     | CD number                                                                                      | Amazon S3 file path                                                                            |
| ------------------------------- | ------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `SAP HANA database<br>software` | hana-20-sp05 | `51056441`                                                                                     | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06                    | `51056431`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07                    | `51057071`   | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

Solution Manager 7.2

| CD name              | Versions                 | CD number                                                                                                                 | Amazon S3 file path                                                                                             |
| -------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `SWPM`               | SWPM 1.0 latest version  | `SWPM10SP42_1-20009701.SAR`                                                                                               | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/SWPM`                 |
| `SAPCAR`             | SAPCAR_1010-70006178.exe | N/A                                                                                                                       | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/SAPCAR`               |
| `Exports`            | SAP Solution Manager 7.2 | `51054655_1.ZIP…51054655_4.ZIP`<br>`igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`                                | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/Exports`              |
| `Kernel components`  | NW 7.53 and later        | `SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_700-80002572.SAR`<br>`SAPHOSTAGENT49_49-20009394.SAR`<br>`SAPJVM8_89-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/Kernel`               |
| `SAP HANA Client`    | 2.5                      | `IMDB_CLIENT20_005_111-80002082.SAR`                                                                                      | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/HANA_Client_Software` |
| `SAP Web Dispatcher` | 7.93                     | See [Note 908097](https://me.sap.com/notes/908097/E "https://me.sap.com/notes/908097/E") in the SAP documentation.        | `S3://`Your SAP software bucket<`/webdisp/`                                                                     |

The following HANA DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name      | Versions   | CD number                                                                                      | Amazon S3 file path |
| ------------ | ---------- | ---------------------------------------------------------------------------------------------- | ------------------- |
| hana-20-sp05 | `51058046` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp06 | `51056431` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp07 | `51057071` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |
| hana-20-sp08 | `51058521` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/HANA_DB_Software` |

## Making software available for SAP ASE based

applications

NetWeaver 7.52

| CD name             | Versions                | CD number                                                                                                                                                                             | Amazon S3 file path                                                                |
| ------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `SWPM`              | SWPM 1.0 latest version | `SWPM10SP38_4-20009701.SAR`                                                                                                                                                           | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`    |
| `SAPCAR`            | Latest                  | `SAPCAR_1115-70006178.EXE`                                                                                                                                                            | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`  |
| `Exports`           | NW 7.52                 | `51051806_part1.exe`<br>`51051806_part2.rar`                                                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports` |
| `Kernel components` | NW 7.53 and later       | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_1000-80002616.SAR`<br>`SAPHOSTAGENT61_61-80004822.SAR`<br>`SAPJVM8_95-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`  |

The following SAP ASE DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                     | Versions           | CD number        | Amazon S3 file path                                                                              |
| --------------------------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------ |
| `SAP ASE Database software` | SAP ASE 16.0.04.04 | `51056521_1.ZIP` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/SAPASE_DB_Software` |

NetWeaver 7.50

| CD name             | Versions                | CD number                                                                                                                                                                             | Amazon S3 file path                                                                |
| ------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `SWPM`              | SWPM 1.0 latest version | `SWPM10SP38_4-20009701.SAR`                                                                                                                                                           | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`    |
| `SAPCAR`            | Latest                  | `SAPCAR_1115-70006178.EXE`                                                                                                                                                            | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`  |
| `Exports`           | NW 7.50                 | `51050829_3.ZIP`                                                                                                                                                                      | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports` |
| `Kernel components` | NW 7.53 and later       | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_1000-80002616.SAR`<br>`SAPHOSTAGENT61_61-80004822.SAR`<br>`SAPJVM8_95-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`  |

The following SAP ASE DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                     | Versions           | CD number        | Amazon S3 file path                                                                              |
| --------------------------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------ |
| `SAP ASE Database software` | SAP ASE 16.0.04.04 | `51056521_1.ZIP` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/SAPASE_DB_Software` |

NetWeaver 750 (JAVA)

| CD name             | Versions                | CD number                                                                                                                                                                             | Amazon S3 file path                                                                |
| ------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `SWPM`              | SWPM 1.0 latest version | `SWPM10SP42_1-20009701.SAR`                                                                                                                                                           | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SWPM`    |
| `SAPCAR`            | Latest                  | `SAPCAR_1115-70006178.EXE`                                                                                                                                                            | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/SAPCAR`  |
| `Exports`           | NW 7.50                 | `51055106.ZIP`                                                                                                                                                                        | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Exports` |
| `Kernel components` | NW 7.53 and later       | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_1000-80002616.SAR`<br>`SAPHOSTAGENT61_61-80004822.SAR`<br>`SAPJVM8_95-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`  |

The following SAP ASE DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                     | Versions           | CD number        | Amazon S3 file path                                                                              |
| --------------------------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------ |
| `SAP ASE Database software` | SAP ASE 16.0.04.04 | `51056521_1.ZIP` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/SAPASE_DB_Software` |

Solution Manager 7.2

| CD name             | Versions                 | CD number                                                                                                                                                                             | Amazon S3 file path                                                                                |
| ------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `SWPM`              | SWPM 1.0 latest version  | `SWPM10SP42_1-20009701.SAR`                                                                                                                                                           | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/SWPM`    |
| `SAPCAR`            | Latest                   | `SAPCAR_1115-70006178.EXE`                                                                                                                                                            | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/SAPCAR`  |
| `Exports`           | SAP Solution Manager 7.2 | `51054655_1.ZIP`<br>`51054655_2.ZIP`<br>`51054655_3.ZIP`<br>`51054655_4.ZIP`                                                                                                          | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>SolutionManager<br>version>`/Exports` |
| `Kernel components` | NW 7.53 and later        | `igsexe_12-80003187.sar`<br>`igshelper_17-10010245.sar`<br>`SAPEXE_700-80002573.SAR`<br>`SAPEXEDB_1000-80002616.SAR`<br>`SAPHOSTAGENT61_61-80004822.SAR`<br>`SAPJVM8_95-80000202.SAR` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW version>`/Kernel`                  |

The following SAP ASE DB versions are supported (ZIP files only).

###### Note

The CD versions are for reference only. Use the latest versions
available on SAP Software Center.

| CD name                     | Versions           | CD number        | Amazon S3 file path                                                                              |
| --------------------------- | ------------------ | ---------------- | ------------------------------------------------------------------------------------------------ |
| `SAP ASE Database software` | SAP ASE 16.0.04.04 | `51056521_1.ZIP` | `S3://`<Your SAP software<br>bucket>`/`<Path representing<br>NW<br>version>`/SAPASE_DB_Software` |
