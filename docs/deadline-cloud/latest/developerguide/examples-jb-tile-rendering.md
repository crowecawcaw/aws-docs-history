

# Tile rendering on Deadline Cloud
<a name="examples-jb-tile-rendering"></a>

Tile rendering divides each frame into evenly sized regions, renders each region as a separate task in parallel across workers, then assembles the regions into the final image. The samples repository on the GitHub website includes several tile rendering job bundles for different DCC and renderer combinations.

[tile\_render\_with\_maya\_arnold](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/tile_render_with_maya_arnold)  
A two-step job that renders frames in tiles using a 3-dimensional task parameter space (Frame × TileNumberX × TileNumberY) and then assembles the tiles for each frame using FFmpeg. The bundle includes a simple scene and default parameters to make it easy to try.

[tile\_render\_with\_maya\_vray](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/tile_render_with_maya_vray)  
A tile rendering job that uses Maya and V-Ray to create EXRs as output, then uses OpenImageIO to assemble them into a single image. The bundle relies on the V-Ray render handler in the Maya adaptor. For more information about OpenImageIO, see [OpenImageIO](https://github.com/AcademySoftwareFoundation/OpenImageIO) on the GitHub website.

[tile\_render\_with\_vray\_linux](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/tile_render_with_vray_linux)  
Renders a V-Ray scene by dividing the image into a configurable grid of regions (rows × columns × frames), rendering each region as a separate task using V-Ray's `-crop` flag, and merging the regions with ImageMagick. Optionally creates an MP4 movie from the rendered frames using FFmpeg. Automatically handles asset path remapping between workstation and workers.

[tile\_render\_maya\_ffmpeg\_for\_blogpost](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/tile_render_maya_ffmpeg_for_blogpost)  
A companion job for the AWS blog post [Create a tile rendering job with modifications for AWS Deadline Cloud](https://aws.amazon.com/blogs/media/create-a-tile-rendering-job-with-modifications-for-aws-deadline-cloud/). The blog post walks through customizing the Deadline Cloud Maya adaptor and writing a tile rendering job template.

Choose a tile count based on image size, scene complexity, and worker pool size. More regions create more parallelism but also add overhead. For small images, fewer regions can be faster. For large images and complex scenes, more regions can significantly reduce total render time.