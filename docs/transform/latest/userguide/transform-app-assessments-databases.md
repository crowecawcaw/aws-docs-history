

# Database assessments
<a name="transform-app-assessments-databases"></a>

AWS Transform assesses your Microsoft SQL Server workloads and helps you choose between a fully managed database on Amazon RDS for SQL Server and running SQL Server yourself on Amazon EC2. For each option, AWS Transform detects the SQL Server edition, right-sizes compute and storage to your workload, analyzes licensing, and produces a cost comparison so you can see the trade-offs side by side.

## Amazon RDS for SQL Server
<a name="transform-app-assessments-databases-rds-sql"></a>

AWS Transform assesses the cost of migrating on-premises SQL Server databases to Amazon RDS for SQL Server. Using AI-powered agents, AWS Transform analyzes your on-premises SQL Server environment and delivers a complete migration business case in minutes, with compute and memory recommendations matched to your workload requirements so you avoid over-provisioning and only pay for what you need.

The RDS for SQL Server assessment includes the following capabilities:
+ Bring Your Own Media (BYOM) licensing, allowing you to use your existing SQL Server licenses through Microsoft License Mobility with Software Assurance. With BYOM there is no SQL Server license fee from AWS; you pay only for AWS infrastructure and Windows operating system fees. BYOM supports SQL Server Standard and Enterprise editions.
+ License Included (LI) licensing, where the SQL Server license is included in your Amazon RDS hourly rate. License Included supports the Web, Express, Standard, Developer, and Enterprise editions.
+ Cost optimization using Database Savings Plans. When a Database Savings Plan rate is available for the recommended instance, AWS Transform uses it to price the one-year term, and reports the discount compared with On-Demand pricing.
+ Eligibility checks for [Optimize CPU](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Concepts.General.OptimizeCPU.html), which can reduce the vCPU count and the licensing cost of an instance. These checks are on by default.
+ Discounts that you specify, such as an Enterprise Discount Program (EDP) percentage or a custom discount percentage, applied across the assessment.

AWS Transform also reports two savings that come from moving to a managed database. Labor savings compare the operating effort for SQL Server on Amazon EC2 with Amazon RDS, using an hourly labor rate that you can change. Software Assurance savings estimate the annual Microsoft Software Assurance fees that you no longer pay when you move to License Included pricing on Amazon RDS. Bring Your Own Media is the default license model. With it, you keep paying Software Assurance, so Software Assurance savings appear only when you choose License Included.

### Right-sizing and edition recommendations
<a name="transform-app-assessments-databases-rds-sql-rightsizing"></a>

On-premises SQL Server environments are frequently over-provisioned. AWS Transform right-sizes each database to its actual workload, taking advantage of the fact that scaling an RDS instance up or down later is a fast, low-downtime operation. Because the number of vCPUs is the largest driver of ongoing cost—instance classes with more vCPUs are more expensive, and SQL Server is licensed per core— AWS Transform focuses right-sizing on matching compute and memory to demand, and favors memory-optimized instance classes for memory-bound workloads.

AWS Transform also reviews whether a workload needs SQL Server Enterprise edition or can run on the lower-cost Standard edition. Because more capabilities move into Standard edition with each SQL Server release, many workloads that historically required Enterprise edition can migrate to Standard, reducing licensing cost.

For non-production servers, AWS Transform recommends SQL Server Developer edition. Non-production instances priced On-Demand are costed for reduced uptime rather than for every hour of the month.

### Getting started
<a name="transform-app-assessments-databases-rds-sql-inputs"></a>

You can start your RDS for SQL Server assessment with any supported data format, including RVTools exports, configuration management database (CMDB) data, exports from the AWS Transform discovery tool, and other third-party discovery tools. Create what-if scenarios to compare multiple cost models with customized assumptions, including AWS Region, resource utilization, and pricing terms.

Example prompts:
+ "Estimate the cost of migrating my SQL Server databases to RDS for SQL Server"
+ "Compare BYOM vs License Included pricing for RDS for SQL Server"
+ "Show me Database Savings Plans options for my RDS workloads"
+ "Which of my databases can run on Standard edition instead of Enterprise?"

## SQL Server on Amazon EC2
<a name="transform-app-assessments-databases-sql-ec2"></a>

AWS Transform assesses SQL Server workloads that you intend to run on Amazon EC2 and provides right-sizing recommendations and licensing analysis. For Amazon EC2, you can bring your existing SQL Server licenses through License Mobility (Bring Your Own License, or BYOL), which is the default, or use License Included (LI) pricing. SQL Server workloads on Amazon EC2 are priced on shared tenancy. To reduce licensing cost, you can also turn on core optimization, which reduces the number of licensable cores, with a minimum of four licensable cores.

Running SQL Server on Amazon EC2 gives you full control over the operating system and the SQL Server instance, while Amazon RDS for SQL Server removes the undifferentiated management of the database engine. AWS Transform lets you compare the two so you can decide per workload. Consider these factors when comparing:
+ Bring Your Own License and Bring Your Own Media require active Microsoft Software Assurance, which is an annual cost. When the Amazon RDS for SQL Server recommendation uses License Included pricing, AWS Transform reports the Software Assurance fees that you would no longer pay.
+ Amazon RDS for SQL Server also reduces operating effort. AWS Transform reports the labor savings of Amazon RDS compared with SQL Server on Amazon EC2.

Example prompts:
+ "What if I move my SQL Server workloads to RDS for SQL Server instead of EC2?"
+ "Compare BYOL on EC2 with License Included on RDS for my SQL Server estate"
+ "Create a License Included scenario for all SQL Server workloads on EC2"