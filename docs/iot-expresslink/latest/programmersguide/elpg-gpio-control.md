# 14 GPIO control (new with v1.3)

General Purpose I/O control is provided to allow ExpressLink modules to act as I/O expanders for the host processor by allowing control with
serial interface of additional pins beyond the basic set defined in section 2.2.
This command group is optional, and dependent on the capabilities of the connectivity module and underlying SoC.
GPIOs will be numbered 0..MaxIO and made available individually to operate in digital and analog input/output modes, as available.
Each I/O has an associated output register which can be set independently of the control mode.
Reading I/O inputs will always report the current state of the pin.

`14.1.1.1`   The number of GPIO pins available (MaxIO), their physical location and DC characteristics (current drive, voltage thresholds)
is dependent on the specific module (and underlying SoC) capabilities and must be detailed in the vendor module datasheet.

`14.1.1.2`   Testing of the GPIO functionality is limited to a few pins during the device qualification,
leaving to the partner the responsibility to ensure its proper operation on all pins supported.

`14.1.1.3`   Pin configuration is volatile and is initially set to all digital inputs after a power cycle or a reset command.

## 14.1.2 GPIO# SET »Set pin output value to high«

Set the GPIO# pin to a logic high value.

###### Returns:

`14.1.2.1`   `OK 1*{EOL}*`

Returns the new output register value.

`14.1.2.2`   `ERR7 OUT OF RANGE*{EOL}*`

If the # index is greater than the available number of GPIOs.

`14.1.2.3`   `ERR25 NOT ALLOWED*{EOL}*`

If the GPIO is configured in an analog mode (input or output).

## 14.1.3 GPIO# CLR »Set pin output value to low«

Sets the GPIO# pin to a logic low value.

###### Returns:

`14.1.3.1`   `OK 0*{EOL}*`

Returns the new output register value.

`14.1.3.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.3.3`   `ERR25 NOT ALLOWED*{EOL}*`

The GPIO is configured in analog mode (input or output).

## 14.1.4 GPIO# TOGGLE »Toggle output value«

Inverts the output logic value of the GPIO# pin.

###### Returns:

`14.1.4.1`   `OK 0/1*{EOL}*`

Returns the new output register value.

`14.1.4.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.4.3`   `ERR25 NOT ALLOWED*{EOL}*`

The GPIO is configured in analog mode (input or output).

## 14.1.5 GPIO# OUTPUT »Enable output mode«

Enables the GPIO# pin digital output mode and publishes the current output register value to the pin.

###### Returns:

`14.1.5.1`   `OK 0/1*{EOL}*`

Returns the current output register binary value.

`14.1.5.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.5.3`   `ERR17 MODE NOT AVAILABLE*{EOL}*`

The GPIO cannot be configured as a digital output.

Example:

```
AT+GPIO1 SET{EOL}                    # Set the output register of pin1 to high
OK 1{EOL}

AT+GPIO1 OUTPUT{EOL}                 # Set pin1 to output mode (i.e., to turn on an LED)
OK 1{EOL}

AT+SLEEP 1{EOL}                      # Wait for 1 second
OK{EOL}

AT+GPIO1 TOGGLE{EOL}                 # Toggle the pin (turn the LED off)
OK 0{EOL}
```

## 14.1.6 GPIO# INPUT »Enable input mode«

Sets the pin mode to digital input mode and releases the pin output control.

###### Returns:

`14.1.6.1`   `OK 0/1*{EOL}*`

Returns the current digital input value.

`14.1.6.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.6.3`   `ERR17 MODE NOT AVAILABLE*{EOL}*`

The GPIO cannot be configured as a digital input.

## 14.1.7 GPIO# READ »Read current pin value«

Reads the input value of the GPIO. If the pin is configured for digital input or output modes, this returns the current logic value present on the actual pin. If the GPIO# is configured for analog input or output modes, this returns the current ADC reading or the output register (decimal integer) value.

###### Returns:

`14.1.7.1`   `OK *{value}**{EOL}*`

Returns the current GPIO value.

`14.1.7.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

Example:

```
AT+GPIO2 INPUT{EOL}                 # Make pin2 an input (i.e., sensing a push button)
OK 1{EOL}                           # Returns current input value (push button not pressed)

...

AT+GPIO2 READ{EOL}                  # Read the current value of pin2
OK 0{EOL}                           # Input is low (the push button is being pressed)
```

## 14.1.8 GPIO# ANALOG »Enable analog input mode«

The maximum integer (IOMaxInt) value is provided in the response to allow the host processor to scale the following readings. This command implementation is optional and must be documented on the device datasheet if available.

`14.1.8.1`   The IOMaxInt value depends on the module ADC resolution (IOMaxInt = 2^resolution) and must be documented in the module datasheet.

###### Returns:

`14.1.8.2`   `OK *{IOMaxInt}**{EOL}*`

Returns the maximum input integer value.

`14.1.8.3`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.8.4`   `ERR17 MODE NOT AVAILABLE*{EOL}*`

The GPIO cannot be configured as an analog input.

Example:

```
AT+GPIO3 ANALOG{EOL}                # Configure pin3 as analog input (i.e., potentiometer)
OK 1024{EOL}                        # A 10-bit resolution ADC is available on this module

AT+GPIO3 READ{EOL}                  # Sample pin3 and convert the analog input
OK 512{EOL}                         # The analog input is at mid-scale (potentiometer middle)
```

## 14.1.9 GPIO# DAC »Enable analog output mode«

Disconnects the digital output logic and enables the digital to analog (DAC) feature. Publishes the output value. The maximum integer (IOMaxInt) value is provided in the response to allow the host processor to scale the output values. This command implementation is optional and must be documented on the device datasheet if available.

###### Returns:

`14.1.9.1`   `OK *{IOMaxInt}**{EOL}*`

Returns the maximum output integer value.

`14.1.9.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.9.3`   `ERR17 MODE NOT AVAILABLE*{EOL}*`

The GPIO cannot be configured as an analog output.

## 14.1.10 GPIO# WRITE {value} »Set a new output register value«

Assigns a new value to GPIO# pin output register. You can use this command to assign non-binary values to the output register (e.g., to assign analog outputs). This command implementation is optional and must be documented on the device datasheet if available.

###### Returns:

`14.1.10.1`   `OK *{value}**{EOL}*`

Returns the new output register value.

`14.1.10.2`   `ERR7 OUT OF RANGE*{EOL}*`

The # index exceeds the available number of GPIOs.

`14.1.10.3`  

If the assigned new value is greater than IOMaxInt for the GPIO current mode, the new value is _reduced modulo IOMaxInt_.

Example 1 - Analog output write:

```
AT+GPIO4 DAC{EOL}                   # Enable analog output mode
OK 256{EOL}                         # An 8-bit DAC is available on this pin

AT+GPIO4 WRITE 64{EOL}              # Set the output to ¼ of the scale
OK 64{EOL}                          # The actual output value
```

Example 2 - Digital output write:

```
AT+GPIO4 OUTPUT{EOL}                # Enable digital output
OK 0{EOL}                           # Current output register value

AT+GPIO4 WRITE 33{EOL}              # Write a new value to the output register
OK 0{EOL}                           # The actual output value (33 mod 1)
```

Example 3 - Analog output write, exceeding IOMaxInt:

```
AT+GPIO4 DAC{EOL}                   # Enable analog output mode
OK 256{EOL}                         # An 8-bit DAC is available on this pin

AT+GPIO4 WRITE 356{EOL}             # Set the output to a value larger than IOMaxInt
OK 100{EOL}                         # The actual output value (356 mod IOMaxInt)
```
