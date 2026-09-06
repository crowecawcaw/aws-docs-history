

# How zonal autoshift and practice runs work
<a name="arc-zonal-autoshift.how-it-works"></a>

The zonal autoshift capability in Amazon Application Recovery Controller (ARC) allows AWS to shift traffic for a resource away from an Availability Zone, on your behalf, when AWS determines that there's an impairment that could potentially affect customers in the Availability Zone. Zonal autoshift is designed for a resource that is pre-scaled in all Availability Zones in an AWS Region, so that an application can operate normally with the loss of one Availability Zone.

With zonal autoshift, you are required to configure practice runs, where ARC regularly shifts traffic for the resource away from one Availability Zone. ARC schedules practice runs about weekly for each resource that has a practice run configuration associated with it. Practice runs for each resource are scheduled independently.

For each practice run, ARC records an outcome. If a practice run is interrupted by a blocking condition, the practice run outcome is not marked as successful. For more information about practice run outcomes, see [Outcomes for practice runs](arc-zonal-autoshift.considerations.md#ZAConsiderationsPracticeRunOutcomes). 

You can configure Amazon EventBridge notifications to send you information about autoshifts and practice runs. For more information, see [Using zonal autoshift with Amazon EventBridge](eventbridge-zonal-autoshift.md).

**Topics**
+ [About zonal autoshift](arc-zonal-autoshift.how-it-works.about.md)
+ [When AWS starts and stops autoshifts](arc-zonal-autoshift.how-it-works.start-stop-auto.md)
+ [When ARC schedules, starts, and ends practice runs](arc-zonal-autoshift.how-it-works.scheduled-practice-runs.md)
+ [Capacity checks for practice runs](arc-zonal-autoshift.how-it-works.capacity-check.md)
+ [Notification for practice runs and autoshifts](arc-zonal-autoshift.how-it-works.notifications.md)
+ [Precedence for zonal shifts](arc-zonal-autoshift.how-it-works.precedence.md)
+ [Stopping an active autoshift or practice run](arc-zonal-autoshift.how-it-works.stop-shift.md)
+ [How traffic is shifted away](arc-zonal-autoshift.how-it-works.how-traffic-shifted.md)
+ [Alarms for practice runs](arc-zonal-autoshift.how-it-works.alarms.md)
+ [Blocked windows and allowed windows (in UTC)](arc-zonal-autoshift.how-it-works.blocked-windows.md)