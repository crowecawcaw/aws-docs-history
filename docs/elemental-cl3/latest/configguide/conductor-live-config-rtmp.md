# Configuring for RTMP

inputs

The Elemental Live nodes are configured by default to support RTMP inputs. In
this mode, Elemental Live is using processing resources to continually poll for input
at the RTMP port. If you don't plan to support RTMP inputs, you can choose
to disable these inputs, to release the processing resources.

###### To disable polling for RTMP inputs

If you want to enable this feature after you've enabled user
authentication, you must log into the Elemental Live node as an administrator.
Regular users can't log into the worker nodes.

1. On the Elemental Live web interface, go to **Settings**
   and choose **Advanced**.
2. Set **Enable RTMP input** to unselected.
