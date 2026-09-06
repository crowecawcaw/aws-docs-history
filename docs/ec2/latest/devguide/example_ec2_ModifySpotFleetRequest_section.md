

# Use `ModifySpotFleetRequest` with a CLI
<a name="example_ec2_ModifySpotFleetRequest_section"></a>

The following code examples show how to use `ModifySpotFleetRequest`.

------
#### [ CLI ]

**AWS CLI**  
**To modify a Spot fleet request**  
This example command updates the target capacity of the specified Spot fleet request.  
Command:  

```
aws ec2 modify-spot-fleet-request --target-capacity {{20}} --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}
```
Output:  

```
{
    "Return": true
}
```
This example command decreases the target capacity of the specified Spot fleet request without terminating any Spot Instances as a result.  
Command:  

```
aws ec2 modify-spot-fleet-request --target-capacity {{10}} --excess-capacity-termination-policy {{NoTermination}} --spot-fleet-request-id {{sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE}}
```
Output:  

```
{
    "Return": true
}
```
+  For API details, see [ModifySpotFleetRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-spot-fleet-request.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the target capacity of the specified Spot fleet request.**  

```
Edit-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TargetCapacity 10
```
**Output:**  

```
True
```
+  For API details, see [ModifySpotFleetRequest](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the target capacity of the specified Spot fleet request.**  

```
Edit-EC2SpotFleetRequest -SpotFleetRequestId sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE -TargetCapacity 10
```
**Output:**  

```
True
```
+  For API details, see [ModifySpotFleetRequest](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.