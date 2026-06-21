# Concepts

## Automated offers

Automated offers allow you to define rules that create private offers automatically based on triggers such as Buyer requests, CRM events, or governance approvals. This reduces manual effort for high-volume operations and ensures consistent offer creation.

### How automated offers work

1. **A trigger occurs** - A Buyer submits a BWA request, a CRM deal reaches a specific stage, or a governance rule approves a request.
2. **The automation rule evaluates** - The system checks whether the event matches the rule's conditions (product, amount threshold, Buyer segment).
3. **An offer is created** - If conditions are met, a private offer is generated using a predefined offer template with auto-populated fields from the trigger data.
4. **Post-creation actions fire** - Notifications, CRM updates, or Slack messages are sent as configured.

### Key concepts

#### Offer templates

Automated offers are based on saved offer templates. The template defines:

- Product and pricing structure
- Contract duration
- Payment terms
- EULA

Trigger data (Buyer account ID, amount, product selection) is merged into the template at creation time.

#### Automation modes

| Mode      | Behavior                                                                |
| --------- | ----------------------------------------------------------------------- |
| Draft     | Offer is created but held for manual review before sending to the Buyer |
| Auto-send | Offer is created and sent to the Buyer immediately                      |

Use Draft mode during initial setup to validate that offers are being created correctly.

#### Conditions and filters

Rules can include conditions that limit when they fire:

- **Amount threshold** - Only trigger for deals above a minimum value
- **Product filter** - Only trigger for specific products
- **Buyer segment** - Only trigger for Buyers in specific governance groups

### Benefits

- **Speed** - Offers are created within seconds of trigger events
- **Consistency** - Every offer follows the same template and pricing structure
- **Scale** - Handle high-volume BWA requests without manual bottlenecks
- **Auditability** - Full execution log of every automated action

### Limitations

- Automated offers cannot override governance policies. If governance requires approval, the automation waits.
- Template changes do not retroactively affect previously created offers.
- Auto-send mode should only be used with validated templates to avoid incorrect offers reaching Buyers.

### Related topics

- Private offer automation
- Creating offers
- Governance: Policies

## Governance and approval workflows

Governance in AWS Marketplace Storefront provides a framework for controlling how procurement requests are evaluated, approved, and processed. It allows you to define rules that balance Buyer autonomy with organizational spending controls.

### Governance components

| Component | Purpose                                                  |
| --------- | -------------------------------------------------------- |
| Groups    | Organize Buyers into sets with shared procurement rules  |
| Policies  | Define approval thresholds and routing logic             |
| Segments  | Control which products are visible to which Buyer groups |
| Users     | Manage individual Buyer access and group membership      |

### How the approval workflow operates

```
Buyer submits BWA request
        |
        v
System identifies Buyer's group
        |
        v
System retrieves group's policy
        |
        v
Request amount vs. policy threshold?
        |
   +---------+---------+
   |                   |
Below threshold    Above threshold
   |                   |
   v                   v
Auto-approve      Route to approver
   |                   |
   v                   v
Offer created      Approver reviews
                       |
                  +----+----+
                  |         |
               Approve   Decline
                  |         |
                  v         v
            Offer created  Buyer notified
```

### Configuration levels

Governance operates at the **storefront level**. Each storefront has its own governance configuration, allowing different storefronts to serve different Buyer communities with different rules.

#### Default behavior (no governance configured)

When no groups or policies are configured:

- All BWA requests are sent directly to the Seller team for manual processing
- No auto-approval
- All products visible to all Buyers

#### With governance configured

- Buyers are assigned to groups
- Groups have assigned policies with thresholds
- Requests are auto-approved or routed based on policy rules
- Products can be segmented by group

### Best practices

- **Start simple** - Create one default policy with a single threshold before adding complexity.
- **Use draft mode for automation** - When combining governance with automated offers, use draft mode until you validate the workflow.
- **Monitor approval times** - If manual approvals take too long, consider raising auto-approval thresholds.
- **Communicate with Buyers** - Inform Buyers about approval requirements and expected timelines.

### Related topics

- Groups and auto-approval
- Policies
- Segments
- [Automated offers](#automated-offers "#automated-offers")
- Configuring Buy With AWS
