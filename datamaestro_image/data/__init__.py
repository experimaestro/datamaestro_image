from datamaestro.data import Generic
from datamaestro.definitions import Data, Argument, Type, DataTasks, DataTags, Dataset

@Argument("images", Generic)
@Argument("labels", Generic)
@DataTasks("image classification")
@DataTags("images")
@Data()
class ImageClassification:
  """Image classification dataset"""
  pass

