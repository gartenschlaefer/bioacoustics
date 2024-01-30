# --
# birdnet demo

import numpy as np
import yaml

from birdnetlib import Recording
from birdnetlib.analyzer import Analyzer
from datetime import datetime
from pathlib import Path


if __name__ == '__main__':

  # yaml config file
  cfg = yaml.safe_load(open("./config.yaml"))['birdnet']
  print(cfg)

  # path
  test_file = Path(cfg['test_file'])
  print(str(test_file))

  # Load and initialize the BirdNET-Analyzer models.
  analyzer = Analyzer()

  # use date or week_48 min_conf=0.25,
  recording = Recording(analyzer, test_file, min_conf=0.08,)

  # analyze
  recording.analyze()

  # print
  print(recording.detections)