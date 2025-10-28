# Configure the Raspberry Pi camera

Follow these steps to configure the [Raspberry Pi camera module](https://www.raspberrypi.com/documentation/accessories/camera.html "https://www.raspberrypi.com/documentation/accessories/camera.html") to send video from the
device to a Kinesis video stream.

###### Note

If you’re using a USB web cam, skip to [Install software prerequisites](producersdk-cpp-rpi-software.md "producersdk-cpp-rpi-software.md").

Camera module 1
Follow these instructions to update the modules file, enable the camera interface, and verify functionality of your camera. Updating the modules file tells the Raspberry Pi which kernel modules to load at boot time. The camera driver isn't loaded by default in order to conserve system resources on Raspberry Pi devices that aren't using a camera.

1. Open an editor to make changes to the modules file. Open the
   terminal and use the following command to edit the file using the
   `nano` editor:

```
sudo nano /etc/modules
```

2. Add the following line to the end of the file, if it's not already
   there:

```
bcm2835-v4l2
```

3. Save the file and exit the editor. To save and exit using the `nano` editor, use Ctrl+X.
4. Reboot the Raspberry Pi:

```
sudo reboot
```

5. When the device reboots, connect to it again through your terminal application
   if you are connecting remotely.
6. Open `raspi-config`:

```
sudo raspi-config
```

7. Choose **Interfacing Options**, **Legacy
   Camera**. In older builds of the Raspbian Operating System, this
   menu option might be under **Interfacing Options**,
   **Camera**.

Enable the camera if it's not already enabled, and reboot if prompted. 8. Verify that the camera is working by typing the following command:

```
raspistill -v -o test.jpg
```

If your camera is configured correctly, this command captures an image from
the camera, saves it to a file named `test.jpg`, and displays
informational messages.

Camera module 2 or 3If you’re using a Camera module 2, you use either `bcm2835-v4l2` (legacy) or `libcamera` (modern). However, the `libcamera` stack is recommended for better support and features. Follow the steps below to confirm that `libcamera` is up-to-date on your system.

1. [libcamera](https://www.raspberrypi.com/documentation/computers/camera_software.html#libcamera "https://www.raspberrypi.com/documentation/computers/camera_software.html#libcamera") should come pre-installed on your Raspberry
   Pi. Check for any updates and update to the latest version for bug
   fixes and security updates. Open the terminal and type the following
   commands:

```
sudo apt-get update
sudo apt-get upgrade
```

2. Reboot your system for the updates to take effect.

```
sudo reboot
```

3. Test your camera. This application starts a camera preview stream and displays it on the screen.

```
libcamera-hello
```

If you have issues with your camera module, see the [Raspberry Pi documentation](https://raspberrypi.com/documentation/computers/camera_software.html#troubleshooting "https://raspberrypi.com/documentation/computers/camera_software.html#troubleshooting") for troubleshooting.
