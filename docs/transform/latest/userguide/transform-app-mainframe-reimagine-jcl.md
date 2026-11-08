

# JCL
<a name="transform-app-mainframe-reimagine-jcl"></a>

This reference describes how AWS Transform represents JCL (Job Control Language) statements in the business rules produced by the reimagine workflow. For the definitions of the representation categories used on this page, see [Supported languages for business rules extraction](transform-app-mainframe-reimagine-supported.md).

AWS Transform reads a batch job as a sequence of steps: it extracts the job and step structure, the program each step runs, the conditions that decide whether a step runs, and the data sets each step reads and writes. The program named on a step, and the data set management commands the step issues, are what AWS Transform turns into business rules. Most other statements either enter the wording of those rules or supply the context the rules refer to; the remaining statements are not represented.

The following tables cover z/OS JCL and group the statements and mechanisms by how each one is represented in the extracted business rules.

## Statements that generate a rule
<a name="transform-app-mainframe-reimagine-jcl-generates"></a>

These statements anchor business rules. AWS Transform builds a rule around each one and describes the rest of the step in relation to it.


| Statements | How it appears in the output | 
| --- | --- | 
| EXEC PGM= | The program named on EXEC PGM= is the anchor of a business rule, and the conditions and data sets of that step are described in relation to it. When the step runs a utility that hosts another program or task, such as a TSO batch program run, a sort, a database utility, or a copy utility, the rule names the program or operation the utility performs and carries the control statements that drive it. A step that runs the access method services utility (IDCAMS) is represented by the data set management commands it issues (see the next row) rather than by the step itself. A step that runs no program, or only allocates or deletes data sets, does not anchor a rule; it is taken into account only through the return code that later steps test. | 
| DD \* / DD DATA (in-stream data) | Supplies control statements or input data directly in the job stream; how it is represented depends on the program that reads it. IDCAMS commands that create, copy, modify, or delete data sets or their contents (REPRO, DELETE, DEFINE, BLDINDEX, IMPORT, EXPORT, ALTER) each generate a rule; listing and verification commands, such as LISTCAT and VERIFY, do not. For TSO batch, sort, and database utility steps, the control statements are carried into the rule of the step that uses them. For other programs, in-stream data is kept as the text of the step. In-stream data is never recorded as a data set that a step reads or writes. | 

## Statements that contribute to a rule
<a name="transform-app-mainframe-reimagine-jcl-contributes"></a>

These statements do not produce a rule on their own. Their effect enters the wording of the rule for the step they govern.


| Statements | How it appears in the output | 
| --- | --- | 
| IF / THEN / ELSE / ENDIF | Runs or skips steps based on return codes or abnormal-end conditions. The condition is not a rule by itself; it is preserved as the circumstance under which the steps it guards run, and it links those rules to the earlier steps whose return codes it tests. | 
| COND parameter (EXEC) | Bypasses a step based on the return codes of earlier steps, including the EVEN and ONLY forms. The test is represented as a condition on the step, in the same way as an IF statement, and enters the wording of that step's rule. | 
| PARM parameter (EXEC) | Passes a parameter string to the program the step runs. It enters a rule when the parameter identifies the program or script that actually runs, for example an IMS batch program or a UNIX shell script run from the step; the rule then names that program or script. Other parameter strings are kept only as part of the step's text. | 
| Comment (//\*) | A statement that starts with //\* and carries no executable meaning. Comments that precede a step are kept with that step's source in its rule, which helps reviewers read the rule; they do not change the rule's logic. | 

## Statements that shape rules as context
<a name="transform-app-mainframe-reimagine-jcl-context"></a>

These statements do not appear as rules. They establish the job and step structure, resolve procedures and symbolic values, and identify the data sets each step reads and writes, so they shape the content of the rules that refer to them.


| Statements | How it appears in the output | 
| --- | --- | 
| JOB | Marks the start of a job and sets job-level attributes. The job is the enclosing scope that owns the steps; it is never a rule on its own. Job-level parameters such as COND and RESTART are not applied. | 
| EXEC PROC= or EXEC procname (procedure invocation) | Starts a job step that runs an in-stream or cataloged procedure. The procedure's steps are inserted in place of the invocation, and each of those steps is represented as described on this page and attributed to the invoking statement. If the procedure cannot be found, the invocation produces a rule that names the procedure but has no step content. | 
| PROC | Defines a procedure and supplies default values for its symbolic parameters. The procedure supplies the steps and default values used where it is invoked; the procedure definition itself is not a rule. | 
| Symbolic parameters and procedure overrides | Substitute symbolic values, and override procedure-step parameters or data definitions from the invoking step. Symbols in data set names are resolved, and overriding data definitions replace the ones in the procedure, before the step's data sets are determined. The rule refers to the resolved values. | 
| SET | Assigns symbolic parameter values used later in the job. The values are resolved into the data set names that later statements use; the assignment is not a rule. | 
| INCLUDE | Inserts a group of JCL statements from a library at the point of the statement. The included statements are inserted into the job before extraction and are represented as the statements they contain, attributed to the included member. If the member cannot be found, the statement has no effect. | 
| DD | Connects a program's logical file name to a physical data set or device. Each data definition is resolved to the physical data set it points to. Data sets that a step reads or writes, according to their disposition, are recorded as such and link a step to the earlier steps that produced them. Data sets that a step only creates or deletes, or whose access cannot be determined, are not recorded as reads or writes. The data definitions of a step are also passed to the program the step runs, so the program's rules can refer to the physical data sets behind its files. | 
| STEPLIB DD | Names the load libraries searched for the step's program. The library is treated like any other data set the step reads. | 
| Concatenated DD statements | Read several data sets as one input under a single logical file name. Every data set in the concatenation is recorded as an input of the step. | 
| Temporary data sets (&&name) | Hold data that is passed between steps of the same job. A temporary data set links the step that writes it to the steps that read it, like a permanent data set. | 
| Generation data group (GDG) relative references | Refer to the current, previous, or a new generation of a data set, such as (0), (-1), or (\+1). The reference is kept as written and links the steps that use the same relative generation. | 
| Delimiter (/\*) | Ends a group of in-stream data. It determines where the in-stream data of the preceding data definition ends; it does not appear on its own. | 

## JCL statements not represented in the rules
<a name="transform-app-mainframe-reimagine-jcl-not-represented"></a>

These statements are read when the job is parsed, but they do not produce a rule, contribute to one, or supply context, so they do not appear in the extracted business rules.


| Statements | How it appears in the output | 
| --- | --- | 
| DD DUMMY / DSN=NULLFILE | Defines a dummy data set. A dummy data set is not recorded as a data set the step reads or writes. | 
| DD SYSOUT= | Routes output to a print class. Print output is not recorded as a data set; the statement appears only in the text of its step. | 
| PEND | Marks the end of an in-stream procedure. It is a structural marker. | 
| JCLLIB | Names the libraries searched for procedures and included groups. The library search order does not affect business logic. | 
| RESTART and RD parameters | Restart a job from a step or checkpoint. Restart options do not affect business logic. | 
| OUTPUT (OUTPUT JCL) | Defines processing options for print output. Print options do not produce business logic. | 
| EXPORT | Makes JCL symbols available to the job step program at run time. It does not produce business logic. | 
| JES2 and JES3 control statements | Give directives to the job entry subsystem, such as /\*JOBPARM, /\*ROUTE, or //\*MAIN. Job entry subsystem directives do not produce business logic. | 
| Null statement (//) | Marks the end of a job or of the input stream. It is a structural marker. | 

## Representing utilities in the rules
<a name="transform-app-mainframe-reimagine-jcl-utilities"></a>

AWS Transform reads the control statements of a recognized utility and describes the business action the step performs, such as copying the transaction records to the backup, rather than the utility or the JCL syntax used to run it. The names of your own business programs are kept. For a utility or vendor program that is not one of these families, the step still generates a rule that names the program, and its control statements are kept as the text of the step without being interpreted; when the source of the program is not among the files you provide, AWS Transform does not infer what the program does. A step that runs IEFBR14, which only allocates or deletes data sets, produces no rule.

### Representing TSO batch
<a name="transform-app-mainframe-reimagine-jcl-utilities-tso"></a>

For IKJEFT01 and IKJEFT1B, AWS Transform reads the TSO commands on SYSTSIN (or on SYSIN when the step has no SYSTSIN). The rule names the program on the RUN PROGRAM command, together with its plan and parameters, rather than IKJEFT01. When the program run is an SQL runner (DSNTEP2, DSNTEP4, DSNTIAD, or DSNTIAUL), the SQL statements on SYSIN and the Db2 tables they reference are carried into the rule. DSNTIAUL is recognized only when it runs under TSO batch.

### Representing sort
<a name="transform-app-mainframe-reimagine-jcl-utilities-sort"></a>

For SORT, DFSORT, ICEMAN, SYNCSORT, and ICETOOL, AWS Transform reads the sort control statements on SYSIN (or SORTCNTL). The rule carries the sort keys or the COPY option, the INCLUDE and OMIT conditions, and, for each OUTFIL statement, the output files and the condition that routes records to them. Other statements, such as INREC, OUTREC, and SUM, are kept as written. Exit routines named on a MODS statement are recorded as programs that the sort calls. For an ICETOOL step, each operator on TOOLIN, such as COPY, COUNT, SELECT, or SPLICE, is carried into the rule with its operands.

### Representing access method services
<a name="transform-app-mainframe-reimagine-jcl-utilities-idcams"></a>

For IDCAMS, the step itself does not produce a rule. Each command that creates, copies, modifies, or deletes data sets or their contents (REPRO, DELETE, DEFINE, BLDINDEX, IMPORT, EXPORT, ALTER) generates its own rule. Listing and verification commands do not.

### Representing Db2 utilities
<a name="transform-app-mainframe-reimagine-jcl-utilities-db2"></a>

For DSNUTILB and DSNUTPN, the first utility statement on SYSIN, such as LOAD, UNLOAD, REORG, or RUNSTATS, identifies the operation, and the tables named on LOAD and UNLOAD statements are recorded. For DSNTEP2, DSNTEP4, and DSNTIAD, the SQL statements on SYSIN and the tables they reference are carried into the rule; Db2 catalog tables are left out.

### Representing copy and update utilities
<a name="transform-app-mainframe-reimagine-jcl-utilities-copy"></a>

For IEBCOPY, IEBGENER, IEBUPDTE, and SYNCGENR, the rule describes a copy or an update and names the members that the SELECT and EXCLUDE statements (or, for IEBUPDTE, the ./ ADD statements) include or skip. An IEBGENER step without control statements is represented as a plain copy.

### Representing IMS and z/OS UNIX
<a name="transform-app-mainframe-reimagine-jcl-utilities-ims"></a>

For IMS (DFSRRC00) and z/OS UNIX (BPXBATCH and BPXBATSL), AWS Transform reads the program and its arguments from the PARM parameter and names them in the rule.

### Control statements in a library member
<a name="transform-app-mainframe-reimagine-jcl-utilities-library"></a>

Control statements can be in a library member instead of in-stream. When the control data definition points to a library member, for example DSN=PROD.CNTL(PAYSORT), AWS Transform looks for that member among the source files you provide. If the member is not found, the rule names the utility but does not describe the operation it performs. Include your control-statement libraries in the source files.

## Example – A utility step that generates a rule
<a name="transform-app-mainframe-reimagine-jcl-example"></a>

The following JCL IDCAMS step copies the payroll primary file to its backup. The REPRO command generates a rule; the LISTCAT command, which only lists catalog entries, does not:

```
//STEP03   EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
  REPRO INDATASET(PAY.PRIMARY) OUTDATASET(PAY.PRIMARY.BACKUP)
  LISTCAT ENTRIES(PAY.PRIMARY.BACKUP)
/*
```

The step behaves as follows:
+ The `REPRO` command generates the rule, a copy of the payroll primary file to its backup data set.
+ The `LISTCAT` command is a listing operation and generates no rule.