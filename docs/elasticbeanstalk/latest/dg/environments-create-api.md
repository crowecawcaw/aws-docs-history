# Creating Elastic Beanstalk environments with the API

1. Call `CheckDNSAvailability` with the following parameter:
   - `CNAMEPrefix` = `SampleApp`

###### Example

```
https://elasticbeanstalk.us-east-2.amazonaws.com/?CNAMEPrefix=sampleapplication
&Operation=CheckDNSAvailability
&AuthParams
```

2. Call `DescribeApplicationVersions` with the following
   parameters:
   - `ApplicationName` = `SampleApp`
   - `VersionLabel` = `Version2`

###### Example

```
https://elasticbeanstalk.us-east-2.amazonaws.com/?ApplicationName=SampleApp
&VersionLabel=Version2
&Operation=DescribeApplicationVersions
&AuthParams
```

3. Call `CreateConfigurationTemplate` with the following
   parameters:
   - `ApplicationName` = `SampleApp`
   - `TemplateName` = `MyConfigTemplate`
   - `SolutionStackName` =
     `64bit%20Amazon%20Linux%202015.03%20v2.0.0%20running%20Ruby%202.2%20(Passenger%20Standalone)`

###### Example

```
https://elasticbeanstalk.us-east-2.amazonaws.com/?ApplicationName=SampleApp
&TemplateName=MyConfigTemplate
&Operation=CreateConfigurationTemplate
&SolutionStackName=64bit%20Amazon%20Linux%202015.03%20v2.0.0%20running%20Ruby%202.2%20(Passenger%20Standalone)
&AuthParams
```

4. Call `CreateEnvironment` with one of the following sets of
   parameters.
   1. Use the following for a web server environment tier:
      - `EnvironmentName` = `SampleAppEnv2`
      - `VersionLabel` = `Version2`
      - `Description` = `description`
      - `TemplateName` = `MyConfigTemplate`
      - `ApplicationName` = `SampleApp`
      - `CNAMEPrefix` = `sampleapplication`
      - `OptionSettings.member.1.Namespace` =
        `aws:autoscaling:launchconfiguration`
      - `OptionSettings.member.1.OptionName` =
        `IamInstanceProfile`
      - `OptionSettings.member.1.Value` =
        `aws-elasticbeanstalk-ec2-role`

   ###### Example

   ```
   https://elasticbeanstalk.us-east-2.amazonaws.com/?ApplicationName=SampleApp
   &VersionLabel=Version2
   &EnvironmentName=SampleAppEnv2
   &TemplateName=MyConfigTemplate
   &CNAMEPrefix=sampleapplication
   &Description=description
   &Operation=CreateEnvironment
   &OptionSettings.member.1.Namespace=aws%3Aautoscaling%3Alaunchconfiguration
   &OptionSettings.member.1.OptionName=IamInstanceProfile
   &OptionSettings.member.1.Value=aws-elasticbeanstalk-ec2-role
   &AuthParams
   ```

   2. Use the following for a worker environment tier:
      - `EnvironmentName` = `SampleAppEnv2`
      - `VersionLabel` = `Version2`
      - `Description` = `description`
      - `TemplateName` = `MyConfigTemplate`
      - `ApplicationName` = `SampleApp`
      - `Tier` = `Worker`
      - `OptionSettings.member.1.Namespace` =
        `aws:autoscaling:launchconfiguration`
      - `OptionSettings.member.1.OptionName` =
        `IamInstanceProfile`
      - `OptionSettings.member.1.Value` =
        `aws-elasticbeanstalk-ec2-role`
      - `OptionSettings.member.2.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.2.OptionName` =
        `WorkerQueueURL`
      - `OptionSettings.member.2.Value` = `sqsd.elasticbeanstalk.us-east-2.amazonaws.com`
      - `OptionSettings.member.3.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.3.OptionName` =
        `HttpPath`
      - `OptionSettings.member.3.Value` = `/`
      - `OptionSettings.member.4.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.4.OptionName` =
        `MimeType`
      - `OptionSettings.member.4.Value` =
        `application/json`
      - `OptionSettings.member.5.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.5.OptionName` =
        `HttpConnections`
      - `OptionSettings.member.5.Value` = `75`
      - `OptionSettings.member.6.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.6.OptionName` =
        `ConnectTimeout`
      - `OptionSettings.member.6.Value` = `10`
      - `OptionSettings.member.7.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.7.OptionName` =
        `InactivityTimeout`
      - `OptionSettings.member.7.Value` = `10`
      - `OptionSettings.member.8.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.8.OptionName` =
        `VisibilityTimeout`
      - `OptionSettings.member.8.Value` = `60`
      - `OptionSettings.member.9.Namespace` =
        `aws:elasticbeanstalk:sqsd`
      - `OptionSettings.member.9.OptionName` =
        `RetentionPeriod`
      - `OptionSettings.member.9.Value` =
        `345600`

   ###### Example

   ```
   https://elasticbeanstalk.us-east-2.amazonaws.com/?ApplicationName=SampleApp
   &VersionLabel=Version2
   &EnvironmentName=SampleAppEnv2
   &TemplateName=MyConfigTemplate
   &Description=description
   &Tier=Worker
   &Operation=CreateEnvironment
   &OptionSettings.member.1.Namespace=aws%3Aautoscaling%3Alaunchconfiguration
   &OptionSettings.member.1.OptionName=IamInstanceProfile
   &OptionSettings.member.1.Value=aws-elasticbeanstalk-ec2-role
   &OptionSettings.member.2.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.2.OptionName=WorkerQueueURL
   &OptionSettings.member.2.Value=sqsd.elasticbeanstalk.us-east-2.amazonaws.com
   &OptionSettings.member.3.Namespace=aws%3elasticbeanstalk%3sqsd
   &OptionSettings.member.3.OptionName=HttpPath
   &OptionSettings.member.3.Value=%2F
   &OptionSettings.member.4.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.4.OptionName=MimeType
   &OptionSettings.member.4.Value=application%2Fjson
   &OptionSettings.member.5.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.5.OptionName=HttpConnections
   &OptionSettings.member.5.Value=75
   &OptionSettings.member.6.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.6.OptionName=ConnectTimeout
   &OptionSettings.member.6.Value=10
   &OptionSettings.member.7.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.7.OptionName=InactivityTimeout
   &OptionSettings.member.7.Value=10
   &OptionSettings.member.8.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.8.OptionName=VisibilityTimeout
   &OptionSettings.member.8.Value=60
   &OptionSettings.member.9.Namespace=aws%3Aelasticbeanstalk%3Asqsd
   &OptionSettings.member.9.OptionName=RetentionPeriod
   &OptionSettings.member.9.Value=345600
   &AuthParams
   ```
