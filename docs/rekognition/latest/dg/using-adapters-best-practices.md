# Best practices for training

adapters

It's suggested you abide by the dollowing best practices when creating, training, and
using your adapters:

1. The sample image data should capture the representative errors that the
   customers intend to suppress. If the model is making repeated mistakes on
   visually similar images, make sure to bring many of those images for
   training.
2. Instead of only bringing in images that the model makes mistakes on a
   particular Moderation label, also make sure to bring in images that the
   model are not making mistakes on that Moderation label.
3. Supply a minimum of 50 False Negative samples OR 20 False Positive samples
   for training and a minimum of 20 samples for testing. However, supply as
   many annotated images as possible for better adapter performance.
4. Annotating all labels that matters to you for all images - if you decide
   that you need to annotate the occurrence for a label on an image, make sure
   to annotate the occurrence for this label on all other images.
5. The sample image data should contain as many variations on the label as
   possible, focusing on instances that are representative of the images that
   will analyzed in a production setting.
