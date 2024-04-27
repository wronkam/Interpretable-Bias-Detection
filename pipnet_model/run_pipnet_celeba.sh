#!/bin/bash -l
#SBATCH --job-name=PiPnet_celeb
#SBATCH --qos=quick
#SBATCH --gres=gpu:1
#SBATCH --mem=24G
#SBATCH --partition=student
#SBATCH --output="train_pipnet_celeba.out"



cd $HOME/TML
mamba init
mamba activate TML

this_date=$(date +%d_%m_%g__%k_%M)

python3 ./pipnet_model/main.py --dataset celeba \
--validation_size 0.0 \
--net resnet34 \
--batch_size 8 \
--batch_size_pretrain 16 \
--epochs 60 \
--optimizer Adam \
--lr 0.05 \
--lr_block 0.0005 \
--lr_net 0.0005 \
--weight_decay 0.0 \
--log_dir ./pipnet_logs/pipnet_celeba_$this_date \
--num_features 0 \
--image_size 224 \
--freeze_epochs 10 \
--dir_for_saving_images visualization_celeba_$this_date \
--epochs_pretrain 10 \
--seed 42 \
--num_workers 8 \
--num_features 764 \
--skip-ood-eval \
--dataset-root /home/z1162449/TML/data

