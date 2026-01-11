# Working with the EXTRACT and REPLICAT utilities of

Oracle GoldenGate

The Oracle GoldenGate utilities `EXTRACT` and `REPLICAT` work together to keep the
source and target databases in sync via incremental transaction replication using trail
files. All changes that occur on the source database are automatically detected by
`EXTRACT`, then formatted and transferred to trail files on the Oracle GoldenGate
on-premises or Amazon EC2 instance hub. After initial load is completed, the data is read from
these files and replicated to the target database by the `REPLICAT`
utility.

## Running the Oracle GoldenGate EXTRACT utility

The `EXTRACT` utility retrieves, converts, and outputs data from the source
database to trail files. The basic process is as follows:

1. `EXTRACT` queues transaction details to memory or to temporary disk
   storage.
2. The source database commits the transaction.
3. `EXTRACT` writes the transaction details to a trail file.
4. The trail file routes these details to the Oracle GoldenGate on-premises or the Amazon EC2
   instance hub and then to the target database.

The following steps start the `EXTRACT` utility, capture the data from
`EXAMPLE.TABLE` in source database `OGGSOURCE`, and create the
trail files.

###### To run the EXTRACT utility

1. Configure the `EXTRACT` parameter file on the Oracle GoldenGate hub
   (on-premises or Amazon EC2 instance). The following listing shows an example
   `EXTRACT` parameter file named
   `$GGHOME/dirprm/eabc.prm`.

```
EXTRACT EABC
 
USERID oggadm1@OGGSOURCE, PASSWORD "`my-password`"
EXTTRAIL `/path/to/goldengate/dirdat/ab`
 
IGNOREREPLICATES
GETAPPLOPS
TRANLOGOPTIONS EXCLUDEUSER OGGADM1
	 
TABLE EXAMPLE.TABLE;
```

2. On the Oracle GoldenGate hub, log in to the source database and launch the Oracle GoldenGate command
   line interface `ggsci`. The following example shows the format for
   logging in.

```
dblogin oggadm1@OGGSOURCE
```

3. Add transaction data to turn on supplemental logging for the database
   table.

```
add trandata EXAMPLE.TABLE
```

4. Using the `ggsci` command line, enable the `EXTRACT`
   utility using the following commands.

```
add extract EABC tranlog, INTEGRATED tranlog, begin now
add exttrail `/path/to/goldengate/dirdat/ab`
   extract EABC,
   MEGABYTES 100
```

5. Register the `EXTRACT` utility with the database so that the
   archive logs are not deleted. This task allows you to recover old, uncommitted
   transactions if necessary. To register the `EXTRACT` utility with the
   database, use the following command.

```
register EXTRACT EABC, DATABASE
```

6. Start the `EXTRACT` utility with the following command.

```
start EABC
```

## Running the Oracle GoldenGate REPLICAT utility

The `REPLICAT` utility "pushes" transaction information in the trail files to the
target database.

The following steps enable and start the `REPLICAT` utility so that it can
replicate the captured data to the table `EXAMPLE.TABLE` in target database
`OGGTARGET`.

###### To run the REPLICATE utility

1. Configure the `REPLICAT` parameter file on the Oracle GoldenGate hub
   (on-premises or EC2 instance). The following listing shows an example
   `REPLICAT` parameter file named
   `$GGHOME/dirprm/rabc.prm`.

```
REPLICAT RABC
 
USERID oggadm1@OGGTARGET, password "`my-password`"
 
ASSUMETARGETDEFS
MAP EXAMPLE.TABLE, TARGET EXAMPLE.TABLE;
```

###### Note

Specify a password other than the prompt shown here as a security best practice. 2. Log in to the target database and launch the Oracle GoldenGate command line interface
(`ggsci`). The following example shows the format for logging
in.

```
dblogin userid oggadm1@OGGTARGET
```

3. Using the `ggsci` command line, add a checkpoint table. The user indicated
   should be the Oracle GoldenGate user account, not the target table schema owner. The
   following example creates a checkpoint table named
   `gg_checkpoint`.

```
add checkpointtable oggadm1.oggchkpt
```

4. To enable the `REPLICAT` utility, use the following command.

```
add replicat RABC EXTTRAIL `/path/to/goldengate/dirdat/ab` CHECKPOINTTABLE oggadm1.oggchkpt
```

5. Start the `REPLICAT` utility by using the following command.

```
start RABC
```
