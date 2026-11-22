

# Creating, viewing, updating, and deleting IPS rule groups

You create, view, update, and delete an IPS rule group with the same console pages and API operations as a firewall rule group, choosing the IPS rule group type. The following list links to the shared procedures and notes what's specific to an IPS rule group.
+ **Create** – Follow [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md). On the **Choose rule group type** page, choose **IPS rule group**. The only rule group format for an IPS rule group is **Text rule builder**: you provide the rules as Suricata compatible rule strings, using the same syntax as a Classic Network Firewall stateful rule group. With the AWS CLI, use `create-rule-group` with `--type IPS` and the `--ips-rule-group` parameter.
+ **View** – Follow [Viewing your rule groups in AWS Network Firewall](rule-groups-v2-viewing.md). The details page for an IPS rule group shows an **IPS signatures** section that lists each signature's description and its rule string.
+ **Update** – Follow [Updating a rule group for a Next Generation policy](rule-groups-v2-updating.md). You can change an IPS rule group's rules, but not its name, capacity, or type. With the AWS CLI, use `update-rule-group` with `--type IPS`.
+ **Delete** – Follow [Deleting a rule group for a Next Generation policy](rule-groups-v2-deleting.md). You can't delete a rule group that a firewall policy still references. With the AWS CLI, use `delete-rule-group` with `--type IPS`.