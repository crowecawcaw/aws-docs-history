# Mask prompts

Mask prompts are used in editing operations. A mask prompt allows you to use natural
language to describe the elements within an image that you want to change (in the case of
inpainting) or to remain untouched (in the case of outpainting). You pass a mask prompt as
part of your request using the `maskPrompt` parameter. Below are some examples
that visualize the result of a mask prompt. The masked area is colored in dark blue.

**Mask Prompt: "dog"**

![A dog](images/Screenshot1.png)
**maskPrompt: "dog"**

![A dog](images/Screenshot3.png)
**Mask Prompt: "dog in a bucket"**

![A dog in a bucket](images/Screenshot2.png)
**maskPrompt: "black dog"**

![A black dog](images/Screenshot4.png)
