# Can't see subscribed users

**Problem: Subscribed users are not appearing in the Amazon Q Developer
console.**

You have subscribed one or more users to the Pro tier, but when you navigate to the Amazon Q Developer
console's **Subscriptions** page, you can't see them.

**Solutions:**

- Make sure you're signed in to the correct AWS account and AWS Region.
- Try switching to the **Amazon Q** console. The Amazon Q console is able to
  display users who were subscribed as part of a group, and is also able to display
  subscriptions across multiple accounts in an organization managed by AWS Organizations.
- If you switched to the **Amazon Q** console, and still can't see users, do
  the following:
  - Make sure you're in the correct AWS Region. You will need to be in the Region
    where your IAM Identity Center instance is deployed. This might be a different Region from your
    Amazon Q Developer console and profile.
  - If you're using AWS Organizations, try enabling trusted access so that you can see
    subscriptions in both management and member accounts. For more information, see
    [Viewing an aggregated list of Amazon Q Developer subscriptions](subscribe-visibility.md "subscribe-visibility.md").
