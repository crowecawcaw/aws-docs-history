# Assess

The assess phase of AWS migration is a crucial step that lays the
foundation for a successful migration journey. In this phase, you
delve into various aspects of your migration plan, aligning it
with your organization's goals. To achieve this, you must consider
the scope, technology, and processes involved. Your migration plan
should be based on up-to-date data obtained through a
comprehensive discovery exercise, particularly vital for
long-running migrations. This data informs your migration patterns
and helps in refining your plans regularly.

| MIG-OPS-01: Does your migration planning consider scope, technology, and process? |
| --------------------------------------------------------------------------------- |
|                                                                                   |

Your migration planning is the key to a successful migration to
AWS, and needs to cover many aspects. These include ensuring you
have the right skills at the points when they are needed and the
capacity required to meet your timeline, scope, and budget. The
requirements on your staff are driven by what you are migrating,
so your plan has to be based on up-to-date data from your
environment, obtained through a discovery exercise early on in
the migration process. For long running migrations spanning over
a year, this data needs to be refreshed and used to refine the
plans on a regular basis. The gathered discovery data may inform
which migration patterns can be adopted.

## MIG-OPS-BP-1.1 Your migration plan must be informed by and reflect technology, processes and business

This BP applies to the following best practice areas:
Organization

### Implementation guidance

**Suggestion 1.1.1**: Define the scope. What are you migrating?

In large migrations, the scope of the program can often remain undefined, even when you're halfway through the migration process. This uncertainty arises because certain factors may only surface in later stages. For instance, you might discover pockets of shadow IT or overlooked network and security requirements essential for your applications to function correctly. To address this, it's advisable to invest time in clearly defining the scope, starting from your desired business outcomes and potentially using discovery tools to uncover assets, as discussed later in this guide.

Furthermore, it's important to acknowledge that the scope is likely to evolve as large migrations frequently encompass unexpected elements. These surprises may include unidentified systems or unforeseen production incidents that can disrupt your plans. Therefore, it's crucial to remain adaptable and have contingency plans in place to ensure the smooth progress of your migration program. For more detail, see [Strategy and best practices for AWS large migrations](../../../prescriptive-guidance/latest/strategy-large-scale-migrations/scope-strategy-time.md "../../../prescriptive-guidance/latest/strategy-large-scale-migrations/scope-strategy-time.md").

**Suggestion 1.1.2:** Understand your current on-premise inventory. Identify the missing details you need to collect and select the right discovery tool to do so.

Begin by identifying the information you have available regarding the environment you intend to migrate and the format in which it exists. Determine what additional information is missing, which is crucial for the workloads you plan to migrate. For instance, you may need insights into your on-premises database systems, networking metrics, application dependencies, visualization requirements, or other resource utilization profiles. Based on these requirements, you should select a discovery tool that can provide this information while adhering to your organization's operational and security standards (for example, whether the tool should be agent-based or agent-less).

Once you've pinpointed the discovery requirements, use a [comparison matrix](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/ "https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/") to filter out some of the available options. This results in a list of discovery tools that meet your specific requirements. Following this initial filtration, it is advisable to apply [this three-step technique](https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/ "https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/") to further narrow down and prioritize the list of discovery tools based on the essential features required for your business.

**Suggestion 1.1.3:** Perform a comprehensive portfolio discovery exercise to understand dependencies and complexity.

Completing a portfolio and discovery exercise is a requirement for a successful migration. In rehost migrations, this discovery exercise needs to be focused on capturing inventory, server to application mapping, and dependencies between systems in order to understand the affinities to drive migration waves and planning. It also provides validation of the scope and approach. For further guidance, see [Portfolio playbook for AWS large migrations](../../../prescriptive-guidance/latest/large-migration-portfolio-playbook/welcome.md "../../../prescriptive-guidance/latest/large-migration-portfolio-playbook/welcome.md").

**Suggestion 1.1.4**: Familiarize yourself with recommended strategies and best practices for large migrations.

Migrating to AWS can be driven by various reasons, such as moving away from aging data centers, improving operational resilience and security posture, or reducing costs. Regardless of the motive, it's crucial to identify and prioritize these drivers, as they can impact migration in terms of time, cost, scope, and risk. Alignment of requirements across different teams, including Infrastructure, security, application, and operations, is key to a successful migration. This alignment aligns everyone towards a common goal and timeline. It's essential to explore how desired business outcomes can harmonize with various team objectives. In large migrations, it's advisable to adopt a _migrate first, then modernize_ mindset to manage technical debt efficiently and leverage AWS scalability for long-term benefits in infrastructure deployment and feature release cycles. For detail on setting up and running a migration project at scale, see [Strategy and best practices for AWS large migrations](../../../prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.md "../../../prescriptive-guidance/latest/strategy-large-scale-migrations/welcome.md").

**Suggestion 1.1.5**: Familiarize yourself with the technology available to you to expedite the migration.

Technology provides a great foundation for accelerating large migrations. For example, the [Cloud Migration Factory solution](https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/ "https://aws.amazon.com/solutions/implementations/cloud-migration-factory-on-aws/") is focused on how to provide end-to-end automation for migrations. For more detail, review the Technology Perspective in [Strategy and best practices for AWS large migrations](../../../prescriptive-guidance/latest/strategy-large-scale-migrations/technology.md "../../../prescriptive-guidance/latest/strategy-large-scale-migrations/technology.md"). Check this guidance to explore some of the best practices for using technology to achieve the scale and velocity required, aligned with the scope, strategy, and timelines.

**Suggestion 1.1.6**: Define your process.

Having a well-defined process is a key for a successful
migration. Things like clear escalation path to remove
blocker, communication plan, and change request process are
examples of processes that need to be defined and refined as
the migration occurs. For a more comprehensive list of
example processes to define, see
[Process
perspective](../../../prescriptive-guidance/latest/strategy-large-scale-migrations/process.md "../../../prescriptive-guidance/latest/strategy-large-scale-migrations/process.md").
