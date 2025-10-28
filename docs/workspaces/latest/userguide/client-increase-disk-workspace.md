# Increasing WorkSpace disk size

You can increase your WorkSpace disk size to add more storage capacity. You can
increase the size of your C: drive (for Linux, this is /) up to 175 GB, and you can
increase the size of your D: drive (for Linux, this is /home) up to 100 GB without
contacting your administrator. If you need your drives increased beyond these limits,
your administrator must increase the sizes of your drives for you.

If your administrator recently created your WorkSpace, you must wait 6 hours before
you can increase your WorkSpace disk sizes. After that, you can increase your disk sizes
once in a 6-hour period.

You cannot increase the size of the C: and D: drives at the same time. (The same is
true of the / and /home volumes in Linux.) To increase the C: drive (or / in Linux), you
must first increase the D: drive (or /home in Linux) to 100 GB. After the D: drive (or
/home in Linux) has been increased, you can increase the C: drive (or / in
Linux).

While your WorkSpace disk size increase is in progress, you can perform most tasks on
your WorkSpace. However, you can't change your WorkSpace compute type, switch the
WorkSpace running mode, rebuild your WorkSpace, or restart your WorkSpace. The disk size
increase process might take up to an hour.

###### Important

- You can resize only SSD volumes.
- Increasing your WorkSpace disk size will increase the amount that your
  organization pays for your WorkSpace.

###### To increase your WorkSpace disk size

1. Open your WorkSpaces client and connect to your WorkSpace.
2. Depending on which client you're using, do one of the following.

| If you're using...  | Do this                                          |
| ------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 3.0+ client         | Choose **Settings**, **Increase Disk Size**.     |
| 1.0+ or 2.0+ client | Choose **My WorkSpace**, **Increase disk size**. | 3. The **Increase disk size** dialog box displays the current disk size of your C: drive and D: drive (or / and /home in Linux). If you proceed with the disk size increase, it also displays the amount by which your storage increases. 4. To proceed with the disk size increase, choose **Increase**. 5. A message displays information about the disk size increase process. Review the information, and choose **Close**. 6. When the disk size increase is finished, you must [restart the WorkSpace](client-restart-workspace.md "client-restart-workspace.md") for the changes to take effect. Save any open files before restarting the WorkSpace. |
