# Timers in Amazon SWF

With a timer, you can notify your decider when a certain amount of time has elapsed.

When responding to a
decision task, the decider has the option to respond with a `StartTimer` decision. This decision
specifies an amount of time after which the timer should fire. After the specified time has elapsed, Amazon SWF will add
a `TimerFired` event to the workflow execution history and schedule a decision task. The decider can then
use this information to inform further decisions. One common application for a timer is to delay the execution of an
activity task. For example, a customer might want to take delayed delivery of an item.
