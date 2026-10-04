

# Built-in function and system object rules
<a name="sc-default-rules-builtins-oracle"></a>

DMS Schema Conversion applies default rules to convert Oracle built-in functions, packages, procedures, and system objects when it converts a source schema to Amazon Aurora PostgreSQL-Compatible Edition or Amazon RDS for PostgreSQL. The following sections list the source objects in each package and show how DMS Schema Conversion converts each one.

Each table uses the following columns:
+ **Source** – the Oracle built-in function, package, procedure, or system object.
+ **Conversion** – how DMS Schema Conversion converts the object. A value of `Same name` means a direct mapping, `Renamed` means the object maps to a target with a different name, `Rewritten` means DMS Schema Conversion rewrites the object as a target expression, `Extension pack` means the conversion uses a function from the DMS Schema Conversion extension pack, and `Not converted` means DMS Schema Conversion does not convert the object automatically.
+ **Target** – the target object or expression that DMS Schema Conversion produces.
+ **Action item** – the action item code that DMS Schema Conversion reports for the object. An action item can mean that the object needs manual work, or be informational about an object that DMS Schema Conversion converted.

**Note**  
**Extension pack helper names.** Helper functions are named `<package>$<member>`. DMS Schema Conversion copies the member name with the spelling used in your source call, so `htp.htmlOpen` becomes `aws_oracle_ext.htp$htmlOpen` and `HTP.HTMLOPEN` becomes `aws_oracle_ext.htp$HTMLOPEN`. Because the call is not quoted, PostgreSQL treats all these spellings as the same function.  
**Object member calls.** Where a source built-in is a method called on an object — a member of the Oracle `ANYDATA` or `XMLTYPE` type — the object becomes the helper's first argument: `v.data.AccessDate()` becomes `aws_oracle_ext.sys_anydata$AccessDate(v.data)`.

## Terms used in this topic
<a name="sc-default-rules-builtins-terms-oracle"></a>

The following table defines the terms that describe each conversion outcome.


| Term | Meaning | 
| --- | --- | 
| Same name | Converted automatically to a target object of the same name. | 
| Renamed | Converted automatically to a differently named target equivalent. | 
| Rewritten | Replaced by an equivalent native expression. | 
| Extension pack | DMS Schema Conversion converts the call to a function in the AWS DMS extension pack, a helper schema that emulates source functions with no PostgreSQL equivalent (aws\_oracle\_ext for Oracle sources, aws\_sqlserver\_ext for SQL Server sources). Apply the extension pack to your target database before you run the converted code. | 
| Not converted | No automatic conversion. An action item is raised and the code needs manual work. | 

## DBMS\_AQ
<a name="sc-default-rules-builtins-oracle-dbms-aq"></a>

The following table lists each source object in the DBMS\_AQ package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_AQ.BEFORE | Extension pack | aws\_oracle\_ext.sqs\_before() | None | 
| DBMS\_AQ.BROWSE | Extension pack | aws\_oracle\_ext.sqs\_browse() | None | 
| DBMS\_AQ.DEQUEUE | Extension pack | aws\_oracle\_ext.dbms\_aq$dequeue(…), with record arguments wrapped in to\_json() | None | 
| DBMS\_AQ.DEQUEUE\_OPTIONS\_T | Extension pack | aws\_oracle\_ext.dbms\_aq$dequeue\_options\_t | None | 
| declaration of DBMS\_AQ.DEQUEUE\_OPTIONS\_T | Extension pack | aws\_oracle\_ext.sqs\_init\_dbms\_aq$dequeue\_options\_t() initialiser | None | 
| DBMS\_AQ.ENQUEUE | Extension pack | aws\_oracle\_ext.dbms\_aq$enqueue(…), with record arguments wrapped in to\_json() | None | 
| DBMS\_AQ.ENQUEUE\_OPTIONS\_T | Extension pack | aws\_oracle\_ext.dbms\_aq$enqueue\_options\_t | None | 
| declaration of DBMS\_AQ.ENQUEUE\_OPTIONS\_T | Extension pack | aws\_oracle\_ext.sqs\_init\_dbms\_aq$enqueue\_options\_t() initialiser | None | 
| DBMS\_AQ.EXPIRED | Extension pack | aws\_oracle\_ext.sqs\_expired() | None | 
| DBMS\_AQ.FIRST\_MESSAGE | Extension pack | aws\_oracle\_ext.sqs\_first\_message() | None | 
| DBMS\_AQ.FOREVER | Extension pack | aws\_oracle\_ext.sqs\_forever() | None | 
| DBMS\_AQ.IMMEDIATE | Extension pack | aws\_oracle\_ext.sqs\_immediate() | None | 
| DBMS\_AQ.LOCKED | Extension pack | aws\_oracle\_ext.sqs\_locked() | None | 
| DBMS\_AQ.MESSAGE\_PROPERTIES\_T | Extension pack | aws\_oracle\_ext.dbms\_aq$message\_properties\_t | None | 
| declaration of DBMS\_AQ.MESSAGE\_PROPERTIES\_T | Extension pack | aws\_oracle\_ext.sqs\_init\_dbms\_aq$message\_properties\_t() initialiser | None | 
| DBMS\_AQ.NAMESPACE\_ANONYMOUS | Extension pack | aws\_oracle\_ext.sqs\_namespace\_anonymous() | None | 
| DBMS\_AQ.NAMESPACE\_AQ | Extension pack | aws\_oracle\_ext.sqs\_namespace\_aq() | None | 
| DBMS\_AQ.NEVER | Extension pack | aws\_oracle\_ext.sqs\_never() | None | 
| DBMS\_AQ.NO\_DELAY | Extension pack | aws\_oracle\_ext.sqs\_no\_delay() | None | 
| DBMS\_AQ.NO\_WAIT | Extension pack | aws\_oracle\_ext.sqs\_no\_wait() | None | 
| DBMS\_AQ.NTFN\_GROUPING\_FOREVER | Extension pack | aws\_oracle\_ext.sqs\_ntfn\_grouping\_forever() | None | 
| DBMS\_AQ.NTFN\_GROUPING\_TYPE\_LAST | Extension pack | aws\_oracle\_ext.sqs\_ntfn\_grouping\_type\_last() | None | 
| DBMS\_AQ.NTFN\_GROUPING\_TYPE\_SUMMARY | Extension pack | aws\_oracle\_ext.sqs\_ntfn\_grouping\_type\_summary() | None | 
| DBMS\_AQ.ON\_COMMIT | Extension pack | aws\_oracle\_ext.sqs\_on\_commit() | None | 
| DBMS\_AQ.PROCESSED | Extension pack | aws\_oracle\_ext.sqs\_processed() | None | 
| DBMS\_AQ.READY | Extension pack | aws\_oracle\_ext.sqs\_ready() | None | 
| DBMS\_AQ.REMOVE | Extension pack | aws\_oracle\_ext.sqs\_remove() | None | 
| DBMS\_AQ.REMOVE\_NODATA | Extension pack | aws\_oracle\_ext.sqs\_remove\_nodata() | None | 
| DBMS\_AQ.TOP | Extension pack | aws\_oracle\_ext.sqs\_top() | None | 
| DBMS\_AQ.WAITING | Extension pack | aws\_oracle\_ext.sqs\_waiting() | None | 

## DBMS\_LOB
<a name="sc-default-rules-builtins-oracle-dbms-lob"></a>

The following table lists each source object in the DBMS\_LOB package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_LOB.APPEND | Extension pack | aws\_oracle\_ext.dbms\_lob$append | None | 
| DBMS\_LOB.CALL | Extension pack | aws\_oracle\_ext.dbms\_lob$call() | None | 
| DBMS\_LOB.COMPARE | Extension pack | aws\_oracle\_ext.dbms\_lob$compare | None | 
| DBMS\_LOB.COMPRESS\_OFF | Extension pack | aws\_oracle\_ext.dbms\_lob$compress\_off() | None | 
| DBMS\_LOB.COMPRESS\_ON | Extension pack | aws\_oracle\_ext.dbms\_lob$compress\_on() | None | 
| DBMS\_LOB.CONTENTTYPE\_MAX\_SIZE | Extension pack | aws\_oracle\_ext.dbms\_lob$contenttype\_max\_size() | None | 
| DBMS\_LOB.COPY | Extension pack | aws\_oracle\_ext.dbms\_lob$copy | None | 
| DBMS\_LOB.CREATETEMPORARY | Extension pack | aws\_oracle\_ext.dbms\_lob$createtemporary | None | 
| DBMS\_LOB.DBFS\_LINK\_CACHE | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_cache() | None | 
| DBMS\_LOB.DBFS\_LINK\_NEVER | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_never() | None | 
| DBMS\_LOB.DBFS\_LINK\_NO | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_no() | None | 
| DBMS\_LOB.DBFS\_LINK\_NOCACHE | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_nocache() | None | 
| DBMS\_LOB.DBFS\_LINK\_PATH\_MAX\_SIZE | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_path\_max\_size() | None | 
| DBMS\_LOB.DBFS\_LINK\_YES | Extension pack | aws\_oracle\_ext.dbms\_lob$dbfs\_link\_yes() | None | 
| DBMS\_LOB.DEDUPLICATE\_OFF | Extension pack | aws\_oracle\_ext.dbms\_lob$deduplicate\_off() | None | 
| DBMS\_LOB.DEDUPLICATE\_ON | Extension pack | aws\_oracle\_ext.dbms\_lob$deduplicate\_on() | None | 
| DBMS\_LOB.DEFAULT\_CSID | Extension pack | aws\_oracle\_ext.dbms\_lob$default\_csid() | None | 
| DBMS\_LOB.DEFAULT\_LANG\_CTX | Extension pack | aws\_oracle\_ext.dbms\_lob$default\_lang\_ctx() | None | 
| DBMS\_LOB.ENCRYPT\_OFF | Extension pack | aws\_oracle\_ext.dbms\_lob$encrypt\_off() | None | 
| DBMS\_LOB.ENCRYPT\_ON | Extension pack | aws\_oracle\_ext.dbms\_lob$encrypt\_on() | None | 
| DBMS\_LOB.ERASE | Extension pack | aws\_oracle\_ext.dbms\_lob$erase | None | 
| DBMS\_LOB.FILEOPEN | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_LOB.FILEOPEN function | 
| DBMS\_LOB.FILE\_READONLY | Extension pack | aws\_oracle\_ext.dbms\_lob$file\_readonly() | None | 
| DBMS\_LOB.FREETEMPORARY | Extension pack | aws\_oracle\_ext.dbms\_lob$freetemporary | None | 
| DBMS\_LOB.GETLENGTH | Extension pack | aws\_oracle\_ext.dbms\_lob$getlength | None | 
| DBMS\_LOB.INSTR | Extension pack | aws\_oracle\_ext.dbms\_lob$instr | None | 
| DBMS\_LOB.ISTEMPORARY | Extension pack | aws\_oracle\_ext.dbms\_lob$istemporary | None | 
| DBMS\_LOB.LOBMAXSIZE | Extension pack | aws\_oracle\_ext.dbms\_lob$lobmaxsize() | None | 
| DBMS\_LOB.LOB\_READONLY | Extension pack | aws\_oracle\_ext.dbms\_lob$lob\_readonly() | None | 
| DBMS\_LOB.LOB\_READWRITE | Extension pack | aws\_oracle\_ext.dbms\_lob$lob\_readwrite() | None | 
| DBMS\_LOB.NO\_WARNING | Extension pack | aws\_oracle\_ext.dbms\_lob$no\_warning() | None | 
| DBMS\_LOB.OPT\_COMPRESS | Extension pack | aws\_oracle\_ext.dbms\_lob$opt\_compress() | None | 
| DBMS\_LOB.OPT\_DEDUPLICATE | Extension pack | aws\_oracle\_ext.dbms\_lob$opt\_deduplicate() | None | 
| DBMS\_LOB.OPT\_ENCRYPT | Extension pack | aws\_oracle\_ext.dbms\_lob$opt\_encrypt() | None | 
| DBMS\_LOB.READ | Extension pack | aws\_oracle\_ext.dbms\_lob$read | None | 
| DBMS\_LOB.SESSION | Extension pack | aws\_oracle\_ext.dbms\_lob$session() | None | 
| DBMS\_LOB.SUBSTR | Extension pack | aws\_oracle\_ext.dbms\_lob$substr | None | 
| DBMS\_LOB.TRANSACTION | Extension pack | aws\_oracle\_ext.dbms\_lob$transaction() | None | 
| DBMS\_LOB.TRIM | Extension pack | aws\_oracle\_ext.dbms\_lob$trim | None | 
| DBMS\_LOB.WARN\_INCONVERTIBLE\_CHAR | Extension pack | aws\_oracle\_ext.dbms\_lob$warn\_inconvertible\_char() | None | 
| DBMS\_LOB.WRITE | Extension pack | aws\_oracle\_ext.dbms\_lob$write | None | 
| DBMS\_LOB.WRITEAPPEND | Extension pack | aws\_oracle\_ext.dbms\_lob$writeappend | None | 

## DBMS\_OUTPUT
<a name="sc-default-rules-builtins-oracle-dbms-output"></a>

The following table lists each source object in the DBMS\_OUTPUT package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_OUTPUT.DISABLE | Extension pack | aws\_oracle\_ext.dbms\_output$disable | None | 
| DBMS\_OUTPUT.ENABLE | Extension pack | aws\_oracle\_ext.dbms\_output$enable | None | 
| DBMS\_OUTPUT.GET\_LINE | Extension pack | aws\_oracle\_ext.dbms\_output$get\_line | None | 
| DBMS\_OUTPUT.GET\_LINES | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_OUTPUT.GET\_LINES function | 
| DBMS\_OUTPUT.NEW\_LINE | Extension pack | aws\_oracle\_ext.dbms\_output$new\_line | None | 
| DBMS\_OUTPUT.PUT | Extension pack | aws\_oracle\_ext.dbms\_output$put | None | 
| DBMS\_OUTPUT.PUT\_LINE | Extension pack | aws\_oracle\_ext.dbms\_output$put\_line | None | 

## DBMS\_XMLQUERY
<a name="sc-default-rules-builtins-oracle-dbms-xmlquery"></a>

The following table lists each source object in the DBMS\_XMLQUERY package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_XMLQUERY.ALL\_ROWS | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$all\_rows() | None | 
| DBMS\_XMLQUERY.CLOSECONTEXT | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$closecontext | None | 
| DBMS\_XMLQUERY.DB\_ENCODING | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$db\_encoding() | None | 
| DBMS\_XMLQUERY.DEFAULT\_DATE\_FORMAT | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$default\_date\_format() | None | 
| DBMS\_XMLQUERY.DEFAULT\_ERRORTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$default\_errortag() | None | 
| DBMS\_XMLQUERY.DEFAULT\_ROWIDATTR | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$default\_rowidattr() | None | 
| DBMS\_XMLQUERY.DEFAULT\_ROWSETTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$default\_rowsettag() | None | 
| DBMS\_XMLQUERY.DEFAULT\_ROWTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$default\_rowidattr() | None | 
| DBMS\_XMLQUERY.DTD | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$dtd() | None | 
| DBMS\_XMLQUERY.GETDTD | Not converted | Not applicable | 5141: DMS SC can't convert the DBMS\_XMLQUERY.GETDTD method | 
| DBMS\_XMLQUERY.GETEXCEPTIONCONTENT | Not converted | Not applicable | 5141: DMS SC can't convert the DBMS\_XMLQUERY.GETEXCEPTIONCONTENT method | 
| DBMS\_XMLQUERY.GETNUMROWSPROCESSED | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$getNumRowsProcessed | None | 
| DBMS\_XMLQUERY.GETVERSION | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$getVersion | None | 
| DBMS\_XMLQUERY.GETXML | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$getxml | 5091: PostgreSQL ignores optional parameters when you call the DBMS\_XMLQUERY.GETXML method | 
| DBMS\_XMLQUERY.LOWER\_CASE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$lower\_case() | None | 
| DBMS\_XMLQUERY.NEWCONTEXT | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$newcontext | 5100: The GETXML call might fail | 
| DBMS\_XMLQUERY.NONE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$none() | None | 
| DBMS\_XMLQUERY.PROPAGATEORIGINALEXCEPTION | Not converted | Not applicable | 5141: DMS SC can't convert the DBMS\_XMLQUERY.PROPAGATEORIGINALEXCEPTION method | 
| DBMS\_XMLQUERY.REMOVEXSLTPARAM | Not converted | Not applicable | 5141: DMS SC can't convert the DBMS\_XMLQUERY.REMOVEXSLTPARAM method | 
| DBMS\_XMLQUERY.SCHEMA | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$schema() | None | 
| DBMS\_XMLQUERY.SETBINDVALUE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setBindValue | 5092: Calling the DBMS\_XMLQUERY.SETBINDVALUE method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETCOLLIDATTRNAME | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setCollIdAttrName | 5092: Calling the DBMS\_XMLQUERY.SETCOLLIDATTRNAME method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETDATAHEADER | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setDataHeader | None | 
| DBMS\_XMLQUERY.SETDATEFORMAT | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setDateFormat | 5092: Calling the DBMS\_XMLQUERY.SETDATEFORMAT method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETENCODINGTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setEncodingTag | 5092: Calling the DBMS\_XMLQUERY.SETENCODINGTAG method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETERRORTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setErrorTag | 5092: Calling the DBMS\_XMLQUERY.SETERRORTAG method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETMAXROWS | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setMaxRows | 5092: Calling the DBMS\_XMLQUERY.SETMAXROWS method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETMETAHEADER | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setMetaHeader | 5092: Calling the DBMS\_XMLQUERY.SETMETAHEADER method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETRAISEEXCEPTION | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRaiseException | 5092: Calling the DBMS\_XMLQUERY.SETRAISEEXCEPTION method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETRAISENOROWSEXCEPTION | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRaiseNoRowsException | 5092: Calling the DBMS\_XMLQUERY.SETRAISENOROWSEXCEPTION method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETROWIDATTRNAME | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRowidAttrName | 5092: Calling the DBMS\_XMLQUERY.SETROWIDATTRNAME method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETROWIDATTRVALUE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRowidAttrValue | 5092: Calling the DBMS\_XMLQUERY.SETROWIDATTRVALUE method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETROWSETTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRowSetTag | None | 
| DBMS\_XMLQUERY.SETROWTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setRowTag | None | 
| DBMS\_XMLQUERY.SETSKIPROWS | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setSkipRows | 5092: Calling the DBMS\_XMLQUERY.SETSKIPROWS method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETSQLTOXMLNAMEESCAPING | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setSQLToXMLNameEscaping | 5092: Calling the DBMS\_XMLQUERY.SETSQLTOXMLNAMEESCAPING method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETSTYLESHEETHEADER | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setStyleSheetHeader | 5092: Calling the DBMS\_XMLQUERY.SETSTYLESHEETHEADER method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETTAGCASE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setTagCase | 5092: Calling the DBMS\_XMLQUERY.SETTAGCASE method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.SETXSLT | Not converted | Not applicable | 5141: DMS SC can't convert the DBMS\_XMLQUERY.SETXSLT method | 
| DBMS\_XMLQUERY.SETXSLTPARAM | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$setXSLTParam | 5092: Calling the DBMS\_XMLQUERY.SETXSLTPARAM method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.UPPER\_CASE | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$upper\_case() | None | 
| DBMS\_XMLQUERY.USENULLATTRIBUTEINDICATOR | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$useNullAttributeIndicator | 5092: Calling the DBMS\_XMLQUERY.USENULLATTRIBUTEINDICATOR method doesn't influence the GETXML call | 
| DBMS\_XMLQUERY.USETYPEFORCOLLELEMTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlquery$useTypeForCollElemTag | 5092: Calling the DBMS\_XMLQUERY.USETYPEFORCOLLELEMTAG method doesn't influence the GETXML call | 

## DBMS\_RANDOM
<a name="sc-default-rules-builtins-oracle-dbms-random"></a>

The following table lists each source object in the DBMS\_RANDOM package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_RANDOM.INITIALIZE | Extension pack | aws\_oracle\_ext.dbms\_random$initialize | None | 
| SYS.DBMS\_RANDOM.NORMAL | Extension pack | aws\_oracle\_ext.dbms\_random$normal | None | 
| SYS.DBMS\_RANDOM.RANDOM | Extension pack | aws\_oracle\_ext.dbms\_random$random | None | 
| SYS.DBMS\_RANDOM.SEED | Extension pack | aws\_oracle\_ext.dbms\_random$seed | None | 
| SYS.DBMS\_RANDOM.STRING | Extension pack | aws\_oracle\_ext.dbms\_random$string | None | 
| SYS.DBMS\_RANDOM.TERMINATE | Extension pack | aws\_oracle\_ext.dbms\_random$terminate | None | 
| SYS.DBMS\_RANDOM.VALUE | Extension pack | aws\_oracle\_ext.dbms\_random$value | None | 

## Jobs
<a name="sc-default-rules-builtins-oracle-jobs"></a>

The following table lists each source object in the Jobs category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_JOB.BROKEN | Extension pack | aws\_oracle\_ext.dbms\_job$broken | None | 
| DBMS\_JOB.CHANGE | Extension pack | aws\_oracle\_ext.dbms\_job$change | None | 
| DBMS\_JOB.INSTANCE | Extension pack | aws\_oracle\_ext.dbms\_job$instance | None | 
| DBMS\_JOB.INTERVAL | Extension pack | aws\_oracle\_ext.dbms\_job$interval | None | 
| DBMS\_JOB.NEXT\_DATE | Extension pack | aws\_oracle\_ext.dbms\_job$next\_date | None | 
| DBMS\_JOB.REMOVE | Extension pack | aws\_oracle\_ext.dbms\_job$remove | None | 
| DBMS\_JOB.RUN | Extension pack | aws\_oracle\_ext.dbms\_job$run | None | 
| DBMS\_JOB.SUBMIT | Extension pack | aws\_oracle\_ext.dbms\_job$submit | None | 
| DBMS\_JOB.USER\_EXPORT | Extension pack | aws\_oracle\_ext.dbms\_job$user\_export | None | 
| DBMS\_JOB.WHAT | Extension pack | aws\_oracle\_ext.dbms\_job$what | None | 

## Mail sending
<a name="sc-default-rules-builtins-oracle-mail-sending"></a>

The following table lists each source object in the Mail sending category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| UTL\_SMTP.AUTH | Extension pack | aws\_oracle\_ext.utl\_smtp$auth | None | 
| UTL\_SMTP.CLOSE\_CONNECTION | Extension pack | aws\_oracle\_ext.utl\_smtp$close\_connection | None | 
| UTL\_SMTP.CLOSE\_DATA | Extension pack | aws\_oracle\_ext.utl\_smtp$close\_data | None | 
| UTL\_SMTP.COMMAND | Not converted | Not applicable | 5501: PostgreSQL doesn't support functionality similar to the UTL\_SMTP.COMMAND module | 
| UTL\_SMTP.COMMAND\_REPLIES | Not converted | Not applicable | 5501: PostgreSQL doesn't support functionality similar to the UTL\_SMTP.COMMAND\_REPLIES module | 
| UTL\_SMTP.CONNECTION | Extension pack | aws\_oracle\_ext.utl\_smtp$connection | None | 
| UTL\_SMTP.DATA | Extension pack | aws\_oracle\_ext.utl\_smtp$data | None | 
| UTL\_SMTP.EHLO | Extension pack | aws\_oracle\_ext.utl\_smtp$ehlo | None | 
| UTL\_SMTP.HELO | Extension pack | aws\_oracle\_ext.utl\_smtp$helo | None | 
| UTL\_SMTP.HELP | Not converted | Not applicable | 5501: PostgreSQL doesn't support functionality similar to the UTL\_SMTP.HELP module | 
| UTL\_SMTP.MAIL | Extension pack | aws\_oracle\_ext.utl\_smtp$mail | None | 
| UTL\_SMTP.NOOP | Extension pack | aws\_oracle\_ext.utl\_smtp$noop | None | 
| UTL\_SMTP.OPEN\_CONNECTION | Extension pack | aws\_oracle\_ext.utl\_smtp$open\_connection | None | 
| UTL\_SMTP.OPEN\_DATA | Extension pack | aws\_oracle\_ext.utl\_smtp$open\_data | None | 
| UTL\_SMTP.QUIT | Extension pack | aws\_oracle\_ext.utl\_smtp$quit | None | 
| UTL\_SMTP.RCPT | Extension pack | aws\_oracle\_ext.utl\_smtp$rcpt | None | 
| UTL\_SMTP.REPLIES | Extension pack | aws\_oracle\_ext.utl\_smtp$replies | None | 
| UTL\_SMTP.REPLY | Extension pack | aws\_oracle\_ext.utl\_smtp$reply | None | 
| UTL\_SMTP.RSET | Extension pack | aws\_oracle\_ext.utl\_smtp$rset | None | 
| UTL\_SMTP.STARTTLS | Extension pack | aws\_oracle\_ext.utl\_smtp$starttls | None | 
| UTL\_SMTP.VRFY | Not converted | Not applicable | 5501: PostgreSQL doesn't support functionality similar to the UTL\_SMTP.VRFY module | 
| UTL\_SMTP.WRITE\_DATA | Extension pack | aws\_oracle\_ext.utl\_smtp$write\_data | None | 
| UTL\_SMTP.WRITE\_RAW\_DATA | Extension pack | aws\_oracle\_ext.utl\_smtp$write\_raw\_data | None | 

## Operators and language constructs
<a name="sc-default-rules-builtins-oracle-operators-language-constructs"></a>

The following table lists each source object in the Operators and language constructs category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| ALL(expr1, expr2, …) | Rewritten | ALL (SELECT expr1 UNION ALL SELECT expr2 …) | None | 
| ALL(subquery) | Same name | ALL(subquery) | None | 
| ANY(expr1, expr2, …) | Rewritten | ANY (SELECT expr1 UNION ALL SELECT expr2 …) | None | 
| ANY(subquery) | Same name | ANY(subquery) | None | 
| AVG | Same name | AVG | None | 
| AVG(DISTINCT …) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the AVG(DISTINCT …) OVER (…) function | 
| AVG(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| BIN\_TO\_NUM | Rewritten | lpad(CONCAT(⟨exp⟩), 64, '0')::bit(64)::bigint | None | 
| COLLECT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the COLLECT function | 
| COUNT | Same name | COUNT | None | 
| COVAR\_POP | Same name | COVAR\_POP | None | 
| COVAR\_SAMP | Same name | COVAR\_SAMP | None | 
| CUME\_DIST | Same name | CUME\_DIST | None | 
| DELETING | Rewritten | TG\_OP = 'DELETE' | None | 
| DENSE\_RANK | Same name | DENSE\_RANK | None | 
| EXTRACT(XMLType value) | Rewritten | array\_to\_string(xpath(⟨xpath⟩, ⟨xml⟩), '')::xml | None | 
| EXTRACT(datetime value) | Same name | EXTRACT | None | 
| EXTRACTVALUE | Rewritten | (xpath('//self::text()', (xpath(⟨arg2⟩,⟨arg1⟩))[1]))[1]::text | None | 
| FIRST\_VALUE | Same name | FIRST\_VALUE | None | 
| INSERTING | Rewritten | TG\_OP = 'INSERT' | None | 
| LAG | Same name | LAG | None | 
| LAST\_VALUE | Same name | LAST\_VALUE | None | 
| LEAD | Same name | LEAD | None | 
| LISTAGG | Rewritten | STRING\_AGG(…) | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| LNNVL | Extension pack | aws\_oracle\_ext.lnnvl(⟨char⟩) | None | 
| MAX | Same name | MAX | None | 
| MAX(DISTINCT …) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the MAX(DISTINCT …) OVER (…) function | 
| MAX(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| MEDIAN | Rewritten | PERCENTILE\_CONT(0.5) WITHIN GROUP(order by ⟨n⟩) | None | 
| MEDIAN(…) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the MEDIAN(…) OVER (…) function | 
| MEDIAN(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| MIN | Same name | MIN | None | 
| MIN(DISTINCT …) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the MIN(DISTINCT …) OVER (…) function | 
| MIN(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| MOD | Same name | MOD | None | 
| NTILE | Same name | NTILE | None | 
| NVL2 | Rewritten | CASE WHEN ⟨expr1⟩ IS NOT NULL THEN ⟨expr2⟩ ELSE ⟨expr3⟩ END | None | 
| ORA\_HASH | Not converted | Not applicable | 5340: PostgreSQL doesn't support the ORA\_HASH function | 
| ORA\_INVOKING\_USER | Not converted | Not applicable | 5340: PostgreSQL doesn't support the ORA\_INVOKING\_USER function | 
| ORA\_INVOKING\_USERID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the ORA\_INVOKING\_USERID function | 
| OVER | Same name | OVER | None | 
| PERCENTILE\_CONT | Same name | PERCENTILE\_CONT | None | 
| PERCENTILE\_CONT(…) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the PERCENTILE\_CONT(…) OVER (…) function | 
| PERCENTILE\_CONT(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| PERCENTILE\_DISC | Same name | PERCENTILE\_DISC | None | 
| PERCENTILE\_DISC(…) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the PERCENTILE\_DISC(…) OVER (…) function | 
| PERCENTILE\_DISC(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| PERCENT\_RANK | Same name | PERCENT\_RANK | None | 
| RAISE\_APPLICATION\_ERROR | Rewritten | RAISE EXCEPTION USING … | None | 
| RANK | Same name | RANK | None | 
| RATIO\_TO\_REPORT | Extension pack | aws\_oracle\_ext.ratio\_to\_report(⟨expr1⟩, sum(⟨expr1⟩)) | None | 
| REVERSE | Same name | REVERSE | None | 
| ROW\_NUMBER | Same name | ROW\_NUMBER | None | 
| SCN\_TO\_TIMESTAMP | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SCN\_TO\_TIMESTAMP function | 
| SOME(expr1, expr2, …) | Rewritten | SOME (SELECT expr1 UNION ALL SELECT expr2 …) | None | 
| SOME(subquery) | Same name | SOME(subquery) | None | 
| STDDEV | Same name | STDDEV | None | 
| STDDEV\_POP | Same name | STDDEV\_POP | None | 
| STDDEV\_SAMP | Same name | STDDEV\_SAMP | None | 
| SUM | Same name | SUM | None | 
| SUM(DISTINCT …) OVER (…) | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SUM(DISTINCT …) OVER (…) function | 
| SUM(…) in a CONNECT BY query | Not converted | Not applicable | 5073: PostgreSQL doesn't support hierarchical queries with pseudocolumns | 
| SYS\_CONNECT\_BY\_PATH | Same name | SYS\_CONNECT\_BY\_PATH | None | 
| SYS\_TYPEID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS\_TYPEID function | 
| TIMESTAMP\_TO\_SCN | Not converted | Not applicable | 5340: PostgreSQL doesn't support the TIMESTAMP\_TO\_SCN function | 
| TO\_LOB | Rewritten | ⟨expr⟩::Bytea | None | 
| UPDATING | Rewritten | TG\_OP = 'UPDATE' | None | 
| VARIANCE | Same name | VARIANCE | None | 
| WIDTH\_BUCKET | Same name | WIDTH\_BUCKET | None | 
| XMLSEQUENCE(cursor) | Rewritten | unnest(xpath('table/\*', cursor\_to\_xml(⟨cursor⟩, 2147483647, FALSE, FALSE, ''))) | None | 

## Package constant
<a name="sc-default-rules-builtins-oracle-package-constant"></a>

The following table lists each source object in the Package constant category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| UTL\_TCP.CRLF | Rewritten | CHR(10) | None | 

## SYS.DBMS\_AQADM
<a name="sc-default-rules-builtins-oracle-sys-dbms-aqadm"></a>

The following table lists each source object in the SYS.DBMS\_AQADM package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.AQ$\_AGENT | Extension pack | aws\_oracle\_ext.sqs\_aq$\_agent | None | 
| SYS.AQ$\_SIG\_PROP | Extension pack | aws\_oracle\_ext.sqs\_aq$\_sig\_prop | None | 
| SYS.DBMS\_AQADM.CREATE\_QUEUE | Extension pack | aws\_oracle\_ext.dbms\_aqadm$create\_queue | None | 
| SYS.DBMS\_AQADM.CREATE\_QUEUE\_TABLE | Extension pack | aws\_oracle\_ext.dbms\_aqadm$create\_queue\_table | None | 
| SYS.DBMS\_AQADM.DROP\_QUEUE | Extension pack | aws\_oracle\_ext.dbms\_aqadm$drop\_queue | None | 
| SYS.DBMS\_AQADM.DROP\_QUEUE\_TABLE | Extension pack | aws\_oracle\_ext.dbms\_aqadm$drop\_queue\_table | None | 
| SYS.DBMS\_AQADM.EXCEPTION\_QUEUE | Extension pack | aws\_oracle\_ext.sqs\_exception\_queue() | None | 
| SYS.DBMS\_AQADM.GRANT\_QUEUE\_PRIVILEGE | Not converted | Not applicable | 5793: DMS SC creates the queue with the GRANT ALL option | 
| SYS.DBMS\_AQADM.NONE | Extension pack | aws\_oracle\_ext.sqs\_none() | None | 
| SYS.DBMS\_AQADM.NON\_PERSISTENT\_QUEUE | Extension pack | aws\_oracle\_ext.sqs\_non\_persistent\_queue() | None | 
| SYS.DBMS\_AQADM.NORMAL\_QUEUE | Extension pack | aws\_oracle\_ext.sqs\_normal\_queue() | None | 
| SYS.DBMS\_AQADM.START\_QUEUE | Not converted | Not applicable | 5794: PostgreSQL sets the queue mode to ENABLE by default | 
| SYS.DBMS\_AQADM.STOP\_QUEUE | Not converted | Not applicable | 5795: Amazon Simple Queue Service doesn't support queues in the DISABLE mode | 
| SYS.DBMS\_AQADM.TRANSACTIONAL | Extension pack | aws\_oracle\_ext.sqs\_transactional() | None | 

## SYS.DBMS\_ASSERT
<a name="sc-default-rules-builtins-oracle-sys-dbms-assert"></a>

The following table lists each source object in the SYS.DBMS\_ASSERT package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_ASSERT.ENQUOTE\_LITERAL | Extension pack | aws\_oracle\_ext.dbms\_assert$enquote\_literal((⟨str\_literal⟩)::TEXT) | None | 
| SYS.DBMS\_ASSERT.ENQUOTE\_NAME | Extension pack | aws\_oracle\_ext.dbms\_assert$enquote\_name((⟨str\_sqlname⟩)::TEXT) | None | 
| SYS.DBMS\_ASSERT.NOOP | Rewritten | (⟨str\_literal⟩)::TEXT | None | 
| SYS.DBMS\_ASSERT.QUALIFIED\_SQL\_NAME | Extension pack | aws\_oracle\_ext.dbms\_assert$qualified\_sql\_name((⟨str\_sqlname⟩)::TEXT) | None | 
| SYS.DBMS\_ASSERT.SCHEMA\_NAME | Extension pack | aws\_oracle\_ext.dbms\_assert$schema\_name((⟨schema\_name⟩)::TEXT) | None | 
| SYS.DBMS\_ASSERT.SIMPLE\_SQL\_NAME | Extension pack | aws\_oracle\_ext.dbms\_assert$simple\_sql\_name((⟨str\_sqlname⟩)::TEXT) | None | 
| SYS.DBMS\_ASSERT.SQL\_OBJECT\_NAME | Extension pack | aws\_oracle\_ext.dbms\_assert$sql\_object\_name((⟨object\_name⟩)::TEXT) | None | 

## SYS.DBMS\_LOCK
<a name="sc-default-rules-builtins-oracle-sys-dbms-lock"></a>

The following table lists each source object in the SYS.DBMS\_LOCK package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_LOCK.ALLOCATE\_UNIQUE | Extension pack | SELECT aws\_oracle\_ext.dbms\_lock$allocate\_unique(⟨lockname⟩, ⟨lockhandle⟩) INTO ⟨lockhandle⟩ | None | 
| SYS.DBMS\_LOCK.CONVERT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_LOCK.CONVERT function | 
| DBMS\_LOCK.RELEASE(lock id) | Extension pack | aws\_oracle\_ext.dbms\_lock$release(⟨id⟩) | None | 
| DBMS\_LOCK.RELEASE(lock name) | Extension pack | aws\_oracle\_ext.dbms\_lock$release(id => aws\_oracle\_ext.get\_id\_by\_name(⟨name⟩)) | None | 
| DBMS\_LOCK.REQUEST(id, lockmode, timeout) | Extension pack | aws\_oracle\_ext.dbms\_lock$request(⟨id⟩) | None | 
| DBMS\_LOCK.REQUEST(id, lockmode, timeout, release\_on\_commit) | Extension pack | aws\_oracle\_ext.dbms\_lock$request | None | 
| SYS.DBMS\_LOCK.SLEEP | Renamed | pg\_sleep | None | 

## SYS.DBMS\_OBFUSCATION\_TOOLKIT
<a name="sc-default-rules-builtins-oracle-sys-dbms-obfuscation-toolkit"></a>

The following table lists each source object in the SYS.DBMS\_OBFUSCATION\_TOOLKIT package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| STANDARD\_HASH | Extension pack | aws\_oracle\_ext.standard\_hash | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DES3DECRYPT | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DES3DECRYPT(⟨arg1⟩, ⟨arg2⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DES3ENCRYPT | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DES3ENCRYPT(⟨arg1⟩, ⟨arg2⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DES3GETKEY | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DESGETKEY(⟨arg2⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DESDECRYPT | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DESDECRYPT(⟨arg1⟩, ⟨arg2⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DESENCRYPT | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DESENCRYPT(⟨arg1⟩, ⟨arg2⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.DESGETKEY | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$DESGETKEY(⟨arg1⟩) | None | 
| SYS.DBMS\_OBFUSCATION\_TOOLKIT.MD5 | Extension pack | aws\_oracle\_ext.DBMS\_OBFUSCATION\_TOOLKIT$MD5(⟨arg1⟩) | None | 
| SYS.XMLTYPE | Rewritten | XMLPARSE(…) | None | 

## SYS.DBMS\_SESSION
<a name="sc-default-rules-builtins-oracle-sys-dbms-session"></a>

The following table lists each source object in the SYS.DBMS\_SESSION package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| STANDARD.SYS\_CONTEXT | Extension pack | aws\_oracle\_ext.SYS\_CONTEXT(…) | None | 
| USERENV | Extension pack | aws\_oracle\_ext.USERENV | None | 
| USERENV('SESSIONID'), USERENV('COMMITSCN'), USERENV('ENTRYID') | Extension pack | aws\_oracle\_ext.USERENV\_NUMBER | None | 
| USERENV(…) in an autonomous transaction | Extension pack | aws\_oracle\_ext.USERENV | 5666: PostgreSQL supports only global application contexts in routines with PRAGMA AUTONOMOUS\_TRANSACTION | 
| SYS.DBMS\_SESSION.CLEAR\_ALL\_CONTEXT | Extension pack | aws\_oracle\_ext.dbms\_session$clear\_all\_context | None | 
| SYS.DBMS\_SESSION.CLEAR\_CONTEXT | Extension pack | aws\_oracle\_ext.dbms\_session$clear\_context | None | 
| SYS.DBMS\_SESSION.CLEAR\_IDENTIFIER | Extension pack | aws\_oracle\_ext.dbms\_session$clear\_identifier | None | 
| SYS.DBMS\_SESSION.CLOSE\_DATABASE\_LINK | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.CLOSE\_DATABASE\_LINK function | 
| SYS.DBMS\_SESSION.FREE\_ALL\_RESOURCES | Extension pack | aws\_oracle\_ext.dbms\_session$free\_all\_resources() | None | 
| SYS.DBMS\_SESSION.FREE\_UNUSED\_USER\_MEMORY | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.FREE\_UNUSED\_USER\_MEMORY function | 
| SYS.DBMS\_SESSION.IS\_ROLE\_ENABLED | Extension pack | aws\_oracle\_ext.DBMS\_SESSION$IS\_ROLE\_ENABLED | None | 
| SYS.DBMS\_SESSION.IS\_SESSION\_ALIVE | Extension pack | aws\_oracle\_ext.DBMS\_SESSION$IS\_SESSION\_ALIVE | None | 
| SYS.DBMS\_SESSION.LIST\_CONTEXT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.LIST\_CONTEXT function | 
| SYS.DBMS\_SESSION.MODIFY\_PACKAGE\_STATE | Extension pack | aws\_oracle\_ext.dbms\_session$modify\_package\_state | None | 
| SYS.DBMS\_SESSION.REINITIALIZE | Extension pack | aws\_oracle\_ext.dbms\_session$reinitialize() | None | 
| SYS.DBMS\_SESSION.RESET\_PACKAGE | Extension pack | aws\_oracle\_ext.dbms\_session$reset\_package | None | 
| SYS.DBMS\_SESSION.SESSION\_TRACE\_DISABLE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.SESSION\_TRACE\_DISABLE function | 
| SYS.DBMS\_SESSION.SESSION\_TRACE\_ENABLE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.SESSION\_TRACE\_ENABLE function | 
| SYS.DBMS\_SESSION.SET\_CONTEXT | Extension pack | aws\_oracle\_ext.DBMS\_SESSION$SET\_CONTEXT | 5976: Your source code uses the crypto() function from the pgcrypto extension | 
| SYS.DBMS\_SESSION.SET\_EDITION\_DEFERRED | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.SET\_EDITION\_DEFERRED function | 
| SYS.DBMS\_SESSION.SET\_IDENTIFIER | Extension pack | aws\_oracle\_ext.dbms\_session$set\_identifier | None | 
| SYS.DBMS\_SESSION.SET\_NLS | Extension pack | aws\_oracle\_ext.DBMS\_SESSION$SET\_NLS | None | 
| SYS.DBMS\_SESSION.SET\_SQL\_TRACE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.DBMS\_SESSION.SET\_SQL\_TRACE function | 
| SYS.DBMS\_SESSION.UNIQUE\_SESSION\_ID | Rewritten | pg\_backend\_pid() | None | 

## SYS.DBMS\_SQL
<a name="sc-default-rules-builtins-oracle-sys-dbms-sql"></a>

The following table lists each source object in the SYS.DBMS\_SQL package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_SQL.BIND\_ARRAY | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.BIND\_ARRAY function | 
| DBMS\_SQL.BIND\_VARIABLE | Extension pack | aws\_oracle\_ext.dbms\_sql$bind\_variable | None | 
| DBMS\_SQL.BIND\_VARIABLE\_CHAR | Extension pack | aws\_oracle\_ext.dbms\_sql$bind\_variable\_char | None | 
| DBMS\_SQL.BIND\_VARIABLE\_RAW | Extension pack | aws\_oracle\_ext.dbms\_sql$bind\_variable | None | 
| DBMS\_SQL.BIND\_VARIABLE\_ROWID | Extension pack | aws\_oracle\_ext.dbms\_sql$bind\_variable | None | 
| DBMS\_SQL.CLOSE\_CURSOR | Extension pack | aws\_oracle\_ext.dbms\_sql$close\_cursor | None | 
| DBMS\_SQL.COLUMN\_VALUE | Extension pack | aws\_oracle\_ext.dbms\_sql$column\_value | None | 
| DBMS\_SQL.COLUMN\_VALUE\_CHAR | Extension pack | aws\_oracle\_ext.dbms\_sql$column\_value\_char | None | 
| DBMS\_SQL.COLUMN\_VALUE\_LONG | Extension pack | aws\_oracle\_ext.dbms\_sql$column\_value\_long | None | 
| DBMS\_SQL.COLUMN\_VALUE\_RAW | Extension pack | aws\_oracle\_ext.dbms\_sql$column\_value | None | 
| DBMS\_SQL.COLUMN\_VALUE\_ROWID | Extension pack | aws\_oracle\_ext.dbms\_sql$column\_value | None | 
| DBMS\_SQL.DEFINE\_ARRAY | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.DEFINE\_ARRAY function | 
| DBMS\_SQL.DEFINE\_COLUMN | Extension pack | aws\_oracle\_ext.dbms\_sql$define\_column | None | 
| DBMS\_SQL.DEFINE\_COLUMN\_CHAR | Extension pack | aws\_oracle\_ext.dbms\_sql$define\_column\_char | None | 
| DBMS\_SQL.DEFINE\_COLUMN\_LONG | Extension pack | aws\_oracle\_ext.dbms\_sql$define\_column\_long | None | 
| DBMS\_SQL.DEFINE\_COLUMN\_RAW | Extension pack | aws\_oracle\_ext.dbms\_sql$define\_column | None | 
| DBMS\_SQL.DEFINE\_COLUMN\_ROWID | Extension pack | aws\_oracle\_ext.dbms\_sql$define\_column | None | 
| DBMS\_SQL.DESCRIBE\_COLUMNS | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.DESCRIBE\_COLUMNS function | 
| DBMS\_SQL.DESCRIBE\_COLUMNS2 | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.DESCRIBE\_COLUMNS2 function | 
| DBMS\_SQL.DESCRIBE\_COLUMNS3 | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.DESCRIBE\_COLUMNS3 function | 
| DBMS\_SQL.EXECUTE | Extension pack | aws\_oracle\_ext.dbms\_sql$execute((⟨cursor\_id⟩)::INTEGER) | None | 
| DBMS\_SQL.EXECUTE\_AND\_FETCH | Extension pack | aws\_oracle\_ext.dbms\_sql$execute\_and\_fetch((⟨cursor\_id⟩)::INTEGER) | None | 
| DBMS\_SQL.FETCH\_ROWS | Extension pack | aws\_oracle\_ext.dbms\_sql$fetch\_rows((⟨cursor\_id⟩)::INTEGER) | None | 
| DBMS\_SQL.GET\_NEXT\_RESULT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.GET\_NEXT\_RESULT function | 
| DBMS\_SQL.IS\_OPEN | Extension pack | aws\_oracle\_ext.dbms\_sql$is\_open((⟨cursor\_id⟩)::INTEGER) | None | 
| DBMS\_SQL.LAST\_ERROR\_POSITION | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.LAST\_ERROR\_POSITION function | 
| DBMS\_SQL.LAST\_ROW\_COUNT | Extension pack | aws\_oracle\_ext.dbms\_sql$last\_row\_count | 30212: Converted code doesn't cover native DML SQL statements because of the dbms\_sql$last\_row\_count method limitations | 
| DBMS\_SQL.LAST\_ROW\_ID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.LAST\_ROW\_ID function | 
| DBMS\_SQL.LAST\_SQL\_FUNCTION\_CODE | Extension pack | aws\_oracle\_ext.dbms\_sql$last\_sql\_function\_code | 30211: Converted code doesn't cover native DML SQL statements because of the dbms\_sql$last\_sql\_function\_code method limitations | 
| DBMS\_SQL.OPEN\_CURSOR | Extension pack | aws\_oracle\_ext.dbms\_sql$open\_cursor | None | 
| DBMS\_SQL.PARSE | Extension pack | aws\_oracle\_ext.dbms\_sql$parse | None | 
| DBMS\_SQL.RETURN\_RESULT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the DBMS\_SQL.RETURN\_RESULT function | 
| DBMS\_SQL.TO\_CURSOR\_NUMBER | Extension pack | aws\_oracle\_ext.dbms\_sql$to\_cursor\_number | 30213: DMS SC can't convert dbms\_sql$to\_cursor\_number method. Make sure that each REFCURSOR column has a unique alias. | 
| DBMS\_SQL.TO\_REFCURSOR | Extension pack | aws\_oracle\_ext.dbms\_sql$to\_refcursor((⟨cursor\_id⟩)::INTEGER) | None | 
| DBMS\_SQL.VARIABLE\_VALUE | Extension pack | aws\_oracle\_ext.dbms\_sql$variable\_value | None | 
| DBMS\_SQL.VARIABLE\_VALUE\_CHAR | Extension pack | aws\_oracle\_ext.dbms\_sql$variable\_value\_char | None | 
| DBMS\_SQL.VARIABLE\_VALUE\_RAW | Extension pack | aws\_oracle\_ext.dbms\_sql$variable\_value | None | 
| DBMS\_SQL.VARIABLE\_VALUE\_ROWID | Extension pack | aws\_oracle\_ext.dbms\_sql$variable\_value | None | 

## SYS.DBMS\_TYPES
<a name="sc-default-rules-builtins-oracle-sys-dbms-types"></a>

The following table lists each source object in the SYS.DBMS\_TYPES package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_TYPES.NO\_DATA | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('NO\_DATA') | None | 
| SYS.DBMS\_TYPES.SUCCESS | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('SUCCESS') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_BDOUBLE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_BDOUBLE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_BFILE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_BFILE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_BFLOAT | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_BFLOAT') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_BLOB | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_BLOB') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_CFILE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_CFILE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_CHAR | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_CHAR') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_CLOB | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_CLOB') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_DATE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_DATE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_INTERVAL\_DS | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_INTERVAL\_DS') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_INTERVAL\_YM | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_INTERVAL\_YM') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_MLSLABEL | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_MLSLABEL') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_NAMEDCOLLECTION | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_NAMEDCOLLECTION') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_NCHAR | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_NCHAR') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_NCLOB | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_NCLOB') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_NUMBER | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_NUMBER') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_NVARCHAR2 | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_NVARCHAR2') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_OBJECT | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_OBJECT') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_OPAQUE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_OPAQUE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_RAW | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_RAW') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_REF | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_REF') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_TABLE | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_TABLE') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_TIMESTAMP | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_TIMESTAMP') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_TIMESTAMP\_LTZ | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_TIMESTAMP\_LTZ') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_TIMESTAMP\_TZ | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_TIMESTAMP\_TZ') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_UROWID | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_UROWID') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_VARCHAR | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_VARCHAR') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_VARCHAR2 | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_VARCHAR2') | None | 
| SYS.DBMS\_TYPES.TYPECODE\_VARRAY | Extension pack | aws\_oracle\_ext.DBMS\_TYPES('TYPECODE\_VARRAY') | None | 

## SYS.DBMS\_UTILITY
<a name="sc-default-rules-builtins-oracle-sys-dbms-utility"></a>

The following table lists each source object in the SYS.DBMS\_UTILITY package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_UTILITY.CURRENT\_INSTANCE | Extension pack | aws\_oracle\_ext.dbms\_utility$current\_instance | None | 
| DBMS\_UTILITY.FORMAT\_CALL\_STACK | Extension pack | aws\_oracle\_ext.dbms\_utility$format\_call\_stack | None | 
| DBMS\_UTILITY.FORMAT\_ERROR\_BACKTRACE | Rewritten | aws$frmt\_err\_bcktrc, declared and set by: GET STACKED DIAGNOSTICS aws$frmt\_err\_bcktrc = PG\_EXCEPTION\_CONTEXT; | None | 
| DBMS\_UTILITY.FORMAT\_ERROR\_STACK | Rewritten | aws$frmt\_err\_stck, declared and set by: GET STACKED DIAGNOSTICS aws$frmt\_err\_num = RETURNED\_SQLSTATE, aws$frmt\_err\_stck = MESSAGE\_TEXT; aws$frmt\_err\_stck := CONCAT(aws$frmt\_err\_num, ': ', aws$frmt\_err\_stck); | None | 
| DBMS\_UTILITY.GET\_TIME | Extension pack | aws\_oracle\_ext.dbms\_utility$get\_time | None | 

## SYS.DBMS\_XMLGEN
<a name="sc-default-rules-builtins-oracle-sys-dbms-xmlgen"></a>

The following table lists each source object in the SYS.DBMS\_XMLGEN package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_XMLGEN.CLOSECONTEXT | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$closecontext | None | 
| SYS.DBMS\_XMLGEN.CONVERT | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$convert | None | 
| SYS.DBMS\_XMLGEN.DROP\_NULLS | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$drop\_nulls() | None | 
| SYS.DBMS\_XMLGEN.DTD | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$dtd() | None | 
| SYS.DBMS\_XMLGEN.EMPTY\_TAG | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$empty\_tag() | None | 
| SYS.DBMS\_XMLGEN.ENTITY\_DECODE | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$entity\_decode() | None | 
| SYS.DBMS\_XMLGEN.ENTITY\_ENCODE | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$entity\_encode() | None | 
| SYS.DBMS\_XMLGEN.GETNUMROWSPROCESSED | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$getNumRowsProcessed | None | 
| SYS.DBMS\_XMLGEN.GETXML | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$getXML(…) | 5096: The call of the converted method might produce different results compared to the source method | 
| SYS.DBMS\_XMLGEN.GETXMLTYPE | Not converted | Not applicable | 5141: DMS SC can't convert the SYS.DBMS\_XMLGEN.GETXMLTYPE method | 
| SYS.DBMS\_XMLGEN.NEWCONTEXT | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$newContext(…) | None | 
| SYS.DBMS\_XMLGEN.NONE | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$none() | None | 
| SYS.DBMS\_XMLGEN.NULL\_ATTR | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$null\_attr() | None | 
| SYS.DBMS\_XMLGEN.RESTARTQUERY | Not converted | Not applicable | 5141: DMS SC can't convert the SYS.DBMS\_XMLGEN.RESTARTQUERY method | 
| SYS.DBMS\_XMLGEN.SCHEMA | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$schema() | None | 
| SYS.DBMS\_XMLGEN.SETCONVERTSPECIALCHARS | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setConvertSpecialChars | 5092: Calling the SYS.DBMS\_XMLGEN.SETCONVERTSPECIALCHARS method doesn't influence the GETXML call | 
| SYS.DBMS\_XMLGEN.SETMAXROWS | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setMaxRows | None | 
| SYS.DBMS\_XMLGEN.SETNULLHANDLING | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setNullHandling | 5092: Calling the SYS.DBMS\_XMLGEN.SETNULLHANDLING method doesn't influence the GETXML call | 
| SYS.DBMS\_XMLGEN.SETROWSETTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setRowSetTag | None | 
| SYS.DBMS\_XMLGEN.SETROWTAG | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setRowTag | None | 
| SYS.DBMS\_XMLGEN.SETSKIPROWS | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$setskiprows | None | 
| SYS.DBMS\_XMLGEN.USEITEMTAGSFORCOLL | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$useitemtagsforcoll | 5092: Calling the SYS.DBMS\_XMLGEN.USEITEMTAGSFORCOLL method doesn't influence the GETXML call | 
| SYS.DBMS\_XMLGEN.USENULLATTRIBUTEINDICATOR | Extension pack | aws\_oracle\_ext.dbms\_xmlgen$usenullattributeindicator | 5092: Calling the SYS.DBMS\_XMLGEN.USENULLATTRIBUTEINDICATOR method doesn't influence the GETXML call | 

## SYS.UTL\_ENCODE
<a name="sc-default-rules-builtins-oracle-sys-utl-encode"></a>

The following table lists each source object in the SYS.UTL\_ENCODE package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.UTL\_ENCODE.BASE64 | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$base64() | None | 
| SYS.UTL\_ENCODE.BASE64\_DECODE | Rewritten | decode(decode(⟨r⟩::text,'hex')::text, 'base64') | None | 
| SYS.UTL\_ENCODE.BASE64\_ENCODE | Rewritten | encode(encode(⟨r⟩,'base64')::bytea, 'hex') | None | 
| SYS.UTL\_ENCODE.MIMEHEADER\_DECODE | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$MIMEHEADER\_DECODE | None | 
| SYS.UTL\_ENCODE.MIMEHEADER\_ENCODE | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$MIMEHEADER\_ENCODE | None | 
| SYS.UTL\_ENCODE.QUOTED\_PRINTABLE | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$quoted\_printable() | None | 
| SYS.UTL\_ENCODE.QUOTED\_PRINTABLE\_DECODE | Rewritten | decode(⟨r⟩::text,'hex') | None | 
| SYS.UTL\_ENCODE.QUOTED\_PRINTABLE\_ENCODE | Rewritten | encode(⟨r⟩, 'hex') | None | 
| SYS.UTL\_ENCODE.TEXT\_DECODE | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$TEXT\_DECODE | None | 
| SYS.UTL\_ENCODE.TEXT\_ENCODE | Extension pack | aws\_oracle\_ext.UTL\_ENCODE$TEXT\_ENCODE | None | 
| SYS.UTL\_ENCODE.UUDECODE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.UTL\_ENCODE.UUDECODE function | 
| SYS.UTL\_ENCODE.UUENCODE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the SYS.UTL\_ENCODE.UUENCODE function | 
| SYS.UTL\_MATCH.EDIT\_DISTANCE | Extension pack | aws\_oracle\_ext.utl\_match$edit\_distance | None | 
| SYS.UTL\_MATCH.EDIT\_DISTANCE\_SIMILARITY | Extension pack | aws\_oracle\_ext.utl\_match$edit\_distance\_similarity | None | 
| SYS.UTL\_MATCH.JARO\_WINKLER | Extension pack | aws\_oracle\_ext.utl\_match$jaro\_winkler | None | 
| SYS.UTL\_MATCH.JARO\_WINKLER\_SIMILARITY | Extension pack | aws\_oracle\_ext.utl\_match$jaro\_winkler\_similarity | None | 

## Spatial
<a name="sc-default-rules-builtins-oracle-spatial"></a>

The following table lists each source object in the Spatial category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| MDSYS.ALL\_SDO\_GEOM\_METADATA | Extension pack | aws\_oracle\_ext.all\_sdo\_geom\_metadata | None | 
| MDSYS.ALL\_SDO\_INDEX\_INFO | Extension pack | aws\_oracle\_ext.all\_sdo\_index\_info | None | 
| MDSYS.SDO\_EQUAL | Renamed | ST\_Equals | None | 
| MDSYS.SDO\_GEOMETRY.GET\_DIMS | Rewritten | ST\_CoordDim(⟨geom⟩) | None | 
| MDSYS.SDO\_GEOMETRY.GET\_GTYPE | Rewritten | CASE GeometryType(⟨geom⟩) WHEN 'POINT' THEN 1 … END | None | 
| MDSYS.SDO\_GEOMETRY.GET\_LRS\_DIM | Not converted | Not applicable | 5632: DMS SC can't convert MDSYS.SDO\_GEOMETRY.GET\_LRS\_DIM Spatial object such as the type, function, method, or operator | 
| MDSYS.SDO\_GEOMETRY.GET\_WKB | Rewritten | ST\_AsBinary(⟨geom⟩) | None | 
| MDSYS.SDO\_GEOMETRY.GET\_WKT | Rewritten | ST\_AsText(⟨geom⟩) | None | 
| MDSYS.SDO\_GEOMETRY.SDO\_GTYPE | Extension pack | aws\_oracle\_ext.sdo\_gtype(⟨geom⟩) | None | 
| MDSYS.SDO\_GEOMETRY.ST\_COORDDIM | Rewritten | ST\_CoordDim(⟨geom⟩) | None | 
| MDSYS.SDO\_GEOMETRY.ST\_ISVALID | Rewritten | CASE ST\_isvalid(⟨geom⟩) WHEN TRUE THEN 1 WHEN FALSE THEN 0 END | None | 
| MDSYS.USER\_SDO\_GEOM\_METADATA | Extension pack | aws\_oracle\_ext.user\_sdo\_geom\_metadata | None | 
| MDSYS.USER\_SDO\_INDEX\_INFO | Extension pack | aws\_oracle\_ext.user\_sdo\_index\_info | None | 
| SDO\_GEOM.SDO\_ARC\_DENSIFY | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.SDO\_ARC\_DENSIFY Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_AREA | Rewritten | ST\_Area(⟨geom⟩) | None | 
| SDO\_AREA(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_AREA(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_BUFFER | Rewritten | ST\_Buffer(⟨geom⟩, ⟨dist⟩) | None | 
| SDO\_BUFFER(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_BUFFER(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_CENTROID | Rewritten | ST\_Centroid(⟨geom⟩) | None | 
| SDO\_CENTROID(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_CENTROID(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_CLOSEST\_POINTS | Extension pack | aws\_oracle\_ext.sdo\_closest\_points(…) | None | 
| SDO\_GEOM.SDO\_CONVEXHULL | Rewritten | ST\_ConvexHull(⟨geom⟩) | None | 
| SDO\_GEOM.SDO\_DIFFERENCE | Rewritten | ST\_Difference(⟨geom1⟩, ⟨geom2⟩) | None | 
| SDO\_DIFFERENCE(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_DIFFERENCE(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_DISTANCE | Rewritten | ST\_Distance(⟨geom1⟩, ⟨geom2⟩) | None | 
| SDO\_DISTANCE(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_DISTANCE(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_INTERSECTION | Rewritten | ST\_Intersection(⟨geom1⟩, ⟨geom2⟩) | None | 
| SDO\_INTERSECTION(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_INTERSECTION(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_LENGTH | Extension pack | aws\_oracle\_ext.sdo\_length | 5632: DMS SC can't convert SDO\_GEOM.SDO\_LENGTH Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_MAX\_MBR\_ORDINATE | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.SDO\_MAX\_MBR\_ORDINATE Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_MBR | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.SDO\_MBR Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_MIN\_MBR\_ORDINATE | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.SDO\_MIN\_MBR\_ORDINATE Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_POINTONSURFACE | Rewritten | ST\_PointOnSurface(⟨geom⟩) | None | 
| SDO\_POINTONSURFACE(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_POINTONSURFACE(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_UNION | Rewritten | ST\_Union(⟨geom1⟩, ⟨geom2⟩) | None | 
| SDO\_UNION(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_UNION(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_VOLUME | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.SDO\_VOLUME Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.SDO\_XOR | Rewritten | ST\_SymDifference(⟨geom1⟩, ⟨geom2⟩) | None | 
| SDO\_XOR(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_XOR(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.VALIDATE\_GEOMETRY\_WITH\_CONTEXT | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.VALIDATE\_GEOMETRY\_WITH\_CONTEXT Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.VALIDATE\_LAYER\_WITH\_CONTEXT | Not converted | Not applicable | 5632: DMS SC can't convert SDO\_GEOM.VALIDATE\_LAYER\_WITH\_CONTEXT Spatial object such as the type, function, method, or operator | 
| SDO\_GEOM.WITHIN\_DISTANCE | Extension pack | aws\_oracle\_ext.within\_distance | None | 
| WITHIN\_DISTANCE(…, SDO\_DIM\_ARRAY argument) | Not converted | Not applicable | 5632: DMS SC can't convert WITHIN\_DISTANCE(…, SDO\_DIM\_ARRAY argument) Spatial object such as the type, function, method, or operator | 
| SDO\_UTIL.FROM\_WKTGEOMETRY | Renamed | ST\_GeomFromText | None | 

## Standard scalar functions
<a name="sc-default-rules-builtins-oracle-standard-scalar-functions"></a>

The following table lists each source object in the Standard scalar functions category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| STANDARD.ABS | Same name | ABS | None | 
| STANDARD.ACOS | Same name | ACOS | None | 
| STANDARD.ADD\_MONTHS | Extension pack | aws\_oracle\_ext.ADD\_MONTHS | None | 
| STANDARD.ASCII | Same name | ASCII | None | 
| ASCII(DATE argument) | Rewritten | ASCII(TO\_CHAR(⟨arg\_1⟩, 'DD-MON-YY'))::TEXT | None | 
| STANDARD.ASCIISTR | Extension pack | aws\_oracle\_ext.ASCIISTR | None | 
| STANDARD.ASIN | Same name | ASIN | None | 
| STANDARD.ATAN | Same name | ATAN | None | 
| STANDARD.ATAN2 | Same name | ATAN2 | None | 
| STANDARD.BFILENAME | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.BFILENAME function | 
| STANDARD.BINARY\_DOUBLE\_INFINITY | Rewritten | CAST('INFINITY' AS DOUBLE PRECISION) | None | 
| STANDARD.BINARY\_DOUBLE\_NAN | Rewritten | 'NAN' | None | 
| STANDARD.BINARY\_FLOAT\_INFINITY | Rewritten | CAST('INFINITY' AS DOUBLE PRECISION) | None | 
| STANDARD.BINARY\_FLOAT\_NAN | Rewritten | 'NAN' | None | 
| STANDARD.BITAND | Rewritten | (⟨n1⟩ & ⟨n2⟩) | None | 
| STANDARD.CARDINALITY | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.CARDINALITY function | 
| STANDARD.CAST | Same name | CAST | None | 
| STANDARD.CEIL | Same name | CEIL | None | 
| STANDARD.CHARTOROWID | Extension pack | aws\_oracle\_ext.CHARTOROWID(⟨arg⟩) | None | 
| STANDARD.CHR | Same name | CHR | None | 
| STANDARD.COALESCE | Same name | COALESCE | None | 
| STANDARD.COMPOSE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.COMPOSE function | 
| STANDARD.CONCAT | Same name | CONCAT | None | 
| STANDARD.CONVERT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.CONVERT function | 
| STANDARD.COS | Same name | COS | None | 
| STANDARD.COSH | Rewritten | ((EXP(⟨n⟩) \+ EXP(-⟨n⟩))/2) | None | 
| CURRENT\_DATE | Extension pack | aws\_oracle\_ext.current\_date() | None | 
| CURRENT\_DATE in a column default expression | Rewritten | clock\_timestamp()::timestamp without time zone | 5584: The CURRENT\_DATE function depends on the time zone settings | 
| CURRENT\_TIMESTAMP | Extension pack | aws\_oracle\_ext.current\_timestamp() | None | 
| CURRENT\_TIMESTAMP in a column default expression | Rewritten | CLOCK\_TIMESTAMP() | 5584: The CURRENT\_TIMESTAMP function depends on the time zone settings | 
| STANDARD.CV | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.CV function | 
| STANDARD.DBTIMEZONE | Extension pack | aws\_oracle\_ext.dbtimezone | None | 
| STANDARD.DECODE | Rewritten | CASE WHEN … expression | None | 
| STANDARD.DECOMPOSE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.DECOMPOSE function | 
| STANDARD.DEREF | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.DEREF function | 
| STANDARD.DUMP | Rewritten | engine-generated rewrite | None | 
| STANDARD.EMPTY\_BLOB | Rewritten | '\\x'::BYTEA | None | 
| STANDARD.EMPTY\_CLOB | Rewritten | ''::TEXT | None | 
| STANDARD.EXP | Same name | EXP | None | 
| STANDARD.FLOOR | Same name | FLOOR | None | 
| STANDARD.FROM\_TZ | Extension pack | aws\_oracle\_ext.FROM\_TZ | 5584: The STANDARD.FROM\_TZ function depends on the time zone settings | 
| STANDARD.GREATEST | Same name | GREATEST | None | 
| STANDARD.HEXTORAW | Rewritten | DECODE(⟨char⟩ , 'hex') | None | 
| STANDARD.INITCAP | Same name | INITCAP | None | 
| INITCAP(DATE argument) | Rewritten | INITCAP(TO\_CHAR(⟨arg⟩, 'DD-MON-YY')) | None | 
| STANDARD.INSTR | Extension pack | aws\_oracle\_ext.INSTR | None | 
| STANDARD.INSTRB | Extension pack | aws\_oracle\_ext.instrb | None | 
| INSTRB(…) with 3 arguments | Not converted | Not applicable | 5340: PostgreSQL doesn't support the INSTRB(…) function | 
| STANDARD.ITERATION\_NUMBER | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.ITERATION\_NUMBER function | 
| STANDARD.LAST\_DAY | Extension pack | aws\_oracle\_ext.LAST\_DAY | None | 
| STANDARD.LEAST | Same name | LEAST | None | 
| STANDARD.LENGTH | Same name | LENGTH | None | 
| LENGTH(DATE argument) | Rewritten | LENGTH(TO\_CHAR(⟨arg\_1⟩, 'DD-MON-YY')) | None | 
| STANDARD.LENGTHB | Rewritten | OCTET\_LENGTH(⟨geom⟩) | None | 
| STANDARD.LN | Same name | LN | None | 
| LOCALTIMESTAMP | Extension pack | aws\_oracle\_ext.localtimestamp() | None | 
| LOCALTIMESTAMP in a column default expression | Rewritten | LOCALTIMESTAMP | 5584: The LOCALTIMESTAMP function depends on the time zone settings | 
| LOCALTIMESTAMP(p) with p ≤ 6 | Extension pack | aws\_oracle\_ext.localtimestamp(p) | None | 
| LOCALTIMESTAMP(p) with p ≥ 7 | Not converted | Not applicable | 5340: PostgreSQL doesn't support the LOCALTIMESTAMP(p) function | 
| STANDARD.LOG | Same name | LOG | None | 
| STANDARD.LOWER | Same name | LOWER | None | 
| LOWER(DATE argument) | Rewritten | LOWER(TO\_CHAR(⟨arg⟩, 'DD-MON-YY')) | None | 
| STANDARD.LPAD | Same name | LPAD | None | 
| STANDARD.LTRIM | Same name | LTRIM | None | 
| LTRIM(DATE argument) | Rewritten | LTRIM(TO\_CHAR(⟨arg\_1⟩, 'DD-MON-YY')) | None | 
| STANDARD.MAKE\_REF | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.MAKE\_REF function | 
| STANDARD.MONTHS\_BETWEEN | Extension pack | aws\_oracle\_ext.MONTHS\_BETWEEN | None | 
| STANDARD.NANVL | Extension pack | aws\_oracle\_ext.nanvl | None | 
| STANDARD.NEW\_TIME | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NEW\_TIME function | 
| STANDARD.NEXT\_DAY | Extension pack | aws\_oracle\_ext.NEXT\_DAY | None | 
| STANDARD.NLSSORT | Rewritten | ⟨src⟩ COLLATE "C" | None | 
| STANDARD.NLS\_CHARSET\_DECL\_LEN | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_CHARSET\_DECL\_LEN function | 
| STANDARD.NLS\_CHARSET\_ID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_CHARSET\_ID function | 
| STANDARD.NLS\_CHARSET\_NAME | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_CHARSET\_NAME function | 
| STANDARD.NLS\_INITCAP | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_INITCAP function | 
| STANDARD.NLS\_LOWER | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_LOWER function | 
| STANDARD.NLS\_UPPER | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.NLS\_UPPER function | 
| STANDARD.NULLIF | Same name | NULLIF | None | 
| STANDARD.NUMTODSINTERVAL | Rewritten | concat\_ws(' ', (⟨arg1⟩)::text, ⟨arg2⟩)::interval | None | 
| STANDARD.NUMTOYMINTERVAL | Rewritten | concat\_ws(' ', (⟨arg1⟩)::text, ⟨arg2⟩)::interval | None | 
| STANDARD.NVL | Renamed | COALESCE | None | 
| STANDARD.POWER | Same name | POWER | None | 
| STANDARD.PRESENTNNV | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.PRESENTNNV function | 
| STANDARD.PRESENTV | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.PRESENTV function | 
| STANDARD.PREVIOUS | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.PREVIOUS function | 
| STANDARD.RAWTOHEX | Rewritten | UPPER(ENCODE(⟨raw⟩, 'hex')) | None | 
| STANDARD.RAWTONHEX | Rewritten | UPPER(ENCODE(⟨raw⟩, 'hex')) | None | 
| STANDARD.REF | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.REF function | 
| STANDARD.REFTOHEX | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.REFTOHEX function | 
| STANDARD.REGEXP\_COUNT | Same name | REGEXP\_COUNT (PostgreSQL 15) | None | 
| STANDARD.REGEXP\_COUNT | Extension pack | aws\_oracle\_ext.regexp\_count((⟨src\_string⟩)::TEXT, (⟨regexp\_pattern⟩)::TEXT) (PostgreSQL 14) | 5617: PostgreSQL doesn't fully support m and x as match parameters or as subexpression parameters for regular expressions | 
| STANDARD.REGEXP\_INSTR | Same name | REGEXP\_INSTR (PostgreSQL 15) | None | 
| STANDARD.REGEXP\_INSTR | Extension pack | aws\_oracle\_ext.regexp\_instr((⟨src\_string⟩)::TEXT, (⟨regexp\_pattern⟩)::TEXT) (PostgreSQL 14) | 5617: PostgreSQL doesn't fully support m and x as match parameters or as subexpression parameters for regular expressions | 
| STANDARD.REGEXP\_LIKE | Same name | REGEXP\_LIKE (PostgreSQL 15) | None | 
| STANDARD.REGEXP\_LIKE | Extension pack | aws\_oracle\_ext.regexp\_like((⟨src\_string⟩)::TEXT, (⟨regexp\_pattern⟩)::TEXT) (PostgreSQL 14) | None | 
| STANDARD.REGEXP\_REPLACE | Same name | REGEXP\_REPLACE (PostgreSQL 15) | None | 
| STANDARD.REGEXP\_REPLACE | Extension pack | aws\_oracle\_ext.regexp\_replace((⟨src\_string⟩)::TEXT, (⟨regexp\_pattern⟩)::TEXT) (PostgreSQL 14) | 5617: PostgreSQL doesn't fully support m and x as match parameters or as subexpression parameters for regular expressions | 
| STANDARD.REGEXP\_SUBSTR | Same name | REGEXP\_SUBSTR (PostgreSQL 15) | None | 
| STANDARD.REGEXP\_SUBSTR | Extension pack | aws\_oracle\_ext.regexp\_substr((⟨src\_string⟩)::TEXT, (⟨regexp\_pattern⟩)::TEXT) (PostgreSQL 14) | 5617: PostgreSQL doesn't fully support m and x as match parameters or as subexpression parameters for regular expressions | 
| STANDARD.REMAINDER | Rewritten | (⟨n1⟩ - ⟨n2⟩\*ROUND((CAST((⟨n1⟩) as NUMERIC )/⟨n2⟩))) | None | 
| STANDARD.REPLACE | Same name | REPLACE | None | 
| STANDARD.ROUND | Same name | ROUND | None | 
| STANDARD.ROWIDTOCHAR | Extension pack | aws\_oracle\_ext.ROWIDTOCHAR(⟨arg⟩) | None | 
| STANDARD.ROWIDTONCHAR | Extension pack | aws\_oracle\_ext.ROWIDTOCHAR(⟨arg⟩) | None | 
| STANDARD.RPAD | Same name | RPAD | None | 
| STANDARD.RTRIM | Same name | RTRIM | None | 
| RTRIM(DATE argument) | Rewritten | RTRIM(TO\_CHAR(⟨arg\_1⟩, 'DD-MON-YY')) | None | 
| SESSIONTIMEZONE | Extension pack | aws\_oracle\_ext.sessiontimezone() | None | 
| SESSIONTIMEZONE in a column default expression | Rewritten | current\_setting('TIMEZONE') | 5584: The SESSIONTIMEZONE function depends on the time zone settings | 
| STANDARD.SET | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.SET function | 
| STANDARD.SIGN | Same name | SIGN | None | 
| STANDARD.SIN | Same name | SIN | None | 
| STANDARD.SINH | Rewritten | ((EXP(⟨n⟩) - EXP(-⟨n⟩))/2) | None | 
| STANDARD.SOUNDEX | Same name | SOUNDEX | None | 
| STANDARD.SQLCODE | Rewritten | SQLSTATE | None | 
| STANDARD.SQLERRM | Same name | SQLERRM | None | 
| STANDARD.SQRT | Same name | SQRT | None | 
| SUBSTR | Extension pack | aws\_oracle\_ext.substr | None | 
| SUBSTR(CHAR or VARCHAR2 argument) | Same name | SUBSTR | None | 
| STANDARD.SUBSTRB | Extension pack | aws\_oracle\_ext.substrb | None | 
| STANDARD.SYSDATE | Extension pack | (CLOCK\_TIMESTAMP() AT TIME ZONE COALESCE(CURRENT\_SETTING('aws\_oracle\_ext.tz', TRUE), ⟨timezone⟩))::TIMESTAMP(0) | 5584: The STANDARD.SYSDATE function depends on the time zone settings | 
| SYSTIMESTAMP | Extension pack | aws\_oracle\_ext.systimestamp() | None | 
| SYSTIMESTAMP in a column default expression | Rewritten | clock\_timestamp() | 5584: The SYSTIMESTAMP function depends on the time zone settings | 
| STANDARD.SYS\_EXTRACT\_UTC | Rewritten | ⟨arg1⟩ AT TIME ZONE 'UTC' | None | 
| STANDARD.SYS\_GUID | Extension pack | aws\_oracle\_ext.sys\_guid | None | 
| STANDARD.TAN | Same name | TAN | None | 
| STANDARD.TANH | Rewritten | (((EXP(⟨n⟩) - EXP(-⟨n⟩)))/((EXP(⟨n⟩) \+ EXP(-⟨n⟩)))) | None | 
| STANDARD.TO\_BINARY\_DOUBLE | Rewritten | CAST(⟨expr⟩ AS DOUBLE PRECISION) | None | 
| STANDARD.TO\_BINARY\_FLOAT | Rewritten | CAST(⟨expr⟩ AS REAL) | None | 
| STANDARD.TO\_CHAR | Extension pack | aws\_oracle\_ext.TO\_CHAR(…) | None | 
| STANDARD.TO\_CLOB | Rewritten | ⟨expr⟩::Text | None | 
| STANDARD.TO\_DATE | Extension pack | aws\_oracle\_ext.TO\_DATE(…) | None | 
| STANDARD.TO\_DSINTERVAL | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.TO\_DSINTERVAL function | 
| STANDARD.TO\_MULTI\_BYTE | Extension pack | aws\_oracle\_ext.to\_multi\_byte(⟨char⟩) | None | 
| STANDARD.TO\_NCHAR | Extension pack | aws\_oracle\_ext.TO\_CHAR(…) | None | 
| STANDARD.TO\_NCLOB | Rewritten | ⟨expr⟩::Text | None | 
| STANDARD.TO\_NUMBER | Extension pack | aws\_oracle\_ext.TO\_NUMBER(…) | None | 
| STANDARD.TO\_SINGLE\_BYTE | Extension pack | aws\_oracle\_ext.to\_single\_byte(⟨char⟩) | None | 
| STANDARD.TO\_TIMESTAMP | Rewritten | TO\_TIMESTAMP(…) | None | 
| STANDARD.TO\_TIMESTAMP\_TZ | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.TO\_TIMESTAMP\_TZ function | 
| STANDARD.TO\_YMINTERVAL | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.TO\_YMINTERVAL function | 
| STANDARD.TRANSLATE | Same name | TRANSLATE | None | 
| STANDARD.TREAT | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.TREAT function | 
| STANDARD.TRIM | Same name | TRIM | None | 
| STANDARD.TRUNC | Same name | TRUNC | None | 
| TRUNC(DATE argument) | Extension pack | aws\_oracle\_ext.TRUNC | None | 
| TRUNC(TIME argument) | Rewritten | DATE(⟨datetime⟩) | None | 
| STANDARD.TZ\_OFFSET | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.TZ\_OFFSET function | 
| STANDARD.UID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.UID function | 
| STANDARD.UNISTR | Extension pack | aws\_oracle\_ext.UNISTR | None | 
| STANDARD.UPPER | Same name | UPPER | None | 
| UPPER(DATE argument) | Rewritten | UPPER(TO\_CHAR(⟨arg\_1⟩, 'DD-MON-YY')) | None | 
| STANDARD.USER | Rewritten | SESSION\_USER | None | 
| STANDARD.VALUE | Rewritten | engine-generated rewrite | None | 
| STANDARD.VSIZE | Not converted | Not applicable | 5340: PostgreSQL doesn't support the STANDARD.VSIZE function | 

## System object views
<a name="sc-default-rules-builtins-oracle-system-object-views"></a>

The following table lists each source object in the System object views category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.ALL\_ARGUMENTS | Not converted | Not applicable | 5619: DMS SC can't convert the SYS.ALL\_ARGUMENTS system object | 
| SYS.ALL\_CONSTRAINTS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_CONSTRAINTS | None | 
| SYS.ALL\_CONS\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_CONS\_COLUMNS | None | 
| SYS.ALL\_INDEXES | Extension pack | aws\_oracle\_ext.SYS\_ALL\_INDEXES | None | 
| SYS.ALL\_IND\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_IND\_COLUMNS | None | 
| SYS.ALL\_OBJECTS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_OBJECTS | None | 
| SYS.ALL\_POLICIES | Extension pack | aws\_oracle\_ext.SYS\_ALL\_POLICIES | None | 
| SYS.ALL\_SEQUENCES | Extension pack | aws\_oracle\_ext.SYS\_ALL\_SEQUENCES | None | 
| SYS.ALL\_SOURCE | Extension pack | aws\_oracle\_ext.SYS\_ALL\_SOURCE | None | 
| SYS.ALL\_TABLES | Extension pack | aws\_oracle\_ext.SYS\_ALL\_TABLES | None | 
| SYS.ALL\_TAB\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_TAB\_COLUMNS | None | 
| SYS.ALL\_TAB\_COMMENTS | Extension pack | aws\_oracle\_ext.sys\_all\_tab\_comments | None | 
| SYS.ALL\_TAB\_PARTITIONS | Extension pack | aws\_oracle\_ext.sys\_all\_tab\_partitions | None | 
| SYS.ALL\_TAB\_SUBPARTITIONS | Extension pack | aws\_oracle\_ext.sys\_all\_tab\_subpartitions | None | 
| SYS.ALL\_TRIGGERS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_TRIGGERS | None | 
| SYS.ALL\_USERS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_USERS | None | 
| SYS.ALL\_VIEWS | Extension pack | aws\_oracle\_ext.SYS\_ALL\_VIEWS | None | 
| SYS.DBA\_CONSTRAINTS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_CONSTRAINTS | None | 
| SYS.DBA\_CONS\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_CONS\_COLUMNS | None | 
| SYS.DBA\_INDEXES | Extension pack | aws\_oracle\_ext.SYS\_DBA\_INDEXES | None | 
| SYS.DBA\_IND\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_IND\_COLUMNS | None | 
| SYS.DBA\_OBJECTS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_OBJECTS | None | 
| SYS.DBA\_POLICIES | Extension pack | aws\_oracle\_ext.SYS\_DBA\_POLICIES | None | 
| SYS.DBA\_ROLES | Extension pack | aws\_oracle\_ext.SYS\_DBA\_ROLES | None | 
| SYS.DBA\_SEQUENCES | Extension pack | aws\_oracle\_ext.SYS\_DBA\_SEQUENCES | None | 
| SYS.DBA\_SOURCE | Extension pack | aws\_oracle\_ext.SYS\_DBA\_SOURCE | None | 
| SYS.DBA\_TABLES | Extension pack | aws\_oracle\_ext.SYS\_DBA\_TABLES | None | 
| SYS.DBA\_TAB\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_TAB\_COLUMNS | None | 
| SYS.DBA\_TAB\_COMMENTS | Extension pack | aws\_oracle\_ext.sys\_dba\_tab\_comments | None | 
| SYS.DBA\_TAB\_PARTITIONS | Extension pack | aws\_oracle\_ext.sys\_dba\_tab\_partitions | None | 
| SYS.DBA\_TAB\_SUBPARTITIONS | Extension pack | aws\_oracle\_ext.sys\_dba\_tab\_subpartitions | None | 
| SYS.DBA\_TRIGGERS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_TRIGGERS | None | 
| SYS.DBA\_USERS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_USERS | None | 
| SYS.DBA\_VIEWS | Extension pack | aws\_oracle\_ext.SYS\_DBA\_VIEWS | None | 
| SYS.GLOBAL\_NAME | Not converted | Not applicable | 5619: DMS SC can't convert the SYS.GLOBAL\_NAME system object | 
| SYS.USER\_COL\_COMMENTS | Extension pack | aws\_oracle\_ext.sys\_user\_col\_comments | None | 
| SYS.USER\_CONSTRAINTS | Extension pack | aws\_oracle\_ext.SYS\_USER\_CONSTRAINTS | None | 
| SYS.USER\_CONS\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_USER\_CONS\_COLUMNS | None | 
| SYS.USER\_INDEXES | Extension pack | aws\_oracle\_ext.SYS\_USER\_INDEXES | None | 
| SYS.USER\_IND\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_USER\_IND\_COLUMNS | None | 
| SYS.USER\_OBJECTS | Extension pack | aws\_oracle\_ext.SYS\_USER\_OBJECTS | None | 
| SYS.USER\_POLICIES | Extension pack | aws\_oracle\_ext.SYS\_USER\_POLICIES | None | 
| SYS.USER\_SEQUENCES | Extension pack | aws\_oracle\_ext.SYS\_USER\_SEQUENCES | None | 
| SYS.USER\_SOURCE | Extension pack | aws\_oracle\_ext.SYS\_USER\_SOURCE | None | 
| SYS.USER\_TABLES | Extension pack | aws\_oracle\_ext.SYS\_USER\_TABLES | None | 
| SYS.USER\_TAB\_COLUMNS | Extension pack | aws\_oracle\_ext.SYS\_USER\_TAB\_COLUMNS | None | 
| SYS.USER\_TAB\_COMMENTS | Extension pack | aws\_oracle\_ext.sys\_user\_tab\_comments | None | 
| SYS.USER\_TAB\_PARTITIONS | Extension pack | aws\_oracle\_ext.sys\_user\_tab\_partitions | None | 
| SYS.USER\_TAB\_SUBPARTITIONS | Extension pack | aws\_oracle\_ext.sys\_user\_tab\_subpartitions | None | 
| SYS.USER\_TRIGGERS | Extension pack | aws\_oracle\_ext.SYS\_USER\_TRIGGERS | None | 
| SYS.USER\_USERS | Extension pack | aws\_oracle\_ext.SYS\_USER\_USERS | None | 
| SYS.USER\_VIEWS | Extension pack | aws\_oracle\_ext.SYS\_USER\_VIEWS | None | 
| SYS.V\_$INSTANCE | Extension pack | aws\_oracle\_ext.v$instance | None | 
| SYS.V\_$VERSION | Extension pack | aws\_oracle\_ext.v$version | None | 

## System objects
<a name="sc-default-rules-builtins-oracle-system-objects"></a>

The following table lists each source object in the System objects category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| DBMS\_TRANSACTION.LOCAL\_TRANSACTION\_ID | Not converted | Not applicable | 5622: DMS SC converts the dbms\_transaction.local\_transaction\_id function with the parameter set to true | 
| DBMS\_TRANSACTION.LOCAL\_TRANSACTION\_ID(TRUE) | Rewritten | txid\_current()::text | None | 
| SYS.DUAL.DUMMY | Same name | DUMMY | None | 
| SYS.DUAL.ROWID | Same name | ROWID | None | 

## UTL\_RAW
<a name="sc-default-rules-builtins-oracle-utl-raw"></a>

The following table lists each source object in the UTL\_RAW package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.UTL\_RAW.BIT\_AND | Extension pack | aws\_oracle\_ext.utl\_raw$bit\_and | None | 
| SYS.UTL\_RAW.BIT\_COMPLEMENT | Extension pack | aws\_oracle\_ext.utl\_raw$bit\_complement | None | 
| SYS.UTL\_RAW.BIT\_OR | Extension pack | aws\_oracle\_ext.utl\_raw$bit\_or | None | 
| UTL\_RAW.CAST\_TO\_NUMBER | Not converted | Not applicable | 5340: PostgreSQL doesn't support the UTL\_RAW.CAST\_TO\_NUMBER function | 
| UTL\_RAW.CAST\_TO\_NUMBER('00') | Rewritten | CAST('-INF' AS DOUBLE PRECISION) | None | 
| UTL\_RAW.CAST\_TO\_NUMBER('FF65') | Rewritten | CAST('INF' AS DOUBLE PRECISION) | None | 
| SYS.UTL\_RAW.CAST\_TO\_RAW | Rewritten | ENCODE(⟨arg⟩::bytea, 'hex') | None | 
| SYS.UTL\_RAW.CAST\_TO\_VARCHAR2 | Rewritten | DECODE(⟨arg⟩::text, 'hex') | None | 
| SYS.UTL\_RAW.CONVERT | Extension pack | convert(⟨arg1⟩, aws\_oracle\_ext.get\_charset\_name(⟨arg3⟩), aws\_oracle\_ext.get\_charset\_name(⟨arg2⟩)) | None | 
| SYS.UTL\_RAW.LENGTH | Rewritten | octet\_length(⟨arg⟩) | None | 
| SYS.UTL\_RAW.REVERSE | Rewritten | reverse(⟨arg⟩::text) | None | 
| UTL\_RAW.SUBSTR(…) with 2 arguments | Rewritten | substring(⟨arg1⟩ from ⟨arg2⟩) | None | 
| UTL\_RAW.SUBSTR(…) with 3 arguments | Rewritten | substring(⟨arg1⟩ from ⟨arg2⟩ for ⟨arg3⟩) | None | 

## UTL\_URL
<a name="sc-default-rules-builtins-oracle-utl-url"></a>

The following table lists each source object in the UTL\_URL package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| UTL\_URL.ESCAPE | Extension pack | aws\_oracle\_ext.utl\_url$escape((⟨arg1⟩)::TEXT) | None | 
| UTL\_URL.UNESCAPE | Extension pack | aws\_oracle\_ext.utl\_url$unescape((⟨url\_string⟩)::TEXT) | None | 

## XDB.DBMS\_XSLPROCESSOR
<a name="sc-default-rules-builtins-oracle-xdb-dbms-xslprocessor"></a>

The following table lists each source object in the XDB.DBMS\_XSLPROCESSOR package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| XDB.DBMS\_XSLPROCESSOR.CLOB2FILE | Extension pack | aws\_oracle\_ext.dbms\_xslprocessor$clob2file | None | 
| XDB.DBMS\_XSLPROCESSOR.READ2CLOB | Extension pack | aws\_oracle\_ext.dbms\_xslprocessor$read2clob | None | 

## XMLTYPE
<a name="sc-default-rules-builtins-oracle-xmltype"></a>

The following table lists each source object in the XMLTYPE package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| XMLTYPE.CREATEXML(BLOB or BFILE argument) | Rewritten | xmlparse(document convert\_from(⟨arg⟩, 'utf-8')) | 5146: PostgreSQL doesn't support character set identifiers | 
| XMLTYPE.CREATEXML(CHAR, VARCHAR2 or CLOB argument) | Rewritten | xmlparse(document ⟨arg⟩) | None | 
| XMLTYPE.CREATEXML(SYS\_REFCURSOR argument) | Rewritten | xmlroot(xmlelement(name rowset, (SELECT xmlagg(row) FROM unnest(xpath('table/\*', cursor\_to\_xml(⟨arg⟩, …))))), version '1.0') | None | 
| XMLTYPE.CREATEXML(cursor expression) | Rewritten | xmlroot(xmlelement(name rowset, (SELECT xmlagg(row) FROM unnest(xpath('table/\*', query\_to\_xml(⟨arg⟩, …))))), version '1.0') | None | 
| XMLTYPE.CREATEXML(user-defined object type argument) | Rewritten | xmlelement(name ⟨type⟩, xmlforest(⟨attributes⟩)) | None | 
| XMLTYPE.CREATEXML(…) with more than one argument | Rewritten | As for the first argument's type; the remaining arguments are dropped | 5145: PostgreSQL doesn't validate input values of the XML data type | 
| XMLTYPE.EXISTSNODE | Rewritten | xmlexists(⟨arg1⟩ passing (⟨arg2⟩))::integer | None | 
| XMLTYPE.EXTRACT | Rewritten | array\_to\_string(xpath(⟨arg1⟩, ⟨arg2⟩), '')::xml | 5143: Converted code might not work correctly | 
| XMLTYPE.EXTRACT applied to an XMLAGG result | Rewritten | array\_to\_string(xpath(concat\_ws('/','rowset', ⟨arg1⟩), xmlelement(name rowset, ⟨arg2⟩)), '')::xml | 5143: Converted code might not work correctly | 
| XMLTYPE.EXTRACT applied to an XMLFOREST result | Rewritten | array\_to\_string(xpath('//'\|\|⟨arg1⟩, ⟨arg2⟩), '')::xml | 5143: Converted code might not work correctly | 
| XMLTYPE.EXTRACT(…).EXTRACT(…) chained | Rewritten | array\_to\_string(xpath(⟨arg1⟩, ⟨arg2⟩), '')::xml | `5142`: DMS SC can't convert nested calls of the same method<br />`5143`: Converted code might not work correctly | 
| XMLTYPE.GETCLOBVAL | Rewritten | xmlserialize(content ⟨arg⟩ as text) | None | 
| XMLTYPE.GETROOTELEMENT | Rewritten | (xpath('name(/\*)', ⟨arg⟩))[1] | None | 
| XMLTYPE.GETSTRINGVAL | Rewritten | xmlserialize(content ⟨arg⟩ as text) | None | 
| XMLTYPE.TOOBJECT | Extension pack | ⟨arg1⟩ := json\_populate\_record(base => ⟨arg1⟩, from\_json => aws\_oracle\_ext.xmltype$tojson(pxml => ⟨arg2⟩, ptargetjobj => to\_json(⟨arg3⟩))) | 5096: The call of the converted method might produce different results compared to the source method | 
| XMLTYPE.TOOBJECT(…) with more arguments than the object and its XML source | Rewritten | As above; the extra arguments are dropped | `5096`: The call of the converted method might produce different results compared to the source method<br />`5147`: PostgreSQL doesn't support XML schemas | 
| XMLTYPE.TRANSFORM | Not converted | Not applicable | 5141: DMS SC can't convert the XMLTYPE.TRANSFORM method | 

## DBMS\_APPLICATION\_INFO
<a name="sc-default-rules-builtins-oracle-dbms-application-info"></a>

The following table lists each source object in the DBMS\_APPLICATION\_INFO package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_APPLICATION\_INFO.READ\_CLIENT\_INFO | Extension pack | aws\_oracle\_ext.dbms\_application\_info$read\_client\_info | None | 
| SYS.DBMS\_APPLICATION\_INFO.READ\_MODULE | Extension pack | aws\_oracle\_ext.dbms\_application\_info$read\_module | None | 
| SYS.DBMS\_APPLICATION\_INFO.SET\_ACTION | Extension pack | aws\_oracle\_ext.dbms\_application\_info$set\_action | None | 
| SYS.DBMS\_APPLICATION\_INFO.SET\_CLIENT\_INFO | Extension pack | aws\_oracle\_ext.dbms\_application\_info$set\_client\_info | None | 
| SYS.DBMS\_APPLICATION\_INFO.SET\_MODULE | Extension pack | aws\_oracle\_ext.dbms\_application\_info$set\_module | None | 
| SYS.DBMS\_APPLICATION\_INFO.SET\_SESSION\_LONGOPS | Extension pack | aws\_oracle\_ext.dbms\_application\_info$set\_session\_longops | None | 
| SYS.DBMS\_APPLICATION\_INFO.SET\_SESSION\_LONGOPS\_NOHINT | Extension pack | aws\_oracle\_ext.dbms\_application\_info$set\_session\_longops\_nohint() | None | 

## DBMS\_LOCK constants
<a name="sc-default-rules-builtins-oracle-dbms-lock-constants"></a>

The following table lists each source object in the DBMS\_LOCK constants category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.DBMS\_LOCK.MAXWAIT | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('MAXWAIT') | None | 
| SYS.DBMS\_LOCK.NL\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('NL\_MODE') | None | 
| SYS.DBMS\_LOCK.SSX\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('SSX\_MODE') | None | 
| SYS.DBMS\_LOCK.SS\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('SS\_MODE') | None | 
| SYS.DBMS\_LOCK.SX\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('SX\_MODE') | None | 
| SYS.DBMS\_LOCK.S\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('S\_MODE') | None | 
| SYS.DBMS\_LOCK.X\_MODE | Extension pack | aws\_oracle\_ext.dbms\_lock$constant('X\_MODE') | None | 

## Grouping
<a name="sc-default-rules-builtins-oracle-grouping"></a>

The following table lists each source object in the Grouping category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| GROUPING\_ID | Renamed | grouping | None | 
| GROUP\_ID | Not converted | Not applicable | 5340: PostgreSQL doesn't support the GROUP\_ID function | 
| STANDARD.GROUPING | Same name | GROUPING | None | 

## HTF constants
<a name="sc-default-rules-builtins-oracle-htf-constants"></a>

The following table lists each source object in the HTF constants category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.HTF.ADDRESS | Extension pack | aws\_oracle\_ext.htf$address | None | 
| SYS.HTF.ANCHOR | Extension pack | aws\_oracle\_ext.htf$anchor | None | 
| SYS.HTF.ANCHOR2 | Extension pack | aws\_oracle\_ext.htf$anchor2 | None | 
| SYS.HTF.APPLETCLOSE | Extension pack | aws\_oracle\_ext.htf$appletClose() | None | 
| SYS.HTF.APPLETOPEN | Extension pack | aws\_oracle\_ext.htf$appletopen | None | 
| SYS.HTF.AREA | Extension pack | aws\_oracle\_ext.htf$area | None | 
| SYS.HTF.BASE | Extension pack | aws\_oracle\_ext.htf$base | None | 
| SYS.HTF.BASEFONT | Extension pack | aws\_oracle\_ext.htf$basefont | None | 
| SYS.HTF.BGSOUND | Extension pack | aws\_oracle\_ext.htf$bgsound | None | 
| SYS.HTF.BIG | Extension pack | aws\_oracle\_ext.htf$big | None | 
| SYS.HTF.BLOCKQUOTECLOSE | Extension pack | aws\_oracle\_ext.htf$blockquoteClose() | None | 
| SYS.HTF.BLOCKQUOTEOPEN | Extension pack | aws\_oracle\_ext.htf$blockquoteopen | None | 
| SYS.HTF.BOLD | Extension pack | aws\_oracle\_ext.htf$bold | None | 
| SYS.HTF.BR | Extension pack | aws\_oracle\_ext.htf$br | None | 
| SYS.HTF.CENTER | Extension pack | aws\_oracle\_ext.htf$center | None | 
| SYS.HTF.CENTERCLOSE | Extension pack | aws\_oracle\_ext.htf$centerClose() | None | 
| SYS.HTF.CENTEROPEN | Extension pack | aws\_oracle\_ext.htf$centerOpen() | None | 
| SYS.HTF.CITE | Extension pack | aws\_oracle\_ext.htf$cite | None | 
| SYS.HTF.CODE | Extension pack | aws\_oracle\_ext.htf$code | None | 
| SYS.HTF.COMMENT | Extension pack | aws\_oracle\_ext.htf$comment | None | 
| SYS.HTF.DFN | Extension pack | aws\_oracle\_ext.htf$dfn | None | 
| SYS.HTF.DIRLISTCLOSE | Extension pack | aws\_oracle\_ext.htf$dirlistClose() | None | 
| SYS.HTF.DIRLISTOPEN | Extension pack | aws\_oracle\_ext.htf$dirlistOpen() | None | 
| SYS.HTF.DIV | Extension pack | aws\_oracle\_ext.htf$div | None | 
| SYS.HTF.DLISTCLOSE | Extension pack | aws\_oracle\_ext.htf$dlistClose() | None | 
| SYS.HTF.DLISTDEF | Extension pack | aws\_oracle\_ext.htf$dlistdef | None | 
| SYS.HTF.DLISTOPEN | Extension pack | aws\_oracle\_ext.htf$dlistopen | None | 
| SYS.HTF.DLISTTERM | Extension pack | aws\_oracle\_ext.htf$dlistterm | None | 
| SYS.HTF.EM | Extension pack | aws\_oracle\_ext.htf$em | None | 
| SYS.HTF.EMPHASIS | Extension pack | aws\_oracle\_ext.htf$emphasis | None | 
| SYS.HTF.ESCAPE\_SC | Extension pack | aws\_oracle\_ext.htf$escape\_sc | None | 
| SYS.HTF.ESCAPE\_URL | Extension pack | aws\_oracle\_ext.htf$escape\_url | None | 
| SYS.HTF.FONTCLOSE | Extension pack | aws\_oracle\_ext.htf$fontClose() | None | 
| SYS.HTF.FONTOPEN | Extension pack | aws\_oracle\_ext.htf$fontopen | None | 
| SYS.HTF.FORMAT\_CELL | Extension pack | aws\_oracle\_ext.htf$format\_cell | None | 
| SYS.HTF.FORMCHECKBOX | Extension pack | aws\_oracle\_ext.htf$formcheckbox | None | 
| SYS.HTF.FORMCLOSE | Extension pack | aws\_oracle\_ext.htf$formClose() | None | 
| SYS.HTF.FORMFILE | Extension pack | aws\_oracle\_ext.htf$formfile | None | 
| SYS.HTF.FORMHIDDEN | Extension pack | aws\_oracle\_ext.htf$formhidden | None | 
| SYS.HTF.FORMIMAGE | Extension pack | aws\_oracle\_ext.htf$formimage | None | 
| SYS.HTF.FORMOPEN | Extension pack | aws\_oracle\_ext.htf$formopen | None | 
| SYS.HTF.FORMPASSWORD | Extension pack | aws\_oracle\_ext.htf$formpassword | None | 
| SYS.HTF.FORMRADIO | Extension pack | aws\_oracle\_ext.htf$formradio | None | 
| SYS.HTF.FORMRESET | Extension pack | aws\_oracle\_ext.htf$formreset | None | 
| SYS.HTF.FORMSELECTCLOSE | Extension pack | aws\_oracle\_ext.htf$formSelectClose() | None | 
| SYS.HTF.FORMSELECTOPEN | Extension pack | aws\_oracle\_ext.htf$formselectopen | None | 
| SYS.HTF.FORMSELECTOPTION | Extension pack | aws\_oracle\_ext.htf$formselectoption | None | 
| SYS.HTF.FORMSUBMIT | Extension pack | aws\_oracle\_ext.htf$formsubmit | None | 
| SYS.HTF.FORMTEXT | Extension pack | aws\_oracle\_ext.htf$formtext | None | 
| SYS.HTF.FORMTEXTAREA | Extension pack | aws\_oracle\_ext.htf$formtextarea | None | 
| SYS.HTF.FORMTEXTAREA2 | Extension pack | aws\_oracle\_ext.htf$formtextarea2 | None | 
| SYS.HTF.FORMTEXTAREACLOSE | Extension pack | aws\_oracle\_ext.htf$formTextareaClose() | None | 
| SYS.HTF.FORMTEXTAREAOPEN | Extension pack | aws\_oracle\_ext.htf$formtextareaopen | None | 
| SYS.HTF.FORMTEXTAREAOPEN2 | Extension pack | aws\_oracle\_ext.htf$formtextareaopen2 | None | 
| SYS.HTF.FRAME | Extension pack | aws\_oracle\_ext.htf$frame | None | 
| SYS.HTF.FRAMESETCLOSE | Extension pack | aws\_oracle\_ext.htf$framesetClose() | None | 
| SYS.HTF.FRAMESETOPEN | Extension pack | aws\_oracle\_ext.htf$framesetopen | None | 
| SYS.HTF.HEADER | Extension pack | aws\_oracle\_ext.htf$header | None | 
| SYS.HTF.HR | Extension pack | aws\_oracle\_ext.htf$hr | None | 
| SYS.HTF.HTITLE | Extension pack | aws\_oracle\_ext.htf$htitle | None | 
| SYS.HTF.IMG | Extension pack | aws\_oracle\_ext.htf$img | None | 
| SYS.HTF.IMG2 | Extension pack | aws\_oracle\_ext.htf$img2 | None | 
| SYS.HTF.ISINDEX | Extension pack | aws\_oracle\_ext.htf$isindex | None | 
| SYS.HTF.ITALIC | Extension pack | aws\_oracle\_ext.htf$italic | None | 
| SYS.HTF.KBD | Extension pack | aws\_oracle\_ext.htf$kbd | None | 
| SYS.HTF.KEYBOARD | Extension pack | aws\_oracle\_ext.htf$keyboard | None | 
| SYS.HTF.LINE | Extension pack | aws\_oracle\_ext.htf$line | None | 
| SYS.HTF.LINKREL | Extension pack | aws\_oracle\_ext.htf$linkrel | None | 
| SYS.HTF.LINKREV | Extension pack | aws\_oracle\_ext.htf$linkrev | None | 
| SYS.HTF.LISTHEADER | Extension pack | aws\_oracle\_ext.htf$listheader | None | 
| SYS.HTF.LISTINGCLOSE | Extension pack | aws\_oracle\_ext.htf$listingClose() | None | 
| SYS.HTF.LISTINGOPEN | Extension pack | aws\_oracle\_ext.htf$listingOpen() | None | 
| SYS.HTF.LISTITEM | Extension pack | aws\_oracle\_ext.htf$listitem | None | 
| SYS.HTF.MAILTO | Extension pack | aws\_oracle\_ext.htf$mailto | None | 
| SYS.HTF.MAPCLOSE | Extension pack | aws\_oracle\_ext.htf$mapClose() | None | 
| SYS.HTF.MAPOPEN | Extension pack | aws\_oracle\_ext.htf$mapopen | None | 
| SYS.HTF.MENULISTCLOSE | Extension pack | aws\_oracle\_ext.htf$menulistClose() | None | 
| SYS.HTF.MENULISTOPEN | Extension pack | aws\_oracle\_ext.htf$menulistOpen() | None | 
| SYS.HTF.META | Extension pack | aws\_oracle\_ext.htf$meta | None | 
| SYS.HTF.NEXTID | Extension pack | aws\_oracle\_ext.htf$nextid | None | 
| SYS.HTF.NL | Extension pack | aws\_oracle\_ext.htf$nl | None | 
| SYS.HTF.NOBR | Extension pack | aws\_oracle\_ext.htf$nobr | None | 
| SYS.HTF.NOFRAMESCLOSE | Extension pack | aws\_oracle\_ext.htf$noframesClose() | None | 
| SYS.HTF.NOFRAMESOPEN | Extension pack | aws\_oracle\_ext.htf$noframesOpen() | None | 
| SYS.HTF.OLISTCLOSE | Extension pack | aws\_oracle\_ext.htf$olistClose() | None | 
| SYS.HTF.OLISTOPEN | Extension pack | aws\_oracle\_ext.htf$olistopen | None | 
| SYS.HTF.PARA | Extension pack | aws\_oracle\_ext.htf$para() | None | 
| SYS.HTF.PARAGRAPH | Extension pack | aws\_oracle\_ext.htf$paragraph | None | 
| SYS.HTF.PARAM | Extension pack | aws\_oracle\_ext.htf$param | None | 
| SYS.HTF.PLAINTEXT | Extension pack | aws\_oracle\_ext.htf$plaintext | None | 
| SYS.HTF.PRECLOSE | Extension pack | aws\_oracle\_ext.htf$preClose() | None | 
| SYS.HTF.PREOPEN | Extension pack | aws\_oracle\_ext.htf$preopen | None | 
| SYS.HTF.S | Extension pack | aws\_oracle\_ext.htf$s | None | 
| SYS.HTF.SAMPLE | Extension pack | aws\_oracle\_ext.htf$sample | None | 
| SYS.HTF.SCRIPT | Extension pack | aws\_oracle\_ext.htf$script | None | 
| SYS.HTF.SMALL | Extension pack | aws\_oracle\_ext.htf$small | None | 
| SYS.HTF.STRIKE | Extension pack | aws\_oracle\_ext.htf$strike | None | 
| SYS.HTF.STRONG | Extension pack | aws\_oracle\_ext.htf$strong | None | 
| SYS.HTF.STYLE | Extension pack | aws\_oracle\_ext.htf$style | None | 
| SYS.HTF.SUB | Extension pack | aws\_oracle\_ext.htf$sub | None | 
| SYS.HTF.SUP | Extension pack | aws\_oracle\_ext.htf$sup | None | 
| SYS.HTF.TABLECAPTION | Extension pack | aws\_oracle\_ext.htf$tablecaption | None | 
| SYS.HTF.TABLECLOSE | Extension pack | aws\_oracle\_ext.htf$tableClose() | None | 
| SYS.HTF.TABLEDATA | Extension pack | aws\_oracle\_ext.htf$tabledata | None | 
| SYS.HTF.TABLEHEADER | Extension pack | aws\_oracle\_ext.htf$tableheader | None | 
| SYS.HTF.TABLEOPEN | Extension pack | aws\_oracle\_ext.htf$tableopen | None | 
| SYS.HTF.TABLEROWCLOSE | Extension pack | aws\_oracle\_ext.htf$tableRowClose() | None | 
| SYS.HTF.TABLEROWOPEN | Extension pack | aws\_oracle\_ext.htf$tablerowopen | None | 
| SYS.HTF.TELETYPE | Extension pack | aws\_oracle\_ext.htf$teletype | None | 
| SYS.HTF.TITLE | Extension pack | aws\_oracle\_ext.htf$title | None | 
| SYS.HTF.ULISTCLOSE | Extension pack | aws\_oracle\_ext.htf$ulistClose() | None | 
| SYS.HTF.ULISTOPEN | Extension pack | aws\_oracle\_ext.htf$ulistopen | None | 
| SYS.HTF.UNDERLINE | Extension pack | aws\_oracle\_ext.htf$underline | None | 
| SYS.HTF.VARIABLE | Extension pack | aws\_oracle\_ext.htf$variable | None | 
| SYS.HTF.WBR | Extension pack | aws\_oracle\_ext.htf$wbr() | None | 
| SYS.HTP.ADDRESS | Extension pack | aws\_oracle\_ext.htp$address | None | 
| SYS.HTP.ANCHOR | Extension pack | aws\_oracle\_ext.htp$anchor | None | 
| SYS.HTP.ANCHOR2 | Extension pack | aws\_oracle\_ext.htp$anchor2 | None | 
| SYS.HTP.APPLETCLOSE | Extension pack | aws\_oracle\_ext.htp$appletclose | None | 
| SYS.HTP.APPLETOPEN | Extension pack | aws\_oracle\_ext.htp$appletopen | None | 
| SYS.HTP.AREA | Extension pack | aws\_oracle\_ext.htp$area | None | 
| SYS.HTP.BASE | Extension pack | aws\_oracle\_ext.htp$base | None | 
| SYS.HTP.BASEFONT | Extension pack | aws\_oracle\_ext.htp$basefont | None | 
| SYS.HTP.BGSOUND | Extension pack | aws\_oracle\_ext.htp$bgsound | None | 
| SYS.HTP.BIG | Extension pack | aws\_oracle\_ext.htp$big | None | 
| SYS.HTP.BLOCKQUOTECLOSE | Extension pack | aws\_oracle\_ext.htp$blockquoteclose | None | 
| SYS.HTP.BLOCKQUOTEOPEN | Extension pack | aws\_oracle\_ext.htp$blockquoteopen | None | 
| SYS.HTP.BODYCLOSE | Extension pack | aws\_oracle\_ext.htp$bodyclose | None | 
| SYS.HTP.BODYOPEN | Extension pack | aws\_oracle\_ext.htp$bodyopen | None | 
| SYS.HTP.BOLD | Extension pack | aws\_oracle\_ext.htp$bold | None | 
| SYS.HTP.BR | Extension pack | aws\_oracle\_ext.htp$br | None | 
| SYS.HTP.CENTER | Extension pack | aws\_oracle\_ext.htp$center | None | 
| SYS.HTP.CENTERCLOSE | Extension pack | aws\_oracle\_ext.htp$centerclose | None | 
| SYS.HTP.CENTEROPEN | Extension pack | aws\_oracle\_ext.htp$centeropen | None | 
| SYS.HTP.CITE | Extension pack | aws\_oracle\_ext.htp$cite | None | 
| SYS.HTP.CODE | Extension pack | aws\_oracle\_ext.htp$code | None | 
| SYS.HTP.COMMENT | Extension pack | aws\_oracle\_ext.htp$comment | None | 
| SYS.HTP.DFN | Extension pack | aws\_oracle\_ext.htp$dfn | None | 
| SYS.HTP.DIRLISTCLOSE | Extension pack | aws\_oracle\_ext.htp$dirlistclose | None | 
| SYS.HTP.DIRLISTOPEN | Extension pack | aws\_oracle\_ext.htp$dirlistopen | None | 
| SYS.HTP.DIV | Extension pack | aws\_oracle\_ext.htp$div | None | 
| SYS.HTP.DLISTCLOSE | Extension pack | aws\_oracle\_ext.htp$dlistclose | None | 
| SYS.HTP.DLISTDEF | Extension pack | aws\_oracle\_ext.htp$dlistdef | None | 
| SYS.HTP.DLISTOPEN | Extension pack | aws\_oracle\_ext.htp$dlistopen | None | 
| SYS.HTP.DLISTTERM | Extension pack | aws\_oracle\_ext.htp$dlistterm | None | 
| SYS.HTP.EM | Extension pack | aws\_oracle\_ext.htp$em | None | 
| SYS.HTP.EMPHASIS | Extension pack | aws\_oracle\_ext.htp$emphasis | None | 
| SYS.HTP.ESCAPE\_SC | Extension pack | aws\_oracle\_ext.htp$escape\_sc | None | 
| SYS.HTP.FONTCLOSE | Extension pack | aws\_oracle\_ext.htp$fontclose | None | 
| SYS.HTP.FONTOPEN | Extension pack | aws\_oracle\_ext.htp$fontopen | None | 
| SYS.HTP.FORMCHECKBOX | Extension pack | aws\_oracle\_ext.htp$formcheckbox | None | 
| SYS.HTP.FORMCLOSE | Extension pack | aws\_oracle\_ext.htp$formclose | None | 
| SYS.HTP.FORMFILE | Extension pack | aws\_oracle\_ext.htp$formfile | None | 
| SYS.HTP.FORMHIDDEN | Extension pack | aws\_oracle\_ext.htp$formhidden | None | 
| SYS.HTP.FORMIMAGE | Extension pack | aws\_oracle\_ext.htp$formimage | None | 
| SYS.HTP.FORMOPEN | Extension pack | aws\_oracle\_ext.htp$formopen | None | 
| SYS.HTP.FORMPASSWORD | Extension pack | aws\_oracle\_ext.htp$formpassword | None | 
| SYS.HTP.FORMRADIO | Extension pack | aws\_oracle\_ext.htp$formradio | None | 
| SYS.HTP.FORMRESET | Extension pack | aws\_oracle\_ext.htp$formreset | None | 
| SYS.HTP.FORMSELECTCLOSE | Extension pack | aws\_oracle\_ext.htp$formselectclose | None | 
| SYS.HTP.FORMSELECTOPEN | Extension pack | aws\_oracle\_ext.htp$formselectopen | None | 
| SYS.HTP.FORMSELECTOPTION | Extension pack | aws\_oracle\_ext.htp$formselectoption | None | 
| SYS.HTP.FORMSUBMIT | Extension pack | aws\_oracle\_ext.htp$formsubmit | None | 
| SYS.HTP.FORMTEXT | Extension pack | aws\_oracle\_ext.htp$formtext | None | 
| SYS.HTP.FORMTEXTAREA | Extension pack | aws\_oracle\_ext.htp$formtextarea | None | 
| SYS.HTP.FORMTEXTAREA2 | Extension pack | aws\_oracle\_ext.htp$formtextarea2 | None | 
| SYS.HTP.FORMTEXTAREACLOSE | Extension pack | aws\_oracle\_ext.htp$formtextareaclose | None | 
| SYS.HTP.FORMTEXTAREAOPEN | Extension pack | aws\_oracle\_ext.htp$formtextareaopen | None | 
| SYS.HTP.FORMTEXTAREAOPEN2 | Extension pack | aws\_oracle\_ext.htp$formtextareaopen2 | None | 
| SYS.HTP.FRAME | Extension pack | aws\_oracle\_ext.htp$frame | None | 
| SYS.HTP.FRAMESETCLOSE | Extension pack | aws\_oracle\_ext.htp$framesetclose | None | 
| SYS.HTP.FRAMESETOPEN | Extension pack | aws\_oracle\_ext.htp$framesetopen | None | 
| SYS.HTP.HEADCLOSE | Extension pack | aws\_oracle\_ext.htp$headclose | None | 
| SYS.HTP.HEADER | Extension pack | aws\_oracle\_ext.htp$header | None | 
| SYS.HTP.HEADOPEN | Extension pack | aws\_oracle\_ext.htp$headopen | None | 
| SYS.HTP.HR | Extension pack | aws\_oracle\_ext.htp$hr | None | 
| SYS.HTP.HTITLE | Extension pack | aws\_oracle\_ext.htp$htitle | None | 
| SYS.HTP.HTMLCLOSE | Extension pack | aws\_oracle\_ext.htp$htmlclose | None | 
| SYS.HTP.HTMLOPEN | Extension pack | aws\_oracle\_ext.htp$htmlopen | None | 
| SYS.HTP.IMG | Extension pack | aws\_oracle\_ext.htp$img | None | 
| SYS.HTP.IMG2 | Extension pack | aws\_oracle\_ext.htp$img2 | None | 
| SYS.HTP.ISINDEX | Extension pack | aws\_oracle\_ext.htp$isindex | None | 
| SYS.HTP.ITALIC | Extension pack | aws\_oracle\_ext.htp$italic | None | 
| SYS.HTP.KBD | Extension pack | aws\_oracle\_ext.htp$kbd | None | 
| SYS.HTP.KEYBOARD | Extension pack | aws\_oracle\_ext.htp$keyboard | None | 
| SYS.HTP.LINE | Extension pack | aws\_oracle\_ext.htp$line | None | 
| SYS.HTP.LINKREL | Extension pack | aws\_oracle\_ext.htp$linkrel | None | 
| SYS.HTP.LINKREV | Extension pack | aws\_oracle\_ext.htp$linkrev | None | 
| SYS.HTP.LISTHEADER | Extension pack | aws\_oracle\_ext.htp$listheader | None | 
| SYS.HTP.LISTINGCLOSE | Extension pack | aws\_oracle\_ext.htp$listingclose | None | 
| SYS.HTP.LISTINGOPEN | Extension pack | aws\_oracle\_ext.htp$listingopen | None | 
| SYS.HTP.LISTITEM | Extension pack | aws\_oracle\_ext.htp$listitem | None | 
| SYS.HTP.MAILTO | Extension pack | aws\_oracle\_ext.htp$mailto | None | 
| SYS.HTP.MAPCLOSE | Extension pack | aws\_oracle\_ext.htp$mapclose | None | 
| SYS.HTP.MAPOPEN | Extension pack | aws\_oracle\_ext.htp$mapopen | None | 
| SYS.HTP.MENULISTCLOSE | Extension pack | aws\_oracle\_ext.htp$menulistclose | None | 
| SYS.HTP.MENULISTOPEN | Extension pack | aws\_oracle\_ext.htp$menulistopen | None | 
| SYS.HTP.META | Extension pack | aws\_oracle\_ext.htp$meta | None | 
| SYS.HTP.NEXTID | Extension pack | aws\_oracle\_ext.htp$nextid | None | 
| SYS.HTP.NL | Extension pack | aws\_oracle\_ext.htp$nl | None | 
| SYS.HTP.NOBR | Extension pack | aws\_oracle\_ext.htp$nobr | None | 
| SYS.HTP.NOFRAMESCLOSE | Extension pack | aws\_oracle\_ext.htp$noframesclose | None | 
| SYS.HTP.NOFRAMESOPEN | Extension pack | aws\_oracle\_ext.htp$noframesopen | None | 
| SYS.HTP.OLISTCLOSE | Extension pack | aws\_oracle\_ext.htp$olistclose | None | 
| SYS.HTP.OLISTOPEN | Extension pack | aws\_oracle\_ext.htp$olistopen | None | 
| SYS.HTP.P | Extension pack | aws\_oracle\_ext.htp$p | None | 
| SYS.HTP.PARA | Extension pack | aws\_oracle\_ext.htp$para | None | 
| SYS.HTP.PARAGRAPH | Extension pack | aws\_oracle\_ext.htp$paragraph | None | 
| SYS.HTP.PARAM | Extension pack | aws\_oracle\_ext.htp$param | None | 
| SYS.HTP.PLAINTEXT | Extension pack | aws\_oracle\_ext.htp$plaintext | None | 
| SYS.HTP.PRECLOSE | Extension pack | aws\_oracle\_ext.htp$preclose | None | 
| SYS.HTP.PREOPEN | Extension pack | aws\_oracle\_ext.htp$preopen | None | 
| SYS.HTP.PRINT | Extension pack | aws\_oracle\_ext.htp$print | None | 
| SYS.HTP.PRINTS | Extension pack | aws\_oracle\_ext.htp$prints | None | 
| SYS.HTP.PRN | Extension pack | aws\_oracle\_ext.htp$prn | None | 
| SYS.HTP.PS | Extension pack | aws\_oracle\_ext.htp$ps | None | 
| SYS.HTP.PUTRAW | Extension pack | aws\_oracle\_ext.htp$putraw | None | 
| SYS.HTP.S | Extension pack | aws\_oracle\_ext.htp$s | None | 
| SYS.HTP.SAMPLE | Extension pack | aws\_oracle\_ext.htp$sample | None | 
| SYS.HTP.SCRIPT | Extension pack | aws\_oracle\_ext.htp$script | None | 
| SYS.HTP.SMALL | Extension pack | aws\_oracle\_ext.htp$small | None | 
| SYS.HTP.STRIKE | Extension pack | aws\_oracle\_ext.htp$strike | None | 
| SYS.HTP.STRONG | Extension pack | aws\_oracle\_ext.htp$strong | None | 
| SYS.HTP.STYLE | Extension pack | aws\_oracle\_ext.htp$style | None | 
| SYS.HTP.SUB | Extension pack | aws\_oracle\_ext.htp$sub | None | 
| SYS.HTP.SUP | Extension pack | aws\_oracle\_ext.htp$sup | None | 
| SYS.HTP.TABLECAPTION | Extension pack | aws\_oracle\_ext.htp$tablecaption | None | 
| SYS.HTP.TABLECLOSE | Extension pack | aws\_oracle\_ext.htp$tableclose | None | 
| SYS.HTP.TABLEDATA | Extension pack | aws\_oracle\_ext.htp$tabledata | None | 
| SYS.HTP.TABLEHEADER | Extension pack | aws\_oracle\_ext.htp$tableheader | None | 
| SYS.HTP.TABLEOPEN | Extension pack | aws\_oracle\_ext.htp$tableopen | None | 
| SYS.HTP.TABLEROWCLOSE | Extension pack | aws\_oracle\_ext.htp$tablerowclose | None | 
| SYS.HTP.TABLEROWOPEN | Extension pack | aws\_oracle\_ext.htp$tablerowopen | None | 
| SYS.HTP.TELETYPE | Extension pack | aws\_oracle\_ext.htp$teletype | None | 
| SYS.HTP.TITLE | Extension pack | aws\_oracle\_ext.htp$title | None | 
| SYS.HTP.ULISTCLOSE | Extension pack | aws\_oracle\_ext.htp$ulistclose | None | 
| SYS.HTP.ULISTOPEN | Extension pack | aws\_oracle\_ext.htp$ulistopen | None | 
| SYS.HTP.UNDERLINE | Extension pack | aws\_oracle\_ext.htp$underline | None | 
| SYS.HTP.VARIABLE | Extension pack | aws\_oracle\_ext.htp$variable | None | 
| SYS.HTP.WBR | Extension pack | aws\_oracle\_ext.htp$wbr | None | 
| SYS.OWA\_COOKIE.GET | Extension pack | aws\_oracle\_ext.owa\_cookie$get | None | 
| SYS.OWA\_COOKIE.SEND | Extension pack | aws\_oracle\_ext.owa\_cookie$send | None | 
| SYS.OWA\_UTIL.GET\_CGI\_ENV | Extension pack | aws\_oracle\_ext.owa\_util$get\_cgi\_env | None | 
| SYS.OWA\_UTIL.GET\_OWA\_SERVICE\_PATH | Extension pack | aws\_oracle\_ext.owa\_util$get\_owa\_service\_path | None | 
| SYS.OWA\_UTIL.HTTP\_HEADER\_CLOSE | Extension pack | aws\_oracle\_ext.owa\_util$http\_header\_close | None | 
| SYS.OWA\_UTIL.MIME\_HEADER | Extension pack | aws\_oracle\_ext.owa\_util$mime\_header | None | 
| SYS.OWA\_UTIL.PRINT\_CGI\_ENV | Extension pack | aws\_oracle\_ext.owa\_util$print\_cgi\_env | None | 
| SYS.OWA\_UTIL.REDIRECT\_URL | Extension pack | aws\_oracle\_ext.owa\_util$redirect\_url | None | 
| SYS.OWA\_UTIL.STATUS\_LINE | Extension pack | aws\_oracle\_ext.owa\_util$status\_line | None | 

## ROLLUP and CUBE clause
<a name="sc-default-rules-builtins-oracle-rollup-cube-clause"></a>

The following table lists each source object in the ROLLUP and CUBE clause category and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| STANDARD.CUBE | Same name | CUBE | None | 
| STANDARD.ROLLUP | Same name | ROLLUP | None | 

## SYS.ANYDATA
<a name="sc-default-rules-builtins-oracle-sys-anydata"></a>

The following table lists each source object in the SYS.ANYDATA package and shows how DMS Schema Conversion converts it.


| Source | Conversion | Target | Action item | 
| --- | --- | --- | --- | 
| SYS.ANYDATA.ACCESSBDOUBLE | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessBDouble | None | 
| SYS.ANYDATA.ACCESSBFILE | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessBfile | None | 
| SYS.ANYDATA.ACCESSBFLOAT | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessBFloat | None | 
| SYS.ANYDATA.ACCESSBLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessBlob | None | 
| SYS.ANYDATA.ACCESSCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessChar | None | 
| SYS.ANYDATA.ACCESSCLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessClob | None | 
| SYS.ANYDATA.ACCESSDATE | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessDate | None | 
| SYS.ANYDATA.ACCESSINTERVALDS | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessIntervalDS | None | 
| SYS.ANYDATA.ACCESSINTERVALYM | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessIntervalYM | None | 
| SYS.ANYDATA.ACCESSNCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessNchar | None | 
| SYS.ANYDATA.ACCESSNCLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessNClob | None | 
| SYS.ANYDATA.ACCESSNUMBER | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessNumber | None | 
| SYS.ANYDATA.ACCESSNVARCHAR2 | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessNVarchar2 | None | 
| SYS.ANYDATA.ACCESSRAW | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessRaw | None | 
| SYS.ANYDATA.ACCESSTIMESTAMP | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessTimestamp | None | 
| SYS.ANYDATA.ACCESSTIMESTAMPLTZ | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessTimestampLTZ | None | 
| SYS.ANYDATA.ACCESSTIMESTAMPTZ | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessTimestampTZ | None | 
| SYS.ANYDATA.ACCESSUROWID | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessURowid | None | 
| SYS.ANYDATA.ACCESSVARCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessVarchar | None | 
| SYS.ANYDATA.ACCESSVARCHAR2 | Extension pack | aws\_oracle\_ext.sys\_anydata$AccessVarchar2 | None | 
| SYS.ANYDATA.CONVERTBDOUBLE | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertBDouble | None | 
| SYS.ANYDATA.CONVERTBFILE | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertBfile | None | 
| SYS.ANYDATA.CONVERTBFLOAT | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertBFloat | None | 
| SYS.ANYDATA.CONVERTBLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertBlob | None | 
| SYS.ANYDATA.CONVERTCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertChar | None | 
| SYS.ANYDATA.CONVERTCLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertClob | None | 
| SYS.ANYDATA.CONVERTDATE | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertDate | None | 
| SYS.ANYDATA.CONVERTINTERVALDS | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertIntervalDS | None | 
| SYS.ANYDATA.CONVERTINTERVALYM | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertIntervalYM | None | 
| SYS.ANYDATA.CONVERTNCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertNchar | None | 
| SYS.ANYDATA.CONVERTNCLOB | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertNClob | None | 
| SYS.ANYDATA.CONVERTNUMBER | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertNumber | None | 
| SYS.ANYDATA.CONVERTNVARCHAR2 | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertNVarchar2 | None | 
| SYS.ANYDATA.CONVERTRAW | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertRaw | None | 
| SYS.ANYDATA.CONVERTTIMESTAMP | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertTimestamp | None | 
| SYS.ANYDATA.CONVERTTIMESTAMPLTZ | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertTimestampLTZ | None | 
| SYS.ANYDATA.CONVERTTIMESTAMPTZ | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertTimestampTZ | None | 
| SYS.ANYDATA.CONVERTUROWID | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertURowid | None | 
| SYS.ANYDATA.CONVERTVARCHAR | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertVarchar | None | 
| SYS.ANYDATA.CONVERTVARCHAR2 | Extension pack | aws\_oracle\_ext.sys\_anydata$ConvertVarchar2 | None | 
| SYS.ANYDATA.GETTYPENAME | Extension pack | aws\_oracle\_ext.sys\_anydata$getTypeName | None | 