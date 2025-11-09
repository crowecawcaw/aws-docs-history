# Best Practice 19.3 – Use compression,

reorganization, and reclaim strategies

All databases supported by SAP provide mechanisms for reclaiming space. These
mechanisms should be part of regular maintenance activities to minimize cost increases
associated with extending memory or EBS volumes.

**Suggestion 19.3.1 – Use database compression**

Compression is a default characteristic in SAP HANA. Use of compression in other
databases might require additional licenses but should be explored for cost and
performance benefits. The following notes provide a starting point for the various
databases, but refer to SAP and database documentation for additional information.

| Database             | SAP Documentation or SAP Notes                                                                                                                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAP HANA             | SAP Note: [2112604<br>• FAQ: SAP HANA<br>Compression](https://launchpad.support.sap.com/#/notes/2112604 "https://launchpad.support.sap.com/#/notes/2112604") [Requires SAP Portal Access]                |
| SAP ASE              | (Consult SAP or Vendor documentation for guidance)                                                                                                                                                       |
| IBM Db2              | SAP Note: [1555903<br>• DB6: Supported<br>IBM Db2 Database Features](https://launchpad.support.sap.com/#/notes/1555903 "https://launchpad.support.sap.com/#/notes/1555903") [Requires SAP Portal Access] |
| Oracle               | SAP Note: [1289494<br>• FAQ: Oracle<br>compression](https://launchpad.support.sap.com/#/notes/1289494 "https://launchpad.support.sap.com/#/notes/1289494") [Requires SAP Portal Access]                  |
| Microsoft SQL Server | SAP Note: [1488135<br>• Database<br>compression for SQL Server](https://launchpad.support.sap.com/#/notes/1488135 "https://launchpad.support.sap.com/#/notes/1488135") [Requires SAP Portal Access]      |
| SAP MaxDB            | (Consult SAP or Vendor documentation for guidance)                                                                                                                                                       |

**Suggestion 19.3.2 – Use database reorganizations and reclaim
operations**

Space which is unused within the database, due to organic use or targeted archive and
cleanup activities, might require a reorganization or reclaim operation to realize the
space savings. By reclaiming space regularly, you will reduce the overall growth and
requirement for additional storage or memory. The following notes provide a starting point
for the various databases, but refer to SAP and database documentation:

| Database             | SAP Documentation or SAP Notes                                                                                                                                                                                                |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SAP HANA             | SAP Note: [2499913<br>• How to shrink<br>SAP HANA Data Volume size](https://launchpad.support.sap.com/#/notes/2499913 "https://launchpad.support.sap.com/#/notes/2499913") [Requires SAP Portal Access]                       |
| SAP ASE              | SAP Note: [2543407<br>• reorg rebuild<br>with online<br>• SAP ASE for Business Suite](https://launchpad.support.sap.com/#/notes/2543407 "https://launchpad.support.sap.com/#/notes/2543407") [Requires SAP Portal Access]     |
| IBM Db2              | SAP Note: [1942183<br>• DB6: When to<br>consider a table or index reorganization](https://launchpad.support.sap.com/#/notes/1942183 "https://launchpad.support.sap.com/#/notes/1942183") [Requires SAP Portal Access]         |
| Oracle               | SAP Note: [541538<br>• FAQ:<br>Reorganization](https://launchpad.support.sap.com/#/notes/541538 "https://launchpad.support.sap.com/#/notes/541538") [Requires SAP Portal Access]                                              |
| Microsoft SQL Server | SAP Note: [1721843<br>• MSSQL:<br>Post-steps after archiving, deleting or compression](https://launchpad.support.sap.com/#/notes/1721843 "https://launchpad.support.sap.com/#/notes/1721843") [Requires SAP Portal<br>Access] |
| SAP MaxDB            | (Consult SAP or Vendor documentation for guidance)                                                                                                                                                                            |
