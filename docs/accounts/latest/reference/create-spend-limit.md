

# Create a spend limit in AWS Settings
<a name="create-spend-limit"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

## What is a spend limit?
<a name="what-is-spend-limit"></a>

Spend limits enable developers to use AWS with confidence that they can operate within a predictable and controlled budget. Use a spend limit to set the most you'll pay per month for a project. Spend limits are at the project level. You can have spend limits on some of your projects and have other projects without spend limits.

If your usage in a project reaches its limit, AWS pauses that project which stops its resources so your costs stay within it. Spend limits are designed for experimentation, learning, and sandbox workloads. They can be used for production environments when it is acceptable to have a brief pause of your resources in cases when your applications incur unexpected costs.

Spend limits are visible to anyone with project access, but can only be managed by project owners. You must be on a Paid Plan to create a spend limit. For more information, see [Upgrade your account in AWS Settings](upgrade-account.md).

Spend limits are a type of [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html).

## Set your spend limit
<a name="set-your-spend-limit"></a>

Your spend limit is the ceiling on your project's pre-tax costs, not a fee. When you set a spend limit, the minimum allowed value is the greater of $20 or a conservative estimate of your likely spend.

**Why a minimum exists:** Hitting a spend limit is a disruptive experience. The minimum exists to make it unlikely that normal variations in your usage will lead to hitting the spend limit.

**How the conservative estimate is calculated:** The estimate is based on your activity month to date, but it's not a strict linear extrapolation. AWS looks at your spend to date and the resources you currently have running. AWS also uses your activity from the prior month — if that was high, it becomes the minimum.

**If you have many resources running:** The conservative estimate of your likely spend will be high. If you want to set a lower spend limit, you need to stop those resources first.

**If you are reactivating a paused project:** The conservative estimate of your likely spend is your spend to date during the month plus any usage that was not charged.

**Note**  
Spend limits exclude credits and apply to pre-tax charges.

## Notifications
<a name="spend-limit-notifications"></a>

You'll receive notifications when actual costs reach 50%, 75%, and 90% of your limit, or when you are on track to reach or exceed your spend limit in the next 10 days.

## Customize your spend limit settings with optional early cost controls
<a name="spend-limit-early-controls"></a>

Your spend limit keeps your bill from growing past the amount you set. If your usage reaches it, AWS pauses your resources to protect you. These optional controls act earlier and more gently, so you stay well below the limit.

### Stop new resource creation
<a name="spend-limit-stop-new-resources"></a>

About 7 days before you would reach your limit, new resources stop launching. This is achieved through application of a service control policy that is managed by AWS. The service control policy depends on the service. To view all service control policies that might be applied to your project, see [Service control policies for spend limits](scps-and-rcps-for-projects.md#scps-for-spend-limits).

All your resources that are already running stay running. In most cases, nothing you have built is affected. However, in some cases this could lead to a disruptive experience. For example, if you have enabled auto-scaling, and if conditions are met to execute this action, new instances won't launch.

### Pause idle resources
<a name="spend-limit-pause-idle"></a>

About 5 days before you would reach your limit, idle resources are paused. Your active apps keep running. Idle resources are paused based on recommendations by AWS Compute Optimizer. For more information, see [View idle recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/view-idle-recommendations.html).

You can also view your idle resources recommendations by logging into your project and viewing savings opportunities. For more information, see [Cost Optimization Hub](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html). At this time, as part of your spend limits experience we will automatically pause EC2, RDS and SageMaker endpoints.

**Why we pause an EC2 instance:** We pause EC2 instances if the peak CPU utilization is below 5% and your network I/O is less than 5 MB per day over the last 14 days.

If you have a G or P instance type, there's a different idle criterion. G or P instance types will be paused if the following is true over the last 14 days:
+ GPU isn't actively working for more than 99% of the lookback period
+ GPU encoder isn't used for 99% or more of the instance's runtime
+ GPU memory usage at instance level is less than 5%
+ CPU maximum utilization is less than 5%
+ Network utilization is less than 5 MB/day

**Why we pause an RDS database:** We pause RDS for MySQL and RDS for PostgreSQL if the database instance is not a read replica and has the following over the past 14 days:
+ No database connections
+ Low CPU usage
+ Low read/write activity

**Why we pause an idle SageMaker endpoint:** We pause SageMaker endpoints if the endpoint had zero invocations in the past 14 days.

### Pause top cost drivers
<a name="spend-limit-pause-top-cost"></a>

About 4 days before you would reach your limit, your highest cost incurring active resources are paused. This can be a disruptive experience. At this time, we select the resources from these five services: EC2, RDS, Lambda, Bedrock, and SageMaker. This opt-in control might prevent you from incurring costs if you have a runaway Lambda or unexpected Bedrock spike.

## What happens if you reach your limit
<a name="spend-limit-reached"></a>

AWS pauses your project and stops all resources. Your data is preserved.

To reactivate your project, increase your spend limit from AWS Settings. After reactivation, some resources may need to be manually restarted.

**Important**  
If you take no action within 90 days of your project being paused, AWS permanently deletes your project data.

## Other important things to note
<a name="spend-limit-other-notes"></a>
+ If you use Amazon Route 53, you can only purchase one domain every 24 hours. You must ensure that domain costs are within spend limits, otherwise, your domain purchase won't go through. In such cases, you must increase spend limits before making a purchase.
+ You can apply spend limits to up to 10 projects.

## Create a spend limit in AWS Settings
<a name="create-spend-limit-procedure"></a>

**To create a spend limit in AWS Settings**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Billing**.

1. In **Cost by project**, for **Spend limit**, choose **Set limit** for a project.

1. You can either choose the recommended spend limit or a custom limit.

1. If you choose a custom limit, enter the custom amount.

1. Choose **Set spend limit**.

1. To customize your spend limit with early cost controls, you can select **Stop new resource launches**, **Pause idle resources**, or **Pause top cost drivers**.

1. Choose **Save early cost controls**.

The spend limit will take effect immediately.