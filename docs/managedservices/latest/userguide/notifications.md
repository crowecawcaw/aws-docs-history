# Receiving AMS notifications

Communications between you and AMS occur for many reasons:

- An RFC created by AMS that requires your approval
- An AMS case created to investigate an RFC you created that has failed
- Events created by monitoring alerts
- Patching service notifications that inform you of upcoming patching
- Service requests and incident reports
- Monthly CRM reports
- Occasional important AWS announcements (your CSDM contacts you if any action on
  your part is required)
  All of these notifications are sent to the default contact information (the root account email) that you provided
  AMS when you were onboarded.
  Because it's difficult to keep individual emails updated, we recommend that you use a group email that can be updated
  on your end. All notifications sent to you are also received by AMS operations and analyzed before making a
  response.

AMS notification service provides two additional ways to set up contacts for notifications:

- Tag your resources with contact tags (the tag Key Value being contact information) and provide
  the tag Key Name to your CSDM. Alarms on those resources will be sent to the
  contacts provided in the Key Value, in addition to the account contact created at
  onboarding. This is especially useful for application owners. For more information,
  see [Tag-based alert notification](how-monitoring-works.md#how-mon-works-alert-notes-tags "how-monitoring-works.md#how-mon-works-alert-notes-tags").
- (Required at onboarding) Send to your CSDM named lists of contacts for non-resource based notifications.
  For example, you might have a list named "SecurityContacts" and another named "OperationsContacts", and so forth.
  AMS adds the list to the notification service, and
  alarms that apply to that list's context are sent to those contacts. This is especially useful for
  organizational matters.
  This advanced alert routing feature is active for most of the essential CloudWatch alarms such
  as Amazon EC2 instance failure, Amazon Elastic Block Store (Amazon EBS) volume capacity utilization - Root usage,
  Amazon EBS NonRoot usage, High Memory utilization, High Swap usage, and High CPU utilization for Amazon EC2.

Additionally, when you file a service request, or incident report, you have the option of adding "CC Emails"
(highly recommended) and those email addresses receive notifications about the service request or incident.

###### Important

While the CC email addresses provided in service requests and incident reports receive
email notifications
of communications, other notifications, such as patching notifications, appear in your Service Request list
(an email is also sent to the default contact), _without_ explicit notification to you
that you have a communication awaiting your attention. This is why we strongly recommend
adding a CC email where you can, and setting up the default contact email as a group to which everyone
using AMS is a member.

Additionally, you can request special notifications for new AMIs, for RFC state change, and for configuration
changes in your AMS account. These optional notification services are discussed next.
