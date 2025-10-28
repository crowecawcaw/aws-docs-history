# Recomendations for

searching faces in a collection

- When searching for faces in a collection, ensure that recent face images
  are indexed.
- When creating a collection using `IndexFaces`, use multiple
  face images of an individual with different pitches and yaws (within the
  recommended range of angles). We recommend that at least five images of the
  person are indexed—straight on, face turned left with a yaw of 45
  degrees or less, face turned right with a yaw of 45 degrees or less, face
  tilted down with a pitch of 30 degrees or less, and face tilted up with a
  pitch of 45 degrees or less. If you want to track that these face instances
  belong to the same individual, consider using the external image ID
  attribute if there is only one face in the image being indexed. For example,
  five images of John Doe can be tracked in the collection with external image
  IDs as `John_Doe_1.jpg, … John_Doe_5.jpg`.
