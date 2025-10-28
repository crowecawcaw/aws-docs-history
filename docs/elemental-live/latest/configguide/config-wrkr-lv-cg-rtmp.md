# Enable RTMP inputs

Elemental Live is configured by default to support Real Time Messaging Protocol (RTMP)
inputs. To confirm that this feature is enabled, do the following:

1. On the Elemental Live web interface, choose **Settings** and then
   select the **Advanced** tab.
2. Locate the RTMP fields and verify that they have the following values:
   - **Enable RTMP input**: Checked.
   - **RTMP input port**: Specifies the desired port. The default port
     (1935) is already enabled on the node. If you specify a different port, you have to open
     it on the firewall. For firewall help, see [Open ports on the firewall for Elemental Live nodes](config-wrkr-cf-cg-firewall.md "config-wrkr-cf-cg-firewall.md").

###### Note

The remaining fields on the **Advanced** tab aren't used in the initial
configuration. They relate to fine-tuning the node load-balancing if the node is in a cluster.
Therefore, we do not address these fields in this guide.
