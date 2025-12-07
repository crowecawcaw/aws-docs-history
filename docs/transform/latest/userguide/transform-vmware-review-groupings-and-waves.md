# Migration planning

The Migration planning job step within AWS Transform for VMware is a collaborative chat-based experience for
planning large migrations. AWS Transform agents apply AWS Prescriptive Guidance to guide customers from analysis of on-premises data to finalized migration wave plans.

After the Discover on-premises data job completes successfully, AWS Transform uses the discovery data to group applications into migration waves. AWS Transform guides
you through steps to analyze and scope your servers, group them into applications, generate move groups, and build migration waves. When analyzing your on-premises environment, you can ask questions to better understand how
AWS Transform analyzed your installed software, for example, server dependencies and network architecture.

AWS Transform supports scope adjustments within application groups and waves. You can re-upload discovery data at any time,
and AWS Transform will automatically process, de-duplicate, and merge new records with existing data.
When changes are detected—such as newly discovered dependencies or infrastructure additions, AWS Transform will flag impacted dependency groups and provide recommendations for wave plan adjustments.
Migration planning can also make use of unstructured text data to enrich the planning process.

There are four migration planning stages:

- In **Scope and analyze**, you can review your discovery data,
  ask questions about your software and network environment and determine the resources in
  scope for migration.
- In **Group apps**, you can provide a combination of business
  and technical rules regarding, for example, hostname analysis, network dependencies, and business rules, so that migration planning can group your infrastructure
  into applications. If you already have an inventory of your applications,
  migration planning can use that instead.
- In **Generate move groups**, you can give migration planning your
  technical and business requirements so that it can determine which applications must
  be moved together. Technical dependencies include databases, message queues, or other resources shared between multiple apps.
  Business and operational dependencies include business criticality, RPO and RTO, data center location, and application owners.
- Finally, in **Build waves**, you can give migration planning
  context about your timelines and priorities so it can build a wave plan that
  you can migrate. You can select move groups for inclusion in a wave based on
  factors such as priority score, move group size, user counts, and
  application complexity.
  **Migration Planning Terminology:**

- _Migration waves_ are logical groups that are migrated
  together. Migration waves are comprised of one or more move groups.
- A _move group_ is a set of co-dependent applications that
  must be moved together. They may have technical dependencies such as a
  shared database or they have business dependencies such as supporting a
  shared business function.
- A _dependency_ is a relationship between systems. There are
  several types of dependencies including:
  - Critical or hard dependencies, where systems cannot operate without the dependency. Common
    examples of this are applications that depend on databases, other
    applications, or services.
  - Soft dependencies, which are not critical for the operation of the system. Common examples of
    this include latency insensitive dependencies that can be migrated
    independently.
  - Non-technical dependencies include business, organizational, operational and compliance
    dependencies. These are dependencies related to your organization
    and its priorities. Examples of this include shared business
    function and organizational ownership.

## Workflow

Migration planning is an interactive and iterative workflow. You can go back and make changes to previous steps at any time. A typical migration planning workflow is:

1. Migration planning starts by summarizing the discovery data that is available. Review the available data and return to the discovery step at any time to provide additional data.
2. Within the scoping and analysis step you can ask questions about your on-premises environment
   to validate the data you have collected. Example questions
   include:
   1. List my servers by operating system
   2. Summarize my on-premises network topology
   3. List the most common technologies running in my environment.

3. While analyzing your environment, if you identify servers that should not be in scope for migration you can tell AWS Transform to exclude those resources. Examples of this include:
   1. Remove all servers which have _legacy_ in their
      hostname
   2. Remove all servers in the 10.0.2.0/24 subnet
   3. Remove all servers running versions of Windows older than 2022

4. Once you have sufficiently explored your environment and determined your migration scope you
   can tell AWS Transform to move to the next migration planning step.
5. The next step is application grouping. If you already have your servers mapped to applications, you can tell AWS Transform to use that mapping and skip this step. If you do not have your applications pre-defined you can provide the technical and business logic that defines your applications. AWS Transform will guide you through the application grouping process and suggest the data points that you can provide to effectively group your servers together into applications. The more information you can provide about your on-premises applications, the more effectively AWS Transform can group your servers into apps. Once you have provided sufficient information, you can then instruct AWS Transform to perform application grouping.
6. Once application grouping has been performed, review the application groups. You can instruct
   AWS Transform to make any necessary changes, for example:
   1. Move server example-server to application-5
   2. Rename application-5 "HR App Test Environment"
   3. Remove all Linux servers from IIS Dev Farm

7. Once your apps are grouped, instruct AWS Transform to move to the next step
8. The next step is move grouping. In the move grouping step you identify applications that must
   be moved together. Provide context around your technical and
   non-technical dependencies. AWS Transform will guide you through the process and
   suggest data points that you can provide to group your apps together.
   There are several considerations to make at this stage including:
   1. What should be the target size of move group?
   2. Do you want to combine environments, for example dev, test, and prod, for each app, or split
      them?
   3. How do you want to consider network dependencies? Are all dependencies critical or can some
      dependencies be considered soft dependencies and be split across
      move groups?

9. Once you have provided your rules for move grouping, instruct AWS Transform to
   execute your move grouping strategy. You can then review and modify your
   move groups. Once you have reviewed your move groups you can instruct
   AWS Transform to move to the final migration planning step.
10. Wave planning is the final step within migration planning. In this step, you group your move
    groups into migration waves and prioritize those waves. Within the wave
    planning step, AWS Transform will guide you through providing the business
    prioritization required to group your move groups into waves and then
    prioritize those waves. Considerations within wave planning
    include:
    1. The business criticality of each of your move groups
    2. The migration timelines and the timelines for each move group
    3. The risks associated with each move group
    4. The number of servers to migrate per wave

11. Once you have provided sufficient guidance on how to group into waves, instruct AWS Transform to execute the wave planning. You can then review your waves and modify them.
12. Once you have finalized your wave plan, you can complete migration planning and move to
    execution. You can return to migration planning at any time to refine
    and iterate on your plan.
