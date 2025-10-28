# HTJ2K decoding libraries for AWS HealthImaging

During [import](importing-imaging-data.md "importing-imaging-data.md"), some transfer syntaxes retain
their original encoding, while others are transcoded to High-Throughput JPEG 2000 (HTJ2K) lossless
by default. HTJ2K delivers consistently fast image display and universal access to HTJ2K’s
advanced features. Because some image frames are encoded in HTJ2K during import, they must be
decoded prior to viewing in an image viewer. For information about determining transfer syntaxes,
see [Supported transfer syntaxes](supported-transfer-syntaxes.md "supported-transfer-syntaxes.md").

###### Note

HTJ2K is defined in [Part 15 of the
JPEG2000 standard (ISO/IEC 15444-15:2019)](https://www.iso.org/standard/76621.html "https://www.iso.org/standard/76621.html"). HTJ2K retains the advanced features of
JPEG2000 such as resolution scalability, precincts, tiling, high bit depth, multiple channels,
and color space support.

###### Topics

- [HTJ2K decoding libraries](#decoding-libraries "#decoding-libraries")
- [Image viewers](#web-viewers "#web-viewers")

## HTJ2K decoding libraries

Depending on your programming language, we recommend the following decoding libraries to
decode [image frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame").

- [NVIDIA
  nvJPEG2000](https://docs.nvidia.com/cuda/nvjpeg2000/userguide.html "https://docs.nvidia.com/cuda/nvjpeg2000/userguide.html") – Commercial, GPU-accelerated
- [Kakadu Software](https://kakadusoftware.com/ "https://kakadusoftware.com/") – Commercial, C++
  with Java and .NET bindings
- [OpenJPH](https://github.com/aous72/OpenJPH "https://github.com/aous72/OpenJPH") – Open source, C++
  and WASM
- [OpenJPEG](https://www.openjpeg.org/ "https://www.openjpeg.org/") – Open source, C/C++,
  Java
- [openjphpy](https://github.com/UM2ii/openjphpy "https://github.com/UM2ii/openjphpy") – Open source,
  Python
- [pylibjpeg-openjpeg](https://github.com/pydicom/pylibjpeg-openjpeg/ "https://github.com/pydicom/pylibjpeg-openjpeg/")
  – Open source, Python

## Image viewers

You can view [image frames](getting-started-concepts.md#concept-image-frame "getting-started-concepts.md#concept-image-frame") after you've decoded
them. AWS HealthImaging API actions support a variety of open-source image viewers, including:

- [Open Health Imaging Foundation (OHIF)](https://www.ohif.org/ "https://www.ohif.org/")
- [Cornerstone.js](https://www.cornerstonejs.org/ "https://www.cornerstonejs.org/")
