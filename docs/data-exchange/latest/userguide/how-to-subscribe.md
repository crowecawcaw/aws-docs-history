

# Subscribing to AWS Data Exchange Heartbeat on AWS Data Exchange
<a name="how-to-subscribe"></a>

The following procedure shows how to browse the AWS Data Exchange catalog to find and subscribe to AWS Data Exchange Heartbeat.

**To find and subscribe to AWS Data Exchange Heartbeat**

1. Open and sign in to the [AWS Data Exchange console](https://console.aws.amazon.com/dataexchange).

1. From the left navigation pane, under **Discover data products**, choose **Browse catalog**.

1. From the search bar, enter **AWS Data Exchange Heartbeat** and press **Enter**.

1. Choose the **AWS Data Exchange Heartbeat** product to view its details page.

   1. (Optional) To view the data dictionary, scroll down to the product **Overview** section to see the data dictionary under **Data dictionaries**.

   1. (Optional) To download the data dictionary, choose the **Data dictionary and samples** tab, choose the option button next to **Data dictionary**, and then choose **Download**.

   1. (Optional) To download the sample, choose the option button next to the sample name (**Heartbeat manifest sample.json**), and then choose **Download**.

1. In the top right corner, choose **Continue to subscribe**. 

1. Choose your preferred price and duration combination, choose whether to enable auto-renewal for the subscription, and review the offer details, including the data subscription agreement.
**Note**  
AWS Data Exchange Heartbeat doesn't require subscription verification, but some products do. For more information, see [Subscription verification for subscribers in AWS Data Exchange](subscription-verification-sub.md).

1. Review the pricing information, choose the pricing offer, and then choose **Subscribe**.
**Note**  
AWS Data Exchange Heartbeat is a free product. If you subscribe to a paid product, you are prompted to confirm your decision to subscribe.

1. On the **Set up your first export** page, select the check boxes for the data sets containing the revisions you would like to export. Selecting a data set will prepare its most recently published revision to be exported.

1. Choose an Amazon S3 bucket location or configure an Amazon S3 key naming pattern. This will determine where your revisions will be exported. For more information about using key patterns, see [Key patterns when exporting asset revisions from AWS Data Exchange](revision-export-keypatterns.md).

1. Choose **Export** to export the data to Amazon S3, or choose **Skip** if you'd rather wait and export or download later.

**Note**  
It can take a few minutes for your subscription to become active after you choose **Subscribe**. If you choose **Export** before the subscription is active, you are prompted to wait until it is complete. After your subscription is active, your export will begin.  
Navigating away from this page prior to your subscription becoming active will not prevent the subscription from processing. It will prevent your data export from occurring.