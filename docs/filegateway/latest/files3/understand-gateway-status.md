# Understanding gateway status

Each gateway in your AWS Storage Gateway deployment has an associated status that tells you at
a glance what the health of the gateway is. Most of the time, the status indicates that
the gateway is functioning normally and that no action is needed on your part. In some
cases, the status indicates a problem that might or might not require action on your
part.

You can see the status for each gateway in your deployment on the
**Gateways** page of the Storage Gateway console. The gateway status
appears in the **Status** column next to the name of the gateway. A
gateway that is functioning normally has a status of `RUNNING`.

In the following table, you can find a description of each gateway status, and whether
you should act based on the status. A gateway should have `RUNNING` status
all or most of the time it's in use.

| Status    | Meaning                                                                                                                                                                                                                                                                                                                |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `RUNNING` | The gateway is configured properly and is available to use.                                                                                                                                                                                                                                                            |
| `OFFLINE` | Your gateway might be in an `OFFLINE` status for one or<br>more of the following reasons:<br>• The gateway can't reach the Storage Gateway service<br>endpoints.<br>• The gateway had an unexpected shutdown.<br>• The gateway has an associated cache disk that is<br>disconnected, has been modified, or has failed. |
