# Demos: Retrieving the last seven days of

AWS Health event data programmatically

In the following code examples, AWS Health uses a DNS lookup against the global
endpoint to determine the active regional endpoint and signing Region. AWS Health uses
this information to retrieve a report of the last seven days of event data. The code
restarts the workflow if the active endpoint changes.

###### Topics

- [Demo: Retrieving the last seven days of
  AWS Health event data using Java](#using-the-java-sample-code "#using-the-java-sample-code")
- [Demo: Retrieving the last seven days of
  AWS Health event data using Python](#using-the-python-code "#using-the-python-code")

## Demo: Retrieving the last seven days of

AWS Health event data using Java

###### Prerequisite

You must install [Gradle](https://docs.gradle.org/current/userguide/installation.html "https://docs.gradle.org/current/userguide/installation.html").

###### To use the Java example

1. Download the [AWS Health high availability endpoint demo](https://github.com/aws/aws-health-tools/tree/master/high-availability-endpoint "https://github.com/aws/aws-health-tools/tree/master/high-availability-endpoint") from GitHub.
2. Navigate to the demo project
   `high-availability-endpoint/java` directory.
3. In a command line window, enter the following command.

```
`gradle build`
```

4. Enter the following commands to specify your AWS credentials.

```
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_SESSION_TOKEN="`your-aws-token`"

```

5. Enter the following command to run the demo.

```
`gradle run`
```

###### Example: AWS Health event output

The code example returns the recent AWS Health event in the last
seven days in your AWS account. In the following example, the output
includes an AWS Health event for the AWS Config service.

```
> Task :run
[main] INFO aws.health.high.availability.endpoint.demo.HighAvailabilityV2Workflow - EventDetails(Event=Event(Arn=arn:aws:health:global::event/CONFIG/AWS_CONFIG_OPERATIONAL_NOTIFICATION/AWS_CONFIG_OPERATIONAL_NOTIFICATION_88a43e8a-e419-4ca7-9baa-56bcde4dba3,
Service=CONFIG, EventTypeCode=AWS_CONFIG_OPERATIONAL_NOTIFICATION, EventTypeCategory=accountNotification, Region=global, StartTime=2020-09-11T02:55:49.899Z, LastUpdatedTime=2020-09-11T03:46:31.764Z,
StatusCode=open, EventScopeCode=ACCOUNT_SPECIFIC), EventDescription=EventDescription(LatestDescription=As part of our ongoing efforts to optimize costs associated with recording changes related to certain ephemeral workloads,
AWS Config is scheduled to release an update to relationships modeled within ConfigurationItems (CI) for 7 EC2 resource types on August 1, 2021.
Examples of ephemeral workloads include changes to Amazon Elastic Compute Cloud (Amazon EC2) Spot Instances, Amazon Elastic MapReduce jobs, and Amazon EC2 Autoscaling.
This update will optimize CI models for EC2 Instance, SecurityGroup, Network Interface, Subnet, VPC, VPN Gateway, and Customer Gateway resource types to record direct relationships and deprecate indirect relationships.

A direct relationship is defined as a one-way relationship (A->B) between a resource (A) and another resource (B), and is typically derived from the Describe API response of resource (A).
An indirect relationship, on the other hand, is a relationship that AWS Config infers (B->A), in order to create a bidirectional relationship.
For example, EC2 instance -> Security Group is a direct relationship, since security groups are returned as part of the describe API response for an EC2 instance.
But Security Group -> EC2 instance is an indirect relationship, since EC2 instances are not returned when describing an EC2 Security group.

Until now, AWS Config has recorded both direct and indirect relationships. With the launch of Advanced queries in March 2019, indirect relationships can easily be answered by running Structured Query Language (SQL) queries such as:

SELECT
 resourceId,
 resourceType
WHERE
 resourceType ='AWS::EC2::Instance'
AND
 relationships.resourceId = 'sg-234213'

By deprecating indirect relationships, we can optimize the information contained within a
Configuration Item while reducing AWS Config costs related to relationship changes.
This is especially useful in case of ephemeral workloads where there is a high volume of configuration changes for EC2 resource types.

Which resource relationships are being removed?

Resource Type: Related Resource Type
1 AWS::EC2::CustomerGateway: AWS::VPN::Connection
2 AWS::EC2::Instance: AWS::EC2::EIP, AWS::EC2::RouteTable
3 AWS::EC2::NetworkInterface: AWS::EC2::EIP, AWS::EC2::RouteTable
4 AWS::EC2::SecurityGroup: AWS::EC2::Instance, AWS::EC2::NetworkInterface
5 AWS::EC2::Subnet: AWS::EC2::Instance, AWS::EC2::NetworkACL, AWS::EC2::NetworkInterface, AWS::EC2::RouteTable
6 AWS::EC2::VPC: AWS::EC2::Instance, AWS::EC2::InternetGateway, AWS::EC2::NetworkACL, AWS::EC2::NetworkInterface, AWS::EC2::RouteTable, AWS::EC2::Subnet, AWS::EC2::VPNGateway, AWS::EC2::SecurityGroup
7 AWS::EC2::VPNGateway: AWS::EC2::RouteTable, AWS::EC2::VPNConnection

Alternate mechanism to retrieve this relationship information:
The SelectResourceConfig API accepts a SQL SELECT command, performs the corresponding search, and returns resource configurations matching the properties. You can use this API to retrieve the same relationship information.
For example, to retrieve the list of all EC2 Instances related to a particular VPC vpc-1234abc, you can use the following query:

SELECT
 resourceId,
 resourceType
WHERE
 resourceType ='AWS::EC2::Instance'
AND
 relationships.resourceId = 'vpc-1234abc'

If you have any questions regarding this deprecation plan, please contact AWS Support [1]. Additional sample queries to retrieve the relationship information for the resources listed above is provided in [2].

[1] https://aws.amazon.com/support
[2] https://docs.aws.amazon.com/config/latest/developerguide/examplerelationshipqueries.html),
EventMetadata={})
```

### Java resources

- For more information, see the [Interface HealthClient](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/health/HealthClient.html "https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/health/HealthClient.html") in the
  _AWS SDK for Java API Reference_ and the [source code](https://repo1.maven.org/maven2/software/amazon/awssdk/health/2.14.2/ "https://repo1.maven.org/maven2/software/amazon/awssdk/health/2.14.2/").
- For more information about the library used in this demo for DNS
  lookups, see the [dnsjava](https://github.com/dnsjava/dnsjava "https://github.com/dnsjava/dnsjava") in GitHub.

## Demo: Retrieving the last seven days of

AWS Health event data using Python

###### Prerequisite

You must install [Python
3](https://www.python.org/downloads/ "https://www.python.org/downloads/").

###### To use the Python example

1. Download the [AWS Health high availability endpoint demo](https://github.com/aws/aws-health-tools/tree/master/high-availability-endpoint "https://github.com/aws/aws-health-tools/tree/master/high-availability-endpoint") from GitHub.
2. Navigate to the demo project
   `high-availability-endpoint/python` directory.
3. In a command line window, enter the following commands.

```
`pip3 install virtualenv
virtualenv -p python3 v-aws-health-env`
```

###### Note

For Python 3.3 and later, you can use the built-in `venv`
module to create the virtual environment, instead of installing
`virtualenv`. For more information, see [venv - Creation of
virtual environments](https://docs.python.org/3/library/venv.html "https://docs.python.org/3/library/venv.html") on the Python website.

```
`python3 -m venv v-aws-health-env`
```

4. Enter the following command to activate the virtual environment.

```
`source v-aws-health-env/bin/activate`
```

5. Enter the following command to install the dependencies.

```
`pip install -r requirements.txt`
```

6. Enter the following commands to specify your AWS credentials.

```
export AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
export AWS_SESSION_TOKEN="`your-aws-token`"

```

7. Enter the following command to run the demo.

```
`python3 main.py`
```

###### Example: AWS Health event output

The code example returns the recent AWS Health event in the last
seven days in your AWS account. The following output returns an
AWS Health event for an AWS security notification.

```
INFO:botocore.credentials:Found credentials in environment variables.
INFO:root:Details: {'arn': 'arn:aws:health:global::event/SECURITY/AWS_SECURITY_NOTIFICATION/AWS_SECURITY_NOTIFICATION_0e35e47e-2247-47c4-a9a5-876544042721',
'service': 'SECURITY', 'eventTypeCode': 'AWS_SECURITY_NOTIFICATION', 'eventTypeCategory': 'accountNotification', 'region': 'global', 'startTime': datetime.datetime(2020, 8, 19, 23, 30, 42, 476000,
tzinfo=tzlocal()), 'lastUpdatedTime': datetime.datetime(2020, 8, 20, 20, 44, 9, 547000, tzinfo=tzlocal()), 'statusCode': 'open', 'eventScopeCode': 'PUBLIC'}, description:
{'latestDescription': 'This is the second notice regarding TLS requirements on FIPS endpoints.\n\nWe
are in the process of updating all AWS Federal Information Processing Standard (FIPS) endpoints across all AWS regions
to Transport Layer Security (TLS) version 1.2 by March 31, 2021 . In order to avoid an interruption in service, we encourage you to act now, by ensuring that you connect to AWS FIPS endpoints at a TLS version of 1.2.
If your client applications fail to support TLS 1.2 it will result in connection failures when TLS versions below 1.2 are no longer supported.\n\nBetween now and March 31, 2021 AWS will remove TLS 1.0 and TLS 1.1 support from each FIPS endpoint where no connections below TLS 1.2 are detected over a 30-day period.
After March 31, 2021 we may deploy this change to all AWS FIPS endpoints, even if there continue
to be customer connections detected at TLS versions below 1.2. \n\nWe will provide additional updates and reminders on the AWS Security Blog, with a ‘TLS’ tag [1]. If you need further guidance or assistance, please contact AWS Support [2] or your Technical Account Manager (TAM).
Additional information is below.\n\nHow can I identify clients that are connecting with TLS
1.0/1.1?\nFor customers using S3 [3], Cloudfront [4] or Application Load Balancer [5] you can use
your access logs to view the TLS connection information for these services, and identify client
connections that are not at TLS 1.2. If you are using the AWS Developer Tools on your clients,
you can find information on how to properly configure your client’s TLS versions by visiting Tools to Build on AWS [7] or our associated AWS Security Blog has a link for each unique code language [7].\n\nWhat is Transport Layer Security (TLS)?\nTransport Layer Security (TLS Protocols) are cryptographic protocols designed to provide secure communication across a computer network
[6].\n\nWhat are AWS FIPS endpoints? \nAll AWS services offer Transport Layer Security (TLS) 1.2 encrypted endpoints that can be used for all API calls. Some AWS services also offer FIPS 140-2 endpoints [9] for customers that require use of FIPS validated cryptographic libraries. \n\n[1] https://aws.amazon.com/blogs/security/tag/tls/\n[2] https://aws.amazon.com/support\n[3]
https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html\n[4] https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html\n[5] https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html\n[6] https://aws.amazon.com/tools\n[7] https://aws.amazon.com/blogs/security/tls-1-2-to-become-the-minimum-for-all-aws-fips-endpoints\n[8]
https://en.wikipedia.org/wiki/Transport_Layer_Security\n[9] https://aws.amazon.com/compliance/fips'}
```

8. When you're finished, enter the following command to deactivate the
   virtual machine.

```
`deactivate`
```

### Python resources

- For more information about the `Health. Client`, see the
  [AWS SDK for Python (Boto3) API Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/health.html#Health.Client").
- For more information about the library used in this demo for DNS
  lookups, see the [dnspython](https://dnspython.readthedocs.io/en/stable/ "https://dnspython.readthedocs.io/en/stable/")
  toolkit and the [source code](https://github.com/rthalley/dnspython/ "https://github.com/rthalley/dnspython/") on GitHub.
