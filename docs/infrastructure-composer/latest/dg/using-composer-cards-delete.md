

# Delete cards in Infrastructure Composer
<a name="using-composer-cards-delete"></a>

This section provides instructions for deleting cards in AWS Infrastructure Composer.

## Enhanced component cards
<a name="using-composer-cards-delete-enhanced-card"></a>

To delete an enhanced component card, select a card you have place on the visual canvas. From the **Card actions** menu, select **Delete**.

![An enhanced component card with its Card actions menu displayed and the Delete option shown.](http://docs.aws.amazon.com/infrastructure-composer/latest/dg/images/aac-enhanced-delete.png)


## Standard component cards
<a name="using-composer-cards-use-standard-resource-delete"></a>

To delete standard component cards, you must manually remove the infrastructure code for each CloudFormation resource from your template. The following is a simple way to accomplish this:

1. Take note of the logical ID for the resource to delete.

1. On your template, locate the resource by its logical ID from the `Resources` or `Outputs` section.

1. Delete the resource from your template. This includes the resource logical ID and its nested values, such as `Type` and `Properties`.

1. Check the **Canvas** view to verify that the resource has been removed from your canvas.