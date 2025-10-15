# Amazon CloudWatch Logs template snippets

Amazon CloudWatch Logs can monitor your system, application, and custom log files from Amazon EC2 instances
 or other sources. You can use AWS CloudFormation to provision and manage log groups and metric filters.
 For more information about Amazon CloudWatch Logs, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html").

###### Topics

* [Send logs to CloudWatch Logs from a Linux
 instance](#quickref-cloudwatchlogs-example1 "#quickref-cloudwatchlogs-example1")
* [Send logs to CloudWatch Logs from a Windows
 instance](#quickref-cloudwatchlogs-example2 "#quickref-cloudwatchlogs-example2")
* [See also](#w71aac11c39c35c11 "#w71aac11c39c35c11")

## Send logs to CloudWatch Logs from a Linux
 instance


The following template demonstrates how to set up a web server on Amazon Linux 2023 with
 CloudWatch Logs integration. The template performs the following tasks:



* Installs Apache and PHP.
* Configures the CloudWatch agent to forward Apache access logs to CloudWatch Logs.
* Sets up an IAM role to allow the CloudWatch agent to send log data to
 CloudWatch Logs.
* Creates custom alarms and notifications to monitor for 404 errors or high
 bandwidth usage.

Log events from the web server provide metric data for CloudWatch alarms. The two metric
 filters describe how the log information is transformed into CloudWatch metrics. The 404
 metric counts the number of 404 occurrences. The size metric tracks the size of a
 request. The two CloudWatch alarms will send notifications if there are more than two 404s
 within 2 minutes or if the average request size is over 3500 KB over 10 minutes.



### JSON



```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Sample template that sets up and configures CloudWatch Logs on Amazon Linux 2023 instance.",
    "Parameters": {
        "KeyName": {
            "Description": "Name of an existing EC2 KeyPair to enable SSH access to the instances",
            "Type": "AWS::EC2::KeyPair::KeyName",
            "ConstraintDescription": "must be the name of an existing EC2 KeyPair."
        },
        "SSHLocation": {
            "Description": "The IP address range that can be used to SSH to the EC2 instances",
            "Type": "String",
            "MinLength": "9",
            "MaxLength": "18",
            "Default": "0.0.0.0/0",
            "AllowedPattern": "(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})",
            "ConstraintDescription": "must be a valid IP CIDR range of the form x.x.x.x/x."
        },
        "OperatorEmail": {
            "Description": "Email address to notify when CloudWatch alarms are triggered (404 errors or high bandwidth usage)",
            "Type": "String"
        }
    },
    "Resources": {
        "LogRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",		 	 	 
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "ec2.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
                    ]
                },
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "LogRolePolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",		 	 	 
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:PutLogEvents",
                                        "logs:DescribeLogStreams",
                                        "logs:DescribeLogGroups",
                                        "logs:CreateLogGroup",
                                        "logs:CreateLogStream"
                                    ],
                                    "Resource": "*"
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "LogRoleInstanceProfile": {
            "Type": "AWS::IAM::InstanceProfile",
            "Properties": {
                "Path": "/",
                "Roles": [{"Ref": "LogRole"}]
            }
        },
        "WebServerSecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Enable HTTP access via port 80 and SSH access via port 22",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 80,
                        "ToPort": 80,
                        "CidrIp": "0.0.0.0/0"
                    },
                    {
                        "IpProtocol": "tcp",
                        "FromPort": 22,
                        "ToPort": 22,
                        "CidrIp": {"Ref": "SSHLocation"}
                    }
                ]
            }
        },
        "WebServerHost": {
            "Type": "AWS::EC2::Instance",
            "Metadata": {
                "Comment": "Install a simple PHP application on Amazon Linux 2023",
                "AWS::CloudFormation::Init": {
                    "config": {
                        "packages": {
                            "dnf": {
                                "httpd": [],
                                "php": [],
                                "php-fpm": []
                            }
                        },
                        "files": {
                            "/etc/amazon-cloudwatch-agent/amazon-cloudwatch-agent.json": {
                                "content": {
                                    "logs": {
                                        "logs_collected": {
                                            "files": {
                                                "collect_list": [{
                                                    "file_path": "/var/log/httpd/access_log",
                                                    "log_group_name": {"Ref": "WebServerLogGroup"},
                                                    "log_stream_name": "{instance_id}/apache.log",
                                                    "timestamp_format": "%d/%b/%Y:%H:%M:%S %z"
                                                }]
                                            }
                                        }
                                    }
                                },
                                "mode": "000644",
                                "owner": "root",
                                "group": "root"
                            },
                            "/var/www/html/index.php": {
                                "content": "<?php\necho '<h1>AWS CloudFormation sample PHP application on Amazon Linux 2023</h1>';\n?>\n",
                                "mode": "000644",
                                "owner": "apache",
                                "group": "apache"
                            },
                            "/etc/cfn/cfn-hup.conf": {
                                "content":  {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "[main]\n",
                                            "stack=",
                                            {"Ref": "AWS::StackId"},
                                            "\n",
                                            "region=",
                                            {"Ref": "AWS::Region"},
                                            "\n"
                                        ]
                                    ]
                                },
                                "mode": "000400",
                                "owner": "root",
                                "group": "root"
                            },
                            "/etc/cfn/hooks.d/cfn-auto-reloader.conf": {
                                "content": {
                                    "Fn::Join": [
                                        "",
                                        [
                                            "[cfn-auto-reloader-hook]\n",
                                            "triggers=post.update\n",
                                            "path=Resources.WebServerHost.Metadata.AWS::CloudFormation::Init\n",
                                            "action=/opt/aws/bin/cfn-init -s ",
                                            {"Ref": "AWS::StackId"},
                                            " -r WebServerHost ",
                                            " --region     ",
                                            {"Ref": "AWS::Region"},
                                            "\n",
                                            "runas=root\n"
                                        ]
                                    ]
                                }
                            }
                        },
                        "services": {
                            "systemd": {
                                "httpd": {
                                    "enabled": "true",
                                    "ensureRunning": "true"
                                },
                                "php-fpm": {
                                    "enabled": "true",
                                    "ensureRunning": "true"
                                }
                            }
                        }
                    }
                }
            },
            "CreationPolicy": {
                "ResourceSignal": {
                    "Timeout": "PT5M"
                }
            },
            "Properties": {
                "ImageId": "{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}",
                "KeyName": {"Ref": "KeyName"},
                "InstanceType": "t3.micro",
                "SecurityGroupIds": [{"Ref": "WebServerSecurityGroup"}],
                "IamInstanceProfile": {"Ref": "LogRoleInstanceProfile"},
                "UserData": {"Fn::Base64": {"Fn::Join": [ "", [
                    "#!/bin/bash\n",
                    "dnf update -y aws-cfn-bootstrap\n",
                    "dnf install -y amazon-cloudwatch-agent\n",
                    "/opt/aws/bin/cfn-init -v --stack ", {"Ref": "AWS::StackName"}, " --resource WebServerHost --region ", {"Ref": "AWS::Region"}, "\n",
                    "\n",
                    "# Verify Apache log directory exists and create if needed\n",
                    "mkdir -p /var/log/httpd\n",
                    "\n",
                    "# Start CloudWatch agent\n",
                    "/opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/etc/amazon-cloudwatch-agent/amazon-cloudwatch-agent.json -s\n",
                    "\n",
                    "# Signal success\n",
                    "/opt/aws/bin/cfn-signal -e $? --stack ", {"Ref": "AWS::StackName"}, " --resource WebServerHost --region ", {"Ref": "AWS::Region"}, "\n"
                ]]}}
            }
        },
        "WebServerLogGroup": {
            "Type": "AWS::Logs::LogGroup",
            "DeletionPolicy": "Retain",
            "UpdateReplacePolicy": "Retain",
            "Properties": {
                "RetentionInDays": 7
            }
        },
        "404MetricFilter": {
            "Type": "AWS::Logs::MetricFilter",
            "Properties": {
                "LogGroupName": {"Ref": "WebServerLogGroup"},
                "FilterPattern": "[ip, identity, user_id, timestamp, request, status_code = 404, size, ...]",
                "MetricTransformations": [
                    {
                        "MetricValue": "1",
                        "MetricNamespace": "test/404s",
                        "MetricName": "test404Count"
                    }
                ]
            }
        },
        "BytesTransferredMetricFilter": {
            "Type": "AWS::Logs::MetricFilter",
            "Properties": {
                "LogGroupName": {"Ref": "WebServerLogGroup"},
                "FilterPattern": "[ip, identity, user_id, timestamp, request, status_code, size, ...]",
                "MetricTransformations": [
                    {
                        "MetricValue": "$size",
                        "MetricNamespace": "test/BytesTransferred",
                        "MetricName": "testBytesTransferred"
                    }
                ]
            }
        },
        "404Alarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmDescription": "The number of 404s is greater than 2 over 2 minutes",
                "MetricName": "test404Count",
                "Namespace": "test/404s",
                "Statistic": "Sum",
                "Period": "60",
                "EvaluationPeriods": "2",
                "Threshold": "2",
                "AlarmActions": [{"Ref": "AlarmNotificationTopic"}],
                "ComparisonOperator": "GreaterThanThreshold"
            }
        },
        "BandwidthAlarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmDescription": "The average volume of traffic is greater 3500 KB over 10 minutes",
                "MetricName": "testBytesTransferred",
                "Namespace": "test/BytesTransferred",
                "Statistic": "Average",
                "Period": "300",
                "EvaluationPeriods": "2",
                "Threshold": "3500",
                "AlarmActions": [{"Ref": "AlarmNotificationTopic"}],
                "ComparisonOperator": "GreaterThanThreshold"
            }
        },
        "AlarmNotificationTopic": {
            "Type": "AWS::SNS::Topic",
            "Properties": {
                "Subscription": [{"Endpoint": {"Ref": "OperatorEmail"}, "Protocol": "email"}]
            }
        }
    },
    "Outputs": {
        "InstanceId": {
            "Description": "The instance ID of the web server",
            "Value": {"Ref": "WebServerHost"}
        },
        "WebsiteURL": {
            "Value": {"Fn::Sub": "http://${WebServerHost.PublicDnsName}"},
            "Description": "URL for the web server"
        },
        "PublicIP": {
            "Description": "Public IP address of the web server",
            "Value": {"Fn::GetAtt": ["WebServerHost","PublicIp"]
            }
        },
        "CloudWatchLogGroupName": {
            "Description": "The name of the CloudWatch log group",
            "Value": {"Ref": "WebServerLogGroup"}
        }
    }
}
```



### YAML



```
AWSTemplateFormatVersion: 2010-09-09
Description: Sample template that sets up and configures CloudWatch Logs on Amazon Linux 2023 instance.
Parameters:
  KeyName:
    Description: Name of an existing EC2 KeyPair to enable SSH access to the instances
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.
  SSHLocation:
    Description: The IP address range that can be used to SSH to the EC2 instances
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
  OperatorEmail:
    Description: Email address to notify when CloudWatch alarms are triggered (404 errors or high bandwidth usage)
    Type: String
Resources:
  LogRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17		 	 	 
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      Path: /
      Policies:
        - PolicyName: LogRolePolicy
          PolicyDocument:
            Version: 2012-10-17		 	 	 
            Statement:
              - Effect: Allow
                Action:
                  - 'logs:PutLogEvents'
                  - 'logs:DescribeLogStreams'
                  - 'logs:DescribeLogGroups'
                  - 'logs:CreateLogGroup'
                  - 'logs:CreateLogStream'
                Resource: '*'
  LogRoleInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref LogRole
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable HTTP access via port 80 and SSH access via port 22
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 80
          ToPort: 80
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: !Ref SSHLocation
  WebServerHost:
    Type: AWS::EC2::Instance
    Metadata:
      Comment: Install a simple PHP application on Amazon Linux 2023
      'AWS::CloudFormation::Init':
        config:
          packages:
            dnf:
              httpd: []
              php: []
              php-fpm: []
          files:
            /etc/amazon-cloudwatch-agent/amazon-cloudwatch-agent.json:
              content: !Sub |
                {
                  "logs": {
                    "logs_collected": {
                      "files": {
                        "collect_list": [
                          {
                            "file_path": "/var/log/httpd/access_log",
                            "log_group_name": "${WebServerLogGroup}",
                            "log_stream_name": "{instance_id}/apache.log",
                            "timestamp_format": "%d/%b/%Y:%H:%M:%S %z"
                          }
                        ]
                      }
                    }
                  }
                }
              mode: '000644'
              owner: root
              group: root
            /var/www/html/index.php:
              content: |
                <?php echo '<h1>AWS CloudFormation sample PHP application on Amazon Linux 2023</h1>';
                ?>
              mode: '000644'
              owner: apache
              group: apache
            /etc/cfn/cfn-hup.conf:
              content: !Sub |
                [main]
                stack=${AWS::StackId}
                region=${AWS::Region}
              mode: '000400'
              owner: root
              group: root
            /etc/cfn/hooks.d/cfn-auto-reloader.conf:
              content: !Sub |
                [cfn-auto-reloader-hook]
                triggers=post.update
                path=Resources.WebServerHost.Metadata.AWS::CloudFormation::Init
                action=/opt/aws/bin/cfn-init -s ${AWS::StackId} -r WebServerHost --region ${AWS::Region}
                runas=root
          services:
            systemd:
              httpd:
                enabled: 'true'
                ensureRunning: 'true'
              php-fpm:
                enabled: 'true'
                ensureRunning: 'true'
    CreationPolicy:
      ResourceSignal:
        Timeout: PT5M
    Properties:
      ImageId: '{{resolve:ssm:/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64}}'
      KeyName: !Ref KeyName
      InstanceType: t3.micro
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      IamInstanceProfile: !Ref LogRoleInstanceProfile
      UserData: !Base64
        Fn::Sub: |
          #!/bin/bash
          dnf update -y aws-cfn-bootstrap
          dnf install -y amazon-cloudwatch-agent
          /opt/aws/bin/cfn-init -v --stack ${AWS::StackName} --resource WebServerHost --region ${AWS::Region}
          
          # Verify Apache log directory exists and create if needed
          mkdir -p /var/log/httpd
          
          # Start CloudWatch agent
          /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -c file:/etc/amazon-cloudwatch-agent/amazon-cloudwatch-agent.json -s
          
          # Signal success
          /opt/aws/bin/cfn-signal -e $? --stack ${AWS::StackName} --resource WebServerHost --region ${AWS::Region}
          echo "Done"
  WebServerLogGroup:
    Type: AWS::Logs::LogGroup
    DeletionPolicy: Retain
    UpdateReplacePolicy: Retain
    Properties:
      RetentionInDays: 7
  404MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: !Ref WebServerLogGroup
      FilterPattern: >-
        [ip, identity, user_id, timestamp, request, status_code = 404, size, ...]
      MetricTransformations:
        - MetricValue: '1'
          MetricNamespace: test/404s
          MetricName: test404Count
  BytesTransferredMetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: !Ref WebServerLogGroup
      FilterPattern: '[ip, identity, user_id, timestamp, request, status_code, size, ...]'
      MetricTransformations:
        - MetricValue: $size
          MetricNamespace: test/BytesTransferred
          MetricName: testBytesTransferred
  404Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: The number of 404s is greater than 2 over 2 minutes
      MetricName: test404Count
      Namespace: test/404s
      Statistic: Sum
      Period: '60'
      EvaluationPeriods: '2'
      Threshold: '2'
      AlarmActions:
        - !Ref AlarmNotificationTopic
      ComparisonOperator: GreaterThanThreshold
  BandwidthAlarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: The average volume of traffic is greater 3500 KB over 10 minutes
      MetricName: testBytesTransferred
      Namespace: test/BytesTransferred
      Statistic: Average
      Period: '300'
      EvaluationPeriods: '2'
      Threshold: '3500'
      AlarmActions:
        - !Ref AlarmNotificationTopic
      ComparisonOperator: GreaterThanThreshold
  AlarmNotificationTopic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint: !Ref OperatorEmail
          Protocol: email
Outputs:
  InstanceId:
    Description: The instance ID of the web server
    Value: !Ref WebServerHost
  WebsiteURL:
    Value: !Sub 'http://${WebServerHost.PublicDnsName}'
    Description: URL for the web server
  PublicIP:
    Description: Public IP address of the web server
    Value: !GetAtt WebServerHost.PublicIp
  CloudWatchLogGroupName:
    Description: The name of the CloudWatch log group
    Value: !Ref WebServerLogGroup

```


## Send logs to CloudWatch Logs from a Windows
 instance


The following template configures CloudWatch Logs for a Windows 2012R2 instance.


The CloudWatch Logs agent on Windows (SSM agent on Windows 2012R2 and Windows 2016 AMIs) only
 sends logs after it's started, so any logs that are generated before startup aren't
 sent. To work around this, the template helps to ensure that the agent starts before any
 logs are written by:



* Configuring the agent setup as the first `config` item in cfn-init
 `configSets`.
* Using `waitAfterCompletion` to insert a pause after the command
 that starts the agent.


### JSON



```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Sample template that sets up and configures CloudWatch Logs on Windows 2012R2 instance.",
    "Parameters": {
        "KeyPair": {
            "Description": "Name of an existing EC2 KeyPair to enable RDP access to the instances",
            "Type": "AWS::EC2::KeyPair::KeyName",
            "ConstraintDescription": "must be the name of an existing EC2 KeyPair."
        },
        "RDPLocation": {
            "Description": "The IP address range that can be used to RDP to the EC2 instances",
            "Type": "String",
            "MinLength": "9",
            "MaxLength": "18",
            "Default": "0.0.0.0/0",
            "AllowedPattern": "(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})\\.(\\d{1,3})/(\\d{1,2})",
            "ConstraintDescription": "must be a valid IP CIDR range of the form x.x.x.x/x."
        },
        "OperatorEmail": {
            "Description": "Email address to notify when CloudWatch alarms are triggered (404 errors)",
            "Type": "String"
        }
    },
    "Resources": {
        "WebServerSecurityGroup": {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupDescription": "Enable HTTP access via port 80 and RDP access via port 3389",
                "SecurityGroupIngress": [
                    {
                        "IpProtocol": "tcp",
                        "FromPort": "80",
                        "ToPort": "80",
                        "CidrIp": "0.0.0.0/0"
                    },
                    {
                        "IpProtocol": "tcp",
                        "FromPort": "3389",
                        "ToPort": "3389",
                        "CidrIp": {"Ref": "RDPLocation"}
                    }
                ]
            }
        },
        "LogRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",		 	 	 
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Principal": {
                                "Service": [
                                    "ec2.amazonaws.com"
                                ]
                            },
                            "Action": [
                                "sts:AssumeRole"
                            ]
                        }
                    ]
                },
                "ManagedPolicyArns": [
                    "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
                ],
                "Path": "/",
                "Policies": [
                    {
                        "PolicyName": "LogRolePolicy",
                        "PolicyDocument": {
                            "Version": "2012-10-17",		 	 	 
                            "Statement": [
                                {
                                    "Effect": "Allow",
                                    "Action": [
                                        "logs:Create*",
                                        "logs:PutLogEvents",
                                        "s3:GetObject"
                                    ],
                                    "Resource": [
                                        "arn:aws:logs:*:*:*",
                                        "arn:aws:s3:::*"
                                    ]
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "LogRoleInstanceProfile": {
            "Type": "AWS::IAM::InstanceProfile",
            "Properties": {
                "Path": "/",
                "Roles": [{"Ref": "LogRole"}]
            }
        },
        "WebServerHost": {
            "Type": "AWS::EC2::Instance",
            "CreationPolicy": {
                "ResourceSignal": {
                    "Timeout": "PT15M"
                }
            },
            "Metadata": {
                "AWS::CloudFormation::Init": {
                    "configSets": {
                        "config": [
                            "00-ConfigureCWLogs",
                            "01-InstallWebServer",
                            "02-ConfigureApplication",
                            "03-Finalize"
                        ]
                    },
                    "00-ConfigureCWLogs": {
                        "files": {
                            "C:\\Program Files\\Amazon\\SSM\\Plugins\\awsCloudWatch\\AWS.EC2.Windows.CloudWatch.json": {
                                "content": {
                                    "EngineConfiguration": {
                                        "Components": [
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "ApplicationEventLog",
                                                "Parameters": {
                                                    "Levels": "7",
                                                    "LogName": "Application"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "SystemEventLog",
                                                "Parameters": {
                                                    "Levels": "7",
                                                    "LogName": "System"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "SecurityEventLog",
                                                "Parameters": {
                                                    "Levels": "7",
                                                    "LogName": "Security"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "EC2ConfigLog",
                                                "Parameters": {
                                                    "CultureName": "en-US",
                                                    "Encoding": "ASCII",
                                                    "Filter": "EC2ConfigLog.txt",
                                                    "LogDirectoryPath": "C:\\Program Files\\Amazon\\Ec2ConfigService\\Logs",
                                                    "TimeZoneKind": "UTC",
                                                    "TimestampFormat": "yyyy-MM-ddTHH:mm:ss.fffZ:"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CfnInitLog",
                                                "Parameters": {
                                                    "CultureName": "en-US",
                                                    "Encoding": "ASCII",
                                                    "Filter": "cfn-init.log",
                                                    "LogDirectoryPath": "C:\\cfn\\log",
                                                    "TimeZoneKind": "Local",
                                                    "TimestampFormat": "yyyy-MM-dd HH:mm:ss,fff"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "IISLogs",
                                                "Parameters": {
                                                    "CultureName": "en-US",
                                                    "Encoding": "UTF-8",
                                                    "Filter": "",
                                                    "LineCount": "3",
                                                    "LogDirectoryPath": "C:\\inetpub\\logs\\LogFiles\\W3SVC1",
                                                    "TimeZoneKind": "UTC",
                                                    "TimestampFormat": "yyyy-MM-dd HH:mm:ss"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.PerformanceCounterComponent.PerformanceCounterInputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "MemoryPerformanceCounter",
                                                "Parameters": {
                                                    "CategoryName": "Memory",
                                                    "CounterName": "Available MBytes",
                                                    "DimensionName": "",
                                                    "DimensionValue": "",
                                                    "InstanceName": "",
                                                    "MetricName": "Memory",
                                                    "Unit": "Megabytes"
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchApplicationEventLog",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/ApplicationEventLog",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchSystemEventLog",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/SystemEventLog",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchSecurityEventLog",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/SecurityEventLog",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchEC2ConfigLog",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/EC2ConfigLog",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchCfnInitLog",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/CfnInitLog",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatchIISLogs",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "LogGroup": {"Ref": "LogGroup"},
                                                    "LogStream": "{instance_id}/IISLogs",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            },
                                            {
                                                "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatch.CloudWatchOutputComponent,AWS.EC2.Windows.CloudWatch",
                                                "Id": "CloudWatch",
                                                "Parameters": {
                                                    "AccessKey": "",
                                                    "NameSpace": "Windows/Default",
                                                    "Region": {"Ref": "AWS::Region"},
                                                    "SecretKey": ""
                                                }
                                            }
                                        ],
                                        "Flows": {
                                            "Flows": [
                                                "ApplicationEventLog,CloudWatchApplicationEventLog",
                                                "SystemEventLog,CloudWatchSystemEventLog",
                                                "SecurityEventLog,CloudWatchSecurityEventLog",
                                                "EC2ConfigLog,CloudWatchEC2ConfigLog",
                                                "CfnInitLog,CloudWatchCfnInitLog",
                                                "IISLogs,CloudWatchIISLogs",
                                                "MemoryPerformanceCounter,CloudWatch"
                                            ]
                                        },
                                        "PollInterval": "00:00:05"
                                    },
                                    "IsEnabled": true
                                }
                            }
                        },
                        "commands": {
                            "0-enableSSM": {
                                "command": "powershell.exe -Command \"Set-Service -Name AmazonSSMAgent -StartupType Automatic\" ",
                                "waitAfterCompletion": "0"
                            },
                            "1-restartSSM": {
                                "command": "powershell.exe -Command \"Restart-Service AmazonSSMAgent \"",
                                "waitAfterCompletion": "30"
                            }
                        }
                    },
                    "01-InstallWebServer": {
                        "commands": {
                            "01_install_webserver": {
                                "command": "powershell.exe -Command \"Install-WindowsFeature Web-Server  -IncludeAllSubFeature\"",
                                "waitAfterCompletion": "0"
                            }
                        }
                    },
                    "02-ConfigureApplication": {
                        "files": {
                            "c:\\Inetpub\\wwwroot\\index.htm": {
                                "content": "<html> <head> <title>Test Application Page</title> </head> <body> <h1>Congratulations!! Your IIS server is configured.</h1> </body> </html>"
                            }
                        }
                    },
                    "03-Finalize": {
                        "commands": {
                            "00_signal_success": {
                                "command": {
                                    "Fn::Sub": "cfn-signal.exe -e 0 --resource WebServerHost --stack ${AWS::StackName} --region ${AWS::Region}"
                                },
                                "waitAfterCompletion": "0"
                            }
                        }
                    }
                }
            },
            "Properties": {
                "KeyName": {
                    "Ref": "KeyPair"
                },
                "ImageId": "{{resolve:ssm:/aws/service/ami-windows-latest/Windows_Server-2012-R2_RTM-English-64Bit-Base}}",
                "InstanceType": "t2.xlarge",
                "SecurityGroupIds": [{"Ref": "WebServerSecurityGroup"}],
                "IamInstanceProfile": {"Ref": "LogRoleInstanceProfile"},
                "UserData": {
                    "Fn::Base64": {
                        "Fn::Join": [
                            "",
                            [
                                "<script>\n",
                                "wmic product where \"description='Amazon SSM Agent' \" uninstall\n",
                                "wmic product where \"description='aws-cfn-bootstrap' \" uninstall \n",
                                "start /wait c:\\Windows\\system32\\msiexec /passive /qn /i https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-win64-latest.msi\n",
                                "powershell.exe -Command \"iwr https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe  -UseBasicParsing -OutFile C:\\AmazonSSMAgentSetup.exe\"\n",
                                "start /wait C:\\AmazonSSMAgentSetup.exe /install /quiet\n",
                                "cfn-init.exe -v -c config -s ", {"Ref": "AWS::StackName"}, " --resource WebServerHost --region ", {"Ref": "AWS::Region"}, " \n",
                                "</script>\n"
                            ]
                        ]
                    }
                }
            }
        },
        "LogGroup": {
            "Type": "AWS::Logs::LogGroup",
            "Properties": {
                "RetentionInDays": 7
            }
        },
        "404MetricFilter": {
            "Type": "AWS::Logs::MetricFilter",
            "Properties": {
                "LogGroupName": {"Ref": "LogGroup"},
                "FilterPattern": "[timestamps, serverip, method, uri, query, port, dash, clientip, useragent, status_code = 404, ...]",
                "MetricTransformations": [
                    {
                        "MetricValue": "1",
                        "MetricNamespace": "test/404s",
                        "MetricName": "test404Count"
                    }
                ]
            }
        },
        "404Alarm": {
            "Type": "AWS::CloudWatch::Alarm",
            "Properties": {
                "AlarmDescription": "The number of 404s is greater than 2 over 2 minutes",
                "MetricName": "test404Count",
                "Namespace": "test/404s",
                "Statistic": "Sum",
                "Period": "60",
                "EvaluationPeriods": "2",
                "Threshold": "2",
                "AlarmActions": [{"Ref": "AlarmNotificationTopic"}],
                "ComparisonOperator": "GreaterThanThreshold"
            }
        },
        "AlarmNotificationTopic": {
            "Type": "AWS::SNS::Topic",
            "Properties": {
                "Subscription": [{"Endpoint": {"Ref": "OperatorEmail"}, "Protocol": "email"}]
            }
        }
    },
    "Outputs": {
        "InstanceId": {
            "Description": "The instance ID of the web server",
            "Value": {"Ref": "WebServerHost"}
        },
        "WebsiteURL": {
            "Value": {"Fn::Sub": "http://${WebServerHost.PublicDnsName}"},
            "Description": "URL for the web server"
        },
        "PublicIP": {
            "Description": "Public IP address of the web server",
            "Value": {"Fn::GetAtt": ["WebServerHost","PublicIp"]}
        },
        "CloudWatchLogGroupName": {
            "Description": "The name of the CloudWatch log group",
            "Value": {"Ref": "LogGroup"}
        }
    }
}
```



### YAML



```
AWSTemplateFormatVersion: 2010-09-09
Description: >-
  Sample template that sets up and configures CloudWatch Logs on Windows 2012R2 instance.
Parameters:
  KeyPair:
    Description: Name of an existing EC2 KeyPair to enable RDP access to the instances
    Type: AWS::EC2::KeyPair::KeyName
    ConstraintDescription: must be the name of an existing EC2 KeyPair.
  RDPLocation:
    Description: The IP address range that can be used to RDP to the EC2 instances
    Type: String
    MinLength: '9'
    MaxLength: '18'
    Default: 0.0.0.0/0
    AllowedPattern: '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})/(\d{1,2})'
    ConstraintDescription: must be a valid IP CIDR range of the form x.x.x.x/x.
  OperatorEmail:
    Description: Email address to notify when CloudWatch alarms are triggered (404 errors)
    Type: String
Resources:
  WebServerSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Enable HTTP access via port 80 and RDP access via port 3389
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: '80'
          ToPort: '80'
          CidrIp: 0.0.0.0/0
        - IpProtocol: tcp
          FromPort: '3389'
          ToPort: '3389'
          CidrIp: !Ref RDPLocation
  LogRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: 2012-10-17		 	 	 
        Statement:
          - Effect: Allow
            Principal:
              Service:
                - ec2.amazonaws.com
            Action:
              - 'sts:AssumeRole'
      ManagedPolicyArns:
        - 'arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore'
      Path: /
      Policies:
        - PolicyName: LogRolePolicy
          PolicyDocument:
            Version: 2012-10-17		 	 	 
            Statement:
              - Effect: Allow
                Action:
                  - 'logs:Create*'
                  - 'logs:PutLogEvents'
                  - 's3:GetObject'
                Resource:
                  - 'arn:aws:logs:*:*:*'
                  - 'arn:aws:s3:::*'
  LogRoleInstanceProfile:
    Type: AWS::IAM::InstanceProfile
    Properties:
      Path: /
      Roles:
        - !Ref LogRole
  WebServerHost:
    Type: AWS::EC2::Instance
    CreationPolicy:
      ResourceSignal:
        Timeout: PT15M
    Metadata:
      'AWS::CloudFormation::Init':
        configSets:
          config:
            - 00-ConfigureCWLogs
            - 01-InstallWebServer
            - 02-ConfigureApplication
            - 03-Finalize
        00-ConfigureCWLogs:
          files:
            'C:\Program Files\Amazon\SSM\Plugins\awsCloudWatch\AWS.EC2.Windows.CloudWatch.json':
              content: !Sub |
                {
                  "EngineConfiguration": {
                      "Components": [
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "ApplicationEventLog",
                              "Parameters": {
                                  "Levels": "7",
                                  "LogName": "Application"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "SystemEventLog",
                              "Parameters": {
                                  "Levels": "7",
                                  "LogName": "System"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.EventLog.EventLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "SecurityEventLog",
                              "Parameters": {
                                  "Levels": "7",
                                  "LogName": "Security"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "EC2ConfigLog",
                              "Parameters": {
                                  "CultureName": "en-US",
                                  "Encoding": "ASCII",
                                  "Filter": "EC2ConfigLog.txt",
                                  "LogDirectoryPath": "C:\\Program Files\\Amazon\\Ec2ConfigService\\Logs",
                                  "TimeZoneKind": "UTC",
                                  "TimestampFormat": "yyyy-MM-ddTHH:mm:ss.fffZ:"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "CfnInitLog",
                              "Parameters": {
                                  "CultureName": "en-US",
                                  "Encoding": "ASCII",
                                  "Filter": "cfn-init.log",
                                  "LogDirectoryPath": "C:\\cfn\\log",
                                  "TimeZoneKind": "Local",
                                  "TimestampFormat": "yyyy-MM-dd HH:mm:ss,fff"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CustomLog.CustomLogInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "IISLogs",
                              "Parameters": {
                                  "CultureName": "en-US",
                                  "Encoding": "UTF-8",
                                  "Filter": "",
                                  "LineCount": "3",
                                  "LogDirectoryPath": "C:\\inetpub\\logs\\LogFiles\\W3SVC1",
                                  "TimeZoneKind": "UTC",
                                  "TimestampFormat": "yyyy-MM-dd HH:mm:ss"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.PerformanceCounterComponent.PerformanceCounterInputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "MemoryPerformanceCounter",
                              "Parameters": {
                                  "CategoryName": "Memory",
                                  "CounterName": "Available MBytes",
                                  "DimensionName": "",
                                  "DimensionValue": "",
                                  "InstanceName": "",
                                  "MetricName": "Memory",
                                  "Unit": "Megabytes"
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchApplicationEventLog",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/ApplicationEventLog",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchSystemEventLog",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/SystemEventLog",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchSecurityEventLog",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/SecurityEventLog",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchEC2ConfigLog",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/EC2ConfigLog",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchCfnInitLog",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/CfnInitLog",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatchLogsOutput,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatchIISLogs",
                              "Parameters": {
                                  "AccessKey": "",
                                  "LogGroup": "${LogGroup}",
                                  "LogStream": "{instance_id}/IISLogs",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          },
                          {
                              "FullName": "AWS.EC2.Windows.CloudWatch.CloudWatch.CloudWatchOutputComponent,AWS.EC2.Windows.CloudWatch",
                              "Id": "CloudWatch",
                              "Parameters": {
                                  "AccessKey": "",
                                  "NameSpace": "Windows/Default",
                                  "Region": "${AWS::Region}",
                                  "SecretKey": ""
                              }
                          }
                      ],
                      "Flows": {
                          "Flows": [
                              "ApplicationEventLog,CloudWatchApplicationEventLog",
                              "SystemEventLog,CloudWatchSystemEventLog",
                              "SecurityEventLog,CloudWatchSecurityEventLog",
                              "EC2ConfigLog,CloudWatchEC2ConfigLog",
                              "CfnInitLog,CloudWatchCfnInitLog",
                              "IISLogs,CloudWatchIISLogs",
                              "MemoryPerformanceCounter,CloudWatch"
                          ]
                      },
                      "PollInterval": "00:00:05"
                  },
                  "IsEnabled": true
                }
          commands:
            0-enableSSM:
              command: >-
                powershell.exe -Command "Set-Service -Name AmazonSSMAgent
                -StartupType Automatic" 
              waitAfterCompletion: '0'
            1-restartSSM:
              command: powershell.exe -Command "Restart-Service AmazonSSMAgent "
              waitAfterCompletion: '30'
        01-InstallWebServer:
          commands:
            01_install_webserver:
              command: >-
                powershell.exe -Command "Install-WindowsFeature Web-Server 
                -IncludeAllSubFeature"
              waitAfterCompletion: '0'
        02-ConfigureApplication:
          files:
            'c:\Inetpub\wwwroot\index.htm':
              content: >-
                <html> <head> <title>Test Application Page</title> </head>
                <body> <h1>Congratulations !! Your IIS server is
                configured.</h1> </body> </html>
        03-Finalize:
          commands:
            00_signal_success:
              command: !Sub >-
                cfn-signal.exe -e 0 --resource WebServerHost --stack
                ${AWS::StackName} --region ${AWS::Region}
              waitAfterCompletion: '0'
    Properties:
      KeyName: !Ref KeyPair
      ImageId: "{{resolve:ssm:/aws/service/ami-windows-latest/Windows_Server-2012-R2_RTM-English-64Bit-Base}}"
      InstanceType: t2.xlarge
      SecurityGroupIds:
        - !Ref WebServerSecurityGroup
      IamInstanceProfile: !Ref LogRoleInstanceProfile
      UserData: !Base64 
        'Fn::Sub': >
          <script>

          wmic product where "description='Amazon SSM Agent' " uninstall

          wmic product where "description='aws-cfn-bootstrap' " uninstall 

          start /wait c:\\Windows\\system32\\msiexec /passive /qn /i
          https://s3.amazonaws.com/cloudformation-examples/aws-cfn-bootstrap-win64-latest.msi

          powershell.exe -Command "iwr
          https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/windows_amd64/AmazonSSMAgentSetup.exe 
          -UseBasicParsing -OutFile C:\\AmazonSSMAgentSetup.exe"

          start /wait C:\\AmazonSSMAgentSetup.exe /install /quiet

          cfn-init.exe -v -c config -s ${AWS::StackName} --resource
          WebServerHost --region ${AWS::Region} 

          </script>
  LogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      RetentionInDays: 7
  404MetricFilter:
    Type: AWS::Logs::MetricFilter
    Properties:
      LogGroupName: !Ref LogGroup
      FilterPattern: >-
        [timestamps, serverip, method, uri, query, port, dash, clientip,
        useragent, status_code = 404, ...]
      MetricTransformations:
        - MetricValue: '1'
          MetricNamespace: test/404s
          MetricName: test404Count
  404Alarm:
    Type: AWS::CloudWatch::Alarm
    Properties:
      AlarmDescription: The number of 404s is greater than 2 over 2 minutes
      MetricName: test404Count
      Namespace: test/404s
      Statistic: Sum
      Period: '60'
      EvaluationPeriods: '2'
      Threshold: '2'
      AlarmActions:
        - !Ref AlarmNotificationTopic
      ComparisonOperator: GreaterThanThreshold
  AlarmNotificationTopic:
    Type: AWS::SNS::Topic
    Properties:
      Subscription:
        - Endpoint: !Ref OperatorEmail
          Protocol: email
Outputs:
  InstanceId:
    Description: The instance ID of the web server
    Value: !Ref WebServerHost
  WebsiteURL:
    Value: !Sub 'http://${WebServerHost.PublicDnsName}'
    Description: URL for the web server
  PublicIP:
    Description: Public IP address of the web server
    Value: !GetAtt 
      - WebServerHost
      - PublicIp
  CloudWatchLogGroupName:
    Description: The name of the CloudWatch log group
    Value: !Ref LogGroup

```


## See also


For more information about CloudWatch Logs resources, see [AWS::Logs::LogGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loggroup.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-loggroup.html") or
 [AWS::Logs::MetricFilter](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-metricfilter.html "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-logs-metricfilter.html").
