#!/bin/bash -l
#SBATCH --job-name=BCos_CelebA
#SBATCH --qos=normal
#SBATCH --gres=gpu:1
#SBATCH --mem=24G
#SBATCH --partition=rtx2080
#SBATCH --output="train_bcos_celeba.out"


cd $HOME/TML/bcos_model
mamba init
mamba activate TML


python train.py  \
 --dataset celebA \
--base_network bcos_final  \
--experiment_name resnet_34  \
--wandb_logger  \
--wandb_project TML_interpretable_bias_detection  \
--wandb_entity wronkam  \
--wandb_name bcos_celebA_$(date +%d_%m_%g__%k_%M)  \
--explanation_logging  \
--explanation_logging_every_n_epochs 5
