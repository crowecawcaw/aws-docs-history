Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Allocating extra compute resources for automatic database optimization

Autonomics improve query performances on your cluster and help manage storage costs
and optimization. You can choose to allocate extra compute resources to ensure that
autonomics features run consistently, even during times of high traffic, to benefit
from the optimization. Note that autonomics run using these extra resources are billable.
For more information on billing for autonomics, see [Billing for autonomics operations](t_autonomics-billing.md "t_autonomics-billing.md")
and [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/").

If extra compute resources for autonomics are disabled, Amazon Redshift temporarily suspends
autonomics operations during periods of high system load in order to minimize impact
on concurrent workloads, until there are enough resources to run them without negatively
impacting user queries, potentially impacting performances.

## Managing extra compute resources for autonomics

By default, extra compute resources for autonomics are disabled for both provisioned clusters and serverless workgroups,
with the exception of serverless workgroups with AI-driven scaling and optimization. For serverless workgroups
with AI-driven scaling and optimization, extra compute resources for autonomics are always enabled and managed
automatically depending on your price-performance profile.

You can choose to enable extra compute resources both during or after creating the cluster or workgroup.

###

Managing extra compute resource for autonomics on provisioned clusters using the Amazon Redshift console

While creating a new cluster, you can enable extra compute resources for autonomics by choosing
**Enable extra compute** in the **Autonomics configuration** panel. To do this:

- Choose **Create cluster**.
- In the **Autonomics configuration** panel, choose **Enable extra compute**.
- You will create a cluster with extra compute enabled.

For more information, see [Creating a cluster](../mgmt/create-cluster.md "../mgmt/create-cluster.md") in the _Amazon Redshift Management Guide_.

To enable extra compute resources after creating a cluster:

- Navigate to the cluster in the Amazon Redshift console.
- In the cluster details page, select **Edit autonomics configuration** from the **Actions** drop-down menu.
- Choose **Enable extra compute**.

###

Managing extra compute autonomics for provisioned clusters using the AWS CLI

To create a provisioned cluster with extra compute resources for autonomics,
use the `create-cluster` command with the `extra-compute-for-automatic-optimization` option.

```

aws redshift create-cluster --cluster-identifier <value> \
--node-type <value> \
--cluster-type <value> \
--master-username <value> \
--master-user-password <value> \
--extra-compute-for-automatic-optimization \
--region <value>
```

To enable extra compute resources for autonomics on an existing provisioned cluster,
use the `modify-cluster` command with the `extra-compute-for-automatic-optimization` option.

```

aws redshift modify-cluster --cluster-identifier <value> \
--extra-compute-for-automatic-optimization \
--region <value>
```

To disable extra compute resources for autonomics on an existing provisioned cluster,
use the `modify-cluster` command with the `no-extra-compute-for-automatic-optimization` option.

```

aws redshift modify-cluster --cluster-identifier <value> \
--no-extra-compute-for-automatic-optimization \
--region <value>
```

###

Managing extra compute autonomics for serverless workgroups using the Amazon Redshift console

While creating a new workgroup, you can enable extra compute resources for autonomics by choosing
**Enable extra compute** in the **Autonomics configuration** panel.

- Choose **Create workgroup**.
- At **Step 1**, in the **Autonomics configuration** panel, choose **Enable extra compute**.
- You will create a serverless workgroup with extra compute enabled.

###### Note

The **Enable extra compute** option may not be available if you have selected a **Price-performance target**.
This is because for serverless workgroups with AI-driven scaling and optimization, extra compute resources for autonomics
are automatically enabled and managed based on your price-performance profile.

To enable extra compute resources after creating a workgroup:

- Navigate to the workgroup in the Amazon Redshift Serverless console.
- From the workgroup's details page, select **Edit autonomics configuration** from the **Actions** drop-down menu.
- Choose **Enable extra compute**.

###### Note

The **Edit autonomics configuration** option may be grayed out if the workgroup has a **Price-performance target** set.
This is because for serverless workgroups with AI-driven scaling and optimization, extra compute resources for autonomics
are automatically enabled and managed based on your price-performance profile.

###

Managing extra compute autonomics for serverless workgroups using the AWS CLI

To create a serverless workgroup with extra compute resources allocated for autonomics,
use the `create-workgroup` command with the `extra-compute-for-automatic-optimization` option.

```

aws redshift-serverless create-workgroup --base-capacity <value> \
--namespace-name <value> \
--workgroup-name <value> \
--extra-compute-for-automatic-optimization \
--region <value>
```

To enable extra compute resources for autonomics on an existing serverless workgroup,
use the `update-workgroup` command with the `--extra-compute-for-automatic-optimization` option.

```

aws redshift-serverless update-workgroup \
--workgroup-name <value> \
--extra-compute-for-automatic-optimization \
--region <value>
```

To disable extra compute resources for autonomics on an existing serverless workgroup,
use the `update-workgroup` command with the `--no-extra-compute-for-automatic-optimization` option.

```

aws redshift-serverless update-workgroup \
--workgroup-name <value> \
--no-extra-compute-for-automatic-optimization \
--region <value>
```

## Cost control for autonomics using extra compute resources

###

Cost control for extra compute autonomics on provisioned clusters

You can set usage limits on extra compute resources used for autonomics on provisioned clusters using the Amazon Redshift
console. Extra compute resources used for autonomics don't count against any
limits you might have set for concurrency scaling and vice versa.

To create a usage limit for extra compute using the console:

- Navigate to the cluster details page and select the **Maintenance** tab from the cluster navigation menu.
- Scroll down and click **Create usage limits**, it will navigate to **Manage usage limits** page.
- On the **Manage usage limits** page, locate the section titled **Usage limit for extra compute for automatic optimization** and select **Add limit**.

To create a usage limit for extra compute using the AWS CLI, use the `create-usage-limit` command
with the feature type `extra-compute-for-automatic-optimization`. The `--limit-type` parameter
must be set to `time` for this feature type.

```

aws redshift create-usage-limit \
--cluster-identifier <value> \
--feature-type extra-compute-for-automatic-optimization \
--limit-type time \
--period <value> \
--amount <value> \
--breach-action <value>
```

The `--period` and `--breach-action` parameters accept the same values as other usage limits.
For more information, see
[Setting a usage limit](../mgmt/rs-mgmt-set-limit-cluster.md "../mgmt/rs-mgmt-set-limit-cluster.md")  
 in the _Amazon Redshift Management Guide_.

###

Cost control for extra compute autonomics on serverless workgroups

Amazon Redshift Serverless provides capabilities to set usage limits for serverless workgroups, see
[Setting usage limits, including setting RPU limits](../mgmt/serverless-workgroup-max-rpu.md "../mgmt/serverless-workgroup-max-rpu.md")  
 in the _Amazon Redshift Management Guide_. Usage for extra compute autonomics in Amazon Redshift Serverless is included
in the overall serverless usage, including user queries.

You can see how many RPU-seconds that your serverless workgroup is using for extra compute
autonomics using the Amazon Redshift Serverless console. To do this:

- Navigate to the **Amazon Redshift Serverless console**.
- Select **Resource monitoring** from the sidebar.
- Select a workgroup.
- Scroll down to the **Extra compute for automatic optimizations charged seconds** graph.

For more information, see
[Amazon Redshift Serverless console](../mgmt/serverless-console.md "../mgmt/serverless-console.md")  
 in the _Amazon Redshift Management Guide_.

You can also check the [SYS_SERVERLESS_USAGE](SYS_SERVERLESS_USAGE.md "SYS_SERVERLESS_USAGE.md") system view
to find the `charged_extra_compute_for_automatic_optimization_seconds`, which records accumulated
compute unit (RPU) seconds charged for automatic optimizations.
