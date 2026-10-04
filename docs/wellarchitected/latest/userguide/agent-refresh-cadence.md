

AWS Well-Architected Agent is in preview release and is subject to change.

# Recommendation refresh and data freshness
<a name="agent-refresh-cadence"></a>

AWS WA Agent keeps recommendations current through scheduled refresh cycles:
+ **Scheduled refresh:** Resource and application recommendations are refreshed automatically on a weekly cadence after the initial set of recommendations is generated. You do not need to trigger this manually.
+ **Cooldown periods:** Scheduled recommendation generation runs on a weekly cycle for the same profile. You cannot trigger resource or application recommendations on demand.

**Note**  
Architecture recommendations are not part of the scheduled refresh cycle. They are generated on demand through architecture reviews. For more information, see [Conducting architecture reviews](agent-architecture-reviews.md).

**Staleness detection:** Recommendation timestamps are updated during each refresh cycle, even when the recommendation content does not change. A recommendation without a recent timestamp update may no longer be relevant to your current environment.

**Infrastructure changes:** Changes to your environment (new resources, modified configurations) are picked up during the next scheduled refresh cycle. Recommendations are re-evaluated against the current state of your infrastructure at each refresh.