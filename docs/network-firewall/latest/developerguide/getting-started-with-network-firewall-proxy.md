# Getting started with Network Firewall Proxy

###### Note

Network Firewall Proxy is in public preview release and is subject to change.

AWS Network Firewall Proxy provides network traffic filtering and protection for your applications hosted in Amazon VPCs and on-premises environment. This tutorial provides steps for getting started with Network Firewall Proxy using the AWS Management Console. You can also use Network Firewall API operations to create and manage your firewalls. For more information about working with Network Firewall API operations, see the _AWS Network Firewall Proxy Reference._

## Before you begin

This tutorial walks you through the steps required to configure your Proxy in the same VPC as your application., like the one depicted in the [Architecture overview](proxy-architecture-overview.md "proxy-architecture-overview.md").

To follow this tutorial, you'll need a test VPC where you want to configure a Network Firewall Proxy . Additionally, ensure you have set up all the prerequisites until pre-requisite step 4 (setting up trust) as mentioned in the [Pre-requisites](proxy-pre-requisites.md "proxy-pre-requisites.md").

## High-level steps for implementation

Setting up Network Firewall Proxy involves the following main configuration steps:

1. Create Rule Groups – Create rules to define your security controls, specifying which phase each rule should be applied in (pre-DNS, pre-request, or post-response). You can create multiple rules within each rule group to handle different security requirements.
2. Configure Proxy Configuration – Set up your proxy configuration by defining default (catch-all) rules for each phase (pre-DNS, pre-request, or post-response) and attaching the relevant rule groups created in step 1. This configuration establishes the processing order and priority for rule evaluation.
3. Create Proxy – While creating the proxy, you must select the NAT Gateway that it is created on. The Proxy uses this NAT Gateway for network address translation
4. Test and validate the proxy behavior
5. Monitor logs and metrics for proper operation

These steps work together to create a complete proxy configuration that processes and secures your outbound traffic according to your security policies.

## Step 1. Creating Rule Groups

A Rule Group in VPC proxy is a reusable collection of ordered access control rules (ACLs) used to evaluate and filter HTTP/s traffic. For information about Rule Groups, see [Managing Your Rule Groups](managing-proxy-rule-groups.md "managing-proxy-rule-groups.md").

###### To create a Rule Group

1.  Sign in to the AWS Management Console and open the Amazon VPC console.
2.  In the navigation pane, under **Network Firewall Proxy**, choose **Proxy rule groups**.
3.  Choose **Create rule group.**
4.  Enter a name.
5.  Optionally enter the description for your Rule Group and add a tag.
6.  Click Next.
7.  Enter the phase to which this rule would apply. If you want the rule to apply to all 3 phases, select all 3 phases (Note: This will create 3 different rules for each phase).
8.  Next, enter the action that you would like to take on the traffic. This can be allow, deny or alert.
9.  Optionally, enter a description for the rule.
10. Enter the conditions, operators and values. Condition operators will be used to define how to perform a match. This is similar to how conditions are defined in AWS IAM service. For more details, look [here](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md"). Condition keys define what is to be matched. Condition value specifies the exact value that needs to be matched against. For example, if you want to deny traffic for certain social media sites, you would define the following:

        * Rule group name: Deny social media.

    Create a rule with the following

        * Action: deny.
        * Description: Rule that will deny if requests attempt to go to social media websites.
        * ConditionOperator: "StringLike"
        * ConditionKey: "request:DestinationDomain"
        * "ConditionValues": [
         \*facebook.com,
         \*instagram.com,
         wa.com,
         whatsapp.net,
         whatsapp.com,
         x.com
         ]

11. Click next
12. Review the details and click Create

## Step 2. Creating Proxy Configuration

Proxy configurations use rule groups and other settings to define the traffic filtering behavior for a Proxy. In this procedure, you'll create a Proxy configuration using the rule groups that you created in the previous step. For information, see [Managing Your Proxy Configuration](managing-proxy-configuration.md "managing-proxy-configuration.md").

###### To create a Proxy configuration

1. Sign in to the AWS Management Console and open the Amazon VPC console.
2. In the navigation pane, under **Network Firewall Proxy**, choose Proxy configuration
3. Choose Create Proxy configuration
4. Enter a name, optionally enter a description
5. Under default action, choose an action for each phase of the traffic. This will determine what will happen to traffic incase it does not match any rules.
6. Optionally add a tag
7. Click next
8. Click on attach rule group
9. Set a priority for the rule group. Lower the number means higher the priority.
10. Select the rule group that you created in the last step from the drop down.
11. Click Attach.
12. Check to make sure your rule group shows up in the attach rule group screen and click next.
13. Review the details and click create.

## Step 3. Creating Proxy

Configure and deploy Proxy with NAT Gateway associations.
A proxy configuration serves as the container for your filtering rules and settings. You create the configuration first. Then you attach it to one or more NAT gateways to enable traffic inspection.

Note: If the proxy creation fails and you need to attach another proxy to the NAT Gateway, you will need to delete the proxy resource that failed and then try to attach a new proxy.

###### To create a Proxy

1. Sign in to the AWS Management Console and open the Amazon VPC console.
2. In the navigation pane, under **Network Firewall Proxy**, choose Proxy
3. Enter a name.
4. Add the proxy configuration that you created in the previous step from the dropdown.
5. Attach to the right NAT Gateway.
6. Optionally, if you want to perform TLS interception on your traffic to filter on attributes in the HTTP header, check the box to enable TLS intercept mode. These are optional values you can enter:
   1. TLS interception + PCM
   2. Listener ports
   3. AWS account number
   4. Logging configuration
   5. Tags

7. Select a certificate (in PCA) from the dropdown with which the Proxy can establish trust with your applications.
8. Under VPC settings, select the NAT GW ARN from the dropdown that you want to associate the Proxy with.
9. Next, Enter the listener ports, usually it would be 8080 and 443 for HTTP and HTTPS traffic.
10. Next, enter your AWS account number.
11. Optionally, add tags.
12. Click Next.
13. Review the details and click Create.

Your configuration is now complete. You can setup your proxy variables on the workloads as mentioned in [Pre-requisites](proxy-pre-requisites.md "proxy-pre-requisites.md") and send traffic from your VPCs and test out the proxy.
