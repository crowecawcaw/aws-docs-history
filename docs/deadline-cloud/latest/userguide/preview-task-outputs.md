

# Preview task outputs in the job monitor
<a name="preview-task-outputs"></a>

The **Task outputs** panel shows the output files of the task that you select in the **Tasks** list. The panel previews images, text, tables, logs, video, audio, and 3D files, so you can check what a task produced without downloading its files or leaving the job monitor.

To try the panel with sample data, open the [demo compositing job](https://_demo.us-east-1.deadlinecloud.amazonaws.com/us-west-2/farms/farm-94d29d9475dd814529b87a52f20ff9cb/queues/queue-b5fb7c92ae42326d3851bab4b0568d97?jobId=job-1cf313e2991e74375006ea6092c5a2ed&stepId=step-ed81a8594ee0f700b2f915af2582cc26&taskId=task-ed81a8594ee0f700b2f915af2582cc26-0&demo=moonrise), and then add the **Task outputs** panel.

**To preview the outputs of a task**

1. Follow the steps in [View and manage job details in Deadline Cloud](view-a-job.md) to view a list of jobs.

1. Choose the **Add panel** tile that follows the last panel on the page. In **Add a panel**, choose **Task outputs**. You only need to add the panel once. For more information, see [Customize the panels in the job monitor](customize-job-monitor-panels.md).

1. Select a job in the **Jobs** list, a step in the **Steps** list, and a task in the **Tasks** list. The panel lists the output files of the task and previews the first image or video. If the task has no image or video output, the panel opens the first file.

1. (Optional) To preview a different file, choose it in the **Files** tree.

The panel shows a message instead of files in the following cases:
+ **No task selected** appears until you select a task in the **Tasks** list.
+ **Multiple jobs selected**, **Multiple steps selected**, or **Multiple tasks selected** appears when you select more than one job, step, or task. The panel previews the outputs of one task at a time.
+ **No outputs** appears when the task hasn't uploaded any output files yet.

## Browsing and saving output files
<a name="preview-task-outputs-browse"></a>

The panel shows the **Files** tree on the left and a preview of the selected file on the right. To give the preview more room, choose the **Hide file tree** icon in the upper left of the panel. To show the tree again, choose **Show file tree**.

From the panel, you can do the following:
+ To step through the files in the order of the tree, choose **Previous preview** or **Next preview** under the preview. Between the two buttons, the panel shows the position of the file in the list, such as **4 of 6**. You can also select the preview and press the left arrow or right arrow key. The buttons and keys also stop at files that can't be previewed, such as EXR images. For these files, the panel shows the file name and a message that a preview isn't available. A video or audio file that your browser can't play shows a similar message.
+ To save the selected file, choose the download icon next to the file name.
+ To save all of the task's output files, choose **Download all outputs** in the panel header.
+ To open the task's outputs in the attachments browser, choose **Open in full view** in the panel header. In a browser, the attachments browser opens in a new tab. In the Deadline Cloud monitor desktop application, it opens in the application. The attachments browser adds filtering, file details, and a full-screen preview. For more information, see [Browsing job attachments in Deadline Cloud](browse-job-attachments.md).

## Viewing 3D meshes and point clouds
<a name="preview-task-outputs-3d"></a>

The panel previews meshes and point clouds in GLB, glTF, OBJ, STL, PLY, and PCD format, and Universal Scene Description (USD) scenes in USD, USDA, USDC, and USDZ format.

In the following image, the panel previews an OBJ file of a cube. The **Files** tree and the **Properties** panel are on the left, and the 3D view is on the right. The zoom, **Reset view**, **Save snapshot as PNG**, download, **Show controls**, and **View settings** controls are in a row at the top of the panel, next to the file name. The axis indicator is in the lower-right corner of the 3D view.

![An OBJ cube in the Task outputs panel, with the zoom, Reset view, snapshot, download, Show controls, and View settings controls next to the file name and the axis indicator in the corner of the 3D view.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-mesh.png)


The buttons next to the file name zoom the view and fit the content to the view again. They also save the current view as a PNG image and list the mouse controls. The axis indicator in the 3D view shows the X, Y, and Z axes of the file as the camera sees them.

To change how the file is drawn, choose the **View settings** icon. The settings that appear depend on whether the file contains a mesh, a point cloud, or a USD scene. A PLY file can contain either one, so the panel checks the file's contents instead of its extension. The settings stay in effect as you step between the files of the selected task.

The following table lists the view settings and the files that each one applies to.


| Setting | Applies to | Description | 
| --- | --- | --- | 
| Show wireframe | Meshes and USD scenes | Draws surfaces as the edges of their triangles. | 
| Ambient light | Meshes and USD scenes | Sets the strength of the light that reaches every surface evenly. | 
| Directional light | Meshes and USD scenes | Sets the strength of the light that shines from one direction and shades the surfaces. | 
| Light direction | Meshes and USD scenes | Turns the directional light around the vertical axis. | 
| Point size | Point clouds | Scales the size of each point. | 
| Up axis | Point clouds | Sets which axis of the file points up. Mesh formats define their own up axis. | 
| Background | Meshes, point clouds, and USD scenes | Sets the color behind the content. To return to the default color, choose Reset to default. | 
| Show grid | Meshes, point clouds, and USD scenes | Draws a floor grid under the content. | 
| Show axes | Meshes, point clouds, and USD scenes | Draws the X, Y, and Z axes of the file through the content. | 
| Show bounding box | Meshes, point clouds, and USD scenes | Draws a box around the whole model. | 

USD scenes have the same view buttons and settings, except **Point size** and **Up axis**, because a USD scene sets its own up axis. They do not have the axis indicator or the **Show controls** icon.

Under the view, the panel shows the scene's up axis, its meters per unit, and the number of prims in the scene.

A USD, USDA, or USDC file shows only the geometry that it defines itself. The files that it refers to are not part of the attachment. When the file refers to other files, the panel says so: it shows **Showing this file only** under the view, or, when the file has no geometry of its own, it shows a message in place of the view.

If a file is too large to preview, or the monitor can't read it, the panel shows a message in place of the view. To open the file in other software, save it with the download icon.

## Viewing the properties of a mesh or point cloud
<a name="preview-task-outputs-properties"></a>

When you preview a GLB, glTF, OBJ, STL, PLY, or PCD file, the **Properties** panel under the **Files** tree describes the file. The panel shows the following properties:
+ **Format**: the file format, such as **Wavefront OBJ** or **Point Cloud Data**.
+ **Objects**: the number of objects in the file.
+ **Vertices**: the number of vertices. Shown for meshes only.
+ **Triangles**: the number of triangles. Shown when the file contains triangles.
+ **Points**: the number of points. Shown when the file contains a point cloud.
+ **Size (X × Y × Z)**: the size of the model along each axis. Shown when the model has a size.
+ **Materials**: the number of materials.
+ **Vertex colors**: **Yes** when the file stores a color for each vertex or point.
+ **Animations**: the number of animations. Shown when the file contains animations.

In the following image, the panel previews a PLY point cloud. The **Files** tree is on the left with the **Properties** panel under it, and the point cloud is in the 3D view on the right. The **Properties** panel lists each property name with its value next to it: **Format** is PLY, **Objects** is 1, **Points** is 240, **Size (X × Y × Z)** is 2.7 × 0.7 × 2.7, **Materials** is 1, and **Vertex colors** is **Yes**.

![A PLY point cloud in the Task outputs panel. The Properties panel lists a PLY format, 1 object, 240 points, a size of 2.7 by 0.7 by 2.7, 1 material, and vertex colors.](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/images/monitor/job-monitor-task-outputs-point-cloud.png)


When you hide the file tree, the **Properties** panel is hidden too. Under the view, the panel then shows the number of triangles and objects in a mesh, or the number of points in a point cloud.

The full-screen preview in the attachments browser also shows the **Properties** panel, next to the view. For more information, see [Previewing files](browse-job-attachments.md#browse-job-attachments-preview).

## Viewing data and log files
<a name="preview-task-outputs-data"></a>

The panel opens the following data and log files in viewers of their own:
+ CSV, TSV, and JSON Lines (JSONL and NDJSON) files appear as a table. The table shows the first rows and columns of the file. To read the file as plain text instead, choose **Text** for **View** in the view settings. For a JSON Lines file, a message at the top of the preview lists the lines that aren't valid JSON, and the table leaves those lines out.
+ Parquet files appear as a table of the first rows, with the data type of each column under its name. The full-screen preview also lists the schema of the file and the software that wrote it.
+ JSON files appear as formatted text. To explore the file as an expandable tree, choose **Tree** for **View** in the view settings. If the file isn't valid JSON, the panel shows the raw text and the line and column where parsing stopped.
+ YAML files appear with highlighting. If the file has a syntax error, the panel shows the line and column of the first error.
+ Log files appear with line numbers, and errors and warnings are colored. To show only the lines with errors and warnings, turn on **Show errors and warnings only** in the view settings. A very large log shows its first and last lines, and the panel says how many lines it leaves out.

If a file is larger than the viewer can read, the panel shows the start of the file, or a message that the file is too large to preview, and suggests that you save the file to view all of it.