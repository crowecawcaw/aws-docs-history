# Printing from a WorkSpace

The following printing methods are supported by Amazon WorkSpaces.

###### Note

- The WorkSpaces clients for iPad, Android, Chromebook, Web Access,
  and Linux support network printing and cloud printing services. Local printing is not currently supported
  for the iPad, Android, Chromebook, Web Access, and Linux clients.
- Local printer redirection is not available for Linux WorkSpaces, regardless of the client being used to
  access them.
- If you're using a PCoIP zero client device to connect to your WorkSpace and you're having trouble using a
  USB printer or other USB peripheral devices, contact your WorkSpaces administrator for assistance. For more
  information, see [USB printers and other USB peripherals aren't working for PCoIP zero clients](../adminguide/amazon-workspaces-troubleshooting.md#pcoip_zero_client_usb "../adminguide/amazon-workspaces-troubleshooting.md#pcoip_zero_client_usb") in the
  _Amazon WorkSpaces Administration Guide_.

###### Printing methods

- [Local printers](#local_printers "#local_printers")
- [Other printing methods](#other_printing "#other_printing")

## Local printers

Windows WorkSpaces support local printer redirection. When you print from an application in your
WorkSpace, the local printers are contained in your list of available printers. The
local printers have "(Local – `workspace username`.`directory
 name`.`client computer name`)" appended to the
printer's display name. Select one of the local printers and your documents are printed
on that printer.

In some cases, you need to download and install the driver for your local printer
manually on the WorkSpace. When you install a printer driver on your WorkSpace, there
are different types of drivers that you might encounter:

- Add Printer wizard driver. This driver includes only the printer drivers, and
  is for users who are familiar with installation using the Add Printer wizard in
  Windows.
- Printer model-specific drivers that do not require communication with the
  printer. In these cases, you can install the printer driver directly.
- Printer model-specific drivers that require communication with the printer.
  In these cases, you can use the printer driver files to add a local printer
  using an existing port (LPT1:). After selecting the port, you can choose
  **Have Disk** and select the `.INF` file
  for the printer driver.

After installing the printer driver, you must [restart (reboot) the WorkSpace](client-restart-workspace.md "client-restart-workspace.md") for the new printer to be recognized.

If you cannot print to your local printer from your WorkSpace, make sure that you can
print to your local printer from your client computer. If you cannot print from your
client computer, refer to the printer documentation and support to resolve the issue. If
you can print from your client computer, contact [AWS Support](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") for further assistance.

## Other printing methods

You can also use one of the following methods to print from a Windows or Linux WorkSpace:

- If your organization exposes printers through Active Directory, you can connect your
  WorkSpace to printers on your internal company network.
- Print to a file, transfer the file to your local desktop and print the file
  locally to an attached printer.
