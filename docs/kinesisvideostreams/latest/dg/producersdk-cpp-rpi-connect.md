# Connect remotely to your Raspberry Pi

If you are using an attached monitor and keyboard, proceed to [Configure the Raspberry Pi camera](producersdk-cpp-rpi-camera.md "producersdk-cpp-rpi-camera.md").

These instructions are written to help you to set up your Raspberry Pi when run in
_headless_ mode, that is, without an attached
keyboard, monitor, or network cable. Follow the instructions below to locate your
Raspberry Pi on your network and SSH into it from your host machine.

1.  Before connecting to your Raspberry Pi device remotely, do one of the
    following to determine its IP address:
    - If you have access to your network's Wi-Fi router, look at the
      connected Wi-Fi devices. Find the device named `Raspberry
Pi` to find your device's IP address.
    - If you don't have access to your network's Wi-Fi router, you can use
      other software to find devices on your network. [Fing](https://www.fing.com/ "https://www.fing.com/") is a popular application
      that is available for both Android and iOS devices. You can use the free
      version of this application to find the IP addresses of devices on your
      network.

2.  When you know the IP address of the Raspberry Pi device, you can use any
    terminal application to connect.

        * On macOS or Linux, use `ssh`:



        ```
        ssh pi@`<IP address>`
        ```
        * On Windows, use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html "https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html"), a free SSH client for Windows.

    For a new installation of Raspbian, the user name is
    `pi`, and the password is `raspberry`.
    We recommend that you [change
    the default password](https://www.raspberrypi.com/documentation/computers/configuration.html#change-user-password-nonint "https://www.raspberrypi.com/documentation/computers/configuration.html#change-user-password-nonint").
