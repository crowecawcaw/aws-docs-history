# Disable outbound campaigns in Connect Customer

###### Prerequisite

You must delete all existing campaigns before you disable outbound campaigns.

To disable outbound campaigns, delete your outbound campaigns configuration by using the
Outbound campaigns `DeleteConnectInstanceConfig` API or the
`delete-connect-instance-config` AWS CLI command. The console does not include a
control to turn off the feature.

The following example deletes the outbound campaigns configuration for an instance. Replace
`instance-id` with the ID of your Connect Customer instance.

```

aws connectcampaigns delete-connect-instance-config --connect-instance-id `instance-id`
```

After you delete the configuration, you can no longer create outbound campaigns.
