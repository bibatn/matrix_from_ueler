from math import acos, asin, atan2, cos, pi, radians, sin, sqrt
def from_euler(roll, pitch, yaw):
    
    cp = cos(pitch)
    sp = sin(pitch)
    sr = sin(roll)
    cr = cos(roll)
    sy = sin(yaw)
    cy = cos(yaw)
    
    HMatrix = np.zeros((3,3), np.float32)
    HMatrix[0][0] = cp * cy
    HMatrix[0][1] = (sr * sp * cy) - (cr * sy)
    HMatrix[0][2] = (cr * sp * cy) + (sr * sy)
    HMatrix[1][0] = cp * sy
    HMatrix[1][1] = (sr * sp * sy) + (cr * cy)
    HMatrix[1][2] = (cr * sp * sy) - (sr * cy)
    HMatrix[2][0] = -sp
    HMatrix[2][1] = sr * cp
    HMatrix[2][2] = cr * cp
    return HMatrix
