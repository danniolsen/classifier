import sys
import os
import subprocess
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

lable = "python -m scripts.label_image "
graph = "--graph=tf_files/retrained_graph.pb "
image_tf = "--image=tf_files/test_images/"
image = sys.argv[1]

evaluate = lable + graph + image_tf + image

process = subprocess.Popen(evaluate.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
