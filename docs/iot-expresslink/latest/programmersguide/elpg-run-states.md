# 3 Run states

An ExpressLink module operates as a state machine that moves through a number
of internal states. See figure below for details.

![Figure 2 - ExpressLink internal states diagram (partial)](images/internal-states.png)

Figure 2 - ExpressLink internal states diagram (partial)

 

The application or host processor is presented with a small command set that is
independent from the connectivity solution offered by the specific module
(such as ethernet, cellular, and Wi-Fi).

The serial interface is designed to be stateless, with all interactions initiated
exclusively from the host side. When an asynchronous event occurs (a message is received
or an internal error condition occurs), the ExpressLink module queues the event and
flags its availability to the host via the Event pin. A host can choose to ignore the
Event pin (to conserve I/Os) and instead poll the module periodically. (See [8.2 Event handling commands](elpg-event-handling.md#elpg-event-handling-commands "elpg-event-handling.md#elpg-event-handling-commands").)
