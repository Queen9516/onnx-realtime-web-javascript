
from google.protobuf.json_format import MessageToDict
import onnx

model = onnx.load("./mnist.onnx")
for _input in model.graph.input:
    print(MessageToDict(_input))