

# PL/I
<a name="transform-app-mainframe-reimagine-pli"></a>

This reference describes how the statements in a PL/I program contribute to the business rules and requirements produced by the reimagine workflow. The output is a set of business rules, not a classification of statements; the categories used here are an aid to understanding what appears in the rules. Statements are grouped by function.

For the definitions of the representation categories used on this page, see [Supported languages for business rules extraction](transform-app-mainframe-reimagine-supported.md). A short final section lists PL/I statements that are recognized but are not represented in the extracted rules.

## Statements that generate a rule
<a name="transform-app-mainframe-reimagine-pli-generates"></a>

These statements anchor business rules. AWS Transform builds a rule around each one and describes the surrounding logic in relation to it.


| Statements | How it appears in the output | 
| --- | --- | 
| WRITE, REWRITE, DELETE, LOCATE (record output) | Record output generates rules that store, modify, or remove records in a file or data set, resolved to the file named in the statement. | 
| PUT FILE (stream output) | Stream output to a named file generates a rule that writes the listed values to that file. A PUT without a FILE option, which writes to SYSPRINT, generates a rule only when it is the program's sole output and the values it writes come from data the program read (see the next section). | 
| Assignment to a procedure parameter, RETURN with a value | Writing a value into a parameter of the procedure, including through a pointer to the parameter, or returning a value, generates a rule describing the result handed back to the caller. | 
| CALL to an external program or entry variable, EXEC CICS LINK, EXEC CICS XCTL | Calls to other programs generate rules describing the invocation, resolved to the target program where possible. Calls to Language Environment callable services (CEE routines such as CEEDAYS or CEESECS) generate a rule the same way. The Language Environment condition-handling, abend, and dump services (CEE3ABD, CEE3AB2, CEE3DMP, CEE3GRN, CEE3GRO, CEEHDLR, CEESGL) do not generate a rule. | 
| EXEC SQL INSERT, UPDATE, DELETE, EXECUTE | Embedded SQL data changes generate rules that add, modify, or remove database data, resolved to the table. | 
| EXEC CICS WRITE, REWRITE, DELETE, WRITEQ, DELETEQ, SEND, START | CICS file, queue, terminal, and transaction output generates rules describing the data written or the transaction started. | 
| EXEC CICS SEND MAP | Sending a BMS map generates a rule that presents the screen, with its fields described when the map definition is available. | 
| CALL PLITDLI, CEETDLI, AIBTDLI, ASMTDLI, AERTDLI (GU, GN, GHU, GHN, GNP, GHNP, ISRT, REPL, DLET) | IMS DL/I calls generate rules that retrieve, insert, replace, or delete database segments, identified by the DL/I function code. A call with any other function code, including the checkpoint and restart calls CHKP and XRST, also generates a rule; that rule describes a call to the DL/I interface, not a database operation. | 
| CALL MQPUT, MQPUT1 | Putting a message on an IBM MQ queue generates a rule describing the message sent. | 

## Statements that contribute to a rule
<a name="transform-app-mainframe-reimagine-pli-contributes"></a>

These statements do not produce a rule on their own. Their effect enters the wording of a nearby rule, as its conditions, computations, retrievals, and decisions, or as the value movement, initialization, file opening and closing, and pointer setup it depends on. For example, opening a file is expressed as part of the rule that writes to it.

### Data access
<a name="transform-app-mainframe-reimagine-pli-contributes-data"></a>

The following statements retrieve data from files, databases, and queues.


| Statements | How it appears in the output | 
| --- | --- | 
| READ (INTO, SET, KEY) | Record retrieval is described as reading records, keyed or sequential, as part of the rule that acts on the data. | 
| GET (LIST, EDIT, DATA; FILE or STRING) | Stream input is described as the values obtained, as part of the rule that uses them. | 
| OPEN, CLOSE, FLUSH | File lifecycle control is described as part of the rule whose file access it supports. | 
| EXEC SQL SELECT INTO, OPEN, FETCH, CLOSE, PREPARE | Database retrieval and cursor handling are described as looking up or reading rows from the table, as part of the rule that acts on the data. The table is named rather than the cursor. | 
| EXEC CICS READ, READNEXT, READPREV, STARTBR, READQ, RECEIVE, RECEIVE MAP, RETRIEVE, ASKTIME, SYNCPOINT | CICS retrieval and control operations are described as part of the rule whose data they feed. Receiving a map captures the operator's input for the rule that processes it. | 
| CALL MQOPEN, MQGET, MQCLOSE | Queue connection and message retrieval are described as part of the rule that processes the message. | 

### Control flow and decisions
<a name="transform-app-mainframe-reimagine-pli-contributes-flow"></a>

The following statements control the flow of the program and its decisions.


| Statements | How it appears in the output | 
| --- | --- | 
| IF, THEN, ELSE | Decisions become the conditions and branches of a rule. | 
| SELECT, WHEN, OTHERWISE | Each WHEN branch with a distinct outcome is described as its own condition and result; OTHERWISE is described as the default case. | 
| DO WHILE, DO UNTIL, DO (iterative TO, BY, REPEAT, value list), DO LOOP, DO FOREVER, DO groups | Iteration is described as processing that repeats over a set of data or until a condition is met. | 
| LEAVE, ITERATE | Loop exits and early continuation are described as the condition under which the processing stops or skips an item. | 
| GO TO (to a label) | Branching to a label is followed as part of the program's control flow. | 
| CALL to an internal procedure, function reference to an internal procedure | Internal procedure logic is included as part of the rules of the procedures that call it. | 
| RETURN, STOP, EXIT | Ending a procedure or the program is described as the completion of the processing. | 
| BEGIN blocks | Statements inside a BEGIN block are analyzed as part of the enclosing procedure. | 

### Conditions and errors
<a name="transform-app-mainframe-reimagine-pli-contributes-conditions"></a>

The following statements handle conditions and errors.


| Statements | How it appears in the output | 
| --- | --- | 
| ON ENDFILE, ENDPAGE, KEY, UNDEFINEDFILE, TRANSMIT, RECORD | Establishing a handler for a file condition contributes the condition (for example, end of file reached or key not found) to the rule whose file operation can raise it. A status variable set inside the handler is followed as data in the rules that test it. | 
| SIGNAL, ON CONDITION, ON ERROR and other ON units | Handler logic entered explicitly with SIGNAL is included as part of the rules of the signaling procedure. Handlers for conditions raised by the runtime rather than by SIGNAL are described as the handling that applies when the operation fails. | 
| REVERT, ON SYSTEM | Restoring default condition handling is described as part of the surrounding processing. | 
| EXEC CICS HANDLE ABEND, HANDLE CONDITION; EXEC SQL WHENEVER | Error-handling registrations are described as the handling that applies when a CICS or SQL operation fails, and the branch they take is followed. | 

### Computation and data movement
<a name="transform-app-mainframe-reimagine-pli-contributes-compute"></a>

The following statements compute values, move data, and manage storage.


| Statements | How it appears in the output | 
| --- | --- | 
| Assignment (=, compound operators, BY NAME) | Assignments that carry a calculation are described as computing the result; plain value movement is preserved in the rule that uses the moved value. | 
| Built-in functions (string, arithmetic, date and time, conversion) and pseudovariables (SUBSTR, UNSPEC) | Built-in functions are described by their effect on the value they produce or modify. | 
| Pointer and based storage (ADDR, pointer assignment, BASED, DEFINED, UNION, structure and array references) | Data accessed through pointers, overlays, and structure members is followed to the underlying storage, so rules name the business fields rather than the pointer. | 
| ALLOCATE, FREE | Storage allocation and release are preserved in the rule whose data they prepare. | 
| FETCH, RELEASE, DELAY, DISPLAY | Dynamic program loading, waits, and operator messages are described as the action they perform, as part of the surrounding rule. | 
| CALL to PL/I built-in subroutines (PLIRETC, PLIMOVE, PLIFILL, PLIOVER, PLISRTD, PLISAXA, PLISAXB, PLISAXC, PLIEBCDIC) | Return-code setting, storage moves, sorting, XML parsing, and character conversion are described by the value they set or arrange. For the full list of supported built-in subroutines, see [Language level and runtime services](#transform-app-mainframe-reimagine-pli-support). | 

## Statements that shape rules as context
<a name="transform-app-mainframe-reimagine-pli-context"></a>

Declarations and program structure do not become rules themselves. They resolve the fields, records, files, keys, and resources that the rules reference, so they shape the content of the rules around them.


| Constructs | How it appears in the output | 
| --- | --- | 
| DECLARE / DCL (data, structures, arrays, PICTURE, INITIAL, LIKE, DEFINED, BASED, CONTROLLED, UNION, REFER, FILE and ENTRY declarations), DEFAULT | Declarations define the data, files, and entry points that the rules reference, including the layout of the records that are read and written. | 
| DEFINE ALIAS, DEFINE ORDINAL, DEFINE STRUCTURE | Type definitions resolve the types of the data the rules reference. | 
| PROCEDURE, ENTRY, END, PACKAGE, OPTIONS(MAIN), RETURNS | Program structure defines the procedures and entry points whose rules are extracted and the parameters they exchange. | 
| %INCLUDE, -INC, \+\+INCLUDE, EXEC SQL INCLUDE | Include directives bring in source before extraction; the included statements are analyzed in the including program and carry no rule of their own. | 
| Preprocessor macros (%IF, %DO, %DECLARE, %ACTIVATE, %REPLACE, preprocessor procedures) | Preprocessor macros are not supported. A program that uses them is analyzed on a best-effort basis: a macro that cannot be resolved leaves the analysis of that program incomplete. For complete rules, provide the source as produced by the preprocessor. See [Language level and runtime services](#transform-app-mainframe-reimagine-pli-support). | 
| EXEC SQL DECLARE CURSOR, DECLARE TABLE, INCLUDE SQLCA | Declarations establish the cursor or table that the executable SQL rules reference. | 
| Database artifacts (Db2 table, column, and view definitions; IMS segment and view definitions) | PL/I programs reach Db2 through embedded SQL, and IMS databases through DL/I calls. The rules reference table, column, segment, and view definitions. These are resolved from the database artifacts in your source and attached to the rules that use them. | 
| \*PROCESS, condition prefixes, labels, comments | Compiler options, checking prefixes, and labels carry no business rule of their own. Comments are kept with the statements they describe. | 

## PL/I statements not represented in the rules
<a name="transform-app-mainframe-reimagine-pli-not-represented"></a>

The following statements are recognized when AWS Transform reads a PL/I program, but they do not appear as rules of their own and do not change the logic that other rules describe.


| Statements | How it appears in the output | 
| --- | --- | 
| Transaction-control statements (EXEC SQL COMMIT, ROLLBACK) | These mark transaction boundaries and do not appear in the rules. The rules of the statements that make the data changes describe what the transaction commits or rolls back. | 
| Diagnostic and dump calls (PLIDUMP, the Language Environment condition-handling, abend, and dump services such as CEE3ABD, CEE3DMP, CEEHDLR, CEESGL) | These are recognized as diagnostic calls and do not generate business rules. | 
| EXEC DLI command-level statements | Command-level DL/I statements are not analyzed. IMS database access is analyzed through the DL/I call interface (CALL PLITDLI and the related entry points). | 

## Language level and runtime services
<a name="transform-app-mainframe-reimagine-pli-support"></a>

This section describes the PL/I language level that AWS Transform reads, how it handles preprocessing and include directives, and the built-in subroutines and runtime services it recognizes.

### Include directives and macros
<a name="transform-app-mainframe-reimagine-pli-preprocessing"></a>

**Include directives.** Include directives (`%INCLUDE`, `-INC`, `++INCLUDE`, and `EXEC SQL INCLUDE`) are expanded before analysis when the included members are part of the input, so statements that come from an included member are analyzed in the program that includes them. When an included member is missing, the analysis of that program is incomplete and the rules extracted from it can be partial; to obtain complete rules, provide the missing members.

**Macros.** Preprocessor macros (`%` directives and preprocessor procedures) are not supported. A program that uses them is analyzed on a best-effort basis. When a macro cannot be resolved, the analysis of that program is incomplete and the rules extracted from it can be partial. To obtain complete rules, provide the source as produced by the preprocessor (macros already expanded).

### Built-in subroutines and runtime services
<a name="transform-app-mainframe-reimagine-pli-builtins"></a>

AWS Transform handles the following built-in subroutines and runtime services. Each term lists the calls and how they appear in the rules.

`PLIRETC`  
Sets the program return code. Contributes to the rules around it.

`PLIMOVE`, `PLIFILL`, `PLIOVER`  
Moves or fills storage. Contributes to the rules around it.

`PLISRTD`  
Sorts records. Contributes to the rules around it.

`PLISAXA`, `PLISAXB`, `PLISAXC`  
Parses XML. Contributes to the rules around it.

`PLIEBCDIC`  
Converts character data. Contributes to the rules around it.

`CEEDAYS`, `CEESECS`, `CEEDATE` (Language Environment callable services)  
Generate a rule describing the call, like any external call.

`PLIDUMP`  
Recognized as a diagnostic call and left out of the rules.

`CEE3ABD`, `CEE3AB2`, `CEE3DMP`, `CEE3GRN`, `CEE3GRO`, `CEEHDLR`, `CEESGL` (condition-handling, abend, and dump services)  
Do not generate rules of their own.

Other built-in subroutines (`PLISRTA`, `PLISRTB`, `PLISRTC`, `PLISAXD`, `PLIASCII`, `PLICKPT`, `PLICANC`, `PLIREST`, `PLIFREE`, `PLIDELETE`, `PLITRAN`)  
Not supported. The call is left out of the analysis, and the rest of the program is analyzed normally.

## Example – Rewriting a record on a condition
<a name="transform-app-mainframe-reimagine-pli-example"></a>

The following PL/I fragment reads a customer record, raises its balance when the account is active, and rewrites the record:

```
READ FILE(CUST) INTO(CUST_REC) KEY(CUST_ID);
IF STATUS = 'A' THEN
  DO;
    BALANCE = BALANCE + INCREASE;
    REWRITE FILE(CUST) FROM(CUST_REC) KEY(CUST_ID);
  END;
```

In this fragment:
+ The `READ` and the `IF` test on `STATUS` contribute to the rule: they describe how the record is retrieved and the condition under which it is changed.
+ The `REWRITE` is the statement that generates the rule, record output that modifies a record in the `CUST` file, and the rule describes raising the balance of an active customer.