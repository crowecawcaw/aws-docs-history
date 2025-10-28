# Including or excluding operational

recommendations

AWS Resilience Hub provides an option to include or exclude the alarms, SOPs, and AWS FIS
experiments (tests) that were recommended for improving the resiliency score of your
application at any point of time. Including and excluding operational
recommendations will have an impact on the resiliency score of your application only
after you run a new assessment. Hence, we recommend you to run an assessment to get
the updated resiliency score and understand its impact on your application.

For more information about restricting permissions to include or exclude
recommendations per application, see [Limiting permissions to
include or exclude AWS Resilience Hub recommendations](include-exclude-limit-permissions.md "include-exclude-limit-permissions.md").

###### To include or exclude operational recommendations from applications

1. In the left navigation menu, choose **Applications**.
2. In **Applications**, open an
   application.
3. Choose **Assessments** and select an assessment from the
   **Resiliency assessments** table. If you don't have an
   assessment, complete the procedure in [Running resiliency assessments in AWS Resilience Hub](run-assessment.md "run-assessment.md") and
   then return to this step.
4. Select **Operational recommendations** tab.
5. To include or exclude operational recommendations from your application,
   complete the following procedures:

###### To include or exclude recommended alarms from your application

1. To exclude alarms, complete the following steps:
   1. Under **Alarms** tab, from
      **Alarms** table, select all the alarms (with
      **Not implemented** state) you want to exclude.
      You can identify the current implementation state of an alarm from
      the **State** column.
   2. From **Actions**, choose **Exclude
      selected**.
   3. From **Exclude recommendations** dialog, select
      one of the following reasons (optional), and choose
      **Exclude selected** to exclude the selected
      alarms from the application.
      - **Already implemented** – Choose
        this option if you have already implemented these alarms in
        an AWS service such as Amazon CloudWatch, or any other third-party
        service provider.
      - **Not relevant** – Choose this
        option if the alarms do not suit your business
        requirements.
      - **Too complicated to implement** –
        Choose this option if you think these alarms are too
        complicated to implement.
      - **Other** – Choose this option to
        specify any other reason for excluding the
        recommendation.

2. To include alarms, complete the following steps:
   1. Under **Alarms** tab, from
      **Alarms** table, select all the alarms (with
      **Excluded** state) you want to include. You
      can identify the current implementation state of the alarm from the
      **State** column.
   2. From **Actions**, choose **Include
      selected**.
   3. From **Include recommendations** dialog, choose
      **Include selected** to include all the
      selected alarms in your application.

###### To include or exclude recommended standard operating procedures (SOPs) from

your application

1. To exclude recommended SOPs, complete the following steps:
   1. Under **Standard operating procedures** tab, from
      **SOPs** table, select all the SOPs (with
      **Implemented** or **Not
      implemented** state) you want to exclude. You can
      identify the current implementation state of an SOP from the
      **State** column.
   2. From **Actions**, choose **Exclude
      selected** to exclude the selected SOPs from your
      application.
   3. From **Exclude recommendations** dialog, select
      one of the following reasons (optional), and choose
      **Exclude selected** to exclude the selected
      SOPs from the application.
      - **Already implemented** – Choose
        this option if you have already implemented these SOPs in an
        AWS service, or any other third-party service
        provider.
      - **Not relevant** – Choose this
        option if the SOPs do not suit your business
        requirements.
      - **Too complicated to implement** –
        Choose this option if you think these SOPs are too
        complicated to implement.
      - **None** – Choose this option if
        you don't want to specify the reason.

2. To include SOPs, complete the following steps:
   1. Under **Standard operating procedures** tab, from
      **SOPs** table, select all the alarms (with
      **Excluded** state) you want to include. You
      can identify the current implementation state of the alarm from the
      **State** column.
   2. From **Actions**, choose **Include
      selected**.
   3. From **Include recommendations** dialog, choose
      **Include selected** to include all the
      selected SOPs in your application.

###### To include or exclude recommended tests from your application

1. To exclude recommended tests, complete the following steps:
   1. Under **Fault injection experiment templates**
      tab, from **Fault injection experiment templates**
      table, select all the tests (with **Implemented**
      or **Not implemented** state) you want to exclude.
      You can identify the current implementation state of a test from the
      **State** column.
   2. From **Actions**, choose **Exclude
      selected**.
   3. From **Exclude recommendations** dialog, select
      one of the following reasons (optional), and choose
      **Exclude selected** to exclude the selected
      AWS FIS experiments from the application.
      - **Already implemented** – Choose
        this option if you have already implemented these tests in
        an AWS service, or any other third-party service
        provider.
      - **Not relevant** – Choose this
        option if the tests do not suit your business
        requirements.
      - **Too complicated to implement** –
        Choose this option if you think these tests are too
        complicated to implement.
      - **None** – Choose this option if
        you don't want to specify the reason.

2. To include recommended tests, complete the following steps:
   1. Under **Fault injection experiment templates**
      tab, from **Fault injection experiment templates**
      table, select all the tests (with **Excluded**
      state) you want to include. You can identify the current
      implementation state of the test from the **State**
      column.
   2. From **Actions**, choose **Include
      selected**.
   3. From **Include recommendations** dialog, choose
      **Include selected** to include all the
      selected tests in your application.
