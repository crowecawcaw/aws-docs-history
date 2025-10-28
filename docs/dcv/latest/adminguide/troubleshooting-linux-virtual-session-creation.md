# Troubleshooting Virtual Session Creation on Linux

If connecting to a virtual session results in a `No session available` or `The sessionId
 `session` is not available` error, this is probably due to the fact that the virtual
session creation failed and was terminated.

You can check if the session is present with the `dcv list-sessions` command. See [Viewing Amazon DCV sessions](managing-sessions-lifecycle-view.md "managing-sessions-lifecycle-view.md") for more information about inspecting running sessions. If the session
is not present in the list, then it might have failed.

###### Topics

- [Investigating Virtual Session Creation Failure on Linux](investigating-linux-virtual-session-creation-failure.md "investigating-linux-virtual-session-creation-failure.md")
- [Creating a Failsafe Virtual Session on Linux](creating-linux-failsafe-virtual-session-creation.md "creating-linux-failsafe-virtual-session-creation.md")
