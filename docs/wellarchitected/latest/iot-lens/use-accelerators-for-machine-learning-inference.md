# Use accelerators for machine learning inference

Performing Machine Learning (ML) inference on the IoT device can
greatly reduce the amount of data transmitted to the cloud.  ML
inference is a computationally intensive process which might not
be energy optimal when run on a CPU without the right
instruction set.  For ML applications, the use of a CPU with
additional vector operations and specialized acceleration
hardware can lower the energy consumption of IoT devices.

Inference-class devices can come in various forms such as GPUs
(Graphics Processing Units), NPUs (Neural Processing Units),
Digital Signal Processors (DSPs) and FPGA (Field-Programmable
Gate Array) devices or CPUs with vector manipulation operators.

If there are no performance or latency constraints in the
workload it might be preferable to run inference on standard MCU
devices, for cost and energy savings. For further optimization,
resources such as
[TinyEngine](https://github.com/mit-han-lab/tinyengine "https://github.com/mit-han-lab/tinyengine")
and other frameworks can be used to run machine learning models
directly on the microcontroller.  

When lower latency than what is achievable by the MCUs is
desired, specialized hardware accelerators for ML tasks, such as
built-in
[Digital
Signal Processors (DSPs)](https://www.sciencedirect.com/topics/computer-science/digital-signal-processor "https://www.sciencedirect.com/topics/computer-science/digital-signal-processor") or ML accelerators, can provide
efficient ML inferencing at the edge with lower power
consumption.

DSPs are designed to perform mathematical functions quickly
without using the host MCU's clock cycles. They are more power
efficient than an MCU. In a typical DSP-accelerated ML
application, such as wake-word detection in a smart speaker, the
DSP first processes an analog signal such as an audio or voice
signal and then wakes up the host MCU from a deep-sleep mode via
an interrupt. The processor can thus remain in a low-power mode
while performing inference, and only wakes up when necessary for
further processing or connection to the cloud.

MPUs are suitable for edge ML applications that require higher
processing capabilities, such as running more complex ML models
or handling larger input datasets. MPUs may also have built-in
hardware accelerators for ML tasks, such as Neural Processing
Units (NPUs) which improves ML inferencing performance.

NPUs are optimized for artificial neural networks. If your
application involves inference using deep neural networks, such
as image recognition, natural language processing, or
recommendation systems, an NPU can provide inference
acceleration and an order of magnitude or more energy efficiency
compared to general-purpose CPUs or GPUs. 

GPUs are specialized processors designed for graphics-intensive
tasks, but can offer high performance for ML inference. If you
are already using a deep learning framework or software that is
optimized for GPUs, it may be more convenient to continue using
GPUs. GPUs are not power efficient and should only be selected
for the highest intensity workloads.
