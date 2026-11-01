

# How to check capacity
<a name="capacity-manager-check-capacity"></a>

Call get-capacity-manager-supportability-scores through the console or the API. Provide your market type (on-demand or spot), how much capacity you need, where you want to launch, and either the instance types to consider or the attributes they must meet. The API returns a score for each instance type and Availability Zone combination in your request, plus an aggregate score for the entire set. This API checks current supportability only — it doesn't accept dates.

Call get-capacity-manager-supportability-scores in the Region where you turned on Capacity Manager. A single call can check Availability Zones in any Region. Run checks when you plan or review a workload rather than on every launch, so launches in other Regions don't depend on a cross-Region call.

The following AWS CLI command checks On-Demand capacity for a list of instance types:

```
aws ec2 get-capacity-manager-supportability-scores \
    --market-type "on-demand" \
    --capacity-amount 50 \
    --capacity-unit "instances" \
    --capacity-availability-zone-ids '["use1-az1"]' \
    --instance-types '["c6g.xlarge", "c7g.xlarge", "m6g.xlarge"]'
```

This command uses the following parameters:
+ `--market-type` — The capacity market to check (`on-demand` \| `spot`).
+ `--capacity-amount` — The amount of capacity you need.
+ `--capacity-unit` — The unit for `--capacity-amount` (`instances` \| `vcpus`).
+ `--capacity-availability-zone-ids` — The Availability Zones to check.
+ `--instance-types` — The instance types to consider.

The following JSON structure shows the supportability score response.

```
{
    "AggregateScore": "high",
    "CapacityManagerSupportabilityScores": [
        { "InstanceType": "c6g.xlarge", "AvailabilityZoneId": "use1-az1", "Score": "high" },
        { "InstanceType": "c7g.xlarge", "AvailabilityZoneId": "use1-az1", "Score": "high" },
        { "InstanceType": "m6g.xlarge", "AvailabilityZoneId": "use1-az1", "Score": "medium" }
    ]
}
```

Instead of a list of instance types, you can describe the instances you need by attribute. Provide the vCPU and memory ranges your workload needs, and Amazon EC2 resolves them into matching instance types and scores each one. Provide either `--instance-types` or `--instance-requirements-with-metadata`, not both.

```
aws ec2 get-capacity-manager-supportability-scores \
    --market-type "on-demand" \
    --capacity-amount 1000 \
    --capacity-unit "vcpus" \
    --capacity-availability-zone-ids '["use1-az1"]' \
    --instance-requirements-with-metadata '{"ArchitectureTypes":["arm64"],"InstanceRequirements":{"VCpuCount":{"Min":4,"Max":8},"MemoryMiB":{"Min":16384,"Max":32768},"CpuManufacturers":["amazon-web-services"]}}'
```

In the `--instance-requirements-with-metadata` object, specify the attributes your workload needs:
+ `ArchitectureTypes` — The processor architectures to allow, such as `arm64` or `x86_64`.
+ `InstanceRequirements` — The instance attributes to match, including the following:
  + `VCpuCount` — The minimum and maximum vCPU count your workload needs.
  + `MemoryMiB` — The minimum and maximum memory, in MiB.
  + `CpuManufacturers` — The CPU manufacturers to allow.

A request with one instance type and one Availability Zone returns one combination score plus an aggregate equal to it. A request with 10 types across 3 Availability Zones returns 30 combination scores plus an aggregate.