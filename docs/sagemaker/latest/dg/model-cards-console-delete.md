

# Delete a model card
<a name="model-cards-console-delete"></a>

Follow these steps to permanently delete one or more model cards.

1. Go to the Amazon SageMaker Model Cards console.

1. Check the box to the left of the name of the card(s) you want to delete.

1. Choose **Delete** in the upper right-hand corner.

1. Confirm your request to permanently delete one or more cards..

You can also delete a model card when viewing the model card overview in the console by choosing **Actions** and then **Delete model card**.

Within the SageMaker Python SDK, you can permanently delete a model card with the following command:

```
{{my_card}}.delete()
```