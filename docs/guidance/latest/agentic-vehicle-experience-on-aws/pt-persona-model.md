

# Persona model
<a name="pt-persona-model"></a>

## Primary persona: the Customer
<a name="pt-primary-persona"></a>

The primary persona is the Customer — the person at the other end of the voice call, chat message, or mobile interaction. Rather than a single undifferentiated customer type, AVX recognizes four operating contexts in which a customer interacts with a vehicle or a prospective vehicle:


| Operating context | Relationship to the vehicle | Typical concern | 
| --- | --- | --- | 
| OEM owner | Owns or leases the vehicle through a brand relationship; registered in the OEM’s customer identity platform. | Check-engine-light interpretation, recall resolution, warranty service scheduling, vehicle lifecycle management. | 
| Rental customer | Has temporary use of a vehicle through a rental or subscription arrangement. | In-trip warnings (tire pressure, charging alerts), roadside assistance routing, quick resolution that lets them continue their journey. | 
| Fleet driver | Operates a company-owned or leased vehicle as part of a fleet under a commercial operator. | Vehicle health monitoring, DTC-to-action triage, service scheduling within fleet SLA constraints, escalation to fleet operations. | 
| Anonymous / session-scoped visitor | No existing relationship to the vehicle or the OEM yet; browsing the OEM’s own website or app pre-purchase. No Cognito authentication precondition — identity is an ephemeral session identifier only, promoted to a durable lead/reservation record only if the visitor saves a configuration, requests a callback, or authenticates. | Feature and pricing questions, inventory and offer browsing, lead capture. See [Stage 1 — Discover / Find](discover-find.md) for the full session-bootstrap and identity-promotion pattern. | 

The anonymous / session-scoped visitor context differs from the other three in one structural way: it has no verifiable identity claim to resolve persona from, because none exists yet. The other three contexts are resolved server-side from Cognito claims at session start, per the inference rule in [Server-side persona inference](pt-persona-inference.md); the anonymous visitor context has no such claim to resolve, and the agent operates entirely on session-scoped state until (and unless) the visitor is promoted to one of the other three contexts through account creation or a completed acquisition.

These contexts shape which tenant configuration is loaded, which grounding data is available, and which specialist agents may be invoked. The six named personas ([The six named personas](#pt-six-personas)) are the concrete expressions of these contexts plus the service-side roles that support them.

## Secondary persona: the tier-2 human agent
<a name="pt-secondary-persona"></a>

When an AVX session exceeds autonomous resolution scope — because of a P0 safety classification, a low-confidence triage, a customer request for a human, or a policy-defined escalation rule — it hands off to a tier-2 human agent in Amazon Connect. This agent is the secondary persona.

The tier-2 agent receives the context with the chat: the triage classification and its reason, the VIN and vehicle, the driver, and a conversation summary, in the contact attributes and the chat’s first message. The tier-2 agent never starts from zero.

The mechanics of the Connect handoff are covered in [Contact Center Integration](contact-center-integration.md).

## The six named personas
<a name="pt-six-personas"></a>

AVX defines six named interaction personas. Each persona represents a distinct role, operating context, and information need. Grounding surfaces (which ADP data products are loaded into AgentCore Memory and which Knowledge Base source categories are available) are described in [Knowledge and Grounding](knowledge-and-grounding.md).

 `fleet_driver`   
A driver operating a commercial fleet vehicle. This is the default persona — when persona inference cannot determine a more specific role from available identity claims, the system falls back to `fleet_driver`. The persona frames the agent as a vehicle-health and operations assistant: DTC-to-action triage, service scheduling within fleet SLA constraints, recall awareness, and routing between self-service and shop-based resolution.  
The fleet driver persona is fully functional and has comprehensive tool coverage, evaluation harnesses, and tested escalation paths.

 `fleet_owner`   
A fleet manager or operator responsible for multiple vehicles across a commercial fleet. The agent frames itself as a fleet-operations assistant: rolled-up coverage exposure across the fleet, predictive analytics (tire wear trends, brake condition degradation), upcoming maintenance window planning scoped to fleet SLA constraints, and cohort-level recalls and warranty insights.  
The fleet owner persona is fully functional and provides fleet-level data aggregation features. The persona receives Findings that are aggregated across 20–100 vehicles (tenant-configured) rather than single-vehicle DTC cards. Interactions are typically asynchronous (scheduled check-in reports, compliance dashboards) rather than reactive call-in triage.  
Grounding for fleet\_owner includes: ADP Vehicle Lifecycle summarized over the fleet cohort, ADP predictive signals (tire health scores, EV battery degradation curves) aggregated by cohort, CMS service history summarized by service type and vehicle group, and fleet-specific policies loaded from the ADP Fleet SLA Knowledge Base source category.

 `consumer`   
A rental customer or short-term vehicle user. The agent acts as a concierge for in-trip events: understanding in-vehicle warnings, locating charging stops or service centers, opening a support ticket, and escalating to roadside when warranted. Tone is warm and jargon-free; this persona prioritizes resolution speed over technical depth.  
The consumer persona is available and provides support for rental customers and short-term users. The underlying persona definition, grounding bindings, and tool coverage are fully implemented.

 `retail_advisor`   
A dealer-network sales or service advisor interacting with a customer at point of contact. The agent acts as a co-pilot: surfacing customer history, vehicle configuration, pending follow-up items, and relevant brand policies to support a high-quality advisor-customer interaction.  
The retail advisor persona is available and provides sales and service advisor support. The persona definition, grounding bindings, and dealer-network integration capabilities are fully implemented.

 `vehicle_owner`   
A private owner of a specific vehicle registered through an OEM identity platform. The agent provides ownership-oriented answers: service history, OTA campaign status, recall lookup scoped to the specific VIN, and lifecycle events. Grounding is focused on the owner’s own vehicle data rather than fleet-wide or reference content.  
The vehicle owner persona is available and provides OEM customer support for individual vehicle owners. The agent delivers ownership-oriented answers scoped to the owner’s specific vehicle data and lifecycle.

 `service_advisor`   
A service-center employee reviewing an inbound vehicle before drop-off or during in-bay diagnostic work. The agent surfaces relevant Technical Service Bulletins (TSBs), recall bulletins, service policies, and the vehicle’s prior interaction and service history so the advisor can deliver an informed, efficient check-in. This persona uses mixed grounding: Knowledge Base for reference content and AgentCore Memory for vehicle- and customer-specific history. See [Knowledge and Grounding](knowledge-and-grounding.md) for the distinction.

 `technician`   
A certified technician executing a repair. The agent is a repair-procedure co-pilot: DTC diagnostic guides, repair procedures, part-number lookups, parts supersessions, and prior service-record notes for the specific VIN. This persona is Knowledge-Base-heavy — the `knowledge()` and `parts_lookup()` tools are called before consulting vehicle history. See [Knowledge and Grounding](knowledge-and-grounding.md) for the grounding detail.

**Note**  
 `service_advisor` and `technician` are fully functional personas — their grounding definitions, tool factories, and system prompts are fully implemented. End-to-end integration testing through the Connect channel is complete and available for service-center deployments.