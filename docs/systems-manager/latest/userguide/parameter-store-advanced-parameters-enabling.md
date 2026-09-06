

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Changing a standard parameter to an advanced parameter
<a name="parameter-store-advanced-parameters-enabling"></a>

Use the following procedure to change an existing standard parameter to an advanced parameter. For information about how to create a new advanced parameter, see [Creating Parameter Store parameters in Systems Manager](sysman-paramstore-su-create.md).

------
#### [ Console ]

**To change a standard parameter to an advanced parameter**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Parameter Store**.

1. Choose a parameter, and then choose **Edit**.

1. For **Description**, enter information about this parameter.

1. Choose **Advanced**.

1. For **Value**, enter the value of this parameter. Advanced parameters have a maximum value limit of 8 KB.

1. Choose **Save changes**.

------
#### [ AWS CLI ]

You can override the default setting by specifying the parameter tier using the `[PutParameter](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html)` operation. For example, you might want to share the default AMI value across AWS accounts. The following AWS CLI example explicitly sets the parameter tier to `Advanced` for the `default-ami` parameter in Linux & macOS.

```
aws ssm put-parameter \
    --region us-east-1 \
    --name "default-ami" \
    --type "String" \
    --value "t3.micro" \
    --tier "Advanced"
```

------