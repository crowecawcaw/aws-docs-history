# Analyzing top Oracle PDB load

When analyzing the load on an Oracle container DB (CDB), you might want to
identify which pluggable databases (PDBs) contribute the most to DB load.
You might also want to compare the performance of individual PDBs
that are running similar queries to fine tune performance. For more information about Oracle CDBs, see
[RDS for Oracle database architecture](oracle-multi-architecture.md "oracle-multi-architecture.md").

In the Amazon RDS Performance Insights dashboard, you can find information about pluggable databases (PDBs) under **Top PDB** tab
in the **Dimensions** tab.

For the region, DB engine, and instance class support information for this feature, see
[Amazon RDS DB engine, Region, and instance class support
for Performance Insights features](USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport "USER_PerfInsights.Overview.md#USER_PerfInsights.Overview.PIfeatureEngnRegSupport").

###### To analyze Top PDB load in an Oracle CDB

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, select **Performance Insights**.
3. Choose an Oracle CDB instance.

The Performance Insights dashboard appears for the DB instance. 4. In the **Database load (DB load)** section, choose **Pluggable database (PDB)** next to Slice by.

The Average active sessions chart shows the PDB with the highest load.
The PDB identifiers appear to the right of the color-coded squares. Each identifier uniquely identifies a PDB.

![Average active sessions chart for PDB load](images/perf_insights_topPDB_AAS.png) 5. Scroll down to the **Top SQL** tab.

In the following example, you can see the same SQL query and the load it drives to multiple PDBs.

![Same SQL query load for multiple PDBs](images/perf_insights_topPDB_ex1.png)

In the following example, a single PDB is handling higher load than other PDBs in the CDB.

![High SQL query load for PDB](images/perf_insights_topPDB_ex2.png)

For more information about Oracle CDBs, see
[CDBs and PDBs](https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/CDBs-and-PDBs.html#GUID-FC2EB562-ED31-49EF-8707-C766B6FE66B8 "https://docs.oracle.com/en/database/oracle/oracle-database/21/cncpt/CDBs-and-PDBs.html#GUID-FC2EB562-ED31-49EF-8707-C766B6FE66B8").
