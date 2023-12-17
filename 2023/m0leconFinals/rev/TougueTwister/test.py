import numpy as np

from PIL import Image
import csv
from sklearn.preprocessing import MinMaxScaler

def end(m):
    processed_matrix = m.astype(np.uint8)
    image = Image.fromarray(processed_matrix, mode='L')  
    image.save("output_image.png")


def simple_manipolation(m):
    m1 = m / 3
    m2 = m1 - 69
    m3 = m2 * 5
    m4 = m3 + 42
    return m4



def convert_to_float(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = float(matrix[i][j])
    return matrix

def read_csv_to_matrix(file_path):
    matrix = []
    
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Skip the first row
        next(csv_reader, None)
        
        # Read the remaining rows and build the matrix
        for row in csv_reader:
            matrix.append(row)

    convert_to_float(matrix)
    
    return np.matrix(matrix)


def divide_matrix_in_2_part(m):
    R = m[:,0:50]
    X = m[:,50:100]
    return R.transpose(), X.transpose()


mat = read_csv_to_matrix("ziopera.csv")

end(mat)

