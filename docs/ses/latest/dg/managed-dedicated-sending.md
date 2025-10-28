# Dedicated IP addresses (managed) for Amazon SES

_Dedicated IP addresses (managed)_ is an Amazon SES feature that automatically sets up and
manages dedicated IP addresses on your behalf to provide a quick and easy way to start using
dedicated IP addresses that are managed by SES. This helps to ensure that your
dedicated IP addresses are used efficiently and optimally for how you send email.

To enable dedicated IPs (managed) in your account, you just create a managed IP pool and SES does
all the rest. SES will determine how many dedicated IPs you require based on your
sending patterns, create them for you, and then manage how they scale based on your sending
requirements.

Once enabled, you can utilize dedicated IPs (managed) in your email sending by associating the managed IP
pool with a [configuration set](using-configuration-sets.md "using-configuration-sets.md"), and then
specifying that configuration set when sending email. The configuration set can also be
applied to a sending identity by using a [default
configuration set](managing-configuration-sets.md#default-config-sets "managing-configuration-sets.md#default-config-sets").

## Benefits and features of dedicated IPs (managed)

The dedicated IP addresses that you create with dedicated IPs (managed) automate management tasks to
help ensure that your dedicated IP addresses are used in a way that's optimal for how
you send email:

- Easy
  onboarding
  – To get started with dedicated IPs (managed), you create a managed IP
  pool directly from the SES console. Dedicated IP addresses are
  automatically allocated to the pool. You can start sending with the managed IP
  pool without having to open a request case through the AWS Support
  Center.
- Auto-scaling per ISP – You don't have to
  manually monitor or scale your dedicated IP pools because the managed IP pool
  scales out automatically based on usage. It also takes into consideration
  ISP-specific policies. For example, if SES detects that an ISP supports a
  low daily send quota, the pool scales out to better distribute traffic to that
  ISP across more IP addresses.
- Intelligent warmup
  – Dedicated IPs (managed)
  start to send mail to ISPs based on their capacity. That is, how much they are
  currently warmed up. They automatically keep track of the level of warmup for
  each ISP individually. Additionally, the dedicated IPs (managed) feature provides information
  about your reputation at an effective daily rate with top ISPs in the form of
  Amazon CloudWatch metrics and built-in dashboards.
  - Warmup per
    ISP – SES tracks the reputation for each IP in
    the managed IP pool for each ISP individually. For example, if you've
    been sending all your traffic to Gmail, the IP addresses are considered
    warmed up only for Gmail and cold for other ISPs. If you change your
    traffic pattern by ramping up email sent to Hotmail, SES ramps up
    traffic slowly for Hotmail, as the IP addresses are not warmed up
    yet.
  - Adaptive warmup
    & Shared pool transitioning – The warmup
    adjustment is adaptive and takes into account actual sending patterns.
    When sending volume to an ISP drops, the warmup percentage also drops
    for that ISP. In the early phase of warmup, any sending that's excessive
    based on the current level of warmup _is sent through the IP
    addresses that are shared with other Amazon SES users—the
    SES shared
    pool_. In later stages of
    warmup, any sending that's excessive is proactively slowed down and
    retried later.

  ###### Important

  While dedicated IPs (managed) automatically warms up your dedicated IP addresses,
  part of that automatic process is working interactively with the
  SES shared IP pool.

      - If your sending rate is too aggressive for your new
       dedicated IPs while they're being warmed up, SES will
       automatically spill part of your sending over into the
       SES shared IP pool to protect the reputation of your
       new dedicated IPs.
      - Even after your new dedicated IPs are fully warmed up, it
       isn't guaranteed that all of your sending will go through
       them 100% of the time. For example, if your sending rate
       suddenly rises and dedicated IPs (managed) determines it must allocate an
       additional dedicated IP address, it will initiate the warmup
       process which includes using the shared pool. Likewise, if
       your sending rate suddenly drops very low, all of your
       sending could switch over to the SES shared IP pool,
       see [Why proper IP warmup is important](#importance-of-warmup "#importance-of-warmup").

- Automatic request & relinquish of dedicated IP
  addresses – You don't need to request or relinquish managed
  dedicated IP addresses through the AWS Support Center, as is required when
  using dedicated IPs (standard). When onboarding with dedicated IPs (managed) directly from the SES
  console, CLI, or API, you are automatically allocated dedicated IP addresses and
  charged a fee based on the volume of messages that you send. When you delete an
  IP pool that's created by dedicated IPs (managed) or opt out of dedicated IPs (managed), your allocated IP
  addresses are automatically relinquished and charges cease immediately.
  - Getting your first
    dedicated IP address – The dedicated IPs (managed) feature will
    automatically allocate your first dedicated IP address once your sending
    volume reaches hundreds of emails over a period of a few days. This
    ensures that the IP you send from can build a sending reputation and
    improve deliverability. (If you don’t expect your sending volume to be
    at this level, you should be using shared IP addresses. See the
    comparison table in [Dedicated IP addresses for Amazon SES](dedicated-ip.md "dedicated-ip.md") to review the type of
    IP addresses that are best for how you send email.)

## Why proper IP warmup is important

To ensure that your email will be delivered through your dedicated IP address, it must
have a good reputation with the receiving ISP. ISPs will only accept a small volume of
email from an IP that they don’t recognize. When you’re first allocated an IP, it’s new
and won’t be recognized by the receiving ISP because it doesn’t have a reputation
associated with it. In order for an IP’s reputation to be established, it must gradually
build trust with receiving ISP—this gradual trust building process is referred to
as _warming-up_. Immediately after dedicated IPs (managed) allocates an IP, it
starts the [Intelligent warmup](#intel-warmup "#intel-warmup") process.

With the [Warmup per ISP](#warmup-per-isp "#warmup-per-isp") and [Adaptive warmup](#adaptive-warmup "#adaptive-warmup") features of dedicated IPs (managed), business
continuity is maintained throughout the warmup cycle by ensuring that your email will be
delivered. Once the warmup phase is complete, any excess capacity is queued and sent
only through the dedicated IP pool. However, if you have one dedicated IP address and
your sending falls below the minimum volume required to maintain IP reputation,
_dedicated IPs (managed) may remove your dedicated IP and your sending will be routed
through the SES shared IP pool_.

###### Note

If you send small volumes of email (less than a few hundred per day over a few
days), it would be more beneficial to send through the SES [shared IP pool](managing-ip-pools.md "managing-ip-pools.md"). See if dedicated IPs (managed) is right for
how you send mail by reviewing the comparison table in [Dedicated IP addresses for Amazon SES](dedicated-ip.md "dedicated-ip.md").

## Understanding the shared responsibility between you

and SES when using dedicated IPs (managed)

While dedicated IP addresses (managed) offers numerous automated features for dedicated IP management,
scaling, and warmup, the extent of this automation and SES' responsibilities
needs to be understood. It would be incorrect to assume that "managed" means SES
completely handles all aspects of IP reputation and listing issues. To clarify these
misconceptions, we need to emphasize that while the service automates technical aspects
like scaling and warmup, you remain responsible for maintaining your sending reputation
and managing any reputation related issues such as getting listed in a Reputation Block
List (RBL).

The following FAQs clarify the shared responsibility model between you and SES
and address common misconceptions about the service's scope.
These FAQS highlight that while the "managed"
aspect refers to technical infrastructure management, you must still actively monitor
and maintain your sending reputation, keep bounce rates low, and handle most RBL
delisting requests yourself:

- [Dedicated IP addresses (managed) FAQs](faqs-managed-dips.md "faqs-managed-dips.md")

## Creating a managed IP pool to enable

dedicated IPs (managed)

To enable dedicated IPs (managed), you first create a managed IP pool. After you create a managed
pool, the feature determines how many dedicated IPs you require based on your sending
patterns and will dynamically scale them to your requirements.

To use your managed pool to send email, you must associate the managed pool with a
[configuration set](using-configuration-sets.md "using-configuration-sets.md"), and then specify
that configuration set when sending email. The configuration set can also be applied to
a sending identity by using a [default configuration
set](managing-configuration-sets.md#default-config-sets "managing-configuration-sets.md#default-config-sets").

There are two ways you can create a managed IP pool:

- Create a new pool.
- Convert an existing pool from standard to managed.

In the following procedures, instructions are provided for either method.

###### To create or convert to a managed IP pool using the SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Dedicated IPs**.
3. Depending on whether you want to create a new managed IP pool or convert a
   standard dedicated IP pool to a managed one, follow the respective
   instructions:

Create new pool

###### To create a new managed IP pool

    1. Do one of the following:


    	1. If you *don't* have existing
    	 dedicated IPs in your account:


    		1. The **Dedicated IPs**
    		 onboarding page is displayed. In the
    		 **Dedicated IPs (managed) overview** panel,
    		 choose **Enable dedicated
    		 IPs**.


    		The **Create IP Pool** page
    		 opens.
    	2. If you have existing dedicated IPs in your
    	 account:


    		1. Select the **Managed IP
    		 pools** tab on the **Dedicated
    		 IPs** page.
    		2. In the **All Dedicated IP (managed)
    		 pools** panel, choose **Create
    		 Managed IP pool**.


    		The **Create IP Pool** page
    		 opens.
    2. In the **Pool details** panel,


    	1. Choose **Managed (auto managed)**
    	 in the **Scaling mode**
    	 field.
    	2. Enter a name for your managed pool in the
    	 **IP pool name** field.


    	###### Note



    		* The IP pool name must be unique. It can't be
    		 a duplicate of a standard dedicated IP pool name
    		 in your account.
    		* You
    		 can't have more than 50 dedicated IP pools per
    		 AWS Region in your account inclusive of both
    		 managed and standard IP pools.
    3. (Optional) You can associate this managed IP pool with a
     configuration set by choosing one from the dropdown list in
     the **Configuration sets** field.


    ###### Note



    	* If you choose a configuration set that's
    	 already associated with an IP pool, it will become
    	 associated with this managed pool, and no longer
    	 be associated with the previous pool.
    	* To add or remove associated configuration sets
    	 after this managed pool is created, edit the
    	 configuration set's [Sending IP pool](managing-configuration-sets.md#console-detail-configuration-sets "managing-configuration-sets.md#console-detail-configuration-sets")
    	 parameter in the **General
    	 details** panel.
    	* If you haven’t created any configuration sets
    	 yet, see [Using configuration sets in Amazon SES](using-configuration-sets.md "using-configuration-sets.md").
    4. (Optional) You can add one or more **Tags** to your IP pool by including a tag key
     and an optional value for the key.


    	1. Choose **Add new tag** and enter
    	 the **Key**. You can
    	 also add an optional **Value** for the tag. You can add up to
    	 50 tags, if you make a mistake, choose
    	 **Remove**.
    	2. To add the tags, choose **Save
    	 changes**.


    	After you create the pool, you can add, remove, or
    	 edit tags by selecting the managed pool and choosing
    	 **Edit**.
    5. Select **Create pool**.


    ###### Note



    	* After you create a managed IP pool, it can't
    	 be converted to a standard IP pool.
    	* When using dedicated IPs (managed), you can't have more than
    	 10,000 sending identities (domains and email
    	 addresses, in any combination) per AWS Region in
    	 your account.

Convert standard to managed

###### To convert a standard dedicated IP pool to managed

    1. Select the **Standard IP pools** tab on
     the **Dedicated IPs** page.
    2. In the **All Dedicated IP (standard)
     pools** panel, select the checkbox of the
     dedicated IP pool you want to convert from standard to
     managed.
    3. Choose **Convert to managed
     pool**—read the **Convert to managed
     IP pool** dialogue to confirm that you
     understand the conditions of converting your standard
     dedicated IP pool to a managed one.


    ###### Note

    Before converting your dedicated IP pool from standard
     to managed, note the following:



    	1. All of your current dedicated IPs (standard) will be moved to
    	 the managed pool.
    	2. If you’re currently leasing too many dedicated IPs (standard)
    	 for your sending volume, then dedicated IPs (managed) will remove
    	 the redundant IPs.
    	3. If any of your dedicated IPs (standard) are part of an
    	 allow-list for other applications, you should not
    	 transfer them to the managed pool as they will be
    	 removed if they become
    	 redundant—*refer to point
    	 2*.
    	4. You will no longer be charged per IP, but
    	 instead will be charged based on the volume you
    	 send through the managed pool. See [Amazon SES
    	 pricing](https://aws.amazon.com/ses/pricing "https://aws.amazon.com/ses/pricing").
    4. If you agree to the conditions as stated, choose
     **Confirm**—a banner appears,
     confirming that your standard dedicated IP pool has been
     converted to a managed pool.


    ###### Note

    Any configurations sets or tags you had associated
     with the standard pool before conversion will now be
     associated with the managed pool providing a seamless
     transition for any email sending using the configuration
     set.

Event publishing can be used to track the managed pool's sending performance. For more
information, see [Monitor email sending using Amazon SES event
publishing](monitor-using-event-publishing.md "monitor-using-event-publishing.md").

## Viewing managed IP pool sending

and capacity in the Amazon SES console

For the managed IP pools you've created, the SES console provides an easy way
for you to observe how they're being used for your email sending through the use of
cards and time series graphs that show sending metrics and ISP utilization and
capacity.

###### To view managed IP pool sending and capacity using the SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Dedicated IPs**.
3. Select the **Managed IP pools** tab on the
   **Dedicated IPs** page.
4. Depending on whether you want to view sending and capacity metrics in the
   Amazon SES console or the Amazon CloudWatch console, follow the respective
   instructions:

Amazon SES console

###### To view sending and capacity metrics in the Amazon SES

console

    1. In the **All Dedicated IP (managed)
     pools** table, select the name of a managed IP
     pool listed in the **IP pool** column to
     view its details.


    The selected IP pool's detail page opens with the
     following cards and time series graphs:


    	1. Cards:




    		* *Sending status* –
    		 Indicates if your sending volume and frequency is
    		 enough to utilize dedicated IPs by displaying one
    		 of two statuses:




    			+ *Insufficient volume*
    			 – Your sending volume is too low.
    			+ *Sending via Dedicated
    			 IPs* – One or more dedicated IPs
    			 are being used in your managed pool.
    		* *Managed dedicated IP send
    		 volume* – The volume of email
    		 sent through dedicated IPs in your managed pool
    		 in the last 7
    		 days.
    		* *Managed dedicated IP send
    		 percentage* – The percentage of
    		 email sent through dedicated IPs in your managed
    		 pool in the last 7 days.
    	2. Graphs:




    		* *Sent volume* –
    		 The volume of email sent in the last 7 days
    		 through managed dedicated IPs as compared to
    		 shared IPs.
    		* *Percentage of sent
    		 volume* – The percentage of email
    		 sent in the last 7 days through managed dedicated
    		 IPs as compared to shared IPs.
    		* *ISP capacity* –
    		 Displays how much email is being sent through
    		 dedicated IPs in your managed pool per the top 10
    		 most widely used ISPs and their available capacity
    		 during your sending:




    			+ *Sends for ISP (red
    			 bars)* – The volume of email you
    			 sent in the last 24 hours through the selected
    			 ISP.
    			+ *Capacity for ISP (blue
    			 line)* – The selected ISP’s
    			 available capacity during the last 24
    			 hours.
    2. To filter on a specific ISP for the **ISP
     capacity** graph, choose the
     **ISP** list box and select an
     ISP—the graph will update with metrics for the
     selected ISP. (If you don't filter on an ISP, Gmail is
     displayed by default).

Amazon CloudWatch console

###### To view sending and capacity metrics in the Amazon CloudWatch

console

    * In the **All Dedicated IP (managed)
     pools** table, select the
     **See**
    *<pool\_name>*
    **CloudWatch metrics** link in the **CloudWatch
     metrics** column to view its details.


    The selected IP pool's page opens in the CloudWatch console
     displaying the following metrics:




    	+ *Send* – The volume of
    	 email sent through both managed dedicated IPs and
    	 shared IPs.
    	+ *ApproximateDedicatedSendingPercentage*
    	 – Indicates the approximate percentage of
    	 traffic that has been delivered through a dedicated
    	 IP.
    	+ *SentLast24Hours* – The
    	 volume of email you sent in the last 24 hours
    	 through the selected ISP. (Labeled *Sends
    	 for ISP* in the SES
    	 console.)
    	+ *Available24HourSend* –
    	 The selected ISP’s available capacity during the
    	 last 24 hours. (Labeled *Capacity for
    	 ISP* in the SES console.)

## Deleting a managed IP pool and opting

out of dedicated IPs (managed)

When you delete a managed IP pool, all of its allocated IP addresses are automatically
relinquished. If you only have one managed IP pool and you delete it, or you delete your
last remaining managed IP pool, you'll be opting out of the dedicated IPs (managed) feature and charges
will cease immediately.

###### To delete a managed IP pool using the SES console

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the left navigation pane, choose **Dedicated IPs**.
3. Select the **Managed IP pools** tab on the
   **Dedicated IPs** page.
4. In the **All Dedicated IP (managed) pools** table, select the
   radio button next to the **IP pool** name of the managed pool
   you want to remove and choose **Delete**.
5. In the pop-up modal, you'll have the opportunity to confirm your choice by
   selecting **Delete**, or **Cancel** to keep
   your managed pool.

###### Note

If you only have one managed pool or you're removing your last managed
pool, the pop-up modal will remind you that by deleting your remaining
managed pool, you'll be opting out of the dedicated IPs (managed) feature and will no
longer be charged for it. You will be required to enter
`*Disable*` in the confirmation field
before you can choose **Delete**.
