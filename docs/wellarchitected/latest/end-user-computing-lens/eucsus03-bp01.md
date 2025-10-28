# EUCSUS03-BP01 Adapt your

AppStream 2.0 fleet timeout

Configure timeouts for AppStream 2.0 fleets to minimize unnecessary resource consumption
whilst also factoring in usability. Minimize resource consumption by verifying that
instances are not consuming resources unnecessarily when users are not using them or
unlikely to use them.

Usability is an important consideration when shortening
timeouts. Setting them too low results in sessions being
terminated too early with the risk of impacting user
productivity, whereas setting them too high results in instances
running without any users, which incurs a higher carbon
footprint as well as higher costs.

Strike an appropriate balance in timeout durations to maintain
user productivity while reducing resource consumption in periods
of low usage.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

You can select a session duration to configure a maximum active session for a user,
which defaults to 16 hours. Disconnect timeout and idle disconnect timeout determine when
to log off an existing user session. By default, they are both configured at 15 minutes
each. The default value can be reduced without disrupting the end user experience.

For example, you can set the idle disconnect timeout for five minutes. You can set
timecout configurations in the [fleet console](../../../appstream2/latest/developerguide/set-up-stacks-fleets.md "../../../appstream2/latest/developerguide/set-up-stacks-fleets.md").
