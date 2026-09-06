

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Moving an asset
<a name="moving-assets"></a>

Assets in a project can be grouped under various [sites](https://docs.aws.amazon.com/Monitron/latest/user-guide/site-management-chapterSM.html). If you need to re-organize your assets and sites, you can choose to move an asset from one site to another without having to create each asset again.

**Note**  
You can move assets from the project level to the site level. However, you can't move assets from the site level to the project level.

Once an asset is moved, it continues generating notifications in its new destination site. All positions associated with the asset move to the new site. However, it stops generating notifications and being visible to users in its older source site.

**Important**  
Only an user with admin access to *both* source and destination sites can move an asset.

**Topics**
+ [To move an asset on the web app](#asset-move-web)
+ [To move an asset on the mobile app](#asset-move-mobile)

## To move an asset on the web app
<a name="asset-move-web"></a>

1. From the web app's main menu, choose **Assets**.

1. Choose the asset that you want to move.

1. From the asset menu, choose **Actions**, and then choose **Move asset**.  
![Actions menu expanded showing Move asset option highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-move-1.png)

1. From the dialog box that opens, select a site to move your asset to from the **New site** dropdown menu, and then select **Move**.  
![Move Example_Asset dialog box with New site dropdown menu highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-move-2.png)  
![Move Example_Asset dialog box with Site 2 selected as new parent and Move button highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-move-4.png)

   The app displays a success message if your asset is moved successfully.

## To move an asset on the mobile app
<a name="asset-move-mobile"></a>

1. From the mobile app's main menu, choose **Assets**.

1. Choose asset that you want to move to a new site. Then, open the asset details menu.  
![Assets page showing two assets with No sensor status and vertical three-dot menu icons.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-mob-1.png)

1. From the asset details menu, choose **Move asset**.   
![Asset details menu with Move asset option highlighted.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-mob-2.png)

1. From the asset page, from **New site**, choose the new site you want to move the asset to. Then, choose **Move**.   
![Move asset dialog with Site dropdown menu and Move button highlighted in sequence.](http://docs.aws.amazon.com/Monitron/latest/user-guide/images/asset-mob-3.png)

   The app displays a success message if your asset is moved successfully.