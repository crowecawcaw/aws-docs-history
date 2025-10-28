# Learn about media handling

Amazon Silk supports a wide range of media types.

###### Topics

- [Images](#image-handling "#image-handling")
- [Audio](#audio-handling "#audio-handling")
- [Video](#video-handling "#video-handling")

## Images

In addition to all the expected image formats, Amazon Silk supports scalable vector graphics
(SVG) both inline via the <svg> tag and externally using the <img>,
<object>, and <embed> tags. For more information, see [SVG Element](html5-elements.md#svg "html5-elements.md#svg").

###### Image Optimization

Though not specific to Amazon Silk, the following tips can help you optimize images for
your web site.

- **Set the width and height attributes:** It's usually a
  good idea to set the width and height attributes explicitly on images. Browsers use the
  width and height attributes to determine the amount of space that an image needs in the
  page layout. If these attributes are not set, or if they don't match the actual dimensions
  of the image, the browser may have to reflow the page, which can increase page load
  time.
- **Remove excess white space:** If you want to add padding
  around an image, you're better off doing it with CSS than with extra white space around
  the image itself. Extra space in an image increases file size.
- **Use the right file format:** Using the correct file
  format for a given color palette and use case can help you minimize file size. As a
  general rule, use GIF for animations, GIF or PNG-8 for flat graphics or where transparency
  is needed, and JPG or PNG for photos and colorful, detailed images.
- **Consider using an image optimizer:** Image optimizers
  can reduce the size of image files. Available image optimization tools include [TinyPNG](https://tinypng.com/ "https://tinypng.com/") and the [Grunt imagemin
  plugin](https://github.com/gruntjs/grunt-contrib-imagemin "https://github.com/gruntjs/grunt-contrib-imagemin").

For more information on image optimization, see [Optimizing web
graphics](https://developers.google.com/speed/articles/optimizing-images "https://developers.google.com/speed/articles/optimizing-images").

## Audio

Amazon Silk fully supports the HTML5 [Audio Element](html5-elements.md#audio-element "html5-elements.md#audio-element"), with playback occurring in the browser. The default
controls are improved from earlier Fire devices, and Silk also supports custom controls;
playback of multiple streams; and MP3, OGG, and WAV audio formats. JavaScript support is good,
enabling, for example, algorithmic PCM Audio using data URIs.

Amazon Silk doesn’t support background audio, meaning that audio playback is paused when a
tab loses focus.

## Video

Amazon Silk supports the HTML5 `video` tag, and MP4 and WEBM video formats. Note
that the audio encoding in video streams must be at most stereo. The Fire family of devices
doesn’t support 5.1 audio.

Amazon Silk also supports the RTSP and HLS network protocols. For more information about
media formats that the Android platform supports, see [Android Supported Media
Formats](http://developer.android.com/guide/appendix/media-formats.html "http://developer.android.com/guide/appendix/media-formats.html").

### Graceful Degradation with the Video Element

It's usually a good idea to use [Learn about feature detection](feature-detection.md "feature-detection.md") for features and media formats that aren't supported
by all browsers. To detect video support, you can also try a simpler solution: graceful
degradation with the HTML5 video element, which doesn't require JavaScript. In the example
below, the video element provides a built-in fallback structure that lets you easily deliver
multiple video container formats.

```
<video controls>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
</video>
```

The example tries to serve MP4 and then falls back to the WebM file. The browser will
play the first compatible format. For more on graceful video degradation, see [Video for Everybody](http://camendesign.com/code/video_for_everybody "http://camendesign.com/code/video_for_everybody"); for
more on HTML5 video, see [Video Element](html5-elements.md#video-element "html5-elements.md#video-element").
