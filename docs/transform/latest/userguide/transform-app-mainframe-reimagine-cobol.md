

# COBOL z/OS
<a name="transform-app-mainframe-reimagine-cobol"></a>

This reference describes how the statements in a COBOL program contribute to the business rules and requirements produced by the reimagine workflow. The output is a set of business rules, not a classification of statements; the categories used here are an aid to understanding what appears in the rules. Statements are grouped by function.

For the definitions of the representation categories used on this page, see [Supported languages for business rules extraction](transform-app-mainframe-reimagine-supported.md). A short section lists COBOL elements that are recognized but are not represented in the extracted rules.

AWS Transform analyzes z/OS COBOL. It also recognizes CA-IDMS data-manipulation statements and some OS/VS COBOL constructs (such as `EXAMINE` and `TRANSFORM`). You do not select a dialect; AWS Transform recognizes these forms wherever they appear in your source.

## What is analyzed
<a name="transform-app-mainframe-reimagine-cobol-analyzed"></a>

**How programs are recognized**  
A source member is treated as COBOL from its file type and content. Each program is read in full, including its data declarations and its PROCEDURE DIVISION, so that the rules reference the fields, records, and files the program actually declares.

**Source formats and preprocessing**  
Source is read in the traditional fixed-column layout, with its sequence area, indicator area (for example a continuation or comment marker), and continuation lines. Copybooks are resolved and expanded before the program is analyzed, so the copied text is treated like any other source.

**Missing source**  
AWS Transform analyzes the source you provide. When a referenced artifact is missing, for example an unresolved copybook, the missing part is ignored. Business rules are still produced for the rest of the program. Rules may be degraded around the affected area.

## Statements that generate a rule
<a name="transform-app-mainframe-reimagine-cobol-generates"></a>

These statements anchor business rules. AWS Transform builds a rule around each one and describes the surrounding logic in relation to it. For a call, whether a rule is generated depends on what the call resolves to, as the CALL row below describes.


| Statements | How it appears in the output | 
| --- | --- | 
| WRITE, REWRITE, DELETE (file) | Data changes to a file generate rules that store, modify, or remove records in a data store. | 
| CALL (with the resolved program as the target) | Calls to programs generate rules describing the invocation, resolved to the target program where possible. Calls to a z/OS Language Environment callable service (for example a condition-handling or date/time service, identified by its CEE-prefixed name) are excluded because they carry no business logic. | 
| A statement writing a LINKAGE SECTION field | Writing a value into a LINKAGE SECTION field generates a rule: the field is caller-visible, so the write is the output the program returns to its caller, named by the enclosing 01-level record. A write to the CICS exec interface block (DFHEIBLK) is CICS-managed plumbing and is excluded. | 
| EXEC CICS data and transfer commands (WRITE, REWRITE, DELETE, SEND MAP, LINK, XCTL, RETURN) | CICS data changes, screen sends, and program transfers generate rules. A SEND MAP generates a rule that presents the named screen. | 
| EXEC SQL INSERT, UPDATE, DELETE, EXECUTE | Embedded SQL data changes generate rules that add, modify, or remove database rows. EXECUTE covers dynamically built SQL. The tables and columns these rules bind to are grounded by the Db2 artifacts (DDL, DCLGEN). | 
| DL/I change calls (ISRT, REPL, DLET), issued through CBLTDLI or EXEC DLI | DL/I inserts, replaces, and deletes generate rules that change an IMS segment. For a "get hold" retrieval that precedes a replace or delete, the rule is built around the change. The segments and keys these rules act on are grounded by the IMS artifacts (DBD, PSB/PCB). | 
| CALL to an IBM MQ interface routine (for example, MQPUT, MQPUT1) | A message-queue put generates a rule describing the output to the queue. MQ is recognized by the called routine, not by dedicated syntax; queue handles and options are carried as the values passed to the call. | 
| SORT, MERGE with a GIVING or USING file | A sort or merge that writes its ordered result to an output file generates a rule describing the records written to that file. | 

## Statements that contribute to a rule
<a name="transform-app-mainframe-reimagine-cobol-contributes"></a>

These statements do not produce a rule on their own. Their effect enters the wording of a nearby rule, as its conditions, computations, retrievals, and decisions, or as the value movement and initialization it depends on. For example, initializing a total is expressed as part of the rule that accumulates into it.

### Data access
<a name="transform-app-mainframe-reimagine-cobol-contributes-data"></a>

The following table lists the COBOL statements that access data in a file or database.


| Statements | How it appears in the output | 
| --- | --- | 
| READ, START (file), EXEC CICS READ, STARTBR, READNEXT, READPREV | Data retrieval is described as looking up or reading records, keyed or sequential, as part of the rule that acts on the data. | 
| EXEC SQL singleton SELECT INTO, and cursor FETCH | An embedded SQL retrieval reads from one or more tables into host variables; its result and selection criteria contribute to the rule that acts on the retrieved data. | 
| DL/I retrieval calls (GU, GN, GNP and the hold variants), issued through CBLTDLI or EXEC DLI | A DL/I retrieval is described as reading a segment occurrence, with its segment and qualification, as part of the rule that acts on the retrieved data. | 
| OPEN, CLOSE, EXEC CICS ENDBR | File open and close, and browse termination, are described as part of the rule whose data access they support. | 

### Control flow and decisions
<a name="transform-app-mainframe-reimagine-cobol-contributes-flow"></a>

The following table lists the statements that control the flow of a program and its decisions.


| Statements | How it appears in the output | 
| --- | --- | 
| IF, ELSE, END-IF, EVALUATE, WHEN, END-EVALUATE | Decisions become the conditions and branches of a rule. | 
| PERFORM (inline, out-of-line, UNTIL, VARYING, TIMES, THRU) | The logic a PERFORM runs is included in the rules of the paragraphs it drives, and the clauses that control it (UNTIL, VARYING, TIMES) are reflected as the repetition or condition under which that logic runs. | 
| SEARCH, SEARCH ALL | Table searches are described by the entry they find and the condition they match. | 
| GO TO, ALTER, CONTINUE, NEXT SENTENCE | Branching and no-op flow are followed as part of the program's control flow. | 
| Program-end and return statements (STOP RUN, GOBACK, EXIT, EXIT PROGRAM) | These close the program's logic; AWS Transform follows them as control flow and the statement itself does not become a rule. A condition that guards such a statement (for example IF ... GOBACK) still appears as a decision, with one branch ending the program's flow. | 

### Computation and data movement
<a name="transform-app-mainframe-reimagine-cobol-contributes-compute"></a>

The following table lists the statements that compute values, move data, and manage working storage.


| Statements | How it appears in the output | 
| --- | --- | 
| COMPUTE, ADD, SUBTRACT, MULTIPLY, DIVIDE | Arithmetic is described as the calculation it performs. | 
| STRING, UNSTRING, INSPECT, EXAMINE | String operations are described by their effect on the text value or on the count they return. | 
| MOVE, SET, INITIALIZE, TRANSFORM | Value movement and initialization are preserved in the rule that uses the value, rather than reported as rules of their own. | 
| SORT, MERGE, RELEASE, RETURN | An internal sort or merge is described as part of the processing of the records it orders, together with its input and output procedures. | 

### Screen interaction and error handling
<a name="transform-app-mainframe-reimagine-cobol-contributes-screen"></a>

The following table lists the statements that handle screen interaction and errors.


| Statements | How it appears in the output | 
| --- | --- | 
| EXEC CICS RECEIVE MAP, ACCEPT, DISPLAY | Reading from a screen and console input and output are described as part of the surrounding screen interaction that the operator responds to. | 
| EXEC CICS HANDLE CONDITION, HANDLE AID, HANDLE ABEND; declaratives (USE, DECLARATIVES) | Condition and error handling is described as the handling that applies when an operation fails or a key is pressed. | 

## Statements that shape rules as context
<a name="transform-app-mainframe-reimagine-cobol-context"></a>

Declarations and divisions do not become rules themselves. They resolve the fields, records, files, keys, and resources that the rules reference, so they shape the content of the rules around them. The following table lists these declarations and divisions.


| Constructs | How it appears in the output | 
| --- | --- | 
| DATA DIVISION entries (WORKING-STORAGE, LOCAL-STORAGE, LINKAGE SECTION, level numbers, PIC, VALUE, OCCURS, REDEFINES, 88 condition names) | Data declarations resolve the fields and records that the rules reference, including the conditions that condition names stand for and the overlapping layouts that redefinitions establish. | 
| FILE SECTION: FD/SD entries and ENVIRONMENT DIVISION SELECT and ASSIGN clauses | File descriptions and their SELECT assignments resolve the files, record layouts, access modes, and keys that the file rules reference. | 
| COPY, COPY with the REPLACING phrase, and REPLACE | Copybooks are brought in and expanded before extraction; the copied text is treated like any other source, and the directive itself carries no rule. | 
| IDENTIFICATION, ENVIRONMENT, and PROCEDURE DIVISION USING headers | Division and program headers establish the program and the parameters passed to it, which the call rules reference. | 
| SQL and DL/I definitions: EXEC SQL DECLARE (cursor, table), EXEC SQL INCLUDE, PCB/PSB references | SQL cursor and table declarations and the IMS program's access blocks resolve the tables, columns, segments, and database views that the executable rules reference. | 

## COBOL statements not represented in the rules
<a name="transform-app-mainframe-reimagine-cobol-not-represented"></a>

The following statements are recognized when AWS Transform reads a COBOL program, but they do not appear as rules of their own and do not change the logic that other rules describe. They are followed where they affect control flow, for example, a program end stops the logic that follows it, but they carry no business meaning on their own.


| Statements | How it appears in the output | 
| --- | --- | 
| IMS and database housekeeping calls (CHKP, XRST, TERM) | Checkpoint, restart, and terminate calls carry no business meaning as a database operation and do not generate a rule. | 
| Transaction-control statements (COMMIT, ROLLBACK) | These mark transaction boundaries; the data changes they commit are described by their own rules. | 
| Diagnostic and listing statements (such as EXHIBIT and DISPLAY used only for tracing) | These do not generate business rules. | 
| BMS map definitions (the .bms source) | The screen layout is used to generate the modernized user interface, not to extract business rules; its field geometry does not appear in the rules. The SEND MAP and RECEIVE MAP statements that use the map are represented in control flow. | 
| MQ-specific options (such as queue-manager options) | The message put itself generates a rule; MQ-specific details beyond the queue handle and the message passed are not extracted as separate facts. | 

## Example – Flagging a high-balance account
<a name="transform-app-mainframe-reimagine-cobol-example"></a>

The following fragment reads a customer account record, checks its balance, and writes an updated record when the balance is over a threshold:

```
    READ ACCOUNT-FILE
        INVALID KEY
            MOVE 'N' TO WS-FOUND
    END-READ

    IF WS-FOUND = 'Y' AND ACCT-BALANCE > 10000
        MOVE 'FLAGGED' TO ACCT-STATUS
        REWRITE ACCOUNT-RECORD
    END-IF
```
+ The `READ` and the `IF` condition on `ACCT-BALANCE` contribute to the rule: they describe how the account record is retrieved and the condition under which it is updated.
+ The `REWRITE` is the statement that generates the rule, a data change to a file, and the rule produced from this fragment describes updating an account's status to `FLAGGED` when its balance exceeds the threshold.
+ The intervening `MOVE` statements do not appear as rules of their own; the values they set are carried into the rule that uses them.