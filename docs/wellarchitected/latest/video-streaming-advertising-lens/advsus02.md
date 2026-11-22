

# Bid stream efficiency

 Waste accumulates on both legs of the bid stream. Some inbound requests a bidder can never act on, some outbound requests a seller should never have sent, most responses carry no bid at all, and every message on the path tends to carry fields and connection overhead that no counterparty needs. Most bid requests never convert to wins: mismatched targeting, depleted budgets, and unsuitable inventory mean these requests consume compute, memory, and network resources without generating value. Each processed request requires energy to power the infrastructure with no environmental return. 


|  ADVSUS02: How do you reduce bid stream resources, from inbound intake to outbound response, on traffic with no advertising value?  | 
| --- | 
| [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) | 
| [ADVSUS02-BP02 Apply rate limiting to control inbound request volume per partner](advsus02-bp02.md) | 
| [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) | 
| [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md) | 
| [ADVSUS02-BP05 Minimize bid response payload sizes](advsus02-bp05.md) | 
| [ADVSUS02-BP06 Reduce per-auction network overhead by consolidating bid request fan-out and reusing transport connections](advsus02-bp06.md) | 

## Capability intent
<a name="advsus02-capability-intent"></a>
+  Bid requests that can't convert (malformed, unsupported, economically incompatible, or in excess of agreed volume) are rejected in the network path before they consume bidder compute. 
+  Compute and the energy behind it are reserved for requests with a genuine chance of producing a bid, lowering the carbon intensity of each useful response. 
+  Inbound demand from each advertising partner is bounded to agreed queries-per-second limits, keeping aggregate load within deliberately provisioned, right-sized capacity. 
+  Rejection rates and per-partner request volume are observable and attributable, feeding continuous refinement of filters and limits. 
+  Filter and rate-limit rules evolve from real no-bid and traffic analysis rather than being set once and left to drift. 
+  Senders shape their own outbound traffic, suppressing requests with a low predicted probability of a bid before transmission commits network and downstream compute. 
+  Responders reduce and cheaply absorb the no-bid responses that remain, and work with supply partners to suppress traffic they cannot act on at its source. 
+  Every message on the bid path carries only the fields its counterparty consumes, and connections are reused rather than re-established per request. 

## Common issues to watch for
<a name="advsus02-common-issues-to-watch-for"></a>
+  Admitting every inbound request into application compute and deciding to no-bid only after deserialization and business-logic evaluation. 
+  Relying solely on automatic scaling to absorb partner spikes, which drives unplanned capacity and energy growth. 
+  Applying coarse or single global rules, such as source IP or one shared limit, instead of structural OpenRTB validation and per-partner caps. 
+  Setting filter rules and rate limits once and never revisiting them as traffic patterns, partners, and floor prices drift. 
+  Treating rejected-request volume as an operational afterthought, with no visibility into how much traffic is filtered, by whom, or why. 