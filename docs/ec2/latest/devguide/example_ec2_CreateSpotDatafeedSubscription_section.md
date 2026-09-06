

# Use `CreateSpotDatafeedSubscription` with a CLI
<a name="example_ec2_CreateSpotDatafeedSubscription_section"></a>

The following code examples show how to use `CreateSpotDatafeedSubscription`.

------
#### [ CLI ]

**AWS CLI**  
**To create a Spot Instance data feed**  
The following `create-spot-datafeed-subscription` example creates a Spot Instance data feed.  

```
aws ec2 create-spot-datafeed-subscription \
    --bucket {{amzn-s3-demo-bucket}} \
    --prefix {{spot-data-feed}}
```
Output:  

```
{
    "SpotDatafeedSubscription": {
        "Bucket": "amzn-s3-demo-bucket",
        "OwnerId": "123456789012",
        "Prefix": "spot-data-feed",
        "State": "Active"
    }
}
```
The data feed is stored in the Amazon S3 bucket that you specified. The file names for this data feed have the following format.  

```
amzn-s3-demo-bucket.s3.amazonaws.com/spot-data-feed/123456789012.YYYY-MM-DD-HH.n.abcd1234.gz
```
For more information, see [Spot Instance data feed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html) in the *Amazon EC2 User Guide*.  
+  For API details, see [CreateSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-spot-datafeed-subscription.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example creates a Spot instance data feed.**  

```
New-EC2SpotDatafeedSubscription -Bucket amzn-s3-demo-bucket -Prefix spotdata
```
**Output:**  

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [CreateSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example creates a Spot instance data feed.**  

```
New-EC2SpotDatafeedSubscription -Bucket amzn-s3-demo-bucket -Prefix spotdata
```
**Output:**  

```
Bucket  : amzn-s3-demo-bucket
Fault   :
OwnerId : 123456789012
Prefix  : spotdata
State   : Active
```
+  For API details, see [CreateSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.