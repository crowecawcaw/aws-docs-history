

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Get AWS IoT FleetWise state template information
<a name="get-state-template"></a>

**Important**  
Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md).

You can use the [GetStateTemplate](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_GetStateTemplate.html) API operation to retrieve information about a state template. The following example uses the AWS CLI.

Replace {{identifier}} with the name of the state template.

```
aws iotfleetwise get-state-template \
    --identifier {{idenitfier}}
```

You can use the [ListStateTemplates](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_ListStateTemplates.html) API operation to retrieve a list of your created state templates. The following example uses the AWS CLI.

```
aws iotfleetwise list-state-templates 
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `GetStateTemplate` or `ListStateTemplates` API operations.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:{{us-east-1}}:{{111122223333}}:key/{{KMS_KEY_ID}}"
            ]
        }
    ]
}
```

------