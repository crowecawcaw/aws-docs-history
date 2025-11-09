AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Configuring replication sets and Findings in

Incident Manager

After you have completed the Incident Manager Get prepared wizard, you can manage certain
options on the **Settings** page. These options include your
replication set, tags applied to the replication set, and the Findings feature.

###### Topics

- [Configuring the Incident Manager replication set](#replication "#replication")
- [Managing tags for a replication set](#general-tags "#general-tags")
- [Managing the Findings feature](#settings-findings "#settings-findings")

## Configuring the Incident Manager replication set

The Incident Manager replication set replicates your data to many AWS Regions in
order to do the following:

- Increase cross-Region redundancy
- Allow Incident Manager to access resources in different Regions and reduce
  latency for your users.
- Encrypt your data with either an AWS managed key or your own customer managed key.

All Incident Manager resources are encrypted by default. To learn more about
how your resources are encrypted, see [Data protection in Incident Manager](data-protection.md "data-protection.md").

To get started with Incident Manager, first create your replication set using the
**Get prepared** wizard. To learn more about getting prepared
in Incident Manager, see the [Get prepared wizard](getting-started.md#getting-started-wizard "getting-started.md#getting-started-wizard").

### Editing your replication set

By using the Incident Manager **Settings** page, you can edit your
replication set. You can add Regions, delete Regions, and enable or disable
replication set deletion protection. You can't edit the key used to encrypt your
data. To change the key, delete and recreate the replication set.

###### Add a Region

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home"), and then choose
   **Settings** in the left navigation pane.
2. Choose **Add Region**.
3. Select the **Region**.
4. Choose **Add**.

###### Delete a Region

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home"), and then choose
   **Settings** in the left navigation pane.
2. Select the Region that you want to delete.
3. Choose **Delete**.
4. Enter **delete** into the text box, and choose
   **Delete**.

### Deleting your replication set

Deleting the last Region in your replication set deletes the entire
replication set. Before you can delete the last Region, disable the deletion
protection by turning off **Deletion protection** on the
**Settings** page. After you delete your replication set,
you can create a new replication set by using the **Get
prepared** wizard.

To delete a Region from your replication set, wait 24 hours after creating it.
Attempting to delete a Region from your replication set sooner than 24 hours
after creation causes the deletion to fail.

Deleting your replication set deletes all Incident Manager data.

###### Delete the replication set

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home"), and then choose
   **Settings** in the left navigation pane.
2. Select the last Region in your replication set.
3. Choose **Delete**.
4. Enter **delete** into the text box, and choose
   **Delete**.

## Managing tags for a replication set

Tags are optional metadata that you assign to a resource. Use tags to categorize a
resource in different ways, such as by purpose, owner, or environment.

###### To manage tags for a replication set

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home"), and then choose
   **Settings** in the left navigation pane.
2. In the **Tags** area, choose
   **Edit**.
3. To add a tag, do the following:
   1. Choose **Add new tag**.
   2. Enter a key and optional value for the tag.
   3. Choose **Save**.

4. To delete a tag, do the following:
   1. Under the tag you want to delete, choose
      **Remove**.
   2. Choose **Save**.

## Managing the Findings feature

The Findings feature helps responders in your organization identify potential root
causes of incidents soon after the incidents begin. Currently, Incident Manager provides
findings for AWS CodeDeploy deployments and AWS CloudFormation stack updates.

For cross-account support for findings, after you enable the feature, you must
complete an additional setup step in each application account in the
organization.

To use the feature, you let Incident Manager create a service role that includes the
required permissions to access data on your behalf.

###### To enable the Findings feature

1. Open the [Incident Manager console](https://console.aws.amazon.com/systems-manager/incidents/home "https://console.aws.amazon.com/systems-manager/incidents/home"), and then choose
   **Settings** in the left navigation pane.
2. In the **Findings** area, choose **Create service
   role**.
3. Review information about the service role to be created, and then choose
   **Create**.

###### To disable the Findings feature

To stop using the Findings feature, delete the
`IncidentManagerIncidentAccessServiceRole` role from each
account where it has been created.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the left navigation pane, choose **Roles**.
3. In the search box, enter
   `IncidentManagerIncidentAccessServiceRole`.
4. Choose the name of the role, and then choose
   **Delete**.
5. Enter the role name in the dialog box to confirm that you want to delete
   the role, and then choose **Delete**.
