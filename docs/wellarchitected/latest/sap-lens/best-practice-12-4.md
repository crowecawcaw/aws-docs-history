# Best Practice 12.4 – Conduct periodic

tests to validate your recovery procedure

Periodically test recovery from critical failure scenarios to prove that software and
procedures result in a predictable outcome, and to validate the state and health of the
backup files. You should evaluate any change to architecture, software, or support
personnel to determine if additional testing is necessary.

**Suggestion 12.4.1 – Identify the failure scenarios for recovery
testing**

You should define the failure scenarios in which a recovery would be required based
on [Reliability]: [Suggestion 10.3.2 – Determine in
which failure scenarios a recovery from backup would be necessary](best-practice-10-3.md "best-practice-10-3.md") and decide the
appropriate level of testing required to validate the process and tooling.

**Suggestion 12.4.2 – Determine the impact of a system change on your
recovery approach**

Define an approach for evaluating the impact of a change and the subsequent recovery
testing required to ensure it does not invalidate your approach. Examples of the types of
change that could impact your workload recovery include software upgrades, patches and
parameter changes.

A recovery test should also be planned in the event of a significant change in the
operating model used to support your SAP environments, for example, a change in Managed
Service Partner or key personnel.

**Suggestion 12.4.3 – Define a recovery test plan**

You should have a complete set of tests defined to simulate the critical failure
scenarios that would result in the need for a recovery. Recovery testing should be planned
for during initial implementation and subsequently on a periodic basis or when required.

- SAP Lens [Operational Excellence]: [Best
  Practice 4.3 - Regularly test business continuity plans and fault recovery](best-practice-4-3.md "best-practice-4-3.md").
