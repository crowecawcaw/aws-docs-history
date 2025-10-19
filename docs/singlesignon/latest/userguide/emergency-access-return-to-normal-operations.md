# Return to normal operations

Check
 the [AWS Health
 Dashboard](https://health.aws.amazon.com/health/status "https://health.aws.amazon.com/health/status")to confirm when the health of the IAM Identity Center service is
 restored. To return to normal operations, perform the following steps.


1. After the status icon for the IAM Identity Center service indicates that the service is healthy, sign in to IAM Identity Center.
2. If you can sign in to IAM Identity Center successfully, communicate to emergency access users that IAM Identity Center is
 available. Instruct these users to sign out and use the AWS access portal to sign back in to
 IAM Identity Center.
3. After all emergency access users sign out, in the IdP, disable the IdP federation application. We recommend that you perform this task after working hours.
4. Remove all users from the emergency access group in the IdP.
Your emergency access role infrastructure remains in place as a backup access plan, but it is now disabled.
