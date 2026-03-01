# Sharing CloudWatch dashboards

You can share your CloudWatch dashboards with people who do not have direct access to your
AWS account. This enables you to share dashboards across teams, with stakeholders, and
with people external to your organization. You can even display dashboards on big
screens in team areas, or embed them in Wikis and other webpages.

###### Warning

All people who you share the dashboard with are granted the permissions
listed in [Permissions that are granted to people who you share the dashboard with](#share-cloudwatch-dashboard-iamrole "#share-cloudwatch-dashboard-iamrole") for the account. If you share
the dashboard publicly, then everyone who has the link to the dashboard has these permissions.

The `cloudwatch:GetMetricData` and `ec2:DescribeTags` permissions cannot be scoped down
to specific metrics or EC2 instances, so the people with access to the dashboard can query all CloudWatch metrics

and the names and tags of all EC2 instances in the account.

When you share dashboards, you can designate who can view the dashboard in three ways:

- Share a single dashboard and designate as many as five email addresses of people
  who can view the dashboard. Each of these users creates their own password that
  they must enter to view the dashboard.
- Share a single dashboard publicly, so that anyone who has the link can view the dashboard.
- Share all the CloudWatch dashboards in your account and specify a third-party
  single sign-on (SSO)
  provider for dashboard access. All users who are members
  of this SSO provider's list can access all the dashboards in the account. To enable
  this, you integrate the SSO provider with Amazon Cognito. The SSO provider must support
  Security Assertion Markup Language (SAML). For more information about
  Amazon Cognito, see [What is Amazon Cognito?](../../../cognito/latest/developerguide/what-is-amazon-cognito.md "../../../cognito/latest/developerguide/what-is-amazon-cognito.md")
  Sharing a dashboard doesn't incur charges, but widgets inside a shared dashboard incur charges at standard
  CloudWatch rates. For more information about CloudWatch pricing, see
  [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

When you share a dashboard, Amazon Cognito resources are created in the US East (N. Virginia) Region.

###### Important

Do not modify resource names and identifiers that are created by the dashboard sharing process.
This includes Amazon Cognito and IAM resources. Modifying these resources
can cause unexpected and incorrect functionality of shared dashboards.

###### Note

If you share a dashboard that has metric widgets with alarm annotations, the people
that you share the dashboard with will not see those widgets. They will instead see a blank widget with text saying
that the widget is not available. You will still see metric widgets with alarm annotations when you view
the dashboard yourself.

## Permissions required to share a dashboard

To be able to share dashboards using any of the following methods and to see
which dashboards have already been
shared, you must be signed on as a user or with an IAM role that has certain
permissions.

To be able to share dashboards, your user or IAM role must include the
permissions included in the following policy
statement:

```
{
    "Effect": "Allow",
    "Action": [
        "iam:CreateRole",
        "iam:CreatePolicy",
        "iam:AttachRolePolicy",
        "iam:PassRole"
    ],
    "Resource": [
        "arn:aws:iam::*:role/service-role/CWDBSharing*",
        "arn:aws:iam::*:policy/*"
    ]
},
{
    "Effect": "Allow",
    "Action": [
        "cognito-idp:*",
        "cognito-identity:*",
    ],
    "Resource": [
        "*"
    ]
},
{
    "Effect": "Allow",
    "Action": [
        "cloudwatch:GetDashboard",
    ],
    "Resource": [
        "*"
        // or the ARNs of dashboards that you want to share
    ]
}
```

To be able to see which dashboards are shared, but not be able to
share dashboards, a user or an IAM role can include a policy
statement similar to the following:

```
{
    "Effect": "Allow",
    "Action": [
        "cognito-idp:*",
        "cognito-identity:*"
    ],
    "Resource": [
        "*"
    ]
},
{
    "Effect": "Allow",
    "Action": [
        "cloudwatch:ListDashboards",
    ],
    "Resource": [
        "*"
    ]
}
```

## Permissions that are granted to people who you share the dashboard with

When you share a dashboard, CloudWatch creates an IAM role in the account which gives the following permissions
to the people who you share the dashboard with:

- `cloudwatch:GetInsightRuleReport`
- `cloudwatch:GetMetricData`
- `cloudwatch:DescribeAlarms`
- `ec2:DescribeTags`

###### Warning

All people who you share the dashboard with are granted these permissions for the account. If you share
the dashboard publicly, then everyone who has the link to the dashboard has these permissions.

The `cloudwatch:GetMetricData` and `ec2:DescribeTags` permissions cannot be scoped down
to specific metrics or EC2 instances, so the people with access to the dashboard can query all CloudWatch metrics

and the names and tags of all EC2 instances in the account.

When you share a dashboard, by default the permissions that CloudWatch creates restrict access to only the alarms and Contributor Insights rules
that are on the dashboard when it is shared. If you add new alarms or Contributor Insights rules to the dashboard and want them to also
be seen by the people who you shared the dashboard with, you must update the policy to allow these resources.

## Allowing people that you share with to see composite alarms

When you share a dashboard, by default the composite alarm widgets on the dashboard are not visible to the people who you share the dashboard with.
For composite alarm widgets to be visible, you need to add a `DescribeAlarms: *` permission to the dashboard sharing policy. That permission
would look like this:

```
{
    "Effect": "Allow",
    "Action": "cloudwatch:DescribeAlarms",
    "Resource": "*"
}
```

###### Warning

The preceding policy statement give access to all alarms in the account. To reduce the scope of `cloudwatch:DescribeAlarms`, you must use
a `Deny` statement. You can add a `Deny` statement to the policy and specify the ARNs of the alarms that you want to lock down.
That deny statement should look similar to the following:

```
{
    "Effect": "Allow",
    "Action": "cloudwatch:DescribeAlarms",
    "Resource": "*"
},
{
    "Effect": "Deny",
    "Action": "cloudwatch:DescribeAlarms",
    "Resource": [
        "SensitiveAlarm1ARN",
        "SensitiveAlarm1ARN"
    ]
}
```

## Allowing people that you share with to see logs table widgets

When you share a dashboard, by default the CloudWatch Logs Insights widgets that are on the dashboard
are not visible to the people who you share the dashboard with. This affects both
CloudWatch Logs Insights widgets that exist now
and any that are added to the dashboard
after you share it.

If you want these people to be able to see CloudWatch Logs widgets, you must add permissions
to the IAM role for dashboard sharing.

###### To allow the people that you share a dashboard with to see the CloudWatch Logs widgets

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of the shared dashboard.
4. Choose **Actions**, **Share dashboard**.
5. Under **Resources**, choose **IAM Role**.
6. In the IAM console, choose the displayed policy.
7. Choose **Edit policy** and add the following
   statement. In the new statement, we recommend that you specify the ARNs of
   only the log groups that you want shared. See the following example.

```
{
            "Effect": "Allow",
            "Action": [
                "logs:FilterLogEvents",
                "logs:StartQuery",
                "logs:StopQuery",
                "logs:GetLogRecord",
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "`SharedLogGroup1ARN`",
                "`SharedLogGroup2ARN`"
           ]
        },
```

8. Choose **Save Changes**.

If your IAM policy for dashboard sharing already includes those five permissions with
`*` as the resource, we strongly recommend that you change the policy and specify only
the ARNs of the log groups that you want shared. For example, if your `Resource` section
for these permissions was the following:

```
"Resource": "*"
```

Change the policy to specify only the ARNs of the log groups
that you want shared, as in the following example:

```
"Resource": [
  "`SharedLogGroup1ARN`",
  "`SharedLogGroup2ARN`"
]
```

## Allowing people that you share with to see custom widgets

When you share a dashboard, by default the custom widgets that are on the dashboard
are not visible to the people who you share the dashboard with. This affects both
custom widgets that exist now
and any that are added to the dashboard
after you share it.

If you want these people to be able to see custom widgets, you must add permissions
to the IAM role for dashboard sharing.

###### To allow the people that you share a dashboard with to see the custom widgets

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Dashboards**.
3. Choose the name of the shared dashboard.
4. Choose **Actions**, **Share dashboard**.
5. Under **Resources**, choose **IAM Role**.
6. In the IAM console, choose the displayed policy.
7. Choose **Edit policy** and add the following
   statement. In the new statement, we recommend that you specify the ARNs of
   only the Lambda functions that you want shared. See the following example.

```
{
  "Sid": "Invoke",
  "Effect": "Allow",
  "Action": [
      "lambda:InvokeFunction"
  ],
  "Resource": [
    "LambdaFunction1ARN",
    "LambdaFunction2ARN"
  ]
 }
```

8. Choose **Save Changes**.

If your IAM policy for dashboard sharing already includes that permission with
`*` as the resource, we strongly recommend that you change the policy and specify only
the ARNs of the Lambda functions that you want shared. For example, if your `Resource` section
for these permissions was the following:

```
"Resource": "*"
```

Change the policy to specify only the ARNs of the custom widgets
that you want shared, as in the following example:

```
"Resource": [
  "`LambdaFunction1ARN`",
  "`LambdaFunction2ARN`"
]
```
