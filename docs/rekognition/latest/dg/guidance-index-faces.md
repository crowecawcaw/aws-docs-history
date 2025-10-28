# Guidance for indexing faces in common scenarios

The following is guidance for using `IndexFaces` in common
scenarios.

## Critical or public safety

applications

- Call [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md") with images which contain only one face in each
  image and associate the returned Face ID with the identifier for the subject
  of the image.
- You can use [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md") ahead of indexing to verify there is only one face
  in the image. If more than one face is detected, re-submit the image after
  review and with only one face present. This prevents inadvertently indexing
  multiple faces and associating them with the same person.

## Photo sharing and social media

applications

- You should call `IndexFaces` without restrictions on images
  that contain multiple faces in use cases such as family albums. In such
  cases, you need to identify each person in every photo and use that
  information to group photos by the people present in them.

## General usage

- Index multiple different images of the same person, particularly with
  different face attributes (facial poses, facial hair, etc), create a user,
  and associate the different faces to that user to improve matching
  quality.
- Include a review process so that failed matches can be indexed with the
  correct face identifier to improve subsequent face matching ability.
- For information about image quality, see [Recommendations for facial
  comparison input images](recommendations-facial-input-images.md "recommendations-facial-input-images.md").
