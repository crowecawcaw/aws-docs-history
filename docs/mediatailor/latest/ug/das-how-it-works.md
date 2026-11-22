

# How dynamic avail sizing works

Dynamic avail sizing shortens an underfilled avail. To keep the personalized manifest advancing when it does, it holds back a pool of content called the content reserve.

## Ad avail underfill
<a name="das-underfill"></a>

An ad avail underfills when MediaTailor can't fill the whole avail with ads. This can happen when the ADS returns fewer seconds of ads than the avail allows, or when an ad isn't ready for insertion. Without dynamic avail sizing, MediaTailor shows some of the unpersonalized avail content, or inserts slate if slate is configured.

With dynamic avail sizing, MediaTailor shortens the avail by omitting the underfill. The avail ends earlier and programming resumes.

## Content reserve and virtual live edge
<a name="das-content-reserve"></a>

To shorten an avail without stalling the player, dynamic avail sizing uses a *content reserve* (the *reserve*), which is content that MediaTailor holds back from the player. You set the size of the reserve with the `aws.contentReserveSeconds` parameter.

Because MediaTailor holds the reserve back, the personalized manifest ends at the *virtual live edge*, which trails the origin live edge by the duration of the reserve. Playback runs about the reserve's duration further behind the origin live edge than it would without dynamic avail sizing.

The following figure is a timeline that ends at the origin live edge. The part up to the virtual live edge is the content in the personalized manifest. The rest is the reserve, which MediaTailor holds back from the player.

![The player's virtual live edge trails the origin live edge by the duration of the content reserve.](https://docs.aws.amazon.com/mediatailor/latest/ug/images/das-live-edge-diagram.png)


**1**  
Content in the personalized manifest

**2**  
Reserve

**3**  
Virtual live edge, where the personalized manifest ends

**4**  
Origin live edge

For playback to stay healthy, the virtual live edge must advance on every manifest request. The player expects new segments at a regular interval. When MediaTailor shortens an avail, the reserve shrinks by the omitted duration. As the origin publishes the part of the avail that MediaTailor omitted, MediaTailor reveals the same duration of reserved content in its place, so the player keeps receiving new segments.

For recommended reserve and manifest window sizes, see [Best practices](das-enable.md#das-enable-best-practices).

## Reserve replenishment
<a name="das-reserve-replenishment"></a>

Each shortened avail reduces the reserve by the duration that MediaTailor omitted. Dynamic avail sizing replenishes the reserve by *inflating* later avails, which means requesting more ad time than an avail's original duration. When the ADS fills the extra time, the surplus returns content to the reserve.

MediaTailor inflates an avail by the smaller of the deficit and `aws.maxAvailInflationSeconds`. The *deficit* is `aws.contentReserveSeconds` minus the current reserve. MediaTailor inflates an avail only when the deficit is greater than 0 and at least `aws.replenishmentThresholdSeconds`. A threshold of `0` means that any deficit triggers inflation. You control this behavior with `aws.maxAvailInflationSeconds` and `aws.replenishmentThresholdSeconds`.

## When the reserve can't cover the underfill
<a name="das-fallback"></a>

If the reserve can't cover an avail's whole underfill, dynamic avail sizing doesn't shorten that avail. Instead, MediaTailor fills the avail as it would without dynamic avail sizing: ads play, and then slate or unpersonalized avail content fills the remaining time. The reserve doesn't change and the virtual live edge doesn't move. A later avail can still use dynamic avail sizing if the reserve covers its underfill.