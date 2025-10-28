# Opting out of usage tracking for DLAMI instances

The following AWS Deep Learning AMIs operating system distributions include code that allows AWS to collect instance type, instance ID, DLAMI type, and OS information.

###### Note

AWS doesn't collect or retain any other information about the DLAMI, such as the commands that you use within the DLAMI.

- Amazon Linux 2
- Amazon Linux 2023
- Ubuntu 20.04
- Ubuntu 22.04
  **To opt out of usage tracking**

If you choose, you can opt out of usage tracking for a new DLAMI instance. To opt out, you must add a tag to your Amazon EC2 instance during launch. The tag should use the key `OPT_OUT_TRACKING` with the associated value set to `true`. For more information, see [Tag your Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") in the _Amazon EC2 User Guide_.
