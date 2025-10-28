# Install software prerequisites

The C++ producer SDK requires that you install the following software prerequisites on
Raspberry Pi.

1. Update the package list and install the libraries needed to build the SDK.
   Open the terminal and type the following commands:

```
sudo apt-get update
sudo apt-get install -y \
  automake \
  build-essential \
  cmake \
  git \
  gstreamer1.0-plugins-base-apps \
  gstreamer1.0-plugins-bad \
  gstreamer1.0-plugins-good \
  gstreamer1.0-plugins-ugly \
  gstreamer1.0-tools \
  gstreamer1.0-omx-generic \
  libcurl4-openssl-dev \
  libgstreamer1.0-dev \
  libgstreamer-plugins-base1.0-dev \
  liblog4cplus-dev \
  libssl-dev \
  pkg-config
```

2. If you’re using the `libcamera` stack, also install the `libcamerasrc` GStreamer plugin. This GStreamer plugin doesn't come installed by default.

```
sudo apt-get install gstreamer1.0-libcamera
```

3. Copy the following PEM file to `/etc/ssl/cert.pem`:

```
sudo curl https://www.amazontrust.com/repository/AmazonRootCA1.pem -o /etc/ssl/AmazonRootCA1.pem
sudo chmod 644 /etc/ssl/AmazonRootCA1.pem
```
