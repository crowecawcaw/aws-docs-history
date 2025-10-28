# Configuring OCR

Elemental Live includes a feature that lets you convert captions using OCR
conversion. For information about this feature, see [Support for OCR Conversion](../../../elemental-live/latest/ug/support-for-ocr.md "../../../elemental-live/latest/ug/support-for-ocr.md") in the _AWS
Elemental Live User Guide_.

If you want to use this feature, you must enable it. You might have
enabled it when you installed the software on the Elemental Live node. If you
didn't, you can enable it now using the configuration script
(`configure`) instead of the install script. For
example:

```
[elemental@hostname ~]$ **cd /opt/elemental\_se**
[elemental@hostname elemental_se]$ **sudo ./configure --install-ocr --https --skip-all**
```

For complete instructions, see [Install the AWS Elemental Live software](../../../elemental-live/latest/installguide/install-lv-ig-install-sw.md "../../../elemental-live/latest/installguide/install-lv-ig-install-sw.md") in the _AWS Elemental Live Install Guide_.
