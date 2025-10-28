# Maintaining a Neptune Analytics graph

Periodically, Neptune Analytics performs maintenance on Neptune resources. Maintenance most often involves updates to the
following resources in your graph:

- Underlying hardware
- Underlying operating system (OS)
- Graph engine version

Neptune Analytics doesn't have a maintenance window for the graphs. It automatically performs maintenance operations which
require the Neptune service to take your graph offline for a short time, normally on the order of 10s of seconds.
Maintenance items require a resource to be offline during the maintenance period, however Neptune Analytics will make a best
effort attempt to provide request queuing during this time. Required patching is automatically scheduled for patches
related to security, instance reliability, engine upgrades, and other items as required. Such patching occurs
infrequently, typically one to two times every month but may occur as needed. There are no actions required from you
for this to take place.
