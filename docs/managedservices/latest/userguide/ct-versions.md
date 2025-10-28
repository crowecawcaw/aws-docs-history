# Change type versions

Change types are versioned and the version changes when a major update is made to the change type.

After selecting a change type using the AMS console, you have the option of opening the **Additional
configuration** area and selecting a change type version. You can also specify a change type version at
the API/CLI command line. You might want to do this for various reasons, including:

- You know that the version of the **Update** change type that you want must
  match the version of the **Create** change type that you used
  to create the resource that you now want to update. For example, you might have
  an Elastic Load Balancer (ELB) instance that you created with ELB Create change
  type version 1. To update it, choose ELB Update version 1.
- You want to use a change type version that has different options in it than the most recent
  change type. We don't recommend this because AMS updates change types mainly
  for security reasons and we recommend that you always choose the most recent
  version.
