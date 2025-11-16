# Alarms for practice runs

You can specify two types of CloudWatch alarms for
practice runs in zonal autoshift: outcome alarms and blocking alarms.

**Outcome alarms (required)**

For the first type of alarm, the _outcome alarm_,
at least one alarm is required to be specified. You should configure outcome alarms to monitor
the health of your application when traffic is shifted away from an Availability Zone during each
30-minute practice run.

For a practice run to be effective, specify as outcome alarms at least one CloudWatch alarm that meets
both of the following criteria:

The alarm monitors metrics for the resource, or for your application

AND

The alarm responds with an `ALARM` state
when your application is adversely affected by the loss of one Availability Zone.

For more information, see the **Alarms that you specify for practice runs** section in
[Best practices when you configure zonal autoshift](arc-zonal-autoshift.md "arc-zonal-autoshift.md").

Outcome alarms also provide information for the _practice run outcome_ that ARC reports for
each practice run. If an outcome alarm enters an `ALARM` state, ARC ends the practice run and returns
a practice run outcome of `FAILED`. If the practice run completes the 30 minute
test period and none of the outcome alarms that you've specified enters an `ALARM` state, the outcome
returned is `SUCCEEDED`. A list of all outcome values, with descriptions, is provided in the
[Outcomes for practice runs](arc-zonal-autoshift.md#ZAConsiderationsPracticeRunOutcomes "arc-zonal-autoshift.md#ZAConsiderationsPracticeRunOutcomes") section.

**Blocking alarms (optional)**
Optionally, you can specify a second type of alarm, the _blocking alarm_. Blocking alarms
block practice runs from starting, or continuing, when one or more of the alarms is in an `ALARM` state.
Blocking alarms block practice run traffic shifts from being started—and stop any practice runs in progress—when
at least one of the alarms is in an `ALARM` state.

For example, in a large architecture with multiple microservices, when one microservice is experiencing
a problem, you typically want to stop all other changes in the application environment, which would
including blocking practice runs. You can add a blocking alarm in ARC to accomplish this.
