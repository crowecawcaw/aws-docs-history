**Help improve this page**

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# Build a custom Bottlerocket AMI variant for Amazon EKS

When you run GPU workloads on Amazon Elastic Kubernetes Service (Amazon EKS), you choose a Bottlerocket variant. The variant must match your Kubernetes version and accelerator type. Bottlerocket ships validated variants for common configurations. However, your organization might need a different variant for any of the following reasons:

- A newer NVIDIA driver branch
- A pinned driver version for regulatory compliance
- Additional packages for monitoring
- A hardened baseline required by your security team
  Because [Bottlerocket](https://github.com/bottlerocket-os/bottlerocket "https://github.com/bottlerocket-os/bottlerocket") on the GitHub website is fully open-source, you can create a custom variant that meets these needs. This topic shows how to clone an existing variant and swap the NVIDIA driver from the R580 branch to R595 (version 595.71.05). You then build the image and register it as a private AMI.

###### Important

The G7 EC2 instance type requires NVIDIA driver version 595 or later. The EKS Bottlerocket NVIDIA AMIs currently include NVIDIA driver version 580, which does not support G7 instances.

See the [Bottlerocket repository](https://github.com/bottlerocket-os/bottlerocket "https://github.com/bottlerocket-os/bottlerocket") on the GitHub website for instructions on building a variant with NVIDIA driver version 595. This topic walks through the complete process starting at [Step 1](#bottlerocket-custom-variant-step1 "#bottlerocket-custom-variant-step1").

## How the build system works

When you run `cargo make -e BUILDSYS_VARIANT=aws-k8s-1.36-nvidia`, three things happen:

- **Fetch dependencies.** Twoliter (the Bottlerocket build orchestrator) reads `Twoliter.toml` and pulls three Open Container Initiative (OCI) artifacts from `public.ecr.aws/bottlerocket`:

  - **bottlerocket-sdk** — a container image with the full cross-compilation toolchain (GCC, Rust, Go, RPM macros).
  - **bottlerocket-kernel-kit** — pre-built RPMs for kernels, kernel modules (including NVIDIA kmod packages), and firmware.
  - **bottlerocket-core-kit** — pre-built RPMs for userspace: kubelet, containerd, the NVIDIA device plugin and container toolkit, settings plugins, and system services.

  `Twoliter.toml` pins the versions and `Twoliter.lock` locks their digests. To change either, run `./tools/twoliter/twoliter update` to re-resolve.

- **Build the variant.** Twoliter launches a Docker build inside the SDK container. It compiles your variant’s settings-defaults crate, resolves the RPM dependency tree from the kits, and assembles everything into a disk image.
- **Output.** Twoliter writes the final `.img.lz4` file to `build/images/`. The build produces deterministic output: the same `Twoliter.toml` pins and variant `Cargo.toml` always generate the same image, regardless of host.

## Repository layout

The following directories are relevant to variant work:

```
bottlerocket/
├── Cargo.toml                       # workspace: lists every variant
├── Twoliter.toml                    # pins SDK + kit versions
├── Twoliter.lock                    # locked digests for the above
├── Licenses.toml                    # you create this (NVIDIA license acknowledgement)
├── Infra.toml                       # you create this (AMI publish regions)
│
├── variants/
│   ├── aws-k8s-1.36-nvidia/         # example variant you'll copy
│   │   ├── Cargo.toml               #   package list + kernel params
│   │   └── amispec.toml             #   symlink → ../shared/amispec-split.toml
│   └── shared/                      # shared AMI spec templates
│
├── sources/
│   ├── Cargo.toml                   # workspace: lists every settings-defaults crate
│   ├── shared-defaults/             # the actual defaults (symlink targets)
│   └── settings-defaults/
│       └── aws-k8s-1.36-nvidia/
│           ├── Cargo.toml
│           └── defaults.d/          # 30+ symlinks into shared-defaults/
│
└── packages/
    ├── settings-defaults/
    │   └── settings-defaults.spec   # RPM: declares which variants exist
    └── settings-plugins/
        └── settings-plugins.spec    # RPM: maps variants to settings plugins
```

Review the following notes about the repository structure:

- A variant is mostly metadata. The external kits supply the kernel, drivers, and userspace.
- Settings-defaults files are symlinks, not copies. Use `cp -R` (not `cp -r` on macOS) to preserve them.
- Adding a variant requires edits in five places: two workspace `Cargo.toml` files, two `.spec` files, and `README.md`.

## Prerequisites

To complete the walkthrough, you need:

- An AWS account with permissions to launch EC2 instances and register AMIs
- An EC2 instance (or equivalent Linux x86\_64 host) with at least 8 cores, 16 GiB memory, and 150 GB disk
- Ubuntu 24.04 LTS (or Fedora; macOS isn’t supported as a build host)
- Docker 20.10 or later
- Rust (stable toolchain, installed via rustup)
- cargo-make (latest version)
- Familiarity with Git, Rust’s Cargo, and RPM packaging concepts

###### Note

When you complete this walkthrough, terminate the EC2 instance and deregister any AMIs you no longer need to avoid ongoing charges. For instructions on cleaning up, see [Cleaning up](#bottlerocket-custom-variant-cleanup "#bottlerocket-custom-variant-cleanup").

## Step 1: Prepare the build host

Launch an EC2 instance — for example, a `c7i.8xlarge` (32 vCPU, 64 GiB memory). Use a 150 GB gp3 root volume and attach the `AmazonSSMManagedInstanceCore` managed policy for SSM access.

Connect to the instance using AWS Systems Manager (SSM) Session Manager:

```
aws ssm start-session --target <instance-id>
cd ~
```

Install the required operating system packages:

```
apt-get update
apt-get install -y build-essential openssl libssl-dev pkg-config lz4 \
                   git ca-certificates curl gnupg
```

###### Note

The official `BUILDING.md` references `liblz4-tool`. On recent Ubuntu versions, the package is named `lz4`.

Install Docker using the following commands:

```
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
  -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu noble stable" \
  > /etc/apt/sources.list.d/docker.list
apt-get update
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin
systemctl enable --now docker
```

Install Rust and cargo-make using the following commands:

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
. "$HOME/.cargo/env"
cargo install cargo-make
```

## Step 2: Clone the repository

Clone the [Bottlerocket repository](https://github.com/bottlerocket-os/bottlerocket "https://github.com/bottlerocket-os/bottlerocket") on the GitHub website and navigate into the directory:

```
cd ~/bottlerocket
```

To create a reproducible build, check out a tagged release (for example, `git checkout v1.62.1`). To use the latest packages, stay on the `develop` branch.

## Step 3: Verify the kit versions

Open `Twoliter.toml` and confirm the kit versions. For R595 support, you need `bottlerocket-kernel-kit` version 6.2.2 or later:

```
[[kit]]
name = "bottlerocket-kernel-kit"
version = "6.2.2"
vendor = "bottlerocket"
```

If the version is older, update it and regenerate the lock:

```
./tools/twoliter/twoliter update
```

## Step 4: Work around the cargo-make path issue

Twoliter sets `CARGO_HOME` to `~/bottlerocket/.cargo`, which prevents the inner Cargo process from finding your globally installed cargo-make. Create a symlink:

```
mkdir -p ~/bottlerocket/.cargo/bin
ln -sf /root/.cargo/bin/cargo-make ~/bottlerocket/.cargo/bin/cargo-make
```

Without this step, the build fails with `error: no such command: make`.

## Step 5: Find available driver branches

The NVIDIA kmod packages are shipped inside `bottlerocket-kernel-kit`. For information about available driver packages, see the [kernel-kit packages directory](https://github.com/bottlerocket-os/bottlerocket-kernel-kit "https://github.com/bottlerocket-os/bottlerocket-kernel-kit") on the GitHub website, or the [release notes](https://github.com/bottlerocket-os/bottlerocket-kernel-kit/releases "https://github.com/bottlerocket-os/bottlerocket-kernel-kit/releases") on the GitHub website.

For kernel 6.18 (used by `aws-k8s-1.36` variants):

```
kmod-6.18-nvidia-r580   ← driver 580.159.03 (current default)
kmod-6.18-nvidia-r595   ← driver 595.71.05
```

For kernel 6.12 (used by `aws-k8s-1.33`, `1.34`, `1.35`):

```
kmod-6.12-nvidia-r580
kmod-6.12-nvidia-r595
```

###### Note

Each kmod package ships subpackages (`-tesla`, `-open-gpu`, `-grid`, `-fabricmanager`, `-imex`). The official Bottlerocket NVIDIA variants reference `-tesla`, which pulls in all required subpackages via RPM dependencies. At boot, Bottlerocket automatically selects the appropriate driver flavor based on the instance type.

## Step 6: Create the new variant

Copy the existing variant. Use `cp -R` to preserve symlinks:

```
cp -R variants/aws-k8s-1.36-nvidia variants/aws-k8s-1.36-nvidia-595
cp -R sources/settings-defaults/aws-k8s-1.36-nvidia \
      sources/settings-defaults/aws-k8s-1.36-nvidia-595
```

Edit `variants/aws-k8s-1.36-nvidia-595/Cargo.toml`:

```
- name = "aws-k8s-1_36-nvidia"
+ name = "aws-k8s-1_36-nvidia-595"

- "kmod-6.18-nvidia-r580-tesla",
+ "kmod-6.18-nvidia-r595-tesla",
```

Edit `sources/settings-defaults/aws-k8s-1.36-nvidia-595/Cargo.toml`:

```
- name = "settings-defaults-aws-k8s-1_36-nvidia"
+ name = "settings-defaults-aws-k8s-1_36-nvidia-595"
```

## Step 7: Register the variant

Register the new variant in five files:

**1. `Cargo.toml`** — add the workspace member:

```
 "variants/aws-k8s-1.36-nvidia",
+    "variants/aws-k8s-1.36-nvidia-595",
 "variants/aws-k8s-1.36-nvidia-fips",
```

**2. `sources/Cargo.toml`** — add the settings-defaults member:

```
 "settings-defaults/aws-k8s-1.36-nvidia",
+    "settings-defaults/aws-k8s-1.36-nvidia-595",
```

**3. `packages/settings-defaults/settings-defaults.spec`** — add a `%package` block, entries in both build loops, and a `%files` section:

```
%package aws-k8s-1.36-nvidia-595
Summary: Settings defaults for the aws-k8s 1.36 nvidia-595 variant
Requires: %{_cross_os}variant(aws-k8s-1.36-nvidia-595)
Provides: %{_cross_os}settings-defaults(any)
Provides: %{_cross_os}settings-defaults(aws-k8s-1.36-nvidia-595)
Conflicts: %{_cross_os}settings-defaults(any)

%description aws-k8s-1.36-nvidia-595
%{summary}.
```

Add to both `for defaults in` loops:

```
    aws-k8s-1.36-nvidia \
+   aws-k8s-1.36-nvidia-595 \
    metal-dev \
```

Add the `%files` section:

```
%files aws-k8s-1.36-nvidia-595
%{_cross_defaultsdir}/aws-k8s-1.36-nvidia-595.toml
%{_cross_tmpfilesdir}/storewolf-defaults-aws-k8s-1.36-nvidia-595.conf
```

**4. `packages/settings-plugins/settings-plugins.spec`** — add a `Provides:` line under `%package aws-k8s-nvidia`:

```
 Provides: %{_cross_os}settings-plugin(aws-k8s-1.36-nvidia)
+Provides: %{_cross_os}settings-plugin(aws-k8s-1.36-nvidia-595)
 Conflicts: %{_cross_os}settings-plugin(any)
```

## Step 8: Refresh the lockfile

Adding a workspace member invalidates `sources/Cargo.lock`. Refresh it:

```
cd ~/bottlerocket/sources
cargo update --workspace
```

###### Important

Don’t use `cargo generate-lockfile`. It rewrites the entire lockfile and bumps transitive dependencies, which causes `cargo-deny` duplicate-version errors.

## Step 9: Create the NVIDIA license file

NVIDIA restricts redistribution of driver sources. You must add an explicit license acknowledgement before building:

```
cat > ~/bottlerocket/Licenses.toml <<'EOF'
[nvidia]
spdx-id = "LicensesRef-NVIDIA-Customer-Use"
licenses = [
  { path = "LICENSE", license-url = "https://www.nvidia.com/en-us/drivers/nvidia-license/" }
]
EOF
```

## Step 10: Build and publish the AMI

Create an `Infra.toml` with your target regions:

```
cat > ~/bottlerocket/Infra.toml <<'EOF'
[aws]
regions = ["us-west-2", "us-east-1", "us-east-2"]
EOF
```

Build the image:

```
cd ~/bottlerocket
cargo make \
  -e BUILDSYS_VARIANT=aws-k8s-1.36-nvidia-595 \
  -e BUILDSYS_UPSTREAM_SOURCE_FALLBACK=true \
  -e BUILDSYS_UPSTREAM_LICENSE_FETCH=true \
  -e BUILDSYS_JOBS=32
```

The first build pulls the SDK and kit images (~2 GB total). Subsequent builds take 3–5 minutes on a 32-core host.

Publish the AMI:

```
cargo make \
  -e BUILDSYS_VARIANT=aws-k8s-1.36-nvidia-595 \
  -e PUBLISH_REGIONS=us-west-2,us-east-1,us-east-2 \
  ami
```

The build writes AMI IDs to `build/images/x86_64-aws-k8s-1.36-nvidia-595/latest/*-amis.json`. Use these in your EKS managed node groups, Karpenter `EC2NodeClass`, or launch templates.

## Other combinations you can build

This walkthrough swaps the NVIDIA driver branch, but you can use the same approach for any package available in the upstream kits. The following examples show what you can assemble without forking a kit:

| What you want                    | What to change in the variant `Cargo.toml`                    |
| -------------------------------- | ------------------------------------------------------------- |
| Different NVIDIA driver branch   | `kmod-6.18-nvidia-r580-tesla` → `kmod-6.18-nvidia-r595-tesla` |
| Different kernel version         | `kernel-6.18` → `kernel-6.12` (adjust kmod accordingly)       |
| Remove NVIDIA entirely           | Delete the three `nvidia-*` lines from `included-packages`    |
| Add EFA support                  | Add `kmod-6.18-efa` to `included-packages`                    |
| Switch container runtime version | `containerd-2.2` → `containerd-2.1`                           |

For information about available packages, see the [kernel-kit](https://github.com/bottlerocket-os/bottlerocket-kernel-kit "https://github.com/bottlerocket-os/bottlerocket-kernel-kit") on the GitHub website and the [core-kit](https://github.com/bottlerocket-os/bottlerocket-core-kit "https://github.com/bottlerocket-os/bottlerocket-core-kit") on the GitHub website.

###### Important

The Bottlerocket root filesystem is immutable. You can’t install packages at runtime. Every package in the kits is cross-compiled specifically for Bottlerocket — standard upstream RPMs don’t work. If you need software that isn’t already in a kit, consider [bootstrap containers](https://github.com/bottlerocket-os/bottlerocket#bootstrap-containers-settings "https://github.com/bottlerocket-os/bottlerocket#bootstrap-containers-settings") on the GitHub website or [host containers](https://github.com/bottlerocket-os/bottlerocket#host-containers "https://github.com/bottlerocket-os/bottlerocket#host-containers") on the GitHub website as a runtime alternative.

## Cleaning up

If you no longer need the build host, terminate the EC2 instance to avoid ongoing charges. The AMIs persist independently in your account; deregister them with the EC2 console or CLI if you no longer need them.

## Summary

This topic showed how to create a custom Bottlerocket variant with a different NVIDIA driver branch. The process involves copying an existing variant, changing one package reference, registering the new variant in the workspace and RPM specs, and running the build. The same approach applies to any customization: swapping kernel versions, adding packages, or creating variants for new Kubernetes releases.
