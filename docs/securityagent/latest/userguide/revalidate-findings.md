# Revalidate penetration test findings

After you remediate a vulnerability, use AWS Security Agent to revalidate the finding and confirm whether it is still exploitable. Revalidation re-tests one or more existing findings without running a full penetration test. You get a fast answer on whether your fix worked.

During revalidation, AWS Security Agent authenticates to your application and re-runs the validation steps for each selected finding. It does not rediscover new vulnerabilities or test other parts of your application. This makes revalidation faster and more focused than a full penetration test.

## Prerequisites

Before you begin, ensure you have:

- A completed penetration test with at least one finding
- Access to the Agent Space that contains the finding
- A target application that is reachable with the current authentication configuration of the penetration test

## Select findings to revalidate

Choose one or more findings from a completed penetration test run:

1. Log in to the AWS Security Agent web application.
2. Open the penetration test run that contains the findings you want to revalidate.
3. In the findings panel, choose **Multiselect findings for revalidation**.
4. Select the check box next to each finding you want to revalidate. The findings you select are listed as you add them.
5. Choose **Revalidate findings**.

###### Before you revalidate

Revalidate a finding after you deploy a fix to the environment the original test ran against. Revalidation re-tests the same target, so the fix must be live for the result to be accurate.

## Interpret revalidation results

Revalidation runs as its own job and does not change the original finding. For each finding, revalidation reports whether AWS Security Agent could reproduce the vulnerability.

| Result       | What it means                                                                                                    |
| ------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Active**   | AWS Security Agent reproduced the vulnerability. The finding is still exploitable and needs further remediation. |
| **Resolved** | AWS Security Agent could not reproduce the vulnerability during revalidation.                                    |

## Trace revalidation history

Revalidation keeps the link between a finding and the runs that re-tested it, so you can trace remediation over time.

- From a revalidation job, choose **Original finding** to open the finding it re-tested.
- From a finding, view its **Revalidation jobs** to see each time it was revalidated and the result.

A revalidation run appears in your run history with a type of **Revalidation**, which distinguishes it from a full penetration test.

## Next steps

After revalidation, consider these next steps:

- Revalidate a finding again after each remediation attempt until its status is **Resolved**.
- Run a full penetration test for broad changes to your application instead of revalidating individual findings. For details, see [Create a penetration test](perform-penetration-test.md "perform-penetration-test.md").
