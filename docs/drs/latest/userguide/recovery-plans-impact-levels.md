# Controlling how server failures affect a plan

Every server in a server step has an impact level that determines whether its failure
stops the plan:

| Impact level               | Effect when the server fails to recover                                                                                                                                                   |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *_Critical_<br>• (default) | The step fails, the execution fails, and the remaining steps do<br>not run. Servers in the same step that already started continue to<br>completion.                                      |
| **Optional**               | The server fails, but the step still completes and the plan<br>continues to the next step. The failed server is reported on the<br>step so that you can see which server did not recover. |

Mark a server **Optional** when your application can
start without it, for example, a reporting server or a secondary worker node. Leave a
server **Critical** when a later tier depends on it.

If a step contains only **Optional** servers and all of
them fail, the step still completes and the plan continues.

###### Note

Impact levels apply only to servers that actually started recovering and then
failed. They do not apply to validation. If a server fails the validation that runs
when the execution starts, the whole execution fails; if a server fails the
revalidation at the start of its step, that whole step fails. Both happen even if
the server is marked **Optional**, because AWS Elastic Disaster Recovery
starts recovery for all of a step's servers in a single request. For more
information, see [Validation that runs
before a server is recovered](recovery-plans-validation.md "recovery-plans-validation.md").
