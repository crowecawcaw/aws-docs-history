

# Provide agent coaching in Connect Customer
<a name="provide-coaching"></a>

Connect Customer provides integrated coaching tools that help supervisors deliver structured, data-driven feedback to agents based on performance evaluations. For upcoming one-on-one sessions with agents, supervisors can share detailed coaching feedback with concrete examples, and set performance goals directly within Connect Customer. Quality management teams can also assign coaching to supervisors with due dates when they identify improvement opportunities, such as showing greater empathy towards customer issues. After coaching is completed, agents can acknowledge the feedback in Connect Customer, making sure that they understand next steps for improvement. Past coaching feedback is centrally accessible, making it easier for agents, supervisors, and quality managers to track agent progress over time.

**Note**  
This feature is available as part of Connect Customer performance evaluations.

## Assign permissions for coaching
<a name="coaching-permissions"></a>

Permissions can be configured as follows:

1. **Admins and quality managers**: Provide **coaching – manage coaching sessions** permissions. These permissions grant them access to all coaching sessions in your Connect Customer instance. With this permission, they can assign agent coaching to agents' supervisors.

1. **Supervisors**: Provide **coaching – my coaching sessions** (View, Create, Delete, Edit) permissions. These permissions enable them to create and manage agent coaching with themselves as the coach.

1. **Agents**: Provide **coaching – my coaching sessions – View** permission. This permission enables the agent to view and acknowledge coaching where they are the participant.

In addition, admins, quality managers and supervisors can be granted **Contact Search - View** and **Evaluation forms - perform evaluations - View** permissions. With these permissions enabled, users will see automated suggestions of evaluations to coach on, based on the selected coaching topic.

For more information, see [Assign security profile permissions for performance evaluations and coaching](evaluation-and-coaching-permissions.md).

## Provide coaching to agents
<a name="coaching-provide-to-agents"></a>

You can start coaching in two ways:
+ **Coach based on aggregated performance insights**: If you already know topics to coach on by reviewing average evaluation scores within the [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md), you can navigate to the coaching sessions page, create a new coaching session, and select the corresponding evaluation criteria as a topic. You will then receive automated suggestions of evaluations to coach on, which you can use to draft detailed feedback.
+ **Coach on individual evaluations**: While reviewing an evaluation on the Contact Details page, you can start a coaching session to provide detailed feedback based on that specific evaluation. You can link multiple evaluations to a coaching session.

### Coach based on aggregated performance insights
<a name="coaching-aggregated-performance"></a>

For example, if you notice in your [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md) that an agent has been scoring low on empathy, you can navigate to the coaching sessions page and create a new coaching session to address that trend.

1. Log in to Connect Customer with a security profile that has required [permissions](#coaching-permissions) to create coaching, search for contacts and view evaluations.

1. Navigate to **Analytics and Optimization** > **Coaching sessions**.

1. When creating a new coaching session, first select a participant.

1. Add scored evaluation forms as session topics. For example, select the evaluation form, section, or question that contains the empathy criteria the agent scored low on. Suggestions are based on these evaluation forms.  
![Adding a scored evaluation form as a coaching session topic.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-add-scored-topic.png)

1. Connect Customer automatically suggests evaluations for this participant. You can choose to add suggestions as strengths or opportunities.  
![Automated evaluation suggestions shown as strengths or opportunities.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-evaluation-suggestions.png)

1. Select **Show strength suggestions** or **Show opportunity suggestions** to view more suggestions, or filter suggestions based on different criteria, such as score range, date range, or certain topics.  
![Filtering evaluation suggestions by score range, date range, or topic.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-filter-evaluation-suggestions.png)

1. You can edit the coaching session by specifying dates, times, and location, providing detailed feedback, and setting improvement goals on coaching topics.  
![The edit coaching session page with fields for dates, times, location, feedback, and goals.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-edit-coaching-session.png)
**Note**  
**Session due date** is mandatory.

1. Choose **Submit** to save the coaching session as a draft.

1. When the coaching session is ready, choose **Share** to make the coaching session visible to the agent. If the agent has an email configured within Connect Customer (or has a secondary email for a SAML instance), they will receive an email notification with a link to view the coaching session.

1. At the time of coaching, you can access the coaching session on **Analytics and Optimization** > **Coaching sessions**. This page displays all past and upcoming coaching sessions.

1. After the coaching session is finished, choose **Mark as Complete** and optionally add a note.

1. Agents can acknowledge the coaching along with their own coaching notes.

### Coach on individual evaluations
<a name="coaching-individual-evaluations"></a>

1. Log in to Connect Customer with a security profile that has required [permissions](#coaching-permissions) to create coaching, search for contacts and view evaluations.

1. Select **Analytics and Optimization** > **Contact search** from the navigation bar on the left.

1. From **Contact Search**, find contacts that have been evaluated for the agent that you want to coach. For example, you can find contacts where the evaluation score is less than 70%:  
![The Contact Search page with an evaluation score filter applied.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contact-search-evaluation-score-filter.png)

1. Open a contact that has been evaluated, and view the evaluations on the right pane.

1. Open an evaluation and choose **Coach on this evaluation**.  
![The Coach on this evaluation button on an evaluation.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-coach-on-this-evaluation-button.png)

1. You can add the entire evaluation, a specific section or question to a coaching session:  
![Adding evaluation items to a coaching session.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-add-evaluation-items.png)

1. You can link the evaluation, its sections or questions to an existing coaching session, or create a new session. Items can be linked as strength or growth opportunities.  
![The dialog for adding a question to a coaching session.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-add-question-to-coaching-dialog.png)

1. After you add an evaluation or its items for coaching, a link will be provided to view the coaching session.

1. You can link up to 10 evaluations or evaluation items to a single coaching session as examples of agent strength or growth opportunities. To link additional evaluations, repeat steps 2 through 7

1. You can edit the coaching session by specifying dates, times, and location, providing detailed feedback, and setting improvement goals on coaching topics.  
![The edit coaching session page with fields for dates, times, location, feedback, and goals.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-edit-coaching-session.png)
**Note**  
**Session due date** is mandatory.

1. Choose **Submit** to save the coaching session as a draft.

1. When the coaching session is ready, choose **Share** to make the coaching session visible to the agent. If the agent has an email configured within Connect Customer (or has a secondary email for a SAML instance), they will receive an email notification with a link to view the coaching session.

1. At the time of coaching, you can access the coaching session on **Analytics and Optimization** > **Coaching sessions**. This page displays all past and upcoming coaching sessions.

1. After the coaching session is finished, choose **Mark as Complete** and optionally add a note.

1. Agents can acknowledge the coaching along with their own coaching notes.

## Search for coaching sessions
<a name="coaching-search-sessions"></a>

You can view all past and upcoming coaching sessions from the **Analytics and Optimization** > **Coaching sessions** page.

This page provides advanced search capabilities. You can search for coaching sessions:
+ Performed by a particular coach
+ Where a specific agent was the participant
+ Created by a specific quality manager
+ On a specific topic
+ That are past due date but not completed
+ That are pending completion (shared or draft status)
+ That are completed, but not yet acknowledged by the participant
+ And more

![The coaching sessions search page with filter options.](http://docs.aws.amazon.com/connect/latest/adminguide/images/coaching-search-filters.png)
