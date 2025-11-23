# Finding group summary powered by generative

AI

By default, Amazon Detective automatically provides summaries of an individual finding group.
The summaries are powered by generative artificial intelligence (generative AI) models hosted on [Amazon Bedrock](../../../bedrock/latest/userguide/what-is-bedrock.md "../../../bedrock/latest/userguide/what-is-bedrock.md").

By using finding groups, you can examine multiple security findings, as they relate to
a potential security event, and identify potential threat actors. Finding group
summaries for finding groups builds upon these capabilities. Finding group summaries
consume the data for a finding group, rapidly analyze relationships between the findings
and affected resources, and then summarize potential threats in natural language. You
can leverage these summaries to identify larger security threats, improve investigation
efficiency, and shorten the response timelines.

###### Note

Finding group summaries powered by generative AI may and not always provide completely
accurate information. See [AWS Responsible AI
Policy](https://aws.amazon.com//machine-learning/responsible-ai/policy/ "https://aws.amazon.com//machine-learning/responsible-ai/policy/") for more information.

## Reviewing finding group summary

The finding group summary for a finding group gives you a clear, detailed
explanation of a security event. In natural language, the explanation includes a
succinct title, a summary of the resources involved, and curated information about
those resources.

###### To review a finding group summary

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Finding groups**.
3. In the **Finding groups** table, choose the finding group
   that you want to display a summary of. A details page appears.

On the details page, you can use the **Summary** pane to review a
generated, descriptive summary of the top findings in the finding group. You can
also review an analysis of the top threat events in the finding group, which you can
then investigate further. To add the generated summary to your notes or a ticketing
system, choose the copy icon in the pane. This copies the summary to your clipboard.
You can also share your feedback about the finding group summary output in the summary,
which can provide a better experience in the future. To share your feedback, choose
the thumbs up or thumbs down icon, depending on the nature of your feedback.

###### Note

If you provide feedback about the finding group summary, your feedback is not used for model
tuning. We use it only to help facilitate that the prompts in Detective are crafted
effectively.

![The Summary pane, with a generated descriptive summary of the top findings in a finding group and an analysis of the top threat events in the group.](images/Detective-assistant.png)

## Disabling finding group summary

By default, finding group summary is enabled for finding groups. You can disable
finding group summary at any time. If you disable, you can enable them again later.

###### To disable finding group summary

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Preferences**.
3. Under **Finding group summary**, choose
   **Edit**.
4. Turn off **Enabled**.
5. Choose **Save**.

## Enabling finding group summary

If you previously disabled finding group summary for finding groups, you can
enable them again at any time.

###### To enable finding group summary

1. Open the Detective console at [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the navigation pane, choose **Preferences**.
3. Under **Finding group summary**, choose
   **Edit**.
4. Turn on **Enabled**.
5. Choose **Save**.

## Supported Regions

**Finding group summary** is available in the following AWS Regions.

- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
