

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_CONNECTION\_LOG
<a name="SYS_CONNECTION_LOG"></a>

Logs authentication attempts and connections and disconnections.

SYS\_CONNECTION\_LOG is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_CONNECTION_LOG-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| event  | character(50) | Connection or authentication event. | 
| record\_time  | timestamp | Time the event occurred. | 
| remote\_host  | character(45) | Name or IP address of remote host. | 
| remote\_port  | character(32)  | Port number for remote host. | 
| session\_id  | integer  | Process ID associated with the statement.  | 
| database\_name  | character(50)  | Database name. | 
| user\_name | character(50)  | Username. | 
| auth\_method | character(32) | Authentication method. | 
| duration  | integer  | Duration of connection in microseconds. | 
| ssl\_version | character(50)  | Secure Sockets Layer (SSL) version. This column is empty when SSL is disabled. | 
| ssl\_cipher | character(128) | SSL cipher. | 
| mtu  | integer  | Maximum transmission unit (MTU). | 
| ssl\_compression  | character(64)  | SSL compression type. | 
| ssl\_expansion | character(64)  | SSL expansion type. | 
| iam\_auth\_guid | character(36)  | The IAM authentication ID for the CloudTrail request. | 
| application\_name | character(250)  | The initial or updated name of the application for a session. | 
| driver\_version | character(64)  | The version of ODBC or JDBC driver that connects to your Amazon Redshift cluster from your third-party SQL client tools. | 
| os\_version | character(64)  | The version of the operating system that is on the client machine that connects to your Amazon Redshift cluster. | 
| plugin\_name | character(32)  | The name of the plugin used to connect to your Amazon Redshift cluster. | 
| protocol\_version | integer | The internal protocol version that the Amazon Redshift driver uses when establishing its connection with the server. The protocol versions are negotiated between the driver and server. The version describes the features available. Valid values include: +  0 (BASE\_SERVER\_PROTOCOL\_VERSION)  <br />+  1 (EXTENDED\_RESULT\_METADATA\_SERVER\_PROTOCOL\_VERSION) – To save a round trip per query, the server sends extra result set metadata information.  <br />+  2 (BINARY\_PROTOCOL\_VERSION) – Depending on the data type of the result set, the server sends data in binary format.  <br />+  3 (EXTENDED2\_RESULT\_METADATA\_SERVER\_PROTOCOL\_VERSION) – The server sends case sensitivity (collation) information of a column.   | 
| global\_session\_id | character(36)  | The globally unique identifier for the current session. The session ID persists through node failure restarts. | 

## Sample queries
<a name="SYS_CONNECTION_LOG-sample-queries2"></a>

To view the details for open connections, run the following query.

```
select record_time, user_name, database_name, remote_host, remote_port
from sys_connection_log
where event = 'initiating session'
and session_id not in 
(select session_id from sys_connection_log
where event = 'disconnecting session')
order by 1 desc;

record_time         | user_name   | database_name   | remote_host   | remote_port                      
--------------------+-------------+-----------------+---------------+---------------------------------
2014-11-06 20:30:06 | rdsdb       | dev             | [local]       |                            
2014-11-06 20:29:37 | test001     | test            | 10.49.42.138  | 11111                           
2014-11-05 20:30:29 | rdsdb       | dev             | 10.49.42.138  | 33333                                                 
2014-11-05 20:28:35 | rdsdb       | dev             | [local]       |  
(4 rows)
```

The following example reflects a failed authentication attempt and a successful connection and disconnection. 

```
select event, record_time, remote_host, user_name
from sys_connection_log order by record_time;            

            event      |         record_time        |  remote_host  | user_name                      
-----------------------+----------------------------+---------------+---------
authentication failure | 2012-10-25 14:41:56.96391  | 10.49.42.138  | john                                              
authenticated          | 2012-10-25 14:42:10.87613  | 10.49.42.138  | john                                              
initiating session     | 2012-10-25 14:42:10.87638  | 10.49.42.138  | john                                              
disconnecting session  | 2012-10-25 14:42:19.95992  | 10.49.42.138  | john                                              
(4 rows)
```

The following example shows the version of the ODBC driver, the operating system on the client machine, and the plugin used to connect to the Amazon Redshift cluster. In this example, the plugin used is for standard ODBC driver authentication using a login name and password.

```
select driver_version, os_version, plugin_name from sys_connection_log;
                
driver_version                          |  os_version                       | plugin_name
----------------------------------------+-----------------------------------+--------------------
Amazon Redshift ODBC Driver 1.4.15.0001 | Darwin 18.7.0 x86_64              | none
Amazon Redshift ODBC Driver 1.4.15.0001 | Linux 4.15.0-101-generic x86_64   | none
```

The following example shows the version of the operating system on the client machine, the driver version, and the protocol version.

```
select os_version, driver_version, protocol_version from sys_connection_log;
                
os_version                      |  driver_version              | protocol_version
--------------------------------+------------------------------+--------------------
Linux 4.15.0-101-generic x86_64 | Redshift JDBC Driver 2.0.0.0 | 2
Linux 4.15.0-101-generic x86_64 | Redshift JDBC Driver 2.0.0.0 | 2 
Linux 4.15.0-101-generic x86_64 | Redshift JDBC Driver 2.0.0.0 | 2
```