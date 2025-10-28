# DRHCSEC04-BP01 Restrict access by location of resource

Specify IAM actions to restrict based on
where the resource's storage of data would be located.

**Desired outcome:** Access
management policies allow data storage only in locations that
comply with data residency regulations.

**Common anti-patterns:**

- Allowing unrestricted access to all resources
- Allowing the launching of instances in the Region when
  requirements for a given workload only require launching in an
  Outpost or Local Zone
- Allowing creation of roles, users, and attach policies without
  attaching AWS IAM permission boundaries

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- Analyze location of data in your least privilege access
  analysis. This requires awareness of the actions that can
  impact the location of data.
- If need to allow principals to store data in Amazon S3 on
  Outposts but not in Region buckets, then deny the
  `s3:PutObject` action on the Resource `arn:aws:s3:::*`,
  or only allow the action s3:PutObject on specific S3 buckets
  using resource values that match the pattern
  `arn:aws:s3-outposts:${region}:${account-id}:outpost/outpost-id/accesspoint/${accesspoint-name}`.
- Restrict the creation of instances and network interfaces to
  specific subnets by using policy resources to create a
  dynamically-composed list of authorized subnets for the
  following IAM actions: 
  - `ec2:RunInstances`
  - `ec2:CreateNetworkInterface`
  - `ec2:RequestSpotFleet`
  - `ec2:RequestSpotInstances`
  - `rds:CreateDbSubnet`
  - `elasticache:CreateCacheSubnetGroup`
  - `autoscaling:CreateAutoScalingGroup`
  - `elasticloadbalancing:CreateLoadBalancer`
  - `ec2:CreateLaunchTemplate`

- The `ec2:CreateSnapshot*` actions should not be allowed to
  principals that don't need it. For principals that do, you
  can deny data transfer from an Outpost to a Region by
  attaching a deny policy using the condition key
  `ec2:SourceOutpostArn` for designated Outposts, where
  `ec2:OutpostArn` is null (the destination is not the Outpost).
- The `ec2:CopySnapshot*` actions should not be allowed to
  principals that don't need it. Transfer of snapshots from an
  Outpost to a Region is not currently supported. However,
  snapshots can be copied from Region to an Outposts (for
  example, a valid use case is to move an Amazon Machine Image
  (AMI) from Region to an Outpost for faster launching or
  removing repeated bandwidth consumption). You can use the
  ec2:OutpostArn condition key if you need to restrict the
  copying of snapshots to a specified Outpost. If you need to
  restrict copying snapshots to specific Regions, then specify
  the Region portion of the ARN within the resource attribute
  of the policy statement.
- For each of the following actions, only grant them if there
  is a known requirement for the principal, and use the
  policy's resource section to only allow the storage in the
  required Region:
  - `rds:CreateDBSnapshot`
  - `rds:CreateDBClusterSnapshot`
  - `elasticache:CreateSnapshot`
  - `elasticache:CopySnapshot`
  - `ec2:CopyImage`
  - `ec2:CreateInstanceExportTask`
  - `ec2:CreateVolume`
  - `ec2:AttachVolume`
  - `ec2:ImportSnapshot`
  - `ec2:ImportVolume`
  - `datasync:Create*`
  - `datasync:Update*`

- Implement permission guardrails for which include each of
  the applicable restrictions defined in this best practice

## Resources

**Related best practices:**

- [SEC03-BP02
  Grant least privilege access](../security-pillar/sec_permissions_least_privileges.md "../security-pillar/sec_permissions_least_privileges.md")
- [SEC08-BP04
  Enforce access control](../security-pillar/sec_protect_data_rest_access_control.md "../security-pillar/sec_protect_data_rest_access_control.md")
- [SEC03-BP05
  Define permission guardrails for your organization](../security-pillar/sec_permissions_define_guardrails.md "../security-pillar/sec_permissions_define_guardrails.md")

**Related documentation:**

- [Architecting
  for data residency with AWS Outposts rack and landing zone
  guardrails](https://aws.amazon.com/blogs/compute/architecting-for-data-residency-with-aws-outposts-rack-and-landing-zone-guardrails/ "https://aws.amazon.com/blogs/compute/architecting-for-data-residency-with-aws-outposts-rack-and-landing-zone-guardrails/")
- [Best
  Practices for managing data residency in AWS Local Zones
  using landing zone controls](https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/ "https://aws.amazon.com/blogs/compute/best-practices-for-managing-data-residency-in-aws-local-zones-using-landing-zone-controls/")
- [Permission
  boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md")
