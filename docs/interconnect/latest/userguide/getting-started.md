# Getting started with AWS Interconnect

## Plan your network architecture

- Decide whether to use a Virtual private gateway, Transit Gateway, or Cloud WAN. Virtual private gateways and Transit Gateways are Regional networking services that can be used only with a multicloud
  Interconnect provisioned in the local interconnection point to Google Cloud serving that Region. Cloud WAN is a global networking service which can reach any Interconnect globally.
- Review your existing IP address allocations to ensure no conflicts.
- Create a new Direct Connect gateway or repurpose an existing one for use with your new multicloud Interconnect.

## Create your first multicloud Interconnect starting from the AWS Console

1. Go to the AWS Direct Connect Console and navigate to AWS Interconnect on the left side navigation menu.
2. Select **Create new multicloud Interconnect**.
3. Select Google Cloud as your provider.
4. Select your source AWS Region where your workload is located and destination region in Google Cloud.
5. Provide a name or description for your new interconnect, select your required bandwidth (limited to 1Gbps during Public Preview), specify an existing Direct Connect gateway to serve as the attach point
   for the new multicloud Interconnect, and provide the Google Cloud project ID. The project ID is a unique string that can be a combination of letters, numbers, and hyphens, between 6 and 30 characters in
   length. You can optionally apply a tag to your new interconnect. Choose **Next** when you have provided all the necessary information.
6. On the following screen, you can review the details of your new multicloud Interconnect. Choose **Finish** to request the new interconnect.
7. At this point AWS will request the creation of the new multicloud Interconnect to Google Cloud and display the activation key you will use to complete the process on Google Cloud.
8. To complete the creation process use the Activation key following the instructions on Google Cloud.
9. Once you have activated the new Interconnect on Google Cloud, the creation process will complete with the attachment of the new Interconnect to the Direct Connect gateway you specified.
10. Use the main AWS Interconnect view in the AWS Direct Connect Console to review a list of all your Interconnects.

## Accepting a new multicloud Interconnect created from Google Cloud using the AWS Console

1. Go to the AWS Direct Connect Console and navigate to AWS Interconnect on the left side navigation menu.
2. Select **Accept multicloud Interconnect**.
3. Enter into the text field the Activation key generated on Google Cloud as part of create action and select **Next**.
4. Provide a name or description for your new interconnect. Specify an existing Direct Connect gateway to serve as the attach point for the new multicloud Interconnect. You can optionally apply a tag to
   your new interconnect. Choose **Next** to continue the accept action.
5. On the following screen, you can review the details of the new multicloud Interconnect that was requested from Google Cloud. Choose **Finish** to accept the new multicloud Interconnect.
