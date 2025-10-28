After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# .z namespace override

KX uses the `.z` namespace that contains environment variables and
functions, and hooks for callbacks. A FinSpace Managed kdb Insights cluster doesn't
support direct assignment for `.z` namespace callbacks because of
security concerns. For example, the system denies access to the following direct
`.z.ts` assignment.

```
q)con".z.ts:{[x]}" / con is the hopen filehandle
'access
[0]  con".z.ts:{[x]}"
```

Because some of the assignments for `.z` namespace callbacks are
critical for business logic, FinSpace provides a reserved namespace
`.awscust.z` for you to override functions within the
`.z` namespace.

By overriding the functions within the new `.awscust.z` namespace,
you can achieve the same effect as if you were directly overriding allowlisted
`.z` functions.

For example, if you need to override the `.z.ts` function, you can
set a value for `.awscust.z.ts`. The FinSpace Managed kdb cluster invokes
the `.awscust.z.ts` function whenever you invoke the `.z.ts`
function, which provides a safety wrapper.

The following list shows the allowlisted callbacks for the
`.awscust.z` namespace.

```
.awscust.z.ts
.awscust.z.pg
.awscust.z.ps
.awscust.z.po
.awscust.z.pc
.awscust.z.ws
.awscust.z.wo
.awscust.z.wc
.awscust.z.pd
.awscust.z.ph
.awscust.z.pi:
.awscust.z.exit
```

If you override `.z` callbacks that aren't on the preceding list,
you won't have any effects on the `.z` namespace callbacks.
