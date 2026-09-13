

# Dynamic Multiview: Borders
<a name="dynamic-multiview-borders"></a>

AWS Elemental MediaLive adds a black border around every video output that participates in Dynamic Multiview. This section explains why the border is needed, how MediaLive sizes it, and when you might want to change it.

## Why multiview outputs need a border
<a name="dynamic-multiview-borders-why"></a>

When MediaPackage assembles a multiview frame, it places each feed's encoded bitstream next to its neighbors without decoding. In H.264, the deblocking filter smooths pixels across block boundaries — including the boundary that now sits between two unrelated feeds. Without separation, pixels from an adjacent view influence the pixels at the edge of yours, and the seam between views shows visible contamination. A black border absorbs that filtering. The filter operates on border pixels instead of on picture content, so each view stays pristine regardless of what is displayed beside it.

H.265 does not need a border. The encoder settings that multiview requires for H.265 already isolate each view. MediaLive still applies a border to H.265 outputs by default, so that an H.264 and an H.265 ladder of the same content look consistent, but you can reduce or remove it.

## The border sits inside the coded frame
<a name="dynamic-multiview-borders-coded-frame"></a>

The border is part of the coded picture, not something added around it. The coded width and height you configure include the border, and the active picture is what shrinks. The width and height divisibility rules — 16 pixels for H.264, 32 pixels for H.265 — apply to the coded dimensions. The border is inside them. MediaLive produces the border by scaling and repositioning the input video to fit the active area. No input pixels are cropped or obscured — the picture is slightly smaller, not clipped.

**Border values are per side.** A 4-pixel border means 4 pixels on each of the four edges, so it consumes 8 pixels of coded width and 8 pixels of coded height in total.

## How MediaLive sizes borders across a rendition ladder
<a name="dynamic-multiview-borders-ladder"></a>

MediaLive applies a **4-pixel border to the lowest-resolution participating rendition** in the multiview output group and scales the border proportionally for larger renditions. A rendition with twice the linear dimensions of the smallest gets twice the border.

For a three-rung H.264 ladder:



| Rendition | Border (per side) | Border as share of width | 
| --- | --- | --- | 
| 256×144 | 4 | 1.56% | 
| 512×288 | 8 | 1.56% | 
| 1024×576 | 16 | 1.56% | 

The point of the proportional rule is that the border occupies the same *fraction* of the frame at every rung. That matters across ABR switches. When a player switches renditions mid-stream, the border keeps its apparent position and thickness. A fixed 4-pixel border at every rung would instead appear to shrink as the player moved up the ladder, so the border would seem to move or change size on every switch — a visible, distracting artifact.

4 pixels is the minimum for H.264. H.265 has no functional minimum, but defaults to the same values.

## Borders between views are additive
<a name="dynamic-multiview-borders-additive"></a>

Each encode carries its own border, and MediaPackage does not trim them when generating a multiview output. The black space a viewer sees between two views is the sum of the two adjacent borders, while the outer edge of the assembled frame shows only one border.

For a layout of equal-size views, that means the area between views is twice the configured border and the outer frame is only one border wide. For a primary/secondary layout the two borders differ, so the boundary between a primary and a secondary is the sum of a wide border and a narrow one rather than a simple doubling.

## Making borders look thinner
<a name="dynamic-multiview-borders-thinner"></a>

Because the border is a constant fraction of frame width across the whole ladder, that fraction is fixed by the **smallest** rendition: 4 pixels divided by the smallest rendition's width. The way to make borders appear thinner relative to the picture is therefore to increase the resolution of the bottom of your ABR ladder. Dropping the lowest rendition raises the smallest height/width, which lowers the ratio for every rung:



| Smallest rendition | 4-pixel border as share of width | 
| --- | --- | 
| 256×144 | 1.56% | 
| 512×288 | 0.78% | 
| 640×360 | 0.63% | 

This is a trade-off against ABR reach: a higher floor means clients on poor connections have fewer rungs to fall back to. Choose the floor based on how thin you want the borders and how much low-bitrate coverage you need.

## Overriding the defaults
<a name="dynamic-multiview-borders-override"></a>

The border is configured per output through the `border` field on the video description. Set it explicitly to override the value MediaLive would compute.



| Codec | Default | Can you change it? | 
| --- | --- | --- | 
| H.264 | 4 pixels at the smallest rendition, scaled proportionally | Yes, but the 4-pixel minimum still applies | 
| H.265 | Same as H.264, for consistency | Yes — you can change the values or set 0 to remove borders entirely | 

If you override borders, we recommend keeping them proportional across the ladder so that ABR switching doesn't result in a visible shift of the border and content.