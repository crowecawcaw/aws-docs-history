# Get a local toll-free or DID Amazon Connect phone

number

To place or receive calls in your Amazon Connect instance, you need to claim a DID or
toll-free phone number. If you did not claim a phone number when you created your
Amazon Connect instance, follow these steps to claim one now.

## Claim a number for your contact

center

1. Log in to the Amazon Connect admin website with an Admin account, or an account assigned to a
   security profile that has **Phone numbers - Claim**
   permissions.
2. On the navigation menu, choose **Channels**,
   **Phone numbers**.
3. Choose **Claim a number**. You can choose a toll-free
   number or a Direct Inward Dialing (DID) number. If you're in the US, you
   can specify the area code you want for your number, and only available
   numbers with that area code will be displayed. When numbers are
   returned, choose one.

![The Claim phone number page, DID (Direct Inward Dialing) tab.](images/tutorial1-claim-number.png)

###### Note

Create a case by choosing the [Account and billing](https://support.console.aws.amazon.com/support/home#/case/create "https://support.console.aws.amazon.com/support/home#/case/create") option for these situations:

    * If you select a country or region, but no numbers display,
     you can request additional numbers for the country or
     region.
    * If you want to request a specific area code or prefix that
     you don't see listed, we'll try to accommodate your
     request.The following image shows the **Account and

billing** option on the **Create a
case** page of the **Support Center\*\*
console.

![The Account and billing option on the Create a case page.](images/create-case-support.png) 4. Enter a description for the number and, if required, attach it to a
contact flow in **Flow / IVR**. 5. Choose **Save**. 6. Repeat this process until you have claimed all your required phone
numbers. 7. After you claim your numbers, [associate
them with your flow(s)](associate-claimed-ported-phone-number-to-flow.md "associate-claimed-ported-phone-number-to-flow.md"). A flow defines the customer
experience with your contact center from start to finish.

## How many phone numbers you can

claim

There is a service quota for how many phone numbers you can have in each
instance. For the default service quota, see [Amazon Connect service quotas](amazon-connect-service-limits.md "amazon-connect-service-limits.md"). If you reach your quota,
but want a different phone number, you can release one of your previously
claimed numbers. You cannot claim the same phone number after releasing it.

If you need more phone numbers, you can request a service quota increase using
the [Amazon Connect
service quota increase form](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-connect "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase&limitType=service-code-connect").

## Avoid being blocked from claiming

or releasing too many numbers

If you plan to claim and release numbers frequently,
contact us for a service quota exception. Otherwise, it's possible you will be blocked from
claiming and releasing any more numbers until up to 180 days past the oldest number
released has expired.

By default you can claim and release up to 200% of your maximum number of active
phone numbers. If you claim and release phone numbers using
the UI or API during a rolling 180 day cycle that exceeds 200% of your phone number
service level quota, you will be blocked from claiming any more numbers until 180
days past the oldest number released has expired.

For example, if you already have 99 claimed numbers and a service level quota of 99 phone numbers, and in any 180
day period you release 99, claim 99, and then release 99, you will have exceeded the
200% limit. At that point you are blocked from claiming any more numbers until you
open an AWS support ticket.

## API instructions for

claiming phone numbers

To claim a phone number programmatically:

1. Use the [SearchAvailablePhoneNumbers](../APIReference/API_SearchAvailablePhoneNumbers.md "../APIReference/API_SearchAvailablePhoneNumbers.md") API to search for available
   phone numbers that you can claim to your Amazon Connect instance.
2. Use [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API to claim the phone number.

Claiming a number by using the [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") API puts the number in one of the
following three states: `CLAIMED`, `IN_PROGRESS`,
`FAILED`. 3. Run the [DescribePhoneNumber](../APIReference/API_DescribePhoneNumber.md "../APIReference/API_DescribePhoneNumber.md") API to determine the status of your
number claiming process.

    * `CLAIMED` means the previous [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") or [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation succeeded.
    * `IN_PROGRESS` means a [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") or [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation is still in progress
     and has not yet completed. You can call [DescribePhoneNumber](../APIReference/API_DescribePhoneNumber.md "../APIReference/API_DescribePhoneNumber.md") at a later time to verify if
     the previous operation has completed.
    * `FAILED` indicates that the previous [ClaimPhoneNumber](../APIReference/API_ClaimPhoneNumber.md "../APIReference/API_ClaimPhoneNumber.md") or [UpdatePhoneNumber](../APIReference/API_UpdatePhoneNumber.md "../APIReference/API_UpdatePhoneNumber.md") operation has failed. It will
     include a message indicating the failure reason. A common reason
     for a failure may be that the `TargetArn` value you
     are claiming or updating a phone number to has reached its limit
     of total claimed numbers. If you received a `FAILED`
     status from a `ClaimPhoneNumber` API call, you have
     one day to retry claiming the phone number before the number is
     released back to the inventory for other customers to
     claim.

###### Note

You will not be billed for the phone number during the 1-day period if
number claiming fails.

## "We couldn't claim your

number"

Even if it's the first time you've claimed a phone number, it's possible to
get this error message when you attempt to claim a number. All the issues that
cause this error message require help from AWS Support to resolve.

Contact AWS Support and they will provide assistance. For instructions, see
[Get administrative support for Amazon Connect](get-admin-support.md "get-admin-support.md").
