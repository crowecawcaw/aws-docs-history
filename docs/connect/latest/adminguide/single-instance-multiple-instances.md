# Connect Customer: Single Instance or Multiple Instances?

## Single instance of Connect Customer (including single ACGR pair)

### Best For

A centralized contact center operation with shared infrastructure and unified
customer experience.

### Pros

- **Lower operational overhead** –
  Manage/maintain single system, less duplication of
  setup/config.
- **Centralized management** – Unified
  metrics, reporting, queues, routing profiles, users.
- **Consistent customer experience** –
  Common IVR, flows, and settings across teams.

### Cons

- **Data/tenant isolation design** – Data
  isolation across business units, brands, or regions must be
  designed.
- **Single Geographic Location** – Latency
  can be high in regions far away from the instance.
- **Service Quota Management** – Service
  quota management can be more challenging due to difficulty in
  anticipating usage and growth across multiple business units.

## Multiple instances of Connect Customer

### Best For

Enterprises with geographic, regulatory, or security requirements infeasible
to implement in single-region (telephony, data segregation, latency due to
physical distance).

### Pros

- **Strong isolation** – Each BU or region
  can have its own agents, routing, reporting. Isolation is required for
  agents in India, South Korea, and South Africa.
- **Tailored configurations** – Flows,
  prompts, integrations can be customized per instance.
- **Simpler data residency** – Can be
  useful for compliance in multinational organizations.
- **Reduced blast radius** – An issue in
  one instance doesn't affect others.
- **Geographic proximity** – Regions can be
  chosen to keep local telephony traffic local.

### Cons

- **Higher management overhead** – Need to
  maintain and update multiple environments.
- **Fragmented reporting** – Multi-region
  reporting currently needs to be built.
- **Increased costs** – Each instance might
  require duplicate resources (Lambda, Amazon Lex, API).
- **Inconsistent user experience** – Unless
  strictly governed, each instance might drift in flow design, customer
  experience, customer security models.

## Summary

The decision of single- vs. multiple-instance architecture is nuanced, and highly
dependent on the nature of the customer's requirements. Considering the scalability,
customizability, programmability, and security of Connect Customer, we generally recommend
single-instance Connect Customer architectures (including a single Connect Customer Global Resiliency
pair) in the absence of compelling requirements requiring multiple regions.
