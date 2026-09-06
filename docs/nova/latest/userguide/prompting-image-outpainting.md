

# Outpainting prompts
<a name="prompting-image-outpainting"></a>

Outpainting is used to replace the background of an image. For best results, outpainting prompts should describe what you would like the *whole* image to look like, including the parts of the image that will not be changed.

The following example uses a `text` value of *"a coffee maker in a sparse stylish kitchen, a single plate of pastries next to the coffee maker, a single cup of coffee".*

**Input Image**

![Amazon coffee maker](http://docs.aws.amazon.com/nova/latest/userguide/images/amazon-coffee-maker-1.png)


**Mask Prompt**: *"coffee maker"*

**Result**

![Background replacement image](http://docs.aws.amazon.com/nova/latest/userguide/images/background-replacement-mask-prompt-example-1.png)


Here is another example that uses a `text` value of *"detailed photo of a flower pot sitting on an outdoor potting bench".*

**Input Image**

![Three pots](http://docs.aws.amazon.com/nova/latest/userguide/images/three_pots.jpg)


**Mask Image**

![mask image](http://docs.aws.amazon.com/nova/latest/userguide/images/three_pots-remove_mask_INVERTED.png)


**Result**

![Mask item moved to a new background](http://docs.aws.amazon.com/nova/latest/userguide/images/potted.png)
