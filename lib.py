# --
# library for bioacoustics
#
# references:
# [1]: Schlüter, J. (2018). Bird Identification from Timestamped, Geotagged Audio Recordings. Conference and Labs of the Evaluation Forum.
#

import numpy as np


def per_channel_energy_normalization(x):
  """
  Per-Channel Energy Normalization (PCEN)
  """
  pass


def nonlinear_magnitude_transformation_js(x, a=0.0):
  """
  a nonlinear scaling from [1]
  """
  return (x ** (1 / (1 + np.exp(-a))))


