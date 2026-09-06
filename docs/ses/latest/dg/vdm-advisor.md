

# Virtual Deliverability Manager advisor
<a name="vdm-advisor"></a>

The *Virtual Deliverability Manager advisor* helps to optimize your email deliverability and engagement by identifying key performance and infrastructure issues at the account and sending identity levels that are adversely affecting your email deliverability and reputation. It provides solutions by providing specific guidance on how to resolve the identified issue.

Advisor’s infrastructure recommendations are listed in the *Open recommendations* table. The recommendations identify standard email authentication problems, such as when SPF, DKIM, DMARC, or BIMI records don’t exist or have problems with their configuration such as being malformed or having a key length that's too short. They're categorized by severity of *Impact*, *Identity name* of the sending domain, and the *Age* of the alert. In the search bar, a list box provides the option to filter on impact level, infrastructure category, or sending identity name. The *Last checked* column shows a relative time of when the recommendation was last updated, such as "Just now" or "15 minutes ago". The last column, *Resolve issue*, provides a link to the relevant section in the Amazon SES Developer Guide with guidance about how to resolve the identified issue.

Open recommendations display in the Virtual Deliverability Manager advisor sorted by impact level.

![Open recommendations displayed in the Virtual Deliverability Manager advisor sorted by impact level.](http://docs.aws.amazon.com/ses/latest/dg/images/vdm_advisor_overview.png)


If you don't have any ongoing advisor notifications, a message will indicate that you don’t have any open recommendations. We recommend that you check the advisor on a regular basis. Optionally, you can integrate these advisor notification events with Amazon EventBridge to build scalable event-driven applications as explained in [Monitoring SES events using Amazon EventBridge](monitoring-eventbridge.md).

You can also access the *Resolved recommendations* table from the Virtual Deliverability Manager advisor page, which lists infrastructure issues that you’ve resolved by implementing the advisor's guidance. Resolved recommendations are listed with an initial status that describes the issue before it was resolved. Resolved recommendations expire after 30 days.

If you have global deliverability enabled, the advisor also generates recommendations when your monitored domains or IPs are listed on a blocklist. These recommendations include the blocklist name, listing reason, and delisting guidance. For more information, see [Blocklists](vdm-gd-blocklists.md).

## What the Virtual Deliverability Manager advisor's looking for
<a name="vdm-advisor-checks"></a>

In the previous section we discussed that Virtual Deliverability Manager's advisor performs checks against your sending domain to determine if you've configured a safely authenticated infrastructure to ensure you maintain a high rate of email deliverability and maintain a good sender reputation. Before you activate the Virtual Deliverability Manager advisor, we think it would be helpful for you to know exactly what the advisor's checking and what it's looking for in those checks.

You can use this table as a reference to go through your sending domain's configuration and correct any of these elements that are not aligned to the standards listed in this table before they become problems that the advisor has to alert you to.


| Type of check | Advisor message | Why the advisor's alerting you | Learn more | 
| --- | --- | --- | --- | 
| Complaint rate check | {{ISP\_name}} ISP has {{high/med/low}} complaint rate. | Identity has exceeded complaint recommendations threshold for this ISP. | [Monitoring sender reputation](monitor-sender-reputation.md) | 
| DKIM configuration | DKIM verification is not enabled. | DKIM is not enabled per identity. | [Easy DKIM in SES](send-email-authentication-dkim-easy.md) | 
| DKIM key strength | DKIM signing key length is below 2048 bits. | DKIM signing key length is not using at least 2048 bits. | [Easy DKIM in SES](send-email-authentication-dkim-easy.md) | 
| DKIM DNS record validation | DKIM verification has failed. | DKIM CNAME records determined invalid after looking up and trying to validate the key. | [Verifying a DKIM domain identity with your DNS provider](creating-identities.md#just-verify-domain-proc) | 
| DMARC configuration | DMARC configuration was not found. | DMARC TXT records are missing. | [Setting up the DMARC policy on your domain](send-email-authentication-dmarc.md#send-email-authentication-dmarc-dns)  | 
| DMARC DNS record format check | DMARC configuration could not be parsed. | Invalid format found for DMARC TXT records.  | [Setting up the DMARC policy on your domain](send-email-authentication-dmarc.md#send-email-authentication-dmarc-dns) | 
| DMARC's DKIM configuration | DKIM record was not found. | No DKIM record was found in order to comply with DMARC. | [Complying with DMARC through DKIM](send-email-authentication-dmarc.md#send-email-authentication-dmarc-dkim) | 
| DMARC's DKIM configuration | DKIM record is not aligned. | The domain specified in the DKIM signature does not align (match) with the domain in the From address. | [Complying with DMARC through DKIM](send-email-authentication-dmarc.md#send-email-authentication-dmarc-dkim) | 
| SPF configuration | SPF record was not found. | SPF TXT record missing for Custom MAIL FROM domain. | [Configuring your custom MAIL FROM domain](mail-from.md#mail-from-set) | 
| SPF "include" configured | SPF record for Amazon SES was not found. | include:amazonses.com is missing from SPF TXT record. | [Configuring your custom MAIL FROM domain](mail-from.md#mail-from-set) | 
| SPF enforcement configured | SPF all qualifier is missing. | \~all is missing from SPF TXT record. | [Configuring your custom MAIL FROM domain](mail-from.md#mail-from-set) | 
| SPF enforcement validation | An SPF configuration issue was found. | Attempts to detect the required SPF MX record within 72 hours failed. | [Custom MAIL FROM domain setup states](mail-from.md#mail-from-states)  | 
| BIMI configured | BIMI record not found or configured without default selector. | BIMI TXT records are missing or lack the selector attribute. | [Setting up BIMI](send-email-authentication-bimi.md#bimi-setup-procedure) | 
| BIMI format validation | BIMI has malformed TXT record. | BIMI TXT record determined as misconfigured after checking for the presence and valid format of: version, certificate URL, and logo URL. | [Setting up BIMI](send-email-authentication-bimi.md#bimi-setup-procedure) | 

## Using the Virtual Deliverability Manager advisor in the Amazon SES console
<a name="vdm-advisor-console"></a>

The following procedure shows you how to use the Virtual Deliverability Manager advisor in the Amazon SES console to resolve identified deliverability issues using the Amazon SES console.

**To use the Virtual Deliverability Manager advisor to resolve deliverability and reputation issues**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation pane, choose **Advisor** under **Virtual Deliverability Manager**.
**Note**  
**Advisor** will not be visible if you haven't enabled Virtual Deliverability Manager for your account. For more information, see [Getting started with Virtual Deliverability Manager](vdm-get-started.md).

1. The **Open recommendations** table displays by default. Recommendations are categorized by **Impact** (High/Low), **Identity name** (sending domain), **Age** (of the alert), and **Recommendation/Description** (identified issue). In the search bar, filter on the **Impact** level, the infrastructure issue **Category**, or the **Identity name** of the sending domain.

1. To remediate a problem that's described in the **Recommendation/Description** column, choose the link in the **Resolve issue** column for that row, and implement the suggested solution.
**Note**  
After you implement a solution, the resolved issue can take up to six hours to be reflected. You can view the resolved issue on the **Resolved recommendations** tab.

## Accessing your Virtual Deliverability Manager recommendations using the AWS CLI
<a name="vdm-advisor-cli"></a>

The following examples show you how to access your Virtual Deliverability Manager recommendations using the AWS CLI.

**To access your Virtual Deliverability Manager recommendations using the AWS CLI**  
You can use the [`ListRecommendations`](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_ListRecommendations.html) operation in the Amazon SES API v2 to list your deliverability recommendations. You can call this operation from the AWS CLI, as shown in the following examples.
+ List the recommendations to see deliverability issues:

  ```
  aws --region us-east-1 sesv2 list-recommendations
  ```
+ Apply filters to retrieve recommendations for a specific domain that you own:

  ```
  aws --region us-east-1 sesv2 list-recommendations --cli-input-json file://list-recommendations.json
  ```
+ The input file looks similar to this:

  ```
  {
    "PageSize":100,
    "Filter":{
      "RESOURCE_ARN": "arn:aws:ses:us-east-1:123456789012:identity/example.com"
     }  
  }
  ```