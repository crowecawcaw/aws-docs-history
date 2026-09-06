

# Download the Direct Connect LOA-CFA
<a name="download-loa-cfa"></a>

You can download the LOA-CFA using either the Direct Connect console or through the command line. Once you've downloadeded the LOA-CFA and provided that to your network or colocation provider, that provider can order the cross-connect for you.

**To download the LOA-CFA**

1. Open the **Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home).

1. In the navigation pane, choose **Connections**.

1. Select the connection, and then choose **View details**.

1. Choose **Download LOA-CFA**. 
**Note**  
If the link is not enabled, the LOA-CFA is not yet available for you to download. A Support case will be created requesting additional information. Once you've responded to the request, and the request processed, the LOA-CFA will be available for download. If it's still unavailable, contact [AWS Support](https://aws.amazon.com/support/createCase).

1. Send the LOA-CFA to your network provider or colocation provider so that they can order a cross connect for you. The contact process can vary for each colocation provider. For more information, see [Requesting cross connects at Direct Connect locations](Colocation.md).

**To download the LOA-CFA using the command line or API**
+ [describe-loa](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-loa.html) (AWS CLI)
+ [DescribeLoa](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLoa.html) (Direct Connect API)