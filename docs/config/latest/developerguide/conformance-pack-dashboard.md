# Viewing Compliance Data in the Conformance Packs Dashboard for AWS Config

The main page for **Conformance Packs** displays all of the conformance
packs that you currently have in your AWS account. The page also contains the name,
deployment status, and compliance score of each conformance pack. A compliance score is the
percentage of the number of compliant rule-resource combinations in a conformance pack
compared to the number of total possible rule-resource combinations in the conformance
pack.

You can use this dashboard to understand the level of compliance of your conformance packs
and use the compliance score to track remediation progress, perform comparisons across
different sets of requirements, and see the impact a specific change or deployment has on a
conformance pack.

## Navigating the Conformance Packs Main Page

1. Sign in to the AWS Management Console and open the AWS Config console at
   [https://console.aws.amazon.com/config/home](https://console.aws.amazon.com/config/home "https://console.aws.amazon.com/config/home").
2. Navigate to the **Conformance packs** page. Review your
   conformance packs and their compliance score. You can also do the
   following:
   - To add and configure a new conformance pack, choose **Deploy
     conformance pack**.
   - To delete a conformance pack and its data, change the configuration
     settings, or view additional details, such as the delivery location or
     parameters, choose a conformance pack and choose
     **Actions**.

   ###### Note

   You cannot edit a deployed conformance pack. You can modify the
   other selections at any time by choosing the name of the conformance
   pack and **Edit** in the
   **Actions** dropdown.
   - To view the history of compliance state changes, choose a conformance
     pack and choose **Conformance pack timeline**. For more
     information, see [Viewing
     the Compliance History Timeline for Conformance
     Packs](compliance-history-conformance-pack.md "compliance-history-conformance-pack.md").
   - To view the deployment status, compliance score, compliance score
     timeline, and rules for a conformance pack in a detailed view, choose a
     conformance pack and choose **View**.
