

# View and customize the migration dashboard

The **Dashboard** tab of a migration job shows the state of your migration in charts, tables, and headline numbers.

The dashboard includes the inventory, wave plans, assessments, and progress from every job in your workspace, not only the current job. For how AWS Transform keeps this data across jobs, see [How your migration data is kept across jobs](#transform-vmware-dashboard-data-across-jobs).

## What the dashboard shows
<a name="transform-vmware-dashboard-default"></a>

By default, the dashboard has the following tabs:

**Overview**  
Progress bars for waves, applications, and servers, status charts, and a chart of migration status across resources.

**On-premises inventory**  
Tables of your physical servers, virtual machines, and hypervisor hosts, with charts by operating system, power state, and hardware. Also shows your storage volumes and the database instances found on your servers.

**Wave plan**  
The waves of the shown wave plan with their servers, vCPU, and memory per wave, tables of waves and applications, and your recent wave plans. The shown plan is the latest plan that this job created, or the latest plan in your workspace if this job hasn't created one.

**Applications**  
Every application, with a selector that shows the details of one application, the migration strategy (7Rs) report, and the application dependency diagram.

**Assessments**  
Your latest assessment, including estimated AWS and on-premises annual cost and savings, and a list of all assessments.

A tab or part whose data doesn't exist yet tells you which step fills it in. For example, the **Assessments** tab is empty until you run an assessment. Before you add any inventory, the dashboard shows an empty state.

## Keep the dashboard up to date
<a name="transform-vmware-dashboard-refresh"></a>

The dashboard refreshes automatically when your migration data changes, including changes made by other jobs in the same workspace. During server migration, it follows the status of your waves and servers as they progress. The dashboard shows when it was last updated.

To refresh the dashboard on demand, ask the agent in chat. For example, "Refresh the dashboard."

The dashboard doesn't block your migration. If the agent can't update the dashboard, it tells you and continues with the current step.

## Ask about dashboard data
<a name="transform-vmware-dashboard-ask"></a>

Ask the agent a question about what the dashboard shows, and the agent answers in chat from the same data. For example, "How many servers are in wave 1?" or "Which applications are still not started?" Asking a question doesn't change the dashboard.

## Customize the dashboard
<a name="transform-vmware-dashboard-customize"></a>

You can change what the dashboard shows by describing the change in chat. The agent adds, changes, or removes sections, such as a chart, a table, or a group of headline numbers, and keeps the rest of the dashboard as it is. For example:
+ "Add a chart of storage used per wave to the Overview tab"
+ "Show a table of Linux servers that haven't migrated yet"
+ "Show only the wave plans from this job"
+ "Remove the power state chart"

While you view the **Dashboard** tab, you can also enter a short phrase that names what to look at, such as "wave 1 servers" or "only Windows servers", and the agent changes the dashboard to show it.

By default, the dashboard includes data from every job in your workspace. To focus on the current job, ask the agent to show data for this job only. The agent changes only the sections that show that data.

Your customized dashboard is saved and keeps updating with new data until you change it again. To return to the default dashboard, choose **Reset** above the dashboard sections, or ask the agent to reset the dashboard.

## How your migration data is kept across jobs
<a name="transform-vmware-dashboard-data-across-jobs"></a>

AWS Transform keeps your migration data at the workspace level, not in a single job. Each new migration job in the workspace starts with the inventory, wave plans, assessments, and progress that earlier jobs produced. The dashboard and the agent both read from this data.

Your data updates as your jobs run:
+ Each inventory upload creates a new inventory version. AWS Transform keeps earlier versions, so you can see how your inventory changed over time.
+ Each wave plan that migration planning produces is saved as a separate plan. A newer plan doesn't replace an older one.
+ Each assessment is saved with its scenario, scope, and results.
+ Server migration steps update each server's migration status as rehost waves run.

You don't edit or delete this data directly. It changes only as your jobs progress, and asking the agent a question doesn't change it. Jobs in different workspaces don't share data.

### Plan or assess with servers from earlier jobs
<a name="transform-vmware-dashboard-reuse-inventory"></a>

When you plan or assess in a job, AWS Transform works with all of your servers. These include the servers you uploaded in this job and the servers that earlier jobs in your workspace uploaded. You don't need to upload your inventory again in each job.

The same server might have different details in this job and in your workspace, for example because you uploaded a newer export in this job. In that case, the agent asks you once which details to keep before it continues.

To limit the scope, tell the agent which servers to use. For example:
+ "Use only the servers I uploaded in this job"
+ "Start fresh from the servers in my workspace"

If you upload more inventory files later in the job, AWS Transform combines them with your workspace inventory again before the next planning or assessment step.

### Plan or assess with an earlier inventory
<a name="transform-vmware-dashboard-earlier-inventory"></a>

By default, planning and assessment use your latest inventory. To work from your inventory as it was at an earlier point, tell the agent which point you mean. For example, "Assess my inventory as it was before the second upload" or "Plan using my inventory from October 20."

The agent finds the matching inventory version and tells you which one it's using. If more than one version could match, the agent describes each by its date and contents and asks you to choose.

When you use an earlier inventory, it replaces the job's inventory, and the job uses only the servers in that version. To return to your latest inventory, tell the agent. If you upload more inventory files, the job uses your latest inventory again.

### Migrate with a saved wave plan
<a name="transform-vmware-dashboard-saved-wave-plan"></a>

When you start server migration in a job that didn't produce its own wave plan, AWS Transform checks your workspace for saved wave plans before it asks you to upload one.
+ If your workspace has saved wave plans, the agent lists each plan with its creation date, waves, and server counts. The agent then asks which plan to migrate with. You can also upload a different plan. The agent doesn't choose a plan for you.
+ If a saved plan includes servers that are no longer in your inventory, the agent tells you that the migration leaves those servers out.
+ If your workspace has no saved wave plans, upload a wave plan file as described in [Migrate servers](transform-vmware-migrate-servers.md).

After you choose a plan, the job continues with the usual server migration steps, such as choosing the migration method, target accounts, and instance and storage sizing.

### Ask about your migration history and progress
<a name="transform-vmware-dashboard-ask-history"></a>

Ask the agent in chat about your migration across all jobs in the workspace. You can ask about the following:

Inventory versions  
Each inventory version and when you uploaded it.

Inventory contents  
Servers and other resources by type, and counts grouped by a field such as operating system or database engine.

Changes between inventory versions  
Resources added or updated between two uploads.

History of a resource  
For one server or application, its inventory versions, the wave plans and assessments that include it, and its migration status.

Assessments  
Saved assessments with their scenario, scope, and results.

Migration progress  
Servers discovered, migrated, and remaining, and your completion percentage. You can also see servers by status (migrated, on premises, in flight, or failed) and the status of each wave.

Pace and projections  
Migration velocity over a recent period and a projected completion date based on that velocity. Projections are linear estimates and don't account for planned changes in pace.

Wave health  
A red, amber, or green health indicator for a wave, based on replication lag, error rate, and timeline. You can also see which waves are behind schedule and the servers in a wave by target AWS account.

Planning insights  
Servers by migration strategy, applications whose servers are split across more than one wave, and the number of servers in each application.

Data transfer  
Total data transferred and average and peak throughput per server.

For example:
+ "What changed in my inventory since the first upload?"
+ "What percentage of my planned servers have been migrated?"
+ "At the current pace, when will the migration finish?"
+ "Which waves are behind schedule?"
+ "Show me the history of server app-db-01."

To ask about the live progress of a wave that's running in the current job, ask for the wave's status in chat.