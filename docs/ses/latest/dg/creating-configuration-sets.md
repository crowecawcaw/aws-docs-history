# Creating configuration sets in

SES

You can use the SES console, the `CreateConfigurationSet` action in the
Amazon SES API v2, or the `aws sesv2 create-configuration-set` command in the Amazon SES CLI v2
to create a new configuration set. This section shows how to create configuration sets using
the SES console and the Amazon SES CLI v2.

## Create a configuration set

(console)

To create a configuration set using the SES console, follow these steps:

1.  Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2.  In the navigation pane, under **Configuration**, choose
    **Configuration sets**.
3.  Choose **Create set**.
4.  **General details** – This section provides options to
    customize your configuration set:
    - **Configuration set name** – The name for your
      configuration set. The name can contain up to 64 alphanumeric
      characters, including letters, numbers, hyphens (-) and underscores (\_)
      only.
    - **Sending IP pool** – When you send email
      using this configuration set, messages are sent from the dedicated IP
      addresses in the assigned pool. Select an IP pool from the list.

    ###### Note

    The **default** (ses-default-dedicated-pool)
    contains dedicated IP addresses that haven't been assigned to any
    other pool. To learn more about managing IP pools, see [Assign IP pools](managing-ip-pools.md "managing-ip-pools.md").
    - **Tracking options**
      - **Use a custom redirect domain** –
        Select the check box to use a custom redirect domain to handle
        open and click tracking for email sent with this configuration
        set.
      - **Custom redirect domain** – Select a
        verified domain from the _Choose a verified
        domain_ list to be your custom redirect domain.
        You can also enter a subdomain in the _Enter a
        subdomain_ field.

      ###### Note

      Custom redirect domains can be specified as
      follows:

          - You must first create and verify a custom redirect
           domain in the AWS Region you want to send and
           track email, as well as set up a Content Delivery
           Network (CDN). This is explained in [Configuring custom domains to handle
           open and click tracking](configure-custom-open-click-domains.md "configure-custom-open-click-domains.md").
          - Then, to use your custom redirect domain for open
           and click tracking, you must indicate it while
           creating or editing your configuration set here in
           this step.
          - Finally, after specifying your custom redirect
           domain, **View DNS records** will
           appear in the configuration set's **General
           details** container. If you expand it,
           you'll see the CNAME record that contains the
           tracking domain being used in your AWS Region. For
           example, if your custom subdomain is called
           *marketing.example.com* and it
           was created in the AWS Region
           `us-east-1`, expanding **View
           DNS records** would reveal a CNAME record
           with the following values: **Name**
           = *marketing.example.com* and
           **Value** =
           *r.us-east-1.awstrack.me*.


          You can use this information simply as a
           confirmation that you chose the correct tracking
           domain from the table when you set up your CDN as
           explained in [Configuring custom domains to handle
           open and click tracking](configure-custom-open-click-domains.md "configure-custom-open-click-domains.md"), or you can do this first, and use the CNAME
           record values from here to use in your CDN
           setup.

      - **HTTPS policy** – Select an HTTPS
        policy option for the protocol of the open and click tracking
        links for your custom redirect domain:
        - Optional –
          (Default behavior) Open tracking links will be wrapped
          using HTTP. Click tracking links will be wrapped using
          the original protocol of the link.
        - Required – Open
          and Click tracking links will both be wrapped using
          HTTPS.
        - Required for opens
          – Open tracking links will be wrapped using
          HTTPS. Click tracking links will be wrapped using the
          original protocol of the link.

    - **Advanced delivery options** – Choose the
      arrow on the left to expand the advanced delivery options
      section.
      - **Transport Layer Security (TLS)** –
        To require SES to establish a secure connection with the
        receiving mail server, and send emails using the TLS protocol,
        select the **Required** check box.

      ###### Note

      SES supports TLS 1.2 and recommends TLS 1.3. To
      learn more, see [Infrastructure security in
      SES](infrastructure-security.md "infrastructure-security.md").
      - **Maximum delivery duration** – To
        specify a time limit for SES to attempt email delivery
        through this configuration set, enter a value in seconds ranging
        from 300 and up to 50,400.

      ###### Note

      Setting a custom maximum delivery limit (shorter than the
      SES default of 14 hours), can be useful in such cases
      as time-sensitive emails (like those containing a
      one-time-password), transactional emails, and email that you
      want to ensure isn't delivered during non-business
      hours.

      ###### Tip

          - To calculate minutes to seconds, multiply by
           60, e.g., 7 minutes \* 60 = 420 seconds.
          - To calculate hours to seconds, multiply by
           3600, e.g., 2 hours \* 3600 = 7200 seconds.

5.  **Reputation options** – This section provides for
    setting up reputation metrics:
    - **Reputation metrics** – Used to track bounce
      and complaint metrics in CloudWatch for emails sent using this configuration
      set. _(Additional charges apply, see [Price per metric for
      CloudWatch](event-publishing-add-event-destination-cloudwatch.md#cw-add-pricing "event-publishing-add-event-destination-cloudwatch.md#cw-add-pricing").)_
      - **Enabled** – Select this check box to
        enable reputation metrics for the configuration set.

6.  **Suppression list options** – This section provides a
    decision set to define customized suppression starting with the option to use
    this configuration set to override your account-level suppression. The [configuration
    set-level suppression logic map](sending-email-suppression-list-config-level.md "sending-email-suppression-list-config-level.md") will help you understand the effects
    of the override combinations. These multitiered selections of overrides can be
    combined to implement three different levels of suppression:
    1. **Use account-level suppression:** Do not override
       your account-level suppression and do not implement any configuration
       set-level suppression - basically, any email sent using this
       configuration set will just use your account-level suppression. To do
       this:
       1. In **Suppression list settings**, uncheck the
          **Override account level settings**
          box.

    2. **Do not use any suppression:** Override your
       account-level suppression without enabling any configuration set-level
       suppression - this means any email sent using this configuration set
       will not use any of your account-level suppression; in other words, all
       suppression is cancelled. To do this:
       1. In **Suppression list settings**, check the
          **Override account level settings**
          box.
       2. In **Suppression list**, uncheck the
          **Enabled** box.

    3. **Use configuration set-level suppression:** Override
       your account-level suppression with custom suppression list settings
       defined in this configuration set - this means any email sent using this
       configuration set will only use its own suppression settings and ignore
       any account-level suppression settings. To do this:
       1. In **Suppression list settings**, check the
          **Override account level settings** box.
       2. In **Suppression list**, check
          **Enabled**.
       3. In **Specify the reason(s)...**, select one
          of the suppression reasons for this configuration set to
          use.

7.  **Virtual Deliverability Manager options** – This section will only be present
    if you have Virtual Deliverability Manager features enabled. Here, you can define custom settings for how
    this configuration set will use engagement tracking and optimized shared delivery by overriding how they’ve been
    defined in your Virtual Deliverability Manager settings at the account level:
    1. To disable both engagement tracking and optimized shared delivery for this configuration set:
       1. Check the **Override account level settings**
          box.
       2. Ensure **Enabled** is unchecked for both
          _Engagement tracking_ and _Optimized shared delivery_,
          then choose **Save changes**.

    2. To enable or disable either, or both, engagement tracking and optimized shared delivery for this
       configuration set:
       1. Check the **Override account level settings**
          box.
       2. Check or uncheck **Enabled** for either or
          both _Engagement tracking_ and _Optimized shared delivery_,
          then choose **Save changes**.

    3. To revert back to your Virtual Deliverability Manager account level settings for engagement tracking and optimized shared delivery
       for this configuration set:
       1. Uncheck the **Override account level
          settings** box, then choose **Save
          changes**.

8.  **Archiving options** – This section provides the
    option to archive email sent from this configuration set:
    1. Select the **Enabled** check box.
    2. Click inside the **Archive** field and select an
       archive from the list followed by **Save changes**, or
       choose **Create archive** and continue with the
       remaining steps.
    3. Enter a unique name in the **Archive name**
       field.
    4. (Optional) Select a retention period in the **Retention
       period** field to override the default retention period of
       180 days.
    5. (Optional) You can encrypt your archive either by entering your own
       AWS KMS key into the **KMS key ARN** field, or by
       selecting **Create an AWS KMS key**.
    6. Choose **Create archive**.

9.  **Tags** – In this section, you can optionally add one
    or more tags to your configuration set:
    1. Choose **Add new tag**.
    2. Enter the tag **Key**.
    3. Enter the tag **Value** (optional).To remove a tag you've entered, choose **Remove** for that
       tag. You can enter a maximum of 50 tags.

10. Choose **Create set** to create your configuration
    set.

Now that you’ve created your configuration set, you have the option to define event
destinations for your configuration set which enables event publishing that is triggered
on the event types you specify for the event destination. A configuration set can have
multiple event destinations with multiple event types defined. See [Creating Amazon SES event destinations](event-destinations-manage.md "event-destinations-manage.md").

## Create a configuration set (AWS CLI)

You can create a configuration set using a JSON file as input to the `aws sesv2
 create-configuration-set` command in the AWS CLI.

1. ###### Create a CLI input JSON file

Use your favorite file editing tool to create a JSON file with the following
keys, plus values that are valid for your environment, or use the SES API
v2 `aws sesv2 create-configuration-set` command with the
`--generate-cli-skeleton` option with no value specified to print
a sample JSON structure to standard output.

This example uses a file named
`create-configuration-set.json`:

```
{
    "ConfigurationSetName": "`sample-configuration-set`",
    "TrackingOptions": {
        "CustomRedirectDomain": "`some.domain.com`",
        "HttpsPolicy": "`REQUIRE`"
    },
    "DeliveryOptions": {
        "TlsPolicy": "`REQUIRE`",
        "SendingPoolName": "`sending pool`",
        "MaxDeliverySeconds": `300`
    },
    "ReputationOptions": {
        "ReputationMetricsEnabled": `true`,
        "LastFreshStart": `timestamp`
    },
    "SendingOptions": {
        "SendingEnabled": `true`
    },
    "Tags": [
        {
            "Key": "`tag key`",
            "Value": "`tag value`"
        }
    ],
    "SuppressionOptions": {
        "SuppressedReasons": [`"BOUNCE","COMPLAINT"]`
    },
    "ArchivingOptions": {
        "ArchiveArn": "arn:aws:ses:`us-east-1`:`123456789012`:mailmanager-archive/`MyArchiveID`"
    }
}
```

###### Note

    * You must include the `file://` notation
     at the beginning of the JSON file path.
    * The path for the JSON file should follow the appropriate
     convention for the base operating system where you are running
     the command. For example, Windows uses the backslash (\) to
     refer to the directory path, and Linux uses the forward slash (/).

2. Run the following command, using the file you created as input.

```
aws sesv2 create-configuration-set --cli-input-json file://`create-configuration-set.json`
```

###### Note

To review the AWS CLI reference for this command, see [create-configuration-set](../../../cli/latest/reference/sesv2/create-configuration-set.md "../../../cli/latest/reference/sesv2/create-configuration-set.md").
