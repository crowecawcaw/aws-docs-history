

# [CT.EC2.PV.2] Require that an attached Amazon EBS volume is configured to encrypt data at rest
<a name="ct-ec2-pv-2"></a>

This control disallows attaching an unencrypted EBS volume to a running or stopped EC2 instance.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service: **Amazon EC2

**Control metadata**
+ **Control objective: **Encrypt data at rest
+ **Implementation: **Service control policy (SCP)
+ **Control behavior: **Preventive
+ **Control owner: **AWS Control Tower
+ **Control groups: **digital-sovereignty
+ **Resource types: **`AWS::EC2::Volume`

**Usage considerations**  
This control does not prevent replacing an EBS-backed root volume for a running instance with an unencrypted volume, by means of the `CreateReplaceRootVolumeTask` operation.
AWS Control Tower recommends that you enable EBS encryption by default. For information about EBS encryption by default, see [Encryption by default](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html#encryption-by-default) in the *Amazon EC2 User Guide for Linux Instances*.
This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](https://docs.aws.amazon.com/controltower/latest/controlreference/control-parameter-concepts.html).

 The artifact for this control is the following service control policy (SCP). 

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "CTEC2PV2",
            "Effect": "Deny",
            "Action": "ec2:AttachVolume",
            "Resource": "arn:*:ec2:*:*:volume/*",
            "Condition": {
                "Bool": {
                    "ec2:Encrypted": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}
```