End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Maximum duration of a simulation

Each simulation in AWS SimSpace Weaver has a _maximum duration_ setting
that specifies the maximum time that the simulation can run. You provide the maximum
duration as a parameter when you start a simulation. The
[`StartSimulation`
application programming interface (API)](../APIReference/API_StartSimulation.md "../APIReference/API_StartSimulation.md") has an optional parameter `MaximumDuration`.
The value of the parameter is a number of minutes (m or M), hours (h or H),
or days (d or D). For example, `1h` or `1H` means 1 hour.
SimSpace Weaver stops your simulation when it reaches this limit.

## Maximum value

The highest valid value for `MaximumDuration` is
`14D`, or its equivalent in hours
(`336H`) or minutes
(`20160M`).

## Default value

The `MaximumDuration` parameter is optional. If
you don't provide a value, SimSpace Weaver uses a value of `14D`.

## Minimum value

The lowest valid value for `MaximumDuration` is
a value that is numerically equivalent to `0`. For example,
the values `0M`, `0H`, and `0D`, are all
numerically equivalent to `0`.

If you provide the minimum value for maximum duration, your simulation immediately
transitions to the `STOPPING` state as soon as it reaches the
`STARTED` state.

## Starting a simulation using the console

You can provide a value for the **Maximum duration**
when you start a simulation in the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver"). Enter the
value in the **Maximum duration** field of the
**Simulation settings** form when you choose
**Start simulation**.

###### Important

If you don't provide a value for **Maximum duration**, SimSpace Weaver
uses the [default value](#working-with_max-duration_default-value "#working-with_max-duration_default-value")
(`14D`).

## The status of a simulation that reaches its maximum duration

When SimSpace Weaver automatically stops a simulation that reaches its
maximum duration, the **status** of the simulation
is `STOPPING` (if in progress) or `STOPPED`.
In the [SimSpace Weaver console](https://console.aws.amazon.com/simspaceweaver "https://console.aws.amazon.com/simspaceweaver"), the **target status**
of the simulation is still `STARTED`, because that was the last state requested
by a user.
