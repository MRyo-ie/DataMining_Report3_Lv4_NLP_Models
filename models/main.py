# coding: utf-8

import argparse

from BoW import bag_of_words
import pre

parser = argparse.ArgumentParser()
# [モデル]
parser.add_argument('model', choices=['BoW', 'matrix', 'XLNet'], default='BoW',
                    help='Embedding モデル を選ぶ。')
parser.add_argument('--model_dir', type=str, default='./models/ckpts',
                    help='Base directory for the model.')
parser.add_argument('--pre_trained_model', type=str, default='./models/org_resnet/resnet_v2_50.ckpt',
                    help='Path to the pre-trained model checkpoint.')
parser.add_argument('--init_model_dir', action='store_true',
                    help='Whether to clean up the model directory if present.')
parser.add_argument('--base_architecture', type=str, default='resnet_v2_50',
                    choices=['resnet_v2_50', 'resnet_v2_101'],
                    help='The architecture of base Resnet building block.')


if __name__ == "__main__":
    args = parser.parse_args()

    if args.model == 'BoW'
