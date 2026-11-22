

# Managing EC2 Image Builder product availability by AWS Region and country

You choose the AWS Regions where buyers can deploy your product on the **Add Regions** card under **Step 2: Delivery configuration**. You choose the countries where buyers can purchase your product on the **Configure offer availability** step when you create the public offer. These two properties are similar, but they are not the same. For example, a buyer might be located in, and purchasing from, the United States, but they might be planning to install your product in the Europe (Frankfurt) Region. In order for this buyer to purchase your product, you must include both the United States in your list of countries, and the Europe (Frankfurt) Region in your list of Regions. You can use the following sections to update your product availability by Region and country.

**Topics**
+ [Add an AWS Region](#single-ib-adding-regions)
+ [Restrict an AWS Region](#single-ib-restricting-regions)
+ [Update support for future AWS Regions](#single-ib-updating-future-region-support)
+ [Update availability by country](#single-ib-update-availability-by-country)

## Add an AWS Region
<a name="single-ib-adding-regions"></a>

You can add a Region where buyers can use your product.

**To add Regions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. On the **Delivery** tab, in the **Region availability** section, choose **Add Regions**.

   For a new product, you can instead choose **Start** on the **Add Regions** card under **Step 2: Delivery configuration**.

1. In the **Choose Regions** table, select the Regions to add.

   Regions your product already supports are selected and can't be cleared.

1. (Optional) Under **Future Region support**, select **Enable future AWS Region support**, and then choose **Include all future US and non-US Regions** or **Limit to future US Regions only**.

1. (Optional) Under **Tags**, add tags to the change request.

1. Choose **Save Regions**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

**Note**  
To add an AWS GovCloud (US) Region, you need an active AWS GovCloud (US) account that AWS Marketplace has verified. If you don't have one, the request fails. When you select an AWS GovCloud (US) Region, the **AWS GovCloud (US) Region selection** alert appears. To request verification, choose **submit a support request** in the alert. For more information, see [Publishing an AMI product in AWS GovCloud (US)](https://docs.aws.amazon.com/marketplace/latest/userguide/govcloud-publishing.html#govcloud-publishing-ami).  
The **EC2 Image Builder component** delivery method isn't available in the AWS European Sovereign Cloud catalog.

**Note**  
When you add support for a new AWS Region, customers already subscribed to private offers for your product won't be able to access the newly added Region automatically. You must create another private offer with the Region you want customers to access. After accepting the new offer, customers can access the newly added Region. Customers who subscribe to your product at a future date can also access the Region, as long as the Region is included in the private offer. For more information about how to create a new private offer, see [Private offer upgrades, renewals, and amendments](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-upgrades-and-renewals.html).

## Restrict an AWS Region
<a name="single-ib-restricting-regions"></a>

To prevent new buyers from using your product in a specific AWS Region, you can restrict the Region. You can add the Region back at a later time. Existing subscribers of the product in the Region can continue using the product from the Region as long as they're subscribed.

**To restrict Regions**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Region availability** section, choose **Edit**, and then choose **Restrict Regions**.

   This option is available after your product has at least one version.

1. For **Restrict Regions**, choose the Regions to restrict.

   You must keep at least one Region available.

1. Choose **Restrict Regions**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

If your request is successful, your existing users receive the following email message notifying them of the Region to be restricted. They can continue using your product as long as they remain subscribed, but they can’t re-subscribe if they cancel the subscription.

```
Greetings from AWS Marketplace,

This message is a notification detailing a recent change for <ProductName>.
{{{sellerName}}} has opted to restrict the <ProductType> product in <Restricted Region(s)> beginning <DateOfChange>.

This impacts you in the following ways:

1. As long as you're subscribed to the product, you can continue using the software product in the restricted Region.
2. You can't begin new instances of the software product in the restricted Region.
3. You can continue using the software product in all available AWS Regions.

Regards,
The AWS Marketplace Team

AWS, Inc. is a subsidiary of Amazon.com, Inc. Amazon.com (http://amazon.com/) is a registered
trademark of Amazon.com, Inc. This message was produced and distributed by Amazon Web
Services Inc., 410 Terry Ave. North, Seattle, WA 98109-5210.
```

## Update support for future AWS Regions
<a name="single-ib-updating-future-region-support"></a>

If you want your product to be onboarded to newly launched AWS Regions, you can use **Update future Region support**.

**To update future Region support**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Delivery** tab.

1. In the **Region availability** section, choose **Edit**, and then choose **Update future Region support**.

   The **Add Regions** page opens.

1. Under **Future Region support**, do one of the following:
   + To turn on future Region support, select **Enable future AWS Region support**, and then choose **Include all future US and non-US Regions** or **Limit to future US Regions only**.
   + To turn off future Region support, clear **Enable future AWS Region support**.

1. Choose **Save Regions**.

Your change request appears on the product's **Change history** tab. Its status moves from **Preparing** to **Applying**, and then to **Succeeded** or **Failed**. To see why a request failed, choose the request name. While a request is in progress, the actions on the **Delivery** tab are unavailable.

## Update availability by country
<a name="single-ib-update-availability-by-country"></a>

To change the countries where buyers can subscribe to your product, use **Update availability by country**.

**To update availability by country**

1. Open the [**Products and services**](https://console.aws.amazon.com/partnercentral/products) page in AWS Partner Central, and sign in to your seller account.

1. Choose the product.

1. Choose the **Procurement** tab.

1. On the **Public offer** card, choose **Update**, and then choose **Update availability by country**.

   The **Update** menu appears after your public offer is released.

1. Under **Offer availability by country**, choose one of the following options:
   + **All countries** – Buyers in all countries can purchase your product.
   + **All countries with exclusions** – For **Excluded countries**, choose the countries where buyers can't purchase your product.
   + **Allowlisted countries only** – For **Allowlisted countries**, choose the countries where buyers can purchase your product.

   Availability by country applies only to your public offer. You can extend private offers to specific buyers even if they aren't in one of your allowlisted countries.

1. Choose **Submit**.

To track your request, choose the ID under **Offer ID** on the **Public offer** card, and then choose the **Requests log** tab. The **Request status** moves from **Under review** to **Update in progress**, and then to **Succeeded** or **Failed**. While a request is in progress, the **Update** menu is unavailable.