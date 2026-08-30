# Aurora Serverless Scaling execution block

**Category:** Database scaling

During a Region switch, your destination Aurora Serverless cluster may have ACU (Aurora Capacity Unit) settings
that are far below what's needed to absorb production traffic. The Aurora Serverless Scaling execution block
automatically calculates and applies the correct min and max ACU capacity to your destination cluster based on
the source cluster's actual usage, ensuring your serverless database can handle the incoming workload without
throttling or connection failures.

## Key benefits

- **Usage-based capacity calculation:** Rather than relying on
  static configuration, Region switch derives target capacity from the source cluster's actual peak utilization
  over the last 24 hours, giving you right-sized capacity based on real traffic patterns.
- **Cross-engine-type intelligence:** Whether your source is
  Serverless, Provisioned, or a hybrid configuration, Region switch knows how to translate the source capacity
  into appropriate ACU settings for the destination Serverless cluster.
- **Percentage-based scaling for active-active:** Configure a
  target percentage above 100% (for example, 200%) for active-active architectures where the destination
  must absorb combined traffic from both Regions.

## When to use

- **Active-passive with Serverless standby:** Your destination Region
  runs a Serverless cluster at minimal ACUs and needs to scale up before receiving production traffic.
- **Active-active failover:** Both Regions serve traffic, and during a
  switch the remaining Region must handle the combined load – use a target percentage above 100%.
- **Mixed-engine Global Databases:** Your source Region uses provisioned
  instances but your destination uses Serverless – Region switch handles the capacity translation automatically.

### How Aurora Serverless Scaling compares to alternatives

Without this execution block, customers must manually calculate ACU requirements and modify cluster settings
before switching traffic – a complex, error-prone process especially when source and destination use different engine types.

|     | Approach                                   | Pros                                                                                                                                  | Cons                                                                                  |
| --- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| 1   | **Aurora Serverless Scaling block**        | Automated calculation from real usage, handles cross-engine translation, percentage-based control, integrated with plan orchestration | Only scales up; modifies ACU settings which may drift from IaC                        |
| 2   | **Manual ACU adjustment**                  | Full control                                                                                                                          | Requires calculating ACU equivalents under pressure; slow; error-prone                |
| 3   | **Scripted automation**                    | Customizable                                                                                                                          | Must replicate cross-engine translation logic; no plan evaluation; maintenance burden |
| 4   | **Pre-provisioning (max ACU always high)** | No failover delay                                                                                                                     | Expensive; defeats the cost benefit of Serverless; wasteful in standby Region         |

The Aurora Serverless Scaling block is the right choice when you need automated, usage-aware capacity
scaling that handles the complexity of cross-engine ACU translation.

## How it works

After you configure an Aurora Serverless Scaling execution block, Region switch confirms that
there is one source cluster and one destination cluster in the specified global database. The target
capacity is determined based on the source cluster type:

- **Source is Serverless:**

  - Min ACU = source cluster's peak observed ACU utilization (the
    `ServerlessDatabaseCapacity` CloudWatch metric) over the last 24 hours
  - Max ACU = peak of the source cluster's max ACU over the last 24 hours

- **Source is Provisioned:**

  - Maps the source cluster's EC2 instance memory to equivalent ACUs (instance memory in GiB ÷ 2)
  - Sets max ACU to 256

- **Source is Hybrid (Provisioned + Serverless):**

  - Min ACU = maximum of the provisioned instance ACU equivalent and the observed serverless ACU utilization over 24 hours
  - Max ACU = 256

Region switch then applies the target percentage to calculate final values:

```
destination min ACU = round_to_nearest_0.5(targetPercent × source min ACU)
destination max ACU = round_to_nearest_0.5(targetPercent × source max ACU)
```

If the destination cluster's current capacity is already at or above the calculated target, Region switch
completes the step without making changes. Region switch does not scale down
cluster capacity. When the destination cluster is not Serverless, the block completes successfully as
a no-op.

For active-active plans, Region switch uses the other configured Region as the
source. If a Region is being deactivated, Region switch uses the other active Region as the
source to calculate the percentage to scale.

###### Note

Executing this block modifies the min and max ACU capacity settings of your Aurora
Serverless clusters, which may cause configuration drift if you manage these values
through infrastructure-as-code tools or other automation. Ensure your configuration
management processes account for these changes to prevent unintended rollbacks.

## Configuration

When you configure the Aurora Serverless Scaling execution block, you enter the global cluster
identifier for your Aurora Global Database and the database cluster ARNs for each Region that you
want to be scaled up during plan execution.

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
For more information, see [Aurora serverless scaling execution block sample policy](security_iam_region_switch_aurora_serverless_scaling.md "security_iam_region_switch_aurora_serverless_scaling.md").

To configure an Aurora Serverless Scaling execution block, enter the following values:

1. **Step name:** Enter a name.
2. **Step description (optional):** Enter a description of the step.
3. **Aurora Global Database cluster name:** Enter the global cluster identifier.
4. **Cluster ARN for _Region_:** Enter the
   database cluster ARN to use in each Region for your plan.
5. **Target percent (optional):** Enter the percentage of derived source capacity to scale the
   destination cluster to. Defaults to 100. For active-active plans, consider a higher value (for
   example, 200%) to account for combined traffic.
6. **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## Related resources

- [Aurora serverless scaling execution block sample policy](security_iam_region_switch_aurora_serverless_scaling.md "security_iam_region_switch_aurora_serverless_scaling.md")
- [Managing Aurora Serverless v2 capacity](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-administration.md")
  in the _Amazon Aurora User Guide_
