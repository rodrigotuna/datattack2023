import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.metrics import mean_squared_error
from sktime.performance_metrics.forecasting import mean_absolute_scaled_error
import argparse


def predictor():
    #load model
    model = torch.load('model.pth')
    model.eval()

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--date', type=str, required=True)
    parser.add_argument('--latitudes', type=str, required=True)
    parser.add_argument('--longitudes', type=str, required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    {''}
    pred