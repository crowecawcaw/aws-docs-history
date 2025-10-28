# Add fixed cameras to entities

You can attach fixed camera views to your entities within your AWS IoT TwinMaker scenes. These
cameras provide a fixed perspective on a 3d model, allowing you to quickly and easily
shift your perspective in a scene to a targeted entity.

1. Navigate to your scene in the [AWS IoT TwinMaker console](https://console.aws.amazon.com/iottwinmaker/ "https://console.aws.amazon.com/iottwinmaker/").
2. In the scene hierarchy menu, select the entity you want to attach the camera to.
3. Press the **+** button, and from the drop down options select **Add camera from current view**. To apply a camera with the current perspective to the entity.
4. In the inspector, you can configure your camera and adjust the following settings:
   - A camera **Name**
   - The camera **position** and **rotation**
   - The camera **focal length**
   - The **zoom level**
   - **Near** and **Far** clipping planes

5. To access your camera after you have placed it. Select the entity you added the camera to in the hierarchy. Look for the camera name listed under the entity.
6. Once you select the placed camera from your entity, the scenes camera view will snap to the set perspective of the placed camera.
