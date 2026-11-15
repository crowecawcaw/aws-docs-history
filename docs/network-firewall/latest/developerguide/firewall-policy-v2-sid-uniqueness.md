

# Signature ID uniqueness
<a name="firewall-policy-v2-sid-uniqueness"></a>

A signature ID (SID) must be unique within the scope of the object that contains the rule. There are two such scopes:
+ **Within a rule group** – Every rule in a single firewall or IPS rule group must have a SID that is unique among the rules in that rule group.
+ **Within a policy's embedded rules** – Every rule you author directly in a policy—across both the embedded firewall rules and the embedded IPS rules—must have a SID that is unique among all of that policy's embedded rules.

This applies whether you provide a rule as a raw Suricata-compatible string or as a modeled rule that Network Firewall compiles into one. Network Firewall uses the SID to identify which rule a log record came from, so a duplicate SID within one of these scopes is ambiguous and Network Firewall rejects it when you create or update the rule group or policy.

The scopes are independent of each other. SIDs in a referenced rule group don't collide with the SIDs in your embedded rules or with the SIDs in other referenced rule groups—only with other rules in the same rule group.

**Example Duplicate embedded SID is rejected**  
Suppose you author one embedded firewall rule and one embedded IPS rule in the same policy, and both use `sid:100`. Network Firewall rejects the create or update request because the two embedded rules share a SID. Change one of them to a different SID, for example `sid:101`, to resolve the conflict.