

# Campaign management
<a name="campaign-management-ui"></a>

The Fleet Manager UI includes a Data Collection section where operators create, monitor, and manage FleetWise campaigns without writing code or using the AWS CLI.

## Create Campaign wizard
<a name="create-campaign-wizard"></a>

The wizard walks operators through campaign creation in four steps:

 **Step 1 — Campaign details:** 
+ Campaign name and description
+ Scheme type: **Condition-based** (collect when a signal crosses a threshold) or **Time-based** (collect at fixed intervals)
+ For condition-based: select the trigger signal, operator (>, <, =), threshold value, and trigger mode (rising edge or always)
+ Minimum collection interval (milliseconds between samples)
+ Optional: link to a safety event definition from the event catalog

 **Step 2 — Signal selection:** 
+ Browse all 260\+ signals from the signal catalog, grouped by category
+ Multi-select signals to include in the campaign
+ Each signal shows its name, VSS path, unit, and signal group
+ Select a decoder manifest (the default `cms-fleet-v1` is pre-selected if only one exists)

 **Step 3 — Vehicle targeting:** 
+ Browse registered vehicles from DynamoDB
+ Multi-select vehicles to target with this campaign
+ If launched from a vehicle detail page, the vehicle is pre-selected and locked
+ Assign to an entire fleet — all vehicles in the fleet receive the campaign with `sourceFleetId` set. Fleet-assigned campaigns cannot be modified at the vehicle level.

 **Step 4 — Review and create:** 
+ Review all settings before submission
+ On submit, the campaign is written to DynamoDB with status `RUNNING` 
+ The CampaignSyncProcessor picks up the new campaign on the next agent checkin and pushes the collection scheme to targeted vehicles

## Managing campaigns
<a name="campaign-lifecycle-ui"></a>

From the campaigns list view, operators can:
+  **View status** — See which campaigns are RUNNING, SUSPENDED, or COMPLETED
+  **Suspend** — Pause a campaign. The CampaignSyncProcessor pushes an empty collection scheme on the next checkin, stopping signal collection.
+  **Resume** — Reactivate a suspended campaign
+  **Delete** — Remove a campaign permanently