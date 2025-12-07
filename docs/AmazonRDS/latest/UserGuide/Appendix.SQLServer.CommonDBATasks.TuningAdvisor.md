# Running

Tuning Advisor with a trace

Once you create a trace, either as a local file or as a database table, you can then run Tuning Advisor against your DB instance.
Using Tuning Advisor with Amazon RDS is the same process as when working with a standalone, remote SQL Server instance. You can
either use the Tuning Advisor UI on your client machine or use the dta.exe utility from the command line. In both cases, you
must connect to the Amazon RDS DB instance using the endpoint for the DB instance and provide your master user name and master
user password when using Tuning Advisor.

The following code example demonstrates using the dta.exe command line utility against an Amazon RDS DB instance with an endpoint of
`dta.cnazcmklsdei.us-east-1.rds.amazonaws.com`. The example includes the master user name `admin` and the master user password
`test`, the example database to tune is named machine named `C:\RDSTrace.trc`. The example command line code
also specifies a trace session named `RDSTrace1` and specifies output files to the local machine named `RDSTrace.sql` for the
SQL output script, `RDSTrace.txt` for a result file, and `RDSTrace.xml` for an XML file of the analysis. There is also
an error table specified on the RDSDTA database named `RDSTraceErrors`.

```
dta -S dta.cnazcmklsdei.us-east-1.rds.amazonaws.com -U admin -P test -D RDSDTA -if C:\RDSTrace.trc -s RDSTrace1 -of C:\ RDSTrace.sql -or C:\ RDSTrace.txt -ox C:\ RDSTrace.xml -e RDSDTA.dbo.RDSTraceErrors
```

Here is the same example command line code except the input workload is a table on the remote Amazon RDS instance named `RDSTrace` which is on the
`RDSDTA` database.

```
dta -S dta.cnazcmklsdei.us-east-1.rds.amazonaws.com -U admin -P test -D RDSDTA -it RDSDTA.dbo.RDSTrace -s RDSTrace1 -of C:\ RDSTrace.sql -or C:\ RDSTrace.txt -ox C:\ RDSTrace.xml -e RDSDTA.dbo.RDSTraceErrors
```

For a full list of dta utility command-line parameters, see [dta Utility](https://docs.microsoft.com/en-us/sql/tools/dta/dta-utility "https://docs.microsoft.com/en-us/sql/tools/dta/dta-utility") in
the Microsoft documentation.
