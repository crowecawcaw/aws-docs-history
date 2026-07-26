# Run VTK visualization scripts on Deadline Cloud

The
[vtk-latest](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vtk-latest "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vtk-latest")
job bundle runs VTK (Visualization Toolkit) Python scripts on Deadline Cloud. The
bundle is generalizable for any VTK-based Python script that accepts
command-line parameters for output path, width, and height, and saves
visualization output to a specified location.

Your VTK script must accept the following command-line arguments:

- `--output`: Output file path
- `--width`: Image width
- `--height`: Image height
  The bundle includes a sample script
  (`sample/flow_simulation_visualization.py`) that creates a 3D
  airfoil geometry, generates a flow field, calculates pressure
  distribution, and saves the output as an image with streamlines.

To run this bundle, your queue needs the `vtk` and
`numpy` conda packages available in the queue environment's
conda channels.

Submit the job with these parameters:

- `InputDir`: Directory containing your VTK
  script
- `InputScript`: Filename of your script
- `OutputDir`: Where to save the
  visualization
- `OutputFilename`: Name for the output
  file
- `ExtraParams`: Additional script parameters in
  the format `--param1 value1 --param2 value2`
