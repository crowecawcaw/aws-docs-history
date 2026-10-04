

# Database assessments
<a name="transform-app-assessments-databases"></a>

AWS Transform assesses your Microsoft SQL Server workloads and helps you choose between a fully managed database on Amazon RDS for SQL Server and running SQL Server yourself on Amazon EC2. For each option, AWS Transform detects the SQL Server edition, right-sizes compute and storage to your workload, analyzes licensing, and produces a cost comparison so you can see the trade-offs side by side.

## Amazon RDS for SQL Server
<a name="transform-app-assessments-databases-rds-sql"></a>

AWS Transform assesses the cost of migrating on-premises SQL Server databases to Amazon RDS for SQL Server. Using AI-powered agents, AWS Transform analyzes your on-premises SQL Server environment and delivers a complete migration business case in minutes, with compute and memory recommendations matched to your workload requirements so you avoid over-provisioning and only pay for what you need.

The RDS for SQL Server assessment includes the following capabilities:
+ Bring Your Own Media (BYOM) licensing, allowing you to use your existing SQL Server licenses through Microsoft License Mobility with Software Assurance. With BYOM there is no SQL Server license fee from AWS; you pay only for AWS infrastructure and Windows operating system fees. BYOM supports SQL Server Standard and Enterprise editions.
+ License Included (LI) licensing, where the SQL Server license is included in your Amazon RDS hourly rate. License Included supports the Web, Express, Standard, Developer, and Enterprise editions.
+ Cost optimization using Database Savings Plans, which offer up to 20 percent savings compared to On-Demand pricing.
+ Eligibility assessment for the AWS Migration Acceleration Program (MAP), which provides credits and support to offset migration costs.

### Right-sizing and edition recommendations
<a name="transform-app-assessments-databases-rds-sql-rightsizing"></a>

On-premises SQL Server environments are frequently over-provisioned. AWS Transform right-sizes each database to its actual workload, taking advantage of the fact that scaling an RDS instance up or down later is a fast, low-downtime operation. Because the number of vCPUs is the largest driver of ongoing cost—instance classes with more vCPUs are more expensive, and SQL Server is licensed per core— AWS Transform focuses right-sizing on matching compute and memory to demand, and favors memory-optimized instance classes for memory-bound workloads.

AWS Transform also reviews whether a workload needs SQL Server Enterprise edition or can run on the lower-cost Standard edition. Because more capabilities move into Standard edition with each SQL Server release, many workloads that historically required Enterprise edition can migrate to Standard, reducing licensing cost.

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

AWS Transform assesses SQL Server workloads that you intend to run on Amazon EC2 and provides right-sizing recommendations, licensing analysis, and dedicated host mappings. For Amazon EC2, you can bring your existing SQL Server licenses through License Mobility (Bring Your Own License, or BYOL) or use License Included (LI) pricing.

Running SQL Server on Amazon EC2 gives you full control over the operating system and the SQL Server instance, while Amazon RDS for SQL Server removes the undifferentiated management of the database engine. AWS Transform lets you compare the two so you can decide per workload. Consider these factors when comparing:
+ Bring Your Own License and Bring Your Own Media require active Microsoft Software Assurance, which is an annual cost that AWS Transform can account for in the comparison.
+ Dedicated host mappings are relevant when your licensing terms require you to license physical cores or use dedicated tenancy.

Example prompts:
+ "What if I move my SQL Server workloads to RDS for SQL Server instead of EC2?"
+ "Compare BYOL on EC2 with License Included on RDS for my SQL Server estate"
+ "Create a License Included scenario for all SQL Server workloads on EC2"