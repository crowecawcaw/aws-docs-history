# Understanding overlay layers

The **Layer** setting specifies how overlapping image overlays
appear in the video. The service overlays images with higher values for
**Layer** on top of overlays with lower values for
**Layer**. Each overlay must have a unique value for
**Layer**; you can't assign the same layer number to more than
one overlay.

The following illustration shows how the value for **Layer**
affects how a image overlay appears in relation to other overlays. The triangle
has the highest value for **Layer** and appears on top, obscuring
the video frame and all image overlays with lower values of
**Layer**.

![The underlying video is obscured by three image overlays: a blue rectangle with a Layer value of 1, a green ring with a Layer value of 2, and an orange triangle with a Layer value of 3. Where the rectangle and ring overlap, the ring obscures the rectangle. Where the triangle and ring overlap, the triangle obscures the ring. In the transparent portion of the ring, the underlying video and a corner of the rectangle show through.](images/ImgIns-Layer.png)

###### To specify a value for the **Layer** setting

1. Set up your image overlay as described in [Image insertion](graphic-overlay.md "graphic-overlay.md").
2. For **Layer**, enter a whole number from 0 to 99.

###### Note

You can use each number only once. Each image overlay must have its
own layer.
