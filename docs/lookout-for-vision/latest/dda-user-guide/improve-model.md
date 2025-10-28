Defect Detection App is in preview release and is subject to change.

# Improving your model

The performance metrics might show that you can improve your model. For example, if the
model doesn't detect all anomalies in the test dataset, your model has low recall (that is, the
recall metric has a low value). If you need to improve your model, consider the
following:

- Check that the dataset images are properly labeled.
- Reduce the variability of image capture conditions such as lighting and object pose, and
  train your model on objects of the same type.
- Ensure that your images show only the required content. For example, if your project
  detects anomalies in machine parts, make sure that no other objects are in your images.
- [Add](dda-add-more-images-dataset.md "dda-add-more-images-dataset.md") more labeled images to your
  dataset.
- Ensure you have sufficiently diverse normal and anomalous images in your dataset. The
  images must represent the type of normal and anomalous images that your model will encounter.
  For example, when analyzing circuit boards, your normal images should represent the variations
  in position and soldering of components, such as resistors and transistors. The anomalous
  images should represent the different types of anomalies that the system might encounter, such
  as misplaced or missing components.
- If the image size is small, or the image resolution is low, consider capturing images at
  a higher resolution. Image dimensions can range from 64 x 64 pixels up to 4096 pixels X 4096
  pixels.
- If the anomaly size is small, consider dividing the images into separate tiles and use
  the tiled images for training. This lets the model see defects at a larger size in an
  image.
  After you have improved your dataset, retrain and re-evaluate your model. For more
  information, see [Training your model](dda-train-model.md "dda-train-model.md").
