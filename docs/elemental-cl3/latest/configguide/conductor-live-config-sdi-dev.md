# Adding SDI input

devices

Individual Elemental Live nodes in the AWS Elemental Conductor Live cluster might be set up with SDI cards. Each input
on the card can have a direct cable connection to an SDI video input.

If your cluster deployment includes a router for handling SDI (instead
of, or in addition to, direct cable connections), see [Configuring SDI video
routers](conductor-live-config-sdi-rou.md "conductor-live-config-sdi-rou.md").

**Where to perform the configuration**

Make sure you perform the configuration on the correct nodes.

| Node                          | Work on this node?                             |
| ----------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Primary Conductor Live node   | Yes. You perform the import step on this node. |
| Secondary Conductor Live node | No                                             |
| Each worker node              | Yes. You add the devices on these nodes.       | ## Step A: Add the devices to each Elemental Live node You don't configure these devices manually. Each Elemental Live automatically detects its SDI cards. It creates an _input device_ and _inputs_ for each card, as follows: <br>• One _single-link input_ for each input on the card (so four inputs). Each input is given a unique numerical ID. <br>• One _quad-link input_, if the SDI card supports quad link. The quad-link input is used with 4K quad input. When you're creating a profile, select this quad-link input to indicate to AWS Elemental Live that the four inputs on this SDI card are the four parts of a quad-link input. ## Step B: Import the devices into the cluster After you have added the devices on each Elemental Live node, you still need to import the devices so that primary Conductor Live detects the devices. You will perform this step when you [add the worker nodes to the cluster](conductor-live-config-nodes-add.md "conductor-live-config-nodes-add.md"). To verify the import, go to the **Settings** page and choose **Devices**. If any devices are missing, you might have forgotten to import them. After you have imported a device, users will be able to select **SDI Direct Input** as the input type when they create a profile in Conductor Live. |
