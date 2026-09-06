

# Delete a portal in AWS IoT SiteWise
<a name="portal-delete-portal"></a>

**Note**  
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

You might delete a portal if you created it for testing purposes or if you created a duplicate of a portal that already exists.

**Note**  
You must first manually delete all dashboards and projects in a portal before you can delete a portal. For more information, see [Deleting projects](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/delete-projects.html) and [Deleting dashboards](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/delete-dashboards.html) in the *SiteWise Monitor Application Guide*.

1. On the portal details page, choose **Delete**.
**Important**  
When you delete a portal, you lose all projects that the portal contains, and all dashboards in each project. This action can't be undone. Your asset data isn't affected.  
![Portal details page with Delete highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sitewise-delete-portal-console.png)

1. In the **Delete portals** dialog box, choose **Remove admins and users**.

   You must remove the administrators and users from a portal before you can delete it. If your portal doesn't have administrators or users, the button doesn't appear, and you can skip to the next step.  
!["Delete portals" dialog box with "Remove administrators and users" highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sitewise-delete-portal-remove-users-console.png)

1. If you're sure that you want to delete the entire portal, enter **delete** in the field to confirm deletion.  
!["Delete portals" dialog box with "Delete" highlighted.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sitewise-delete-portal-confirm-delete-console.png)

1. Choose **Delete**.