

# What happens when you opt out of a Region
<a name="USER_RegionOptOutOptIn.OptOut"></a>

When you opt out of an AWS Region, the following changes apply to your Amazon RDS resources in that Region:
+ A snapshot of your DB instances and DB clusters in that Region is taken; then, your DB instances and DB clusters are deleted.
+ You can't create new DB instances or DB clusters in the opted-out Region.

You are charged for snapshots in the Region while the Region is opted out.

Opting out of a Region is a reversible action. Your resources are deleted only after taking a snapshot. After you opt back in to the Region, you can restore your resources using the snapshots.