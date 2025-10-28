# Design principles

There are four general design principles to facilitate good
design for hybrid cloud workloads. These design principles help
keep data where it needs to be to meet regulatory or compliance
needs. The design principles are as follows:

- **Classify data:** To comply
  with data residency requirements, it is important to
  understand and classify which workloads and which datasets
  need to stay on-premises and which ones can be moved to the
  Region.
- **Establish operational practices for
  data sovereignty:** Once you have identified which
  datasets and workloads needs to stay on-premises (Outposts)
  or in a certain geographical location with Local Zones,
  build an operational model with your teams to have different
  processes and procedures for the different data
  classifications. This can include different AWS accounts
  with the correct privileges and custom nomenclature for
  sensitive workloads for easy identification.
- **Use Regional cloud services to
  augment on-premise solutions:** Although Local
  Zones and Outposts rack come with a subset of the services
  available in the Region, customers should use Regional
  services such as AWS Organizations, AWS Control Tower, and
  IAM Access Analyzer to provide data residency and regulatory
  compliance. Use Regional services to offer your builders
  pre-approved configurations, self-service provisioning, and
  service quotas.
- **Automate infrastructure:**
  Consider building different automation runbooks or
  automation stacks based on the type of data that is being
  used or stored inside a workload. Your operational teams can
  build compliant technical stacks quickly while removing the
  manual work that introduces mistakes (for example, sending a
  regulatory workload to the Region by accident).
