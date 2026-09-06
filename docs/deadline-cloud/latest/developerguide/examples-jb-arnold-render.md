

# Render Arnold .ass files on Deadline Cloud
<a name="examples-jb-arnold-render"></a>

The [arnold\_standalone\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/arnold_standalone_render) job bundle on the GitHub website renders Arnold `.ass` (Arnold Scene Source) files using the `kick` command-line renderer that ships with MtoA (Arnold for Maya). Point it at a directory of `.ass` files with a naming pattern, and it renders each frame as a separate task distributed across workers. This sample is useful for batch rendering pre-exported Arnold scenes without a full Maya session.

The bundle includes a sample `cornell.0001.ass` file in the `scene/` directory. You can also download additional learning scenes from the [Arnold for Maya learning scenes](https://help.autodesk.com/view/MAYAUL/2024/ENU/?guid=arnold_for_maya_tutorials_am_Learning_Scenes_html) page on the Autodesk website, or export `.ass` files from Maya. To automate the export step, use the [maya\_arnold\_ass\_export\_render](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/maya_arnold_ass_export_render) bundle on the GitHub website.

To run this bundle, you need:
+ A queue with the `kick` binary available through a queue environment. The bundle's `CondaPackages` parameter defaults to `maya-mtoa`, which provides `kick`. On service-managed fleets, the `deadline-cloud` conda channel provides this package. For a specific MtoA version, build a custom package. For more information, see the [maya-mtoa conda recipe](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/conda_recipes/maya-mtoa-2026) on the GitHub website.
+ A Linux fleet associated with the queue. The job template specifies `attr.worker.os.family: linux` as a host requirement.

Submit the bundle:

```
deadline bundle submit arnold_standalone_render/ \
    -p SceneDirectory={{path-to-ass-files}} \
    -p FilePattern={{robot.####.ass}} \
    -p Frames=1-100 \
    -p OutputDir={{./output}}
```