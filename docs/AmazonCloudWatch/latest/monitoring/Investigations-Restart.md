# Restart an archived investigation

You can restart archived investigations.

###### To restart an archived investigation

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **AI Operations**,
 **Investigations**.
3. Choose the name of an archived investigation.
4. Choose **Restart investigation**.
5. (Optional)Update incident reports.


Any incident reports generated from the original investigation remain available in the
 investigation history. You can access these reports from the investigation details page.
 If the restarted investigation discovers more facts, you can regenerate the incident
 report using the following steps:


	1. Choose **Incident report** to regenerate your
	 incident report with new or updated facts.
	2. From the **Incident report** page, review updated
	 facts.
	3. Choose **Regenerate** to update your incident report.
	 If the **Regenerate** button is disabled, no new facts
	 are present.We recommend that you don't leave investigations open indefinitely, because
 alarm state transitions related to the investigation will keep being added to
 the investigation as long as it is open.
