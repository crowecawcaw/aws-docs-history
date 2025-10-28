# Amazon Nova Reel prompting best practices

Prompting for video generation models differs from prompting for large language models
(LLMs). Video generation models do not have the ability to reason or interpret explicit
commands. Therefore, it's best to phrase your prompt as if it were an image caption or
summary of the video rather than a command or conversation. You may want to include details
about the subject, action, environment, lighting, style, and camera motion.

When writing a video generation prompt, be mindful of the following requirements and best
practices:

- Generally, prompts must be no longer than 512 characters.
- For videos longer than six seconds created from a single prompt, your prompt can be up to 4000 characters. In this case, we recommend that you write a longer, more comprehensive prompt. This will better guide the model towards your desired outcome.
- If you'd like to influence camera movement, you will get the best results if you
  place camera movement descriptions at the start or end of your prompt.
- Do not use negation words like _"no"_,
  _"not"_, _"without"_, and so on. The model
  doesn't understand negation in a prompt and attempting to use negation will result
  in the opposite of what you intend. For example, a prompt that includes
  _"pan across a fruit basket with no bananas"_ will actually
  signal to the model to include bananas.
- When the output you get from a prompt is close to what you want but not quite
  perfect, try the following techniques one at a time in turn to refine your
  result:

      + Using a consistent `seed` value, make small changes to your
       prompt and re-run the prompt. This allows you to better understand how your
       prompt wording affects the output, allowing you to iteratively improve your
       results in a controlled way.
      + Once the prompt has been refined to your liking, generate more variations
       using the same prompt but a different `seed` value. It is often
       useful to generate multiple variations of an video by running the sample
       prompt with different seeds in order to find that perfect video clip.

  When using the storyboard, you can include a prompt for each six second interval. Each prompt on the storyboard must follow the preceding requirements and guidelines

###### Topics

- [Example video generation prompts](#prompting-video-examples "#prompting-video-examples")
- [Image-based video generation prompts](prompting-video-image-prompts.md "prompting-video-image-prompts.md")
- [Camera controls](prompting-video-camera-control.md "prompting-video-camera-control.md")

## Example video generation prompts

Here are some example prompts to get you started with video generation.

**Prompt:**
_"Cinematic dolly shot of a juicy cheeseburger with melting cheese, fries, and
a condensation-covered cola on a worn diner table. Natural lighting, visible steam
and droplets. 4k, photorealistic, shallow depth of field"_

**Prompt:**
_"Arc shot on a salad with dressing, olives and other vegetables; 4k;
Cinematic;"_

**Prompt**: _"First person view of a motorcycle
riding through the forest road."_

**Prompt:**
_"Closeup of a large seashell in the sand. Gentle waves flow around the shell.
Camera zoom in."_

**Prompt:**
_"Clothes hanging on a thread to dry, windy; sunny day; 4k; Cinematic; highest
quality;"_

**Prompt:**
_"Slow cam of a man middle age; 4k; Cinematic; in a sunny day; peaceful;
highest quality; dolly in;"_

**Prompt:**
_"A mushroom drinking a cup of coffee while sitting on a couch,
photorealistic."_
