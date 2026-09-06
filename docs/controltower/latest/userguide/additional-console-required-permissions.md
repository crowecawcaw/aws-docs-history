

# Permissions Required to use the AWS Control Tower console
<a name="additional-console-required-permissions"></a>

AWS Control Tower creates three roles automatically when you set up a landing zone. All three roles are required to allow console access. AWS Control Tower splits permissions into three roles as a best practice to restrict access to the minimal sets of actions and resources.

**Three required roles for landing zone access**
+ [AWSControlTowerAdmin role](access-control-managing-permissions.md#AWSControlTowerAdmin)
+ [AWSControlTowerStackSetRole](access-control-managing-permissions.md#AWSControlTowerStackSetRole)
+ [AWSControlTowerCloudTrailRole](access-control-managing-permissions.md#AWSControlTowerCloudTrailRolePolicy)

We recommend that you restrict access to your role trust policies for these roles. For more information, see [Optional conditions for your role trust relationships](https://docs.aws.amazon.com/controltower/latest/userguide/conditions-for-role-trust.html).

## View the Control Catalog in the console
<a name="view-control-catalog-in-console"></a>

To view control information in the AWS Control Tower console, you must add additional `controlcatalog` permissions to your IAM policies. These permissions are as follows:
+ `controlcatalog:GetControl`
+ `controlcatalog:ListControls`
+ `controlcatalog:ListControlMappings`
+ `controlcatalog:ListCommonControls`

Here's an example showing the updated permissions in the policy.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Action": [
                "controlcatalog:GetControl",
                "controlcatalog:ListControls",
                "controlcatalog:ListControlMappings",
                "controlcatalog:ListCommonControls"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow"
        }
    ]
}
```

------

You must add these permissions because AWS Control Tower calls the `controlcatalog` APIs to retrieve certain control metadata, so the AWS Control Tower permissions are not sufficient.

To find more information about how to update your permissions, see [Create roles and assign permissions](https://docs.aws.amazon.com/controltower/latest/userguide/assign-permissions.html).

To find more information about `controlcatalog` IAM actions, see [Actions, resources, and condition keys for Control Catalog](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awscontrolcatalog.html).

**Note**  
Control information is available through the [Control Catalog APIs](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/Welcome.html).