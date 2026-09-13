

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# Awarding a bonus
<a name="AwardingBonus"></a>

You can send bonus payments to workers who have completed an assignment for you in Amazon Mechanical Turk (Mechanical Turk) in the past six months. Requesters commonly use bonus payments to recognize workers that perform tasks particularly well, or go above and beyond in helping to resolve problems with a task interface. 

To send a bonus, you can use the [`SendBonus`](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_SendBonusOperation.html) operation. You need to provide the ID of the worker and a past assignment that they've completed for you. The operation also requires that you specify the bonus amount in US Dollars and provide a reason for the award. 

Note that your account is charged for the bonus payment as well as Mechanical Turk fees. 