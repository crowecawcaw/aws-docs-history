

# W3C\_LOG\_PARSE
<a name="sql-reference-w3c-log-parse"></a>



```
 W3C_LOG_PARSE( <character-expression>, <format-string> )
 <format-string> := '<predefined-format> | <custom-format>'
 <predefined format> :=
         COMMON
       | COMMON WITH VHOST
       | NCSA EXTENDED
       | REFERER
       | AGENT
       | IIS
 <custom-format> := [an Apache log format specifier]
```

## W3C Predefined Formats
<a name="sql-reference-w3c-log-parse-predefined"></a>

Specifying the following W3C-predefined-format names summarizes using the format specifiers indicated, as shown in the following statement:

```
 select stream W3C_LOG_PARSE(message, 'COMMON') r  from w3ccommon t;
```


| Format Name | W3C Name | Format Specifiers | 
| --- | --- | --- | 
| COMMON | Common Log Format (CLF) | %h %l %u %t "%r" %>s %b | 
| COMMON WITH VHOST | Common Log Format with Virtual Host | %v %h %l %u %t "%r" %>s %b | 
| NCSA EXTENDED | NCSA extended/combined log format | %h %l %u %t "%r" %>s %b "%[Referer]i" "%[User-agent]i" | 
| REFERER | Referer log format | %[Referer]i ---> %U | 
| AGENT | Agent (Browser) log format | %[User-agent]i | 

## W3C Format Specifiers
<a name="sql-reference-w3c-log-parse-specfics"></a>

The format specifiers are listed below. W3C\_LOG\_PARSE automatically detects these specifiers and output records with one column for each specifier. The column's type is automatically chosen based on the possible outputs of the specifier. For example, %b represents the number of bytes sent in processing an HTTP request, so the column type is numeric. For %B, however, zero bytes is represented by a dash - forcing the column type to be text. Note A explains what the "..." and "<" or ">" markings shown in the specifier table mean.

The following table lists W3C format specifiers alphabetically by command.


| Format Specifier | Explanation | 
| --- | --- | 
| % | The percent sign (Apache 2.0.44 and later) | 
| %...a | Remote IP-address | 
| %...A | Local IP-address | 
| %...B | Size of response in bytes, excluding HTTP headers. | 
| %...b | Size of response in bytes, excluding HTTP headers, in CLF format, which means that when no bytes are sent, uses a '-' rather than a 0. | 
| %...[Customerdata]C | The contents of cookie Customerdata in the request sent to the server. | 
| %...D | The time taken to serve the request, in microseconds. | 
| %...[CUSTOMERDATA]e | The contents of the environment variable CUSTOMERDATA | 
| %...f | Filename | 
| %...h | Remote host | 
| %...H | The request protocol | 
| %...[Customerdata]i | The contents of Customerdata: header line(s) in the request sent to the server. | 
| %...l | Remote logname (from identd, if supplied) | 
| %...m | The request method | 
| %...[Customerdata]n | The contents of note Customerdata from another module. | 
| %...[Customerdata]o | The contents of Customerdata: header line(s) in the reply. | 
| %...p | The canonical port of the server serving the request | 
| %...P | The process ID of the child that serviced the request. | 
| %...[format]P | The process ID or thread id of the child that serviced the request. Valid formats are pid and tid. (Apache 2.0.46 and later) | 
| %...q | The query string (prepended with a ? if a query string exists, otherwise an empty string) | 
| %...r | First line of request | 
| %...s | Status. For requests that got internally redirected, this is the status of the \*original\* request --- %...>s for the last. | 
| %...t | Time, in common log format time format (standard English format) | 
| %...[format]t | The time, in the form given by format, which should be in strimmer(3) format. (potentially localized) | 
| %...T | The time taken to serve the request, in seconds. | 
| %...u | Remote user (from auth; may be bogus if return status (%s) is 401) | 
| %...U | The URL path requested, not including any query string. | 
| %...v | The canonical ServerName of the server serving the request. | 
| %...V | The server name according to the UseCanonicalName setting. | 
| %...X | Connection status when response is completed<br />X = connection aborted before the response completed.<br />\+ = connection may be kept alive after the response is sent.<br />- = connection will be closed after the response is sent.<br />(The %..X directive was %...c in late versions of Apache 1.3,<br />but this conflicted with the historical ssl %...[var]c syntax.) | 
| :%...I: | Bytes received, including request and headers, cannot be zero. You need to enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html) to use this. | 
| :%...O: | Bytes sent, including headers, cannot be zero. You need to enable [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html) to use this. | 

**Note**  <a name="noteA"></a>
Some W3C format specifiers are shown as containing a "..." indication or a "<" or ">", which are optional controls on suppressing or redirecting the output of that specifier. The "..." can either be empty (as in the COMMON specification "\\%h %u %r \\%s %b") or it can indicate conditions for including the item. The conditions are a list of HTTP status codes, possibly preceded by "\!", and if the specified condition is not met, then the column or field returned shows "-".   
For example, as described in the [Apache documentation](http://httpd.apache.org/docs/2.0/mod/mod_log_config.html), specifying "%400,501[User-agent]i" will log the User-agent only on 400 errors and 501 errors (Bad Request, Not Implemented). Similarly, "%\!200,304,302[Referer]i" will log the Referer: on all requests that fail to return some sort of normal status.   
The modifiers "<" and ">" can be used to choose whether the original or final (respectively) request should be consulted when a request has been internally redirected. By default, the % directives %s, %U, %T, %D, and %r look at the original request while all others look at the final request. So for example, %>s can be used to record the final status of the request and %<u can be used to record the original authenticated user on a request that is internally redirected to an unauthenticated resource.   
For security reasons, starting with Apache 2.0.46, non-printable and other special characters are escaped mostly by using \\xhh sequences, where hh stands for the hexadecimal representation of the raw byte. Exceptions from this rule are " and \\ which are escaped by prepending a backslash, and all white space characters which are written in their C-style notation (\\n, \\t etc). In httpd 2.0 versions prior to 2.0.46, no escaping was performed on the strings from %...r, %...i and %...o, so great care was needed when dealing with raw log files, since clients could have inserted control characters into the log.   
Also, in httpd 2.0, the B format strings represent simply the size in bytes of the HTTP response (which will differ, for instance, if the connection is aborted, or if SSL is used). For the actual number of bytes sent over the network to the client, use the %O format provided by [mod\_logio](http://httpd.apache.org/docs/2.0/mod/mod_logio.html).

## W3C Format Specifiers by Function or Category
<a name="w2aac22c23c17c11"></a>

The categories are bytes sent, connection status, content of environmental variable, filename, host, IP, notes, protocol, query string, replies, requests, and time. For the markings "..." or "<" or "<", see the previous note.


<table>
<thead>
  <tr><th>Function or Category</th><th>W3C Format Specifiers</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Bytes sent, excluding HTTP headers</b></td></tr>
  <tr><td>with a "0" when no bytes are sent</td><td>%...B</td></tr>
  <tr><td>with a "-" (CLF format) when no bytes are sent</td><td>%...b</td></tr>
  <tr><td>Bytes received, including request and headers, cannot be zero<br />Must enable <a href="http://httpd.apache.org/docs/2.0/mod/mod_logio.html">mod_logio</a> to use this.</td><td>:% ... I:</td></tr>
  <tr><td>Bytes sent, including headers, cannot be zero<br />Must enable <a href="http://httpd.apache.org/docs/2.0/mod/mod_logio.html">mod_logio</a> to use this.</td><td>:%... O:</td></tr>
  <tr><td colspan="2"><b>Connection status when response is completed</b></td></tr>
  <tr><td>Connection aborted before the response completed</td><td>X</td></tr>
  <tr><td>Connection may be kept alive after the response is sent</td><td>+</td></tr>
  <tr><td>Connection will be closed after the response is sent</td><td>-</td></tr>
  <tr><td colspan="2">  The %..X directive was %...c in late versions of Apache 1.3, but this conflicted with the historical ssl %...[var]c syntax.  </td></tr>
  <tr><td colspan="2"><b>Environment variable CUSTOMERDATA</b></td></tr>
  <tr><td>contents</td><td>%...[CUSTOMERDATA]e</td></tr>
  <tr><td><b>Filename</b></td><td>%...f</td></tr>
  <tr><td><b>Host (remote)</b></td><td>%...h</td></tr>
  <tr><td><b>Protocol</b></td><td>%...H</td></tr>
  <tr><td colspan="2"><b>IP addresses</b></td></tr>
  <tr><td>Remote</td><td>%...a</td></tr>
  <tr><td>Local</td><td>%...A</td></tr>
  <tr><td><b>Notes</b></td><td></td></tr>
  <tr><td>Contents of note Customerdata from another module</td><td>%...[Customerdata]n</td></tr>
  <tr><td><b>Protocol (request)</b></td><td>%...H</td></tr>
  <tr><td><b>Query string</b> If query exists, prepended with a ? <br />If not, the empty string. </td><td>%...q</td></tr>
  <tr><td colspan="2"><b>Replies</b></td></tr>
  <tr><td>Contents of Customerdata (header lines in the reply)</td><td>%...[Customerdata]o</td></tr>
</tbody>
</table>


The W3C format specifiers for the response and time categories are listed following table.


<table>
<thead>
  <tr><th>Function or Category</th><th>W3C Format Specifiers</th></tr>
</thead>
<tbody>
  <tr><td colspan="2"><b>Requests</b></td></tr>
  <tr><td>Canonical port of the server serving the request</td><td>%...p</td></tr>
  <tr><td>Contents of cookie Customerdata in the request sent to server</td><td>%... [Customerdata]C</td></tr>
  <tr><td>Contents of BAR:header line(s)</td><td>%... [BAR]i</td></tr>
  <tr><td>First line sent:</td><td>%...r</td></tr>
  <tr><td>Microseconds taken to serve a request</td><td>%...D</td></tr>
  <tr><td>Protocol</td><td>%...H</td></tr>
  <tr><td>Process ID of the child that serviced the request</td><td>%...P</td></tr>
  <tr><td>Process ID or thread id of the child that serviced the request.<br />Valid formats are pid and tid. (Apache 2.0.46 and later)</td><td>%...[format]P</td></tr>
  <tr><td>Remote logname (from identd, if supplied)</td><td>%...l</td></tr>
  <tr><td>Remote user: (from auth; may be bogus if return status (%s) is 401)</td><td>%...u</td></tr>
  <tr><td>Server (canonical ServerName) serving the request</td><td>%...v</td></tr>
  <tr><td>Server name by the UseCanonicalName setting</td><td>%...V</td></tr>
  <tr><td>Request method</td><td>%...m</td></tr>
  <tr><td>Return status</td><td>%s</td></tr>
  <tr><td>Seconds taken to serve the request</td><td>%...T</td></tr>
  <tr><td>Status of the *original* request that was internally redirected</td><td>%...s</td></tr>
  <tr><td>Status of the last request</td><td>%...&gt;s</td></tr>
  <tr><td>URL path requested, not including any query string</td><td>%...U</td></tr>
  <tr><td colspan="2"><b>Time</b></td></tr>
  <tr><td>Common log format time format (standard English format)</td><td>%...t</td></tr>
  <tr><td>Time in strftime(3) format, potentially localized</td><td>%...[format]t</td></tr>
  <tr><td>Seconds taken to serve the request</td><td>%...T</td></tr>
</tbody>
</table>


## W3C Examples
<a name="w2aac22c23c17c13"></a>

W3C\_LOG\_PARSE supports access to logs generated by W3C-compliant applications like the Apache web server, producing output rows with one column for each specifier. The data types are derived from the log entry description specifiers listed in the [Apache mod\_log\_config](http://httpd.apache.org/docs/2.0/mod/mod_log_config.html?#formats) specification.

## Example 1
<a name="sql-reference-w3c-log-parse-info"></a>

The input in this example is taken from an Apache log file and is representative of the COMMON log format.

### Input
<a name="sql-reference-w3c-log-parse-info-input"></a>

```
(192.168.254.30 - John [24/May/2004:22:01:02 -0700]
                     "GET /icons/apache_pb.gif HTTP/1.1" 304 0),
(192.168.254.30 - Jane [24/May/2004:22:01:02 -0700]
                     "GET /icons/small/dir.gif HTTP/1.1" 304 0);
```

### DDL
<a name="sql-reference-w3c-log-parse-info-ddl"></a>

```
CREATE OR REPLACE PUMP weblog AS
        SELECT STREAM
            l.r.COLUMN1,
            l.r.COLUMN2,
            l.r.COLUMN3,
            l.r.COLUMN4,
            l.r.COLUMN5,
            l.r.COLUMN6,
            l.r.COLUMN7
        FROM (SELECT STREAM W3C_LOG_PARSE(message, 'COMMON')
              FROM "weblog_read) AS l(r);
```

### Output
<a name="sql-reference-w3c-log-parse-info-output"></a>

```
 192.168.254.30 -  John  [24/May/2004:22:01:02 -0700] GET /icons/apache_pb.gif HTTP/1.1  304  0
 192.168.254.30 -  Jane  [24/May/2004:22:01:02 -0700] GET /icons/small/dir.gif HTTP/1.1  304  0
```

### 
<a name="sql-reference-w3c-log-parse-details"></a>

The specification of COMMON in the FROM clause means the Common Log Format (CLF), which uses the specifiers %h %l %u %t "%r" %>s %b.

The [W3C-predefined formats](https://docs.aws.amazon.com/kinesisanalytics/latest/sqlref/sql-reference-w3c-log-parse.html#sql-reference-w3c-log-parse-predefined) shows the COMMON and other predefined specifier sets.

The specification of COMMON in the FROM clause means the Common Log Format (CLF), which uses the specifiers %h %l %u %t "%r" %>s %b. 

The table below, Specifiers used by the Common Log Format, describes the specifiers used by COMMON in the FROM clause.

## Specifiers Used by the Common Log Format
<a name="w2aac22c23c17c17"></a>


| Output Column | Format Specifier | Returns | 
| --- | --- | --- | 
| COLUMN1 | %h | The IP address of the remote host | 
| COLUMN2 | %l | The remote logname | 
| COLUMN3 | %u | The remote user | 
| COLUMN4 | %t | The time | 
| COLUMN5 | "%r" | The first line of the request | 
| COLUMN6 | %>s | The status: For internally redirected requests,<br />the status of the \*original\* request<br />--- %...>s for the last. | 
| COLUMN7 | %b | The number of bytes sent, excluding HTTP headers | 

## Example 2
<a name="w2aac22c23c17c19"></a>

The DDL in this example shows how to rename output columns and filter out unneeded columns.

### DDL
<a name="sql-reference-w3c-log-parse-ddl"></a>

```
    CREATE OR REPLACE VIEW "Schema1".weblogreduced AS
        SELECT STREAM CAST(s.COLUMN3 AS VARCHAR(5)) AS LOG_USER,
        CAST(s.COLUMN1 AS VARCHAR(15)) AS ADDRESS,
        CAST(s.COLUMN4 AS VARCHAR(30)) as TIME_DATES
        FROM "Schema1".weblog s;
```

### Output
<a name="sql-reference-w3c-log-parse-output"></a>

```
    +----------+-----------------+--------------------------------+
    | LOG_USER |     ADDRESS     |           TIME_DATES           |
    |          |                 |                                |
    +----------+-----------------+--------------------------------+
    | Jane     | 192.168.254.30  | [24/May/2004:22:01:02 -0700]   |
    |          |                 |                                |
    | John     | 192.168.254.30  | [24/May/2004:22:01:02 -0700]   |
    +----------+-----------------+--------------------------------+
```

## W3C Customized Formats
<a name="w2aac22c23c17c21"></a>

The same results would be created by naming the specifiers directly rather than using the "COMMON" name, as shown following: 

```
    CREATE OR REPLACE FOREIGN STREAM schema1.weblog
        SERVER logfile_server
        OPTIONS (LOG_PATH '/path/to/logfile',
                 ENCODING 'UTF-8',
                 SLEEP_INTERVAL '10000',
                 MAX_UNCHANGED_STATS '10',
                 PARSER 'W3C',
                 PARSER_FORMAT '%h %l %u %t \"%r\" %>s %b');
    or
     CREATE FOREIGN STREAM "Schema1".weblog_read
     SERVER "logfile_server"
     OPTIONS (log_path '/path/to/logfile',
     encoding 'UTF-8',
     sleep_interval '10000',
     max_unchanged_stats '10');
     CREATE OR REPLACE VIEW "Schema1".weblog AS
        SELECT STREAM
            l.r.COLUMN1,
            l.r.COLUMN2,
            l.r.COLUMN3,
            l.r.COLUMN4,
            l.r.COLUMN5,
            l.r.COLUMN6
        FROM (SELECT STREAM W3C_LOG_PARSE(message, '%h %l %u %t \"%r\" %>s %b')
              FROM "Schema1".weblog_read) AS l(r);
```

**Note**  
If you change %t to [%t], the date column contains the following:  

```
        24/May/2004:22:01:02 -0700
```
(instead of `[24/May/2004:22:01:02 -0700]`)