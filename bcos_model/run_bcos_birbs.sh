#!/bin/bash -l
#SBATCH --job-name=BCos_birds
#SBATCH --qos=normal
#SBATCH --gres=gpu:1
#SBATCH --mem=24G
#SBATCH --partition=rtx2080
#SBATCH --output="train_bcos_waterbirds.out"


cd $HOME/TML/bcos_model
mamba init
mamba activate TML


this_date=$(date +%d_%m_%g__%k_%M)

 python train.py \
 --dataset waterbirds \
 --base_network bcos_final \
 --experiment_name resnet_34 \
 --wandb_logger \
 --wandb_project TML_interpretable_bias_detection \
 --wandb_name wronkam \
 --wandb_id bcos_birds_$this_date \
 --explanation_logging \
 --explanation_logging_every_n_epochs 5
