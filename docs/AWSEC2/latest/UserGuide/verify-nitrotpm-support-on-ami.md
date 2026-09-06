

# Verify that an AMI is enabled for NitroTPM
<a name="verify-nitrotpm-support-on-ami"></a>

To enable NitroTPM for an instance, you must launch the instance using an AMI with NitroTPM enabled. You can describe an image to verify that it is enabled for NitroTPM. If you are the AMI owner, you can describe the `tpmSupport` image attribute.

The Amazon EC2 console does not display `TpmSupport`.

------
#### [ AWS CLI ]

**To verify that NitroTPM is enabled**  
Use the [describe-images](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html) command.

```
aws ec2 describe-images \
    --image-ids {{ami-0abcdef1234567890}} \
    --query Images[*].TpmSupport
```

If NitroTPM is enabled for the AMI, the output is as follows. If TPM is not enabled, the output is empty.

```
[
    "v2.0"
]
```

Alternatively, if you are the AMI owner, you can use the [describe-image-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-image-attribute.html) command with the `tpmSupport` attribute.

```
aws ec2 describe-image-attribute \
    --image-id {{ami-0abcdef1234567890}} \
    --attribute tpmSupport
```

 The following is example output.

```
{
    "ImageId": "{{ami-0abcdef1234567890}}",
    "TpmSupport": {
        "Value": "v2.0"
    }
}
```

**To find AMIs with NitroTPM enabled**  
The following example lists the IDs of the AMIs that you own with NitroTPM enabled.

```
aws ec2 describe-images \
    --owners self \
    --filters Name=tpm-support,Values=v2.0 \
    --query Images[].ImageId
```

------
#### [ PowerShell ]

**To verify that NitroTPM is enabled**  
Use the [Get-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2Image.html) cmdlet.

```
Get-EC2Image `
    -ImageId {{ami-0abcdef1234567890}} | Select TpmSupport
```

If NitroTPM is enabled for the AMI, the output is as follows. If TPM is not enabled, the output is empty.

```
TpmSupport
----------
v2.0
```

Alternatively, if you are the AMI owner, you can use the [Get-EC2ImageAttribute](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2ImageAttribute.html) cmdlet with the `tpmSupport` attribute.

```
Get-EC2ImageAttribute `
    -ImageId {{ami-0abcdef1234567890}} `
    -Attribute tpmSupport
```

**To find AMIs with NitroTPM enabled**  
The following example lists the IDs of the AMIs that you own with NitroTPM enabled.

```
Get-EC2Image `
    -Owner self `
    -Filter @{Name="tpm-support; Values="v2.0"} | Select ImageId
```

------