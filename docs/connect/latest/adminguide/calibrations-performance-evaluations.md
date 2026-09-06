

# Calibration sessions for performance evaluations
<a name="calibrations-performance-evaluations"></a>

With Connect Customer conversational analytics, you can conduct calibration sessions to drive consistency and accuracy in how managers evaluate agent performance, so that agents receive feedback that is consistent. During a calibration, multiple managers can evaluate the same contact using the same evaluation form. You can then review differences in evaluations filled by different managers to align managers on evaluation best practices and identify opportunities to improve the evaluation form, for example, rephrasing an evaluation question to be more specific, so that it is consistently answered by managers. You can also compare manager's answers with a designated expert, to measure and improve manager accuracy on evaluating agent performance. The expert is usually the quality manager who is conducting the calibration session.

## Permissions needed for calibrations
<a name="calibrations-performance-evaluations-permissions"></a>

You need the following permissions for calibrations:
+ **Creating calibration sessions:** Add the permission **Evaluation forms - manage calibration sessions** to the security profiles of the set of users that should be permitted to conduct calibration sessions for performance evaluations.
+ **Participating in a calibration session:** Any user who has the permission to perform evaluations, namely **Evaluation forms - perform evaluations**, can participate in a calibration session if they are added as one of the participants.

In addition, for both sets of users, you also need permissions to search and view contacts. For more information, see [Manage who can search for contacts and access detailed information](contact-search.md#required-permissions-search-contacts).

## Create a calibration session
<a name="calibrations-performance-evaluations-create"></a>

**To create a calibration session**

1. Login to Amazon Connect Customer with a user account that has the necessary permissions within their security profile.

1. On the left navigation menu, choose **Analytics and optimization, Contact search**.

1. Search for a contact that you want to perform calibrations on, for example, minimum interaction duration, specific queue.

1. On the **Contact details** page of a contact, choose **Evaluations** on the top right to open the **Evaluations** side panel.

1. In the side panel, select the **Calibration session** radio button, choose the desired form for the calibration using the dropdown menu, and then choose the **Setup calibration session** button.  
![A diagram of the calibrations session setup.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibrations-setup1.png)

1. Enter a title for the calibration session, select the participants, and optionally designate an expert participant and set a due date.  
![A diagram of the calibrations session setup with participants and due date.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibration-setup2.png)

1. After creation, the calibration session will appear in the side panel. An evaluation will be automatically generated for each participant.  
![A diagram of the created calibrations session for each participant.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibration-setup3.png)

## Edit a calibration session
<a name="calibrations-performance-evaluations-edit"></a>

**To edit a calibration session**

1. On the side panel locate the calibration sessions and choose **Edit**.  
![A diagram of choosing to edit a calibrations session.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibrations-edit1.png)

1. In the form that opens in the side panel you can modify the calibration session title, add or remove participants, optionally designate an expert participant, and set or adjust the due date.

1. Choose **Save** to update the calibration session. The changes will be reflected in the side panel. New participants will automatically receive an evaluation, while removed participants will have their evaluations deleted. 

## Perform evaluations as a part of a calibration session
<a name="calibrations-perform-evaluations"></a>

Use the following procedure to perform evaluations as a part of a calibration session:

**To perform evaluations**

1. On the side panel locate the **Calibration evaluations assigned to you** section to view your calibration evaluations.  
![A diagram of calibration evaluations assigned to you.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibration-evaluations1.png)

1. Choose an evaluation to open it. You can respond to these evaluations in the same manner as standard evaluations, with options to save your progress or submit the completed evaluation. Automation is disabled on calibration sessions.  
![A diagram of responding to calibration evaluations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibration-evaluations2.png)

1. Calibration managers can access a list of all evaluations associated with a specific calibration session by viewing the calibration session details in the side panel. Calibration managers will also be able to view evaluations submitted by participants.

## Finalize a calibration
<a name="calibrations-finalize"></a>

**To finalize a calibration**

1. Access the calibration session details view and choose **Finalize**.  
![A diagram showing the finalize button for calibrations.](http://docs.aws.amazon.com/connect/latest/adminguide/images/calibrations-finalize.png)

1. Confirm the finalization when prompted. After a session is finalized, neither the session nor its evaluations can be edited.

1. Within a few seconds, a calibration report will be available for download in .csv format. This report contains the answers of participants that have submitted evaluations, along with the weighted scores for each question, section and the overall form, evaluator notes and comparison of the evaluator's scores with the expert evaluator.

   Use the field **absolute deviation from expert** (lower is better) for each participant to determine if an evaluator is significantly deviating from the expert while answering evaluation questions. You can also see **average absolute deviation from expert** (lower is better) to see if there are certain questions that get inconsistent answers from participants and need improvement (For example, better phrasing, more specific questions) 

## Finding calibration sessions
<a name="calibrations-find"></a>

Amazon Connect Customer notifies users participating in calibration sessions through email (for example, if a user is added as a participant, if there is a change to the due date). If a user managing a calibration session has added themselves as the **expert** participant, then they would also receive emails. The email contains a link to the contact which is being used for calibration. For users to receive email notifications, you need to assign emails to the users on Connect Customer. For more information, see [Add users to Connect Customer](user-management.md).

As a manager setting up a calibration, you can copy the contact ID to search for the contact on which the calibration session was set up. If you have not added yourself as an expert or if user emails are not set up within Connect Customer, you will not receive an email containing a link to the contact on which the calibration session was set up.