AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Tracking when you use AWS Application Migration Service to perform discovery

first and then migrate

If you started performing discovery using AWS discovery tools, the servers list will
likely be populated before you start migrating. Migration Hub attempts to automatically map
updates from migration tools to servers in the servers list. If it cannot find a match
in the discovered servers list, then Migration Hub will add a server corresponding to the
migration update to the servers list and automatically map the update to the
server.

Sometimes, when using AWS discovery tools, the automatic mapping of migration
updates to servers can be incorrect. You can see updates and their mappings on the
**Updates** page and can correct the mapping by choosing
**Edit**.

See Step 2.a in _To determine if a migration update must be manually mapped
to a discovered server_ procedures below. If you have to frequently
correct mappings after performing discovery, contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/").

###### To determine if a migration update must be manually mapped to a discovered

server

1. In the navigation pane, under **Migrate**, select
   **Updates**.
2. Verify if the **Mapped servers** column is populated for
   every row of migration updates.
   1. If the **Mapped servers** column is populated for
      every row of migration updates, this means auto-mapping was supported by
      the migration tool and manual mapping is not required. To edit the
      server mapping, select the server, and then choose **Edit server
      mapping**.
   2. If one or more rows of the **Mapped servers** columns
      is _not_ populated, this is an
      indication that manual mapping is required. Proceed to the next set of
      procedures.
