# Find availability zones (AZs) in AMS

**Availability Zone**: All accounts have at least two availability zones. To accurately find
your availability zone names, you must first know the associated subnet ID.

- AMS Console: In the navigation pane click **VPCs**, and then click the relevant VPC, if necessary.
  On the VPCs details page, select the relevant subnet in the table of subnets to open the subnet details page with the name of the associated availability zone.
- AMS SKMS API/CLI:

```
aws amsskms list-subnet-summaries --output table
```

```
aws amsskms get-subnet --subnet-id `SUBNET_ID`
```

###### Note

The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your
authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1`
when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.
