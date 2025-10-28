# Options for correcting metadata

In step 1, you assessed the status of the color space metadata in the MediaLive inputs. You must
now decide if you can clean up any inaccurate metadata.

MediaLive can clean up the color space metadata for any color space except Dolby Vision 8.1
or an unsupported color space.

###### Note

If you want to convert the color space in your channel, the metadata for all the
inputs must be either accurate or cleaned up. If there is even one input that you can't
clean up, you won't be able to convert the color space in the outputs. You will have to
set up to pass through the color space.

If you want to pass through the color space and include its metadata, the metadata for
all the inputs must be either accurate or cleaned up. The downstream system reads this
metadata, so it must be accurate. If there is even one input that you can't clean up, you
can pass through the color space, but you should omit the color space in the
output.

###### Topics

- [Scenario A – Metadata is accurate](color-space-scenario-pass.md "color-space-scenario-pass.md")
- [Scenario B – Metadata can be corrected with
  force](color-space-scenario-correct.md "color-space-scenario-correct.md")
- [Scenario C – Correct the metadata with
  fallback](color-space-scenario-correct-one.md "color-space-scenario-correct-one.md")
- [Scenario D – Metadata can't be
  corrected](color-space-scenario-correct-multiple.md "color-space-scenario-correct-multiple.md")
