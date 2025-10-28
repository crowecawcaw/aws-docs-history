Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Configuring local SMTP

notifications on Snowball Edge

You can set up local notifications for your Snowball Edge devices with Simple Mail
Transfer Protocol (SMTP). The local notifications send emails to configured servers when
the service state (Active, Degraded, Inactive) changes, or if you cross capacity
utilization thresholds of 80%, 90%, or 100%.

Before you begin, confirm that:

- You have access to the latest Snowball Edge client.
- Your device is unlocked and ready to use.
- Your device can connect to the internet (if using Amazon Simple Email Service or external
  SMTP server) or to a local SMTP server.

## Configuring the Snowball Edge for local notifications

Set up a Snowball Edge to send email notifications.

###### To configure the device for SMTP notifications

1. Run the following command to add an SMTP configuration to your
   device:

```
# If you don't specify a port, port 587 is the default.
SMTP_ENDPOINT=`your-local-smtp-server-endpoint`:`port`

# For multiple email recipients, separate with commas
RECIPIENTS_LIST=`your-email-address`

snowballEdge put-notification-configuration \
  --service-id `local-monitoring` \
  --enabled true \
  --type smtp \
  --broker-endpoint "$SMTP_ENDPOINT" \
  --sender `example-sender@domain.com` \
  --recipients "$RECIPIENTS_LIST"
```

You receive a test email from **example-sender@domain.com** if you're successful. 2. Test the configuration by running the following
`get-notification-configuration` command:

```
snowballEdge get-notification-configuration \
  --service-id local-monitoring
```

The response doesn't include a password or certificate, even if you
provide them.
