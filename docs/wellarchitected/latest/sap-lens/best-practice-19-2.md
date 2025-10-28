# Best Practice 19.2 – Delete

unnecessary data through regular housekeeping

Reduce your data footprint to save costs by minimizing database size and other
filesystem usage through regular housekeeping and reorganization activities.

**Suggestion 19.2.1 – Review sizing and perform regular housekeeping
on SAP technical tables**

SAP provides comprehensive guidance on the data management of technical tables. By
identifying and addressing the growth of these tables, it is possible to reduce storage
and compute costs. This is especially relevant for SAP HANA instances because of the
direct relationship between database size and memory requirements.

- SAP Note: [2388483

* How-To: Data Management for Technical Tables](https://launchpad.support.sap.com/#/notes/2388483 "https://launchpad.support.sap.com/#/notes/2388483") [Requires SAP Portal Access]
  Use the "largest table" SQL Statements referenced to get comparative table sizes, in
  particular those marked as Basis tables. A frequent example in established SAP customers is
  the high number of completed SAP workflow items which could be deleted or archived.
  Housekeeping prior to a migration can also improve timelines and performance. If using SAP
  HANA, the report `/SDF/HDB_SIZING` can provide cleanup details and anticipated
  disk requirement.

**Suggestion 19.2.2 – Control filesystem growth through automatic or
regular cleanup of logs, traces, interface files, and backups**

As storage costs are driven by usage, there are opportunities to optimize the
baseline usage, in addition to the multiplier effect of copies and backups of files which
are no longer useful for fault analysis.

- SAP Note: [2399996

* How-To: Configuring automatic SAP HANA Cleanup with SAP HANACleaner](https://launchpad.support.sap.com/#/notes/2399996 "https://launchpad.support.sap.com/#/notes/2399996")
  [Requires SAP Portal Access]
