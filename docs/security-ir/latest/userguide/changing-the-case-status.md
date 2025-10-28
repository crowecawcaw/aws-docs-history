# Changing the case status

A case will be in one of the following states:

- Submitted: This is the initial status of a case. Cases in this status have been submitted by a requested, but are
  not yet being worked on.
- Detection and Analysis: This status indicates an incident responder has started work on the case. This phase includes
  data gathering, triaging the event, and performing analysis to create data driven conclusions.
- Containment, Eradication and Recovery: In this status the incident responder has identified suspicious activity that
  requires additional effort to remove. The incident responder will provide recommendations to you for business risk
  analysis and additional actions. If you have enabled the opt-in features for the service, then an AWS incident responder
  will seek your consent to perform containment actions with SSM documents in the impacted account(s).
- Post-incident activities: In this status the primary security event has been contained. The focus now is to recover and
  return business operations to normal. A summary and root cause analysis is provided if the resolver for the case is
  AWS-supported.
- Closed: This is the final status of the workflow. Cases in a closed status indicate work has been completed. Closed cases
  cannot be reopened, so ensure all actions are complete before transitioning to this status.

Choose **Action/Update Status**
to change the status of the case for self-managed cases. For
AWS supported cases, the status is set by the AWS CIRT responder.
