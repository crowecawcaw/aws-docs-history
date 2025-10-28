# Automated instance configuration setup

Assuming the prerequisites have been met, adding a specific Amazon EC2 instance tag automatically initiates
the AMS Accelerate automated instance configuration. Use one of the following methods to add this tag:

1. (Strongly recommended) Use the AMS Accelerate Resource Tagger

To configure the tagging logic for your account, see [How tagging works](acc-tag-intro.md#acc-tag-how-works "acc-tag-intro.md#acc-tag-how-works"). After tagging is complete, tags and automated
instance configuration are handled automatically. 2. Manually add tags

Manually add the following tag to the Amazon EC2 instances:

Key:**ams:rt:ams-managed**, Value:**true**.

###### Note

The instance configuration service attempts to apply the required AMS configurations once the
**ams:rt:ams-managed** tag is applied to the instance. The service asserts the AMS required
configurations whenever an instance is started, and when a the AMS daily configuration check occurs.
