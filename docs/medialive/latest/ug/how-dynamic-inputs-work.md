# Static inputs and dynamic inputs

If your MediaLive channel includes files inputs, you should decide if you want to set up each
input as a _static input_ or as a _dynamic input_. Using dynamic inputs lets you increase the number of video sources
that you can use in the channel, while still observing the limit on the number of inputs that
you can attach to the channel.

You can set up file inputs as static or dynamic inputs. (Live inputs are always static
inputs.)

To set up a static input, you specify a standard file URL. For example,
`s3ssl://amzn-s3-demo-bucket/my-movie.mp4`.

To set up a dynamic input, you set up the all or part of the file URL with a variable. For
example, `s3ssl://amzn-s3-demo-bucket/movies/$urlPath$`. Each time you set up
in the schedule to switch to this input, you specify the value for the
`$urlPath$`. For example,
`s3ssl://amzn-s3-demo-bucket/movies/my-movie.mp4` in one input switch and
`s3ssl://amzn-s3-demo-bucket/movies/mlaw.mp4` in another input switch.

You can set up for dynamic content in MP4 file inputs and transport stream (TS) file
inputs.

The [procedure for setting up](ips-step-design-inputs.md "ips-step-design-inputs.md") for input
switching, later in this section, provides detailed information about deciding whether you
should set up some inputs as dynamic inputs.
