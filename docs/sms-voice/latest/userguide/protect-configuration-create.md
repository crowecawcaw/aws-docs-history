# Create a protect configuration in

AWS End User Messaging SMS

To create a new protect configuration, you can use the AWS End User Messaging SMS console, the
`CreateProtectConfiguration` action in the AWS End User Messaging SMS and voice v2 API, or the
`aws sms-voice create-protect-configuration` command in the AWS CLI. This
section shows how to create protect configurations using the AWS End User Messaging SMS console and the
AWS CLI.

By default you can have up to 25 protect configurations in your AWS account.

When creating a protect configuration, you can create rules that allow, filter, or block
for countries based on your business needs. To learn more about editing the country rules,
see [Change a protect configuration
country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md").

###### Note

The name of your protect configuration is saved as a tag key/value pair. If you don't
specify a "Name" tag then the name for the protect configuration will appear as
–.

Create a protect configuration (Console)
To create a protect configuration using the AWS End User Messaging SMS console, follow these
steps:

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Protect**, choose
   **Protect configuration** and then **Create
   configuration** .
3. For **Protect configuration name** enter a
   descriptive name for the protect configuration.
4. Set country rules to _block_,
   _filter_, or _allow_ message
   sending based on your business needs. You can sort and filter the
   country list based on Country, Region and Rule.
5. In **Protect configuration associations** for
   **Association type**, choose:
   - **Account default** – To use the
     protect configuration as your account default. If you already
     have an **Account default** protect
     configuration then it is replaced.
   - **Configuration set** – To associate
     the protect configuration with an existing configuration set.
     For **Configuration sets available for
     association**, choose one or more configuration
     sets to associate the protect configuration to. This replaces
     the existing protect configuration association.
   - **No association** – The protect
     configuration is not associated to your account default or a
     configuration set.

6. Choose **Create configuration**.

Now you have created your protect configuration you should edit the country
rules list for MMS and voice. To learn more about editing the country rules, see
[Change a protect configuration
country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md").

Create a protect configuration (AWS CLI)
You can use the create-protect-configuration command to create a new protect
configuration.

###### To create a protect configuration

- At the command line, enter the following command:

```
`$` aws pinpoint-sms-voice-v2 create-protect-configuration --tags Key=`Name`,Value=`ProtectConfigName`
```

In the preceding command, make the following changes:

    + Replace `ProtectConfigName` with a
     friendly name for your protect configuration.

Now you have created your protect configuration you need to edit the country
rules list for SMS, MMS, and voice. To learn more about editing the country
rules, see [Change a protect configuration
country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md"). Optionally you can
associate the protect configuration with the _account
default_ protect configuration or a configuration set.
