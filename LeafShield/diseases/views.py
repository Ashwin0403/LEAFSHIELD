from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import tensorflow as tf
import numpy as np
import os

from .models import Predict  # Make sure to import the model


# Load the model
model_path = os.path.join(settings.BASE_DIR, 'diseases', 'trained_model.keras')
model = tf.keras.models.load_model(model_path)

def predict_disease(request):
    disease_name = None
    image_url = None
   
    description = None  # For storing description
    prevention = None  # For storing prevention
    treatment = None  # For storing treatment details
    
    
    if request.method == 'POST' and request.FILES.get('leaf-image'):
        leaf_image = request.FILES['leaf-image']
        fs = FileSystemStorage()

        filename = fs.save(leaf_image.name, leaf_image)
        file_url = fs.url(filename)
        file_path = fs.path(filename)

        try:
            # Preprocess the image
            image = tf.keras.preprocessing.image.load_img(file_path,target_size=(128,128))
            input_arr = tf.keras.preprocessing.image.img_to_array(image)

            # Debugging preprocessing
            input_arr = np.array([input_arr]) 
            prediction = model.predict(input_arr)
            print(prediction,prediction.shape)

            # Perform prediction
            
            max_probability = np.max(prediction)
            predicted_class_index = np.argmax(prediction) #Return index of max element

            print("Prediction probabilities:", prediction)
            print("Predicted class index:", predicted_class_index)
            print("Max probability:", max_probability)

            if max_probability >= 0.9:
                disease_name = get_disease_name_from_prediction(prediction)
                # Query the database for the treatment based on the disease name
                try:
                    # Query the table using the disease name
                    disease_data = Predict.objects.get(name=disease_name)
                    description = disease_data.description  # Get the description
                    prevention = disease_data.prevention  # Get the prevention methods

                    treatment = disease_data.treatment  # Get the treatment details
                except Predict.DoesNotExist:
                    treatment = ""
                
            else:
                disease_name = "Unable to find the disease."

            image_url = file_url

        except Exception as e:
            print("Error processing image:", e)
            disease_name = "Error in image processing or model prediction."

    return render(request, 'capture1.html', {'disease_name': disease_name, 'image_url': image_url,'description': description,
        'prevention': prevention,'treatment': treatment})


def get_disease_name_from_prediction(prediction):
    classes = [
        'Apple___Apple_scab', 'Cherry_(including_sour)___Powdery_mildew',
        'Corn_(maize)___Common_rust_', 'Grape___Black_rot',
        'Peach___Bacterial_spot', 'Potato___Early_blight',
        'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch',
        'Tomato___Bacterial_spot', 'Tomato___Leaf_Mold'
    ]
    predicted_class_index = np.argmax(prediction, axis=1)[0]
    return classes[predicted_class_index]




def capture(request):
    # Check if user is logged in using session data
    if request.session.get('is_logged_in', False):
        username = request.session.get('username')
        return render(request, 'capture1.html', {'username': username})
    else:
        # Redirect to login if not logged in
        return redirect('login:login')