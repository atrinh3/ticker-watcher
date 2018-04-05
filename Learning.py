import tempfile as tf
import csv


# If there are 5 features in the log regression model, the algorithm
# should have 6 coefficients since the first (b0) coefficient only 
# represents the bias. b1 - bN will represent the coefficients for 
# each of the extracted data features.
def initialize_parameters(name):
    parameters = [1]
    for i in range(0, features + 1):
        parameters.append(0.5)
    return parameters
    
    
# This function returns the trained parameters of the log regression model.
def get_parameters(p_filename):
    try:
        p_file = open(p_filename, 'r')
    except OSError:
        print("No parameters file exists, initializing parameters")
        return initialize_parameters()
    parameters = []
    with open(p_filename) as p_file:
        reader = csv.reader(p_file, newline='', quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            parameters.append(row)
    return parameters
    
    
# Chunk serial streamed data



# main
training_step = 0.3
parameters = get_parameters("parameters.csv")


current_data = tf.TemporaryFile()


current_data.close()

