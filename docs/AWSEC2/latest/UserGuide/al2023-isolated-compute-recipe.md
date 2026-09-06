

# Sample Amazon Linux 2023 image description
<a name="al2023-isolated-compute-recipe"></a>

The sample Amazon Linux 2023 image description has the following characteristics: 

1. **Unified Kernel Image (UKI) boot** — Boot using a single, signed binary that combines the kernel, `initrd`, and boot parameters into one immutable image.

1. **Read-only root filesystem** — Use Enhanced Read-Only File System (`erofs`) with dm-verity protection to ensure that the root filesystem cannot be modified and maintains cryptographic integrity verification.

1. **Ephemeral overlay filesystem** — Create a temporary overlay filesystem that allows temporary writes to directories like `/etc`, `/run`, and `/var`. Since this overlay filesystem exists only in memory, all changes are automatically lost when the instance reboots, ensuring the system returns to its original trusted state.

1. **Disabled remote access methods** — Remove the following remote access mechanisms to prevent remote access:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/al2023-isolated-compute-recipe.html)

   \* For more information, see [ Image Description Elements](https://osinside.github.io/kiwi/image_description/elements.html#packages-ignore).