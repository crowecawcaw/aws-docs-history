# How to generate black video

In the following steps, you will include **Video generator**
to generate a black video. When you do, also specify a numerical value for
**Duration** in milliseconds from `50` to
`86400000`. This creates a video input with black frames for that
duration without an audio track.

Alternatively, MediaConvert automatically creates black video when the
following conditions are met:

- Your input doesn’t have video. Examples include:
  - Audio-only inputs
  - Captions-only inputs (in sidecar formats)

- Your output includes a video track.
  In the previous examples, the duration of the black video that you generate will match the
  duration of the input audio or captions.

**Generate black video by adding an input with Video
generator specified.**

1. In the **Input** pane, toggle on **Video
   generator**.
2. Specify a value for **Duration** in
   milliseconds.
3. After defining the rest of your job settings, choose
   **Create**.
   **Create a black video track for an audio-only
   input.**

4. In the **Input** pane, keep **Input file
   URL** blank.
5. Under **Audio selectors**, **Audio Selector
   1**, switch on **External file**.
6. Enter the URL of your audio input.
   1. If your input has both audio and video, MediaConvert ignores
      the input video.

7. Under **Audio selectors**, specify any other required
   input audio settings.
8. See [Step 3: Create output groups](setting-up-a-job.md#specify-output-groups "setting-up-a-job.md#specify-output-groups") and
   [Step 4: Create outputs](setting-up-a-job.md#create-outputs "setting-up-a-job.md#create-outputs") to set up your outputs.
   1. You must include a video track in your output.
   2. You must include an audio track in your output, with **Audio source**
      set to the **Audio selector** specified from
      step 2, shown previously.

9. After defining the rest of your job settings, choose
   **Create**.
10. MediaConvert automatically creates black video with the same duration as the input
    audio selector.
    **Create a black video track for a captions-only
    input.**

11. In the **Input** pane, keep **Input file
    URL** blank.
12. Next to **Captions selectors**, choose **Add
    captions selector**.
13. In **Captions Selector 1**, under
    **Source**, choose a sidecar captions format.
    1. Non-sidecar captions formats are not supported.

14. Enter the URL of your captions input.
15. See [Step 3: Create output groups](setting-up-a-job.md#specify-output-groups "setting-up-a-job.md#specify-output-groups") and
    [Step 4: Create outputs](setting-up-a-job.md#create-outputs "setting-up-a-job.md#create-outputs") to set up your outputs.
    1. You must include a video track in your output.
    2. You must include a captions track in your output, with
       **Captions source** set to the
       **Captions selector** specified from step 2
       above.

16. After defining the rest of your job settings, choose
    **Create**.
17. MediaConvert automatically creates black video, with the same
    duration as the input **Captions selector**.

## Video Generator FAQ

**Q: What if my job generates black video and I set my output frame
rate to Follow source?**

If your job does not include any other inputs, there is no input frame rate
for MediaConvert to follow. You must specify an output frame rate.

If your job includes any other inputs with video, MediaConvert uses the frame rate from
the first video input.

**Q: What if my job generates black video I don’t define
an output resolution?**

If your job does not include any other inputs, there is no input resolution for
MediaConvert to follow. Specify an output resolution.

If your job includes any other inputs with video, MediaConvert uses the
resolution from the first video input.
