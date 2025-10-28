# Color conversion with 3D LUTs

When you convert a video from one color space to another, AWS Elemental MediaConvert automatically maps
colors from your input color space to your output color space. To optionally specify your own
custom color mapping, use **3D LUTs** (3D lookup
tables).

3D LUTs contain color mapping information for a specific input or set of inputs. You receive
3D LUTs as .cube files from your color grader as part of your video production workflow.

3D LUTs are tools for color transformation in video processing workflows. They allow you to apply
precise color adjustments to your video content, ensuring consistent color appearance across
different displays and viewing environments. Some reasons to include 3D LUTs in your workflow
might include any of the following:

- Apply cinematic or broadcast-grade color grading to your content
- Control color mapping when you convert between different color spaces
- Ensure consistent colors across different content
- Correct color imbalance or exposure shifts in source footage
- Apply creative or stylized color treatments

###### Topics

- [Configuring a job with 3D LUTs](3d-lut-use.md "3d-lut-use.md")
- [3D LUTs job settings requirements](3d-lut-requirements.md "3d-lut-requirements.md")
- [Troubleshooting](3d-lut-troubleshooting.md "3d-lut-troubleshooting.md")
