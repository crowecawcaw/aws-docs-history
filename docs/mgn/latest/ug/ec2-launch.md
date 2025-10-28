NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Launch settings

The launch settings include two sections: the general launch settings, and the EC2 launch
template, which determine how a test or cutover instance is launched for each source server in
AWS.

Launch settings, including the EC2 launch template, are automatically created each time you
add a source server to AWS Application Migration Service.

The launch settings can be modified at any time, including before the source server has
completed its initial sync.

###### Note

Any changes made to the launch settings only affect newly launched test and cutover
instances.

###### Note

For many customers, there is no need to modify the launch settings or the EC2 launch
template in order to launch test or cutover instances.

Launch settings can only be changed for one server at a time though the AWS Application Migration Service
console.

###### Note

You can modify launch settings for multiple servers at a time by using the AWS Application Migration Service
API.

You can access the launch settings of a specific source server through the server details
view by choosing its Hostname from the **Source servers**
page.

Within the individual server view, navigate to the **Launch
settings** tab.

The **Launch settings** tab is divided into two sections:

- General launch settings
- EC2 launch template
