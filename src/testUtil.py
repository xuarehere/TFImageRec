import tensorflow as tf
import data_process as dp
import numpy as np
import fine_tuning

OUTPUT_FILE = '../datasets/flower_processed_data.npy'
VALIDATION_PERCENTAGE = 10
TEST_PERCENTAGE = 10

with tf.Session() as sess:
    processed_data = dp.create_image_list(sess,TEST_PERCENTAGE,VALIDATION_PERCENTAGE)
    np.save(OUTPUT_FILE,processed_data)

# if __name__ == '__main__':
#     main()