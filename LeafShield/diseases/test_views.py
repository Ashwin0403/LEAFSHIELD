
import numpy as np
import tensorflow as tf
import os

image_path = 'D:\Django\LeafShield\media\l.JPG'

print(os.path.exists(image_path))  # Should return True if the file exists


def model_prediction(test_image):
    model =tf.keras.models.load_model('trained_model.keras')
    image = tf.keras.preprocessing.image.load_img(image_path,target_size=(128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr]) 
    prediction = model.predict(input_arr)
    print(prediction,prediction.shape)
    result_index = np.argmax(prediction) #Return index of max element
    print(result_index)
    class_name = ['Apple___Apple_scab',
    'Cherry_(including_sour)___Powdery_mildew',
    'Corn_(maize)___Common_rust_',
    'Grape___Black_rot',
    'Peach___Bacterial_spot',
    'Potato___Early_blight',
    'Squash___Powdery_mildew',
    'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot',
    'Tomato___Leaf_Mold']
    
    # Displaying the disease prediction
    model_prediction = class_name[result_index]
    print(model_prediction)
        
        
model_prediction('D:\Django\LeafShield\media\leaaf.JPG')    