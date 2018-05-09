from __future__ import print_function
import os
import random
import argparse


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


class ModelOptions:
    def __init__(self):
        parser = argparse.ArgumentParser(description='Colorization with GANs')
        parser.add_argument('--seed', type=int, default=0, metavar='S', help='random seed (default: 0)')
        parser.add_argument('--train', type=str2bool, default=True, help='True for training, False for testing (default: True)')
        parser.add_argument('--dataset', type=str, default='places365', help='the name of dataset [places365, cifar10] (default: places365)')
        parser.add_argument('--dataset-path', type=str, default='./dataset', help='dataset path (default: ./dataset)')
        parser.add_argument('--checkpoints-path', type=str, default='./checkpoints', help='models are saved here (default: ./checkpoints)')
        parser.add_argument('--samples-path', type=str, default='./samples', help='samples are saved here (default: ./samples)')
        parser.add_argument('--samples-size', type=int, default=8, help='number of images to sample (default: 8)')
        parser.add_argument('--batch-size', type=int, default=32, metavar='N', help='input batch size for training (default: 32)')
        parser.add_argument('--color-space', type=str, default='lab', help='model color space [lab, yuv, rgb] (default: lab)')
        parser.add_argument('--epochs', type=int, default=30, metavar='N', help='number of epochs to train (default: 30)')
        parser.add_argument('--lr', type=float, default=2e-4, metavar='LR', help='learning rate (default: 2e-4)')
        parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam optimizer (default: 0.5)')
        parser.add_argument("--l1-weight", type=float, default=100.0, help="weight on L1 term for generator gradient (default: 100.0)")
        parser.add_argument('--augment', type=str2bool, default=True, help='True for augmentation (default: True)')
        parser.add_argument('--acc-thresh', type=float, default=2.0, help="accuracy threshold (default: 2.0)")
        parser.add_argument('--save-interval', type=int, default=1000, help='how many batches to wait before saving model (default: 1000)')
        parser.add_argument('--log-interval', type=int, default=1000, help='how many batches to wait before logging training status (default: 1000)')
        parser.add_argument('--gpu-ids', type=str, default='0', help='gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU')

        self._parser = parser

    def parse(self):
        opt = self._parser.parse_args()
        os.environ['CUDA_VISIBLE_DEVICES'] = opt.gpu_ids

        if opt.seed == 0:
            opt.seed = random.randint(0, 2**31 - 1)

        if opt.dataset_path == './dataset':
            opt.dataset_path += ('/' + opt.dataset)

        args = vars(opt)
        print('\n------------ Options -------------')
        for k, v in sorted(args.items()):
            print('%s: %s' % (str(k), str(v)))
        print('-------------- End ----------------\n')

        return opt
