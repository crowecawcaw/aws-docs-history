# Optimize ML models for the edge

Leveraging edge computing for machine learning (ML) inference
and analytics can offer several benefits compared to processing
data in the cloud. Pre-processing and real-time data analysis
and decision making can be done locally, reducing the need for
frequent data transfers to the cloud, thereby reducing messaging
costs, computing power requirements, and the energy consumption
associated with data transmission as well as processing in the
cloud.

Machine learning is a computationally expensive task.  Choose
machine learning frameworks and algorithms that are optimized
for low-power consumption and can run on hardware accelerators.
Models can be developed in the cloud, and then optimized for
edge devices with frameworks such as the Open Neural Network
Exchange, [ONNX,](https://onnx.ai/ "https://onnx.ai/")
before being deployed to the device.

The size and complexity of ML models can impact their
suitability for edge deployment. Techniques such as model
quantization, compression, and pruning can help reduce the size
of ML models, making them more suitable for deployment on edge
devices.

ML models should be observable while deployed on edge devices in
order to detect if the model is being affected by changing data
or model drift. When negative model performance is detected,
updating the model over the air increases the device's useful
lifetime, reducing the need for replacement.
