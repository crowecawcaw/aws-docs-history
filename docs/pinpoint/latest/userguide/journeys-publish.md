**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Publish a journey

After you've [tested your journey](journeys-review-test.md#journeys-test "journeys-review-test.md#journeys-test") and you're ready for
customers to enter it, you can publish the journey. The publishing process requires you to
complete the review process one more time.

###### To publish a journey

1. In the upper-right corner of the journey workspace, choose
   **Review**. The **Review your journey** pane
   appears in the journey workspace.
2. Review the error messages that are shown on the first page of the **Review
   your journey** pane. You can't publish your journey until you resolve
   all the issues that are shown on this page. If there aren't any issues with your
   journey, you see a message stating that your journey doesn't contain any errors.
   When you're ready to proceed, choose **Next**.
3. The second page of the **Review your journey** pane contains
   recommendations and best practices that are relevant to your journey. You can
   proceed without resolving the issues that are shown on this page. When you're ready
   to proceed, choose **Mark as reviewed**.
4. On the third page of the **Review your journey** pane, choose
   **Publish**.

###### Note

Even if you configure the journey to begin immediately, there is a five-minute
delay before participants actually enter the journey. During this time, Amazon Pinpoint
calculates all the segment members, and prepares to start capturing analytics
data. This delay also gives you a final opportunity to stop the journey if
necessary. 5. Reviewing and publishing a journey adds an exit journey element to the journey
flow, indicating that the journey was reviewed and published successfully.
**Next**: [Pause, resume, or stop a journey](journeys-pause-stop.md "journeys-pause-stop.md")
