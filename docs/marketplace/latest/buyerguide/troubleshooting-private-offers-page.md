# Troubleshooting private offers

If you encounter HTTP status code 404 (Not Found) issues or similar difficulties when
working with **Private offers** in AWS Marketplace, consult the topics in this
section.

###### Issues

- [I get a Page not found (404) error when I
  click the offer ID to view the private offer](#troubleshooting-page-not-found "#troubleshooting-page-not-found")
- [None of these suggestions work](#troubleshooting-other-suggestions "#troubleshooting-other-suggestions")

## I get a Page not found (404) error when I

click the offer ID to view the private offer

- Check that you're signed in to the correct AWS account. The seller extends private
  offers to specific AWS account IDs.
- Check if the offer exists under [**Private offers**](https://console.aws.amazon.com/marketplace/home#/private-offers "https://console.aws.amazon.com/marketplace/home#/private-offers") in
  the AWS Marketplace console. If you don't find the offer under **Private
  offers**, it could be because the seller extended the offer to a different
  AWS account ID. Check with the seller to confirm the AWS account ID to which the
  offer was extended.
- Check that the private offer has not expired by viewing the **Accepted and
  expired offers** tab under [**Private offers**](https://console.aws.amazon.com/marketplace/home#/private-offers "https://console.aws.amazon.com/marketplace/home#/private-offers") in
  the AWS Marketplace console. If the offer has expired, work with the seller to modify the
  expiration date of the offer or extend a new offer to your account.
- Check that the account ID is allowlisted to view the private offer. Some ISVs use
  limited listings. Ask the ISV if they have allowlisted your account to view the product.
  Allowlisting is necessary for limited listings of AMI products. If you're in an AWS
  organization, and the seller extends the offer to the management account, linked
  accounts must be allowlisted to subscribe. Otherwise, the buyer's linked accounts that
  aren't allowlisted will get a Page not found (404) error when trying to view the
  offer.
- Check with your AWS administrator to confirm that you have
  `aws-marketplace:ViewSubscriptions` IAM permissions if you need to view
  the offer. For more information about AWS Marketplace security, see [Security on AWS Marketplace](buyer-security.md "buyer-security.md").
- Check if you're using a private marketplace.
  - Make sure that the product is on the allowlist of your private marketplace (if
    applicable), so that you can purchase the product. If you're not sure, contact your
    system administrator to check.

The following video provides information about troubleshooting HTTP status code 404 (Not
Found) errors.

## None of these suggestions work

If none of the previous suggestions resolved the HTTP status code 404 (Not Found) error,
try the following actions in your browser:

- Clear the cache.
- Delete cookies.
- Sign out, and then sign back in.
- Use an incognito or private browsing mode.
- Try a different browser. We don't recommend using Internet Explorer.

If you have completed all of the troubleshooting suggestions and are still receiving a
**Page not found** error, contact the Private Offer Success Team (POST)
through the [AWS Marketplace Management Portal](https://aws.amazon.com/marketplace/management/contact-us/ "https://aws.amazon.com/marketplace/management/contact-us/").
