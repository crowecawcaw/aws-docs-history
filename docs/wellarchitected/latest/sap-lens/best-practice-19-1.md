# Best Practice 19.1 – Understand access

and retention requirements

Understand the ways in which you access and retain data. Consider active data,
document management systems, and backups.

**Suggestion 19.1.1 – Categorize the different types of business data
in the SAP system**

By categorizing the different types of data and how frequently data is accessed (data
temperature) from a business perspective, it is possible to identify opportunities to
archive or offload data from your SAP system to optimize cost.

The following are some of the common data types found in an SAP system:

- **Reference** — Data for which the values change
  infrequently, for example, city, country, and exchange rates
- **SAP Master Data** — Data for which the values
  change rarely, for example, SAP Customer Master, product
- **Audit** — Data kept for audit purposes, for
  example, change logs
- **Transaction** — Data created as part of day-to-day
  business operations, for example, sales orders
- **Analytical** — Data created to support analysis and
  decision making, for example, monthly sales reporting
  Classify the data temperature as follows:

- **Hot** — Data is accessed frequently
- **Warm** — Data is not accessed frequently
- **Cold** — Data is only accessed sporadically
  Classify retention requirements as follows:

- Retain for disaster recovery (DR) purposes
- Retain for reference purposes
- Retain for compliance or audit purposes
