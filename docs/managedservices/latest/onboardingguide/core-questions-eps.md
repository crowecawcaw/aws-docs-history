# Trend Micro Endpoint Protection (EPS)

- Instance sizes for your EC2 instances and Auto Scaling groups

Trend Micro Endpoint Protection (EPS) is the primary component within AMS for operating system security. The system is comprised
of Deep Security Manager (DSM) EC2 instances, relay EC2 instances, and an agent present within all of AMS data plane and your EC2 instances.

    + Relay instance type (minimum supported by AMS is m5.large)
    + DB instance size (200 GB recommended)
    + RDS instance type (only db.m5.large or db.m5.xlarge allowed)

- DSM License type (Marketplace or BYOL)

If you already have a license, choose BYOL (bring your own license). AMS will contact you to obtain the
necessary information about the license.

- AWS IAM user or role Amazon resource name (ARN) for Trend Micro Deep Security Subscription
  (Role ARN: arn:aws:iam::`ACCOUNT_ID`:role/`ROLE_NAME`)

Provide us an IAM role; ARN, or an IAM user ARN from one of your existing AWS accounts to which you have access.
AMS creates an IAM role; in your AMS multi-account landing zone Shared Services account and adds the role or user provided in the trust of an IAM role
in Shared Services so that the role can be assumed by you to subscribe to the Trend Micro Deep Security in AWS Marketplace.
