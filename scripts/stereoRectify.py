import numpy as np
import cv2 as cv

# Left camera
K1 = np.zeros((3, 3, 1), dtype = "float")
K1[0,0] = 0.0 # Fill with right values
K1[1,1] = 0.0 # Fill with right values
K1[0,2] = 0.0 # Fill with right values
K1[1,2] = 0.0 # Fill with right values
K1[2,2] = 1
d1 = np.array([0.0, 0.0, 0.0, 0.0], dtype = "float") # Fill with right values

# Right camera
K2 = np.zeros((3, 3, 1), dtype = "float")
K2[0,0] = 0.0 # Fill with right values
K2[1,1] = 0.0 # Fill with right values
K2[0,2] = 0.0 # Fill with right values
K2[1,2] = 0.0 # Fill with right values
K2[2,2] = 1
d2 = np.array([0.0, 0.0, 0.0, 0.0], dtype = "float") # Fill with right values

# Relative transformation
R = np.array([[1.0, 0.0, 0.0], \
[0.0, 1.0, 0.0], \
 [0.0, 0.0, 1.0]], dtype = "float") # Fill with right values

T = np.array([0.0, 0.0, 0.0], dtype = "float") # Fill with right values

# Computing stereo rectification
R1 = np.zeros((3,3), dtype = "float")
R2 = np.zeros((3,3), dtype = "float")
P1 = np.zeros((3,4), dtype = "float")
P2 = np.zeros((3,4), dtype = "float")
cv.stereoRectify(K1, d1, K2, d2, (0,0), R, T, R1, R2, P1, P2) # Fill with right values

# Printing results
np.set_printoptions(precision=9)
np.set_printoptions(suppress=True)

print('---\n---\nR1:')
print(R1)

print('\n---\nR2:')
print(R2)

print('\n---\nP1:')
print(P1)

print('\n---\nP2:')
print(P2)
