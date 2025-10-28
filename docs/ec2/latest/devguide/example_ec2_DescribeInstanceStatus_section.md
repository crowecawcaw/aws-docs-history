# Use `DescribeInstanceStatus` with an AWS SDK or CLI

The following code examples show how to use `DescribeInstanceStatus`.

CLI

**AWS CLI**

**To describe the status of an instance**

The following `describe-instance-status` example describes the current status of the specified instance.

```
`aws ec2 describe-instance-status \
 --instance-ids `i-1234567890abcdef0``

```

Output:

```
{
    "InstanceStatuses": [
        {
            "InstanceId": "i-1234567890abcdef0",
            "InstanceState": {
                "Code": 16,
                "Name": "running"
            },
            "AvailabilityZone": "us-east-1d",
            "SystemStatus": {
                "Status": "ok",
                "Details": [
                    {
                        "Status": "passed",
                        "Name": "reachability"
                    }
                ]
            },
            "InstanceStatus": {
                "Status": "ok",
                "Details": [
                    {
                        "Status": "passed",
                        "Name": "reachability"
                    }
                ]
            }
        }
    ]
}
```

For more information, see [Monitor the status of your instances](../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check.md "../../../AWSEC2/latest/UserGuide/monitoring-instances-status-check.md") in the _Amazon EC2 User Guide_.

- For API details, see
  [DescribeInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-status.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-status.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the status of the specified instance.**

```
Get-EC2InstanceStatus -InstanceId i-12345678

```

**Output:**

```
AvailabilityZone : us-west-2a
Events           : {}
InstanceId       : i-12345678
InstanceState    : Amazon.EC2.Model.InstanceState
Status           : Amazon.EC2.Model.InstanceStatusSummary
SystemStatus     : Amazon.EC2.Model.InstanceStatusSummary
```

```
$status = Get-EC2InstanceStatus -InstanceId i-12345678
$status.InstanceState

```

**Output:**

```
Code    Name
----    ----
16      running
```

```
$status.Status

```

**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```

```
$status.SystemStatus

```

**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```

- For API details, see
  [DescribeInstanceStatus](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the status of the specified instance.**

```
Get-EC2InstanceStatus -InstanceId i-12345678

```

**Output:**

```
AvailabilityZone : us-west-2a
Events           : {}
InstanceId       : i-12345678
InstanceState    : Amazon.EC2.Model.InstanceState
Status           : Amazon.EC2.Model.InstanceStatusSummary
SystemStatus     : Amazon.EC2.Model.InstanceStatusSummary
```

```
$status = Get-EC2InstanceStatus -InstanceId i-12345678
$status.InstanceState

```

**Output:**

```
Code    Name
----    ----
16      running
```

```
$status.Status

```

**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```

```
$status.SystemStatus

```

**Output:**

```
Details           Status
-------           ------
{reachability}    ok
```

- For API details, see
  [DescribeInstanceStatus](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ec2#code-examples").

```
async fn show_all_events(client: &Client) -> Result<(), Error> {
    let resp = client.describe_regions().send().await.unwrap();

    for region in resp.regions.unwrap_or_default() {
        let reg: &'static str = Box::leak(Box::from(region.region_name().unwrap()));
        let region_provider = RegionProviderChain::default_provider().or_else(reg);
        let config = aws_config::from_env().region(region_provider).load().await;
        let new_client = Client::new(&config);

        let resp = new_client.describe_instance_status().send().await;

        println!("Instances in region {}:", reg);
        println!();

        for status in resp.unwrap().instance_statuses() {
            println!(
                "  Events scheduled for instance ID: {}",
                status.instance_id().unwrap_or_default()
            );
            for event in status.events() {
                println!("    Event ID:     {}", event.instance_event_id().unwrap());
                println!("    Description:  {}", event.description().unwrap());
                println!("    Event code:   {}", event.code().unwrap().as_ref());
                println!();
            }
        }
    }

    Ok(())
}


```

- For API details, see
  [DescribeInstanceStatus](https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_instance_status "https://docs.rs/aws-sdk-ec2/latest/aws_sdk_ec2/client/struct.Client.html#method.describe_instance_status")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
