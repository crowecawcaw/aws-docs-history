# Best Practice 15.2 – Modify database

parameters to align with hardware selection

SAP provides specific guidance to optimize performance of an SAP system by modifying
certain parameters of the underlying database. These parameters are specific to database
type and can vary based on whether it’s supporting an analytical or a transactional type
application.

**Suggestion 15.2.1 – Review SAP HANA-specific tuning parameters, if
applicable**

Operating System and SAP HANA Database parameters can significantly impact
performance. Follow SAP on AWS recommendations for Operating system and storage
configuration.

- AWS Documentation: [SAP HANA on AWS – Operating System and Storage Configuration](../../../sap/latest/sap-hana/operating-system-and-storage-configuration.md "../../../sap/latest/sap-hana/operating-system-and-storage-configuration.md")
  Refer to SAP notes and documentation for guidance on SAP HANA parameters including
  memory allocation.

- SAP Note: [2000000

* FAQ: SAP HANA Performance Optimization](https://launchpad.support.sap.com/#/notes/2000000 "https://launchpad.support.sap.com/#/notes/2000000") [Requires SAP Portal Access]

- SAP Documentation: [HANA Parameter: global_allocation_limit](https://help.sap.com/viewer/009e68bc5f3c440cb31823a3ec4bb95b/2.0.05/en-US/514ab38a2e574c85a70ebba80ff16d99.html#loio514ab38a2e574c85a70ebba80ff16d99__configSPS05_id_805 "https://help.sap.com/viewer/009e68bc5f3c440cb31823a3ec4bb95b/2.0.05/en-US/514ab38a2e574c85a70ebba80ff16d99.html#loio514ab38a2e574c85a70ebba80ff16d99__configSPS05_id_805")
- SAP Note: [1999997

* FAQ: SAP HANA Memory](https://launchpad.support.sap.com/#/notes/1999997 "https://launchpad.support.sap.com/#/notes/1999997") [Requires SAP Portal Access]

- SAP Note: [2926166

* How to limit the overall SAP HANA memory allocation](https://launchpad.support.sap.com/#/notes/2926166 "https://launchpad.support.sap.com/#/notes/2926166") [Requires SAP Portal
  Access]

**Suggestion 15.2.2 – Review database tuning guidance for non-SAP HANA
databases**

Regardless of the underlying database for your SAP system, performance of the system
is in part dependent on how the database is tuned. Each database has specific
recommendations for tuning based on available compute, memory, and disk storage. Certain
database parameters are dependent on your choice of underlying EC2 instance size; for
example, the physical memory available will limit the `db_cache_size` for an
Oracle database.

For information relevant to your database, refer to the following:

| Database             | Guidance                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAP ASE              | SAP Note: [2473646 - Performance and Tuning information for ASE -SAP ASE](https://launchpad.support.sap.com/#/notes/2473646 "https://launchpad.support.sap.com/#/notes/2473646") [Requires SAP Portal Access]                                                                                                                                                                                                             |
| IBM Db2              | SAP Note: [2751102 – DB6: DB2 11.5 Standard Parameter Settings](https://launchpad.support.sap.com/#/notes/2751102 "https://launchpad.support.sap.com/#/notes/2751102") [Requires SAP Portal Access]                                                                                                                                                                                                                       |
| Oracle               | SAP Note: [2470718 – Oracle Database Parameter 12.2 / 18c / 19c](https://launchpad.support.sap.com/#/notes/2470718 "https://launchpad.support.sap.com/#/notes/2470718") [Requires SAP Portal Access]                                                                                                                                                                                                                      |
| Microsoft SQL Server | SAP Note: [2779607 – Configuration Parameters for SQL Server 2019](https://launchpad.support.sap.com/#/notes/2779607 "https://launchpad.support.sap.com/#/notes/2779607") [Requires SAP Portal Access] , SAP Note: [2729848 – SAP Installation Media and SQL4SAP for SQL Server 2019](https://launchpad.support.sap.com/#/notes/2729848 "https://launchpad.support.sap.com/#/notes/2729848") [Requires SAP Portal Access] |
| SAP MaxDB            | SAP Note: [819641 – FAQ: SAP MaxDB performance](https://launchpad.support.sap.com/#/notes/819641 "https://launchpad.support.sap.com/#/notes/819641") [Requires SAP Portal Access]                                                                                                                                                                                                                                         |
