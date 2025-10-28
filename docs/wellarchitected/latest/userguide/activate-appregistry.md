# Activating AppRegistry for a workload

Using AppRegistry is optional, and AWS Business and Enterprise Support customers can
activate it on a per-workload basis.

Whenever Discovery support is turned on and AppRegistry is associated with a new or
existing workload, AWS Well-Architected Tool creates a service-managed attribute group. The attribute
group **Metadata** in AppRegistry contains the workload ARN, the
workload name, and the risks associated with the workload.

- When Discovery support is turned on, any time there is a change to the workload, the
  attribute group is updated.
- When Discovery support is turned off or the application is removed from the workload, the
  workload information is removed from AWS Service Catalog.
  If you want an AppRegistry application to drive the data fetched from Trusted Advisor, set
  your workload **Resource definition** as
  **AppRegistry** or **All**. Create roles for all
  accounts that own resources in your application following the guidelines in [Activating Trusted Advisor for a workload in
  IAM](activate-ta-in-iam.md "activate-ta-in-iam.md").
