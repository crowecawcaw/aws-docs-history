

# Getting started with Mail Manager
<a name="eb-getting-started"></a>

To start using Amazon SES Mail Manager you can use the *Get started with Mail Manager* wizard in the Amazon SES console, where you'll create an ingress endpoint and configure it with a traffic policy and rule set.

An ingress endpoint is your first building block in setting up Mail Manager—it’s a key infrastructure component that utilizes:
+ **Traffic policies** – A traffic policy contains policy statements that you define to sort the incoming mail by allowing or blocking specific types of email when the policy statement’s conditions are met. 
+ **Rule sets** – A rule set contains rules that you define to perform actions on the email you allow in when the rule’s conditions are met.

However, part of creating an ingress endpoint is selecting a traffic policy and a rule set that have already been created and then assigning them to the ingress endpoint. The steps in the following procedure will walk you through the correct order of configuring your first ingress endpoint. 

## Getting started with Mail Manager using the SES console
<a name="eb-get-started-console"></a>

The following procedure shows you how to get started with Mail Manager using the SES console.

**To get started with Mail Manager using the Amazon SES console**

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/).

1. In the left navigation panel, choose **Mail Manager** and select any of the **Get started with Mail Manager** buttons on the **Mail Manager overview** page.

1. On the *Get set up* page, select **Create traffic policy** on the *Create a traffic policy* card.

   1. Complete the workflow on the *Create a traffic policy* page. If you need additional information, see [Creating traffic policies and policy statements in the SES console](eb-filters.md#eb-filters-create-console). 

   1. After creating your first traffic policy and policy statements, use your browser's back button to return to the *Get set up* page or select **Get set up** under *Mail Manager* in the left navigation panel.

1. On the *Get set up* page, select **Create rule set** on the *Create a rule set* card.

   1. Complete the workflow on the *Create a rule set* page. If you need additional information, see [Creating rule sets and rules in the SES console](eb-rules.md#eb-rules-create-console). 

   1. After creating your first rule set and rules, use your browser's back button to return to the *Get set up* page or select **Get set up** under *Mail Manager* in the left navigation panel.

1. Now that you've created your first traffic policy and rule set, you'll be able to create your first ingress endpoint. On the *Get set up* page, select **Create ingress endpoint** on the *Create an ingress endpoint* card.

   1. Part of the workflow on the *Email ingress endpoint* page will be to assign the traffic policy and rule set you just created to the ingress endpoint. If you need additional information, see [Creating an ingress endpoint in the SES console](eb-ingress.md#eb-ingress-create-console). 

With your first ingress endpoint created, you can start using Mail Manager and utilize its other features such as SMTP relays and email archiving. You can also create additional ingress endpoints with unique traffic policies and rule sets to further customize how you manage all of your incoming email.