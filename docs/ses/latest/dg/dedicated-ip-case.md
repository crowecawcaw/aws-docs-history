# Requesting and relinquishing dedicated IP addresses (standard)

To use _dedicated IP addresses (standard)_, you must first request them. When you no longer
need them, you must relinquish them. Request and relinquish dedicated IPs (standard) through the
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/"). Your account is charged an additional monthly fee for each
standard dedicated IP address that you lease for use with Amazon SES. There's no minimum
commitment when using dedicated IPs (standard).

For more information about the costs associated with dedicated IPs (standard), see [Amazon SES Pricing](https://aws.amazon.com/ses/pricing/#Optional_Services "https://aws.amazon.com/ses/pricing/#Optional_Services").

For a list of all of the Regions where Amazon SES is currently available, see [AWS Region and Endpoints](../../../general/latest/gr/rande.md#ses_region "../../../general/latest/gr/rande.md#ses_region") in the
_Amazon Web Services General Reference_. To learn more about the number of
Availability Zones that are available in each AWS Region, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

## Request or relinquish dedicated IPs (standard)

You can request as many dedicated IPs (standard) as you need by creating a service quota increase
case in the AWS Support Center.

###### To request or relinquish dedicated IPs (standard)

1.  Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2.  In the left navigation pane, choose **Dedicated IPs**.
3.  Do one of the following:
    1. If you _don't_ have existing dedicated IPs in your
       account:
       1. The **Dedicated IPs** onboarding page is
          displayed. In the **Dedicated IPs (standard) overview** panel,
          choose **Request dedicated IPs**.

    2. If you have existing dedicated IPs in your account:
       1. Select the **Standard IP pools** tab on the
          **Dedicated IPs** page.
       2. In the **Standard overview** panel, choose
          **Request or relinquish Standard dedicated
          IPs**.

4.  The **Hello! We're here to help** page opens in the AWS
    Support Console. All the fields on this page will have the following values
    preselected:

        * **Choose the related issue for your case** –
         *Account and billing*
        * **Service** – *Service
         Quotas*
        * **Category** –
         *Amazon SES*
        * **Severity** – *General
         question*

    After verifying these values, choose **Next step: Additional
    information**.

5.  Under **Additional information**, complete the following
    selections:
    - For **Region**, select the AWS Region that your
      request applies to.
    - For **Quota Title**, select **Desired
      Dedicated IP**.
    - For **Value**, select the number of dedicated IPs you
      are requesting
      or relinquishing in the region selected.
    - If you want to request or relinquish dedicated IPs (standard) in another
      AWS Region, choose **Add another limit**, and fill in
      the fields accordingly. Repeat for each additional AWS Region.
    - For **Description**, make it clear what you have and
      what you want to do in each region specified as in the following
      examples:

    Request – _"I have two DIPs in the Milan region, but
    would like to add one more for a total of three"_

    Relinquish – _"I have two DIPs in the Ohio region, but
    want to remove one of them—please remove the DIP that has the
    address 23.251.228.95"_.

    ###### Important

    The process of relinquishing a dedicated IP address can't be
    reversed. If you relinquish a _dedicated IP
    address_ in the middle of a month, we prorate the
    monthly dedicated IP usage fee, based on the number of days that
    have elapsed in the current month.
    - Choose **Next step: Solve now or contact us**.
    - On the **Solve now or contact us** page, select your
      preferred contact language, and choose
      **Submit**.

After you submit the form, we'll evaluate your request. If we grant your request,
we'll reply to your case in the Support Center to confirm that the dedicated IP
addresses have been added to or removed from your account according to your
request.
