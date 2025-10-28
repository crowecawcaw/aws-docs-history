# MAP program tagging

The AWS Migration Acceleration Program (MAP) provides tools that are designed to reduce costs, boost productivity, improve operational resilience and increase business agility.

The DRS MAP program tagging is a feature that allows you to apply MAP program
tags to your source servers and replication resources in order to offset the
ongoing cost of protecting your servers.

[Learn more about the AWS Migration Acceleration Program (MAP)](https://aws.amazon.com/migration-acceleration-program "https://aws.amazon.com/migration-acceleration-program").

Select **Add MAP tag to Launched Instances option**, if you want
Application Migration Service to automatically tag your launched instances with
the tag key and value combination required for MAP program. Then, specify the
MAP tag value that is used in your MAP tagging. Application Migration Service
automatically tags your migrated resources with the key: “map-migrated”, and the
value of the tag that you provided. For more details about the tag value that
should be used here, please refer to the MAP tagging guide provided in your MAP
term.

You can choose to add tags to:

- One or more existing source servers and replication resources
- All newly added source servers and replication resources

## Adding tags to existing source servers and replication sources

To add tags to one or more existing source servers and replication sources:

- Select the relevant source servers.
- Select **Edit replication settings** from the replication
  drop-down menu
- Check the box to the left of **Add MAP tag to the source servers and
  replication resources**.
- Specify the MAP tag value that is used in your MAP tagging.

DRS automatically tags your source servers and replication resources with the
tag key "map-migrated” and the value of the tag that you provide.

## Adding tags to newly added source servers and replication sources

To add tags to all newly added source servers and replication sources:

- Select **Settings** from the left-hand menu.
- select **Edit** to change the default replication
  settings.
- Check the box to the left of **Add MAP tag to the source servers and replication resources** option.
- Specify the MAP tag value that is used in your MAP tagging.
- select **Save changes**.

AWS Elastic Disaster Recovery automatically tags every newly-added source server and replication
resources with the tag key “map-migrated” and the value of the tag, that you
provide.

For more details about the tag value that should be used here, please refer to the MAP tagging guide provided in your MAP term.
