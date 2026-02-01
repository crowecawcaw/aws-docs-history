#

Running a client-side trace on a SQL Server DB instance

**To run a client-side trace on a SQL Server DB
instance**

1. Start SQL Server Profiler. It is installed in the Performance Tools folder
   of your SQL Server instance folder. You must load or define a trace
   definition template to start a client-side trace.
2. In the SQL Server Profiler File menu, choose **New
   Trace**. In the **Connect to Server** dialog box,
   enter the DB instance endpoint, port, master user name, and password of the
   database you would like to run a trace on.
3. In the **Trace Properties** dialog box, enter a trace name and choose a trace definition template. A default
   template, TSQL_Replay, ships with the application. You can edit this template to define your trace. Edit events and
   event information under the **Events Selection** tab of the **Trace Properties**
   dialog box.

For more information about trace definition templates and using the SQL Server Profiler to specify a client-side
trace, see [Database Engine Tuning Advisor](https://docs.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor "https://docs.microsoft.com/en-us/sql/relational-databases/performance/database-engine-tuning-advisor") in the Microsoft documentation. 4. Start the client-side trace and watch SQL queries in real-time as they
run against your DB instance. 5. Select **Stop Trace** from the **File** menu when you
have completed the trace. Save the results as a file or as a trace table on
you DB instance.
