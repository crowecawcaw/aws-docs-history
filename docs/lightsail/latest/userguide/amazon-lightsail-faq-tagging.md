# Tags in Lightsail

## What are tags?

A tag is a label that you assign to a Lightsail resource. Each tag consists of a key
and a value, both of which you define. A tag value is optional, so you can choose to create
“key-only” tags for filtering resources in the Lightsail console.

## How can I use tags in Lightsail?

With tags, you can group and filter your resources in the Lightsail console and API,
track and organize your costs in your bill, and regulate who can see or modify your
resources through access management rules. By tagging your resources you can:

- Organize – use the Lightsail console and API
  filters to view and manage resources based on their tags you have assigned them. This is
  useful when you have many resources of the same type—you can quickly identify a specific
  resource based on the tags you've assigned to it.
- Cost-allocate – track and allocate costs
  across different projects or users by tagging your resources and creating “cost
  allocation tags” in the billing console. For instance, you can split out your bill and
  understand your costs by project or by client.
- Manage access – control how users with access
  to your AWS account can edit, create, and delete Lightsail resources by using
  AWS Identity and Access Management policies. This allows you to more easily collaborate with others without
  needing to give them full access to your Lightsail resources.

For more information about using tags in Lightsail, see [Tags](amazon-lightsail-tags.md "amazon-lightsail-tags.md").

## What resources can be tagged?

Lightsail currently supports tagging for the following resources:

- Instances (Linux and Windows)
- Container services
- Block storage disks
- Load balancers
- Databases
- DNS zones
- Manual snapshots of instances, disks, and databases

Manual snapshots support tags; however, you must use the Lightsail API, or AWS CLI to
tag snapshots. If you use the Lightsail console to create a manual snapshot of a tagged
instance, disk, or database, the manual snapshot is automatically given the same tags as the
source resource. You can edit these tags when you use the Lightsail console to create a
new resource from a tagged manual snapshot.

Automatic snapshots cannot be tagged.

## How can I tag my Lightsail

snapshots?

The Lightsail console automatically tags manual snapshots with the same tags as its
source resource. If you use the Lightsail API, or AWS CLI to create a snapshot, you can
choose the tags for the snapshot yourself.

###### Important

Tags for manual snapshots of databases are not currently included in billing reports
(cost allocation tags).

## What is the

difference between key-value and key-only tags?

Lightsail tags are key-value pairs, allowing you to organize resources such as
instances across different categories (e.g. project:Blog, project:Game, project:Test). This
allows you full control across all use cases such as resource organization, bill reporting,
and access management. The Lightsail console also allows you to tag your resources with
key-only tags for quick filtering in the console.
