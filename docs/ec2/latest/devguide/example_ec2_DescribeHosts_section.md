

# Use `DescribeHosts` with a CLI
<a name="example_ec2_DescribeHosts_section"></a>

The following code examples show how to use `DescribeHosts`.

------
#### [ CLI ]

**AWS CLI**  
**To view details about Dedicated Hosts**  
The following `describe-hosts` example displays details for the `available` Dedicated Hosts in your AWS account.  

```
aws ec2 describe-hosts --filter {{"Name=state,Values=available"}}
```
Output:  

```
{
    "Hosts": [
        {
            "HostId": "h-07879acf49EXAMPLE",
            "Tags": [
                {
                    "Value": "production",
                    "Key": "purpose"
                }
            ],
            "HostProperties": {
                "Cores": 48,
                "TotalVCpus": 96,
                "InstanceType": "m5.large",
                "Sockets": 2
            },
            "Instances": [],
            "State": "available",
            "AvailabilityZone": "eu-west-1a",
            "AvailableCapacity": {
                "AvailableInstanceCapacity": [
                    {
                        "AvailableCapacity": 48,
                        "InstanceType": "m5.large",
                        "TotalCapacity": 48
                    }
                ],
                "AvailableVCpus": 96
            },
            "HostRecovery": "on",
            "AllocationTime": "2019-08-19T08:57:44.000Z",
            "AutoPlacement": "off"
        }
    ]
}
```
For more information, see [Viewing Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-managing) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.  
+  For API details, see [DescribeHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example returns the EC2 host details**  

```
Get-EC2Host
```
**Output:**  

```
AllocationTime    : 3/23/2019 4:55:22 PM
AutoPlacement     : off
AvailabilityZone  : eu-west-1b
AvailableCapacity : Amazon.EC2.Model.AvailableCapacity
ClientToken       :
HostId            : h-01e23f4cd567890f1
HostProperties    : Amazon.EC2.Model.HostProperties
HostReservationId :
Instances         : {}
ReleaseTime       : 1/1/0001 12:00:00 AM
State             : available
Tags              : {}
```
**Example 2: This example queries the AvailableInstanceCapacity for the host h-01e23f4cd567899f1**  

```
Get-EC2Host -HostId h-01e23f4cd567899f1 | Select-Object -ExpandProperty AvailableCapacity | Select-Object -expand AvailableInstanceCapacity
```
**Output:**  

```
AvailableCapacity InstanceType TotalCapacity
----------------- ------------ -------------
11                m4.xlarge    11
```
+  For API details, see [DescribeHosts](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example returns the EC2 host details**  

```
Get-EC2Host
```
**Output:**  

```
AllocationTime    : 3/23/2019 4:55:22 PM
AutoPlacement     : off
AvailabilityZone  : eu-west-1b
AvailableCapacity : Amazon.EC2.Model.AvailableCapacity
ClientToken       :
HostId            : h-01e23f4cd567890f1
HostProperties    : Amazon.EC2.Model.HostProperties
HostReservationId :
Instances         : {}
ReleaseTime       : 1/1/0001 12:00:00 AM
State             : available
Tags              : {}
```
**Example 2: This example queries the AvailableInstanceCapacity for the host h-01e23f4cd567899f1**  

```
Get-EC2Host -HostId h-01e23f4cd567899f1 | Select-Object -ExpandProperty AvailableCapacity | Select-Object -expand AvailableInstanceCapacity
```
**Output:**  

```
AvailableCapacity InstanceType TotalCapacity
----------------- ------------ -------------
11                m4.xlarge    11
```
+  For API details, see [DescribeHosts](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.