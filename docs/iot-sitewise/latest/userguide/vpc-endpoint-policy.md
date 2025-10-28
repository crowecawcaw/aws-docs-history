# Create a VPC endpoint policy for AWS IoT SiteWise

You can attach an endpoint policy to your VPC endpoint that controls access to
AWS IoT SiteWise. The policy specifies the following information:

- The principal that can perform operations.
- The operations that can be performed.
- The resources on which operations can be performed.
  For more information, see [Control access to VPC endpoints using
  endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example: VPC endpoint policy for AWS IoT SiteWise actions

The following is an example of an endpoint policy for AWS IoT SiteWise. When attached to an
endpoint, this policy grants access to the listed AWS IoT SiteWise actions for the user
`iotsitewiseadmin` in AWS account
`123456789012` on the specified asset.

```
{
    "Statement": [
        {
            "Action": [
                "iotsitewise:CreateAsset",
                "iotsitewise:ListGateways",
                "iotsitewise:ListTagsForResource"
            ],
            "Effect": "Allow",
            "Resource": "arn:aws:iotsitewise:us-west-2:123456789012:asset/a1b2c3d4-5678-90ab-cdef-33333EXAMPLE",
            "Principal": {
                "AWS": [
                    "123456789012:user/iotsitewiseadmin"
                ]
            }
        }
    ]
}
```
