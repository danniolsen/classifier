## classifier

all commands are executed from the computers root directory
# place images is tf_files

#run command 
`IMAGE_SIZE=224
ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"`

#run tensor board
`tensorboard --logdir tf_files/training_summaries &`

#check traning script
`python -m scripts.retrain -h`

#run traning
`python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=tf_files/training_data`

#--image_dir=tf_files/ this goes to the tf_files folder and trains image in folders under flower_photos

#run network on an image
`python -m scripts.label_image \
    --graph=tf_files/retrained_graph.pb  \
    --image=tf_files/<path to your .jpg file>`

