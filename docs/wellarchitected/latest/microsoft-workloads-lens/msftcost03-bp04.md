# MSFTCOST03-BP04 Evaluate SQL Server Developer edition

SQL Server Developer edition includes all functionality of the
Enterprise edition. It is a free edition that can be used in
non-production environments. A production environment is defined as
an environment that is accessed by the end users of an application
(for example, a website) and is used for more than gathering
feedback or acceptance testing of that application. The Developer
edition can be leveraged for development and testing your workload.

**Desired outcome:** By evaluating
and implementing SQL Server Developer edition in non-production
environments, the organization aims to reduce licensing costs while
maintaining full Enterprise edition functionality for development
and testing purposes. This change will optimize costs without
compromising the ability to develop and test workloads effectively,
ensuring that production environments remain properly licensed while
development environments leverage the free Developer edition.

**Common anti-patterns:**

- Using SQL Server Developer edition in production environments to
  save costs, exposing the organization to licensing compliance
  issues and violating Microsoft's terms of use while putting
  end-user applications at risk.
- Maintaining Enterprise edition licenses across all development
  and testing environments without evaluating Developer edition
  alternatives, resulting in unnecessary licensing costs and
  inefficient resource allocation for non-production workloads.

**Benefits of establishing this best
practice:**

- Significant cost savings: By implementing SQL Server Developer
  edition in non-production environments, organizations can
  substantially reduce licensing costs, as Developer edition is
  free for use in development and testing scenarios.
- Full feature access for development: Teams gain access to all
  Enterprise edition features in their development and testing
  environments, ensuring that they can build and test applications
  using the full range of SQL Server capabilities without
  incurring additional costs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Identify non-production SQL Server instances, create a migration
plan for downgrading to Developer edition, and implement controls
to ensure Developer edition is only used in development and
testing environments while maintaining proper licensing
compliance.

### Implementation steps

1. Inventory all SQL Server instances, identifying
   non-production environments.
2. Develop a migration plan for downgrading eligible instances
   to Developer edition.
3. Implement the downgrade process following AWS documentation.
4. Test applications thoroughly in the downgraded environments.
5. Implement controls and monitoring to prevent Developer
   edition use in production.

## Resources

**Related documents:**

- [Evaluate
  SQL Server Developer edition](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-dev.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-dev.md")
- [How
  to manually downgrade SQL Server Enterprise edition to
  Developer edition on AWS and save on licensing costs](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-manually-downgrade-sql-server-enterprise-edition-to-developer-edition-on-aws-and-save-on-licensing-costs/ "https://aws.amazon.com/blogs/modernizing-with-aws/how-to-manually-downgrade-sql-server-enterprise-edition-to-developer-edition-on-aws-and-save-on-licensing-costs/")
- [Automate
  downgrading SQL Server to Developer edition on Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-automate-downgrading-sql-server-to-developer-edition-on-amazon-ec2/ "https://aws.amazon.com/blogs/modernizing-with-aws/how-to-automate-downgrading-sql-server-to-developer-edition-on-amazon-ec2/")
