# AWS IoT TwinMaker

Grafana dashboard integration

AWS IoT TwinMaker supports Grafana integration through an application plugin. Use Grafana
version 10.4.0 and later versions to interact with your digital twin application. The AWS IoT TwinMaker plugin
provides custom panels, dashboard templates, and a datasource to connect to your digital twin
data.

For more information about how to onboard with Grafana and set up permissions for your
dashboard, see the following topics:

###### Topics

- [CORS configuration for Grafana scene viewer](cors-configuration-grafana.md "cors-configuration-grafana.md")
- [Setting up your Grafana environment](grafana-environment.md "grafana-environment.md")
- [Creating a dashboard IAM role](dashboard-IAM-role.md "dashboard-IAM-role.md")
- [Creating an AWS IoT TwinMaker video player policy](tm-video-policy.md "tm-video-policy.md")

###### Note

You need to modify CORS (cross-origin resource sharing) configuration of the Amazon S3
bucket to allow the Grafana user interface to load resources from the bucket.
For the instructions, see [CORS configuration for Grafana scene viewer](cors-configuration-grafana.md "cors-configuration-grafana.md").

For more information about the AWS IoT TwinMaker Grafana plugin, see the [AWS IoT TwinMaker App](https://grafana.com/grafana/plugins/grafana-iot-twinmaker-app/ "https://grafana.com/grafana/plugins/grafana-iot-twinmaker-app/")
documentation.

For more information about the key components of the Grafana plugin, see the
following:

- [AWS IoT TwinMaker datasource](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/datasource/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/datasource/README.md")
- [Dashboard templates](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/datasource/dashboards/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/datasource/dashboards/README.md")
- [Scene Viewer panel](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/scene-viewer/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/scene-viewer/README.md")
- [Video Player panel](https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/video-player/README.md "https://github.com/grafana/grafana-iot-twinmaker-app/blob/main/src/panels/video-player/README.md")
