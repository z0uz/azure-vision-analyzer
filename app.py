import os
from flask import Flask, request, render_template, jsonify
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from dotenv import load_dotenv
import uuid

load_dotenv()

app = Flask(__name__)

# Initialize the Computer Vision client
vision_client = ComputerVisionClient(
    endpoint=os.getenv('AZURE_VISION_ENDPOINT'),
    credentials=CognitiveServicesCredentials(os.getenv('AZURE_VISION_KEY'))
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_image():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image uploaded'}), 400

        image = request.files['image']
        
        # Analyze the image
        features = [
            VisualFeatureTypes.description,
            VisualFeatureTypes.tags,
            VisualFeatureTypes.objects,
            VisualFeatureTypes.faces
        ]
        
        results = vision_client.analyze_image_in_stream(image, features)
        
        # Process and return results
        response = {
            'description': results.description.captions[0].text if results.description.captions else '',
            'tags': [tag.name for tag in results.tags],
            'objects': [obj.object_property for obj in results.objects],
            'faces': len(results.faces)
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
