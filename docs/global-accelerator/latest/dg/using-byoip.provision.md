

# Provision the address range for use with Global Accelerator
<a name="using-byoip.provision"></a>

When you provision an address range for use with AWS, you are confirming that you own the address range and authorize Amazon to advertise it. We'll verify that you own the address range.

You must provision your address range using the CLI or Global Accelerator API operations. This functionality is not available in the AWS console.

To provision the address range, use the following [ProvisionByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ProvisionByoipCidr.html) command. The `--cidr-authorization-context` parameter uses the variables that you created in the previous section, not the ROA message.

```
aws globalaccelerator --region us-west-2 provision-byoip-cidr --cidr {{address-range}} --cidr-authorization-context Message="$text_message",Signature="$signed_message"
```

The following is an example of provisioning an address range.

```
aws globalaccelerator --region us-west-2 provision-byoip-cidr \
    --cidr 203.0.113.0/24 \
    --cidr-authorization-context Message="$text_message",Signature="$signed_message"
```

Provisioning an address range is an asynchronous operation, so the call returns immediately. However, the address range is not ready to use until its state changes from `PENDING_PROVISIONING` to `READY`. It can take up to 3 weeks to complete the provisioning process. To monitor the state of the address ranges that you've provisioned, use the following [ ListByoipCidrs](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ListByoipCidrs.html) command:

```
aws globalaccelerator --region us-west-2 list-byoip-cidrs
```

To see a list of the states for an IP address range, see [ByoipCidr](https://docs.aws.amazon.com/global-accelerator/latest/api/API_ByoipCidr.html). 

When your IP address range is provisioned, the `State` returned by `list-byoip-cidrs` is `READY`. For example:

```
{
    "ByoipCidrs": [
        {
            "Cidr": "203.0.113.0/24",
            "State": "READY"
        }
    ]
}
```