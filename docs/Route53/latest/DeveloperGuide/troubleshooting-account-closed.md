

# My AWS account is closed or permanently closed, and my domain is registered with Route 53
<a name="troubleshooting-account-closed"></a>

If you close your AWS account, or if your account is closed or permanently closed, your domains will go through a deletion process:

1. We will notify you that your account is closed and your domain will be suspended in the next 5 days on a daily basis.

1. After your domain is suspended, the following will take place: 
   + If your registrar is Amazon Registrar, we will notify you that we will delete your domain in 30 days. For more information, see [Finding your registrar and other information about your domain](find-your-registrar.md).
   + If your registrar is Gandi, we will notify you that we will release your domain to Gandi when your account becomes permanently closed.

1. After waiting 30 days, we will delete all the domains registered with Amazon Registrar in the account and send you an update.

1. When your account becomes permanently closed, we will release all the domains registered with Gandi in the account to Gandi.

If you reopen your account during the time period that your domains can be recovered, we will unsuspend your domains, or inform you that your domains were deleted but they might be able to be restored. For more information, see [Domains that you can register with Amazon Route 53](registrar-tld-list.md).

**Note**  
After 90 days have passed from when you closed your account, you can no longer reopen it. For more information, see [Closing an account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-closing.html) in the *AWS Account Management guide*.

For more information, see [Contacting AWS Support about domain registration issues](domain-contact-support.md).