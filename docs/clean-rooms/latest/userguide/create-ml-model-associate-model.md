

# Associating a configured lookalike model
<a name="create-ml-model-associate-model"></a>

After you have configured a lookalike model, you can associate it to a collaboration.

**To associate a configured lookalike model in AWS Clean Rooms**

1. Sign in to the AWS Management Console and open the [AWS Clean Rooms console](https://console.aws.amazon.com/cleanrooms/home) with your AWS account (if you haven't yet done so).

1. In the left navigation pane, choose **Collaborations**.

1. On the **With active membership** tab, choose a collaboration.

1. On the **ML models** tab, under **Ready-to-use lookalike models**, choose **Associate lookalike model**.

1. On the **Associate configured lookalike model** page, for **Configured lookalike model association details**:

   1. Enter a **Name** for the associated configured audience model.

   1. Enter a **Description** of the table. 

      The description helps differentiate between other associated configured audience models with similar names.

1. For **Configured lookalike model**, choose a configured lookalike model from the dropdown list.

1. Choose **Associate**. 

For the corresponding API action, see [CreateConfiguredAudienceModelAssociation](https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_CreateConfiguredAudienceModelAssociation.html).