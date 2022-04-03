
from google.protobuf.json_format import MessageToDict
import onnx

model = onnx.load("./model.onnx")
for _input in model.graph.input:
    print(MessageToDict(_input))

for _output in model.graph.output:
    print(MessageToDict(_output))