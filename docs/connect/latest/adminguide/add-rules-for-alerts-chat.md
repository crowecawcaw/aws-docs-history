# Add real-time alerts to

Contact Lens for supervisors based on keywords and phrases in a
chat

After you [enable real-time analytics](enable-analytics.md "enable-analytics.md")
in your flow, you can add rules that automatically alert supervisors when a
customer experience issue occurs.

For example, Contact Lens can automatically send an alert when certain
keywords or phrases are mentioned during the chat, or when it detects other
criteria. The supervisor can then view the **Contact details**
page for a real-time chat to view the issue. From there, supervisors can join
the chat, and provide guidance to the agent over chat to help them resolve the
issue faster.

The following image shows an example of what a supervisor would see on the
**Contact details** page when they get an alert for a
real-time chat. In this case, Contact Lens has detected an angry customer
situation.

![The contact details page, an alert for an angry real-time chat customer.](images/contact-lens-realtime-alert-chat.png)
When the supervisor monitors a chat, Contact Lens provides them with a
real-time transcript and customer sentiment trend that helps them understand the
situation and assess the appropriate action. The transcript also eliminates the
need for customers to repeat themselves if they are transferred to another
agent.

## Add rules for real-time

alerts for chats

1. Log in to Amazon Connect with a user account that is assigned the
   **CallCenterManager** security profile, or that
   is enabled for **Rules** permissions.
2. On the navigation menu, choose **Analytics and
   optimization**, **Rules**.
3. Select **Create a rule**,
   **Conversational analytics**.
4. Assign a name to the rule.
5. Under **When**, use the dropdown list to choose
   **real-time analysis**.
6. Choose **Add condition**, and then choose the
   type of match. The following image shows a rule configured for a
   **Sentiment - Time period** condition.

![The conditions for a real-time chat analysis rule.](images/contact-lens-realtime-chat-rule2.png)

Choose from the following options:

    * **Exact Match**: Finds only the exact
     words or phrases.
    * **Pattern Match**: Finds matches that may
     be less than 100 percent exact. You can also specify the
     distance between words. For example, you might look for
     contacts where the word "credit" was mentioned, but you do
     not want to see any mention of the words "credit card." You
     can define a pattern matching category to look for the word
     "credit" that is not within a one-word distance of the word
     "card."

###### Tip

Semantic Match isn't available for real-time analysis. 7. Enter the words or phrases, separated by a comma, that you want to
highlight. Real-time rules only support any keywords or phrases that
**were mentioned**.

![A words and phrases rule.](images/contact-lens-add-alert-rules-1.png) 8. Choose **Add**. Each word or phrase separated by
a comma gets its own line.

![A words and phrases rule with multiple phrases, each on it's own line.](images/contact-lens-add-alert-rules-2.png)

The logic that Contact Lens uses to read these words or
phrases is: (Talk OR to OR your OR manager) OR (this OR is OR not OR
helpful) OR (speak OR to OR your OR supervisor), etc. 9. To add more words or phrases, choose **Add group of words
or phrases**. In the following image, the first group
of words or phrases are what the agent might mention. The second
group is what the customer might mention.

![A words and phrases rule with multiple phrases for customer and agent.](images/contact-lens-add-category-rules-script3.png)

    1. In this first card, Contact Lens reads each line as
     an OR. For example: (Hello) OR (thank OR you OR for OR
     calling OR Example OR Corp) OR (we OR value OR your OR
     business).
    2. The two cards are connected with an AND. This means, one
     of the rows in the first card needs to be mentioned AND then
     one of the phrases in the second card needs to be
     mentioned.

The logic that Contact Lens uses to read the two cards of
words or phrases is (card 1) AND (card 2). 10. Choose **Add condition** to apply the rules
to:

    * Specific queues
    * When contact attributes have certain values
    * When sentiment scores have certain values

For example, the following image shows a rule that applies when an
agent is working the BasicQueue or Billing and Payments queues, the
customer is for auto insurance, and the agent is located in
Seattle.

![A words and phrases rule with multiple conditions.](images/contact-lens-add-category-rules-3.png) 11. When done, choose **Next**. 12. In the **Assign contact category** box, add a
name for the category. For example, **Compliant**
or **Not_Compliant**. 13. Choose **Add action** to specify what action
Amazon Connect should take when the conditions are met. You can configure
supervisor alerts by using email notifications or by developing a
custom integration with EventBridge.

![The Generate an EventBridge event and Send email notification options.](images/contact-lens-realtime-chat-rule3.png) 14. If you chose **Send email notification**, see
[Create rules that send
email notifications](contact-lens-rules-email.md "contact-lens-rules-email.md") for more
details about completing the page and for information about email
limits.

If you chose **Generate an EventBridge event**, see
[Create rules
that generate EventBridge events](contact-lens-rules-eventbridge-event.md "contact-lens-rules-eventbridge-event.md") for
more details about completing the page and for information about
subscribing to EventBridge event types.
