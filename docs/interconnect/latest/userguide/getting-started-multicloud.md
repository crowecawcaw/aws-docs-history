# Getting started with AWS Interconnect - multicloud

## Plan your network architecture

- Decide whether to use a Virtual private gateway, Transit Gateway, or Cloud WAN. Virtual private gateways and Transit Gateways are Regional networking services that can be used only with a multicloud Interconnect provisioned in the local interconnection point to the other CSPs serving that Region. Cloud WAN is a global networking service which can reach any Interconnect globally.
- Review your existing IP address allocations to ensure no conflicts.
- Create a new Direct Connect gateway or repurpose an existing one for use with your new multicloud Interconnect.

## Create your first multicloud Interconnect starting from the AWS Console

1. Go to the AWS Direct Connect Console and navigate to AWS Interconnect on the left side navigation menu.
2. Select **Create new multicloud Interconnect**.
3. Select your other cloud services provider (CSP). CSPs in Public Preview will include a "Preview" tag in their card.

###### Note

Previews are limited to one Interconnect per customer per supported Region. The connection can be used at no cost for the duration of Preview. At the time AWS Interconnect goes Generally Available with a CSP, any preview 1Gbps connections will be removed from your account. Use of Preview services is governed by the [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/"), including the terms regarding access to "Betas and Previews." 4. Select your source AWS Region where your workload is located and destination region on the other CSP. Your choice of AWS region determines the physical infrastructure where your Interconnect will be placed and it will be considered the Local Region for your Interconnect. However, your Interconnect can reach workloads in remote AWS Regions when using Cloud WAN. 5. Provide a name or description for your new interconnect, select your required bandwidth (limited to 1Gbps with any CSPs currently in Public Preview), specify an existing Direct Connect gateway to serve as the attach point for the new multicloud Interconnect or create a new one using the "Create Direct Connect gateway" button in the same screen, and provide your ID on the other CSP. This ID is used by AWS and the other CSP to identify you as the requestor of a new Interconnect, and correspond to the ownership construct where your new Interconnect will be placed on other CSP. In the case of Google Cloud, you require a project ID. The project ID is a unique string that can be a combination of letters, numbers, and hyphens, between 6 and 30 characters in length. In the case of Oracle Cloud Infrastructure, you require a Tenancy OCID in the format `ocid1.tenancy.oc1..<unique_ID>`. You can optionally apply a tag to your new interconnect. Choose **Next** when you have provided all the necessary information. 6. On the following screen, you can review the details of your new multicloud Interconnect. Choose **Finish** to request the new interconnect. 7. At this point AWS will request the creation of the new multicloud Interconnect to the other CSP and display the activation key you will use to complete the process on the other CSP. 8. To complete the creation process use the Activation key following the instructions provided by your other CSP. In the case of CSPs in Public Preview, you might need to use the CLI to complete the Activation flow. Review the relevant documentation. 9. Once you have activated the other CSP, the creation process will complete with the attachment of the new Interconnect to the Direct Connect gateway you specified. 10. Use the main AWS Interconnect view in the AWS Direct Connect Console to review a list of all your Interconnects.

## Accepting a new multicloud Interconnect created from another CSP using the AWS Console

1. Go to the AWS Direct Connect Console and navigate to AWS Interconnect on the left side navigation menu.
2. Select **Accept multicloud Interconnect**.
3. Enter into the text field the Activation key generated on the other CSP as part of create action and select **Next**.
4. Provide a name or description for your new interconnect. Specify an existing Direct Connect gateway to serve as the attach point for the new multicloud Interconnect. You can optionally apply a tag to your new interconnect. Choose **Next** to continue the accept action.
5. On the following screen, you can review the details of the new multicloud Interconnect that was requested from the other CSP. Choose **Finish** to accept the new multicloud Interconnect.
