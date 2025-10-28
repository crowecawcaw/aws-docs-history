# W3C_LOG_PARSE

````
 W3C_LOG_PARSE( <character-expression>, <format-string> )
 <format-string> := '<predefined-format> | <custom-format>'
 <predefined format> :=
         COMMON
| COMMON WITH VHOST
| NCSA EXTENDED
| REFERER
| AGENT
| IIS <custom-format> := [an Apache log format specifier] ``` ## W3C Predefined Formats Specifying the following W3C-predefined-format names summarizes using the format specifiers indicated, as shown in the following statement: ``` select stream W3C_LOG_PARSE(message, 'COMMON') r  from w3ccommon t; ```
| Format Name | W3C Name | Format Specifiers |
| --- | --- | --- |
| COMMON | Common Log Format (CLF) | %h %l %u %t "%r" %>s %b |
| COMMON WITH VHOST | Common Log Format with Virtual Host | %v %h %l %u %t "%r" %>s %b |
| NCSA EXTENDED | NCSA extended/combined log format | %h %l %u %t "%r" %>s %b "%[Referer]i" "%[User-agent]i" |
| REFERER | Referer log format | %[Referer]i ---> %U |
| AGENT | Agent (Browser) log format | %[User-agent]i | ## W3C Format Specifiers The format specifiers are listed below. W3C\_LOG\_PARSE automatically detects these specifiers and output records with one column for each specifier. The column's type is automatically chosen based on the possible outputs of the specifier. For example, %b represents the number of bytes sent in processing an HTTP request, so the column type is numeric. For %B, however, zero bytes is represented by a dash - forcing the column type to be text. Note A explains what the "..." and "<" or ">" markings shown in the specifier table mean. The following table lists W3C format specifiers alphabetically by command.
| Format Specifier | Explanation | | --- | --- |
| % | The percent sign (Apache 2.0.44 and later) | | %...a | Remote IP-address |
| %...A | Local IP-address | | %...B | Size of response in bytes, excluding HTTP headers. |
| %...b | Size of response in bytes, excluding HTTP headers, in CLF format, which means that when no bytes are sent, uses a '-' rather than a 0. | | %...[Customerdata]C | The contents of cookie Customerdata in the request sent to the server. |
| %...D | The time taken to serve the request, in microseconds. | | %...[CUSTOMERDATA]e | The contents of the environment variable CUSTOMERDATA |
| %...f | Filename | | %...h | Remote host |
| %...H | The request protocol | | %...[Customerdata]i | The contents of Customerdata: header line(s) in the request sent to the server. |
| %...l | Remote logname (from identd, if supplied) | | %...m | The request method |
| %...[Customerdata]n | The contents of note Customerdata from another module. | | %...[Customerdata]o | The contents of Customerdata: header line(s) in the reply. |
| %...p | The canonical port of the server serving the request | | %...P | The process ID of the child that serviced the request. |
| %...[format]P | The process ID or thread id of the child that serviced the request. Valid formats are pid and tid. (Apache 2.0.46 and later) | | %...q | The query string (prepended with a ? if a query string exists, otherwise an empty string) |
| %...r | First line of request | | %...s | Status. For requests that got internally redirected, this is the status of the \*original\* request --- %...>s for the last. |
| %...t | Time, in common log format time format (standard English format) | | %...[format]t | The time, in the form given by format, which should be in strimmer(3) format. (potentially localized) |
| %...T | The time taken to serve the request, in seconds. | | %...u | Remote user (from auth; may be bogus if return status (%s) is 401) |
| %...U | The URL path requested, not including any query string. | | %...v | The canonical ServerName of the server serving the request. |
| %...V | The server name according to the UseCanonicalName setting. | | %...X | Connection status when response is completed X = connection aborted before the response completed. + = connection may be kept alive after the response is sent. <br>• = connection will be closed after the response is sent. (The %..X directive was %...c in late versions of Apache 1.3, but this conflicted with the historical ssl %...[var]c syntax.) |
| :%...I: | Bytes received, including request and headers, cannot be zero. You need to enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html "http://httpd.apache.org/docs/2.0/mod/mod_logio.html") to use this. | | :%...O: | Bytes sent, including headers, cannot be zero. You need to enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html "http://httpd.apache.org/docs/2.0/mod/mod_logio.html") to use this. | ###### Note Some W3C format specifiers are shown as containing a "..." indication or a "<" or ">", which are optional controls on suppressing or redirecting the output of that specifier. The "..." can either be empty (as in the COMMON specification "\%h %u %r \%s %b") or it can indicate conditions for including the item. The conditions are a list of HTTP status codes, possibly preceded by "!", and if the specified condition is not met, then the column or field returned shows "-". For example, as described in the [Apache documentation](http://httpd.apache.org/docs/2.0/mod/mod_log_config.html "http://httpd.apache.org/docs/2.0/mod/mod_log_config.html"), specifying "%400,501[User-agent]i" will log the User-agent only on 400 errors and 501 errors (Bad Request, Not Implemented). Similarly, "%!200,304,302[Referer]i" will log the Referer: on all requests that fail to return some sort of normal status. The modifiers "<" and ">" can be used to choose whether the original or final (respectively) request should be consulted when a request has been internally redirected. By default, the % directives %s, %U, %T, %D, and %r look at the original request while all others look at the final request. So for example, %>s can be used to record the final status of the request and %<u can be used to record the original authenticated user on a request that is internally redirected to an unauthenticated resource. For security reasons, starting with Apache 2.0.46, non-printable and other special characters are escaped mostly by using \xhh sequences, where hh stands for the hexadecimal representation of the raw byte. Exceptions from this rule are " and \ which are escaped by prepending a backslash, and all white space characters which are written in their C-style notation (\n, \t etc). In httpd 2.0 versions prior to 2.0.46, no escaping was performed on the strings from %...r, %...i and %...o, so great care was needed when dealing with raw log files, since clients could have inserted control characters into the log. Also, in httpd 2.0, the B format strings represent simply the size in bytes of the HTTP response (which will differ, for instance, if the connection is aborted, or if SSL is used). For the actual number of bytes sent over the network to the client, use the %O format provided by [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html "http://httpd.apache.org/docs/2.0/mod/mod_logio.html"). ## W3C Format Specifiers by Function or Category The categories are bytes sent, connection status, content of environmental variable, filename, host, IP, notes, protocol, query string, replies, requests, and time. For the markings "..." or "<" or "<", see the previous note.
| Function or Category | W3C Format Specifiers | | --- | --- |
| **Bytes sent, excluding HTTP headers** | | with a "0" when no bytes are sent | %...B |
| with a "-" (CLF format) when no bytes are sent | %...b | | Bytes received, including request and headers, cannot be zero Must enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html "http://httpd.apache.org/docs/2.0/mod/mod_logio.html") to use this. | :% ... I: |
| Bytes sent, including headers, cannot be zero Must enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html "http://httpd.apache.org/docs/2.0/mod/mod_logio.html") to use this. | :%... O: | | **Connection status when response is completed** |
| Connection aborted before the response completed | X | | Connection may be kept alive after the response is sent | + |
| Connection will be closed after the response is sent | - | | NoteThe %..X directive was %...c in late versions of Apache 1.3, but this conflicted with the historical ssl %...[var]c syntax. |
| **Environment variable CUSTOMERDATA** | | contents | %...[CUSTOMERDATA]e |
| **Filename** | %...f | | **Host (remote)** | %...h |
| **Protocol** | %...H | | **IP addresses** |
| Remote | %...a | | Local | %...A |
| **Notes** | | Contents of note Customerdata from another module | %...[Customerdata]n |
| **Protocol (request)** | %...H | | **Query string** NoteIf query exists, prepended with a ?If not, the empty string. | %...q |
| **Replies** | | Contents of Customerdata (header lines in the reply) | %...[Customerdata]o | The W3C format specifiers for the response and time categories are listed following table.
| Function or Category | W3C Format Specifiers | | --- | --- |
| **Requests** | | Canonical port of the server serving the request | %...p |
| Contents of cookie Customerdata in the request sent to server | %... [Customerdata]C | | Contents of BAR:header line(s) | %... [BAR]i |
| First line sent: | %...r | | Microseconds taken to serve a request | %...D |
| Protocol | %...H | | Process ID of the child that serviced the request | %...P |
| Process ID or thread id of the child that serviced the request. Valid formats are pid and tid. (Apache 2.0.46 and later) | %...[format]P | | Remote logname (from identd, if supplied) | %...l |
| Remote user: (from auth; may be bogus if return status (%s) is 401) | %...u | | Server (canonical ServerName) serving the request | %...v |
| Server name by the UseCanonicalName setting | %...V | | Request method | %...m |
| Return status | %s | | Seconds taken to serve the request | %...T |
| Status of the \*original\* request that was internally redirected | %...s | | Status of the last request | %...>s |
| URL path requested, not including any query string | %...U | | **Time** |
| Common log format time format (standard English format) | %...t | | Time in strftime(3) format, potentially localized | %...[format]t |
| Seconds taken to serve the request | %...T | ## W3C Examples W3C\_LOG\_PARSE supports access to logs generated by W3C-compliant applications like the Apache web server, producing output rows with one column for each specifier. The data types are derived from the log entry description specifiers listed in the [Apache mod\_log\_config](http://httpd.apache.org/docs/2.0/mod/mod_log_config.html?#formats "http://httpd.apache.org/docs/2.0/mod/mod_log_config.html?#formats") specification. ## Example 1 The input in this example is taken from an Apache log file and is representative of the COMMON log format. ### Input ``` (192.168.254.30 - John [24/May/2004:22:01:02 -0700] "GET /icons/apache_pb.gif HTTP/1.1" 304 0), (192.168.254.30 - Jane [24/May/2004:22:01:02 -0700] "GET /icons/small/dir.gif HTTP/1.1" 304 0); ``` ### DDL ``` CREATE OR REPLACE PUMP weblog AS SELECT STREAM l.r.COLUMN1, l.r.COLUMN2, l.r.COLUMN3, l.r.COLUMN4, l.r.COLUMN5, l.r.COLUMN6, l.r.COLUMN7 FROM (SELECT STREAM W3C_LOG_PARSE(message, 'COMMON') FROM "weblog_read) AS l(r); ``` ### Output ``` 192.168.254.30 -  John  [24/May/2004:22:01:02 -0700] GET /icons/apache_pb.gif HTTP/1.1  304  0 192.168.254.30 -  Jane  [24/May/2004:22:01:02 -0700] GET /icons/small/dir.gif HTTP/1.1  304  0 ``` ### The specification of COMMON in the FROM clause means the Common Log Format (CLF), which uses the specifiers %h %l %u %t "%r" %>s %b. The [W3C-predefined formats](sql-reference-w3c-log-parse.md#sql-reference-w3c-log-parse-predefined "sql-reference-w3c-log-parse.md#sql-reference-w3c-log-parse-predefined") shows the COMMON and other predefined specifier sets. The specification of COMMON in the FROM clause means the Common Log Format (CLF), which uses the specifiers %h %l %u %t "%r" %>s %b. The table below, Specifiers used by the Common Log Format, describes the specifiers used by COMMON in the FROM clause. ## Specifiers Used by the Common Log Format
| Output Column | Format Specifier | Returns |
| --- | --- | --- |
| COLUMN1 | %h | The IP address of the remote host |
| COLUMN2 | %l | The remote logname |
| COLUMN3 | %u | The remote user |
| COLUMN4 | %t | The time |
| COLUMN5 | "%r" | The first line of the request |
| COLUMN6 | %>s | The status: For internally redirected requests, the status of the \*original\* request --- %...>s for the last. |
| COLUMN7 | %b | The number of bytes sent, excluding HTTP headers | ## Example 2 The DDL in this example shows how to rename output columns and filter out unneeded columns. ### DDL ``` CREATE OR REPLACE VIEW "Schema1".weblogreduced AS SELECT STREAM CAST(s.COLUMN3 AS VARCHAR(5)) AS LOG_USER, CAST(s.COLUMN1 AS VARCHAR(15)) AS ADDRESS, CAST(s.COLUMN4 AS VARCHAR(30)) as TIME_DATES FROM "Schema1".weblog s; ``` ### Output ``` +----------+-----------------+--------------------------------+
| LOG_USER |     ADDRESS     |           TIME_DATES           |
|          |                 |                                | +----------+-----------------+--------------------------------+
| Jane     | 192.168.254.30  | [24/May/2004:22:01:02 -0700]   |
|          |                 |                                |
| John     | 192.168.254.30  | [24/May/2004:22:01:02 -0700]   | +----------+-----------------+--------------------------------+ ``` ## W3C Customized Formats The same results would be created by naming the specifiers directly rather than using the "COMMON" name, as shown following: ``` CREATE OR REPLACE FOREIGN STREAM schema1.weblog SERVER logfile_server OPTIONS (LOG_PATH '/path/to/logfile', ENCODING 'UTF-8', SLEEP_INTERVAL '10000', MAX_UNCHANGED_STATS '10', PARSER 'W3C', PARSER_FORMAT '%h %l %u %t \"%r\" %>s %b'); or CREATE FOREIGN STREAM "Schema1".weblog_read SERVER "logfile_server" OPTIONS (log_path '/path/to/logfile', encoding 'UTF-8', sleep_interval '10000', max_unchanged_stats '10'); CREATE OR REPLACE VIEW "Schema1".weblog AS SELECT STREAM l.r.COLUMN1, l.r.COLUMN2, l.r.COLUMN3, l.r.COLUMN4, l.r.COLUMN5, l.r.COLUMN6 FROM (SELECT STREAM W3C_LOG_PARSE(message, '%h %l %u %t \"%r\" %>s %b') FROM "Schema1".weblog_read) AS l(r); ``` ###### Note If you change %t to [%t], the date column contains the following: ``` 24/May/2004:22:01:02 -0700 ``` (instead of `[24/May/2004:22:01:02 -0700]`)
````
