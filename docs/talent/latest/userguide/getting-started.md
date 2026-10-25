

# Getting started with Amazon Connect Talent
<a name="getting-started"></a>

Amazon Connect Talent is an AI-powered hiring and candidate evaluation service integrated with Amazon Connect. Recruiters use it to create candidate evaluations, run AI-led interviews and assessments, and review candidate results. This chapter shows you how to sign in and find your way around the homepage.

**Topics**
+ [Signing in to Amazon Connect Talent](#signing-in)
+ [Navigating the homepage](#navigate-home-dashboard)
+ [Testing Amazon Connect Talent](#getting-started-test)

## Signing in to Amazon Connect Talent
<a name="signing-in"></a>

How you sign in to Amazon Connect Talent depends on how your administrator set up your instance. If your instance stores users in Amazon Connect Talent, you sign in with the username and password your administrator created for you. If your instance uses SAML 2.0 single sign-on, you sign in through your organization's identity provider. Your administrator gives you the sign-in address for your organization.

1. Open the Amazon Connect Talent sign-in address provided by your administrator.

1. Sign in. If your instance stores users in Amazon Connect Talent, enter the username and password your administrator provided. If your organization uses single sign-on, authenticate through your identity provider.

1. After you sign in, Amazon Connect Talent opens to the homepage.

If you cannot sign in, contact your Amazon Connect Talent administrator to confirm that your account has access.

## Navigating the homepage
<a name="navigate-home-dashboard"></a>

The homepage is the first page a recruiter sees after signing in to Amazon Connect Talent. It gives you a quick overview of your top jobs and recently created evaluations.

### First-time welcome screen
<a name="navigate-home-dashboard-welcome"></a>

When you sign in for the first time, Amazon Connect Talent displays a welcome screen with a greeting by name. The screen introduces a three-step hiring process:

1. **Create your candidate evaluation** – Build AI-powered interviews and assessments.

1. **Interview candidates** – Scale screening with AI-led interviews.

1. **Hire the best role fit** – Make data-driven hiring decisions.

Choose **Create your first candidate evaluation** to get started. After you create your first evaluation, the welcome screen switches to the standard homepage.

### Homepage layout
<a name="navigate-home-dashboard-layout"></a>

The standard homepage contains two main areas:
+ **Top jobs to review** – Job cards that display the job title, metrics, and a **View job** button.
+ **Recently created evaluations** – A table with a **Name** column. The header includes a **Create** button.

### To view job details from the homepage
<a name="navigate-home-dashboard-view-job"></a>

1. Choose **View job** on a job card.

1. Review the job detail page, which displays metrics with candidate data and a filterable list of candidates.

1. Use the **Status**, **Evaluation**, and **Sort by** filters to narrow the candidate list.

1. Enter candidate properties in the search box to find specific candidates.

### Navigation sidebar
<a name="navigate-home-dashboard-sidebar"></a>

The navigation sidebar is available on every page in Amazon Connect Talent. It provides access to the following areas:
+ **Home** – Top jobs and recent evaluations.
+ **Evaluations** – Full list of all evaluations.
+ **Jobs** – Full list of all jobs.
+ **Settings** – Instance configuration.

The sidebar collapses to icons on smaller screens.

### Amazon Connect Talent Teammate
<a name="navigate-home-dashboard-assist"></a>

Amazon Connect Talent Teammate is an AI-powered teammate that answers questions about your work and surfaces information from across the application. For more information, see [Amazon Connect Talent Teammate](connect-talent-assistant.md).

## Testing Amazon Connect Talent
<a name="getting-started-test"></a>

After you set up your instance, test Amazon Connect Talent end-to-end by creating an evaluation and sending it to yourself or your team.

### Optional prerequisites
<a name="getting-started-test-prerequisites"></a>

Before you test Amazon Connect Talent, you can complete the following optional tasks:
+ **Upload your knowledge base** – Amazon Connect Talent uses your knowledge base to understand your company values and the key competencies you want to assess. This informs how evaluations are tailored to your organization. For more information, see [Manage knowledge bases](https://docs.aws.amazon.com/talent/latest/adminguide/manage-knowledge-bases.html).
+ **Connect your applicant tracking system (ATS)** – Amazon Connect Talent imports all the jobs you're currently hiring for. If your ATS isn't connected yet, you can upload or describe your job directly during evaluation creation. For more information, see [ATS integrations](https://docs.aws.amazon.com/talent/latest/adminguide/integrations.html).

### Build and test an evaluation
<a name="getting-started-test-build"></a>

This end-to-end walkthrough covers creating, publishing, sending, and reviewing a test evaluation:

1. **Create an evaluation** – Choose a role and generate a tailored evaluation. For more information, see [Create an evaluation](managing-evaluations.md#create-candidate-evaluation).

1. Publish the evaluation – finalize and publish it.

1. **Send to candidates** – Navigate to the published evaluation and choose **Send to candidates**. Enter the email addresses of yourself or your team members to send test evaluations.
**Tip**  
Sending a test evaluation to the same email address will overwrite your previous results. Some email clients support plus addressing, which lets you create variations of your email to generate separate candidate records. Add `+` followed by any number or text before the `@` symbol—for example, `yourname+1@yourcompany.com`, `yourname+2@yourcompany.com`. Each variation creates a separate candidate record in Amazon Connect Talent, but all emails deliver to the same inbox. Check whether your email client supports plus addressing before relying on this approach.

1. Review results – after your testers complete their evaluations, review their results to understand how Amazon Connect Talent evaluates and scores candidates. For more information, see [How scoring works](how-scoring-works.md).