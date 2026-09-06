

# Concepts
<a name="concepts-storefront"></a>

## Automated offers
<a name="automated-offers"></a>

Automated offers allow you to define rules that create private offers automatically based on triggers such as Buyer requests, CRM events, or governance approvals. This reduces manual effort for high-volume operations and ensures consistent offer creation.

### How automated offers work
<a name="automated-offers-how-automated-offers-work"></a>

1. **A trigger occurs** - A Buyer submits a BWA request, a CRM deal reaches a specific stage, or a governance rule approves a request.

1. **The automation rule evaluates** - The system checks whether the event matches the rule's conditions (product, amount threshold, Buyer segment).

1. **An offer is created** - If conditions are met, a private offer is generated using a predefined offer template with auto-populated fields from the trigger data.

1. **Post-creation actions fire** - Notifications, CRM updates, or Slack messages are sent as configured.

### Key concepts
<a name="automated-offers-key-concepts"></a>

#### Offer templates
<a name="automated-offers-offer-templates"></a>

Automated offers are based on saved offer templates. The template defines:
+ Product and pricing structure
+ Contract duration
+ Payment terms
+ EULA

Trigger data (Buyer account ID, amount, product selection) is merged into the template at creation time.

#### Automation modes
<a name="automated-offers-automation-modes"></a>


| Mode | Behavior | 
| --- | --- | 
| Draft | Offer is created but held for manual review before sending to the Buyer | 
| Auto-send | Offer is created and sent to the Buyer immediately | 

Use Draft mode during initial setup to validate that offers are being created correctly.

#### Conditions and filters
<a name="automated-offers-conditions-and-filters"></a>

Rules can include conditions that limit when they fire:
+ **Amount threshold** - Only trigger for deals above a minimum value
+ **Product filter** - Only trigger for specific products
+ **Buyer segment** - Only trigger for Buyers in specific governance groups

### Benefits
<a name="automated-offers-benefits"></a>
+ **Speed** - Offers are created within seconds of trigger events
+ **Consistency** - Every offer follows the same template and pricing structure
+ **Scale** - Handle high-volume BWA requests without manual bottlenecks
+ **Auditability** - Full execution log of every automated action

### Limitations
<a name="automated-offers-limitations"></a>
+ Automated offers cannot override governance policies. If governance requires approval, the automation waits.
+ Template changes do not retroactively affect previously created offers.
+ Auto-send mode should only be used with validated templates to avoid incorrect offers reaching Buyers.

### Related topics
<a name="automated-offers-related-topics"></a>
+ Private offer automation
+ Creating offers
+ Governance: Policies

## Governance and approval workflows
<a name="governance-and-approval-workflows"></a>

Governance in AWS Marketplace Storefront provides a framework for controlling how procurement requests are evaluated, approved, and processed. It allows you to define rules that balance Buyer autonomy with organizational spending controls.

### Governance components
<a name="governance-and-approval-workflows-governance-components"></a>


| Component | Purpose | 
| --- | --- | 
| Groups | Organize Buyers into sets with shared procurement rules | 
| Policies | Define approval thresholds and routing logic | 
| Segments | Control which products are visible to which Buyer groups | 
| Users | Manage individual Buyer access and group membership | 

### How the approval workflow operates
<a name="governance-and-approval-workflows-how-the-approval-workflow-operates"></a>

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
<a name="governance-and-approval-workflows-configuration-levels"></a>

Governance operates at the **storefront level**. Each storefront has its own governance configuration, allowing different storefronts to serve different Buyer communities with different rules.

#### Default behavior (no governance configured)
<a name="governance-and-approval-workflows-default-behavior"></a>

When no groups or policies are configured:
+ All BWA requests are sent directly to the Seller team for manual processing
+ No auto-approval
+ All products visible to all Buyers

#### With governance configured
<a name="governance-and-approval-workflows-with-governance-configured"></a>
+ Buyers are assigned to groups
+ Groups have assigned policies with thresholds
+ Requests are auto-approved or routed based on policy rules
+ Products can be segmented by group

### Best practices
<a name="governance-and-approval-workflows-best-practices"></a>
+ **Start simple** - Create one default policy with a single threshold before adding complexity.
+ **Use draft mode for automation** - When combining governance with automated offers, use draft mode until you validate the workflow.
+ **Monitor approval times** - If manual approvals take too long, consider raising auto-approval thresholds.
+ **Communicate with Buyers** - Inform Buyers about approval requirements and expected timelines.

### Related topics
<a name="governance-and-approval-workflows-related-topics"></a>
+ Groups and auto-approval
+ Policies
+ Segments
+ [Automated offers](#automated-offers)
+ Configuring Buy With AWS