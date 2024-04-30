"""
General settings. Mainly paths to data.
"""
import os

# data root (mainly for CIFAR10)
DATA_ROOT = os.getenv("DATA_ROOT")

# ImageNet path
IMAGENET_PATH = os.getenv("IMAGENET_PATH") if os.getenv("IMAGENET_PATH") is not None else "../data/Imagenet"
CELEBA_PATH = os.getenv("CELEBA_PATH") if os.getenv("CELEBA_PATH") is not None else "../data/celebA"
WATERBIRDS_PATH = os.getenv("WATERBIRDS_PATH") if os.getenv("WATERBIRDS_PATH") else "../data/waterbirds"

# ---------------------------------------------
# Following are only needed for caching!!!
# ---------------------------------------------
SHMTMPDIR = "/dev/shm"

# ImageNet train data tar files
# Note this is not the same as the official ImageNet tar file
# this expects each class to inside its own tar file, which will then be extracted
# to SHMTMPDIR
IMAGENET_TRAIN_TAR_FILES_DIR = os.getenv("IMAGENET_TRAIN_TAR_FILES_DIR")

# Path to redis server
REDIS_SERVER = os.getenv("REDIS_SERVER_PATH")
