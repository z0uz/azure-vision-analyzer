# Azure Vision Analyzer

This is a web application that uses Azure's Computer Vision API to analyze images. Users can upload images and get AI-powered descriptions, detect objects, identify tags, and count faces in the images.

## Features

- Image upload and preview
- AI-powered image description
- Object detection
- Tag identification
- Face detection
- Modern, responsive UI

## Setup Instructions

1. Create an Azure account and set up a Computer Vision resource
2. Clone this repository
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and fill in your Azure credentials:
   ```bash
   cp .env.example .env
   ```
6. Run the application:
   ```bash
   python app.py
   ```

## Azure Deployment

To deploy to Azure App Service:

1. Install Azure CLI
2. Login to Azure:
   ```bash
   az login
   ```
3. Create an App Service plan:
   ```bash
   az appservice plan create --name myAppServicePlan --resource-group myResourceGroup --sku B1
   ```
4. Create a web app:
   ```bash
   az webapp create --name your-app-name --resource-group myResourceGroup --plan myAppServicePlan --runtime "PYTHON:3.9"
   ```
5. Configure the app settings:
   ```bash
   az webapp config appsettings set --name your-app-name --resource-group myResourceGroup --settings AZURE_VISION_ENDPOINT=your_endpoint AZURE_VISION_KEY=your_key
   ```
6. Deploy your code:
   ```bash
   az webapp up --name your-app-name --resource-group myResourceGroup
   ```

## Technologies Used

- Python Flask
- Azure Computer Vision API
- Bootstrap 5
- HTML5/CSS3
- JavaScript
