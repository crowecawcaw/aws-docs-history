

# How Dynamic Multiview works
<a name="dynamic-multiview-how-it-works"></a>

A multiview is assembled from several MediaLive channels that deliver into one MediaPackage channel group. This section describes how those pieces fit together and what each one contributes.

![Architecture diagram. Four MediaLive channels labeled A through D each deliver to a same-named channel in a MediaPackage channel group, and each of those channels is delivered to viewers as a single-view stream. A multiview channel in the same channel group reads segments from the source channels and generates combined streams, shown as a two-view, a three-view, and a four-view arrangement.](https://docs.aws.amazon.com/medialive/latest/ug/images/dynamic-multiview-architecture.png)


## How the pieces fit together
<a name="dynamic-multiview-pieces"></a>

1. **One MediaLive channel per source feed.** Each MediaLive channel has a MediaPackage output group that delivers CMAF Ingest outputs to a MediaPackage V2 channel.

1. **All source channels deliver into the same MediaPackage channel group.** The channel group also contains a multiview channel, which reads segments from the source channels.

1. **The player requests a layout and an ordered list of sources** as query parameters on the manifest request. Because the layout is a request parameter, an application can change the arrangement during playback.

1. **The multiview channel assembles the matching segments on demand** and returns one HLS or DASH stream — one video track, one decoder, one DRM key, whichever layout the viewer chose.

Because the combining happens at delivery, your encoding footprint scales with the number of source feeds, not with the number of arrangements viewers can request.

## What MediaLive contributes
<a name="dynamic-multiview-medialive-contributes"></a>

MediaLive encodes each source feed using encoder settings that make the resulting renditions combinable downstream. MediaLive does not composite feeds together and has no awareness of which arrangement a viewer will eventually request.

What MediaLive produces is a ladder of renditions per feed, where every rendition is:
+ encoded with settings that make it multiview compatible, so that MediaPackage can combine it with renditions from other feeds, and
+ sized so that it fits the view positions of the layouts you want to support.

Each participating output also declares one or more multiview usages in the `outputUsage` field, which tells MediaLive which view positions the rendition is intended to fill. MediaLive uses that declaration to apply the multiview validations. For the enum values and the validation rules they trigger, see [Dynamic Multiview: MediaLive Configuration Reference](dynamic-multiview-reference.md).

## Views and layouts
<a name="dynamic-multiview-views-layouts"></a>

MediaPackage supports combining two to four feeds per layout. All feeds in one multiview must be channels in the same MediaPackage channel group.

A layout is either **equal-size**, where every view is the same size, or **primary/secondary**, where one large view is accompanied by smaller ones. In a primary/secondary layout, a secondary view is always exactly half the width and half the height of its primary.



| Layout | Views | Arrangement | Views required | 
| --- | --- | --- | --- | 
| 2EH | 2 | Two equal, side by side | equal-size | 
| 3EL | 3 | Three equal, one left and two right | equal-size | 
| 4E | 4 | Four equal, 2×2 grid | equal-size | 
| 2PL | 2 | One large primary on the left, one secondary | primary \+ secondary | 
| 3PL | 3 | One large primary on the left, two secondary | primary \+ secondary | 
| 4PL | 4 | One large primary on the left, three secondary | primary \+ secondary | 

These diagrams show how each layout arranges its views.

![Diagrams of the six supported layouts, labeled 2EH, 3EL, and 4E in the left column and 2PL, 3PL, and 4PL in the right column. Each diagram shows the position and relative size of the views within the assembled frame. The arrangements are described in the preceding table.](https://docs.aws.amazon.com/medialive/latest/ug/images/dynamic-multiview-layouts.png)


## Audio and captions
<a name="dynamic-multiview-audio-captions"></a>

A multiview stream carries the audio and caption tracks of **every** view, not only one. The viewer chooses which to play.

Each source feed's audio and captions are packaged as selectable renditions in the manifest — audio rendition groups and caption tracks in HLS, adaptation sets in DASH. A viewer watching several feeds can listen to any one of them, and switch between them, without changing the visual layout.

### Identifying audio and captions for each view
<a name="dynamic-multiview-identify-renditions"></a>

MediaPackage labels each audio and caption rendition in the stitched manifest so that you can tell which view it belongs to. You supply the label from your MediaLive channel:
+ For audio, set the **Stream Name** field in the **Stream settings** section of each audio description — for example, `English` or `Spanish`.
+ For captions, set the **Language description** field of each caption description — for example, `English` or `Spanish`.

MediaPackage prefixes that label with the view position. An audio rendition labeled `English` on your first source appears as `View1_English`. A rendition labeled `English` on your second source appears as `View2_English`.

In an HLS manifest, this name appears in the `NAME` attribute on the `EXT-X-MEDIA` tag. In a DASH manifest, it appears in the `Label` element on the corresponding adaptation set.

The view number matches the order in which you listed the source channels in the `sources` parameter of your request. The first source is view 1, the second is view 2, and so on. For information about the `sources` parameter, see [Multiview](https://docs.aws.amazon.com/mediapackage/latest/userguide/dynamic-multiview.html) in the *AWS Elemental MediaPackage User Guide*.