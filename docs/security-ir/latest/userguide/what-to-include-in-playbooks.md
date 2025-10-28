# What to include in playbooks

Playbooks should contain technical steps for a security analyst to complete
in order to adequately investigate and respond to a potential security incident.

Items to include in a playbook include:

- **Playbook overview** – What risk or incident scenario
  does this playbook address? What is the goal of the playbook?
- **Prerequisites** – What logs and detection mechanisms
  are required for this incident scenario? What is the expected notification?
- **Stakeholder information** – Who is involved and
  what is their contact information? What are each of the stakeholders’
  responsibilities?
- **Response steps** – Across phases of incident
  response, what tactical steps should be taken? What queries should an analyst run?
  What code should be run to achieve the desired outcome?
  - **Detect** – How will the incident be detected?
  - **Analyze** – How will the scope of impact be
    determined?
  - **Contain** – How will the incident be isolated
    to limit scope?
  - **Eradicate** – How will the threat be removed
    from the environment?
  - **Recover** – How will the affected system or
    resource be brought back into production?

- **Expected outcomes** – After queries and code are
  run, what is the expected result of the playbook?

To verify consistent information in each playbook, it can be helpful to create a playbook
template to use across your other security playbooks. Some of the previously listed items,
such as stakeholder information, can be shared across multiple playbooks. If that is the
case, you can create centralized documentation for that information and reference it in
the playbook, then enumerate the explicit differences in the playbook. This will prevent
you from having to update the same information in all of your individual playbooks. Through
creating a template and identifying common or shared information in playbooks, you can
simplify and speed up playbook development. Lastly, your playbooks will likely evolve
over time; once you have confirmed that the steps are consistent, this forms the
requirements for automation.
