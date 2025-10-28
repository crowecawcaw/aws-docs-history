# Updating the production license

The Amazon DCV server checks licenses on the RLM server every few minutes. In case the license is updated on the RLM
server, Amazon DCV server automatically updates the used license for the running sessions. The following procedure details
how to update a DCV license on RLM.

###### To update the DCV license on the RLM server

1. Update the license file which was previously [installed](setting-up-production.md#setting-up-rlm-server "setting-up-production.md#setting-up-rlm-server"). On
   Linux, it should had been placed in `/opt/dcv/rlm/license/license.lic`, on Windows in
   `C:\RLM\license\license.lic`.
2. Run `C:\RLM\rlmutil.exe rlmreread` on Windows or `/opt/nice/rlm/rlmutil rlmreread` on Linux to force the license file reload.

After the license has been updated on the RLM server, the Amazon DCV server should check the use of the new licenses in
a few minutes (usually 5 minutes or less).

Starting from Amazon DCV version 2021.0, you can use the following command **as
administrator** in order to force the license update immediately:

```
`$` dcv reload-licenses
```
