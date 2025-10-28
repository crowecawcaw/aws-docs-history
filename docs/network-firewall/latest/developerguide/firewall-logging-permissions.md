# Permissions to configure AWS Network Firewall logging

You must have the following permissions to make any changes to your firewall
logging configuration. These settings are included in the permissions requirements
for each logging configuration type, under [AWS Network Firewall logging destinations](firewall-logging-destinations.md "firewall-logging-destinations.md").

```
        {
            "Action": [
                "logs:CreateLogDelivery",
                "logs:GetLogDelivery",
                "logs:UpdateLogDelivery",
                "logs:DeleteLogDelivery",
                "logs:ListLogDeliveries"
            ],
            "Resource": [
                "*"
            ],
            "Effect": "Allow",
            "Sid": "FirewallLogging"
        }
```

The permissions required for logging configuration are in addition to the standard
permissions required to use the Network Firewall API. For information about the
standard permissions that are required to use Network Firewall, see [Managing access using policies](security-iam.md#security_iam_access-manage "security-iam.md#security_iam_access-manage").
