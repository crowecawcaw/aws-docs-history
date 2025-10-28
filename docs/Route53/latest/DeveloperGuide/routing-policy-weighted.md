# Weighted routing

Weighted routing lets you associate multiple resources with a single domain name (example.com) or subdomain name
(acme.example.com) and choose how much traffic is routed to each resource. This can be useful for a variety of purposes,
including load balancing and testing new versions of software.

To configure weighted routing, you create records that have the same name and type for each of your
resources. You assign each record a relative weight that corresponds with how much traffic you want to send to each resource.
Amazon Route 53 sends traffic to a resource based on the weight that you assign to the record as a proportion of the total weight for
all records in the group:

![Formula for how much traffic is routed to a given resource: weight for a specified record / sum of the weights for all records.](images/WRR_calculation.png)
For example, if you want to send a tiny portion of your traffic to one resource and the
rest to another resource, you might specify weights of 1 and 255. The resource with
a weight of 1 gets 1/256th of the traffic (1/(1+255)), and the other resource gets
255/256ths (255/(1+255)). You can gradually change the balance by changing the
weights. If you want to stop sending traffic to a resource, you can change the
weight for that record to 0.

For information about values that you specify when you use the weighted routing policy to create records, see the following topics:

- [Values specific for weighted
  records](resource-record-sets-values-weighted.md "resource-record-sets-values-weighted.md")
- [Values specific for weighted
  alias records](resource-record-sets-values-weighted-alias.md "resource-record-sets-values-weighted-alias.md")
- [Values that are common for all routing
  policies](resource-record-sets-values-shared.md "resource-record-sets-values-shared.md")
- [Values that are common for
  alias records for all routing policies](resource-record-sets-values-alias-common.md "resource-record-sets-values-alias-common.md")
  You can use weighted routing policy for records in a private hosted zone.

## Health checks and weighted routing

If you add health checks to all the records in a group of weighted records, but you give nonzero weights to some records and
zero weights to others, health checks work the same as when all records have nonzero weights with the following exceptions:

- Route 53 initially considers only the nonzero weighted records, if any.
- If all the records that have a weight greater than 0 are unhealthy, then Route 53 considers the zero-weighted records.

The following table details the behavior when the 0-weight record includes a health
check:

|                        | Record 1  | Record 2  | Record 3  |
| ---------------------- | --------- | --------- | --------- | ------------------------------------------------------------------------------------------------- |
| Weight                 | 1         | 1         | 0         |
| Includes health check? | Yes       | Yes       | Yes       |
|                        |
| Health check status    | Unhealthy | Unhealthy | Healthy   |
| DNS query answered?    | No        | No        | Yes       |
|                        |
| Health check status    | Unhealthy | Unhealthy | Unhealthy |
| DNS query answered?    | Yes       | Yes       | No        |
|                        |
| Health check status    | Unhealthy | Healthy   | Unhealthy |
| DNS query answered?    | No        | Yes       | No        |
|                        |
| Health check status    | Healthy   | Healthy   | Unhealthy |
| DNS query answered?    | Yes       | Yes       | No        |
|                        |
| Health check status    | Healthy   | Healthy   | Healthy   |
| DNS query answered?    | Yes       | Yes       | No        | The following table details the behavior when the 0-weight record doesn't include a health check: |
|                        | Record 1  | Record 2  | Record 3  |
| ---                    | ---       | ---       | ---       |
| Weight                 | 1         | 1         | 0         |
| Includes health check? | Yes       | Yes       | No        |
|                        |
| Health check status    | Healthy   | Healthy   | N/A       |
| DNS query answered?    | Yes       | Yes       | No        |
|                        |
| Health check status    | Unhealthy | Unhealthy | N/A       |
| DNS query answered?    | No        | No        | Yes       |
|                        |
| Health check status    | Unhealthy | Healthy   | N/A       |
| DNS query answered?    | No        | Yes       | No        |
