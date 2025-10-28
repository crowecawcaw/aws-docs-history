# Edit a model card

To edit a model card, navigate to the model card of your choice by selecting its
name in the Amazon SageMaker Model Card console and choose **Edit**.

After you save a model card, you cannot edit the name of that model card. After
you save a model card version, you cannot update that version of the model card. Any
edits that you need to make are saved as a subsequent version in order to have an
immutable record of model changes.

To view different versions of the model card, choose **Actions**,
**Select version**, and then choose the version that you want
to view.

You can edit a model card using the
``model_card`.update()` method. Updating a
model card creates a new model card version in order to have an immutable record of
model changes. You cannot update the name of a model card.

```
`my_card`.model_overview.model_description = `"updated-model-decription"`
`my_card`.update()
```
