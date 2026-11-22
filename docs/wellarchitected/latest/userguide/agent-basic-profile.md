

AWS Well-Architected Agent is in preview release and is subject to change.

# Basic profiles

A basic profile is the zero-setup way to start with AWS Well-Architected Agent. Unlike a standard agent profile, a basic profile requires no configuration. You don't choose AWS accounts, create IAM roles, select pillars, or set goals. AWS WA Agent infers everything from the account you're signed in to.

The basic profile is automatically created in AWS accounts with an eligible support plan when you choose **Get started with Well-Architected Agent** from the dashboard in AWS Well-Architected Tool, AWS Support Console, or AWS Trusted Advisor.

**Note**  
For more detail on AWS WA Agent eligibility, see [Access and entitlements](agent-quotas.md#agent-access).

A basic profile only provides resource-level recommendations (application-level recommendations and architecture reviews require a standard agent profile).

To go beyond resource-level recommendations, you must create a standard agent profile. A standard profile adds application context, architecture reviews, multi-account or organization scope, and goals. There is no in-place upgrade from a basic profile. For more detail, see [Step 1: Enter profile details](agent-getting-started.md#agent-create-profile). 

 After you create a standard profile, the basic profile continues to exist in the background. It no longer appears in the console, but it remains accessible by direct link to its recommendations or profile ARN and through the API.

## Console
<a name="agent-basic-profile-console"></a>

Upon choosing **Get started with Well-Architected Agent** from the dashboard in either AWS Well-Architected Tool, AWS Support Console, or AWS Trusted Advisor, AWS WA Agent starts a one-time scan of the account and shows a notification that recommendations are on the way.

In the console, a basic profile provides a simplified version of the dashboard with resource-level recommendations only. Your basic profile is filtered out of the profile list and the profile switcher at all times, so you see recommendations only for the current account.

**Note**  
The scan runs once when the basic profile is first created. There is no recurring or scheduled scan. A refresh action is available to run the scan again on demand.

## API
<a name="agent-basic-profile-api"></a>

You can also create a basic profile directly with the `CreateAgentBasicProfile` API operation. The operation takes an empty request body, and AWS WA Agent infers everything from the calling identity. There is one basic profile per account per AWS Region, under a reserved name.

You can delete a basic profile only through the API. There is no console option to do so.