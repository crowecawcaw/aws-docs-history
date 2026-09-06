

# Bidirectional constraints
<a name="protection-plans-runtime-monitoring-constraints"></a>

The Runtime Monitoring sub-features and infrastructure have the following relationships:

Enable a sub-feature  
Automatically enables Runtime Monitoring Infrastructure if it was disabled.

Disable a sub-feature  
No effect on Runtime Monitoring Infrastructure.

Enable Runtime Monitoring Infrastructure  
No effect on sub-features.

Disable Runtime Monitoring Infrastructure  
Disables all sub-features.

For auto-enable settings, the following constraints apply:

Raise a sub-feature's auto-enable  
Runtime Monitoring Infrastructure always equals the maximum of all sub-features.

Lower a sub-feature's auto-enable  
Runtime Monitoring Infrastructure recalculates to the new maximum of all sub-features.

Raise Runtime Monitoring Infrastructure's auto-enable  
No effect on sub-features.

Lower Runtime Monitoring Infrastructure's auto-enable  
Lowers any sub-feature that exceeds the new parent value to match it.

**Note**  
A warning appears when any sub-feature has a different value from Runtime Monitoring Infrastructure (either toggle or auto-enable mismatch). Enabling only Runtime Monitoring Infrastructure puts you in manual mode without auto-management of the security agent. Enable Runtime Monitoring for EKS, ECS, or EC2 to automatically manage the security agent for your workloads.