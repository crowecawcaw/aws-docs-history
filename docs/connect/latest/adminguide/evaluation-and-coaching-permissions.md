

# Assign security profile permissions for performance evaluations and coaching
<a name="evaluation-and-coaching-permissions"></a>

To allow users to create, automate, and access evaluation forms, assign the following **Analytics and optimization** security profile permissions: 
+ **Evaluation forms - manage form definitions**: Allows admins and managers to [create](create-evaluation-forms.md) and [manage](evaluationform-audit-trail.md) evaluation forms.
+ **Evaluation forms - perform contact evaluations**: Allows a user, such as a Quality Assurance team member, to use an evaluation form to review a contact. For an example image, see [Evaluate agent and self-service interaction performance in Connect Customer](evaluations.md). 

  This permission allows users to [search](search-evaluations.md) evaluations by evaluation form, score, last updated date/range, evaluator, and status. It also allows them to view the evaluation form audit trail.
  + **View** permission enables users to view submitted evaluations. This permission enables users to see evaluations on any contacts they have access to (unless [restricted by tag-based access control](https://docs.aws.amazon.com/connect/latest/adminguide/tag-based-access-control-performance-evaluations.html)). You can grant this permission to users who perform evaluations (such as managers). 
  + **Create** permission enables users to create new evaluations, view and edit draft evaluations. 
  + **Edit** permission enables users to edit submitted evaluations.
  + **Delete** permission enables users to delete both draft and submitted evaluations.
+ **Evaluation forms - view my received evaluations**: Allows agents to search for and view completed evaluations that they have received. This does not grant access to evaluations in draft, under review or part of calibrations. Access to an evaluation will be subject to [tag-based access control ](https://docs.aws.amazon.com/connect/latest/adminguide/tag-based-access-control-performance-evaluations.html). 
+ **Rules**: Permissions to create, view, edit, and delete rules are required to [automatically categorize contacts](rules.md) based on certain agent behaviors and customer outcomes. These contact categories can be used to [configure automation](create-evaluation-forms.md#step-automate) on evaluation forms. In addition, rules permissions are needed to [create a rule to submit automated evaluations](contact-lens-rules-submit-automated-evaluation.md).
+ **Evaluation forms - ask AI assistant**: Provides access to the **Ask AI** button while performing evaluations. With the **Ask AI** button, you can get [generative AI-powered recommendations](generative-ai-performance-evaluations.md) for answers to questions in evaluation forms.
+ **Evaluation forms - manage calibration sessions**: Allows admins to create and manage calibration sessions to drive consistency and accuracy in how managers evaluate agent performance.
+ **Sample contacts**: Allows managers to randomly sample agents' contacts for evaluation. For example, a manager can select all agents in his hierarchy, and get 5 random contacts per agent from the last week for evaluation.

To allow users to manage or access coaching sessions, assign the following **Analytics and optimization** security profile permissions: 
+ **Coaching - my coaching sessions**: Access coaching sessions where you are assigned as a coach or a participant.
  + **View**: View coaching sessions where you are the coach or the participant. If you are the participant, you can acknowledge the coaching session with this permission.
  + **Create**: Create new coaching sessions with yourself as the coach.
  + **Edit**: Edit coaching sessions where you are the coach.
  + **Delete**: Delete coaching sessions where you are the coach.
+ **Coaching - manage coaching sessions**: Access coaching sessions performed by yourself or others. This permission is for admins or quality managers.
  + **View**: View any coaching session.
  + **Create**: Create new coaching sessions. You can choose yourself as the coach or assign other users as the coach.
  + **Edit**: Edit any coaching session.
  + **Delete**: Delete any coaching session.
+ **Contact Search - View** and **Evaluation forms - perform evaluations - View** permissions: Receive automated suggestions of evaluations to coach on after selecting a specific evaluation criteria as a coaching topic.

The **Admin** security profile has these permissions by default. 

For information about how to add more permissions to an existing security profile, see [Update security profiles in Connect Customer](update-security-profiles.md).