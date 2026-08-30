# Aurora Provisioned Scaling execution block

**Category:** Database scaling

When you switch Regions, your Aurora provisioned database in the destination Region may be running a smaller instance class
than your source Region — leaving you with insufficient compute capacity to handle production traffic. The Aurora Provisioned
Scaling execution block automatically scales the destination instance to match the source instance class, ensuring your database
is ready to serve full production load the moment traffic arrives.

## Key benefits

- **Automatic capacity matching:** Region switch reads the source instance class and scales
  the destination instance to match, eliminating the risk of under-provisioned databases receiving production traffic after
  a failover.
- **Instance creation when needed:** If the destination instance doesn't exist yet,
  Region switch creates it with the correct instance class.
- **Cross-family intelligence:** When the source instance type isn't available in
  the destination Region, Region switch automatically selects an equivalent or larger instance type with the same or more vCPU
  and memory, so you don't need to maintain instance-type compatibility mappings yourself.

## When to use

Any recovery plan where Aurora provisioned instances must be at production capacity before traffic shifts.

- **Active-passive Aurora Global Databases:** Your secondary Region runs a smaller
  (cheaper) reader instance that must be scaled up before receiving write traffic.
- **Cost-optimized standby Regions:** You intentionally run smaller instances in your
  standby Region to save costs, and need automated right-sizing during failover.

### How Aurora Provisioned Scaling compares to alternatives

Without this execution block, customers must ensure destination database capacity manually or through custom automation
before switching Regions.

|     | Approach                             | Pros/Cons                                                                                                                                |
| --- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Aurora Provisioned Scaling block** | Fully automated, handles cross-family mapping, creates missing instances, integrated with Region switch orchestration                    |
| 2   | **Manual scaling**                   | Full control over timing and instance selection, but slow, error-prone under pressure, requires operator availability during incident    |
| 3   | **Scripted automation (Lambda/SSM)** | Customizable logic; Must build, test, and maintain; not integrated with Region switch sequencing; cannot leverage native plan evaluation |
| 4   | **Pre-provisioning (always match)**  | Zero failover delay. Doubles cost in standby Region; wasteful for active-passive architectures                                           |

The Aurora Provisioned Scaling block is the right choice when you want automated, validated capacity scaling as an
integrated step in your Region switch recovery plan.

## How it works

When the Aurora Provisioned Scaling execution block runs during plan execution, Region switch
scales the target instance to match the instance class of the source instance through the following sequence:

- If the target instance exists but is not in an `available` state, Region switch
  waits for it to become available before proceeding.
- If the target instance does not exist, Region switch creates it in the target cluster with
  the instance class from the source instance.
- If the target instance exists, Region switch validates that it belongs to the expected cluster,
  then compares the instance classes.
- If both instances are in the same family and the target is smaller, Region switch modifies
  the target instance to match the source class.
- If the instances are in different families, or the target is already at a larger size,
  no scaling is performed.
- If the source instance type doesn't exist in the target Region, Region switch selects another
  instance type with the same or more vCPU and memory (for both create and modify operations).
- Region switch polls the target instance until it reaches `available` status, then marks the
  step as complete.

###### Note

Region switch only scales up. If the destination instance is already equal to or larger than the source, no
modification is made.

## Configuration

###### Important

Before you configure the execution block, make sure that the plan's execution role has the correct IAM policy in place.
For more information, see [Aurora provisioned scaling execution block sample policy](security_iam_region_switch_aurora_provisioned_scaling.md "security_iam_region_switch_aurora_provisioned_scaling.md").

To configure an Aurora Provisioned Scaling execution block, enter the following values:

- **Step name:** Enter a name.
- **Step description (optional):** Enter a description of the step.
- **Global cluster identifier:** Enter the identifier for
  the Aurora global cluster.
- **Cluster ARN for `Region`:** Enter the
  Aurora database cluster ARN for each Region in the plan.
- **Instance ARN for `Region`:** Enter the
  Aurora database instance ARN for each Region in the plan.
- **Timeout:** Enter a timeout value.

Then, choose **Save step.**

## Related resources

- [Aurora provisioned scaling execution block sample policy](security_iam_region_switch_aurora_provisioned_scaling.md "security_iam_region_switch_aurora_provisioned_scaling.md")
- [Amazon Aurora DB instance classes](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.md "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.md") in the _Amazon Aurora User Guide_
