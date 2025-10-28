# Choose an operating system that is appropriate for the type of device's features and functionality

The operating system can greatly impact how power efficient an
IoT device is.

Try to choose an operating system that is appropriate for the
type of device's features and functionality.  For example,
choosing Android or Linux for a simple temperature sensor may be
more convenient for the developer, but is not sustainable
practice due to its impact on the device's resource dimensions
and consequent carbon footprint.

Consider features in the operating system that support low power
modes, power management, and operational efficiency.  Operating
systems must support low power modes that allow the system to
conserve power when idle or when certain subsystems are not in
use. For example, an embedded system might use a sleep mode to
conserve power when the user is not interacting with the system,
or it might shut down peripherals or subsystems that are not
currently in use. The operating system should expose the
hardware's low power modes such that applications can take
advantage of these modes.

Some operating systems support tick-less operation, where the
operating system avoids unnecessary timer interrupts, further
reducing power consumption. For example, FreeRTOS stops the
periodic tick interrupt during periods when there are no
application tasks that are able to execute. Stopping the tick
interrupt allows the microcontroller to remain in a deep power
saving mode until an event occurs or the kernel is ready to
execute a task.

Dynamic voltage and frequency scaling (DVFS) operations adjust
the CPU performance and frequency based on the application
workload's demands. Operating systems that support DVFS can
decrease the CPU's voltage in real time during decreased
workloads, reducing power consumption.
