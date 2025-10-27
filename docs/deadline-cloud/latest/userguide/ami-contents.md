# Worker AMI software contents

This section provides information on software installed on AWS Deadline Cloud service-managed worker Amazon Machine Images (AMIs).

AWS Deadline Cloud service-managed worker AMIs are based on both Windows Server 2022 and Amazon Linux 2023, and include additional
software specifically installed to support rendering workloads. These AMIs are continuously updated to maintain functionality.

The software on these AMIs is organized into one of the following support categories:

Service-provided software packages

Software specifically installed and maintained for rendering workloads

Additional system software

All other software that might change without notice

## Service-provided software packages

These software packages are installed to support rendering workloads and are maintained for compatibility. You can
safely take dependencies on these packages.

### Development Tools & Languages

**Linux (AL2023):**

- Python 3.11
- Git

**Windows (Server 2022):**

- Python 3.11
- Git for Windows

### AWS tools

**Both platforms:**

- AWS Command Line Interface v2 (AWS CLI v2)

### System libraries & utilities

**Linux:**

- FUSE and FUSE3 libraries for filesystem operations
- Image Libraries
  - libpng
  - libjpeg
  - libtiff

- OpenGL Libraries
  - mesa-libGLU
  - mesa-libGL
  - mesa-libEGL
  - libglvnd-opengl

- Development Libraries:
  - json-c (JSON parsing)
  - libnsl (network services library)
  - libxcrypt-compat (encryption compatibility)

- X Window Libraries
  - libXmu
  - libXpm
  - libXinerama
  - libXcomposite
  - libXrender
  - libXrandr
  - libXcursor
  - libXi
  - libxdamage
  - libXtst
  - libxkbcommon
  - libSM

- Network and system utilities
  - tcsh

### GPU accelerated fleets

- Nvidia grid drivers

### Package managers

**Linux:**

- Conda/Mamba package manager (installed in `/opt/conda`)
- DNF package manager (system packages)
- pip (Python package installer)

**Windows:**

- Conda/Mamba package manager (installed in `C:\ProgramData\conda`)
- pip (Python package installer)

### Additional system software

All other software on the AMI can be updated, removed, or changed without notice. Do not take
dependencies on any software not explicitly listed in the _Supported Software Packages_
section above. This includes but is not limited to:

- Operating system packages and libraries
- Service management components
- Base AMI software and drivers
- Software dependencies and runtime libraries
- System configuration tools and utilities

#### Additional system software examples

**Linux:** System packages such as
systemd, kernel modules, hardware drivers, networking components, and
the supporting libraries installed as part of the base AL2023 distribution.

**Windows:** Windows system components,
Microsoft Edge, Amazon EC2 service software, hardware drivers, and Windows
runtime components.

### Best practices

**Dependency management**: Only take dependencies on software listed in the
_Supported software packages_ section.

**Package Versions**: For specific software versions, install specific packages
using package managers (such as pip, conda, and more.) rather than relying on AMI-provided versions.

**Environment Isolation**: Use virtual environments (such as Python venv, and
conda environments) to isolate your specific dependencies.

### AMI update model

Note the following information about how the worker AMI updates.

- Worker AMIs are continuously updated with no versioning system.
- Updates occur automatically as part of the service operation.
- No advance notification system is provided for AMI updates.
