Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Amazon Redshift RSQL error codes

Success messages, warnings, and exceptions:

| Error Code | Error Class                               | Condition Name                                           |
| ---------- | ----------------------------------------- | -------------------------------------------------------- |
| 00000      | Class 00 — Successful Completion          | successful\_completion                                   |
| 01000      | Class 01 — Warning                        | warning                                                  |
| 0100C      | Class 01 — Warning                        | dynamic\_result\_sets\_returned                          |
| 01008      | Class 01 — Warning                        | implicit\_zero\_bit\_padding                             |
| 01003      | Class 01 — Warning                        | null\_value\_eliminated\_in\_set\_function               |
| 01007      | Class 01 — Warning                        | privilege\_not\_granted                                  |
| 01006      | Class 01 — Warning                        | privilege\_not\_revoked                                  |
| 01004      | Class 01 — Warning                        | string\_data\_right\_truncation                          |
| 01P01      | Class 01 — Warning                        | deprecated\_feature                                      |
| 02000      | Class 02 — No Data                        | no\_data                                                 |
| 02001      | Class 02 — No Data                        | no\_additional\_dynamic\_result\_sets\_returned          |
| 03000      | Class 03 — SQL Statement Not Yet Complete | sql\_statement\_not\_yet\_complete                       |
| 08000      | Class 08 — Connection Exception           | connection\_exception                                    |
| 08003      | Class 08 — Connection Exception           | connection\_does\_not\_exist                             |
| 08006      | Class 08 — Connection Exception           | connection\_failure                                      |
| 08001      | Class 08 — Connection Exception           | sqlclient\_unable\_to\_establish\_sqlconnection          |
| 08004      | Class 08 — Connection Exception           | sqlserver\_rejected\_establishment\_of\_sqlconnection    |
| 08007      | Class 08 — Connection Exception           | transaction\_resolution\_unknown                         |
| 08P01      | Class 08 — Connection Exception           | protocol\_violation                                      |
| 09000      | Class 09 — Triggered Action Exception     | triggered\_action\_exception                             |
| 0A000      | Class 0A — Feature Not Supported          | feature\_not\_supported                                  |
| 0A000      | Class 0A — Feature Not Supported          | feature\_not\_supported                                  |
| 0B000      | Class 0B — Invalid Transaction Initiation | invalid\_transaction\_initiation                         |
| 0F000      | Class 0F — Locator Exception              | locator\_exception                                       |
| 0F001      | Class 0F — Locator Exception              | invalid\_locator\_specification                          |
| 0L000      | Class 0L — Invalid Grantor                | invalid\_grantor                                         |
| 0LP01      | Class 0L — Invalid Grantor                | invalid\_grant\_operation                                |
| 0P000      | Class 0P — Invalid Role Specification     | invalid\_role\_specification                             |
| 0Z000      | Class 0Z — Diagnostics Exception          | diagnostics\_exception                                   |
| 0Z002      | Class 0Z — Diagnostics Exception          | stacked\_diagnostics\_accessed\_without\_active\_handler |
| 20000      | Class 20 — Case Not Found                 | case\_not\_found                                         |
| 21000      | Class 21 — Cardinality Violation          | cardinality\_violation                                   |

Data exceptions:

| Error Code | Error Class               | Condition Name                                  |
| ---------- | ------------------------- | ----------------------------------------------- |
| 22000      | Class 22 — Data Exception | data\_exception                                 |
| 2202E      | Class 22 — Data Exception | array\_subscript\_error                         |
| 22021      | Class 22 — Data Exception | character\_not\_in\_repertoire                  |
| 22008      | Class 22 — Data Exception | datetime\_field\_overflow                       |
| 22012      | Class 22 — Data Exception | division\_by\_zero                              |
| 22005      | Class 01 — Warning        | error\_in\_assignment                           |
| 2200B      | Class 01 — Warning        | escape\_character\_conflict                     |
| 22022      | Class 01 — Warning        | indicator\_overflow                             |
| 22015      | Class 01 — Warning        | interval\_field\_overflow                       |
| 2201E      | Class 01 — Warning        | invalid\_argument\_for\_logarithm               |
| 2201F      | Class 01 — Warning        | invalid\_argument\_for\_power\_function         |
| 2201G      | Class 01 — Warning        | invalid\_argument\_for\_width\_bucket\_function |
| 22018      | Class 01 — Warning        | invalid\_character\_value\_for\_cast            |
| 22007      | Class 01 — Warning        | invalid\_datetime\_format                       |
| 22019      | Class 01 — Warning        | invalid\_escape\_character                      |
| 2200D      | Class 01 — Warning        | invalid\_escape\_octet                          |
| 22025      | Class 01 — Warning        | invalid\_escape\_sequence                       |
| 22P06      | Class 01 — Warning        | nonstandard\_use\_of\_escape\_character         |
| 22010      | Class 01 — Warning        | invalid\_indicator\_parameter\_value            |
| 22023      | Class 01 — Warning        | invalid\_parameter\_value                       |
| 2201B      | Class 01 — Warning        | invalid\_regular\_expression                    |
| 22009      | Class 01 — Warning        | invalid\_time\_zone\_displacement\_value        |
| 2200C      | Class 01 — Warning        | invalid\_use\_of\_escape\_character             |
| 2200G      | Class 01 — Warning        | most\_specific\_type\_mismatch                  |
| 22004      | Class 01 — Warning        | null\_value\_not\_allowed                       |
| 22002      | Class 01 — Warning        | null\_value\_no\_indicator\_parameter           |
| 22003      | Class 01 — Warning        | numeric\_value\_out\_of\_range                  |
| 22026      | Class 01 — Warning        | string\_data\_length\_mismatch                  |
| 22001      | Class 01 — Warning        | string\_data\_right\_truncation                 |
| 22011      | Class 01 — Warning        | substring\_error                                |
| 22027      | Class 01 — Warning        | trim\_error                                     |
| 22024      | Class 01 — Warning        | unterminated\_c\_string                         |
| 2200F      | Class 01 — Warning        | zero\_length\_character\_string                 |
| 22P01      | Class 01 — Warning        | floating\_point\_exception                      |
| 22P02      | Class 01 — Warning        | invalid\_text\_representation                   |
| 22P03      | Class 01 — Warning        | invalid\_binary\_representation                 |
| 22P04      | Class 01 — Warning        | bad\_copy\_file\_format                         |
| 22P05      | Class 01 — Warning        | untranslatable\_character                       |

Integrity constraint violations:

| Error Code | Error Class                                                | Condition Name                                            |
| ---------- | ---------------------------------------------------------- | --------------------------------------------------------- |
| 23000      | Class 23 — Integrity Constraint Violation                  | integrity\_constraint\_violation                          |
| 23001      | Class 23 — Integrity Constraint Violation                  | restrict\_violation                                       |
| 23502      | Class 23 — Integrity Constraint Violation                  | not\_null\_violation                                      |
| 23503      | Class 23 — Integrity Constraint Violation                  | foreign\_key\_violation                                   |
| 23505      | Class 23 — Integrity Constraint Violation                  | unique\_violation                                         |
| 23514      | Class 23 — Integrity Constraint Violation                  | check\_violation                                          |
| 24000      | Class 24 — Invalid Cursor State                            | invalid\_cursor\_state                                    |
| 01004      | Class 01 — Warning                                         | string\_data\_right\_truncation                           |
| 25000      | Class 25 — Invalid Transaction State                       | invalid\_transaction\_state                               |
| 25001      | Class 25 — Invalid Transaction State                       | active\_sql\_transaction                                  |
| 25002      | Class 25 — Invalid Transaction State                       | invalid\_transaction\_state                               |
| 25008      | Class 25 — Invalid Transaction State                       | held\_cursor\_requires\_same\_isolation\_level            |
| 25003      | Class 25 — Invalid Transaction State                       | inappropriate\_access\_mode\_for\_branch\_transaction     |
| 25004      | Class 25 — Invalid Transaction State                       | inappropriate\_isolation\_level\_for\_branch\_transaction |
| 25005      | Class 25 — Invalid Transaction State                       | no\_active\_sql\_transaction\_for\_branch\_transaction    |
| 25006      | Class 25 — Invalid Transaction State                       | read\_only\_sql\_transaction                              |
| 25007      | Class 25 — Invalid Transaction State                       | no\_active\_sql\_transaction\_for\_branch\_transaction    |
| 25P01      | Class 25 — Invalid Transaction State                       | no\_active\_sql\_transaction                              |
| 25P02      | Class 25 — Invalid Transaction State                       | in\_failed\_sql\_transaction                              |
| 26000      | Class 26 — Invalid SQL Statement Name                      | invalid\_sql\_statement\_name                             |
| 28000      | Class 28 — Invalid Authorization<br>Specification          | invalid\_authorization\_specification                     |
| 2B000      | Class 2B — Dependent Privilege Descriptors Still<br>Exist  | dependent\_privilege\_descriptors\_still\_exist           |
| 2BP01      | Class 2B — Dependent Privilege Descriptors Still<br>Exist  | dependent\_objects\_still\_exist                          |
| 2D000      | Class 2D — Invalid Transaction Termination                 | invalid\_transaction\_termination                         |
| 2F000      | Class 2F — SQL Routine Exception                           | sql\_routine\_exception                                   |
| 2F005      | Class 2F — SQL Routine Exception                           | function\_executed\_no\_return\_statement                 |
| 2F002      | Class 2F — SQL Routine Exception                           | modifying\_sql\_data\_not\_permitted                      |
| 2F003      | Class 2F — SQL Routine Exception                           | prohibited\_sql\_statement\_attempted                     |
| 2F004      | Class 2F — SQL Routine Exception                           | reading\_sql\_data\_not\_permitted                        |
| 34000      | Class 34 — Invalid Cursor Name                             | invalid\_cursor\_name                                     |
| 38000      | Class 38 — External Routine Exception                      | external\_routine\_exception                              |
| 38001      | Class 38 — External Routine Exception                      | containing\_sql\_not\_permitted                           |
| 38002      | Class 38 — External Routine Exception                      | modifying\_sql\_data\_not\_permitted                      |
| 38003      | Class 38 — External Routine Exception                      | prohibited\_sql\_statement\_attempted                     |
| 38004      | Class 38 — External Routine Exception                      | reading\_sql\_data\_not\_permitted                        |
| 39000      | Class 39 — External Routine Invocation<br>Exception        | external\_routine\_invocation\_exception                  |
| 39001      | Class 39 — External Routine Invocation<br>Exception        | invalid\_sqlstate\_returned                               |
| 39004      | Class 39 — External Routine Invocation<br>Exception        | null\_value\_not\_allowed                                 |
| 39P01      | Class 39 — External Routine Invocation<br>Exception        | trigger\_protocol\_violated                               |
| 39P02      | Class 39 — External Routine Invocation<br>Exception        | srf\_protocol\_violated                                   |
| 3D000      | Class 3D — Invalid Catalog Name                            | invalid\_catalog\_name                                    |
| 3F000      | Class 3F — Invalid Schema Name                             | invalid\_schema\_name                                     |
| 42000      | Class 42 — Syntax Error or Access Rule<br>Violation        | syntax\_error\_or\_access\_rule\_violation                |
| 42601      | Class 42 — Syntax Error or Access Rule<br>Violation        | syntax\_error                                             |
| 42501      | Class 42 — Syntax Error or Access Rule<br>Violation        | insufficient\_privilege                                   |
| 42846      | Class 42 — Syntax Error or Access Rule<br>Violation        | cannot\_coerce                                            |
| 42803      | Class 42 — Syntax Error or Access Rule<br>Violation        | grouping\_error                                           |
| 42830      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_foreign\_key                                     |
| 42602      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_name                                             |
| 42622      | Class 42 — Syntax Error or Access Rule<br>Violation        | name\_too\_long                                           |
| 42939      | Class 42 — Syntax Error or Access Rule<br>Violation        | reserved\_name                                            |
| 42804      | Class 42 — Syntax Error or Access Rule<br>Violation        | datatype\_mismatch                                        |
| 42P18      | Class 42 — Syntax Error or Access Rule<br>Violation        | indeterminate\_datatype                                   |
| 42809      | Class 42 — Syntax Error or Access Rule<br>Violation        | wrong\_object\_type                                       |
| 42703      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined\_column                                         |
| 42883      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined\_function                                       |
| 42P01      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined\_table                                          |
| 42P02      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined\_parameter                                      |
| 42704      | Class 42 — Syntax Error or Access Rule<br>Violation        | undefined\_object                                         |
| 42701      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_column                                         |
| 42P03      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_cursor                                         |
| 42P04      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_database                                       |
| 42723      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_function                                       |
| 42P05      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_prepared\_statement                            |
| 42P06      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_schema                                         |
| 42P07      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_table                                          |
| 42712      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_alias                                          |
| 42710      | Class 42 — Syntax Error or Access Rule<br>Violation        | duplicate\_object                                         |
| 42702      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous\_column                                         |
| 42725      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous\_function                                       |
| 42P08      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous\_parameter                                      |
| 42P09      | Class 42 — Syntax Error or Access Rule<br>Violation        | ambiguous\_alias                                          |
| 42P10      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_column\_reference                                |
| 42611      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_column\_definition                               |
| 42P11      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_cursor\_definition                               |
| 42P12      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_database\_definition                             |
| 42P13      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_function\_definition                             |
| 42P14      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_prepared\_statement\_definition                  |
| 42P15      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_schema\_definition                               |
| 42P16      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_table\_definition                                |
| 42P17      | Class 42 — Syntax Error or Access Rule<br>Violation        | invalid\_object\_definition                               |
| 44000      | Class 44 — WITH CHECK OPTION Violation                     | with\_check\_option\_violation                            |
| 53000      | Class 53 — Insufficient Resources                          | insufficient\_resources                                   |
| 53100      | Class 53 — Insufficient Resources                          | disk\_full                                                |
| 53200      | Class 53 — Insufficient Resources                          | out\_of\_memory                                           |
| 53300      | Class 53 — Insufficient Resources                          | too\_many\_connections                                    |
| 54000      | Class 54 — Program Limit Exceeded                          | program\_limit\_exceeded                                  |
| 54001      | Class 54 — Program Limit Exceeded                          | statement\_too\_complex                                   |
| 54011      | Class 54 — Program Limit Exceeded                          | too\_many\_columns                                        |
| 54023      | Class 54 — Program Limit Exceeded                          | too\_many\_arguments                                      |
| 55000      | Class 55 — Object Not In Prerequisite<br>State             | object\_not\_in\_prerequisite\_state                      |
| 55006      | Class 55 — Object Not In Prerequisite<br>State             | object\_in\_use                                           |
| 55P02      | Class 55 — Object Not In Prerequisite<br>State             | cant\_change\_runtime\_param                              |
| 55P03      | Class 55 — Object Not In Prerequisite<br>State             | lock\_not\_available                                      |
| 57000      | Class 57 — Operator Intervention                           | operator\_intervention                                    |
| 57014      | Class 57 — Operator Intervention                           | query\_canceled                                           |
| 57P01      | Class 57 — Operator Intervention                           | admin\_shutdown                                           |
| 57P02      | Class 57 — Operator Intervention                           | crash\_shutdown                                           |
| 57P03      | Class 57 — Operator Intervention                           | cannot\_connect\_now                                      |
| 58000      | Class 58 — System Error (errors external to<br>PostgreSQL) | system\_error                                             |
| 58030      | Class 58 — System Error (errors external to<br>PostgreSQL) | io\_error                                                 |
| 58P01      | Class 58 — System Error (errors external to<br>PostgreSQL) | undefined\_file                                           |
| 58P02      | Class 58 — System Error (errors external to<br>PostgreSQL) | duplicate\_file                                           |
| F0000      | Class F0 — Configuration File Error                        | duplicate\_file                                           |
| F0001      | Class F0 — Configuration File Error                        | lock\_file\_exists                                        |
| P0000      | Class P0 — PL/pgSQL Error                                  | plpgsql\_error                                            |
| P0001      | Class P0 — PL/pgSQL Error                                  | raise\_exception                                          |
| P0002      | Class P0 — PL/pgSQL Error                                  | no\_data\_found                                           |
| P0003      | Class P0 — PL/pgSQL Error                                  | too\_many\_rows                                           |
| XX000      | Class XX — Internal Error                                  | internal\_error                                           |
| XX001      | Class XX — Internal Error                                  | data\_corrupted                                           |
| XX002      | Class XX — Internal Error                                  | index\_corrupted                                          |
