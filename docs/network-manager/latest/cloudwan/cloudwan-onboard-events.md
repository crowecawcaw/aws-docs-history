

# Onboard CloudWatch Logs Insights for AWS Cloud WAN
<a name="cloudwan-onboard-events"></a>

Before viewing events on the Events dashboard, you must complete a one-time setup that registers your events with CloudWatch Logs Insights. Until you register your events, you'll be unable to view any of your events on the dashboard.

**To onboard CloudWatch Logs Insights**

Before you begin, verify that an AWS Identity and Access Management (IAM) principal (user) in your account has the appropriate permissions to onboard to CloudWatch Logs Insights. Ensure that the IAM policy contains the following permissions.

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
                "events:PutTargets",
                "events:DescribeRule",
                "logs:PutResourcePolicy",
                "logs:DescribeLogGroups",
                "logs:DescribeResourcePolicies",
                "events:PutRule",
                "logs:CreateLogGroup"
            ],
            "Resource": "*"
        }
    ]
}
```

------

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Core network**.

1. The **Overview** page opens by default. 

1. Choose the **Events** tab.

1. Choose **Onboard to CloudWatch Logs Insights**.

1. When you onboard to CloudWatch Logs Insights, the following occurs:
   + An EventBridge rule with the name `DON_NOT_DELETE_networkmanager_rule` is created in the US West (Oregon) Region.
   + A CloudWatch Logs group with the name `/aws/events/networkmanagerloggroup` is created in the US West (Oregon) Region.
   + An EventBridge rule is configured with the CloudWatch Logs group as a target.
   + A resource policy named `DO_NOT_DELETE_networkmanager_TrustEventsToStoreLogEvents` is created in the US West (Oregon) Region.

     To view this policy, run the following AWS CLI command:

     `aws logs describe-resource-policies --region us-west-2`