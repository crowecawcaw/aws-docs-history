AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Blu Age release notes

This section contains the release notes of AWS Blu Age Runtime and Modernization Tools from version
3.5.0 onward, most recent first, organized by version number.

For each release, AWS Blu Age Runtime has been validated on specific versions of tools
(Tomcat, Postgres, Oracle, MQ, etc.) and dependencies (Spring, Angular, etc.). Using other versions
(e.g., upgrading to newer versions) requires thorough customer testing and validation.

###### Note

For release notes predating this document, contact AWS Blu Age delivery services. For information
about the latest Blu Insights features, see [Blu
Insights releases](https://bluinsights.aws/releases "https://bluinsights.aws/releases").

## Release notes 5.1.0

Released on: November 18, 2025

This release of AWS Blu Age Runtime and Transformation Engines introduces significant enhancements to platform capabilities, performance optimizations, and modernized technologies. Some key features and changes include:

For more information about the changes included in this release, see the following
sections.

- **AWS Blu Age Transformation Engines & Runtime for GS21**

Added support of Fujitsu proprietary mainframe GS21 in the context of the MAJI (Modernization Acceleration Joint Initiative) partnership. Main features
include several new languages like PSAM, ADL, ACSGEN or JCL XSP, modernization of the network database NDB, implementation of GS21 ecosystems
like AIM, OFM and ACSAPI and support of the JEF encoding.

- **Java version upgrade**

Upgraded from Java 17 to Java 21, increasing security, performance, and allowing customers to deploy and run applications implemented in a of more modern
language and to use recent third party framework versions

This version of the AWS Blu Age Runtime has been tested with the following stack:

|                           |                         |
| ------------------------- | ----------------------- |
| **Component**             | **Version tested**      |
| Java                      | Java 21                 |
| Presentation layer        | Node JS 22.17.1         |
| Npm 10.9.0                |
| Angular 20                |
| Service layer             | Spring Boot 3.5.7       |
| Spring Core 6.2.12        |
| Spring Session 3.5.2      |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 15.10 |
| Oracle 21c                |
| Report                    | Jasper 6                |
| Application server        | Apache Tomcat 10.1.40   |

## AWS Blu Age Runtime

### zOS

**Improvements**

- COBOL
  - Added Support for CEELOCT, CEESECS, CEEDATE utility routines
  - Improved support for JSON GENERATE statement and option COUNT
  - Improved support for BY VALUE clause in PROCEDURE DIVISION statement
  - Improved support for COMPUTE statement to handle exponential representation for numeric literals
  - Improved support for CICS START command for option TRANS and SYSID
  - Improved support for MOVE statement to handle overflow numeric literal
  - Improved support for division scaling for fixed precision types
  - Improved support for CALL statement with USING clause

- JCL - SORT
  - Added support for DATE format "4MD/"
  - Added support for RESTART keyword
  - Added support for DATENS and TIMENS keywords
  - Added support for format Y2S
  - Improved support for OUTFIL statement with multiple files
  - Improved support for REMARKS fields
  - Improved support for OUTREC statement and SYMNAMES binding
  - Improved support for numeric and alphanumeric checks for INCLUDE statement

- JCL - DSNUTILB
  - Improved support for COPYDDN when GDG file is used as parameter

- JCL - IDCAMS
  - Improved support for dataset definition with single quotes

- JCL - Misc
  - Added support to handle empty PARM passing to program through JCL
  - Added support for INZUTILB utility
  - Added support for parameterized generation number in GDG DD statement
  - Enhanced read of SYSIN files with a record size

- Blusam
  - Change default value for property openwarmup from true to false
  - Added new YML property useBatchInMemoryAtomic to enable in-memory-atomic mode for Redis batch read operations
  - Improved support for indexed data sets rewrite when an invalid key is encountered
  - Improved support for large KSDS internal table creation with OID data type
  - Improved support for large KSDS data read when fetching the previous/next page

- SQL
  - Improved support for host variables in SQL CONNECT statement
  - Improved support for Data conversion in SQL query
  - Improved support for parameterized queries with double-quoted identifiers

- IMS
  - Improved support for NULLVAL in XDFLD statement
  - Added support for SEG statement and multiple END statement

- CICS
  - Improved support for RETURN command to handle INPUTMSG option

### AS400

**Improvements**

- RPG
  - Added support for multi table in LOOKUP for CTDATA
  - Added support for \*OMIT parameter in feedback code handling of CEELOCT API
  - Added support for \*LOVAL assigned to date, time and timestamp field types
  - Added support to convert ISO0 expression to timestamp
  - Improved byte size calculation for indexed array
  - Improved support of MOVEA operation between heterogeneous array types zoned and packed
  - Improved support of MOVEA operation from array defined in DS with OCCURS
  - Improved support of MOVEA with array based on external Data Structure
  - Improved dynamic indicator access using a variable with MOVEA
  - Improved support for MOVE statement from data structure to stand-alone field
  - Improved support for nested built-in %DEC(%SUBST())
  - Improved support for EXTFILE keyword to use the library list only when the library is not specified
  - Improved support for EDITCODE with option A,J,P, K and CHECK(RB)
  - Added support of keyword \*JOBRUN to set the separators for type Date and Time

- CL
  - Added support for QRCVDTAQ command
  - Added support for RNMOBJ command
  - Improved support for CPYFTOIMPF command involving decimal value under 1 and empty values
  - Improved support for CPYTOIMPF command to preserve insertion order and output single spaces for empty strings in non nullable columns
  - Improved support for OPNQRYF command with "QRYSLT" option and DB columns that are different from Java entity field names
  - Improved support for OPNQRYF command when entity field names does not match DB column names
  - Improved support for OPNQRYF command with KEYFLD parameters containing MAPFLD values
  - Improved support for SNDPGMMSG command with parameters MSGTYPE(\*STATUS) and TOPGMQ(\*EXT)
  - Improved support for CPYF command and MBROPT option when partition does not exist and CRTF(\*YES)
  - Improved support for CPYF command with numeric data validation and error handling by adding pre-conversion checks and zero-value fallbacks
  - Improved support for CPYF command with INCREL parameter
  - Improved support for CPYF command to handle manual row insertion to handle NULL numeric fields
  - Improved support for SBMOBJ command to retrieve the user name in the context when it is defined and with the default value JOBD otherwise
  - Improved support for RMVMSG command for parameters MSGQ and MSGKEY
  - Improved support for output format of DSPDBR command
  - Improved support of CHGDTAARA command to handle the Local Data Area
  - Improved DSPDBR command output accuracy by implementing proper case handling, default values, and space padding while ensuring consistent record numbering and member name display
  - Improved support for RTVJOBA command to handle USRLIBL attribute
  - Improved support for MOVOBJ command to handle flat files
  - Improved support for RMVM command to handle RangeReference File as a parameter
  - Improved support for PgmAlcObj and PgmDlcObj commands to ignore lock operations for flat files
  - Improved support of OVRDBF with flat file and \*LIBL
  - Improved support of RTVOBJD to return LIB name with disk file
  - Added support for message CPF999 that catches all unhandled messages
  - Improved view retrieval for RTVMBRD without whereConditions

- Database access
  - Enhanced file override capabilities to support JOIN files
  - Enhanced precedence rules of AND/OR operators when processing multiple Select/Omit conditions
  - Improved concurrent cache synchronization using timestamp-based record versioning
  - Improved support for OVRDBF with batch write operation
  - Improved Database record locking mechanism on multi-thread access
  - Improved cache initialization on READ operation
  - Improved support for DELETE operation under Commit Control
  - Improved support of primary file with multi-format logical files
  - Added support of LIBL for DataArea and CURLIB accross jobs

- Screen
  - Improved escaping of single-quotes for String value
  - Improved web component cleanup when handling write operations with no overlay, specifically for components marked with keep keyword
  - Improved support for keyword SLNO
  - Improved support for Terminal ID
  - Improved support for large numbers in an input field
  - Improved cursor positioning while loading tables in front-end by sorting the display files column by rows and in each row by columns
  - Added support for PUTRETAIN (Put-Retain) keyword for display files
  - Improved support of Terminal ID accross an online session

- Printer
  - Improved support for page number generation
  - Added support for overflow handling in reports
  - Added support for INFDS keyword for printer files

- Job
  - Improved job resources cleaning at the end of a online session
  - Improved Quartz job logging to include username and formatted jobNumber to job properties
  - Improved JobHistory creation to dynamically use netName for interactive sessions
  - Improved support for job submission and date format validation

- Misc
  - Added support for EBCDIC CP1047 sort function for Postgres
  - User Space - Improved Error code parameters for Errc0100 Format for User Space
  - Upgraded Jedis to version 6.0.0 to improve session persistence in Redis and extended session tracking support across multiple endpoints.
  - Improved support for composed program when the program ID format contains "/" characters
  - Improved handling of DDS fields defined as parameter of the program
  - Improved support of the ErrorCode parameter for command QMHSNDPM
  - Improved support for date conversion from ISO to EUR

## AWS Blu Age Transformation Engines

### zOS

**Improvements**

- COBOL
  - Improved support for line continuation and multi-line string
  - Improved support for statement INITIALIZE with multiple fields
  - Improved support for copybooks containing occurs statement in the dependencies
  - Improved file format generation by removing comma separators in numeric values and adding binary type support for COMP fields
  - Improved support for CALL statement using option BY VALUE ZERO
  - Improve support for JSON GENERATE statement to handle NAME phrase

- CICS
  - Improved support for LINK command with SYNCONRETURN option
  - Improved support for GET CONTAINER command with NODATA option
  - Improved support for WRITE OPERATOR TEXT command for option ROUTECODES & NUMROUTES
  - Added support for INQUIRE TSPOOL command

- IMS
  - Improved support for SLASHSX and DDATA in DBD files transformation
  - Enhanced support for TITLE after PRINT keyword in MFS map
  - Added support for COPY and EQU statements support for MFS files

- SQL
  - Accept FLOOR keyword as column name
  - Improved support for TIME-ZONE fields
  - Improved support for if condition and consective subqueries within FROM and JOIN clause

### AS400

**Improvements**

- RPG
  - Improved support of DO operation
  - Added support for result indicators on MOVE/MOVEL operation
  - Improved support for MOVE operation for standalone array field
  - Improved support for MOVEA operation when moving values from arrays to indicators
  - Improved support of Z-ADD operation with result field as an array.
  - Improved support for \*Start keyword for data access funtion like SETLL
  - Improved support for calling procedures with parameters passed byValue defined in external files
  - Improved support for sizePrefixedAlphanumeric using \*ALL figurative
  - Improved support for EXTIND function
  - Added support for GOTOs instruction in subroutines in which their corresponding TAGs are in the main subroutine
  - Improved support of NOT keyword in IFs/LOOPs conditions
  - Improved field renaming through input specifications
  - Improved tracking of intermediary results' scale/precision for multiplications
  - Implemented output specification indicator conditions
  - Improved support of LOOKUP operation
  - Improved support of pointers across programs
  - Improved support for %CHAR for numeric inputs
  - Improved support of %dec builtin function used with a single argument
  - Improved data structure field initialization
  - Improved handling of binary integer target type when processing \*ALL literal
  - Improved handling \*LOVAL with Packed, Float and Double types

- CL
  - Improved support for DCL statement to handle duplicate occurrences
  - Improved support for SUBROUTINE and OTHERWISE statement

- DDS
  - Improved key fields detection for packed type fields
  - Improved support of LIKE keyword in physical files

- DSPF
  - Improved support for DSPATR keyword when COLOR is not explicitly specified
  - Improved support of field override through keyword REFFLD
  - Improved support for input specification for record with no input fields in new design

- PRTF
  - Improved program described prtf transformation with empty .prtf legacy file
  - Improved layout setting on JASPER template generation
  - Improved handling of AS400 output specifications with edit words (formatting patterns)
  - Implemented data formatting capabilities for EditCode, EditWord and negative sign handling in RPGLE output specifications
  - Added support for "DLTEDT" keyword
  - Added support for Output Indicators for PRTF files

- Misc
  - Improved support for PFkey convertion to take into account encoding when converting symbolic constants for CICS aid keys

## AWS Blu Age Transformation Engines & Runtime for GS21

**Improvements**

- Languages:
  - ADL: AIM Description Language, used to describe AIM artifacts (PEDs, NDB (sub)schemas, VSAM schemas, AIM Procedures, etc..)
    - Transformed into database configuration records, DDL scripts, JSON files processed by the Data Migrator, etc...

  - ACSGEN: ACS Environment Generator, used to generate system data sets, control tables, ADL sources, application program entry points...
    - Transformed into database configuration records

  - PSAM: Presentation Service Access Method, used to describe online screens
    - Transformed into Angular artifacts

  - JCLXSP: Job Control Language used on the GS21 XSP platform: special syntax of JCL with specific functionalities
    - Transformed into Groovy scripts

  - GS21 COBOL: support for GS21 specific constructs (mainly related to Japanese language support)

- Database:
  - NDB: Network Database
    - Customizable transformation to a modern relational database
    - Data Migration processing the GS21 TDUMP format
    - Transformation of the network links to modern SQL relations (using foreign keys and additional columns to retain the NEXT/PRIOR order stemming from the legacy database)
    - Code Generation of a modern Java DAO layer backed by the newly introduced GS21 runtime

- GS21 ecosystems:
  - AIM: Advanced Information Manager. Main GS21 middleware handling screens, printers, workstations, databases, and external communications via a messaging approach backed by queues.
  - ACSAPI: GS21 special program implementing the ACS protocol that enables screen scenarios (programs inter-communication, PSAM/printer interactions, VSAM access, etc...) (ancestor of AIM).
  - OFM: Online Format Management, GS21 subsystem used for program communication using message files (ancestor of ACS).
  - JXGIJSM, KQCAMS, KDJBR14, JXKUNLOD, JXKRELOD, etc...: Various GS21 JCL utilities
  - Support for OS commands

- Specific Encoding: JEF
  - Double-byte encoding (same principles as IBM930 but different SOSI values (0x28, 0x29)).
  - Custom JEF-PU encoding preserving private use characters
  - The corresponding font is used in the webapps/pdfs in order to reproduce the display with maximum fidelity

## Release notes 4.10.0

Released on: August 29, 2025

This release of AWS Blu Age Runtime and Transformation Engines introduces enhancements to platform capabilities, performance optimizations, and modernized technologies. Some key features and changes include:

- **Enhanced AS/400 Library Resolution**

Introduced a smart library list management system that delivers native AS/400 library list behavior while maintaining optimal performance. The system automatically resolves object libraries based on the system's library list (\*LIBL) without impacting application speed.

- **Front-end Modernization**

Front-end applications have been upgraded to Angular version 20, bringing the latest features and performance improvements to the user interface.

This version of the AWS Blu Age Runtime has been tested with the following stack:

|                           |                         |
| ------------------------- | ----------------------- |
| **Component**             | **Version tested**      |
| Java                      | Java 17                 |
| Presentation layer        | Node JS 22.17.1         |
| Npm 10.9.0                |
| Angular 20                |
| Service layer             | Spring Boot 3.4.6       |
| Spring Core 6.2.2         |
| Spring Session 3.4.1      |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 15.10 |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.40   |

## AWS Blu Age Runtime

### zOS

**Improvements**

- COBOL
  - Improved support for the JCL-COBOL parameter communication with robust byte-level handling to prevent array boundary exceptions
  - Improved support for DFHEILBK and DFHEIBLC in copy statements
  - Improved support for MOVE statement functionality to handle non-numeric to numeric field conversions with expected zero value output
  - Improved support for EXAMINE statement processing with integer-type parameters
  - Added support for the usage PROCEDURE-POINTER
  - Improved XML escape characters
  - Added support for FREE statement and adapt ALLOCATE statement

- JCL - IDCAMS
  - Added support for keyword SKIP in the REPRO statement
  - Improved support of the DELETE statement for NONVSAM files

- JCL - ICEGENER
  - Improved handling of DCB parameters for dummy SYSUT1
  - Improved support for the Dynamic Control Block (DCB) parameter handling when SYSUT1 is defined as DUMMY, ensuring proper data set allocation and preventing processing errors that could occur during copy operations with dummy input data sets

- JCL - SORT
  - Added support for the case of concatenated empty files
  - Improved record comparison by updating byte calculation for ZD (Zone Decimal) fields
  - Improved support for JOINKEY - FILL and REFORMAT FIELD
  - Improved concatenated file processing to properly maintain record size consistency between input data sets
  - Enhanced Sort grammar and corresponding runtime handling for X'..' (hex literals), DATE=(...), and TIME keywords used in HEADER and TRAILER clauses of OUTFIL.

- JCL - ICETOOL
  - Added support for some COUNT operator options : EMPTY, NOTEMPTY, HIGHER(x), LOWER(y), EQUAL(v), NOTEQUAL(w)

- JCL - DSNUTILB
  - Improved support for null DATE columns insertion
  - Added support for VARCHAR, DECIMAL & INTEGER data types when using delimiters
  - Improved support for default value insertions when columns are not specified in control cards
  - Improved support for variable length record processing by excluding Record Descriptor Word (RDW) fields from the record content
  - Improved support for handling null values in database columns during LOAD operations
  - Improved support for decimal data type loading to ensure precise numeric conversions
  - Improved support for WORKDDN parameter when used in combination with FORMAT DELIMITED and POSITION(\*) specifications

- JCL - Misc
  - Added support for SystemOut definitions with comma-based syntax like SYSOUT=(,)
  - Improved support for DD statements containing special character #
  - Improved support for handling multiple conditions within enclosing brackets
  - Added support for DSN syntax enclosed in double quotes
  - Added support for COPYDDN(name) syntax specification
  - Improved support for duplicate DD statements by maintaining z/OS-like behavior of retaining the first assignment
  - Improved support for SYSOUT data set handling with SPIN and FREE parameters, enabling proper buffering and end-of-job printing of SYSOUT DD content
  - Enhanced error reporting for jobs in the Groovy execution API
  - Enabled dynamic allocation of temporary files through a YML property

- Blusam
  - Improved support for CLEAR operations by enhancing metadata cleanup processes to ensure all references to previously stored data are completely removed
  - Improved performance of WRITE operations with write-behind mode enabled
  - Improved support of data set operations by optimizing table existence verification processes, eliminating redundant lookup operations and enhancing overall performance through reduced database queries
  - Improved performance by adding a new open mode (data set level locking only mode) that sets bulk insertion mode to true. This configuration is useful in custom data set restore scenarios where dataset-level locks are sufficient.
  - Extended configuration for large <noloc>Blusam</noloc> KSDS by allowing the use of yml ds configuration file to set properties
  - Added support for graphic alphanumeric in mask generation
  - Improved error reporting when the alternate index is missing in the data set metadata
  - Enabled asynchronous execution of Redis bulk write operations to improve performance. The feature is configurable through a YML property.

- SQL
  - Added support for the CONNECT statement
  - Enhanced SQL support for variable names and operator expression UPDATE queries involving cursors
  - Improved string replacement in SQL Prepare statement

- Security
  - Enhanced API security: implemented mandatory authentication and role-based authorization for all gapwalk-application REST endpoints when security configuration is enabled.
  - Improved JWT token authorization by implementing custom scope-to-role mapping, enabling proper access to protected endpoints when using Cognito-issued bearer tokens.

- Misc
  - Enhanced Redis integration with comprehensive logging, error handling, and diagnostics, including 50+ new context checks and 137 refined error messages.
  - Improved initialization of the job at first running transaction

### AS400

**New features**

- Added support for the library list feature to automate the library resolution depending on the available libraries and the library list
- CL
  - Added support for QDBRTVFD command that retrieves the description of a database file
  - Added support for command QCMDCHK for checking and analysis.

**Improvements**

- RPG
  - Improved support of Z-ADD operation to handle the case of adding 2 arrays of Packed Type
  - Improved support of constant initialization with built-in functions
  - Improved support of EDTWRD with an empty string
  - Improved support of MOVE statement to handle the case of negative values assigned to packed fields without integer part
  - Improved support of \*LOVAL keyword for Character and Zoned types

- COBOL
  - Improved support of COBOL File status to handle the case when the field is not an elementary range
  - Improved setting of the file status code on retrieve in Random mode
  - Improved string encoding for the COBOL function DISPLAY-OF

- CL
  - Added support for command QCMDCHK
  - Improved support for CPYF command to handle multi-record format LFs
  - Improved support for RMVM command to delete member when other objects depend on it
  - Improved parameters support to handle trailing spaces in command RMVM
  - Improved QCMDEXC command with enhanced argument handling, including support for positional parameters and proper argument order retrieval
  - Improved OVRPRTF command by implementing default value (\*STD) for unspecified FORMTYPE parameter
  - Improved support for RTVJOBA to return job number with 6 characters
  - Improved support for OPNQRYF command and KEYFLD parameter
  - Improved support for Unicode characters for OPNQRYF command and single-quote escaping
  - Improved handling of the output file name for command CPYF
  - Improved RTVMBRD command with enhanced view retrieval capabilities, including support for operations without where conditions and proper header handling for row counting
  - Improved support for DSPJOB command to handle calls using both PATH and JOB parameters
  - Improved support for RTVOBJD command to handle file in directory
  - Improved support of ADDPFM command to handle parameters containing trailing spaces
  - Improved thread synchronization in CHGDTAARA

- Database access
  - Enhanced file override capabilities to support JOIN files
  - Enhanced precedence rules of AND/OR operators when processing multiple Select/Omit conditions

- Screen
  - Improved cursor location when two screens share a field name
  - Improved support of RRN field for Workstation file
  - Handled additional messages screen from Modal windows
  - Improved display of the message line as an array in DS4 format
  - Improved the display of error messages as well as the additional message information screen on AS400 applications
  - Improved support of character @ in modernized front-end
  - Improved session handling in the front-end to enable running multiple sessions on the same browser with multiple tabs

- Printer
  - Improved overflow handling for printer files with multiple record headers.

- Misc
  - Added Redis support for user spaces
  - Added support for the API QUSLFLD that generates a list of fields within a specified file record format name using the user space.

## AWS Blu Age Transformation Engines

### zOS

**Improvements**

- COBOL
  - Improved support for CLOB-LOCATOR / DBBLOB-LOCATOR / BLOB-LOCATOR
  - Improved support for IF statement with abbreviated binary conditions
  - Improved support for DFHEIBLK/EIBLK handling both with and without copy statements
  - Refined state machine functionality with enhanced comment handling and optimized EXIT logic for multiple section calls.
  - Improved support of EXIT SECTION statement
  - Improved support of word REPLACING ALL in INITIALIZE statement

- SQL
  - Improved support for SQL alias declaration for update query
  - Improved support for postgreSQL partition creation by ignoring ENDING and INCLUSIVE keywords

- Common
  - Improved Error reporting for Transformation Errors

### AS400

**Improvements**

- DSPF
  - Enhanced field length calculation to accurately match value format, preventing display issues

- PRTF
  - Improved generation of page number on multi-pages report
  - Improved constant display on report

- RPG
  - Added support for \*ALL when used with Z-ADD on an array
  - Improved support of figurative constant \*ALL with Hexadecimal types
  - Added support for \*HIVAL when specified as a parameter for INZ option
  - Handled extender H to round-up the result of DIV operation
  - Improved support for LOOKUP function to handle high, low and equal indicators based on the sort of input array being passed (ASCENDING OR DESCENDING)
  - Improved support for the ADD function to perform element wise addition when factor1, factor2 and result fields are all arrays
  - Improved support for the EDTWRD function in field declaration
  - Improved support of CLEAR operation with INPUT file
  - Improved initialization of arrays defined as stand-alone fields
  - Improved support of \*NEXT option in OVERLAY keyword
  - Improved support for keyword \*ZEROS when used on MOVEA operation

- Misc
  - Improved support of large numbers using BigDecimal

## Release notes 4.9.0

Release date: July 17, 2025

This release of AWS Blu Age Runtime and Transformation Engines introduces key updates to core dependencies:

- **AS400**: Introduced an alternative JDBC-based implementation alongside the existing JPA support in our DAO framework.
  Users can now switch between JPA and JDBC implementations through YML configuration.
  Initial benchmarks show that the new JDBC support delivers significant performance improvements,
  reducing execution times by approximately 50% compared to the JPA implementation.
- **zOS :** Introduced a DB2 z/OS to DB2 LUW migration solution
  addressing the subtle but critical syntax differences between DB2 z/OS and DB2 LUW
  environments. Although the database syntaxes appear similar, their distinct requirements
  necessitate automated transformation handling for schema management, table spaces, and data
  types. This ensures successful migration from mainframe to distributed platforms while
  maintaining operational integrity.

We tested this version of the AWS Blu Age Runtime with the following stack.

|                           |                         |
| ------------------------- | ----------------------- |
| **Component**             | **Version tested**      |
| Java                      | Java 17                 |
| Presentation layer        | Node JS 22.11.0         |
| Npm 10.9.0                |
| Angular 19.1.3            |
| Service layer             | Spring Boot 3.4.6       |
| Spring Core 6.2.2         |
| Spring Session 3.4.1      |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 15.10 |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.40   |

## Runtime release 4.9.0

### zOS

**Improvements**

- COBOL
  - Added support for DATE-TO-YYYYMMDD function
  - Improved support for UNSTRING statement to enhance TALLYING computation
  - Added Support for DFHRESP(NORMAL) value on 88 Level variable
  - Improved bind operations involving COMMAREA, especially on nested program calls
  - Added support for LINE-COUNTER and PAGE-COUNTER special registers
  - Improved support for WRITE...BEFORE statement for Record Sequential file according to machine control characters for channels (C01 to C12)
  - Improved support for READ/WRITE statement involving variable-length-record file
  - Improved support for CALL statement when passing a parameter by reference with a size difference to the sub program
  - Improved support SORT KEY when the structure has 88 level fields
  - Improved support for signed integer value in the DISPLAY statement
  - Improved string concatenation operations performances by reducing computation overhead
  - Improved support for MOD and REM calculation to handle negative values

- PL/I
  - Improved support of SUBSTR function with bit operations

- JCL - IDCAMS
  - Enhanced support for GDG files for the order of copy
  - Added support to override any CLUSTER-level specification when KEYS is defined in the DATA component
  - Added support for ALTER NEWNAME statement
  - Added support for GDG optional keyword for DELETE statements
  - Enhanced condition code handling by ensuring MAXCC overrides persist through control commands (SET, IF-THEN-ELSE) while resetting appropriately before functional commands

- JCL - SORT
  - Improved support for handling of ZD fields with a combination of Packed and Numeric data
  - Improved support for Zoned Decimal Comparison with Character Field in INCLUDE statement
  - Improved support for INREC FINDREP to handle brackets in OUT parameter
  - Improved support for the OMIT statement for ALL and NONE conditions
  - Improved support for the END statement
  - Improved support for order of logical operator precedence for COND phrase
  - Improved support for UNPAIRED in JOINKEYS

- JCL - DSNUTILB
  - Added support for the DOUBLE PRECISION data type
  - Improved support for LOAD DATA with COLDEL keyword and uses of regex-special delimiters
  - Improved support of TEMPLATE for LOAD statement

- JCL - Misc
  - Improved support to truncate Fixed Block Output record based on LRECL
  - Improved file deletion to prevent issues in high availability environments
  - Added support for IKJEFT1B system utility
  - Improved support to maintain record size across a JOB according to previously executed steps
  - Enhanced support for PARM and STEP focused PARM in JCL and PROC
  - Improved support for DCB=\*.DD to be compliant with the Backward Reference used to reference information from a previously defined DD
  - Improved support to make processing procedure variables available in multi-threading context

- <noloc>Blusam</noloc>
  - Improved the read of <noloc>Blusam</noloc> Large KSDS when navigating to next/previous
    records at page or index boundaries
  - Improved the clear and load of large <noloc>Blusam</noloc> files
  - Improved support for the creation of indexes tables for <noloc>Blusam</noloc> Large KSDS
    when optional data set is missing
  - Improved <noloc>Blusam</noloc> write-behind implementation to address issues with delete
    operations, enforce queuing of batch updates
  - Improved performance of <noloc>Blusam</noloc> Large data sets records operations
    (addition and deletion) by using a local indexes caching mechanism reducing delays from
    multiple interactions with remote cache

- SQL
  - Improved support for statement with HAVING and without GROUP BY clause
  - Improved database schemas metadata caching mechanism

- Message Queue Integration
  - Improved support for MQ CLOSE operation when job is executed in multi-threaded approach
  - Improved performance by implementing JMSTemplate reuse for MQ Operations

- MFS
  - Enhanced support for DSCA parameter in MFS DEV statement

- Screen
  - Improved data entry mechanics to prevent entering single-byte characters into double-byte fields, especially when using virtual keyboard e.g. Text Composition System.

- Misc
  - Added more configuration options for the Redis connection pool, such as `connectionPoolSize`, `connectionMinimumIdleSize`, `idleConnectionTimeout`, and `connectTimeout`
  - Enhanced /triggerscript/{scriptId:.+} endpoint to support POST requests with JSON payload, allowing for complex parameter passing in addition to existing query parameters

### AS400

**Improvements**

- RPG
  - Improved the support for `L0` indicator in total calculations
  - Improved the support of TIME opcode through job initialization
  - Improved DaoCycleManager to read primary and secondary files with different number of match fields
  - Improved %EDITCODE 'J' Number Formatting
  - Improved the support of edit code grouping for edit code 4

- COBOL
  - Improved support of REWRITE on dynamic mode when clause WITH DUPLICATE specified on the file RECORD KEY
  - Enable key field update on Dynamic mode with DUPLICATES keyword
  - Improved resource handling on SORT operation

- CL
  - Improved support for `CHKOBJ` command to handle trailing spaces in the object names
  - Improved support for `CHKOBJ` command to check for the existence of a view with a library
  - Improved the parsing of parameter lists for the `SBMJOB` command
  - Improved support for `CLRSVF` command and `MSGMON` to raise code `CPF9812` when the file isn't existing
  - Improved support for `OVRDBF` command to handle `*END` value for parameter `POSITION`
  - Improved support for `*REPLACE` in `CPYF` when source file is empty
  - Improved support for the `CHGVAR` command to handle parameter without VAR optional keyword

- Database access
  - Improved support of DELETE operation for concurrent jobs
  - Improved support of DELETE operation as first operation on a file.
  - Improved data integrity when reading from join files
  - Improved handling of control characters on READ/WRITE operations when flag INSERTNULL is off.
  - Added technical columns SRCFILE and MEMBER in SQL views to provide mechanisms to handle libraries
  - Improved remaining timeout calculation in object locks
  - Improved support of file overriding on JOIN files
  - Added support for Relative Key on Transaction File

- Screen
  - Improved the handling multiple error message for same field
  - Handled display of STATUS messages when sent to external message queue of job
  - Added message line service to dynamically control the display of error messages
  - Improved the resolution of message for additional message screen

- Misc
  - Improved the session tracking mechanism to return properly formatted last update timestamp and creation timestamp
  - Improved consistency in all record collections when updating/deleting records in database
  - Improved the initialization of as400 switches upon job start by introducing a new YML property `job.default.encoding`
    that specifies the default encoding which is used to initialize the job level storage with default = `CP1047`
  - Improved SQL Grammar to accept quote escape sequence
  - Improved support for packed key types for OVRDBF POSITION.

## AWS Blu Age

Transformation Engine 4.9.0

### zOS

**New features**

- SQL
  - Added support of DDL and in-lined queries transformation from DB2 zOS to DB2 LUW

**Improvements**

- COBOL
  - Improved support Level 88 fields with 01 level parent field
  - Improved support for special names `CTL` and the `WRITE .... AFTER CTL` statement
  - Improved fall-through from Paragraph to Section during `PERFORM SECTION`
  - Added support for the `COPY` statement with relative path
  - Added support for `BODY` as a valid COBOL field name
  - Improved support for the `EVALUATE ... WHEN` statement
  - Improved support for the `RECORDING MODE` clause in `SD` file
  - Added support for figurative constants in the `WRITE` statement
  - Added support for S01 TO S05 and C01 TO C12 as valid field names
  - Added support for `PRINTER` as target file for the `SELECT ASSIGN` clause
  - Added support for the REPLACE statement in the `FD` clause
  - Added support for `COPY` in data definition line in the `FD` clause
  - Added support for the `COPY` statement with relative path
  - Enhanced support for the `STRING` statement to support array element as a delimiter, for example, `STRING ABCDEFG DELIMITED BY IDX-1 (SUB) INTO IDX-2 POINTER ID3`.
  - Added Support for `DFHVALUE` value on 88 Level variable for a data structure
  - Improved support for the `FUNCTION LENGTH` statement when the argument is a SUBSTRING expression
  - Added support for the LOCK Close mode
  - Added supported for OF/IN in the START statement
  - Improved support for the JUSTIFIED clause when the RIGHT keyword is not specified
  - Improved support for FD naming to prevent collision for reserved keywords
  - Improved support for Special names with condition clause
  - Added support for DEBUGGING MODE in the SOURCE-COMPUTER configuration
  - Improved support for the IDENTIFICATION DIVISION and DATA WRITTEN optional paragraph
  - Improved safe exit states on declarative sections
  - Added support for invalid key statements for sequential files
  - Improved support for duplicate names from WORKING STORAGE section and LINKAGE section
  - Enhanced support of the SET ADDRESS OF DFHCOMMAREA statement
  - Improved support for COBOL declarative call

- PSB
  - Improved support for the `SENSEG` statement where `PROCOPT` is before `PARENT`

- JCL
  - IDCAMS - Added support for the abbreviations REPL, IMBD, and WCK for REPLICATE, IMBED, and WRITECHECK, respectively

- SQL
  - Improved support for nested table expression

### AS400

**Improvements**

- CL
  - Improved support of field types on CL-to-groovy generation

- DDS
  - DPSF RTNCSRLOC keyword support multiple space separating parameters
  - Improved record format name determination for indexes in SQL-DDS.
  - Improved support for quote escape sequence `''` inside SQL-DDS.

- RPG
  - RPG
    - Improved support of `LEAVE` statement inside a loop rewritten to support GOTO
    - Added support for `%TIMESTAMP` built-in function used in a procedure cal
    - Improved support for F-Spec keyword containing mixed case
    - Improved support for Code controlled by Control level indicators
    - Improved support for halt indicators
    - Improved TAG support with Control Level
    - Improved support for `CLEAR` statement by handling of recurring data in external record layouts
    - Improved support of indicator arrays
    - Improved support of CTDATA array
    - Improved support of Elementary Fixed Array assignment
    - Enhanced support for complex nested function expressions in RPG calculations
    - Enhanced local data area read/write generation with UDS

- SQL
  - Enhanced support for SQL syntax with parentheses in FROM clause.

## Release notes 4.8.0

Release date: April 23, 2025

This release of AWS Blu Age Runtime and Transformation Engines introduces key updates to enhance database transformation capabilities and performance:

- **IBM IMS database transformation** — Added support
  for transforming IBM IMS databases into our JHDB customized Blu Age
  solution.
- **In-memory cache feature** — Added in-memory cache feature that enables users to cache read-only data within memory, improving performance for data-intensive programs.

We tested this version of the AWS Blu Age Runtime with the following stack.

|                           |                         |
| ------------------------- | ----------------------- |
| **Component**             | **Version tested**      |
| Java                      | Java 17                 |
| Presentation layer        | Node JS 22.11.0         |
| Npm 10.9.0                |
| Angular 19.1.3            |
| Service layer             | Spring Boot 3.4.2       |
| Spring Core 6.2.2         |
| Spring Session 3.4.1      |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 15.10 |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17   |

## Runtime release 4.8.0

### zOS

**New features**

- Introduced support for defining custom headers for secured transactions through the YML property
  `gapwalk-application.security.customAllowedHeaders`. This property is related to
  `gapwalk-application.identity` property with value `oauth`.
- Added a feature to allow customers to rebuild <noloc>Blusam</noloc> metadata based
  on the actual records in the <noloc>Blusam</noloc> database table
- Secured JHDB connections using AWS Secrets Manager integration

**Improvements**

- COBOL
  - Improved support for AT END condition on READ file statement
  - Improved support for MOVE signed numeric literals to alphanumeric fields without moving the sign
  - Improved support for the UNSTRING statement to handle non-numeric to numeric field conversions and retain low-values when the delimiter is not found and no value is moved to other variables
  - Improved the address bind operation for dynamic linkage entities
  - Improved string concatenation operations by including support for shift in/out bytes (SOSI)
  - Improved support for the COBOL ACCEPT statement with DAY-OF-WEEK source
  - Added support for SYSIN and SYSOUT as SPECIAL NAMES values
  - Improved support for STRING concatenation to handle the form feed character

- JCL - IDCAMS
  - Added support for deleting gdg generations using a base name without the GDG parameter
  - Improved support for handling the VOLUME parameter as a variant of the standard VOLUMES
    parameter for the DEFINE CLUSTER statement

- JCL - SORT
  - Added support for SYMNAMES with JOINKEYS command

- JCL - IEBGENER
  - Improved support for IEBGENER to handle invalid SYSIN content by introducing validation checks and automatic fallback to ICEGENER, ensuring continuous operation even with incorrect control statements

- JCL - INFUTILB
  - Improved handling of unload INTO and FROM clauses

- JCL - DSNUTILB
  - Added support for DOUBLE PRECISION data type

- JCL - Misc
  - Improved overriding file configurations using DD names in child procedure from the job
  - DSNTIAUL/INFUTILB - Enhanced customization of SYSREC padding bytes for unload utility
  - Added support for OUTDD option for DISPLAY statement redirection
  - Improved support for Fixed Block Sequential File write. When the LRECL in the COBOL program differs from the JCL LRECL, the JCL LRECL takes precedence.
  - Added support for catalog DCB attributes for the SORTOUT file, but only for permanent datasets
  - Enhanced support for conditional JCL step transformation
  - Improved support for ACCEPT with SYSIN and lines exceeding target size with trailing spaces
  - Improved support for SET statements to handle command not including variable name, command defined inside includes a member file that should be accessible within the JCL and command contains inline comments
  - Added support to retain the job level 'scriptContext' parameters in the JCL checkpoint metadata and the job context for use at restart

- <noloc>Blusam</noloc>
  - Improved record insertion on <noloc>Blusam</noloc> large indexed data sets when
    writing after loading an empty data set
  - Improved performance for large data sets by enabling a warm-up mechanism and introducing an optional prefetch window for records, as well as local storage for indexes and pages
  - Improved support for Export Data Set to handle a larger dataset with AWS Key Management Service

- SQL
  - Improved support for JDBC BLOB data type

- Message Queue Integration
  - Added support for User Identifier on MQ PUT command when XA is activated
  - Added support for concurrent MQ connections when XA is activated

- IMS
  - Added a YML property `jhdb.keepParent` to control whether IMS ISRT calls populate \_parent and \_logicalparent fields in the database when set to true
  - Improved robustness by removing message queue for invalid transaction code

### AS400

**New features**

- Added in-memory cache feature that enables users to cache read-only data within memory, improving performance for data-intensive programs.

**Improvements**

- CL
  - Improved support of QRYSLT parameter in OPNQRYF command to handle RANGE keyword, to parse value when string columns have purely numeric values and to handle empty string values
  - Added support for FTP SENDPASV command
  - Improved support for query formation in command DSPDBR executed using Qcmdexc
  - Improved the support of MONMSG exception to propagate it properly in the execution stack
  - Improved record copying between tables with varying column counts and data types on CPYF
  - Improved message monitoring priority: command-level messages now correctly take precedence over procedure-level ones
  - Improved support for CPYF command to consider the library defined by BLU4IVLIB
  - Improved support of MonMsgs in command CHKOBJ to handle the case when file doesn't exist in library

- Screen
  - Improved handling of BigDecimal values with more than 15 digits by building the value manually and then turning it into a number to be displayed rather than letting the Number be rounded

- Misc
  - Improved support for UserSpace with Replace as NO when UserSpace already exists
  - Enhanced BLU4IVLIB functionality to support both retrieval and writing of records to overridden libraries
  - Improved support for multi-dimensional array fields using DIM and OCCURS operations
  - Enhanced support for low-values passed as key field values in DAO operation
  - Removed conflict on MONMSG instruction for messages that can be handled by a local and a global monitor
  - Improved setting FileStatus on Duplicate Record Insert
  - Reduced userspace lock conflict and reduced creation failure risk by using registry first to check if userspace exists
  - Improved support for readPriorEqual() skipping records after delete()
  - Improved records locking mechanism under commitment control
  - Improved handling of RPG statement RETURN in subroutines
  - Improved the support of user info in SharedContext

## AWS Blu Age

Transformation Engine 4.8.0

### zOS

**Improvements**

- COBOL
  - Improved Printer mode generation for multiple files.
  - Improved support for SPECIAL-NAMES to handle optional end-dot and multiple dots.
  - Improved support of COPY with relative path /REPLACE OFF/COPY-REPLACING statements.
  - Added support for COL as valid field name.
  - Improved parsing to handle spaces after SPECIAL-NAMES, X-COMPUTER and DECLARATIVES.
  - Added support for S01 to S05 and C01 to C12 as valid paragraph names.
  - Added support for LENG function as alias of LENGTH function.
  - Improved Copybooks parsing when cobolMaxCodeWidth configuration value differs from their COBOL includer
  - Improved support for parsing expression with comma and operation e.g. MIN(A \* B, (3 + 1) / 2, 3 + 4).
  - Added support for IS INITIAL PROGRAM in PROGRAM ID clause.
  - Added support for Level 88 condition on SEARCH ALL statement.
  - Added support for REPORT SECTION.

- SQL
  - Added support for DDL transformation from IBM IMS database.

### AS400

**Improvements**

- CL
  - Enhanced support of CL by setting the transformation to JAVA as the default support
  - Improved the transformation to groovy script by adding the use of a metamodel
  - Added keywords CONTINUE and FOR to list of reserved keywords

- DDS
  - Improved support of DSPF fields defined relatively to the prior one
  - Improved support for DDS character field with keyword VARLEN
  - Improved transformation/generation of LF entity DAOs by generating the explicit setting of renamed fields in the convert and updateJPAFromVo methods.

- RPG
  - Improved support of PREFIX keyword parameter to handle cases where values don't have quotes
  - Improved handling of nested method calls in array indices

- COBOL400
  - Improved the generation of record entities imported from a DSPF with directive COPY DDS-ALL-FORMATS

- SQL
  - Improved the transformation of SQL WHERE clauses with non-enclosed OR conditions.

## Release notes 4.7.0

Release date: March 12, 2025

This release of AWS Blu Age Runtime and Transformation Engines introduces key updates to core dependencies:
AWS Blu Age Runtime has been upgraded to use the latest Spring Boot version 3.4.2, and modernized frontend
applications now utilize the latest Angular version 19.

We've tested this version of the AWS Blu Age Runtime with the following stack. Other versions might also
be compatible.

|                      |                           |
| -------------------- | ------------------------- |
| **Component**        | **Version tested**        |
| Java                 | Java 17                   |
| Presentation layer   | Node JS 22.11.0           |
| Npm 10.9.0           |
| Angular 19.1.3       |
| Service layer        | Spring Boot 3.4.2         |
| Spring Core 6.2.2    |
| Spring Session 3.4.1 |
| Persistence layer    | Spring statemachine 4.0.0 |
| PostgreSQL engine 14 |
| Oracle 21c           |
| Application server   | Apache Tomcat 10.1.17     |

## Runtime release 4.7.0

### zOS

**New features**

- Added new YML property `dataSimplifier.doubleFloatingType` to define which format to use when encoding and decoding the floating-point numbers - Allowed values are `IEEE_754` (default) / `HFP` (for Hexadecimal Floating-Point format)
- Added support of decimal scaling position P on the numeric PICTURE

**Improvements**

- COBOL
  - Improved support for INSPECT statement with AFTER INITIAL and BEFORE INITIAL clauses
  - Upgraded Numeric Edited Type support with optimized byte conversion enhancing overall data handling efficiency
  - Added support for FUNCTION MIN & MAX with alphanumeric comparison
  - Improved support for FUNCTION INTEGER for negative values

- PL/I
  - Enhanced support of the PUT statement with FBA/VBA SYSPRINT dataset

- JCL - SORT
  - Added support of the OUTREC option SQZ with the subparameters SHIFT, LEAD, TRAIL, MID, PREBLANK, and PAIR
  - Enhanced cataloging DCB attributes for the SORTOUT file

- JCL - DSNUTILB
  - Enhanced support for DECIMAL EXTERNAL data type
  - Improved support for the NULLIF condition related to another column's values/position
  - Improved support for BYTEA columns

- JCL - INFUTILB
  - Improved support for keywords CURRENT [DATE/TIME/TIMESTAMP] in UNLOAD operation

- JCL - Improved support for qualified return code of called PROCs
- Data Processing
  - Enhanced numeric comparison logic when processing blank-valued fields redefined from alphanumeric to numeric types, ensuring correct evaluation against zero

- <noloc>Blusam</noloc>
  - Improved support for START command to handle partial key searches using segments of the primary key, providing more flexible record retrieval capabilities

- SQL
  - Added support for input parameter passed in ON clause
  - Added support for REPEAT function
  - Improved support for UPDATE statement with an assignment involving column name
  - Improved SQLCODE and SQLSTATE handling in multi-row cursor fetches
  - Added support for DB2 XML function for DB2 database target

- Message Queue Integration
  - Enhanced error handling in MQ GET operations, providing clearer status indication MQCC_FAILED for empty message bodies
  - Enhanced support for MQ PUT operations by handling MQRFH2 header in XA transaction context
  - Improved support for AWS Blu AgeRuntime secrets to handle
    additional properties for JMS MQ
  - Enhanced JMS MQ connection pool configuration capacity

- Misc
  - System Integration - Added support for the schema environment in DFSRRC00 program calls
  - Added compatibility for IMS transaction when <noloc>Blusam</noloc> is
    disabled
  - Improved support for end-of-file condition on a sequential file to align to legacy rule 'EOF is considered an unsuccessful read'

### AS400

**New features**

- Added support for RUNSQLSTM command to execute SQL queries stored in an external source file

**Improvements**

- CL
  - Added file locking mechanism through the ALCOBJ/DLCOBJ commands
  - Improved the CPYF command functionality to maintain record sequence integrity during file copying
  - Improved CPYF command to support output as a flat file
  - Enhanced parameter handling to automatically adjust data length during program calls
  - Improved parameter support to handle range reference
  - Added support for MONMSG CPF2105 on DLTDTAARA command
  - Added support of the QTEMP library for command CHKOBJ on DATAAREA
  - Enhanced support for the ADDLFM command, improving logical file member management capabilities
  - Added support for generic data area names on DLTDTAARA command
  - Added support to SBMJOB to handle passing switches via SWS parameter
  - Improved the data area writing logic by putting the read and write calls into a synchronized block
  - Enhanced data area concurrency management to prevent simultaneous writes through the implementation of a granular locking mechanism, eliminating errors during parallel operations
  - Added support for keyword \*ALL in DTAARA parameter for RTVDTAARA command

- Screen
  - Improved the color of a white attribute in the front end

- RPG
  - Improved support for TESTB operation to better handle different encodings
  - Improved support for EDITC operation with edit code 'Y' and 'P'
  - Improved support for EDITCODE for codes K, Q and Z
  - Implement support for Prototype ExtProc keyword support on local procedure with parameters
  - Handled parameters passed by value for external procedures

- COBOL
  - Improved SORT statement to handle targeted library
  - Truncated a partition when the associated DAO is opened in OUTPUT mode
  - Added support for PREFIX keyword

- DataQueue
  - Added keystore and truststore configuration options for RabbitMQ data and hybrid message queues, enabling secure messaging in production deployments
  - Optimized server restart performance by eliminating redundant data queue existence check
  - Streamlined architecture by removing DataQueueRegistry and DataQueueConnectionProvider components
  - Simplified data queue deletion through direct handling without registry validation
  - Improved queue creation process by ensuring proper exchange creation and queue-to-exchange binding

- Misc
  - Added transaction request size validation to prevent system overload related to excessive range requests
  - Improved lock management on job resource cleaning
  - Improved the DAO locking mechanism to prevent locking a record when the file is opened in INPUT mode
  - Optimized performance for dynamic entities mapping
  - Improved handling of JPA persistence context to enhance performance on DAO operations
  - Improved data area support by adding timestamp columns to handle record metadata
  - Improved data area reliability by implementing synchronized read-write operations to prevent concurrent access issues
  - Improved support for DateHelper#moveDate to support date-to-timestamp conversions

- DDS
  - Improved support of Select/Omit conditions combined with synthetic operation such as SST or CONCAT

- SQL
  - Optimized the SQLExecutorBuilder to handle partial record fetching more efficiently, particularly when retrieving multiple rows with fetch limits exceeding one

## AWS Blu AgeTransformation Engine 4.7.0

### zOS

**Improvements**

- COBOL
  - Added support for CODE-SET statement
  - Added support for option NOT END OF PAGE from WRITE statement
  - Added support for a new syntax on ALTER
  - Added support of multiple line replacement for COPY REPLACING statement
  - Improved parsing of CHARACTERS keyword implied at different clause definition
  - Improved support for alternate keys involved in input-output section when the key's names are duplicated but have different parents
  - Improved support for IF condition with comparison of large fields against spaces
  - Improved logical file reference static resolution by making it case insensitive
  - Enhanced code transformation to automatically generate LINAGE-COUNTER implicit fields for each FD entry that contains a LINAGE clause
  - Improved support for IDCAMS Cluster definition with a name enclosed by simple quotes
  - Improved support of PERFORM statement for Basic format, with TIMES phrase format and format involving section's qualification
  - Enabled the transformation of SORT statement with multiple GIVING files and added an exception to track this case on execution
  - Improved the transformation of RENAMES when specified on a group using the REDEFINES clause

- PL/1
  - Added Support for option DATA or LIST for PUT STRING
  - Added support for Multiple Entry program support

### AS400

**Improvements**

- CL
  - Improved the parsing of parameters for QCMDEXC to be able to execute ALCOBJ/DLCOBJ through QCMDEXC
  - Added support for ElseIf statement on CL
  - Added support for builtin function %SWITCH to set the job switches.

- DDS
  - Improved support of program-described DSPF record to handle dummy record in input specifications
  - Improved the DAO generation WHERE clause conditions in the case of an CREATE INDEX SQLDDS file

- RPG
  - Added support for ZEROES initialization INZ(\*ZEROS) on Unsigned Integer
  - Improved support of command EXCEPT with a file type of Workstation and SQL Index
  - Improved support of RPG internal data type for numeric fields defined externally
  - Improved support of built-in %ERROR to get the current error status after an operation on a file
  - Improved support of COMMIT file keyword to handle multi-format logical file
  - Enhanced SELECT/OMIT processing for multi-format logical files
  - Improved handling MOVEA for setting array with blanks, moving Fixed arrays of Packed, Zoned and Binary to another array of the same type.
  - Improved array handling for Z-ADD \*ZEROS and MOVEA \*ZEROS
  - Improved MOVE/MOVEL operations when moving from numeric and character combinations
  - Implement support for RPGLE Prototype ExtProc keyword support on local procedure with parameters
  - Improved handling of \*HIVAL figurative constant in assignment statements
  - Improved the support for PREFIX keyword to handle character replacement

- COBOL400
  - Improved support for REWRITE and UPDATE operation on Dynamic access mode
  - Added support for ACCEPT Statement FOR clause in CBLLE
  - Improved support of built-in %STATUS to get the current status of a file after an operation

- Misc
  - Improved transformation of programs which define data structures that share the same name as one of the fields in the specified PF/LF
  - Improved array access generation on kanji variables

## Release notes 4.6.0

Release date: January 24, 2025

We've tested this version of the AWS Blu Age Runtime with the following stack. Other versions might also
be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 22.11.0       |
| Npm 10.9.0                |
| Angular 18                |
| Service layer             | Spring Boot 3.3.5     |
| Spring Core 6.1.14        |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

## Runtime release 4.6.0

### zOS

**Improvements**

- COBOL
  - Enhanced `WRITE ADVANCING` capabilities with improved accuracy
    for sequential file line writing, supporting
    multiple contexts (`BEFORE`>, `AFTER`, and Implicit uses)
    and full `PAGE` statement implementation
  - Enhanced support for `FILLER` for cases when a nested table FILLER is used as a group
    with a table as child
  - Improved access to child of ambiguous parents inside one segment
  - Added support for Numeric Edited type with picture='-----'
  - Improved display handling of BINARY type data

- PL/I
  - Improved conversion of binary literal values in assignment statements

- JCL — SORT
  - Improved support for consecutive `OVERLAY` parameters in the same
    `OUTFIL` statement

- JCL — DSNUTILB
  - Optimized loading mechanisms, resulting in 25% faster data retrieval times
  - Enhanced support for XA transactions for external business data-sources

- JCL — INFUTILB
  - UNLOAD - Added support of FLOAT8 data type

- JCL — IDCAMS
  - Optimized handling of return codes for `IDCAMS` commands
  - Added support to delete all GDG generations based on GDG base name
  - Added support for files deletion without `NONVSAM` parameter

- JCL — Misc
  - Enhanced Batch Restart Metadata handling to improve workflow status management during
    restart mode

- <noloc>Blusam</noloc>
  - Added support of TTL for <noloc>Blusam</noloc> cache in both Ehcache and Redis
    implementations
  - Improved support for `DEPENDING ON` field on COBOL File Description
    `FD` for <noloc>Blusam</noloc> KSDS file
  - Enhanced thread safety in Redis <noloc>Blusam</noloc> read operations for
    simultaneous multi-job execution
  - Improved <noloc>Blusam</noloc> schema creation for better robustness regarding
    database user privileges
  - Improved padding to the right on variable block concatenated input dataset `READ`

- BAC
  - Added support for dataset creation in Multi-schema mode, including a new "Schema"
    column to indicate schema association for each dataset

- MFS
  - Improved propagation of user info from Front-end to shared context, ensuring proper
    propagation to JHDB context
  - Added support for IBM MQ IMS information header on XA transactions

- SQL
  - Enhanced `SQLCODE` handling to set 305 during cursor fetch when all column values are
    NULL
  - Added support for `IN` clause involving `OCCURS` parameter
    for `WHERE` conditions
  - Added support for `DECLARE GLOBAL` temporary table statements
  - Extended DB2 SQL support for midnight 24H DB2 specific timestamp format thru dedicated
    conversions at execution according targeted database engine

- Misc
  - Enhanced IBM930 charset to allow both Unicode characters U+2014 and U+2015 to
    correspond to x'44x4A' in EBCDIC
  - TDQUEUE - Refactored SQS implementation to support multi-threading
  - Improved GDG dataset name resolution to allow customer to archive files with the same
    GDG prefix (e.g. `A.B.C.G0002V00` is current file and
    `A.B.C.G0001V00.1236` is an archive file)
  - Enhanced `SQLConverter::toPgmDate/Time/Timestamp` to align the date computation according
    to the legacy format

### AS400

**New features**

- Added support for dynamically created AS400 tables for flat files and duplicated
  entities, enabling access to tables created via CL commands like CRTPF, CRTDUPOBJ, and
  CPYF
- Added a service to support library list through a registry that handles the default
  library for every tables

**Improvements**

- CL
  - CLRPFM - Improved handling of member when the command is called for QTEMP
    library
  - SMBJOB - Improved support of parameter `PARM` to handle dynamically built argument
  - CPYFRMIMPF - Added support for parameter `TIMFMT`, `ERRRCDFILE`,
    and `ERRRCDOPT`
  - CPYFRMIMPF - Improved support of database alphanumeric values that contain single
    quotes
  - CPYF - Refined the command query construction for multi-member `FROM` files with
    `TOMBR(*ALL)`
  - CPYF - Enhanced support to handle `FMTOPT` parameter for `MAP DROP`
  - CPYTOIMPF - Improved support of parameter `FROMFILE` to handle `MEMBER` of the
    table
  - RTVUSRPRF - Added support for parameter `RTNUSRPRF`
  - DSPDBR - Overhaul the command to match expected legacy behavior of printing out
    information about views the exist on a table, as well as the library and member they're a
    part of
  - DSPFD - Improved support of parameter `FILE`
  - DSPFD - Improved support of parameter `TYPE MBR` output to include additional values:
    mbfile, mblib, mbfcdt, mfccn

- Screen
  - Improved cursor position priority for `DSPATR(PC)`
  - Improved the validation of subfile record fields by ignoring the front-end validation
    of “protected” fields
  - Improved support for initializing records in workstation with multiple array fields
    sharing component names
  - Enhanced support for response indicators in `DSPF` keywords
    (`SFLMSG`, `SFLMSGID`, `CHANGE` and
    command keys)

- RPG
  - Enhanced program cycle support for a better handling of the fields read from
    primary/secondary files
  - Added support for Split Control Field for primary/secondary files reading
  - Enhanced `%SUBST` built-in method to handle double-byte fields in compare
    statements
  - Improved support of ZERO indicator for MVR operation

- DDS
  - Added support of multi-format logical files with record format that refer to the same
    physical record

- DataQueue
  - Improved job interruption handling for jobs waiting on data queue messages by cleaning
    up the consumer during interrupts
  - Migrated from RabbitMQ to Spring-AMQP for better channel management and thread
    scaling

- Misc
  - Improved SQLExecutorBuilder to support queries with multiple white spaces and open
    braces without leading spaces
  - Improved DAO support to handle correctly the cursor positioning while changing the
    reading direction
  - Refined key initialization after retrieve and delete operations to ensure proper
    removal of related records before inserting updated records
  - Optimized DAO mapper generated code to improve time execution performances

## AWS Blu Age Transformation Engine 4.6.0

### zOS

**Improvements**

- COBOL
  - Improved parsing of `RESERVE` clause with optional `AREA/AREAS`
    literal
  - Enhanced COBOL support with optional `DATA DIVISION` declaration,
    supporting streamlined test cases
  - Improved special names paragraph by adding support for `ALPHABET`,
    `SYMBOLIC`, and `CLASS` clauses, switches, and `FORMFEED`
    variable
  - Added support for `SYSIN` as a Mnemonic Name in `ACCEPT`
    statements
  - Enhanced `PICTURE` clause support for "$", "0", "CR", "DB" symbols in
    `PIC` logical size calculations
  - Improved `USE` statement transformation for multiple file scenarios
  - Enhanced `ALTER` statement transformation for multiple alterations
  - Added support for figurative constants `ZERO`
    `HIGH-VALUE`
    `LOW-VALUES` in `delimited by` clause

- SQL
  - Improved transformation of default value for postgreSQL target to
    handle quotes around the `CURRENT_TIMESTAMP` default value
  - Handle `WITH CHECK OPTION` clause of SQL views

### AS400

**Improvements**

- DDS
  - Improved support of multi-format logical files that refer to the same physical record
    multiple times

- RPG
  - Enhanced `MOVE` and `MOVEL` operations to better handle padding
    zeros
  - Enhanced handling of nested function calls in evaluations and conditions

- COBOL400
  - Added support for transforming the `IN` keyword in `SELECT`
    statements
  - Improved support for missing dots in data description entries, aligning with the
    latest COBOL version where dots are assumed when missing
  - Enhanced cursor positioning on `REWRITE` operations
  - Enhanced support for `START` statement to lock the record at current file
    position
  - Improved support for compiler directive `COPY DDS` to generate all
    input/output data structure

- Misc
  - StateMachines - Improved transformation to enhance composite states declaration in
    alignment with stateless4j paradigm
  - Improved sanitization for LF files containing special characters
  - Improved support of figurative `*ALL` with hexadecimal values
  - Improved `MOVE` operation support for implicit conversion from numeric to character
    types
  - Optimized report bean generation to sort by associated printer name, preventing
    duplicate or conflicting names
  - Improved support of keyword `EXTFILE` combined with `USROPN` to handle literal value and
    format `libname/filename`

## Release notes 4.5.0

Release date: December 20, 2024

This release of AWS Blu Age Runtime and AWS Blu Age Transformation Engines includes the following key
features.

- **JCL support** — It is now possible to generate and
  execute JCL scripts on the fly within the runtime context. This feature adds flexibility and
  automation in batch job processing. We've updated the support for JCL utilities in the runtime,
  with a set of improvements to SORT, ICETOOL, INFUTILB, and IDCAMS (see details in the following
  sections). These enhancements offer more robust and efficient data processing
  capabilities.
- **Binding Directories and Activation Groups Support for AS/400
  Modernized Applications** — Binding Directories enhance system organization by
  managing exported procedure references, while Activation Groups streamline execution context
  management. These features improve precision and reliability, robust resource management, and
  optimized system interactions. The result is a more resilient, organized, and efficient system
  for modernized AS400 applications.
- **Dependencies updates:** — Update of all frontend
  frameworks (BAC/JAC & modernized applications) to the long-term support (LTS) versions. The
  update of Angular from v17 to v18 introduces a new reactivity model and streamlined state
  management, reducing complexity and improving application maintenance for developers. Node.JS
  has also been updated from v20 to v22.

We've tested this version of the AWS Blu Age Runtime with the following stack. Other versions might also
be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 22.11.0       |
| Npm 10.9.0                |
| Angular 18                |
| Service layer             | Spring Boot 3.3.5     |
| Spring Core 6.1.14        |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

## Runtime release 4.5.0

### zOS

**New features**

- JCL — Added ability to invoke a batch job from online programs. We added a service
  to handle JCL script stored in a dedicated TDQueue when a modernized program generates it on
  the fly. This service makes it possible to reconstruct the JCL message, refactors this message
  into a groovy script, and runs this groovy script.
- ADABAS — Added support for ADABAS program. With this support, the runtime emulates
  the ADABAS commands for database access (available for Oracle only).

**Improvements**

- COBOL
  - Enhanced support of DISPLAY statement leveraging the NO ADVANCING option
  - Increased accuracy in management of currency signs allowing the user to benefit from a
    more accurate transformed COBOL structure
  - Improved support for value assignment when moving an unsigned field to a signed field
    and vice versa
  - Improved support for block size for GDG files and concatenated files

- CICS
  - Added support for OpenStatus and EnableStatus of <noloc>Blusam</noloc>
    datasets
  - Added support for the `SET DATASET` command

- JCL — SORT
  - Improved handling of data set record size
  - Improved support for the `OUTFIL` statement to produce output files
    containing only the records from the input files according values specified in STARTREC and
    `ENDREC` options
  - Enhanced support of `OVERLAY` statements
  - Improved support for the `OUTREC` statement to handle a variant of the
    `EDIT` option. We now support `EDIT(...)` in addition to
    `EDIT=(...)`
  - Added support for the pattern(p,m,f,OPERATOR,p2,m2,f2) in arithmetical
    operations
  - You can use the `DUMMY` file clause of the `SORT` program from a
    JCL to handle empty input files and benefit from empty file generation

- JCL — ICETOOL
  - Enhanced support for the `SORT FIELDS=COPY` statement through the
    `SORT` program

- JCL — INFUTILB
  - Improved support for record size computing if it is not specified in the JCL and the
    property DFSIGDCB is disabled
  - Improved UNLOAD with INTO clause for DECIMAL by updating the precision and scale
    according to the into clause fields
  - Improved format method in VarcharFormatter
  - Enhanced support with a new configurable option that allows users to control how
    VARCHAR fields are handled during data unloading as regards as padding behavior ensuring
    flexibility and accuracy in data extraction processes.

- JCL — IDCAMS
  - Improved deletion for file with wildcard suffix and name defined either directly either
    enclosed by parenthesis or by simple quotes
  - Improved accuracy to leverage MAXCC return code

- JCL — IKJEFT01 - Added feature flag `systin.encoding` (default =
  `ASCII`) to support specific encoding for SYSTSIN file dataset
- JCL — Improved support for BDW property for a generated output file in a JCL step
  and subsequent steps use the same file system as input and `DISP=PASS`
- MF
  - Improved support for 2-byte header for Record Sequential file
  - Improved handling of return codes for the DELETE command
  - Improved Write Advancing Line for Record Sequential file

- Redis
  - Improved Redis template initialization for JCL checkpoints and Jics TSQueues
  - Improved Redis dataset record lock information accessibility and readability

- SQL
  - Improved parsing of FOREIGN KEY with REFERENCES clause
  - Provided an extendable caching feature to store original legacy graphic types in the
    database, enhancing data traceability and facilitate graphic compute
  - Enhanced parsing support of CASE WHEN pattern of SQL queries across runtime
    utilities
  - Improved SQL Postgres Blu Age built-in function gwdecimal the runtime relies on to fit
    with DECIMAL DB2 built-in function.

- Misc
  - Enhanced support of NumericEditedType using SIGN operand
  - Improved primary datasource configuration generation in SpringBootLauncher in the
    modernized application
  - Enhanced flexibility to segregate application logs from path related to the called
    job.
  - Improved support for Blank value in comparing fields from NumberUtils

- FILE — Improved support of variable blocks data sets in the underlying
  files
- MQ — Improved MQ connection management for high availability environment
  ready
- Improved MQ Queue compatibility by adding support for non-JMS clients to enhance encoding
  and character set handling
- Improved support for ANSI Control characters for Ebcdic file

### AS400

**New features**

- Added support for Exported Data within Bound Programs
- Added ILE specific support for the division by zero

**Improvements**

- COBOL400
  - Improved support of EOF in File Status
  - Increase the precision support of Cobol START statement to support EQUAL keyword into
    KEY IS clause

- CL
  - Added support for command UPDENVPARM
  - CRTPF - Added support for table accessed with a partition
  - RCVF - Improved support of logical files with override
  - FTP - Improved support of logical I/O files with OVRDBF and enhanced OUTPUT log and
    added support for I/O files in the working directory
  - CPYFRMIMPF - Added support for parameters `ERRRCDFILE`, `TIMFMT`,
    `ERRRCDOPT`
  - CPYF - Improved QTEMP partition creation
  - CPYF - Added monitoring message when the \*FROM file is empty
  - OVRPRTF - Added support for new parameters: `PAGESIZE`, `OUTQ`,
    `DEV`, `LIP`, `CPI`, `OVRFLOW`,
    `LVLCHK`, `FORMTYPE`, `HOLD`
  - Increased accuracy when using the `FMTOPT` parameter with `MAP`
    _and_
    `DROP` options in the `CPYF` command to allow copying data from a
    source file with extra columns to a target file
  - Increased accuracy in managing the mapping of file system path wildcard patterns in the
    `RMVLNK` command
  - The `RMVM` (Remove Virtual Machine) command has been enhanced to handle
    `DROP` partition tables ensuring complete cleanup of related resources.
  - OPNQRYF - Improved support of parameter \*FILE for command
  - Implemented CPF0000 handling to encompass all CPFx messages
  - CHGDTAARA - Added support for \*ALL keyword to change the entire data area

- Screen
  - Improved tables/subfile displaying by increasing accuracy for scrolling and
    position/priority of cursor
  - Improved `CHECK(RZ)` and `CHECK(RB)` functionality for
    non-numeric and non-signed fields
  - Improved support of help screen feature for keyword `HLPARA`

- RPG
  - Improved support of built-in `%SubDt`
  - Improved support for procedure using a local data structure which is
    externally-described
  - Added support for optional error code parameter `QMHSNDPM`, `QMHRMVPM` , and `QMHRCVPM`
  - Enhanced support of `%SUBST` built-in method to better handle double bytes
    fields.
  - Added support for built-in %TLOOKUP and its variants (%TLOOKUPGE, %TLOOKUPGT,
    %TLOOKUPLE, %TLOOKUPLT)

- Dataarea
  - Improved support for OUT operation when factor1 is blank
  - Improved concurrent reads on the same data area
  - Added configuration variable `blu4iv.dtaara.library.disable` to disable
    libraries for data area
  - Extended support to leverage named libraries thru data area operations enabling user to
    structure data area location as he wish.

- DataQueue
  - Improved RabbitMQ channel usage
  - Improved RabbitMQ Consumer to only attempt to cancel the consumer once
  - Improved data queue retrieve from RabbitMQ by only attempting basicGet when wait time
    is 0

- Misc
  - User Space - Improved behavior when multiple jobs attempt to retrieve the same
    userspace simultaneously
  - Improved support of uncommitted record deletion under commitment control
  - Entity - Improved support for consecutive omits as OMIT carries implicit
    `AND` meaning
  - Added support for camel case in entities mappers setters to handle customs named
    defined through additional refactoring
  - Improved propagation of user information from AS400 environment transactions thru whole
    application.
  - Improved accuracy when ending a job scheduled by Quartz in case of interruption
    case.
  - Improved Commitment Control support to make it program-scope

## AWS Blu Age Transformation Engine 4.5.0

### zOS

**Improvements**

- JCL - Improved groovy generation for KSDS dataset based on LISTCAT parsing
- COBOL
  - Improved parsing of `COPY-REPLACING` statement to handle replacement of
    qualified subfield when ambiguity for this subfield name is present
  - Improved support for `SYSOUT` defined in `SPECIAL-NAMES`
    statement
  - Improved support of figurative ZEROES in `ADD n TO ZERO` statement
  - Improved support for `REPLACE` statement to handle multi-line issue by
    flattening multi-line keys and text blocks
  - Improved support for arithmetic operations ADD/SUBTRACT/MULTIPLY/DIVIDE with
    `GIVING` clause
  - Initiated parsing support of REPORT SECTION and its related actions (INITIATE,
    TERMINATE, GENERATE report)

- Misc - Improve weather report generation and robustness

### AS400

**Improvements**

- DDS
  - Improved support of implicit length of type DATE
  - Improved support of stop-zero-suppression character on keyword EDITWORD
  - Improved support of column name DESC as it is a reserved word in DB

- RPG
  - Improved support of built-in %TIME
  - Improved generation of EVALR statements to handle assignment from a string value to a
    variable of shorter length with a better right-adjustement
  - Enhanced SQL parsing around options setting
  - Improved support for PSDS initialization in NOMAIN RPGLE programs
  - Improved support of keyword LIKE to define a DDS numeric field as Packed, no matter
    its external description
  - Improved file name sanitizing by replacing “$” by “DL”
  - Improved support of built-in %SUBST to handle double byte values

- COBOL400
  - Screen - Improved support of DSPF record around I/O operations

- CL
  - Improved renaming of reserved variable names
  - Improved support of Select/Omits conditions to handle multiple formats file

- Misc
  - Reduced duplicated entities around file operations (EOF, FOUND, EQUAL)
  - Improved generation of JRXML files for QPRINT, a standard printer on AS/400. When it
    is used, the created JSON file will not contain any reference to the program or the file.
    Only one JRXML file is generated (QPRINT-QPRINT.jrxml)
  - Improved the display of additional message information for components displaying
    messages from program queue

## Release notes 4.4.0

Release date: November 13, 2024

This release of AWS Blu Age Runtime and Transformation Engines focuses on upgrading critical dependencies
and supported technologies while boosting performance in multiple functionalities. Some key
features and changes in this release include:

- **Dependencies updates**: Console applications (BAC and JAC),
  and modernized applications are now running on Bootstrap 5. The AWS Blu Age Runtime is now powered by Spring
  Boot 3.3.5 framework.
- **Performance**: Improved the performance of the state
  machines execution (up to 10x faster), thanks to a new implementation that overcomes a
  performance degradation after upgrading the Spring State Machine library from version 2.5.1 to
  4.0.0. This upgrade was not optional as 2.5.1 version was no more maintained and contains
  Critical and High CVEs. It includes a runtime state machine implementation on the platform to a
  new library, with a lightweight and efficient state machine implementation, free of CVE, and
  with better overall performance.
- **Simplification of database access**: Completed a
  significant overhaul of the components used to access the database, including DAOs, JPA
  entities, DDS DataSimplifier entities, and Mappers. This redesign was driven by the need to
  provide better support for the OVRDBF (Override Database File) feature common in AS400
  projects. It allows to handle more cases with a simplified architecture for the generated
  code.

We tested this version of the AWS Blu Age Runtime with the following stack. Other component versions might
also be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 18.18         |
| Npm 9.8                   |
| Angular 17                |
| Service layer             | Spring Boot 3.3.5     |
| Spring Core 6.1.14        |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

For more information about the changes included in this release, see the following
sections.

## Runtime release 4.4.0

### zOS

**New features**

- COBOL - Added support for JSON GENERATE statement
- COBOL - Added support for control blocks
- MF - Added support for FCDREG compiler directive
- <noloc>Blusam</noloc> - Added feature VSAM file-sets with an implementation based
  on database schema - Only PostgresSQL supported
- <noloc>Blusam</noloc> - Added support for handling TTL (Time to live) for
  <noloc>Blusam</noloc> cached data items (Redis cache engine)
- JCL - IDCAMS - Added new property `idcams.encoding.forced` to force charset
  used to decode SYSIN card
- JICS - Extended the `jics.db.dataScriptLocation` property from
  `application-main.yml` to accept a list of file and folder paths. The
  order of the list matters. The first SQL file is executed first and so on. When a folder is
  executed, the SQL scripts it contains are executed in no definite order.
- Added support of CEE3ABD utility

**Improvements**

- <noloc>Blusam</noloc> - Improved loading time and memory footprint from legacy
  large data sets to <noloc>Blusam</noloc> for customers using PostgreSQL engine (we
  observed up to an 8-fold increase in loading speed for large data sets)
- <noloc>Blusam</noloc> - Improved exportDataSetToS3 API with Credentials
  Support
- <noloc>Blusam</noloc> - Improved LISTCAT uploading files for data sets
  creation
- <noloc>Blusam</noloc> - Improved support for Dynamic READ using explicit KEY
- <noloc>Blusam</noloc> - Improved the write-behind mechanism logic
- JCL - Enhanced JES support to improve file locking in parallel execution
- JCL - Added support for statement `INCLUDE MEMBER`
- JCL - DNSUTILB - Improved support for duplicate key to handle special case when primary
  key contains spaces
- JCL - DSNUTILB - Improved LoadTask to optimize performance when loading GRAPHIC
  data
- JCL - INFUTILB - Added support for `fetchsize` when `chunksize`is
  not defined
- JCL - INFUTILB - Improved support to query returning empty resultset
- JCL - INFUTILB - Improved robustness when processing data in CHUNK
- JCL - INFUTILB - Improved support for unload with nullable field
- JCL - INFUTILB - Improved support for numeric type
- JCL - INFUTILB - Improved unload for Nullable Field
- JCL - SORT - Improved support for OUTREC syntax
- JCL - SORT - Improved parsing of statement DATE1
- JCL - SORT - Improved support of clause INREC PARSE with RDW
- JCL - SORT - Improved fields formatting using editing masks
- JCL - SORT - Improved support of 'SubString' in OUTREC
- JCL - SORT - Improved support for MF compatible CARD
- JCL - UNLOAD - Improved support of field size with Postgresql
- JCL - IDCAMS - Improved performance for File Loading VSAM data set by introducing bulk
  mode
- PL/1 - Enhances support for NumericEditedType formatting to prevent scale
  discrepancies
- IMS - Improved support for IMS Database \_right column in NodeSorter
- CICS - Improved command `RECEIVE MAP` with `SET` and no
  `INTO`
- BMS - Improved support of field initial value
- SQL - Improved DateTimeFormat parsing for `ddMMMyy` pattern
- COBOL - Improved support for NumericEditedType value when decimal point not considered
  while getting value
- Improved support for reading variable-length field in line-sequential file
- Improved support for record size inheritance from dataset catalog for GDG files
- Improved support for printing report by allowing customizable advancing lines
- Improved initialization of record data for Variable Block (VB) Files

### GS21

**New features**

- Screen - Added support for PSAM files
- Screen - Added support for ATTR2
- Added support for AIM (Advanced Information Manager) ecosystem.
- Added PED support in AIM

**Improvements**

- Improved BitUtils signatures to handle RangeReference
- Improved support for DummyFileConfiguration to add recordSize / rdw / bdw / blksize /
  blkszlim attributes
- Improved support for VPOINT statement to handle the case of a record not found
- Added robustness when accessing record byte array
- Improved JEF charset character mapping
- Improved support for handling arrays and conditions in JDBC mapping
- Improved support for SQL requests in the different NDB statements, better handling the
  variations of SQL syntaxes using constants for each part of an SQL query.
- Improved support for GS21 PackedType last nibble to be C, D or F for numeric
  validation
- Screen - Improved support for ACSAPI and DefaultPsamController for SPA and ENTER
- Screen - Enhanced support of ACSAPI and NDB verbs

### AS400

**New features**

- Added support for Multi-record format Database files
- Redesigned the AS400 Database access framework
  - Enhanced capabilities around file overriding
  - Removed obsolete components and reduce complexity
  - Streamlined the code generated from legacy programs
  - Integrated DAOCycleManager component into the Blu4iv plugin, enabling us to leverage
    the AS400-specific features of our custom runtime.

- JOB - Improved support for job management (Quartz) to add the ability to interrupt a
  job/group of jobs. Added a REST API endpoint to interrupt a job with the specified execution
  id (unique to each job since it is a primary key). Upon successful interruption, the runtime
  update the status of the job to “INTERRUPTED”.
- Added support for utility program CEERAN0
- Added support for passive mode. Added the YAML `configuration
gapwalk-application.cl:ftpservice:passive` to enable passive mode
- Added feature to create QTEMP sessions and delay QTEMP cleaning
- Added support for compilation feature BNDDIR to define explicit dependencies between
  programs
- Added support for Activation Groups mechanism

**Improvements**

- CL - Improved RMVMSG command on program message queue to handle \*PREV keyword
- CL - Improved support for overrides in OPNQRYF
- CL - Added support for the MSGLEN and SECLVLLEN parameters for the RTVMSG command
- CL - Improved support for CRTDUPOBJ to manage case when NEWOBJ is not passed and added
  support for generic table names
- CL - Improved support of FTP to handle parameters GET, RMTSYS and BINARY
- CL - Improved CLRPFM query performance and added an option to use TRUNCATE instead of
  DELETE
- CL - Improved SBMJOB to properly handle USER parameter to use it as the USER when a job
  is submitted
- CL - Improved DLTOVR command support to handle the case of \*ALL
- Data Area - Improved support for Blu4DataArea by adding logging for Exception
  handling
- Data Area - Improved support for Blu4DataArea to fetch a new DataAreaDao instance for
  every thread
- Data Area - Improved data area locks, avoiding locks at record level and instead using
  the newly implemented locking mechanism
- Data Area - Data Area write operation now continues with execution when a lock isn't
  acquired and an error indicator is provided
- Report - Improved support for report output path/naming convention for the printed
  reports. Allowed customers to customize the report output path and the name as well. The
  customer can specify their own path and naming convention without impacting any other
  project.
- JOB - Improved support for job management (Quartz) to update job status in the event of
  abnormal job termination. e.g.: ‘Shutdown’ or ‘abnormal shutdown’ of Tomcat
- Screen - Improved handling of numerical value on field with edit word with minus
- Screen - Improved rendering popup with only titleColorTop
- Screen - Improved support for help information retrieving to handle case when general
  help item is not found
- Screen - Improved displaying the 'additional information' screen when pressing F1 on
  subfile message line
- Screen - Improved display of message line footers for SFLMSG
- Screen - Improved Front End to remove a Record in its entirety when a new record overlaps
  it
- Queuing - Improved RabbitMQ message retrieval to consume fewer resources
- Queuing - Improved RabbitMQ Data Queue implementation to only retrieve one message at a
  time.
- SQL - Improved SQLExecutorBuilder handling of SQLCODE for dynamic CREATE and DROP table
  queries
- SQL - Improved support of OVRDBF on query
- SQL - Improved SQLExecutorBuilder so that OVRDBF overrides are applied to prepared
  statements
- RPG - Improved support for Input and Output specifications of Program described Disk
  files
- RPG - Improved support for Primary and Secondary File Read with MR (Matching Records)
  indicator. The retrieve order of a DAO Cycle with match fields has been improved.
- RPG - Improved support for Primary and Secondary files. Improvement on the update Primary
  files and output Secondary files update/write code generation.
- RPG - Added support for RETURN statement in free-form format
- RPG - Improved transformation and runtime handling of numeric decimal assignments,
- RPG - Improved generation of binary variables
- RPG - Improved support for EDITC
- RPG - Improved handling of local data area
- Improved support of DDS fields shared by multiple device type (DISK, WORKSATION,
  PRINTER)
- Improved override handling so that overrides on PFs will no longer affect LFs
- Improved Blu4ivWebController not to re-set the username and userid to default
  values
- Improved index adjusting during record reads when the read direction changes
- Improved cursor placement on record reads after update/delete operations
- Improved support of reading on a multi-entities DAO when the reading direction
  changes
- Improved support for User Spaces to avoid instance to be reused by all threads instead of
  each thread having its own instance
- Improved support of multi-threading concurrent access on record read
- Improved the storing of the username/userid in SharedContext through YML
  configuration
- Improved Locked Records Release with Updated Values
- Added support for OPM compiler specific behavior for NEXT SENTENCE statement

### Transversal capabilities

**New features**

- Added new metadata.ini property `legacy.compilerto` specify the legacy
  compiler of the artifacts to transform. The support of some COBOL statements, like NEXT
  SENTENCE, is different depending on the value you set.
  - "ZOS" for a z/OS legacy system.
  - "ILE" or "OPM" for AS400 system. Default = "ILE" when `legacy.system` =
    "as400"

**Improvements**

- Front-End - Redesigned the screen field components to expand the range of supported field
  types. This enhancement enables the runtime to accommodate a wider variety of user input and
  data requirements involved in AS400.
- Improved method `isValid()` for separate sign byte on ZonedType
- Improved support for `StringConcatenationBuilder::withPointer` for
  concatenation involving CRLF
- Improved support for specific double bytes encoding to make them thread-safe
- Improved state machine performances by integrating a new framework
- Improved algorithm for assignment optimization to prevent unexpected rewriting

## AWS Blu Age Transformation Engine 4.4.0

### zOS

**Improvements**

- LISTCAT - Improved parser to prevent duplicate entries
- LISTCAT - Improved support of ESDS to file system in JCL / Groovy
- CICS - Improved support for LENGTH OF for CICS statements

### AS400

**Improvements**

- DDS Record generation enhancement
  - Improved the support of DDS record to generate entities that correspond to the DDS
    record structure
  - Provided support for shared fields and mapping functions that match better with the
    legacy
  - Improved the handling of both externally-described and program-described files

- RPG - Improved RPG detection for module with only free form
- RPG - Improved support for COPY statement to ignore keyword `*LIBL/` as prefix
  to locate an application copybook
- RPG - PF - Improved support for input specification with physical records from
  pfile
- RPG - Added support of On-Exit statement
- RPG - Improved support of LikeRec keyword
- RPG - Improved mapping of renamed DSPF fields
- CL - Improved field name resolving
- COBOL - Improved support of conversion from hexadecimal to character
- Improved support for Decimal type generation
- Improved support of FIXME message for unsupported legacy code (display whole legacy
  line)
- Improved performance on AWS Transformation Engine (AS400 parsing step)
- Improved support of Keyword LikeRec to align it with File Specifications
- Improved support of built-in function %Diff
- Added support for special character Currency sign on DSPF label

## Release notes 4.3.0

Release date: September 16, 2024

This release of AWS Blu Age Runtime and Modernization Tools focuses on extending the capabilities and
coverage to modernize mainframe functionalities. Some key features and changes in this release
include:

- **CICS**: Additional support to exchange data from the
  terminals, and run transactions with incoming data by supporting the SEND MAP command with Map
  Reference.
- **JCL**: New capability that allows to restart the most
  recent execution of a batch job from a previously failed JCL/PROC step, or trigger a delayed
  restart by bypassing previously executed steps. This provides greater control over batch
  processing using persisted step-level checkpoints.
- **AS400**: Additional library support, enhanced performance
  and robustness of commonly used commands such as CPYF, OVRDBF, SBMJOB, and OPNQRYF and many
  more.

We tested this version of the AWS Blu Age Runtime with the following stack. Other component versions might
also be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 18.18         |
| Npm 9.8                   |
| Angular 17                |
| Service layer             | Spring Boot 3.2.5     |
| Spring Core 6.1.5         |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

For more information about the changes included in this release, see the following
sections.

## Runtime release 4.3.0

### zOS

**New features**

- CICS - Added Support for Map Reference in SEND MAP command
- CICS - Added support for RECEIVE command and support for running transaction with data
  from the `JicsTransactionRunner` screen
- Added support for IIH header for the JMS messages
- COBOL - Added support for multiple embedded spaces in Pseudo-text for REPLACING
  statement
- COBOL - Added support for JSON PARSE statement
- <noloc>Blusam</noloc> - Added support for KMS to feature “Export dataset”
- BAC - Added the configuration of `application-main.yaml` to define
  record size to filter loaded masks matching with this record size
- JCL - INFUTILB - Added support for the keyword INTO as part of BMC control
  statement
- GS21 - Added SOSI handling for JEF encoding
- GS21 - JCL - Added KDJBR14 as an alias of IEFBR14
- GS21 - JCL - Added KQCAMS as an alias of IDCAMS
- MF - Added support for COBOL MF Compatible File dependingOn field support
- MF - Added support for SORT mechanism for COBOL MF Compatible file
- MF - Added support for COBOL MF Compatible open non-optional missing file

**Improvements**

- JCL - DSNUTILB - Improved LOAD operation with ZONED DECIMAL Type
- JCL - DSNUTILB - Added support of duplicate key
- JCL - DSNUTILB - Added support for rollback mechanism on LOAD command
- JCL - INFUTILB - Improved UNLOAD with new properties FETCHSIZE and CHUNKSIZE
- JCL - IKJEFT1A - Enhanced SYSTSIN file reading by adding current charset
- JCL - DFSORT - Added support for option DATE4 & DATE5
- JCL - DFSORT - Added support for case of Variable Block type as input and Fixed Block
  type as output
- JCL - DFSORT - Added support for ALTSEQ
- JCL - Enhanced checkpoint metadata with job web identifier
- JCL - Improved Batch restart checkpoint purge for REDIS
- IMS - Implemented EXPRESS function for PURGE command
- IMS - Added support for options PCBNAME and LIST for PCB statement
- COBOL - Added support for GO TO statement without target
- CICS - Improved support for INTO statement with RecordAdaptable in READQ TS
- CICS - Improved support for INQUIRE TRANSACTION command
- CICS - Improved support for setBytes in READNEXT command
- CICS - Improved support for START command without CHANNEL option
- CICS - Added Support for Reference type for Inquire TSQueue
- CICS - Improved support for RECEIVE MAP command when map and mapset are Reference
- CICS - Improved support for options FROM and LENGTH for RECEIVE MAP command
- CICS - Added support of RecordAdaptable attribute
- CICS - Improved support for RECEIVE command to handle overflow
- CICS - Added support for slice rule in CICS statements
- CICS - Improved support for linkage structures DFHCOMMAREA and DFHEIBLK. The
  transformation engine supports more implicit definitions
- CICS - Added support for options START, NEXT and END for INQUIRE CONNECTION
  command
- CICS - Added support for both type ‘int’ and ‘reference’ for option LENGTH of RECEIVE
  command
- CICS - Enhanced support for parsing INQUIRE NETNAME command
- CICS - Added support for group name for JicsQueueBuilder
- <noloc>Blusam</noloc> - Added support for indexed file starting with generic
  key
- <noloc>Blusam</noloc> - Improved <noloc>Blusam</noloc> loaders
- BAC - Improved support for data synchronization in multi-instance environment when Redis
  is used to centralize cached values, including both actual data and locks
- BAC - Improved UI (style, logo, checkbox)
- BAC and JAC - Added the configuration of `application-main.yaml` to retrieve the username
  and the password of the default super admin user in the secret from AWS Secrets Manager by
  specifying the ARN
- BAC and JAC - Upgrading dependency to Bootstrap 5
- Improved JCL checkpoints and JICS TSQueues Redis template configuration
- Improved support for Size of Pointer depending on AMode
- Added support for zero comparison on NumericEditedType
- Enforced Slf4j MDC properties before logging
- Improved support to file reading to handled multiple empty line
- MF - Improved support for initializing pointer variables for COBOL MF compiler directive
  initPtr
- Redis - Improved feature GwFileLock on concurrence aspect through an implementation based
  on Redisson

### AS400

**New features**

- CL - Added support for CHGPF command
- RPG - Added support for functions %HOURS, %MINUTES and %SECONDS
- COBOL - Added support of SORT file with Blu4IV DAO architecture

**Improvements**

- CL - Improved PgmClose to be registered as a program and accept a variety of objects for
  OPNID param
- CL - Refactored RTVMBRD to handle multiple libraries and members
- CL - Added support for TOLIB param on MOVOBJ command
- CL - Improved support of partition on CPYFRMSTMF command
- CL - Added support for SNDMSG parameter TOUSR
- CL - Improved support of OVRDBF command
- CL - Improved performance for OVRDBF command - Update Default Values for srcfile and
  member
- CL - Improved file copy with CPYF command
- CL - Re-engineered CPYF command to be more robust and better handle QTEMP, CRTFILE,
  FROMRCD & TORCD, MBROPT, and FMTOPT(_MAP &_ DROP)
- CL - Improved support for CPYF command for cases where FROMFILE & TOFILE have
  mismatched columns
- CL - Improved CPYF _NOCHK's_ handling of columns with
  different names when REPLACE is specified
- CL - Added empty implementation for CRTDUPOBJ command on logical files
- CL - Handled substring indexing issue with CHGDTAARA command
- CL - Improved support of SBMJOB command
- CL - Made OverrideManager and OpnqryfHelper mappings case insensitive
- Screen - Improved the initial focus of the first editable field when a cursor is not
  specified
- Screen - Improved focus position after closing and when using help menu
- Screen - Improved cursor focus after pressing page up/down in table component
- Screen - Improved support for multiple field error messages and focus
- Screen - Improved line number computation for subfile fields
- Screen - Improved support of sub files initialized using SFLINZ
- Screen - Improved support for numeric only entry
- Screen - Improved handling of WINDOW keyword in DSPF with 3 parameters
- Screen - Improved position of footer for table with records containing more than 1
  line
- Screen - Improved page navigation for rotation message sticking on Page Up/Down
- Improved EDITC functionality for edit code 3
- Improved Blu4iv data area lock mechanism to do nothing when there is no lock to unlock
  instead of throwing exception
- Added support to return the number of rows affected in StraightQueryBuilder
- Improved QTEMP log mechanism
- Improved DAOManager reads/writes/deletes for use cases on file overrided by a different
  file + library

### Transversal capabilities

**New features**

- Added a centralized way to manage the SSL/TLS-related system properties by configuration,
  allowing the use of AWS Secrets Manager
- Enhanced configuration of IBMMQ resources with AWS Secrets Manager
- JCL - Added the temporary location configuration for Runtime resolved groovy files
  through the YML property tempFilesDirectory and added the capability to specify whether to
  purge contents of the temporary files folder at application startup through the YML property
  cleanTempFilesDirectoryAtStartup
- Add AWS secrets for all Redis credentials

**Improvements**

- Improved conversion from type alphanumeric to type numeric edited
- Improved DataUtils::isNumeric check for PackedType
- Enhanced log file timestamping
- Handled separate sign in ZonedType.decodeAsString
- COBOL - Improved support of statement INITIALIZE
- Improved support of DataUtils.compareAlphInt to handle leading and trailing spaces for
  AS400 and ZOS
- SQL - Improved implicit read-only cursor runtime validation
- SQL - Improved Metadata caching mechanism
- Remove Jics/<noloc>Blusam</noloc> database connection from Gapwalk Application
  `application-main.yml`

## Modernization tools release 4.3.0

### zOS

**New features**

- GS21 - Add support for COBOL GS21 CONSTANT SECTION
- GS21 - Added JEF encoding to available charsets

**Improvements**

- CICS - Added support for parsing DOCUMENT CREATE command
- CICS - Added support to parse CICS WEB EXTRACT command
- CICS - Added support for parsing WEB WRITE command
- CICS - Added transformation support for DB2CONN SIGNIN and PLAN
- CICS - Enhanced support for parsing SEND MAP command by ignoring option TERMINAL
- CICS - Enhanced support for parsing RETURN command by ignoring option ENDACTIVITY
- MFS - Improved support to Generate MFS files with specific extension
- COBOL - Improved support for REPLACE statement
- COBOL - Handled dynamic path and MF compiler directive
- COBOL - Improve support for OMITTED value in CALL Statement
- COBOL - Improved multi-dimensional fields access to support signed value
- COBOL - Added support for clause OF for FILE STATUS statement
- COBOL - Improved parsing of statement RESULT-SET-LOCATOR
- JCL - IDCAMS - Added support for RECORDS abbreviation

### AS400

**New features**

- CL - Added support for pointer based and defined variables in CL transformation
- CL - Added support for special characters in DCLF
- Added support for retrieve call stack (QWVRCSTK) API

**Improvements**

- RPG - Improved transformation of procedure parameters using `likeds`
  keyword
- RPG - Review support of keyword EXTNAME
- RPG - Improved support literal value \*ALL
- RPG - Improved support for output specification and program-described files
- DDS - Improved resolution of DDS fields in a LF that references a PF that references a
  Dictionary PF
- Screen - Cleared indicators when CLEAR statement is used to clear a record from
  DSPF
- CL - Improved transformation/generation of CL params with element lists

### Transversal capabilities

**Improvements**

- SQL - Improved generation of SQL queries containing N with tilde character
- COBOL - Improved support of the statement LENGTH OF for group fields
- COBOL - Improved support of REDEFINED fields using copybooks

## Release notes 4.2.0

Release date: July 10, 2024

This release of AWS Blu Age Runtime and Modernization Tools is focused on performance and security. Some
key features and changes in this release are:

- We improved transformation performance, especially for large projects with over 30 million
  lines of code. We implemented a set of improvements and the results we obtained showed a time
  reduction of over 150%, and runs that completed in minutes instead of hours. The key
  improvement we implemented is the configuration of a timeout mechanism to limit the maximum
  time allocated for analysis so as to skip files with detected issues. We mark skipped files so
  that you can investigate them later if necessary.
- We added support for a distributed lock management system for AS400 projects. In a High
  Availability environment (multi-node) where multiple instances of the application target the
  same database, maintaining data consistency throughout the life cycle of these instances is a
  significant challenge. To effectively address this challenge, we added Redis as a shared and
  external caching server to coordinate among all instances when running in batch mode.
- We added a new dynamic pagination feature for the table component. The goal of this
  feature is to improve the response time and reduce memory usage for tables with a large number
  of rows. This feature allows the table component to only load part of the data, and to fetch
  more records on demand as you navigate through the pages. To further improve the experience,
  the platform also supports the prefetching of data. This new dynamic pagination feature
  provides a more efficient and responsive user experience for applications with large data
  sets.
- To address a key challenge that comes up frequently, we added support for nested COBOL
  programs. Previously, the workaround for modernizing nested COBOL programs involved manually
  separating programs into different files, linking them through the linkage section, and making
  them call each other with the necessary arguments. This process was not only time-consuming but
  also error-prone. You can now modernize nested COBOL programs without the need for manual
  separation.

We tested this version of the AWS Blu Age Runtime with the following stack. Other component versions might
also be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 18.18         |
| Npm 9.8                   |
| Angular 17                |
| Service layer             | Spring Boot 3.2.4     |
| Spring Core 6.1.5         |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

For more information about the changes included in this release, see the following
sections.

## Runtime release 4.2.0

### zOS

**New features**

- DB2 - Added support for stored procedure invocation without schema qualifier in the SQL
  query
- COBOL - Added support for HEX-OF function
- COBOL - Added support for nested programs
- COBOL - Added support for FUNCTION TEST-DATE-YYYYMMDD and TEST-DAY-YYYYDDD
- CICS - Added support for option UCTRANST in the SET TERMINAL command
- CICS - Added support for the INQUIRE DB2CONN command
- <noloc>Blusam</noloc> - Added support for key deletion on dynamically accessed
  VSAM
- IMS - Added support for the TERM command
- BAC - Added authorization checks on all BAC REST endpoints
- BAC - Added configuration through `application-main.yaml` to define a
  record size to filter loaded masks that match that record size
- BAC and JAC : Added configuration through `application-main.yaml` to
  retrieve the username and the password of the default super admin user in the secret from
  `command` by specifying the ARN

**Improvements**

- JCL - SORT - Enhanced support for OMIT clause to handle conditions with Shiftin and
  ShiftOut characters
- JCL - SORT - Improved support for the BDW field
- JCL - SORT - Improved support for multiple GDG concatenations with the BDW field
- JCL - DFSORT - Added support for INREC PARSE STARTAFT / STARTAT clauses
- JCL - IEBGENER - Enhanced recordSize handling for output files
- JCL - INFUTILB - Disabled NULL INDICATOR based on YML- FIX GRAPHIC CASE
- JCL - Improved support for FormatterParser to handle constants in the OUTREC field
- JCL - Enhanced load data for graphic type in DSNUTILB program utility
- JCL - SORT - Enhanced support for Zoned Decimal format
- JCL - SORT - Enhanced support for the OMIT clause to handle conditions with Shiftin and
  ShiftOut characters
- MQ - Improved the handling of MQ connection to fit several business workflows
- CICS - Enhanced support of pointer reference for EXEC CICS READ SET (ptr-ref)
  statements
- COBOL - Improved support for ADDRESS OF linkage section record
- COBOL - Added support for EXP and EXP10 functions
- COBOL - Improved support for the REPLACE statement using copybook
- COBOL - Improved multidimensional field access to support signed values
- MF COBOL - Added support for variable-format sequential files
- IMS - Improved reading of the configuration of IMS YML files to make it possible to use
  environment variables
- IMS - Handled additional ways of specifying the segment number
- IMS - Added robustness when an IMS program is called from a programatically-started
  transaction
- IMS - Improved the search criteria SSA build to take the current length of the WHERE
  clause into account if the implied segment length is not provided
- IMS - Improved reading of the configuration of IMS YML files to allow the use of
  environment variables
- Improved support for the VALUE clause in NumericEditedType
- Improved support for string concatenation to handle the case when the first string to be
  concatenated is empty, blank, or spaces

### AS400

**New features**

- Added support for pagination inside the Table component; projects can use this feature to
  decrease the response time and size when a Table component with a large number of rows is
  loaded
- Added library support for SQL queries on the AS400 application; because libraries are
  converted to partitions in modern applications, we adapted the runtime to rewrite the queries
  accordingly
- RPG - Added support for the QTEMP library for SQL queries
- RPG - Added encoding in the CONVERT function to handle empty input values
- RPG - Added support for the %HOURS, %MINUTES, and %SECONDS functions
- CL - Added the CHGPFM command
- CL - Added support for the \*FROMLIB keyword in the CRTDUPOBJ command
- CL - Added support for table and partition creation for table names exceeding 9
  characters
- CL - Added support for deletion of flat files in subfolders for the DLTF command

**Improvements**

- Screen - Improved ErrorMessage to bind with specific field and add to
  ArrayMessageLine
- Screen - Improved errormsg cursor
- Screen - Improved ArrayMessageLine to not be included in Tab Order
- Screen - Improved display of error message arrays for AS400 screen
- SQL - Improved cursor support to commit Transaction upon closing to avoid deadlocks on
  partition creation
- CL - Added support for the PgmCall command and improved the QCMDEXC unsupported
  pattern
- CL - Improved support for the CHKOBJ command to handle OBJTYPE PGM
- CL - Improved multi-library support for CPYF and other CL commands that deal with
  libraries and partitions
- CL - Added support for passing a program name variable in the CALL PGM command
- CL - Handled the case for default type of Object type
- CL - Added multi-library support for the CRTDUPOBJ command
- CL - Enhanced database connection handling on multiple commands
- CL - Improved support for RMVLNK to handle the case when a file or directory isn't found
  and the CPF0000 monitor message
- CL - Improved CLRPFM to take the library into account when removing records
- CL - CPYF - Improved command to support the QTEMP library, FmtOpt(\*NoChk) parameter, and
  control character
- CL - Fixed handling of quotation marks and missing parameters in the RMVLNK and CPY
  commands
- RPG - Enhanced variable scoping; DataArea is now in working scope instead of linkage
  scope
- RPG - Improved DAO read queries to run without a transaction to avoid deadlocks
- Enhanced MQ messaging lookup by adding a trim to MSGQ on DB lookup
- Removed unnecessary transaction declarations on database connection support
- Improved the update of Quartz job status in case of exception
- Added support to handle the case when an indicator array isn't initialized

### Transversal capabilities

**New features**

- Redis - Added global Redis configuration for all Redis caches
- Added session-tracking functionality to make it possible to store session-tracking
  information (session ID, associated username, creation timestamp, and node ID) by persisting
  the data to Redis
- Added temporary location configuration for runtime resolved groovy files through the YML
  property `tempFilesDirectory`; also added the capability to specify whether to
  purge contents of the temporary files folder at application startup through the YML property
  `cleanTempFilesDirectoryAtStartup`

**Improvements**

- Enhanced support for connection pool implementation configuration properties for utility
  data sources
- Improved support for printer mode and ANSI carriage control based on the usage of
  ADVANCING clauses and WRITE BEFORE clauses
- Updated Angular version on front-end application for modernized projects
- Enhanced secret manager URL syntax construction for DB2
- Enhanced the DataUtils.compareAlphInt method to add support for trailing spaces
- Improved SQL support for blob type output
- Added robustness for job triggers through post/script endpoint

## Modernization tools release 4.2.0

### zOS

**New features**

- CICS - Added support for parsing WEB CICS commands
- CICS - Added support for the transformation of the MONITOR command
- CICS - Added support for parsing the CICS command SEND MRO
- COBOL - Added support for parsing the NO REWIND statement
- COBOL - Added support for number type of option UCTRANST in the CICS command SET
  TERMINAL
- COBOL - Add supported for the MULTIPLE FILE clause in I-O-SECTION
- CSD - Added support for the transformation of multiple CSD files
- CSD - Added support for the generation of jicsFileAix.json from multiple CSD files
- IDCAMS - Added support for the creation of a relative record data set (RRDS)

**Improvements**

- Improved performance when computing SQL masks
- COBOL - Improved parsing of useless RESERVE clause in FILE-CONTROL
- COBOL - Improved parsing of SECTION and CLASS
- COBOL - Improved DFHRESP handling
- COBOL - Enhanced support for EXIT PARAGRAPH through perform
- IMS - Improved support for segment names specified by using double parentheses
- IMS - Enriched the generation of status codes when SCHD and TERM are invoked
- COBOL - Improved generation of DEPENDING ON fields
- COBOL - Improved transformation of TO_TIMESTAMP DB2 builtin function

### AS400

**New features**

- Added support for converting alphanumeric fields as CHAR in SQL scripts
- COBOL400 - Added support for program-described DATABASE files

**Improvements**

- DDS - Improved support for ALIAS name
- Enhanced support for type float without initial value
- COBOL 400 - Improved size compute for signed zoned type

### Transversal capabilities

**Improvements**

- Improved error ID reporting around DDS and SQL parsing
- Improved code generation on condition branches
- Improved performance on weather report generation

## Release notes 4.1.0

Release date: May 31, 2024

This release of AWS Blu Age Runtime and Modernization Tools is focused on performance and security. Some
key features and changes in this release are:

- **Transformation and performance**: To allow projects with a
  large codebase (+50M lines of code) to transform successfully, we have optimized the
  performance and memory footprint of the whole transformation mechanism.
- **BAC/JAC**: Security at AWS is the highest priority.
  Applications modernized with AWS Blu Age must comply with security standards. We have made some major
  upgrades to the <noloc>Blusam</noloc> Administration Console (BAC) and the JICS
  Administration Console (JAC) to make them more secure:
  - Updated the application to Angular v17.
  - In addition to the native support for AWS Cognito, we added generic support for OAuth
    that will enable more flexibility to let customers use the identity provider of their
    choice.
  - Configured and extended the security features using appropriate headers.

- _AS400 - Multi-node support for database lock mechanism._ Provided the
  possibility to plug a shared and external caching server (Redis) to run a batch application on
  multiple instances, like managed AWS Mainframe Modernization.

This version of the Blu Age runtime has been tested with the following stack. Other versions
might also be compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 18.18         |
| Npm 9.8                   |
| Angular 16.1              |
| Service layer             | Spring Boot 3.2.5     |
| Spring Core 6.1.5         |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21c                |
| Application server        | Apache Tomcat 10.1.17 |

For more information about the changes included in this release, see the following
sections.

## Runtime release 4.1.0

### zOS

**New features**

- Added configuration for dynamic OAuth2 provider handling. Introduced
  SECRET_OAUTH2_PROVIDER_NAME_KEY to specify provider. Updated secret retrieval method to handle
  multiple providers. Ensured secrets are securely retrieved from AWS Secrets Manager.
- Added support for DB2 SSL properties on AWS Secrets Manager to make it possible for you to define
  an SSL certificate (sslTrustStoreLocation) and a password (sslTrustStorePassword) to unlock
  the keystore file.
- Added support for external business data sources.
- JCL - Added support for checkpoint mechanism for batch restart.
- JCL - Added support for DCB parameters record size and RDW.
- JCL - Added dynamic folder-name configuration for generated temporary files.
- REDIS - Added pool configuration in Redis configuration for JICS.
- REDIS - Added database index in Redis configuration for Catalog and JICS.
- BatchScript - Added propagation of step name for running program executions.
- CICS - Added support for the ADDRESS SET command.
- CICS - Added support for PURGE MESSAGE and JUSTIFY.

**Improvements**

- JCL - INFUTILB - Enhanced support for disabling the null indicator based on YML
  property.
- JCL - INFUTILB - Improved support for the CHAR/BPCHAR datatype.
- JCL - ICEGENER - Added support for copying multiline input streams into files.
- JCL - IEBGENER - Improved support for handling conversion from Variable Block to Fixed
  Block files.
- JCL - DFSORT - Improved support for multi-digit parameters on operation DATE.
- JCL - DFSORT - Added support for the INCLUDE=ALL clause.
- JCL - Improved support for the SORT utility to handle the BDW field in output.
- JCL - Improved support for DD concatenation.
- JCL - Improved support for Input Stream.
- JCL - DSNUTILB - Improved support for the NULLIF() statement.
- JCL - INFUTILB - Added support for unloading data with the NOPAD option.
- JCL - INFUTILB - Enhanced support for current date in INFUTILB.
- JCL - Added file existence and size checks before using a file.
- JCL - GDG - Improved the handling of sub-directories for GDG.
- MQ - Improved connection opening in the JMS implementation.
- MQ - Improved data length setting of GET message for XA datasoure.
- MQ - Decomposed CMQV standard copybook to prevent compilation errors and refactoring
  uses.
- <noloc>Blusam</noloc> - Improved support for delete requests for non-existent data
  sets.
- Improved support for the ALLOCATE statement.
- Improved robustness of TS-QUEUE Naming.
- BatchScript - Enhanced preservation of previous step return code in job
  re-execution.
- Dataset - Improved the file existence check when a file exists and is temporary.
- Dataset - Improved the concurrency when locating GDG files to delete.
- Dataset - Added support for getting GDG Dataset record size.
- CICS - Improved support for the SUSPENDED option in the INQUIRE TASK LIST command.
- CICS - Improved support for LOAD SET using the ADDRESS OF statement.
- CICS - Improved unhandled CICS arguments REMOTESYSTEM when CICS INQUIRE.
- CICS - Enhanced support for the GETMAIN command to handle the SET option with a pointer
  defined with the OF keyword.
- JICS - Improved robustness for the jicsXAPrepare() method by adding the transaction state
  check.
- JICS XA - Added a check for transaction state and enhanced transaction thread
  termination.
- BAC - Enhanced role-based authentication on client side and refactored/centralized all
  API calls.
- BAC - Implemented a feature to block public access to BAC and JAC based on
  configuration
- BAC - Upgrade of the dependencies: Angular 17.
- BAC - Improved security integration with OAuth2.
- BAC - Enhanced hibernate generated DDL.
- BAC - Improved export data set mechanism.
- JAC - Updated to Angular 17 and reporting all specifics work from BAC (ROLE, sadmin conf,
  XSRF, logout).
- COBOL - Added support for the CHAR and ORD-MIN functions.
- Enhanced FileFactory to keep catalog record size in MOD disposition.
- Enabled logging using MDC for JICS transactions.
- Improved SQLCA > SQLSTATE produced for stored procedures generating ad-hoc result
  sets.
- Improved support for task scheduling related to last Spring upgrade.

### AS400

**New features**

- Added multi-node support for database record locks using Redis.
- Added support for BINARY CHARACTER for the DDS type.
- CL - Added support for custom report file generation.
- RPG - Added support for the RENAME keyword on primary/secondary files.

**Improvements**

- Improved database support for handling the CTID column with a JOIN clause.
- Improved cursor position for multiple DSPATR(PC).
- Improved logging on read exception.
- Improved Quartz job logging to include job properties to MDC.
- Improved support for the AS400 help screen.
- CL - Improved support for the RMVJOBSCDE command to accept entry numbers with trailing
  spaces.
- CL - Improved support for the RMVJOBSCDE command to remove a job schedule using a generic
  job name.
- CL - Improved support for the SAVOBJ command to order records by table key.
- CL - Improved support for the CPYF command to establish a new connection for DB
  queries.
- CL - Improved insertion of inquiry messages in queue message with SNDPGMMSG.
- CL - Improved job queue configuration to specify default job queue.
- CL - Improved the CRTPF command to support the QTEMP library and the RCDLEN
  parameter.
- CL - Improved support for the CHKOBJ command - Check for partition with library.
- CL - Improved RTVMGS to send CPF2407 and CPF2419 when file/ID not found.
- CL - Improved CPYTOIMPF and CPYFRMIMPF interpretation of legacy formatting
  parameters.
- CL - Added support for OVRPRTF parameter USRDTA.
- CL - Improved the CPYTOIMPF CL command to establish a new connection to avoid closing
  existing result sets.
- CL - Improved CHGDTAARA so that it no longer modifies the data area length when it
  updates the content.
- CL - Improved ClCommand database connection handling.
- Optimized interaction between the front end and the back end.
- COBOL - Updated transformation to handle FILLER in copybooks.
- Improved additional message information display for custom messages sent to the front
  end.
- Updated the default value for the selector in app.component.ts.
- Improved text splitting in split-dynamic-field display.
- Improved the display of error message with multiple writes followed by a read.

### Transversal capabilities

**New features**

Added support for the dynamic configuration of OAuth2 provider secret.

**Improvements**

- Printing - Improved QCMDEXC parameter support for handling quotation marks and improved
  report name formation
- Improved support for delimited syntax on RecordAdaptable.
- Enhanced InspectBuilder error logging to add context about source string.
- DataSimplifier - added robustness for ByteArray affectation.
- Enhanced MDC logging with new runtime attributes.

## Modernization tools release 4.1.0

### zOS

**New features**

- Added support for multiple CSD file transformations
- COBOL - Added support for the CICS ALLOCATE statement.
- COBOL - Added support for ON SIZE ERROR in the ADD CORRESPONDING statement.
- COBOL - Added support for EXIT PARAGRAPH.

**Improvements**

- COBOL - Improved support for -INC copybook.
- COBOL - Enhanced support for FILLER initialization.
- COBOL - Improved support for figurative values comparison.
- COBOL - Enhanced support for WHEN ANY in consecutive WHEN clauses lacking intermediary
  code blocks.
- COBOL - Improved support for figurative constant.
- COBOL - Improved support for packed type size computation.
- COBOL - Improved unhandled CICS argument KEEP for SPOOLCLOSE.
- COBOL - Improved generation for the TEST-NUMVAL function.
- COBOL - Improved Java generation arguments on INSPECT framework support.
- CICS - Improved support for defining DFHCOMMAREA.

### AS400

**New features**

- RPG - Added an error-catching mechanism to generate the (incomplete) DDS so it won’t
  block program generation.
- Added support for the INCLUDE file description specification keyword.

**Improvements**

- RPG - Improved full-free parsing.
- RPG - Added robustness with error catching.
- RPG - Improved initialization of field/DS with export keyword.
- RPG - Improved DAO operation to handle indicators.
- RPG - Handled the default value of PERRCD with CTDATA.
- RPG - Upgraded the Free-RPG parser to log a unique error per parsing rule.
- PRTF - Handled name collision between PRTF and JRXML.
- COBOL - Improved support of the LIKE keyword.

### Transversal capabilities

**Improvements**

- Added robustness for ErrorID API
- Performance optimization for large project transformation. For example: timeout to skip
  blocked files, re-use of the classification from Blu Insights, and better memory
  allocations.
- Optimized the memory footprint during COBOL/PL1 transformation.
- Fixed CVE on third-party (jQuery and bootstrap).
- Managed timeoutParser options in TC.
- Improved the multiple spaces rewriting on SQL queries.
- Improved Read Only Cursor with sensitivity attribute.

## Release notes 4.0.0

Release date: April 8, 2024

For instructions on how to migrate from AWS Blu Age Runtime 3.10.0 to 4.0.0, see [Migrating from 3.10.0 to 4.0.0](ba-migration-notes.md#3.10-to-4.0 "ba-migration-notes.md#3.10-to-4.0").

This release of AWS Blu Age Runtime and Modernization Tools is focused on upgrading critical dependencies
and supported technologies while boosting performance in multiple functionalities. Some key
features and changes in this release are:

- - **Upgrade from Spring Boot 2.7 to 3.2.4, Spring Core 5.3 to 6.1.5,
    and Tomcat 9.0 to 10.1.17** to provide improved security, performance, and
    maintainability by using versions that are actively being patched and maintained.
  - **Lazy loading on front-end application** to build faster
    large projects with more than 2000 screens and reduce the displaying initialization from 10 s
    to 300 ms.
  - **Support for DBCS display on front-end application**for
    enhancement of the support of double-byte characters to provide a new font that handles
    double-byte and single-byte characters, prevent single-byte input in a double-byte field, and
    handle fields with mixed double-byte and single-byte characters.
  - **Thread monitoring feature for AS400 Online application**
    to run AS400 application with parallelization.
  - **Improved performance on context and RunUnit
    initialization** by adding a configurable mechanism to pre-initialize program
    context reducing the impact of loading complex structures inherent in legacy
    complexity.

This version of the AWS Blu Age Runtime was tested with the following stack. Other versions might also be
compatible.

|                           |                       |
| ------------------------- | --------------------- |
| **Component**             | **Version tested**    |
| Java                      | Java 17               |
| Presentation layer        | Node JS 18.18         |
| Npm 9.8                   |
| Angular 16.1              |
| Service layer             | Spring Boot 3.2.4     |
| Spring Core 6.1.5         |
| Spring statemachine 4.0.0 |
| Persistence layer         | PostgreSQL engine 14  |
| Oracle 21                 |
| Application server        | Apache Tomcat 10.1.17 |

For more information about the changes included in this release, see the following
sections.

## Runtime release 4.0.0

### zOS

**New features**

- Added support for include statement '-INC CPYNAME'.
- CICS - Added support for PUSH/POP HANDLE statement.
- COBOL - Added support for "ASSIGN TO DYNAMIC".
- Added support for DB2 UNLOAD using INFUTILB.
- Added support for keyword SEQNUM in an OVERLAY of INREC statement.

**Improvements**

- SORT - Added support for special chars (parenthesis and asterisks) in sort string
  literals C'....'.
- SORT - Improved support for OUTFIL NOMATCH-(..) argument.
- SORT - Added support for SYMNAMES data definition.
- SORT - Improved handling of TO= and LENGTH= arguments.
- SORT - Improved handling on MOD disposition.
- SORT - Added support for HIT=NEXT argument.
- Enhanced ICEGENER to add support for specific output file encoding.
- INFUTILB - Enhanced support for WITH UR clause.
- INFUTILB - Enhanced support for unload when writeNullIndicator is false.
- DSNUTILB - Enhanced robustness to load step when the NULLIF keyword is after an optional
  SQL keyword.
- DSNUTILB - Enhanced support for isolate column name.
- DSNUTILB - Added support to load an empty file into a table.
- DNSUTILB - Added support for MOD disposition for the DNSUTILB SYSDISC file.
- IDCAMS - Enhanced comments support.
- JCL - Added support for column with double quote in LoadTask.
- JCL - Enhanced UNLOAD SQL query handling regarding whites paces removing.
- JCL - Enhanced response of Groovy script when an exception occurs in processing to assure
  a JSON format.
- JCL - Improved check file disposition in the case of DISP=NEW and DISP=OLD.
- JCL - Enhanced support to handle multiple GDG generation reference with special character
  in GDG base name.
- JCL - Enhanced support to load a dummy file.
- JCL - Enhanced support for tempFilesDirectory YML parameter.
- JCL - Improved JSON return when it is needed to escape double quotes within a string
  element .
- JCL - Enhanced FileUtils to support GDG base name.
- JCL - Enhanced DSNTEP program for DB2 multiple queries execution.
- Added support for Spring beans.
- Enhanced SQLConverter to avoid rectifying wrong dates.
- Improved JicsTimeBuilder handling of YYYYDDD.
- Allowed custom jars to be accessible from groovy.
- IMS - Enhanced navigation across records in the IMS database implementation.
- IMS - Enhanced CBLTDLI to be able to launch program use purge.
- IMS - DFSRRC00 able to pass the params from groovy to backend program.
- Added support for JICS command that was not invoked through a transactionRunner.
- JICS - Improved performance by using configurable cache.
- <noloc>Blusam</noloc> - Add support for disabling warmup
  <noloc>Blusam</noloc> when opening to enhance performance for large dataset.
- <noloc>Blusam</noloc>- Improved delete/rename behaviour on regular
  <noloc>Blusam</noloc> data sets.
- <noloc>Blusam</noloc> - Enhanced performance on record operations.
- Enhanced datasimplifier for the methods determining if a string is low value.
- Enhanced support for Packed-Decimal & sorting order issue.
- Enhanced configuration of DB2 as primary data-source with AWS Secrets.
- Enhanced FileSystem API to expose the file status.
- Enhanced DynamicFileBuilder read stream input with lineSeparator.
- Enhanced datasimplifier for the methods determining if a string is low value when deals
  with CUSTOM930 charset.
- SQL - Improved SQL Stored Procedure Output Processing.
- SQL - Improved lambda mapping for multiple table with aliases.
- COBOL - Improved support fro LENGTH OF statement.
- COBOL - Added support for TRANSFORM statement.
- COBOL - Added support for 9 new mathematical functions.
- COBOL - Improved support for INTEGER-OF-DAY FUNCTION.
- COBOL - Improved support for 88 level involving figurative value.
- COBOL - Improved transformation for SET ADDRESS statement.

### AS400

**New features**

- Removed duplicated indicator entities.
- Added support for DBCS characters.
- Introduced handling of HELP keyword for subfile record control.
- Added configuration parameter to toggle column name capitalization & split comment
  column content on pipe char.
- Added support for using 0x0c as last nibble for Packed type fields.
- RPG - Handled prototypes declared with ExtProc('system').
- CL - Handled 'CLEAR' parameter of cl-command RMVMSG + introduce in-memory non-program
  message queues.
- CL - Handled generic statements being passed to SBMJOB CMD() calls.
- CL - Added command STRCMTCTL and ENDCMTCTL. Modified locking mechanism and cleaning up of
  transactions and locks.
- CL - Added support for RCDDLM parameter for CPYTOIMPF command.
- CL - Added handling of padding zeros in SAVOBJ command.
- CL - Added handling of libraries included in the qualified name of the OBJ parameter for
  RTVOBJD.
- CL - Added support for CPYTOIMPF command params STRDLM, STRESCCHR, and RMVBLANK.
- CL - Enhanced RTVMGS to send CPF2407 and CPF2419 when file/id not found.
- CL - Improved RCVF command to receive records from any provided library in DEV
  parameter.

**Improvements**

- Changed default values for Blu4iv task executor to allow better scaling by
  default.
- Parameterhelper modified to convert list of strings and ElementaryRangeReference to
  String.
- Enhanced CTID to handle not existing column in POSTGRE.
- Added robustness to support user space API "QUSPTRUS".
- Added support for User Spaces APIs QUSRUSAT and QUSCUSAT.
- Enhanced support for User Space API (QUSPTRUS) without error code.
- Added support for CRON Job Scheduling using Quartz.
- Enhanced support of RPG program cycle.
- Improved Blu4iv transaction management.
- Record locking of files under commitment control within same transaction has been
  improved.
- Improved handling of subfile initialization.
- Improved display of scroll indicators for Message Lines.
- Prevented trailing zeros on numbers sent through data queue.
- Improved Additional Message Information Screen.
- Improved JPA write operations to consider current library.
- Improved behavior of ProgramJobExecutor when executing programs without
  parameters.
- Added functionality to directly pass arguments from front end links to back end
  scripts.
- Improved transaction handling for jobs metadata.
- CL - Added support for param SECLVL in RTVMSG.
- CL - Added empty implementation for CLRLIB.
- CL - Improved CPYFRMIMPF support for copying from both database and CSV.
- CL - Improved CPYFRMIMPF implementation to ignore extra columns.
- CL - Improved CPYTOIMPF and CPYFRMIMPF interpretation of legacy formatting
  parameters.
- CL - Added param removeDecimalPoint to format numeric values in SAVOBJ.
- CL - Improved RCVF command to properly handle EOF condition.
- CL - RTVSYSVAL - Implementation SYSVAL = QDATETIME.
- CL - OVRDBF command modified to get field as default table name.
- CL - RTVJOBA Unavailable value for param : USRLIBL.
- CL - Handled leading slashes in SNDPGMMSG MSGF param.
- CL - Improved support for wildcards in sourcefile in command DSPFFD.
- CL - Improved handling of param PGMQ in RCVMSG and SNDPGMMSG.
- CL - Made RTVMSG param MSG optional to align with legacy docs.

### Transversal capabilities

**New features**

- Improved capability when passing parameter at USING clause of OPEN cursor.
- Performance: Improved pre-initialization of context and RunUnit for performance
  tuning.

**Improvements**

- Improved the mechanism to dump low values from UNLOAD command of INFUTILB utility
  program.
- Added support current schema option on datasources secret manager.
- Enhanced runtime to not consider parameters passed at open cursor when they are not
  needed.
- Improved numeric format validation for numeric fields.
- Improved SQL Diagnostic in highly parallel execution environment.
- Introduced unicode for codepage byte sequence (FE FD).
- DataSimplifier performance optimization - Enhanced assign statements.
- DataSimplifier performance optimization - Improve default value for numeric type
  initialization to prevent useless BigDecimal usage.

## Modernization tools release 4.0.0

### zOS

**New features**

- Added support handling Abend PROGRAM.
- Improved support to generate AIX dataset.
- COBOL - Added support for JUSTIFIED clause on ALPHANUMERIC/ALPHABETIC/GRAPHIC
  fields.

**Improvements**

- Improved PURGETHRESH attribute handling for TRANSCLASS resource definitions.
- Improved support for data definition and MOVE statement.
- CICS - Enhanced support for DELAY command on option MILLISECS.
- Improved SQL lambda mapping for multiple tables with aliases.
- Improved support for parent field finding.
- Improved SQLCA sqlstate set for COMMIT and ROLLBACK operation.
- COBOL - Enhance parsing by commenting obsolete paragraphs
- COBOL - Enhanced support for REPLACING clause.
- COBOL - Added support for mathematical functions ASIN ACOS LOG TAN.
- COBOL - Added support for multiple AFTER statements in PERFORM VARYING.
- COBOL - Enhanced support for RENAMES (level 66) fields.
- COBOL - Enhanced LENGTH OF method to get length at a specific index in an array
  field.
- COBOL - Added support for multiple AFTER clauses in PERFORM VARYING statements.
- COBOL - Enhanced support for RENAMES clause.
- COBOL - Enhanced support of PICTURE keyword.
- COBOL - Enhanced support for Level 88 field parsing.
- COBOL - Improved goto depending condition with table data items.

### AS400

**New features**

- Added functionality to pass arguments to direct front end java calls.
- CL - Improved %SST generation including support for \*LDA with CL→Java.
- RPG - Added support Program-Described record for DISK files.

**Improvements**

- Improved display file, resolve referenced fields with the "REFFLD" keyword.
- Improved support of display file keyword SETOF-CSRLOC.
- Removed files from the commitment control after closing.
- Ensured consistent behavior for concurrent Read and Write Operations on a table when
  performed by the same program.
- Handled assignment to substring of SizePrefixedAlphanumericType.
- Handled passing data structure to procedure with varying-length string parameter.
- Improved retention of invalid numeric values upon onBlur event and creation of event
  listeners for valid fields only.
- Improved error messages on screens and highlighting of fields with invalid input.
- Improved handling of screen fields conditioned on indicators.
- Enabled scrolling with mouse wheel.
- Added support for function keys for Help screen.
- Improved support for long text in split-dynamic-field component.
- Improved handling of multi-record LF files when renaming records.
- CL - Improved RTVJOBD command to handle LF files (views).
- CL - Improved OVRDBF command when used on a multi record LF.
- RPG - Handled scenario where procedure defines a variable with same name as renamed
  param.
- RPG - Improved handling of \*ZEROS when initializing signed binaryInteger.
- RPG - Improved handling of pointers to non-local (reference) variables.
- RPG - Improved handling of ELSEIF statements following IFxx statements.
- RPG - Added support for Fields defined with LIKE on prototype.
- RPG - Improved the support for LIKE keyword of a field created by LIKEREC.
- RPG - Improved generation of operators with figuratives.
- RPG - Improved parsing for array expression xxx(\\\*) and support it in %lookup.
- RPG - Improved LookUp operation code with high and equal (or low and equal)
  indicators.
- RPG - Improved free form parsing.
- RPG - Improved parsing of I-card named constants that follow I-card record
  formats.
- RPG - Improved support for type INTEGER and UNSIGNED.
- COBOL - Added support INDIC clause of DSPF format in COPY DDS statement.
- COBOL - Improved grammar for DISPLAY and ACCEPT statements to unblock transformation and
  generation.
- COBOL - Added support fro DISK files.
- COBOL - Improved DDS display files support programs.
- COBOL - Added support for LIKE clause.
- COBOL - Added support for Program-Described DISK file.
- COBOL - Added support for file name with suffix.

### Transversal capabilities

**New features**

- Handled the Lazy loading of Map Components of web projects.

**Improvements**

- Improved java generation of SQL indicators parameters.
- Improved capacity to handle variables involved in SET DB2 statement.
- Improved raise of error at end of fetched cursor when output is a single entity
  array.
- Managed path in Linux.
- Data Migrator manage vulnerabilities and remove unused dependencies.

## Release notes 3.10.0

This release of AWS Blu Age Runtime and Modernization Tools is focused on core baseline upgrades and
improvements across the product striving to increase performance and robustness in all
transformation and execution steps. Some key features and changes in this release are:

- Version upgrade from Java 8 to Java 17, increasing security and performance, and allowing
  customers to deploy and run applications implemented in a more modern language and to use
  recent third-party framework versions.
- Additional support for managing large shared memory spaces between users or jobs, storing
  data reusable after application or instance restart.
- Faster access to large data sets in <noloc>Blusam</noloc> using a pagination
  mechanism that makes it possible to retrieve a subset of records incrementally.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.10.0

This runtime is based on Java17, Spring2.7, and Angular16.

### zOS

**New features**

- <noloc>Blusam</noloc> - Added support for large data sets through a paginated
  mechanism where indexes are stored and loaded using pages

**Improvements**

- Enhanced DataUtils.compare to handle lower precedence conversion from string to
  number
- Added support to check that no ByteRange is created with improper values through YML
  property dataSimplifier.byteRangeBoundsCheck
- Enhanced removeSOSI() to support the initialization of a GraphicAlphanumericType with an
  empty character
- Added robustness for job operation and secure GDG state read
- <noloc>Blusam</noloc> - Added support for clearing Ehcache of
  <noloc>Blusam</noloc> data sets through a new method named
  CoreBluesamManager.removeCache()
- <noloc>Blusam</noloc> - Improved delete/rename behavior for regular
  <noloc>Blusam</noloc> data sets
- Redis - Enhanced support for unlocking data sets and clearing record lock
- JICS - Improved the error message for failed requests
- JCL - Added support for ControlM variable concatenation based on dot character
- JCL - Added support for Write ADVANCING (ADV) for GDG files
- JCL - Enhanced support for current generation number after delete all GDG files
- JCL - Enhanced support for rdw/recordSize reading from catalog at dataset creation
- JCL - Added support to update the resource object (from AbstractSequentialFile) when
  opening the file with the size of data output record
- JCL - Improved IDCAMS performance
- JCL - Enhanced support for PRINT STATEMENT by adding "CHAR" as alias of
  "CHARACTER"
- SORT - Enhanced support for copy operation from a <noloc>Blusam</noloc>
  fixed-length dataset to a dataset with variable length
- SORT - Enhanced sort grammar to handle some specific statements

### AS400

**New features**

- Added support for User Spaces and its related APIs
- Added support for TOMSGQ parameter of SNDPGMMSG and implemented message queues
- CL - Added support for FILE and SPLFNAME params for the OVRPRTF command
- CL - Added support for handling libraries for corresponding partition table with the CPYF
  command
- CL - Added support for handling the CHGCURLIB command and considering the current library
  when building queries
- CL - Added support for handling the cl command as part of the call stacktrace

**Improvements**

- Improved MessageHandlingBuilder for better handling of the call stack trace entry
- Improved parallel execution of the contextPreconstruct feature
- Improved display attributes when a record is created by SFLINZ
- Improved SAVOBJ to allow the handling of multiple output files
- Improved groovy programs handling by adding them to programCallStack when they are called
  from a Java program
- Improved top positioning detection of help modal
- Improved toPgmQ functionality when toMsgQ param is provided for SNDPGMMSG
- Improved fetching of predefined messages and functionality of message loader
- Improved CPYTOIMPF handling of delimiter characters in content
- Improved release lock on READ record

### Transversal capabilities

**New features**

- Added a translation for system messages on Front-End
- Added a new method in ExecutionContext to return the program call stack
- Set a line separator (for data simplifier) regardless of the actual environment
- Added the possibility to configure the SQL model JSON path

**Improvements**

- Improved the comparison method DataUtils.compareAlphInt() when padding is involved
- Creation of a flag to allow custom behavior on exception in cursor queries
- Improved graphic LOWVALUES db conversion

**Third party**

- Upgrade to mitigate CVE-2024-21634, CVE-2023-34055, CVE-2023-34462,
  IN1-JAVA-ORGSPRINGFRAMEWORKSECURITY-5905484, CVE-2023-46120, CVE-2023-6481, CVE-2023-6378,
  CVE-2023-5072)

## Modernization tools release

3.10.0

### zOS

**Improvements**

- COBOL - Added support for ABS function
- JCL - Enhanced variable scope: attached to STEP instead of JOB
- Enhanced cursor parameter injection for low/high value
- Improved CSD parsing, notably for remote TRANSACTIONS

### AS400

**Improvements**

- Removed blank check for Control Level Indicator
- Added support for external name for IMPORT/EXPORT keywords
- Added support for %LEN on fields
- CL - Added support for new operators for the CLLE language
- CL - Added support for nested IF
- COBOL - Improved handling of the START command when used with multiple keys
- DSPF - Improved handling of cursor position with record number
- DSPF - Improved the formatting for signed numeric, numeric only fields, and fields with
  large scale
- DSPF - Improved the determination of the title for Screen General Help
- DSPF - Improved support of Input/Output specifications
- DSPF - Improved handling of grouping separators during validation of numeric field
- Improved mapping output/DDS records
- Improved printer file REFFLT keyword ability to resolve referenced fields
- RPG - Enhanced support for “ALL free” statements
- RPG - Improved condition parsing and added support for handling CABXX without result
  TAG
- RPG - Improved input specification handling of numeric fields
- RPG - Improved handling of procedure calls within IF/ELSEIF/WHEN conditions
- RPG - Improved handling of READ command when called on a dspf file
- RPG - Improve support for files referring to a non-existing DDS
- Improve handling of REFFLD when passed a physical record format name
- Added support to use 'return' as a db column name

### Transversal capabilities

**New features**

- Oracle - Made it possible to define users than SYS to store built-in functions

**Improvements**

- Upgraded Java version from v8 to v17
- Improved SQL condition with Cluster column name
- Added support for ORDER BY clauses from view

## Release notes 3.9.0

This release of AWS Blu Age Runtime and Modernization Tools is focused on multiple transversal
enhancements across the product striving to increase performance in high-availability
architectures, along with new capabilities to raise jobs executions to the next level. Some key
features and changes in this release are:

- Version upgrade from Angular 13 to Angular 16, increasing security and giving access to
  new features that improve the performance in customer’s online applications.
- Add support of cross job features in AS400, with the main high-light that jobs can send
  inquiry messages synchronously among them, enabling decoupling in modernized jobs.
- Performance improvements on the usage of Redis, including connection pool optimization,
  high security on connection and upgraded dataset locking mechanism.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.9.0

### zOS

**New features**

- Sort program: Updated VSAM inputs with fixed length
- JHDB DB: Added configurable timeout

**Improvements**

- Enhanced support for line separator to stream if used in files concatenation
- Enhanced support to open concatenated sequential files. Initialize DataSetIndex after
  opening of the file
- Enhanced support for virtual decimal separator when a NumericEditedType is affected to a
  numeric value
- Enhanced support for NumericEditedType on negative values
- IDCAMS: SYSIN cards are now read using the "encoding" property defined in
  application-utility-pgm.yml
- IDCAMS: Updated grammar to support FILE(..) argument in DEFINE CLUSTER statement
- INFUTILB: Added support for DFSIGDCB argument to override DCB parameters of DD
  SYSREC
- INFUTIL: Enhanced support for "DFSIGDCB YES" parameter
- Improved SPLICE to handle huge input file
- DFSORT: Improved remark fields handling
- DFSORT: Added support for (signed / unsigned) free form numeric format (SFF/UFF)
- SORT: Added parsing support for OPTION PRINT and OPTION ROUTE statements
- SORT/ICEMAN: Added support for enclosed division operations (field with DIV
  operator)
- Enhanced support for CICS READ using generic key
- Function StringUtils.chargraphic fixed to remove SOSI from a graphic type
- Enhance performance on DataUtils.isDoubleByteEncoding
- JCL: Enhanced support for KEEP disposition mode for a temporary data set. The system
  changes the disposition to PASS
- JCL: Handles DCB parameters dynamically
- JCL: Enhanced SUM FIELDS outputs for incorrect values
- JCL: CommonDDUtils::getContent now searches for the recordSize in the catalog
- JCL: Read rdw/recordSize attributes from catalog at dataset creation
- JCL: Added support for DCB=.MYDD to copy DCB parameters of a DD into another in same job
  step
- JCL: Improved record size inheritance system
- JCL: Added (Redis) exclusive dataset lock
- Redis: Added SSL support for standalone mode
- Redis: Added synchronized Redis lock count with lock
- Redis: Supported Pool parameters for Redis lock
- Redis: Optimized metadata refresh with Redis
- Redis: Improved redis cluster support
- Improvement on open locks with IO mode
- Improved datasets locks performance and clear unused locks
- Enhanced path of the dataset during unregister file
- Improved pre-fetch window cache invalidation
- Added support for thread safe utility datasource provider usage
- Enhanced datasetState nullity check
- Enhanced support for not reopening already opened data sets
- Added robustness for job final operation
- Enhanced support for indexes order for keys allowing duplicates
- Enhanced support for skip list serialization order
- Added support for debug dump feature to help diagnose indexes order issues
- Enhanced support for metadata refresh
- Enhanced support for <noloc>Blusam</noloc> bulk read

### AS400

**New features**

- Creates an application-context registry
- Support for DSPF keyword CLRL(NO) Support record locks monitoring
- Support for keyed DataQueue
- Support for INQUIRY messages for batch jobs
- Added support for Program-described Printer file for AS400 COBOL
- Handles RMVJOBSCDE cl command
- Improvement for RUNSQL/DLYJOB
- CHKOBJ: Raising legacy error code for parameter LIB
- SNDPGMMSG: Supports string parameters
- RTVDTAARA: Improved substring in LDA
- DSPFD: FILE param supported added for specific file name
- RUNQRY: Support for sql file in QRY PARAM
- CRTDUPOB: Support to copy the data between data areas
- SBMJOB: Converts instruction to use JobQueueManager
- OPNQRYF: Added support for Qtemp library
- CRTDUPOBJ: Improved logic for copying partition content
- CRTDUPOBJ: Added support for Qtemp for views
- RTVSYSVAL: Support for SYSVAL value, QDATFMT in CL command
- CHKOBJ: Added support for OUTQ
- RTVJOBA: Supports SWS param
- SNDPGMMSG and RCVMSG: Additional parameters supported MSGF, MSGFLIB, MSGDTA, MSGTYPE,
  KEYVAR, MSGKEY, MSGID

**Improvements**

- Improved WORKSTATION I/O cards supports
- Improved handling of set message overlaying previous message
- Supports additional message information on array-messageline
- Improved standalone array wrapper access inside EVAL, SortA, figuratives
- Improve DAOs cleaning when online application ends
- Added support for additional date formats and improve handling of string inputs
- Improved CVTDAT handling of SYSVAL by adding system value helper class Decode and build
  parameters from CL command SbmJob
- Removed package com.netfective.bluage.gapwalk.rt.blu4iv from gapwalk-cl-command component
  scan
- Improved the support of predefined messages for message queue API
- Improved the support of retrieveSubfileRecord for record written in another
  program
- Improved the support of immediate messages for message queue API
- Improved handling of local data area when submitting a job
- Starts JobQueues automatically when the server starts
- Uses applicationContext configuration to decode params for SBMJOB
- Improvement on system-supplied error messages
- Allows RTVMSG to search for .properties files in nested sub-directories
- Handles reset of entities bound to bad/invalid pointers
- Improved MessageHandlingBuilder to display msgId and MsgFile name as strings for
  RCVMSG
- Improved withMsgFileName method of the message queuing API
- Improved data area lock mechanism
- RTVMBRD: Support for lower and upper case for parameter FILE
- CRTDUPOBJ: Improved handling of views
- CPYTOSTMF: Improved handling of connection
- CPYF: Improvement in handling directory name while copying from a flat file
- RCVF: Properly handles DEV/RCDFMT parameters and transformation of RCDFMT for groovy and
  java
- RCVF: Handles subsequent calls and avoid resetting the cursor
- CPYF: Added support for writing from flat files
- CRTDUPOBJ: Added handling of new obj with Qtemp library
- CHGDTAARA: Increased data area max length from 256 to 2000
- SAVOBJ: Ensure records saved are in insertion order
- RTVDTAARA: Values retrieved (not to be trimmed)
- CHKOBJ: Returns correct monitor messages when member does not exist
- RTVDTAARA: Added support of LDA substring
- RTVDTAARA: Returns whitespaces up to the length of variable specified in the RTNVAR
  param
- RTVDTAARA: Supports integer parameters for start and length and support latest
  transformation format
- CHGDTAARA: Added support for parameter that includes lower and upper bounds
- CHKOBJ: Handles VIEW value for parameter object type
- CHKOBJ: result set to true irrespective of member if the view exists

### Transversal capabilities

**New features**

- Handles generating reports to .txt files
- Added currentSchema XA datasource property to secret manager
- Add database.cursor.raise.already.opened.error YAML property to enable framework to raise
  SQLCODE error 502 when already opened cursor is opening

**Improvements**

- Added gapwalk poms to AWS Blu Age on Amazon EC2 packaging
- Uses the new signal handler paradigm by default
- Add support for lock when disposition is MOD or OLD
- Added cache to store database date time patterns
- Improved check function of PackedType
- Improve DataUtils.setTo functions for Records with VariableSizeArray
- Handles MQ SYNCPOINT option as regard as run unit
- Enabled framework to set SQLCODE on rollback transaction
- Added automatic driver class name according to engine key secret
- Program/Transaction timeout
- Restore cursor position after Rollback when accessing cursor

**Third party**

- Upgrade SnakeYAML, Redisson and Amazon SDK, remove YamlBeans (mitigate CVE-2022-25857,
  CVE-2023-24621, CVE-2023-42809, CVE-2023-44487)

## Modernization tools release 3.9.0

### zOS

**Improvements**

- Enhanced support for XML-TEXT as source for target of type String
- Enhanced STM to UML workflow to support X/(Y/Z) division pattern
- JHDB DB: Accepts ROLLBACK call before any database update
- JHDB DB: Accepts ROLLBACK even if transaction is terminated (NOP)
- JCL: Improved step validation function
- SORT: Handles SUM function with zone decimal negative values
- COBOL: Adds support for single/double quote escaping in string literals

### AS400

**Improvements**

- Improved built-in function %editc handling of edit code X by adding leading zeros
- Improved handling of input only fields initial value
- Added action keys to help dialogs
- Footer record of dynamic table appearing at the bottom
- Handled START command without KEY PHASE for files that specify an actual
  RECORD-KEY
- Added default value for float and NumberUtils::pow type
- Added support defining a variable using LIKE(IN)
- Updated FOR loop handling to support omitting optional elements
- Updated RPG parsing to associate records with CTDATA array name
- Improved handling of indicators for CABxx statements
- Supports optional parameter on COMMIT keyword
- Improved FORMAT Keyword support in LF
- Managed LOOKUP operation code with high and equal (or low and equal) indicators
- Handled PF key name declared within double quotes
- Improved the handling of EDTCDE X to not suppress leading zeroes
- Improved support for MSGCON in printer file not generating unnamed labels
- Field CONTENT is shared by multiple data structures
- Handled ERRSFL parameter in combination with SFLMSG/SFLMSGID
- Improved main code before proc declaration scope of full free rpg
- Added parsing conditioned control specification
- Improved support for setErrSfl() method in dataholdermapper
- Improved type resolution for internally created variables
- Improved support for Z-ADD opcode
- Improved the handling of constant field with DFT value
- Improve the support of integer field inside program status ds
- Handled indicator assignment in ENTRY params
- Improved the filter of keywords propagated through ref/reffield keyword
- Supported unnamed DataArea data structure
- Improved handling of pointer data type
- Handled elements of array used to define variables with LIKE keyword support array access
  in output field
- Improved support for signed numeric, only displaying digits
- Supported logical relationship on O card
- Test case for %CHAR on alphanumeric
- Supported control specification keyword main
- EDTCDE with two parameters in printer file
- Improved FullFreeRPG parsing
- Enhanced the dynamic table to ensure the footer is correctly positioned
- Added support for initializing numeric types with ALL figurative constant
- Improved handling of multiple RPG logical files referencing the same physical file
- Improve the detection of modified fields in a modern screen
- Modal synchronization with dynamic fields
- Improved the handling of output only signed numeric field
- Improve WORKSTATION I/O cards supports

### Transversal capabilities

**New features**

- Data Migrator Tool: Added ebcdicFilesWithVarcharInVB property to allow taking VARCHAR
  2-byte length into account when reading bytes
- Implemented a common API to log error
- Implementation of BluAgeErrorDictionaryUtils and use of common API to log error and/or
  info in COBOL2Model, RPGCycleBuilder, Definitions2Model and FieldsProcessor
- Improved SQL grammar to support different isolation clause definition

**Improvements**

- Upgraded Angular version to v16
- Angular: Upgraded ajv version from 6 to 8.9

**Third party**

- Upgraded Groovy to version 2.4.15

## Release notes 3.8.0

This release of AWS Blu Age Runtime and Modernization Tools is focused on multiple transversal
enhancements across the product to improve its quality and security, along with improvements in
performance for caching and the unification of commands supports in a single distribution. Some
key features and changes in this release are:

- Version upgrade from Spring 2.5 to Spring 2.7, increasing the maintenance support,
  performance, and security of the platform.
- Unification of more than 82 CL commands support as part of the over-the-counter
  distribution in order to facilitate the usage and deployment of modernized applications
  previously using CL scripting.
- New APIs available to operate and interact better with <noloc>Blusam</noloc>
  datasets, such as integrated import to the managed service and the capability to list dataset
  metadata information.
- Performance improvements and extension of the usage of Redis, including availability in
  cluster mode, high availability data retrieval, standardization of the usage of secrets.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.8.0

### zOS

**New features**

- Handling key definition as a string for DynamicFileBuilder
- DFSORT: Added support for multi-items in OUTFIL TRAILER1 + DFSORT grammar
  initialization
- CommonDDUtils tool: handling record size in in-stream data
- Indexed file: handling the GENKEY option

**Improvements**

- Externalized <noloc>Blusam</noloc> loading services in a separate jar
- Added support to set up location for storing temporary files
- Improved shared cache mechanisms for multi-nodes cases
- Shared cache usage: IDCAMS verify optimization
- Improve ROWID injection for embedded select
- JCL: Each in-stream job procedure is now generated in a distinct Groovy file
- Ensure card-demo-v2 coverage on IDCAMS JCL cards
- <noloc>Blusam</noloc>: Avoid duplicate warmUp when using multiple instances
- Reduced memory footprint on cache hydration
- Jedis pool config support
- Added line separator to stream if used in file concatenation
- Support for EBCDIC cards + block comments (/\* ... /) in IDCAMS utility
- Database support query: support for double byte strings in the conversion of level49
  towards SQL
- DFSORT grammar: implements 17 control statements + integration of 2 of them
  (OMIT/INCLUDE)
- Enhance GRAPHIC columns fetch INFUTILB
- Support for reading file with variable Size table
- Support for ZonedType with nibble signed where the first bit of last byte is 'E'
- DFSORT/ICETOOL adds support for NOMATCH=(..) argument if a record does not match any of
  the CHANGE find constants
- Redis Cluster compatibility
- Handling Job Status (Failed) based on groovy exit code
- Improved CICS SYNCPOINT ROLLBACK support.
- Pre-fetch window to optimize Redis cache usage
- JCL/GROOVY: Inherits isRDW property from previous step's dataset when DISP=(,PASS)
- Handling partial copy of data with variable size array

### AS400

**New features**

- Support for I/O cards for display files
- Support for additional message information for DSPF keywords ERRMSGID and CHKMSGID
- Support for multiple error messages on frontend screen
- Added or improved support of 82 CL commands within the gapwalk-cl-command
  application

**Improvements**

- Improved support for DELETE and READ under commitment control
- ConvertDate inside of builtin %dec
- Enforced XSS security headers
- Improved robustness and consistency of STM generation (better handling of: continuation
  line in free form rpg, commas for decimal part, free form blocks in
  definition/declaration)
- Improved DataHolderMapper generation
- Added robustness and change scope in DataAreaFactory
- Improved the focus shifting on tab key
- Improved performance on Jasper report generation
- Improved decimal display with padding 0s
- Improved support for ROW/COL field in INFDS
- Improve support for modified fields from the screen
- Added getters for generated report name and path
- Improved on Dataqueue length
- Improved autoconfiguration of Job Queues to match new standards in Spring Boot 2.7
- Improved workstation updates for multiple concurrent sessions

### Transversal capabilities

**New features**

- Support for No Invalid Data Tolerance for Packed
- Added pagination/filtering to list dataset endpoints

**Improvements**

- Enhanced ORACLE query transformation strategy in column comparison against empty
  string
- Handling BLOB DB2 with DSNTEP and INFUTILB utility programs. BLOB DB2 are now modernized
  to BYTEA type postgres.
- Improvement of deletion of last item of cursor
- Enhanced support for delete RRDS file
- Improved AWS <noloc>Blusam</noloc> secret performance
- Improved handling of database connections in SQL framework
- Standardized AWS multi-datasource secret manager keys
- Performance regression fixes
- Improved check function for PackedType
- Improved handling of LOW-VALUE for PackedType
- Upgraded spring security packaging for cognito connection
- Not applying codeshiftpoint encoding and decoding on DB2 targeted databases

**Third party**

- Spring Boot upgrade from 2.5 to 2.7

## Modernization tools release 3.8.0

### zOS

**New features**

- JCL: Handling stream with carriage return "\r"

**Improvements**

- Improved logging to prevent division by zero when modernizing a DIVIDE with ON SIZE ERROR
  clause
- JCL: Enhanced support for calling a procedure in a procedure
- Support for OF keyword in FORMATTIME CICS command when there are ambiguous fields
- JCL: support for Â¥ character in variables
- JCL: computing RC based on previous steps
- Comparing bytes instead of strings when PL1 SUBSTR is used
- Improvement of initialization of multidimensional arrays from single source
- Improved parsing of COBOL when it involves a single SQL query in an IF block

### AS400

**New features**

- Support for nested IF statement in CL
- Improved support for ENDDO statement in RPG freeform

**Improvements**

- Improved support for conditioning Control Level
- Improved prototype return with LIKE
- Improved support for handling functions %months, %year, %days
- Support for help feature for the whole screen
- Handling figurative BLANKS passed as a parameter
- Improvement on expression EVAL with "" operator
- Handling START command without KEY PHASE
- Improvement on handling the Keyword LIKEREC
- Improvement on unnamed subfields
- Improvement on procedure returning an unsigned type
- Improved support for RESET operation (Free RPG), %CHAR and %DEC built-ins
- Improvement in the builtin function %LOOKUPXX
- Improved support for LIKEDS keyword on procedure without prototype
- Handling Dim keyword array type (VAR, AUTO)
- Improved support for XFOOT
- COBOL: improved support for RENAMES fields
- CL: support while(true) condition
- Improved the handling of standalone arrays with LIKE keyword
- Improvement of built-in function %INT
- Improved RPG Full Free parsing
- Improved support for array in the linkage
- CL2GROOVY: Support Select Statement
- Improvement in DSPF keyword "ERRMSGID"
- Improved the handling of initializing bytes with leading zeroes
- Improvement on authorizedValues for numerical fields
- Handling extender H for Free form EVAL statement
- CL to Groovy: Support substring of LDA
- Improved support for RESET on a record
- Improved the handling of EDTCDE and EDTWRD with references
- Improved input-field mapping with DDS fields
- Improvedsupport for MOVEA character into IN array
- Improvement in prototype with LIKEDS keyword
- Improved support for the DSPF keyword DSPATR
- Improved parsing of D-card with +/-
- Added robustness in program calls
- Added robustness in the field-resolving process

### Transversal capabilities

**Improvements**

- FrontEnd: Simulate paste event for IME input

**Third party**

- Spring Boot upgrade from 2.5 to 2.7

## Release notes 3.7.0

This release of AWS Blu Age Runtime and Modernization Tools mainly includes enhancements to better
support commands and utilities, capabilities to integrate with AWS Secrets Manager and new
monitoring features. Some of the key changes in this release are:

- Multiple runtime components can now use AWS Secrets Manager to increase the security setup
  of modernized applications, mostly related to utilities data sources, Redis for TS Queues,
  <noloc>Blusam</noloc> cache and locks.
- Monitoring endpoint that allows to retrieve transaction, batch, and JVM metrics for
  resource usage optimization and operational management, such as status, duration, volume, and
  others.
- New features to support IBM MQ calls in RPG, and increased JCL SORT and IDCAMS
  transformation coverage.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.7.0

###### Topics

- [zOS](#runtime-zos "#runtime-zos")
- [AS400](#runtime-as400 "#runtime-as400")
- [Transversal capabilities](#runtime-transversal "#runtime-transversal")

### zOS

**New features**

- Improve parsing queries involved in program utility application by using SQL like
  grammar. (V7-9401)
- Handle indexed Variable Size Array when offset (V7-9904)
- Support INSERT SQL TIME column into DB2 with 24:00:00 hour format (V7-10023)
- Support INSERT SQL query from arrays with FOR ROWS and ATOMIC options (V7-10105)
- JCL SORT - enhance TranscodeTool to support OUTREC with IFTHEN (V7-10124)
- JCL SORT - add support for DATE keyword in OUTREC command (V7-10125)
- JCL - add support of In-Stream procedures (V7-10223)

**Improvements**

- A dataset marked with the "PASS" disposition should be available across all job steps
  (V7-9504)
- Support JCL attribute SCHENV (V7-9570)
- Support SEND with CTLCHAR option (V7-9714)
- COBOL - Handle different line separator charsets in ACCEPT statements (V7-9875)
- Avoid multiple rollback (V7-9958)
- Allow use of MOD disposition to append at the end of GDG files (V7-10031)
- Optimization: putAll refactoring (V7-10063)
- PutAll refactoring: adding pagination (V7-10063)
- Make Jedis client read timeout configurable (V7-10063)
- UseSsl support for standalone mode (V7-10114)
- Support EIBDS after opening file successfully (V7-10147)
- Support EIBDS after a file control request (V7-10147)
- Improve CICS SYNCPOINT support (V7-10187)
- BluesamRedisSerializer: issue with metadataPersistence (V7-10202)
- Support Redis AWS Secrets Manager for TS queues (V7-10204)
- Support JCLBCICS on customizing DD name size (V7-10224)
- Adds support for absolute path in IDCAMS DELETE statement (V7-10308)

### AS400

**New features**

- Implementation of the help feature for AS400 screens (V7-9673)

**Improvements**

- Number of records in INFDS (V7-9377)

### Transversal capabilities

**New features**

- Support for Runtime on EC2 to send logs to Amazon CloudWatch (D87990246)
- Added new endpoint to retrieve metrics about batches, transactions, and JVM
  (D88393832)

**Improvements**

- Support datasources AWS Secrets Manager for utility pgm (V7-9570)
- Added Db2 support for DSNUTILB DISCARD (V7-9798)
- Support for writing into logger instead of default system output stream in default
  SYSPRINT and SYSPUNCH files (V7-10098)
- Support <noloc>Blusam</noloc> Redis cache and locks connection properties in AWS
  Secrets Manager (V7-10238)
- Support for SSL connection on Db2 XA AWS secret (V7-10258)
- Updated metadata for IDCAMS REPRO and VERIFY (V7-10281)
- Improved IDCAMS Abend Return Code Management (V7-10307)

## Modernization tools release 3.7.0

###### Topics

- [zOS](#modernization-zos "#modernization-zos")
- [AS400](#modernization-as400 "#modernization-as400")
- [Transversal capabilities](#modernization-transversal "#modernization-transversal")

### zOS

**New features**

- PLI - Improved assignment for array cross section and two-dimensional arrays (V7-9830)

### AS400

**New features**

- Handling of control level indicators (V7-9227)
- Support for EXTNAME parameter \*INPUT (V7-9897)
- Enhanced Goto Rewriting: Support for tags located in SELECT OTHER statements
  (V7-9973)
- Support REFSHIT DSPF keyword (V7-10049)

**Improvements**

- Improvement on handling file description keyword EXTIND(\*INUx) (V7-7404)
- Improved SQLDDS file transformation (V7-7687)
- File objects no longer generated for AS400 files (V7-9062)
- Improved handling of file description keyword EXTDESC (V7-9268)
- Improved handling of %CHAR builtin (V7-9311)
- Improved support for pagedown on last record without SFLEND (V7-9322)
- Improved support for prefixed data structures (V7-9436)
- Support for dimension defined with %SIZE (V7-9472)
- Support for handling PF field name declared within double quotes (V7-9557)
- Improved file operation - case insensitive (V7-9785)
- Support for field initialized to \*USER (V7-9806)
- Support for COMP type in AS400 (V7-9840)
- Improved COBOL400 parsing on (Not)InvalidKey (V7-9922)
- Improved handling of SCAN operation (V7-9971)
- Improved support of GOTO opcode (V7-9973)
- Improved handling of EXCEPT operation (V7-9977)
- Improved prefix support (V7-10000)
- Support for MQ calls in RPG (V7-10007)
- Improved %LOOKUP builtin (keyed array data structure) (V7-10022)
- Support for Close \*All operation (V7-10036)
- Support for UPDATE AS ROW CHANGE SQLDDS statement (V7-10051)
- Improvement to handle literal value type Long (V7-10073)
- Improved RPG grammar (the use of the keyword INZ as name of subroutine) (V7-10074)
- Improved RPG grammar to support numeric values with empty fractional part
  (V7-10077)
- Improved support for fields shared between CL and external file (V7-10081)
- Improved support for DDS conditional indicators (V7-10084)
- Support for DDS binary type with COBOL programs (V7-10100)
- Improved name collision with linkage (V7-10109)
- Support for mixing main and export procedures (V7-10112)
- Improved support for DataStructure in a sub-procedure (V7-10113)
- Improved support of CLEAR (V7-10126)
- Improved support of DO loop (V7-10134)
- Support SQLTYPE in Full-Free RPG (V7-10151)
- Improved parsing of conditions on DDS keyword (V7-10155)
- Improved DSL generation (V7-10163)
- Improvement for processIndicators when the condition is a binary expression.
  (V7-10164)
- Improved GOTOs with Else condition (V7-10168)
- Support for type Time and Timestamp in DSPF (V7-10173)
- Improved parsing of continuation line for DDS (V7-10183)
- COBOL support for RENAMES FLD OF RECORD (V7-10195)
- Improved conditional indicator parsing on DSPF fields (V7-10221)
- Support parsing of DDS keyword NOALTSEQ (V7-10288)
- Support Help menu and hidden fields (V7-10314)
- Improved DSPF help keyword sanity check (V7-10328)
- No longer propagating all keywords on Ref field (V7-10347)

### Transversal capabilities

**New features**

- Data Migrator - Handling CLOB data (V7-9665)

**Improvements**

- Propagating JCL property SCHENV from JOB to PROC GROOVY definition through JobContext
  (V7-10225)
- FrontEnd - Adjusting window size in case of no border (V7-10358)

## Release notes 3.6.0

This release of AWS Blu Age Runtime and Modernization Tools provides new features for both zOS and
AS400 legacy migrations, mainly oriented to expanding CICS support mechanisms, complementing JCL
capabilities, optimizing performance in concurrent and high-volume features, and adding
multi-data-source capabilities. Some of the key changes in this release are:

- Enhancement of JCL dynamic file handling, expansion of current statements and management
  of concatenated datasets, execution of multiple statements in a single block, and data transfer
  from batches to programs.
- Enhanced support of multiple CICS commands, including inquiry for several CICS resource
  types.
- The capability to have different databases when using Blu Age Runtime Utilities, best
  suited for scenarios when business data is distributed across multiple sources.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.6.0

###### Topics

- [zOS](#runtime-zos "#runtime-zos")
- [AS400](#runtime-as400 "#runtime-as400")
- [Transversal capabilities](#runtime-transversal "#runtime-transversal")

### zOS

**New features**

- JCL - DynamicFileBuilder - Enhanced file-handle management (V7-9408)
- Enhanced format conversion on some built-in SQL DB2 functions when calling the INFUTILB
  UNLOAD utility (V7-9554)
- Enhanced PLI multi-dimensional array assignments (V7-9592)
- Handling of sysout redirect to file (V7-9992)

**Improvements**

- Add triggering of stored procedures for DB2 RDBMS (V7-9155)
- SORT handles conversion to PDF format (V7-9286)
- JCL/GROOVY - Enhance REPRO statement to support DUMMY datasets (V7-9424)
- Improve CICS UNLOCK support (V7-9606)
- Handle default value size for Union (V7-9648)
- JCL/GROOVY handle different termination/disposition in concatenated datasets
  (V7-9653)
- Make pageSize configurable for <noloc>Blusam</noloc> datasets (V7-9680)
- DSNUTIL - allow loading of 24:00:00 as valid TIME in DB2LUW (V7-9697)
- Support HIGH-VALUES (0xff) comparison in NumberUtils.ne() / NumberUtils.eq()
  (V7-9731)
- JCL/GROOVY - support DO ... THEN keywords in IDCAMS IF-THEN-ELSE clauses to execute
  multiple statements in a single block (V7-9750)
- Invalid JHDB called program outside JHDBBatchRunner (V7-9782)
- Support whitespace characters in SORT OUTFIL control card (V7-9808)
- Improve CICS READ PREV support (V7-9845)
- Improve concurrent access for dataset indexes (V7-9864)
- Improve CICS REWRITE support (V7-9873)
- COBOL - support for multi line SYSIN in ACCEPT statements to pass data from batch (JCL)
  to a program (COBOL) (V7-9875)
- Groovy - Better handling of ConcatenatedFileConfiguration at files creation step
  (V7-9876)
- IDCAMS UTILITY - Handling of DEFINE PATH statement (V7-9878)
- SORT BUILD - Adjust TRAN option and handle implicit blanks (V7-9925)
- Improve CICS DELETE with GENERIC option support (V7-9939)
- Improve CICS STARTBR and ENDBR support (V7-9952)
- Improve close performance on concurrent access (V7-9953)
- Improve file status handling on start (V7-9991)
- Groovy - Allow call of getDisposition()/getNormalTermination()/getAbnormalTermination()
  on ConcatenatedFileConfiguration (V7-10012)

### AS400

**New features**

- Support external indicators on COMMIT keywords (V7-6035)
- Reset ReadC loop after SFLCTL write (V7-8061)
- Support LR indicator in CALL (V7-9250)
- Add new type of dynamic-field (split) to handle input field on multiple lines
  (V7-9370)
- Support primary/secondary file (V7-9390)
- Local Data Area are now passed to the called job when submitting a job (V7-9775)
- Support of QTEMP for data area and support of datarea value creation. (V7-9916)
- Commitment Control - support for enable/disable commitment control (V7-9956)
- Support external indicators on COMMIT keywords

**Improvements**

- Improve 0 value display and EDTWRD (V7-8933)
- Support of DSPF keyword "CHKMSGID" (V7-9125)
- SQL commit transaction upon batch termination (V7-9232)
- Improve support of keywords EXPORT and IMPORT for field and datastructure
  (V7-9265)
- Support lower case in DateHelper (V7-9461)
- Support conversion \*CYMD to \*ISO (numeric) (V7-9488)
- Improve the handle of built-in %len for a varying field (left-hand and right-hand side of
  an expression) (V7-9733)
- Improve support for built-in functions '%LOOKUPXX' XX ("LE","LT","GE","GT")
  (V7-10064)

### Transversal capabilities

**New features**

- CICS - Improve Inquire transaction for option status (V7-9712)
- JCL - Improve Load for sysprint with system out file (V7-9797)
- CICS - Improve INQUIRE TSQUEUE (V7-9823)
- CICS - Improve Inquire terminal for option userid (V7-9906)

**Improvements**

- Improve the handle of the comparison with blank (V7-8047)
- Improve logging for Jics and <noloc>Blusam</noloc> (V7-8847)
- Support BMS extended attributes SOSI and programmed symbol F8 for dynamic fields
  (V7-8857)
- Handle buffer overflow in program parameter (V7-9138)
- Improve threads write concurrency for <noloc>Blusam</noloc> locks registry
  (V7-9505)
- Support multiple datasources configuration for Utility-pgm (V7-9570)
- <noloc>Blusam</noloc> record level locking only mode (V7-9626)
- Ensure metadata persistence resists to server restart (V7-9748)
- Improve DAO clean-up on exception (Browser Close) (V7-9790)
- Support DummyFile for INFUTILB SYSPUNCH (V7-9799)
- Enhance support for negative values on NumericEditedType (V7-9935)

## Modernization tools release 3.6.0

###### Topics

- [zOS](#modernization-zos "#modernization-zos")
- [AS400](#modernization-as400 "#modernization-as400")
- [Transversal capabilities](#modernization-transversal "#modernization-transversal")

### zOS

**New features**

- JCL - Enhance logging for end of procedure (V7-8509)
- PL1 - Enhance bags generation for data type PakedLong (V7-8917)
- JCL - Enhance logging for end of procedure when the file contains the "end" marker //
  (V7-9509)
- PL1 - Enhance support for GET EDIT with Fixed-point and SYSIN stream (V7-9593)
- DB2 - Enhance support for VARGRAPHIC DB2 type (V7-9809)
- CICS - Improve command QUERY SECURITY for option LOGMESSAGE (V7-9969)
- PL1 - Improve bags generation for CHARG/chargraphic built-in (V7-9989)

**Improvements**

- PL1- Enhance support for INCLUDEX keyword (V7-9588)
- PL/I - Handle CHARGRAPHIC keyword as a valid parameter of any method call
  (V7-9589)
- Improving PL1 host variable resolution when named with specific characters @ # $ §.
  (V7-9654)
- COBOL - Support of C01...C12 & S01...S05 keywords as parameter of WRITE ADVANCING
  statement at parsing step (V7-9669)

### AS400

**New features**

- Support SQL-DDS transformation in Analyzer (V7-7687)
- Automate SQL-DDS file detection (V7-7687)
- Implementation of SQL-DDS preprocessing (V7-7687)
- Support ALIGN keyword (V7-9254)
- Support ExtName to DSPF and multi-dim array (V7-9663)
- Support InvalidKey statements on COBOL WRITE (V7-9793)

**Improvements**

- Improvement on TESTB opcode (V7-8865)
- Improve support of DECFMT on focus (V7-8933)
- Handling resulting indicator on MOVE (V7-9224)
- Improve support of keyword TEMPLATE for field and datastructure (V7-9278)
- Improvement of LIKEDS (DS defined using LIKEDS is automatically qualified)
  (V7-9302)
- COBOL - Improve generation of indicators structure (V7-9423)
- Const parameter in prototype is not read-only (V7-9437)
- Improve EDTCDE keyword with edit code "Y" (V7-9443)
- Support generation of \*ROUTINE field in PSDS and INFDS (V7-9487)
- Improve rewriting field XXX to standalone (default value is lost while rewriting)
  (V7-9522)
- Improve Support of DSPF keywords (V7-9658)
- Handling ZEROES default value on binary (V7-9666)
- Support implicit pointer (V7-9719)
- Improve the handling of built-in call %size with one parameter (V7-9730)
- Improve the handling of datastructure references in built-in calls (%ELEM)
  (V7-9736)
- Improve the handling of signed length for field with LIKE reference in definition
  specification (V7-9738)
- Improvement on REWRITE (V7-9791)
- Improvement of the generation of indexes from DDS files (V7-9803)
- Improve mappers robustness with invalid numeric value (V7-9813)
- Improve SQLModel and allIndexes files generation (V7-9818)
- Improve qualified DS support (V7-9863)
- Improve support of LOOKUP (with a standalone field LIKE a DS in parameter)
  (V7-9961)
- Improve LIKE on indicator (V7-9985)
- Handling resulting indicator on MVR (V7-9995)
- Support character N with tilde (V7-10021)
- Improve modern DDL files generation from SQLDDS legacy files (V7-10067)

### Transversal capabilities

**New features**

- Customize resource location with a yml property (D88816105)
- COBOL - Support of EXIT PERFORM statement to exit from an inline PERFORM without using a
  GO TO / PERFORM ... THROUGH (V7-9582)
- Specifying default legacy encoding to consider into global metadata. (V7-9883)

**Improvements**

- Improve mask generation (V7-9602)
- Improve context warm-up (V7-9621)
- Make Charset CUSTOM930 thread safe. (V7-9674)
- Improvement on MOVEA (V7-9773)

## Release notes 3.5.0

This release of AWS Blu Age Runtime and Modernization Tools provides new features for both zOS and
AS400 legacy migrations, mainly oriented to datasets and messaging optimization, as well as
extended Java capabilities as a resulting asset of the transformation process. Some of the key
changes in this release are:

- Capability of migrating CL programs to Java in addition to the pre-existent groovy scripts
  feature, to facilitate its integration with other modernized programs, and to simplify customer
  learning curve by unifying the resulting programming language.
- Time reduction and optimization of the performance of dataset loads in Redis with the new
  data bulk feature.
- Ability to operate and pass datasets within job steps to modernize traditional datasets
  behaviors.
- Extension of SQL migration to support VB input files and Java 11 simplified
  migration.
- Multiple new mechanisms for faster integration with IBM MQ including additional headers,
  extended GET/PUT support and automatic retrieve of queue metadata.
- REST Endpoint for datasets metadata and import datasets from S3 buckets.

For more information about the changes included in this release, see the following
sections.

## Runtime release 3.5.0

###### Topics

- [zOS](#runtime-zos "#runtime-zos")
- [AS400](#runtime-as400 "#runtime-as400")
- [Transversal capabilities](#runtime-transversal "#runtime-transversal")

### zOS

**New features**

- JCL SORT - Handle new keyword overlay (V7-9409)
- ZOS COBOL - enhance support of floating char (V7-9404)
- Port of RedisJicsTSQueue to RedisTemplate & ListOperations (V7-9212)
- ZOS JCL - enhance temporary directory's path with files directory if defined through
  UserDefinedParameters (V7-9012)
- Handle FUNCTION ORD-MAX with ALL (all array items) (V7-9366)
- Prefixed and human-readable keys are now used when storing TS Queues in Redis
  (V7-9212)
- Add get dataset endpoint for <noloc>Blusam</noloc> API
- JCL - ADD support for batch job with name involving special character like #
  (V7-9136)
- TSModel fetching is now robustly performed on demand (V7-9212)

**Improvements**

- Non-versioned INCLUDE support in LNK files (V7-6022)
- MQ - Enhance encoding support (V7-9652)
- Improving support for double bytes or mixed charsets for varying character type
  (V7-9596)
- JCL - Support of filesDirectory configuration in IDCAMS delete NONVSAM statements
  (V7-9609)
- Support bulk mode for ESDS and RRDS datasets loading from files (V7-8639)
- Handle the opening of empty ESDS in input mode. (V7-9287)
- Enhance DEFINE CLUSTER statement with ORD/UNORD abbreviation support (V7-9451)
- <noloc>Blusam</noloc> Redis lock performance improvements (V7-8639)
- Enhance DEFINE CLUSTER statement to support RECORDSIZE provided in DATA() argument scope
  (V7-9337)
- Adds support of BUFFERSPACE/UNIQUE attributes on DEFINE CLUSTER statements
  (V7-9419)
- Improve <noloc>Blusam</noloc> read operation for variable length record dataset.
  (V7-9391)
- CICS ADDRESS properly represents missing CWA as null (V7-9491)
- Remove Unnecessary write at end locks (V7-8639)
- Handle Redis cache template injection in cache (V7-9510)
- Decode correctly BPXWDYN parameter (V7-9417)
- Improvement on LISTCAT export consumption (V7-9201)
- Non-printable chars support in <noloc>Blusam</noloc> TS Queues name
  (V7-9212)
- Handle receive Map building for field with mapset null (V7-9486)
- Improve BluesamRelativeFile delete and rewrite operation for dynamic access mode.
  (V7-8989)

### AS400

**New features**

- Add a feature to generate CL files as Java programs through standard DS/STM pivot
  (V7-9427)
- Support Input File with ADD mode (V7-9378)
- Improved sort order and retrieval management to support cl command OPNQRYF (Open Query
  File) and added support of SHARE parameter in OverrideItem. (V7-9364)

**Improvements**

- Support SFLNXTCHG on UpdateSubfile (V7-8061)
- Modify scope of CL context when run CL command (V7-9624)
- Handle return code for program BPXWDYN (V7-9417)
- Clear local monitors. (V7-9624)
- Support of DSPF keyword RTNCSRLOC (V7-9389)
- setOnGreaterOrEqual() not setting Equal to 1 (V7-9342)
- Update fields cache on UpdateSubfileRecord (V7-9376)
- Improve Support SFLNXTCHG (V7-8061)

### Transversal capabilities

**New features**

- Ignore G prefix on literal graphic string. (V7-9420)
- ZOS COBOL - Enhance support of Fiedl.initialize() for some special structures
  (V7-9485)
- Allow initialization of context asynchronously to improve performance of program startup
  (V7-9446)
- SQL Release explicitly the opened prepare statement and ResulSet. (V7-9422)
- Enhance JMS MQ - support MQRFH2 for MQ PUT / V7-7085 - support of default queue manager
  (V7-9400)
- SQL Management - Enable Lambda conversions on parameters for SET commands
  (V7-9492)
- ZOS MQ JMS - Add support to MQCOMIT and MQBACK (V7-9399)
- ZOS IBMMQ - Enhance support to MQINQ (V7-9544)
- Handle CONCAT operation with byte instead of string when using double byte encoding.
  (V7-8932)
- ZOS IBMMQ - Enhance support of PUT command with options SET_ALL_CONTEXT (V7-9544)

**Improvements**

- Handle gdg file names with $ character (V7-9066)
- SQL Diagnostic return 1 as NUMBER clause when previous SQL statement is successful.
  (V7-9410)
- Outlining for field with non null length (V7-7536)
- Support built-in PL1 GRAPHIC function (V7-9245)
- MQ - Add support of version for MQGMO fields setting (V7-9500)
- JMS MQ GET - Message returned dataLength improvement (V7-9502)
- Set sqlerrd(3) with number of fetched items in ROWSET context. (V7-9371)

## Modernization tools release 3.5.0

###### Topics

- [zOS](#modernization-zos "#modernization-zos")
- [AS400](#modernization-as400 "#modernization-as400")
- [Transversal capabilities](#modernization-transversal "#modernization-transversal")

### zOS

**New features**

- ZOS PLI - Support asterisk index in assignment with binary expression (V7-9178)
- JCL to BatchScript - A "//" marks the end of job execution (V7-9304)
- ZOS PLI - enhance support of floating char and sign in numeric edited type
  (V7-8982)
- COBOL - Support of built-in SUM function (V7-9367)
- JCL- optionally, comment dead code after null statement (//) (V7-9202)
- JCL- Support of operator '|' in condition statement (V7-9499)
- PL/I - Comment of precompilation directives at preprocessing step to prevent parsing
  exceptions (V7-9507)

**Improvements**

- Handle Stream definition with delimiter (V7-9615)
- Improving LISTCAT exports handling. (V7-9201)
- PL/I- Enhancement to support implicit 'null' arguments (V7-9204)

### AS400

**New features**

- Support of DDS keyword CONCAT (V7-9439)
- Refactor the generated java code for DSPF keywords. (V7-7700)
- Support Varying keyword on fields within a data structure definition (V7-9029)

**Improvements**

- Improve parsing of logical relationship AND/OR (V7-9352)
- COBOL Improve mapping between vo and dsEntity (V7-9449)
- Display empty value if numerical input is focused (V7-9374)
- Local variable in SQL Declare Cursor (V7-9456)
- Scope problem with empty DS (V7-9466)
- Truncate lines after col 80 before parsing (V7-9632)
- Improve the handle of field references and built-in calls in keywords (DIM, LIKE,...) in
  definition specification (V7-9358)
- Support SQL comments (--) (V7-9632)
- FullFree parsing, type Date/Time/Timestamp (V7-9542)
- Include SQLCA from FullFree parsing (V7-9333)
- Improve Support of Control Level. (V7-9610)
- Handle DS comparison with \*BLANKS (V7-9668)
- Improve support of multiple indicators in DDS (V7-9318)
- Improve support of multiple DSPF programs (V7-9657)
- Improve the handle of field with LIKE (case of liked data structure and case of liked
  data structure in an array) (V7-9213)
- Free RPG, Handle continuation on literal (V7-9686)
- Improve Support of end of program records (V7-9452)
- Support of the LINKAGE phrase in the CALL statement. (V7-9685)
- CASXX operation code (CASBB without CASXX group) (V7-9357)
- Improve FullFreeRPG parsing (V7-9457)
- Built-in %LEN does not support DS as argument (V7-9267)
- Improvements of MOVEA when factor 2 is \*ALL'X...' (V7-9228)
- Support assign with RENAME field (V7-9385)

### Transversal capabilities

**New features**

- SQL Migrator tool - Add OID option for variable record length at ebcdic loading step.
  (V7-9380)
- SQL Migrator tool - Support for Java 11 on OID option (V7-9599)

**Improvements**

- Improve support for nested arrays (V7-9595)
- Replace Â¬ character by ! in case of Â¬ is supported by original encoding.
  (V7-9465)
- JCL - Support of PASS normal termination to share datasets between job steps
  (V7-9504)
- Apply ON NULL to column definition on ORACLE when deals with VARCHAR and nullable db
  column type. (V7-9681)
- Improve Spring injection compliance (V7-9635)
