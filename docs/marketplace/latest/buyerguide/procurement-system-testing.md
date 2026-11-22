

# Testing your procurement system integration

A working integration is a chain of several steps, and a problem anywhere along it looks the same to a buyer: the purchase didn't go through. Testing deliberately, one step at a time, tells you which link is broken instead of leaving you to guess.

The steps that follow also keep the test away from the rest of your organization. Approval rules apply to the accounts a policy covers, so a rule written to try the integration out would otherwise change how your buyers purchase while you are still configuring it. Limiting the test to one account means nobody else's purchasing is affected if the integration isn't working yet.

The approach is to limit a rule to a single test account, make one inexpensive purchase, and confirm that each step produced the result you expect.

## What you are testing
<a name="procurement-system-testing-what"></a>

A purchase that completes successfully proves all of the following at once:
+ Your buyers can reach the AWS Marketplace catalog from your procurement system.
+ A cart built in AWS Marketplace returns to your procurement system as a purchase requisition.
+ Your approval rules send the purchase where you intended.
+ Your procurement system can send a purchase order back to AWS Marketplace.
+ AWS Marketplace accepts that purchase order and creates the agreement.
+ With electronic invoice delivery set up, the invoice for the purchase is delivered to your procurement system.

## Choosing a test buyer account
<a name="procurement-system-testing-account"></a>

Choose one AWS account to test with. The account you're using to configure the integration is a reasonable choice, since you already have access to it.

If you go on to make a real purchase, that purchase is charged, so pick an account where a small charge is acceptable.

The buyer you test with needs the buyer permissions for procurement system integration. For the managed policy that grants them, see [Permissions](procurement-system-prerequisites.md#procurement-system-prerequisites-permissions).

## Creating an approval policy for that account
<a name="procurement-system-testing-policy"></a>

Create an approval policy, assign it to the test account only, and give it a rule that sends purchases to your procurement system.

A rule matching on offer type, for example **Public**, is a good choice for a test, because it matches whatever you buy without you having to predict the product's delivery method or pricing terms.

**Important**  
A policy assigned to the test account takes the place of the policy that account would otherwise follow, for as long as it exists. During the test, the rules in your wider policy don't apply to that account. For more information about how policies replace one another, see [Routing purchases to your procurement system](procurement-system-routing.md).

## Testing without completing a purchase
<a name="procurement-system-testing-no-agreement"></a>

A test that runs to the end completes the purchase, which creates an agreement. If you want to confirm the integration works without that happening, even for a free product, you can arrange for the purchase to stop short of completing.

Add a second rule to your test policy that matches the same purchases as the first one, and give it an approver in the AWS console from your management account instead of your procurement system. Both rules now match the test purchase, so it collects both approvals at once rather than one after the other.

Everything up to the purchase order still happens. The requisition reaches your procurement system, your own workflow runs on it, and the purchase order comes back to AWS Marketplace and is accepted. That is the part of the chain the integration is responsible for, so an approval arriving from your procurement tool confirms it works.

You can see the result on the [**Approval requests**](https://console.aws.amazon.com/marketplace/private-marketplace/approval-requests?region=us-east-1) page. The request shows as **Approved**, and its details page shows the purchase order your procurement system returned.

The purchase itself can't complete, because the console approval is still outstanding and a purchase needs every approval it collected. No agreement is created and nothing is charged. Once you have confirmed what you need to, reject the console approval to close the request, or leave it to expire at the end of the approval period.

**Note**  
This works because rules that send to different approvers add to each other rather than replace one another. For how overlapping rules combine, see [Routing purchases to your procurement system](procurement-system-routing.md).

**Note**  
Electronic invoice delivery can't be tested this way. An invoice follows a completed purchase, and this arrangement stops the purchase completing, so no invoice is produced. To test invoice delivery, complete a purchase end to end.

## Testing the integration end to end
<a name="procurement-system-testing-purchase"></a>

To confirm that a purchase completes and the agreement is created, run the test without the second approval rule and let the purchase finish.

Using the test account, start in your procurement system, punch out to the AWS Marketplace catalog, and make a purchase. We recommend a product with usage-based pricing, because it carries no charge until the product is used, so you can complete the purchase and see the agreement without incurring a cost. Remove what the test creates when you have finished, as described in [Cleaning up after the test](#procurement-system-testing-cleanup).

**Important**  
You are responsible for purchases made from your account, including purchases that result from a misconfigured integration or from testing. If a purchase is made unintentionally, contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us) immediately.

**Note**  
A usage-based product doesn't let you test electronic invoice delivery, because no invoice is produced until the product is used. To test invoice delivery, make a purchase that carries an upfront charge instead, and accept that the charge applies.

## Checking that each step completed
<a name="procurement-system-testing-check"></a>

The following steps are the test itself, in two parts. Work through them in order, confirming each result before you move on: the first step that doesn't produce the result described tells you where the problem is.

### Part 1. Starting and submitting the purchase
<a name="procurement-system-testing-check-submit"></a>

**To start and submit the purchase**

1. Sign in to your procurement system as a buyer.

1. Start a punchout session by choosing the AWS Marketplace supplier.

1. (Optional) If you have configured single sign-on, confirm that you were redirected to your own sign-in page, and that you were signed in to AWS after authenticating there. Skip this step if you haven't configured single sign-on.

1. Open the offer you're using for the test, and confirm that the button reads **Request Approval**.
**Important**  
If the button has a different name, stop here. Your approval rules aren't matching this purchase, so there is no point continuing the test. For more information about approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).

1. Choose **Request Approval**.

1. Confirm that your procurement system received the cart as a purchase requisition, with the charges as line items.

1. Submit the cart for approval in your procurement system.

### Part 2. Approving and confirming the purchase
<a name="procurement-system-testing-check-approve"></a>

**To approve the purchase and confirm the result**

1. Ask your approver to approve the requisition in your procurement system, and confirm that your own approval workflow ran on it.

1. In your procurement system, confirm that the purchase order was issued and sent to AWS Marketplace.

1. On the [**Approval requests**](https://console.aws.amazon.com/marketplace/private-marketplace/approval-requests?region=us-east-1) page, confirm that the request shows as **Approved** and that the purchase order appears on its details page.

1. If you're testing end to end, confirm on the [**Manage subscriptions**](https://console.aws.amazon.com/marketplace/subscriptions?region=us-east-1) page that the agreement appears, with the purchase order associated with a charge.

1. If you're testing end to end, you set up electronic invoice delivery, and the purchase carried an upfront charge, confirm that the invoice for that charge arrives in your procurement system. For more information about electronic invoice delivery, see [Setting up electronic invoice delivery](procurement-system-invoicing.md).

1. When the test is finished, clean up as described in [Cleaning up after the test](#procurement-system-testing-cleanup).

For what to do when a step doesn't produce the result described, see [Troubleshooting procurement system integration](procurement-system-troubleshooting.md).

## Cleaning up after the test
<a name="procurement-system-testing-cleanup"></a>

A test leaves two things behind: anything you bought, and the policy you created for the test account. Remove both when you have finished.

**To clean up after the test**

1. If you completed a purchase, cancel the subscription it created. On the [**Manage subscriptions**](https://console.aws.amazon.com/marketplace/subscriptions?region=us-east-1) page, open the agreement, then under **Agreement** open the **Actions** list and choose **Cancel subscription**. Cancelling stops future charges but doesn't remove a charge that has already been incurred. For more information, see [Canceling product subscriptions](cancel-subscription.md).

1. Remove the approval policy you created for the test account.

**Important**  
Remove the test policy so that the account's purchases route correctly again, and so that the account follows the policy it should follow. If you leave the test policy in place, that account's purchases keep going to your procurement system, and the account stays outside your wider policy. Both matter if you use the account for real purchases.

## Testing again later
<a name="procurement-system-testing-again"></a>

Repeat this test after you change your connection credentials, after you change the punchout configuration in your procurement system, and before you rely on a new rule that routes somewhere you haven't used before.