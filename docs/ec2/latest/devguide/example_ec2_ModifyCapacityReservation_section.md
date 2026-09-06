

# Use `ModifyCapacityReservation` with a CLI
<a name="example_ec2_ModifyCapacityReservation_section"></a>

The following code examples show how to use `ModifyCapacityReservation`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To change the number of instances reserved by an existing capacity reservation**  
The following `modify-capacity-reservation` example changes the number of instances for which the capacity reservation reserves capacity.  

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id {{cr-1234abcd56EXAMPLE}} \
    --instance-count {{5}}
```
Output:  

```
{
    "Return": true
}
```
For more information, see [Modify a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify.html) in the *Amazon EC2 User Guide*.  
**Example 2: To change the end date and time for an existing capacity reservation**  
The following `modify-capacity-reservation` example modifies an existing capacity reservation to end at the specified date and time.  

```
aws ec2 modify-capacity-reservation \
    --capacity-reservation-id {{cr-1234abcd56EXAMPLE}} \
    --end-date-type {{limited}} \
    --end-date {{2019-08-31T23:59:59Z}}
```
For more information, see [Modify a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [ModifyCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-capacity-reservation.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example modifies the CapacityReservationId cr-0c1f2345db6f7cdba by changing the instane count to 1**  

```
Edit-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba -InstanceCount 1
```
**Output:**  

```
True
```
+  For API details, see [ModifyCapacityReservation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example modifies the CapacityReservationId cr-0c1f2345db6f7cdba by changing the instane count to 1**  

```
Edit-EC2CapacityReservation -CapacityReservationId cr-0c1f2345db6f7cdba -InstanceCount 1
```
**Output:**  

```
True
```
+  For API details, see [ModifyCapacityReservation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.