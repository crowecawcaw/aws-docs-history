

# Configuring virtual input switching
<a name="config-conductor-live-vips"></a>

On ECL3; node, you can configure the maximum number of virtual inputs allowed with the virtual input switching feature. The default is 8 inputs on the node. For information about this feature, see [*AWS Elemental Live User Guide*](https://docs.aws.amazon.com/elemental-live/latest/ug).

**To set the number of virtual inputs**

If you want to enable this feature after you've enabled user authentication, you must log into the Elemental Live node as an administrator. Regular users can't log into the worker nodes.

1. On the Elemental Live web interface, go to **Settings** and choose **Advanced**.

1. Enter a number in **Maximum number of virtual inputs**.