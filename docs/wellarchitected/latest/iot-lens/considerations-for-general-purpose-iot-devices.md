# Considerations for General Purpose IoT Devices

For general purpose IoT devices, the application and use case
will determine the choice between microcontroller (MCU) and
microprocessor (MPU). MCU devices are typically designed for
low-power, often autonomously battery-operated, and resource
constrained applications. MPU class devices are designed for
applications that require higher computational power,
multitasking, and higher-level services provided by more capable
operating systems.

For MCU devices, there are several features that can contribute
to improved energy efficiency and sustainability. 

- Support for multiple low power modes, allowing power
  consumption to be reduced when the processor is not active. 
  - This should include a mode that retains volatile memory
    content, allowing for quick restoration of application
    state when required.

- A Real-Time Clock (RTC) to wake-up the device from a low
  power mode only when needed.
- On-chip or on-board crypto-accelerators to enable secure
  communication while minimizing energy consumption.
- Connectivity module low-power and sleep modes to reduce
  unnecessary power drain when not in use.
- Connectivity module should utilize quick reconnect protocols
- If required, support for a floating point unit (FPU) for
  more efficient and faster processing of numerical
  calculations, contributing to improved energy efficiency.

Similar criteria also apply to the selection of MPUs, though
there are differences.  Some MPUs utilize a combination of
high-performance and low-power cores, such as those using the
[big.LITTLE](https://www.arm.com/technologies/big-little "https://www.arm.com/technologies/big-little")
architecture.  In such architectures, make surethat tasks are
assigned to the appropriate core based on the workload. This
reduces power consumption while maintaining sufficient
processing capabilities. The
[FreeRTOS](https://freertos.org/ "https://freertos.org/")
operating system can take advantage of this architecture through
Asymmetric Multiprocessing (AMP). Each core runs an instance of
FreeRTOS and communicates through shared memory space and
inter-process communication (IPC). The smaller core can be
assigned to run non-intensive applications and the big core can
be put into low-power mode until needed for more compute
intensive tasks.
