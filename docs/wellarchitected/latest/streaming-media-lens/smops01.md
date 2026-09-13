

# Organization
<a name="smops01"></a>

Streaming workflows cross multiple teams (encoding, delivery, client, and operations) and require clear ownership at each stage.


| SMOPS01: How does your organization support streaming media outcomes? | 
| --- | 
| [SMOPS01-BP01 Assess trade-offs between streaming architecture options and associated risks](smops01-bp01.md) | 
| [SMOPS01-BP02 Create RACI matrices for streaming video operations](smops01-bp02.md) | 

## Capability intent
<a name="smops01-intent"></a>
+ Architecture decisions are made with explicit understanding of trade-offs across quality, cost, latency, and reliability.
+ Responsibilities for each workflow stage are documented and assigned.
+ Decision-making processes account for the cross-team nature of streaming delivery.

## Maturity levels
<a name="smops01-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | Ownership of streaming workflow stages is informal. Trade-off decisions happen one-time with no documented rationale. | 
| 2 | Emerging | Some ownership is assigned per team, but cross-team decisions still lack a consistent process. | 
| 3 | Defined | RACI matrices exist for all workflow stages. Trade-off decisions follow a documented process with stakeholder input. | 
| 4 | Proactive | Cross-team governance reviews architecture decisions regularly and adjusts ownership as the system evolves. | 
| 5 | Optimized | Decision-making processes are continuously refined based on incident retrospectives and delivery outcomes. | 

## Common issues to watch for
<a name="smops01-issues"></a>
+ No documented ownership for decisions that span encoding, delivery, and client teams.
+ Architecture trade-offs made implicitly without stakeholder awareness.
+ Operational gaps between teams that surface only during incidents.