#

DNS target resource readiness checks: Auditing resiliency readiness

With DNS target resource readiness checks in ARC, you can audit the architectural and
resiliency readiness of your application. This type of readiness check continually scans
your application's architecture and Amazon Route 53 routing policies to audit for cross-zone and cross-Region
dependencies.

A recovery-oriented application has multiple replicas that are siloed into Availability Zones or AWS Regions, so that the replicas can fail
independently of one another. If your application needs adjusting to be siloed correctly, ARC will suggest changes that you can make, if needed, to
update your architecture to help ensure that it's resilient and ready for failover.

ARC automatically detects the number and the scope of cells (representing replicas, or failure-containment units) in your application, and whether
the cells are siloed by Availability Zone or by Region. Then, ARC identifies and provides information to you about the application resources in the
cells, to determine if they are correctly siloed to zones or Regions. For example, if you have cells that are scoped to specific zones, readiness checks
can monitor if your load balancers and the targets behind them are also siloed to those zones.

With this information, you can determine if there are changes that you need to make to align resources in
your cells to the correct zones or Regions.

To get started, you create DNS target resources for your application, and resource sets and
readiness checks for them. For more information, see [Getting architecture recommendations in ARC](recovery-readiness.md "recovery-readiness.md").
