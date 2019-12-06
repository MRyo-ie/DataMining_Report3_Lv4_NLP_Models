import argparse

parser = argparse.ArgumentParser()
# [データ] TFRecode の場所
parser.add_argument('data_txt_path', type=str, default='./data_in/datas_test/',
                    help='Path to the directory containing the PASCAL VOC data tf record.')
# [モデル]
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
    pass
