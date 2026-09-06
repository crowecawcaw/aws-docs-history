

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Update an AWS IoT FleetWise campaign
<a name="update-campaign-cli"></a>

You can use the [UpdateCampaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_UpdateCampaign.html) API operation to update an existing campaign. The following command uses AWS CLI.
+ Replace {{campaign-name}} with the name of the campaign that you're updating.
+ Replace {{action}} with one of the following:
  + `APPROVE` – Approves the campaign to allow AWS IoT FleetWise to deploy it to a vehicle or fleet.
  + `SUSPEND` – Suspends the campaign. The campaign is deleted from vehicles and all vehicles in the suspended campaign will stop sending data.
  + `RESUME` – Reactivates the `SUSPEND` campaign. The campaign is set to be redeployed to all vehicles on next check-in and the vehicles will resume sending data.
  + `UPDATE` – Updates the campaign by defining attributes and associating them with the campaign.
+ Replace {{description}} with a new description.

  The description can have up to 2,048 characters.
+ Replace {{data-extra-dimensions}} with specified vehicle attributes to enrich data collected during the campaign. For example, you can add vehicle make and model to the campaign, and AWS IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream. You can then query the data against vehicle make and model.

```
aws iotfleetwise update-campaign \
            --name {{campaign-name}} \
            --action {{action}} \
            --description {{description}} \
            --data-extra-dimensions {{data-extra-dimensions}}
```

If you [enabled encryption](key-management.md) using a customer managed AWS KMS key, include the following policy statement so that your role can invoke the `UpdateCampaign` API operation. 

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
                "kms:GenerateDataKey*",
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