

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AMS aggregated service logs
<a name="service-logs"></a>

Each AWS service logs to either CloudWatch Logs or a specific location in an Amazon S3 bucket.

**Note**  
Unless specifically stated, all log locations are local to the account that generated the logs, and are not aggregated into the central Logging account.  
To find the default AMS CloudTrail trail names in SALZ and MALZ accounts, go to the AWS Console for CloudTrail and then to the **Trails** page and search for AMS. Because AMS resources have tags, you can find the trails this way. Example AMS CloudTrail tag:  

```
Environment	  AMSInfrastructure
```

To access your logs, ensure that you have one of the required IAM roles and are in your AMS account. Then navigate to the directory shown.

------
#### [ Multi-Account Landing Zone ]


**AMS multi-account landing zone Aggregated Service Logs**  


- **1**
  - **Service name:** Amazon Aurora
  - **Log details:** General, slow query, and error logs.
  - **Log location:** CloudWatch LogGroup: /aws/rds/cluster/{{{database\_name}}}/{{{log\_name}}}

- **2**
  - **Service name:** AWS CloudFormation (CFN)
  - **Log details:** API call logging only.
  - **Log location:** AWS CloudFormation API calls are documented via CloudTrail, which sends its logs to the CloudWatch LogGroup and then syncs the logs into an S3 bucket. Logs are retained for 14 days by default in the CloudWatch LogGroup, and are retained indefinitely in the S3 bucket.<br />CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-ams-a{{{account\_ID}}}-log-management-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **3**
  - **Service name:** Amazon CloudFront (CloudFront)
  - **Log details:** User request logging. CloudFront logging must be explicitly enabled. For information, see [Enabling logging for supported services](log-customize-enable-service.md).
  - **Log location:** S3 bucket: ams-a{{{account\_ID}}}-log-management-{{{region}}}<br />Path: AWS/RedShift/{{{CloudFront distribution ID}}}

- **4**
  - **Service name:** Amazon CloudWatch (CloudWatch)
  - **Log details:** API call logging only.
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **5**
  - **Service name:** Amazon Elastic Block Store (Amazon EBS)
  - **Log details:** No logs are produced by the EBS service.
  - **Log location:** Not applicable

- **6**
  - **Service name:** Amazon Elastic Compute Cloud (Amazon EC2)
  - **Log details:** System and application logs.<br />For information, see the [Amazon Elastic Compute Cloud (Amazon EC2) - system level logs](access-to-logs-ec2.md).
  - **Log location:** CloudWatch Logs: /{{{instance ID}}}

- **7**
  - **Service name:** Amazon Elastic File System (Amazon EFS)
  - **Log details:** API call logging only.
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **8**
  - **Service name:** Elastic Load Balancing (ELB)
  - **Log details:** Access and error log entries.<br />Elastic load balancers log all requests sent to them, including requests that aren't routed to back-end instances. For example, if a client sends a malformed request, or there are no healthy instances to respond, the request is still logged.<br />For more information about Elastic Load Balancing log entries, see + Classic Load Balancers: [ Access log entries](https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html#access-log-entry-format).<br />+ Application Load Balancers: [ Access log entries](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#access-log-entry-format).<br />+ Network Load Balancers: [ Access log entries](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html#access-log-entry-format).
  - **Log location:** API call logs:<br />CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/<br />Access logs:<br />S3 bucket: mc-a{{{account\_ID}}}-logs{{{region}}}<br />Path: aws/elbaccess

- **9**
  - **Service name:** Amazon OpenSearch Service (OpenSearch Service)
  - **Log details:** Service error logs.<br />You must explicitly enable OpenSearch logging. For information, see [Enabling logging for supported services](log-customize-enable-service.md)
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **10**
  - **Service name:** Amazon ElastiCache
  - **Log details:** API call logging only.
  - **Log location:** CloudWatch LogGroup: //CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **11**
  - **Service name:** Amazon GuardDuty

- **12**
  - **Service name:** Amazon Inspector

- **13**
  - **Service name:** Amazon Macie

- **14**
  - **Service name:** Amazon Redshift
  - **Log details:** Connection, user, and activity logs.<br />Logging is enabled by default when you create your Redshift cluster by invoking the Create Redshift cluster CT (ct-1malj7snzxrkr).<br />For information, see [Database Audit Logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html).
  - **Log location:** S3 bucket: ams-a{{{account\_ID}}}-log-management-{{{region}}}<br />Path: /AWS/RedShift/{{{CloudFront Distribution ID}}}

- **15**
  - **Service name:** Amazon Relational Database Service (RDS)
  - **Log details:** Logs specific to database type.<br />You must explicitly enable RDS logging. For information, see [Enabling logging for supported services](log-customize-enable-service.md)<br />You can only access MSSQL logs through a stored procedure; for information, see [ Archiving Log Files](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Logs.html#Appendix.SQLServer.CommonDBATasks.Logs.SP).
  - **Log location:** CloudWatch LogGroup:<br />/aws/rds/({{instance}} or {{cluster}})/{{{database\_name}}}/{{{log\_name}}}

- **16**
  - **Service name:** Amazon S3 (S3)
  - **Log details:** Bucket access logs. Each access log record provides details about a single access request such as the requester, bucket name, request time, request action, response status, and error code (if any). Access log information can be useful in security and access audits. It can also help you learn about your customer base and understand your Amazon S3 bill.<br />For more information about S3 Access Log entries, see [S3 Server Access Log Format](https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html).
  - **Log location:** S3 bucket: mc-a{{{account\_ID}}}-log-management-{{{region}}}<br />Path: /aws/s3access/{{{bucket\_name}}}<br />S3 bucket [in the central Logging Account]: aws-landing-zone-s3-access-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /

- **17**
  - **Service name:** Amazon Simple Email Service (SES)
  - **Log details:** SES API service calls.
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **18**
  - **Service name:** Amazon Virtual Private Cloud (VPC)
  - **Log details:** VPC flow data (information about the IP traffic going to and from your VPC's network interfaces).
  - **Log location:** CloudWatch LogGroup:<br />/aws/vpcflow/{{{VPC\_ID}}}

- **19**
  - **Service name:** Auto Scaling
  - **Log details:** API call logging only.
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **20**
  - **Service name:** AWS Certificate Manager

- **21**
  - **Service name:** AWS CodeDeploy
  - **Log details:** Instance-specific deployment logs.
  - **Log location:** On Instance

- **22**
  - **Service name:** AWS Config
  - **Log details:** AWS Config API service calls. / **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/
  - **Log details:** Resource configuration changes, as tracked by AWS Config. / **Log location:** S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/Config/

- **23**
  - **Service name:** AWS Database Migration Service
  - **Log details:** Database migration logs.<br />For information, see [ Introducing log management in AWS Database Migration Service](https://aws.amazon.com/blogs/database/introducing-log-management-in-aws-database-migration-service/).
  - **Log location:** Database migration console

- **24**
  - **Service name:** AWS Direct Connect (DX)
  - **Log details:** API call logging only.
  - **Log location:** CloudWatch LogGroup: /CloudTrail/Landing-Zone-Logs<br />S3 bucket [in the central Logging Account]: aws-landing-zone-logs-{{{account\_ID}}}-{{{region}}}<br />Path: /AWSLogs/{{{account\_ID}}}/CloudTrail/

- **25**
  - **Service name:** AWS Glacier

- **26**
  - **Service name:** AWS IAM (IAM)

- **27**
  - **Service name:** AWS Key Management Service

- **28**
  - **Service name:** AWS Management Console (console or AWS Console)

- **29**
  - **Service name:** AWS Simple Notification Service (SNS)

- **30**
  - **Service name:** AWS Simple Queueing Service (SQS)



------
#### [ Single-Account Landing Zone ]


**AMS single-account landing zone Aggregated Service Logs**  

<table>
<thead>
  <tr><th> </th><th>Service name</th><th>Log details</th><th>Log location</th></tr>
</thead>
<tbody>
  <tr><td>1</td><td>Amazon Aurora</td><td>General, slow query, and error logs.</td><td>CloudWatch LogGroup: /aws/rds/cluster/{{{database_name}}}/{{{log_name}}}</td></tr>
  <tr><td>2</td><td>Amazon CloudFormation (CloudFormation or CFN)</td><td>API call logging only.</td><td>CloudFormation API calls are documented via CloudTrail, which sends its logs to the CloudWatch LogGroup and then syncs the logs into an S3 bucket.<br />CloudWatch LogGroup: /aws/ams/cloudtrail<br />S3 bucket: ams-a{{{account_ID}}}-log-management-{{{region}}}</td></tr>
  <tr><td>3</td><td>Amazon CloudFront (CloudFront)</td><td>User request logging.<br />You must explicitly enable CloudFront logging. For information, see <a href="log-customize-enable-service.md">Enabling logging for supported services</a></td><td>S3 bucket: ams-a{{{account_ID}}}-log-management-{{{region}}}<br />Path: AWS/RedShift/{{{CloudFront_distribution_ID}}}</td></tr>
  <tr><td>4</td><td>Amazon CloudWatch (CloudWatch)</td><td>API call logging only.</td><td>CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>5</td><td>Amazon Elastic Block Store (EBS)</td><td>No logs are produced by the EBS service.</td><td>Not applicable</td></tr>
  <tr><td>6</td><td>Amazon Elastic Compute Cloud (EC2)</td><td>System and application logs.<br />For information, see the <a href="access-to-logs-ec2.md">Amazon Elastic Compute Cloud (Amazon EC2) - system level logs</a>.</td><td>CloudWatch Logs: /{{{instance_ID}}}</td></tr>
  <tr><td>7</td><td>Amazon Elastic File System (Amazon EFS)</td><td>API call logging only.</td><td>CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>8</td><td>Elastic Load Balancing (ELB)</td><td>Access and error log entries.<br />Elastic load balancers log all requests sent to them, including requests that aren't routed to back-end instances. For example, if a client sends a malformed request, or there are no healthy instances to respond, the request is still logged.<br />For more information about elastic load balancer log entries, see<ul><li>Classic Load Balancers: <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/classic/access-log-collection.html#access-log-entry-format"> Access log entries</a>.</li><li>Application Load Balancers: <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html#access-log-entry-format"> Access log entries</a>.</li><li>Network Load Balancers: <a href="https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html#access-log-entry-format"> Access log entries</a>.</li></ul></td><td>CloudWatch LogGroup: /aws/ams/cloudtrail<br />S3 bucket: mc-a{{{account_ID}}}-logs-{{{region}}}<br />Path: aws/elbaccess</td></tr>
  <tr><td>9</td><td>Amazon OpenSearch Service (OpenSearch Service)</td><td>Service error logs.<br />You must explicitly enable OpenSearch logging. For information, see <a href="log-customize-enable-service.md">Enabling logging for supported services</a></td><td>CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>10</td><td>Amazon ElastiCache</td><td rowspan="4">API call logging only.</td><td rowspan="4">CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>11</td><td>Amazon GuardDuty</td></tr>
  <tr><td>12</td><td>Amazon Inspector</td></tr>
  <tr><td>13</td><td>Amazon Macie</td></tr>
  <tr><td>14</td><td>Amazon Redshift</td><td>Connection, user, and activity logs.<br />Logging is enabled by default when you create your Redshift cluster by invoking the Create Redshift cluster CT (ct-1malj7snzxrkr).<br />For information, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html">Database Audit Logging</a>.</td><td>S3 bucket: ams-a{{{account_ID}}}-log-management-{{{region}}}<br />Path: /AWS/RedShift/{{{CloudFront_Distribution_ID}}}</td></tr>
  <tr><td>15</td><td>Amazon Relational Database Service (RDS)</td><td>Logs specific to database type.<br />RDS logging must be explicitly enabled. For information, see <a href="log-customize-enable-service.md">Enabling logging for supported services</a><br />You can only access MSSQL logs through a stored procedure; for information, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Logs.html#Appendix.SQLServer.CommonDBATasks.Logs.SP"> Archiving Log Files</a>.</td><td>CloudWatch LogGroup: /aws/rds/(instance|cluster)/{database name}/{log name}</td></tr>
  <tr><td>16</td><td>Amazon S3 (S3)</td><td>Bucket access logs. Each access log record provides details about a single access request, such as: requester, bucket name, request time, request action, response status, and error code (if any). Access log information can be useful in security and access audits; it can also help you learn about your customer base and understand your Amazon S3 bill.<br />For more information on S3 Access Log entries, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html">S3 Server Access Log Format</a>.</td><td>S3 bucket: mc-a{{{account_ID}}}-log-management-{{{region}}}<br />Path: /aws/s3access/{{{bucket_name}}}</td></tr>
  <tr><td>17</td><td>Amazon Simple Email Service (SES)</td><td>SES API service calls.</td><td>CloudWatch LogGroup: /aws/ams/cloudtrail<br />S3 bucket: ams-a{{{account_ID}}}-log-management-{{{region}}}<br />Path: AWS/CloudTrail/AWSLogs/{{{account_ID}}}/CloudTrail/{{{region}}}</td></tr>
  <tr><td>18</td><td>Amazon Virtual Private Cloud (VPC)</td><td>VPC flow data (information about the IP traffic going to and from your VPC's network interfaces).</td><td>CloudWatch LogGroup: /aws/vpcflow/{vpc_id}</td></tr>
  <tr><td>19</td><td>Auto Scaling</td><td rowspan="2">API call logging only.</td><td rowspan="2">CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>20</td><td>AWS Certificate Manager</td></tr>
  <tr><td>21</td><td>AWS CodeDeploy</td><td>Instance specific deployment logs.</td><td>On instance</td></tr>
  <tr><td>22</td><td>AWS Config</td><td>AWS Config API service calls.</td><td>CloudWatch LogGroup: /aws/ams/cloudtrail<br />S3 bucket: ams-a{{{account_ID}}}-log-management-{{{region}}}<br />Path: AWS/CloudTrail/AWSLogs/{{{account_ID}}}/CloudTrail/{{{region}}}</td></tr>
  <tr><td>23</td><td>AWS Database Migration Service</td><td>Database migration logs.<br />For information, see <a href="https://aws.amazon.com/blogs/database/introducing-log-management-in-aws-database-migration-service/"> Introducing log management in AWS Database Migration Service</a>.</td><td>Database migration console</td></tr>
  <tr><td>24</td><td>AWS Direct Connect (DX)</td><td rowspan="7">API call logging only.</td><td rowspan="7">CloudWatch LogGroup: /aws/ams/cloudtrail</td></tr>
  <tr><td>25</td><td>AWS Glacier</td></tr>
  <tr><td>26</td><td>AWS IAM (IAM)</td></tr>
  <tr><td>27</td><td>AWS Key Management Service</td></tr>
  <tr><td>28</td><td>AWS Management Console (console or AWS Console)</td></tr>
  <tr><td>29</td><td>AWS Simple Notification Service (SNS)</td></tr>
  <tr><td>30</td><td>AWS Simple Queueing Service (SQS)</td></tr>
</tbody>
</table>


------