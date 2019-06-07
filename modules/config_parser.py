import argparse
import os

parser = argparse.ArgumentParser(description = 'Convert records/resources.')
parser.add_argument('-c', '--config', default=os.path.dirname(__file__) + "/../config.yaml", help='Configuration file path.')
# parser.add_argument('-d', '--data', default="", help='Source data')

args = parser.parse_args()
