# Outpainting prompts

Outpainting is used to replace the background of an image. For best results, outpainting
prompts should describe what you would like the _whole_ image to look
like, including the parts of the image that will not be changed.

The following example uses a `text` value of _"a coffee maker in a
sparse stylish kitchen, a single plate of pastries next to the coffee maker, a single
cup of coffee"._

**Input Image**

![Amazon coffee maker](images/amazon-coffee-maker-1.png)
**Mask Prompt**: _"coffee maker"_

**Result**

![Background replacement image](images/background-replacement-mask-prompt-example-1.png)
Here is another example that uses a `text` value of _"detailed photo
of a flower pot sitting on an outdoor potting bench"._

**Input Image**

![Three pots](/images/nova/latest/userguide/images/three_pots.jpg)
**Mask Image**

![mask image](images/three_pots-remove_mask_INVERTED.png)
**Result**

![Mask item moved to a new background](images/potted.png)
