# Generating sample findings in GuardDuty

Amazon GuardDuty helps you generate sample findings to visualize and understand the
various finding types that it can generate. When you generate sample findings, GuardDuty
populates your current findings list with one sample for each supported finding
type, including attack sequence finding types.

The generated samples are approximations populated with placeholder values. These samples
may look different from real findings for your environment, but you can use them to test
various configurations for GuardDuty, such as your EventBridge events or filters. For a list of
available values for finding types, see [GuardDuty finding types](guardduty_finding-types-active.md "guardduty_finding-types-active.md") table.

## Generating sample findings through the GuardDuty console or

API

Choose your preferred access method to generate sample findings.

###### Note

The GuardDuty console helps you generate one of each finding type. To generate one or more
specific finding types, perform the associated API/CLI steps.

Console
Use the following procedure to generate sample findings. This process
generates one sample finding for each GuardDuty finding type.

######

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose
   **Settings**.
3. On the **Settings** page, under **Sample
   findings**, choose **Generate sample
   findings**.
4. In the navigation pane, choose **Findings**. The
   sample findings are displayed on the **Current
   findings** page with the prefix
   **[SAMPLE]**.

API/CLI
You can generate a single sample finding matching any of the GuardDuty finding
types through the [CreateSampleFindings](../APIReference/API_CreateSampleFindings.md "../APIReference/API_CreateSampleFindings.md") API, the available
values for finding types are listed in [GuardDuty finding types](guardduty_finding-types-active.md "guardduty_finding-types-active.md") table.

This is useful for the testing of CloudWatch Events rules or automation based on
findings. The following example shows how to generate a single sample
finding of the `Backdoor:EC2/DenialOfService.Tcp` type using the
AWS CLI.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty create-sample-findings --detector-id `12abc34d567e8fa901bc2d34e56789f0` --finding-types `Backdoor:EC2/DenialOfService.Tcp`
```

The title of sample findings generated through these methods always begins with
**[SAMPLE]** in the console. Sample findings have a value of
`"sample": true` in the **additionalInfo** section of
the finding JSON details.

To understand the finding details, such as finding severity and potentially compromised resource,
associated with the generated findings, see [Severity levels of GuardDuty findings](guardduty_findings-severity.md "guardduty_findings-severity.md") and
[Finding details](guardduty_findings-summary.md "guardduty_findings-summary.md").

To generate some common findings based on a simulated activity in a
dedicated and isolated AWS account within your environment, see [Test GuardDuty findings in dedicated
accounts](guardduty_findings-scripts.md "guardduty_findings-scripts.md").
