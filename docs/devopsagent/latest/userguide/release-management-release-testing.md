

# Release testing
<a name="release-management-release-testing"></a>

Release testing generates and executes test plans to validate code changes in realistic environments. The release testing agent runs exploratory UAT and regression testing — functional regression, user journey validation, integration testing, and edge case exploration — against your deployed web applications and REST APIs.

## How release testing works
<a name="how-release-testing-works"></a>

**Important**  
** Release testing executes real requests against your target application, including write operations (POST, PUT, DELETE). The agent explores endpoints, submits forms, and tests error handling — these actions may create, modify, or delete data in the target application. Use only where your risk profile can accept mutating actions as part of the exploratory testing. Ensure your applications can tolerate exploratory write operations without unintended consequences such as sending customer notifications, processing payments, or permanently deleting records. We recommend running against staging deployments; production applications should only be targeted when your application's write operations are safe for automated testing.

When triggered, the release testing agent:

1. **Generates a test plan** — Creates a test plan based on code changes or a test intent provided by the user. When triggered from a pull request or branch, the plan targets affected functionality. When triggered manually or from chat, you can provide a test intent describing what to validate. The plan covers functional correctness, integration behavior, and user-facing scenarios.

1. **Executes tests against a running application** — Given a target URL (web application or API endpoint), the agent explores the application and executes the generated tests. For web applications, this includes browser-based UI interaction and visual inspection. For APIs, this includes direct HTTP endpoint testing, schema validation, and error handling verification.

1. **Reports findings** — Results are returned with specific failures, affected functionality, reproduction steps, and recommended fixes.

Release testing supports web applications (React, Angular, Vue, server-rendered) and REST APIs.

## Supported test types
<a name="supported-test-types"></a>
+ **UI testing** — Browser-based testing with visual interactions for web applications
+ **API testing** — Direct HTTP endpoint testing for REST APIs

## Defining test profiles
<a name="defining-test-profiles"></a>

Test profiles define the web and API applications you want to test and the necessary configurations. Each test profile specifies a target application and its test type.

To create a test profile:

1. In the DevOps Agent web app, navigate to **Release Manager** in the left-hand navigation.

1. Select the **Test profiles** button.

1. Choose **Add test profile**.

1. Fill out the form with the following details:
   + **Name** — A descriptive name for the test profile (for example, "MyApp Staging")
   + **Target URL** — The URL of a staging or test deployment of your application. The agent sends real HTTP traffic including write operations (POST, PUT, DELETE). Do not use production URLs unless you understand and accept the risk of data modification.
   + **Test type** — Select either **UI testing** (browser-based testing with visual interactions) or **API testing** (direct HTTP endpoint testing)

1. Choose **Add test profile** to save.

**Note:** The application must be accessible over the public internet. Private network endpoints are not currently supported.

## Testing applications that require authentication
<a name="testing-applications-that-require-authentication"></a>

If your application requires a user to sign in, you can store credentials on the test profile so the release testing agent can sign in and explore your application without manual intervention. Credentials are stored encrypted and are used only to log in to the target application you specify.

When you configure an authenticated test profile, choose a two-factor authentication (2FA) method that matches how the target application challenges users at login:
+ **None** – Username and password only. The agent signs in with the stored credentials and no additional verification step.
+ **TOTP (time-based one-time password)** – A static value from the target application's authenticator setup. Supply it as a Base32 string or an `otpauth://` URI, or upload the setup QR code, which decodes to the same `otpauth://` URI. The agent uses the stored secret when it signs in. Use this when the application prompts for a verification or authenticator code.
+ **Email** – A one-time code delivered to an email address. The agent retrieves the emailed code at login. Use this when the application emails a verification code instead of using an authenticator.

At a 2FA prompt, the agent automatically generates or retrieves the code, submits it, and continues testing without further action from you.

**Note:** TOTP is supported for UI and API test profiles. Email 2FA is supported for UI test profiles only.

### Configuring TOTP
<a name="configuring-totp"></a>

1. When adding or editing a test profile, select the **Authenticated** user type.

1. Under the 2FA method, choose **TOTP**.

1. Provide the TOTP secret in one of the following ways:

   1. Enter the **Base32 secret** (for example, `JBSWY3DPEHPK3PXP`) from the target application's authenticator setup.

   1. Enter the **`otpauth://` URI** from the authenticator setup.

   1. Choose **Upload QR code** to upload the setup QR code image. The secret is decoded from the image and filled in for you automatically.

1. Save the test profile.

At login, the agent uses the stored secret to complete the verification step when the application prompts for a code. For **UI** profiles the code is entered into the browser; for **API** profiles the code is included in the authentication request body. The secret is stored encrypted and is never exposed in test output or logs.

**Note:** Only time-based codes (TOTP) are supported. Counter-based one-time passwords (HOTP) and hardware security keys are not supported.

### Configuring email 2FA
<a name="configuring-email-2fa"></a>

Email 2FA lets the agent retrieve a one-time code that the target application sends to an email address at login. This method applies to UI test profiles only.

1. When adding or editing a test profile, select the **Authenticated** user type.

1. Under the 2FA method, choose **Email**.

1. (Optional) Enter a **sender filter** — an email address (for example, `noreply@service.com`). When set, the agent only accepts codes sent from that address.

1. Save the test profile. The test profile page displays a **forwarding address** in the form `mfa+<testProfileId>@<stage>.<region>.release-testing.aidevops.aws.dev`.

1. In the mailbox that receives the login codes for your test account, create a one-time rule that forwards the verification emails to the forwarding address shown on the test profile.

At login, expect the application to email a verification code to your test account. Your forwarding rule delivers the code to the forwarding address, and the agent retrieves and submits it to complete the sign-in.

**Note:** Some enterprise mail systems block automatic forwarding to external addresses. If your test account's mailbox cannot forward externally, email 2FA cannot be used for that account.

## Running tests from a test profile
<a name="running-tests-from-a-test-profile"></a>

From the **Test profiles** page, you can manually trigger a test run:

1. Locate your test profile in the list.

1. Choose **Start testing**.

1. (Optional) Specify specific instructions and what to test in **Test intent**. For example, "Verify the checkout flow handles expired coupons correctly" or "Test the user registration form with invalid inputs."

The agent will generate a test plan based on your intent (or explore broadly if no intent is provided), execute tests, and report results in the **Release Manager** section under proposed changes.

## Running tests from DevOps Agent chat
<a name="running-tests-from-devops-agent-chat"></a>

From DevOps Agent chat, you can request release testing. Ask the agent to list your test profiles or specify which one to run. The agent will ask any needed follow-up information, such as what to test or which areas to focus on.

Examples:
+ "List my test profiles"
+ "Run test profile my-test-profile"
+ "Run release testing on my application at https://staging.myapp.com and verify the payment flow"

The agent reports progress as it explores the application, and returns results with specific findings, screenshots (for UI tests), and reproduction steps.

## Running tests from your IDE
<a name="running-tests-from-your-ide"></a>

From Kiro IDE or Claude Code, the coding agent can invoke release testing:

First, install the [Kiro power]() or [Claude Code plugin]().
+ Specify a test requirement or intent describing what to validate (for example, "verify the login flow works after the auth refactor")
+ The coding agent passes the test intent and a target test profile to the release testing agent
+ The release testing agent generates and executes tests, then reports findings back
+ If issues are discovered, the coding agent offers to fix them in place

**Note:** Testing against a pull request directly from the IDE is not currently supported. Use a test profile with a deployed application URL and provide a test requirement to focus the testing.

## Release testing in CI/CD pipelines
<a name="release-testing-in-cicd-pipelines"></a>

### GitHub Actions
<a name="github-actions"></a>

The `aws-actions/devops-agent-release-testing@v1` GitHub Action triggers the release testing agent after deployment and reports results as a GitHub Check Run on your commit or pull request.

#### Prerequisites
<a name="prerequisites"></a>
+ A [test profile](#defining-test-profiles) configured in your Agent Space
+ A [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md) configured in your Agent Space

#### Step 1: Configure GitHub repository secrets
<a name="step-1-configure-github-repository-secrets"></a>

In your GitHub repository, go to **Settings → Secrets and variables → Actions → Repository secrets** and add:


| Secret | Description | 
| --- | --- | 
| DEVOPS\_AGENT\_WEBHOOK\_URL | The webhook URL from your Agent Space | 
| DEVOPS\_AGENT\_WEBHOOK\_SECRET | The webhook signing secret from your Agent Space | 

For information on creating a webhook endpoint, see [Invoking DevOps Agent through Webhook](configuring-integrations-and-knowledge-invoking-devops-agent-through-webhook.md).

#### Step 2: Add the action to your workflow
<a name="step-2-add-the-action-to-your-workflow"></a>

Add the release testing step to your workflow (for example, `.github/workflows/release-tests.yml`):

```
name: Release Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

permissions:
  checks: write
  contents: read
  pull-requests: read

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Trigger Release Tests
        uses: aws-actions/devops-agent-qa@v1
        with:
          webhook-url: ${{ secrets.DEVOPS_AGENT_WEBHOOK_URL }}
          webhook-secret: ${{ secrets.DEVOPS_AGENT_WEBHOOK_SECRET }}
          test-profile-id: <YOUR_TEST_PROFILE_ID>
          test-requirement: <WHAT_TO_TEST>  # optional
        env:
          GITHUB_TOKEN: ${{ github.token }}
```

Replace `<YOUR_TEST_PROFILE_ID>` with the test profile ID from your Agent Space (starts with `ki-`). The `test-requirement` input is optional — use it to focus the agent on specific areas (for example, "verify login flow after auth refactor").

#### Action inputs
<a name="action-inputs"></a>


| Input | Required | Description | 
| --- | --- | --- | 
| webhook-url | Yes | The webhook URL from your Agent Space | 
| webhook-secret | Yes | The webhook signing secret for HMAC-SHA256 authentication | 
| test-profile-id | Yes | The test profile ID to trigger (starts with ki-) | 
| test-requirement | No | Optional focus area for testing | 

#### Required workflow permissions
<a name="required-workflow-permissions"></a>


| Permission | Reason | 
| --- | --- | 
| contents: read | Required for actions/checkout in private repos | 
| pull-requests: read | Resolve PR number from merge commit SHA | 

#### How it works
<a name="how-it-works"></a>

1. Your workflow triggers (for example, after deployment to a staging environment).

1. The action creates a Check Run (`in_progress`) on the commit or PR, which appears as a pending check.

1. The action signs and sends a webhook to your Agent Space.

1. The release testing agent picks up the task and runs tests against your application.

1. Results are reported back as a GitHub Check Run (pass/fail with a detailed summary).

You can view full execution details (timeline, test cases, screenshots for UI tests) in the DevOps Agent web app linked from your Agent Space.

## Reviewing test results
<a name="reviewing-test-results"></a>

Test results appear in the **Releases** section of the DevOps Agent web app under proposed changes. Each test run shows:
+ **Status** — Completed, Failed, or In Progress
+ **Category** — Release Testing
+ **Duration** — How long the test run took
+ **Source** — Whether it was triggered manually, from chat, or from a CI/CD pipeline

Select a test run to view detailed results including specific test failures, screenshots (for UI tests), reproduction steps, and recommended fixes.