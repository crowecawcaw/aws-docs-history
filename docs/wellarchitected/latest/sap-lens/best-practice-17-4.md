# Best Practice 17.4 – Review the size,

granularity, and latest available EC2 instances for SAP components

Smaller EC2 instances provide greater cost flexibility in SAP workloads. They
introduce options for horizontal scaling that allow for compute to be switched off when
not in use or scaled up only during peak loads. Adopting a consistent EC2 instance size at
the application tier will help you maximize the benefits of Reserved Instance and Savings
Plans commitments across all workloads. Take into account the latest available AWS SAP
certified instances. The operational impact, license costs, support, sharing and
reusability for each component should also be evaluated.

**Suggestion 17.4.1 – Evaluate the cost benefits of multiple smaller
application servers to provide flexibility**

For many SAP workloads, application servers can be designed to be immutable. Having a
standard application server configuration, which is scaled horizontally by replicating the
base unit, gives options for consistent repeatable units. The advantages are reusability,
compute utilization, reservations, and automation. Per-unit requirements, such as
operating system licensing, storage duplication, and management costs, should be factored
into the evaluation.

Consider the following:

- SAP on AWS Blog: [DevOps for SAP – Driving Innovation and Lowering Costs](https://aws.amazon.com/blogs/awsforsap/devops-for-sap-driving-innovation-and-lowering-costs/ "https://aws.amazon.com/blogs/awsforsap/devops-for-sap-driving-innovation-and-lowering-costs/").
- SAP on AWS Blog: [Using AWS to allow SAP Application Auto Scaling](https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/ "https://aws.amazon.com/blogs/awsforsap/using-aws-to-enable-sap-application-auto-scaling/")

**Suggestion 17.4.2 – Evaluate the cost benefits of an SAP HANA
scale-out configuration where supported**

SAP OLAP workloads can be deployed in both [scale-up and scale-out](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/a165e192ba374c2a8b17566f89fe8419.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.05/en-US/a165e192ba374c2a8b17566f89fe8419.html") configurations. SAP recommends to scale-up before scaling
out to reduce operational complexity. However, scale-out implementations might be applicable
for larger analytical or native SAP HANA workloads, which require significant compute
(SAPS).

In certain cases, S/4HANA also supports scale-out configuration but with
restrictions. See SAP Note: [2408419 - SAP S/4HANA - Multi-Node Support](https://launchpad.support.sap.com/#/notes/2408419 "https://launchpad.support.sap.com/#/notes/2408419") [Requires SAP Portal Access].

When considering scale-up vs. scale-out consider the following:

- [Certified EC2 instance sizes](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:105 "https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:23;v:105") available for scale-up and scale-out
- The cost per GiB of EC2 memory for each instance family. Larger EC2 instances
  typically have a higher cost per GiB than smaller instances.
- The added complexity and operational overhead of managing data distribution in
  scale-out deployments. See SAP Note: [2081591 - FAQ: SAP HANA
  Table Distribution](https://launchpad.support.sap.com/#/notes/2081591 "https://launchpad.support.sap.com/#/notes/2081591") [Requires SAP Portal Access]
