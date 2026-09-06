

# Configuring Private Marketplace
<a name="configure-private-marketplace"></a>

You can create multiple Private Marketplace experiences with specific procurement controls and customized branding for different audiences in your organization. Private Marketplace provides a multi-step wizard for creating and configuring experiences.

**Topics**
+ [Configuring an experience](#configure-experience)
+ [Selecting audiences (optional)](#select-audiences)
+ [Selecting products (optional)](#select-products)
+ [Customizing branding (optional)](#configure-branding-settings)
+ [Reviewing and creating an experience](#review-and-create-experience)

**Note**  
You can skip the optional steps and update the experience after creation. If you skip the optional steps and use the default settings, your experience will be live without any approved products or associated audiences. Until you associate an audience with this experience, it will not take effect and govern any users. When associated with an audience, it will not allow the users in the audience to procure any products from AWS Marketplace. It will allow users to submit product procurement requests.

## Configuring an experience
<a name="configure-experience"></a>

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace/](https://console.aws.amazon.com/marketplace/).

   1. In the navigation pane, choose **Dashboard** under **Private Marketplace**.

   1. Choose **Create experience**.

1. Specify experience details such as name and description. This is the internal name and description used by administrators to keep track of this experience. End users will not see these fields.

   1. Enter a name for your experience.

   1. (Optional) Enter a description for your experience.

1. (Optional) Update status and requests

   1. By default, the experience will be created with **Live** status and will take effect when it is associated with an audience. Choose **Not live** as **Experience status** if you do not want the experience to take effect immediately.

   1. By default, product requests are enabled which allows users to request more products to be added to the experience. If you do not want to allow users to request products, choose disabled for **Product procurement requests**.

1. (Optional) Specify tags:

   A tag is a custom attribute label that you assign to an AWS resource. Use tags to identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related.

   1. Under **Tags**, choose **Add new tag**.

   1. Specify a key and, optionally, a value for the new tag.

## Selecting audiences (optional)
<a name="select-audiences"></a>

This step is optional. Note that your experience will not govern any users until it is set to **Live** status and associated with an audience.

**To select audiences**

1. Navigate the tree structure to choose your target audiences. The hierarchy shown reflects your organization structure, displaying the organizational units (OUs) and accounts that you manage in Organizations.

1. You can choose the entire organization, organizational units (OUs), or accounts. If you choose an audience that is directly associated with another experience, it will be disassociated from that experience and associated with the experience being created.

1. After making your selections, choose **Next**.

**Note**  
When choosing audiences, do not choose audiences at lower levels of a hierarchy if you have already chosen the audience at the higher level. Experiences flow down through the hierarchy - when applied at a higher level, all lower levels inherit it automatically. For example, if you have chosen an OU as the audience, do not choose the accounts under the OU, as they will automatically inherit the experience.
Choose an audience at a lower level only if you want to override its governance and not have it inherit from a higher level.

## Selecting products (optional)
<a name="select-products"></a>

This step is optional. If you do not select any products, your experience will be created with an empty catalog of approved products. If you use such an experience to govern users, they will not be allowed to procure any products from AWS Marketplace.

**To select products**

1. Choose the AWS Marketplace products you want to approve in the experience you are creating. Users in the audience associated with the experience will be allowed to subscribe to these products.

1. After making your selections, choose **Next**.

## Customizing branding (optional)
<a name="configure-branding-settings"></a>

This step is optional.

**To customize branding**

1. Enter a name and optional description for branding the experience you are creating. This name and description is shown to users on their **Your Private Marketplace** page. You can use these to provide details to your users about the Private Marketplace experience you are curating for them.

1. Choose **Next** to continue.

## Reviewing and creating an experience
<a name="review-and-create-experience"></a>

Review the settings for your Private Marketplace experience, and edit the settings as needed. When you are satisfied with your settings, choose **Create experience**.

Private Marketplace starts a Catalog API change set with multiple change types to create and set up the experience. You can track the changes in the **Change sets** page. Your experience is ready when the **CreateExperience** change set shows **Succeeded** status. Depending on your selections and the size of your organization, your change set can take up to a few hours to complete. To view the updates, refresh the console after processing is complete.