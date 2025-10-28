# Edit a configuration set protect configuration association in AWS End User Messaging SMS

To change a configuration set's associated protect configuration, you can use the AWS End User Messaging SMS
console, the `AssociaterotectConfiguration` action in the AWS End User Messaging SMS and voice v2 API,
or the `aws sms-voice associate-protect-configuration` command in the AWS CLI. This
section shows how to change a configuration set's protect configuration using the AWS End User Messaging SMS
console and the AWS CLI.

To learn more about protect configurations see [Using protect configurations in AWS End User Messaging SMS](protect-configuration.md "protect-configuration.md").

Edit a configuration set's protect configuration association (Console)1. Open the AWS End User Messaging SMS console at
[https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/"). 2. In the navigation pane, under
**Configurations**, choose
**Configuration sets**. 3. On the **Configuration sets** page, choose a configuration set. 4. On the **Configuration set details page**
choose the **Protect configuration** tab and then **Edit settings**. 5. Under **Protect configuration management** for
**Protect configuration**, choose the protect
configuration to associate with the configuration set. This replaces the
current protect configuration association. Choose **No
association** to disassociate the configuration set from a
protect configuration. 6. Choose **Save changes**

Edit a configuration set's protect configuration association (AWS CLI)
To change a configuration set's protect configuration association in the AWS CLI
follow the direction in [Change a protection configuration
association in AWS End User Messaging SMS](protect-configuration-edit-association.md "protect-configuration-edit-association.md") on the Edit a protect
configuration association (AWS CLI) tab.
