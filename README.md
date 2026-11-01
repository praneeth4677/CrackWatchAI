CrackWatch AI
Railway Track Surface Defect Classification with MobileNetV2
CrackWatch AI is an academic computer vision project that classifies railway-track images as Defective or Non_Defective. It uses transfer learning with MobileNetV2, a Flask interface for image prediction, and an OpenCV workflow for classifying video frames.

The project explores how image-based inspection can support the identification of visible railway-track defects and reduce manual inspection effort.
Implementation scope: The supplied code performs whole-image and whole-frame classification. It does not locate cracks with bounding boxes or segmentation masks. The project report discusses broader real-time monitoring applications; GPS tracking, alerts, signaling integration, and YOLO-based detection are not implemented in these files.

Features
- Classifies railway-track images into two categories.
- Returns the predicted label and model confidence score.
- Provides Flask routes for an image upload page and prediction results.
- Processes video files frame by frame and overlays predictions.
- Saves annotated video output and supports pause/resume during playback.
- Includes a training notebook with augmentation and learning-curve plots.
- Includes a utility to create demonstration videos from images.
Technology Stack
Component	Technology
Programming language	Python
Deep learning	TensorFlow / Keras
Pretrained backbone	MobileNetV2 with ImageNet weights
Web application	Flask and HTML templates
Video processing	OpenCV
Data handling and visualization	NumPy, Pandas, Matplotlib
Image loading	Pillow
Notebook environment	Jupyter Notebook
Evaluation utilities	scikit-learn


Model Architecture
The training notebook uses the following configuration:
Setting	Value
Input	224 × 224 RGB image
Preprocessing	Pixel values divided by 255
Backbone	MobileNetV2, include_top=False
Backbone weights	ImageNet; layers frozen during training
Classification head	Dropout (0.5), global average pooling, Dense (256, ReLU), Dense (2, softmax)
Optimizer	Adam
Loss in supplied notebook	Binary cross-entropy
Training epochs	50
Training batch size	100
Training/validation split	70% / 30%
Saved model	MOBILENET.h5


Training augmentation includes rotation, horizontal and vertical flips, shear, and zoom. Inference currently uses the same /255.0 scaling as training; changing preprocessing requires consistent changes across training and prediction.
Project Files
Keep the scripts and notebooks in the project root so their relative paths work as written.
Path	Purpose
app.py	Flask application
predict.py	Image preprocessing, model loading, and prediction
Notebook_Final.ipynb	Model training and evaluation
test_video.ipynb	Video classification and annotated playback
savevideofromimages.py	Image-to-video utility
MOBILENET.h5	Trained model; required for inference
templates/index.html	Image upload page; required for the website
templates/pred.html	Prediction results page; required for the website
static/	Website assets and runtime image-upload folder
dataset/Defective/	Defective images used for training
dataset/Non_Defective/	Non-defective images used for training


Required assets: The supplied source files do not include MOBILENET.h5 or the HTML templates. Add these assets before running the website. If the trained model is distributed separately, download it and place it in the project root. No model download URL was provided with the source materials.
Setup
Download or clone this repository, then open a terminal in its root folder.
1. Create a virtual environment
python -m venv .venv
Activate it on Windows Command Prompt:
.venv\Scripts\activate
Or on macOS/Linux:
source .venv/bin/activate
2. Install dependencies
python -m pip install tensorflow flask werkzeug numpy pillow pandas matplotlib scikit-learn opencv-python notebook
These packages are derived from the source imports. Exact working package versions were not supplied. Use the original training environment where available, particularly when loading the saved HDF5 model or using the notebook's legacy Keras APIs. After verifying a working environment, record its versions in requirements.txt.
3. Prepare the upload folder
In app.py, replace the existing file_path assignment with the following code, immediately after basepath is defined:
upload_folder = os.path.join(basepath, "static", "images")
os.makedirs(upload_folder, exist_ok=True)
file_path = os.path.join(upload_folder, secure_filename(f.filename))
This creates the upload folder and replaces the Windows-specific path separator.
4. Start the website
After adding the trained model and templates:
python app.py
Open http://127.0.0.1:5000 in your browser. Upload a railway-track image to view its predicted class and confidence score. The upload form must send a multipart POST request to /predict/ with the file field named file.

The application starts in debug mode and is intended for local development.
Dataset and Training
The full image dataset is not required to run inference with an existing trained model. It is required to retrain the model.

Place training images under dataset/Defective/ and dataset/Non_Defective/. Verify that train_it.class_indices matches the label order in predict.py and test_video.ipynb:
["Defective", "Non_Defective"]
Start Jupyter from the project root:
jupyter notebook
Open Notebook_Final.ipynb and run the training cells in order. The notebook saves the trained model as MOBILENET.h5.

Dataset availability: The supplied materials do not identify a verified dataset download URL or redistribution license. Add the original dataset source and usage terms before publishing the dataset. A small set of permitted sample images can be included for demonstration; the full training dataset can remain outside the repository.
Video Demonstration
1. Open test_video.ipynb in a local Jupyter environment with desktop display support.
2. Place MOBILENET.h5 in the notebook's working directory.
3. Set video_input to your input video path; the default is v1.mp4.
4. Set video_output to your desired output path; the default is output_video.avi.
5. Run the notebook to view and save frame-level predictions.
Press Space to pause/resume. Press Q, then answer the confirmation prompt in the notebook, to exit.

Preprocessing correction: OpenCV reads frames in BGR order, while image training uses RGB. In the video predict(frame) function, convert the resized frame before passing it to img_to_array:
img = cv2.resize(frame, IMG_SIZE)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
To create a sample video from images, edit image_folder, output_video, frame_rate, and display_time in savevideofromimages.py, then run:
python savevideofromimages.py
Use input images with matching dimensions for this utility.
Evaluation and Limitations
The notebook records training and validation accuracy and loss. No independently verified held-out test accuracy or inference-speed benchmark is reported here.

Before reporting final performance:
- Use a separate test set that does not overlap with training or validation data. The notebook's additional test generator currently reuses the dataset directory and overlaps the training split.
- Disable test augmentation and use shuffle=False when comparing predictions with test_data.classes.
- Report a confusion matrix, precision, recall, and F1-score. The notebook's MSE, MAE, and R-squared calculations are not suitable headline metrics for this classification task.
- Measure video processing speed on the target hardware before claiming real-time performance.
The confidence value is the largest softmax output expressed as a percentage; it is not a guarantee that the prediction is correct. This academic prototype has not been validated for operational railway safety decisions.

The Flask application also needs stronger input validation and consistent error handling before deployment: predict_model() currently returns a string on failure, while the route expects a two-item result.
Future Improvements
- Independent test-set evaluation and reproducible dependency versions.
- Robust upload validation and error handling.
- Crack localization using object detection or segmentation.
- Live camera support and measured inference optimization.
- Location tagging and maintenance alerts.
Project Team
- A. Naga Praneeth
- CH. Sainadh
- B. Jaya Chandra
Guide: Mrs. A. Jyoshna, Assistant Professor
Department: Information Technology
Institution: Teegala Krishna Reddy Engineering College

Academic project title: CrackWatch AI: Real-Time Rail Surface Crack Detection Using Deep Convolutional Architectures.
License
No software license was supplied with the project materials. Add an appropriate LICENSE file after confirming the contributors' agreement. Dataset, model, and third-party asset usage remain subject to their respective terms.
