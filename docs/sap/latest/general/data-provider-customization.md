# Customizing the AWS Data Provider for SAP

Some settings are hard coded in the AWS Data Provider for SAP. You can override existing settings or add new settings. For example, when AWS adds new instance types, you can add these to the AWS Data Provider for SAP configuration.

The AWS Data Provider for SAP creates a database by reading the configuration information from the available `config.properties`, files in this sequence:

- The JAR (Java Archive) file of the data provider application.
- The installation directory. This file is required only if you want to override or extend the current configuration. The default directories are as follows:
  - Linux – `/usr/local/ec2/aws-dataprovider/config.properties`
  - Windows – `C:\Program Files\Amazon\DataProvider\config.properties`

- The Regional S3 bucket. Replace <region> with the Region code for the Region (for example, `us-east-1`).

```
https://aws-sap-dataprovider-<region>.s3.<region>.amazonaws.com/config.properties
```

## Syntax Rules for Configuration Files

- The configuration files require a comma after the last value in every row.
- Spaces are not ignored in strings. The entire string between the commas, including any spaces, is accepted as the value.
- If there are multiple rows with the same instance type, the existing value for that type is overwritten.
- Capitalization in strings is case sensitive.

## User-Configurable EC2 Instance Types

The AWS Data Provider for SAP maintains a database of all relevant Amazon EC2 instance types for SAP.

Entries for EC2 instance types must be in a comma-separated list, as follows:

_ec2type,i-type,cpu,core,threads,t-ecu,ecu,hthread,l-map,w-map,speed,p-ecu,_

For example:

```
ec2type,r3.8xlarge,2,16,2,32,1,thread,eth0,lan2,10000,true,
```

where the following applies:

| Field name                          | Content                                                                                             | Example    | Type    | Description                                                                                                                     |
| ----------------------------------- | --------------------------------------------------------------------------------------------------- | ---------- | ------- | ------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **keyword**                         | ec2type                                                                                             | —          | String  | A token to identify a record with an EC2 instance description                                                                   |
| **i-type (instance-type)**          | [See list](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") | r3.8xlarge | String  | Instance type, which must match the EC2 instance metadata string                                                                |
| **cpu (CPUs)**                      | 1                                                                                                   | 2          | 2       | Integer                                                                                                                         | Number of sockets                                                                                         |
| **core (Cores)**                    | _integer_                                                                                           | 16         | Integer | Total number of processor cores                                                                                                 |
| **threads (threads per core)**      | 1                                                                                                   | 2          | 2       | Integer                                                                                                                         | Threads per core                                                                                          |
| **t-ecu (total ECU value)**         | _integer_                                                                                           | 32         | Double  | ECU value for previous-generation instance types that have ECU ratings; number of cores for post-ECU instance types             |
| **ecu (ECU per core)**              | _double_                                                                                            | 1          | Double  | 1 for all post-ECU instance types; total ECU divided by cores for previous<br>• generation instance types that have ECU ratings |
| **hthread (hyperthreading)**        | thread                                                                                              | core       | thread  | String                                                                                                                          | **thread\*<br>• for hyperthreaded instance types; **core\*<br>• for non<br>• hyperthreaded instance types |
| **l-map (Linux NIC mapping)**       | eth0                                                                                                | eth0       | String  | Linux mapping of network interface                                                                                              |
| **w-map (Windows NIC mapping)**     | eth0                                                                                                | lan2       | String  | Windows mapping of network interface                                                                                            |
| **speed (network interface speed)** | 1000                                                                                                | 2000       | 10000   | 100000                                                                                                                          | Integer                                                                                                   | Maximum speed of network interface, in KB |
| **p-ecu (post ECU)**                | true                                                                                                | false      | true    | Boolean                                                                                                                         | \*_true_<br>• for modern instances that don’t have ECU ratings                                            |

## User-Configurable EBS Volume Types

The AWS Data Provider for SAP maintains a database of all relevant EBS volume types for SAP.

Entries for EBS volume types must be in a comma-separated list, as follows:

_voltype,ebs-type,sample-time,_

For example:

```
voltype,io1,60,
```

where the following applies:

| Field name              | Content | Example | Type   | Description                                                 |
| ----------------------- | ------- | ------- | ------ | ----------------------------------------------------------- | ---------------------------------- | ------ | --------------------------------------------------------- |
| **keyword**             | voltype | —       | String | A token to identify a record with an EBS volume description |
| **ebs-type (EBS-type)** | io1     | gp2     | sc1    | st1                                                         | Io1                                | String | EBS type, which must match the EBS volume metadata string |
| **sample-time**         | 60      | 300     | 60     | Integer                                                     | CloudWatch sample time, in seconds |

###### Important

The sample time is required to calibrate the EBS metrics to the SAP monitoring requirements. Changes in the sample time will lead to incorrect EBS metrics in the SAP monitoring system.
