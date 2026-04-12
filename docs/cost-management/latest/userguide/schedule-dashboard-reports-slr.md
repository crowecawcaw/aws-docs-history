# Service-linked role for scheduled reports

When you create your first scheduled report, you can choose to opt in to the creation of
a service-linked role (SLR). This role allows the BCM Dashboards service to generate reports
and deliver them on your behalf. The SLR includes predefined permissions necessary for the
service to access your cost data (such as `ce:GetCostAndUsage`) and dashboard
configurations (such as `bcm-dashboards:GetDashboard`).

This is a one-time opt-in per account that applies to all future scheduled reports. The SLR
permissions are managed by AWS and cannot be modified directly in the IAM console.
