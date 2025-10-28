# Choosing what AWS DataSync transfers

AWS DataSync lets you choose what to transfer and how you want your data handled. Some
options include:

- Transferring an exact list of files or object by using a manifest.
- Including or excluding certain types of data in your transfer by using a
  filter.
- For recurring transfers, moving only the data that's changed since the last
  transfer
- Overwriting data in the destination location to match what's in the source
  location.
- Choosing which file or object metadata to preserve between your storage
  locations.

###### Topics

- [Transferring specific files or objects by using
  a manifest](transferring-with-manifest.md "transferring-with-manifest.md")
- [Transferring specific files, objects, and folders by using
  filters](filtering.md "filtering.md")
- [Understanding how DataSync handles file and object
  metadata](metadata-copied.md "metadata-copied.md")
- [Links and directories copied by
  AWS DataSync](special-files-copied.md "special-files-copied.md")
- [Configuring how to handle files, objects, and
  metadata](configure-metadata.md "configure-metadata.md")
