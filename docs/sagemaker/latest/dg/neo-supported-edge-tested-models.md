# Tested Models

The following collapsible sections provide information about machine learning models
that were tested by the Amazon SageMaker Neo team. Expand the collapsible
section based on your framework to check if a model was tested.

###### Note

This is not a comprehensive list of models
that can be compiled with Neo.

See [Supported Frameworks](neo-supported-devices-edge-frameworks.md "neo-supported-devices-edge-frameworks.md") and
[SageMaker AI
Neo Supported Operators](https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/ "https://aws.amazon.com/releasenotes/sagemaker-neo-supported-frameworks-and-operators/") to find out if you can compile your model with SageMaker Neo.

| Models      | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| ----------- | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| Alexnet     |        |          |                |        |          |           |                 |           |             |
| Resnet50    | X      | X        |                | X      | X        | X         |                 | X         | X           |
| YOLOv2      |        |          |                | X      | X        | X         |                 | X         | X           |
| YOLOv2_tiny | X      | X        |                | X      | X        | X         |                 | X         | X           |
| YOLOv3_416  |        |          |                | X      | X        | X         |                 | X         | X           |
| YOLOv3_tiny | X      | X        |                | X      | X        | X         |                 | X         | X           |

| Models                    | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| ------------------------- | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| Alexnet                   |        |          | X              |        |          |           |                 |           |             |
| Densenet121               |        |          | X              |        |          |           |                 |           |             |
| DenseNet201               | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| GoogLeNet                 | X      | X        |                | X      | X        | X         |                 | X         | X           |
| InceptionV3               |        |          |                | X      | X        | X         |                 | X         | X           |
| MobileNet0.75             | X      | X        |                | X      | X        | X         |                 |           | X           |
| MobileNet1.0              | X      | X        | X              | X      | X        | X         |                 |           | X           |
| MobileNetV2_0.5           | X      | X        |                | X      | X        | X         |                 |           | X           |
| MobileNetV2_1.0           | X      | X        | X              | X      | X        | X         | X               | X         | X           |
| MobileNetV3_Large         | X      | X        | X              | X      | X        | X         | X               | X         | X           |
| MobileNetV3_Small         | X      | X        | X              | X      | X        | X         | X               | X         | X           |
| ResNeSt50                 |        |          |                | X      | X        |           |                 | X         | X           |
| ResNet18_v1               | X      | X        | X              | X      | X        | X         |                 |           | X           |
| ResNet18_v2               | X      | X        |                | X      | X        | X         |                 |           | X           |
| ResNet50_v1               | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| ResNet50_v2               | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| ResNext101_32x4d          |        |          |                |        |          |           |                 |           |             |
| ResNext50_32x4d           | X      |          | X              | X      | X        |           |                 | X         | X           |
| SENet_154                 |        |          |                | X      | X        | X         |                 | X         | X           |
| SE_ResNext50_32x4d        | X      | X        |                | X      | X        | X         |                 | X         | X           |
| SqueezeNet1.0             | X      | X        | X              | X      | X        | X         |                 |           | X           |
| SqueezeNet1.1             | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| VGG11                     | X      | X        | X              | X      | X        |           |                 | X         | X           |
| Xception                  | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| darknet53                 | X      | X        |                | X      | X        | X         |                 | X         | X           |
| resnet18_v1b_0.89         | X      | X        |                | X      | X        | X         |                 |           | X           |
| resnet50_v1d_0.11         | X      | X        |                | X      | X        | X         |                 |           | X           |
| resnet50_v1d_0.86         | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| ssd_512_mobilenet1.0_coco | X      |          | X              | X      | X        | X         |                 | X         | X           |
| ssd_512_mobilenet1.0_voc  | X      |          | X              | X      | X        | X         |                 | X         | X           |
| ssd_resnet50_v1           | X      |          | X              | X      | X        |           |                 | X         | X           |
| yolo3_darknet53_coco      | X      |          |                | X      | X        |           |                 | X         | X           |
| yolo3_mobilenet1.0_coco   | X      | X        |                | X      | X        | X         |                 | X         | X           |
| deeplab_resnet50          |        |          | X              |        |          |           |                 |           |             |

| Models       | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| ------------ | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| densenet121  | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| densenet201  | X      | X        | X              | X      | X        | X         |                 |           | X           |
| inception_v3 | X      | X        |                | X      | X        | X         |                 | X         | X           |
| mobilenet_v1 | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| mobilenet_v2 | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| resnet152_v1 |        |          |                | X      | X        |           |                 |           | X           |
| resnet152_v2 |        |          |                | X      | X        |           |                 |           | X           |
| resnet50_v1  | X      | X        | X              | X      | X        |           |                 | X         | X           |
| resnet50_v2  | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| vgg16        |        |          | X              | X      | X        |           |                 | X         | X           |

| Models          | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| --------------- | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| alexnet         |        |          | X              |        |          |           |                 |           |             |
| mobilenetv2-1.0 | X      | X        | X              | X      | X        | X         |                 | X         | X           |
| resnet18v1      | X      |          |                | X      | X        |           |                 |           | X           |
| resnet18v2      | X      |          |                | X      | X        |           |                 |           | X           |
| resnet50v1      | X      |          | X              | X      | X        |           |                 | X         | X           |
| resnet50v2      | X      |          | X              | X      | X        |           |                 | X         | X           |
| resnet152v1     |        |          |                | X      | X        | X         |                 |           | X           |
| resnet152v2     |        |          |                | X      | X        | X         |                 |           | X           |
| squeezenet1.1   | X      |          | X              | X      | X        | X         |                 | X         | X           |
| vgg19           |        |          | X              |        |          |           |                 |           | X           |

| Models                  | ARM V8 | ARM Mali | Ambarella CV22 | Ambarella CV25 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| ----------------------- | ------ | -------- | -------------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| densenet121             | X      | X        | X              | X              | X      | X        | X         |                 | X         | X           |
| inception_v3            |        | X        |                |                | X      | X        | X         |                 | X         | X           |
| resnet152               |        |          |                |                | X      | X        | X         |                 |           | X           |
| resnet18                | X      | X        |                |                | X      | X        | X         |                 |           | X           |
| resnet50                | X      | X        | X              | X              | X      | X        |           |                 | X         | X           |
| squeezenet1.0           | X      | X        |                |                | X      | X        | X         |                 |           | X           |
| squeezenet1.1           | X      | X        | X              | X              | X      | X        | X         |                 | X         | X           |
| yolov4                  |        |          |                |                | X      | X        |           |                 |           |             |
| yolov5                  |        |          |                | X              | X      | X        |           |                 |           |             |
| fasterrcnn_resnet50_fpn |        |          |                |                | X      | X        |           |                 |           |             |
| maskrcnn_resnet50_fpn   |        |          |                |                | X      | X        |           |                 |           |             |

TensorFlow

| Models                            | ARM V8 | ARM Mali | Ambarella CV22 | Ambarella CV25 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| --------------------------------- | ------ | -------- | -------------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| densenet201                       | X      | X        | X              | X              | X      | X        | X         |                 | X         | X           |
| inception_v3                      | X      | X        | X              |                | X      | X        | X         |                 | X         | X           |
| mobilenet100_v1                   | X      | X        | X              |                | X      | X        | X         |                 |           | X           |
| mobilenet100_v2.0                 | X      | X        | X              |                | X      | X        | X         |                 | X         | X           |
| mobilenet130_v2                   | X      | X        |                |                | X      | X        | X         |                 |           | X           |
| mobilenet140_v2                   | X      | X        | X              |                | X      | X        | X         |                 | X         | X           |
| resnet50_v1.5                     | X      | X        |                |                | X      | X        | X         |                 | X         | X           |
| resnet50_v2                       | X      | X        | X              | X              | X      | X        | X         |                 | X         | X           |
| squeezenet                        | X      | X        | X              | X              | X      | X        | X         |                 | X         | X           |
| mask_rcnn_inception_resnet_v2     |        |          |                |                | X      |          |           |                 |           |             |
| ssd_mobilenet_v2                  |        |          |                |                | X      | X        |           |                 |           |             |
| faster_rcnn_resnet50_lowproposals |        |          |                |                | X      |          |           |                 |           |             |
| rfcn_resnet101                    |        |          |                |                | X      |          |           |                 |           |             |

TensorFlow.Keras

| Models       | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows |
| ------------ | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- |
| DenseNet121  | X      | X        |                | X      | X        | X         |                 | X         | X           |
| DenseNet201  | X      | X        |                | X      | X        | X         |                 |           | X           |
| InceptionV3  | X      | X        |                | X      | X        | X         |                 | X         | X           |
| MobileNet    | X      | X        |                | X      | X        | X         |                 | X         | X           |
| MobileNetv2  | X      | X        |                | X      | X        | X         |                 | X         | X           |
| NASNetLarge  |        |          |                | X      | X        |           |                 | X         | X           |
| NASNetMobile | X      | X        |                | X      | X        | X         |                 | X         | X           |
| ResNet101    |        |          |                | X      | X        | X         |                 |           | X           |
| ResNet101V2  |        |          |                | X      | X        | X         |                 |           | X           |
| ResNet152    |        |          |                | X      | X        |           |                 |           | X           |
| ResNet152v2  |        |          |                | X      | X        |           |                 |           | X           |
| ResNet50     | X      | X        |                | X      | X        |           |                 | X         | X           |
| ResNet50V2   | X      | X        |                | X      | X        | X         |                 | X         | X           |
| VGG16        |        |          |                | X      | X        |           |                 | X         | X           |
| Xception     | X      | X        |                | X      | X        | X         |                 | X         | X           |

TensorFlow-Lite (FP32)

| Models                         | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows | i.MX 8M Plus |
| ------------------------------ | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- | ------------ |
| densenet_2018_04_27            | X      |          |                | X      | X        | X         |                 |           | X           |              |
| inception_resnet_v2_2018_04_27 |        |          |                | X      | X        | X         |                 |           | X           |              |
| inception_v3_2018_04_27        |        |          |                | X      | X        | X         |                 |           | X           | X            |
| inception_v4_2018_04_27        |        |          |                | X      | X        | X         |                 |           | X           | X            |
| mnasnet_0.5_224_09_07_2018     | X      |          |                | X      | X        | X         |                 |           | X           |              |
| mnasnet_1.0_224_09_07_2018     | X      |          |                | X      | X        | X         |                 |           | X           |              |
| mnasnet_1.3_224_09_07_2018     | X      |          |                | X      | X        | X         |                 |           | X           |              |
| mobilenet_v1_0.25_128          | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_0.25_224          | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_0.5_128           | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_0.5_224           | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_0.75_128          | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_0.75_224          | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_1.0_128           | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v1_1.0_192           | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| mobilenet_v2_1.0_224           | X      |          |                | X      | X        | X         |                 |           | X           | X            |
| resnet_v2_101                  |        |          |                | X      | X        | X         |                 |           | X           |              |
| squeezenet_2018_04_27          | X      |          |                | X      | X        | X         |                 |           | X           |              |

TensorFlow-Lite (INT8)

| Models                | ARM V8 | ARM Mali | Ambarella CV22 | Nvidia | Panorama | TI TDA4VM | Qualcomm QCS603 | X86_Linux | X86_Windows | i.MX 8M Plus |
| --------------------- | ------ | -------- | -------------- | ------ | -------- | --------- | --------------- | --------- | ----------- | ------------ |
| inception_v1          |        |          |                |        |          |           | X               |           |             | X            |
| inception_v2          |        |          |                |        |          |           | X               |           |             | X            |
| inception_v3          | X      |          |                |        |          | X         | X               |           | X           | X            |
| inception_v4_299      | X      |          |                |        |          | X         | X               |           | X           | X            |
| mobilenet_v1_0.25_128 | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_0.25_224 | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_0.5_128  | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_0.5_224  | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_0.75_128 | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_0.75_224 | X      |          |                |        |          | X         | X               |           | X           | X            |
| mobilenet_v1_1.0_128  | X      |          |                |        |          | X         |                 |           | X           | X            |
| mobilenet_v1_1.0_224  | X      |          |                |        |          | X         | X               |           | X           | X            |
| mobilenet_v2_1.0_224  | X      |          |                |        |          | X         | X               |           | X           | X            |
| deeplab-v3_513        |        |          |                |        |          |           | X               |           |             |              |
