# Develop EC2Rescue modules for Amazon EC2 Linux instances

Modules are written in YAML, a data serialization standard. A module's YAML file consists
of a single document, representing the module and its attributes.

## Add module attributes

The following table lists the available module attributes.

| Attribute         | Description                                                                                                                                                                                                                                                                   |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name              | The name of the module. The name should be less than or equal to 18<br>characters in length.                                                                                                                                                                                  |
| version           | The version number of the module.                                                                                                                                                                                                                                             |
| title             | A short, descriptive title for the module. This value should be less than<br>or equal to 50 characters in length.                                                                                                                                                             |
| helptext          | The extended description of the module. Each line should be less than or equal<br>to 75 characters in length. If the module consumes arguments, required or<br>optional, include them in the helptext value.<br>For example:<br>```<br>helptext: !!str                        | <br>Collect output from ps for system analysis<br>Consumes --times= for number of times to repeat<br>Consumes --period= for time period between repetition<br>``` |
| placement         | The stage in which the module should be run. Supported values:<br>• prediagnostic<br>• run<br>• postdiagnostic                                                                                                                                                                |
| language          | The language that the module code is written in. Supported values:<br>• bash<br>• python<br>NotePython code must be compatible with both Python 2.7.9+ and Python<br>3.2+.                                                                                                    |
| remediation       | Indicates whether the module supports remediation. Supported values are<br>`True` or `False`.<br>The module defaults to `False` if this is absent, making it an<br>optional attribute for those modules that do not support remediation.                                      |
| content           | The entirety of the script code.                                                                                                                                                                                                                                              |
| constraint        | The name of the object containing the constraint values.                                                                                                                                                                                                                      |
| domain            | A descriptor of how the module is grouped or classified. The set of<br>included modules uses the following domains:<br>• application<br>• net<br>• os<br>• performance                                                                                                        |
| class             | A descriptor of the type of task performed by the module. The set of<br>included modules uses the following classes:<br>• collect (collects output from programs)<br>• diagnose (pass/fail based on a set of criteria)<br>• gather (copies files and writes to specific file) |
| distro            | The list of Linux distributions that this module supports. The set of<br>included modules uses the following distributions:<br>• **alami** (Amazon Linux)<br>• **rhel**<br>• **ubuntu**<br>• **suse**                                                                         |
| required          | The required arguments that the module is consuming from the CLI<br>options.                                                                                                                                                                                                  |
| optional          | The optional arguments that the module can use.                                                                                                                                                                                                                               |
| software          | The software executables used in the module. This attribute is intended<br>to specify software that is not installed by default. The EC2Rescue for Linux<br>logic ensures that these programs are present and executable before running the<br>module.                        |
| package           | The source software package for an executable. This attribute is intended<br>to provide extended details on the package with the software, including a URL for<br>downloading or getting further information.                                                                 |
| sudo              | Indicates whether root access is required to run the module.<br>You do not need to implement sudo checks in the module script. If the value is<br>true, then the EC2Rescue for Linux logic only runs the module when the executing<br>user has root access.                   |
| perfimpact        | Indicates whether the module can have significant performance impact upon<br>the environment in which it is run. If the value is true and the<br>`--perfimpact=true` argument is not present, then the module is<br>skipped.                                                  |
| parallelexclusive | Specifies a program that requires mutual exclusivity. For example, all<br>modules specifying "bpf" run in a serial manner.                                                                                                                                                    |

## Add environment variables

The following table lists the available environment variables.

| Environment Variable | Description                                                                                                                                                                                                                      |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EC2RL_CALLPATH`     | The path to `ec2rl.py`. This path can be used to locate the<br>lib directory and use vendored Python modules.                                                                                                                    |
| `EC2RL_WORKDIR`      | The main tmp directory for the diagnostic tool.<br>Default value: `/var/tmp/ec2rl`.                                                                                                                                              |
| `EC2RL_RUNDIR`       | The directory where all output is stored.<br>Default value:<br>`/var/tmp/ec2rl/<date&timestamp>`.                                                                                                                                |
| `EC2RL_GATHEREDDIR`  | The root directory for placing gathered module data.<br>Default<br>value:`/var/tmp/ec2rl/<date&timestamp>/mod_out/gathered/`.                                                                                                    |
| `EC2RL_NET_DRIVER`   | The driver in use for the first, alphabetically ordered, non-virtual network<br>interface on the instance.<br>Examples:<br>• xen_netfront<br>• ixgbevf<br>• ena                                                                  |
| `EC2RL_SUDO`         | True if EC2Rescue for Linux is running as root; otherwise, false.                                                                                                                                                                |
| `EC2RL_VIRT_TYPE`    | The virtualization type as provided by the instance metadata.<br>Examples:<br>• default-hvm<br>• default-paravirtual                                                                                                             |
| `EC2RL_INTERFACES`   | An enumerated list of interfaces on the system. The value is a string<br>containing names, such as `eth0`, `eth1`, etc. This is<br>generated via the `functions.bash` and is only available for modules<br>that have sourced it. |

## Use YAML syntax

The following should be noted when constructing your module YAML files:

- The triple hyphen (`---`) denotes the explicit start of a
  document.
- The `!ec2rlcore.module.Module` tag tells the YAML parser which
  constructor to call when creating the object from the data stream. You can find the
  constructor inside the `module.py` file.
- The `!!str` tag tells the YAML parser to not attempt to determine the
  type of data, and instead interpret the content as a string literal.
- The pipe character (`|`) tells the YAML parser that the value is a
  literal-style scalar. In this case, the parser includes all whitespace. This is
  important for modules because indentation and newline characters are kept.
- The YAML standard indent is two spaces, which can be seen in the following examples.
  Ensure that you maintain standard indentation (for example, four spaces for Python) for
  your script and then indent the entire content two spaces inside the module file.

## Example modules

Example one (`mod.d/ps.yaml`):

```
--- !ec2rlcore.module.Module
# Module document. Translates directly into an almost-complete Module object
name: !!str ps
path: !!str
version: !!str 1.0
title: !!str Collect output from ps for system analysis
helptext: !!str |
  Collect output from ps for system analysis
  Requires --times= for number of times to repeat
  Requires --period= for time period between repetition
placement: !!str run
package:
  - !!str
language: !!str bash
content: !!str |
  #!/bin/bash
  error_trap()
  {
      printf "%0.s=" {1..80}
      echo -e "\nERROR:	"$BASH_COMMAND" exited with an error on line ${BASH_LINENO[0]}"
      exit 0
  }
  trap error_trap ERR

  # read-in shared function
  source functions.bash
  echo "I will collect ps output from this $EC2RL_DISTRO box for $times times every $period seconds."
  for i in $(seq 1 $times); do
      ps auxww
      sleep $period
  done
constraint:
  requires_ec2: !!str False
  domain: !!str performance
  class: !!str collect
  distro: !!str alami ubuntu rhel suse
  required: !!str period times
  optional: !!str
  software: !!str
  sudo: !!str False
  perfimpact: !!str False
  parallelexclusive: !!str
```
