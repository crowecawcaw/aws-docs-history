# Assign security profile permissions for

users to create and access evaluation forms

To allow users to create, automate, and access evaluation forms, assign the following
**Analytics and optimization** security profile permissions:

- **Evaluation forms - perform evaluations**: Allows a user,
  such as a Quality Assurance team member, to use an evaluation form to review a
  contact. For an example image, see [Evaluate contact center agent performance in Amazon Connect](evaluations.md "evaluations.md").

This permission allows users to [search](search-evaluations.md "search-evaluations.md") evaluations by evaluation form, score, last updated
date/range, evaluator, and status. It also allows them to view the evaluation
form audit trail.

    + **View** permissions enable users to view submitted
     evaluations. You can grant this permissions to users who perform
     evaluations (such as managers) and users (such as agents) who need to
     view evaluations.
    + **Create** permissions enable users to create new
     evaluations, view and edit draft evaluations.
    + **Edit** permissions enable users to edit submitted
     evaluations.
    + **Delete** permissions enable users to delete both
     draft and submitted evaluations.

- **Evaluation forms - manage form definitions**: Allows admins
  and managers to [create](create-evaluation-forms.md "create-evaluation-forms.md") and [manage](evaluationform-audit-trail.md "evaluationform-audit-trail.md") evaluation forms.
- **Rules**: Permissions to create, view, edit, and delete
  rules are required to [automatically categorize
  contacts](rules.md "rules.md") based on certain agent behaviors and customer outcomes.
  These contact categories can be used to [configure
  automation](create-evaluation-forms.md#step-automate "create-evaluation-forms.md#step-automate") on evaluation forms. In addition, rules permissions are
  needed to [create
  a rule to submit automated evaluations](contact-lens-rules-submit-automated-evaluation.md "contact-lens-rules-submit-automated-evaluation.md").
- **Evaluation forms - ask AI assistant**: Provides access to
  the **Ask AI** button while performing evaluations. The
  **Ask AI** button enables the user to get [generative AI-powered
  recommendations](generative-ai-performance-evaluations.md "generative-ai-performance-evaluations.md") for answers to questions in evaluation forms.
- **Evaluation forms - manage calibration sessions**: Allows
  admins to create and manage calibration sessions to drive consistency and
  accuracy in how managers evaluate agent performance.
  The **Admin** security profile has these permissions by default.

For information about how to add more permissions to an existing security profile,
see [Update security profiles in Amazon Connect](update-security-profiles.md "update-security-profiles.md").
