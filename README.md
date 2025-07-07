frontend:
dahsboard and history record:
downlaod htmal files and css file but remember to create two folders name templates and script follow the structure:


![image](https://github.com/user-attachments/assets/be1fe256-74be-463f-a47c-42bb9b5f9f50)












or you can access the drive link and download the files 

output:
![image](https://github.com/user-attachments/assets/2a6af56b-5dde-447e-8135-0652ea6e48d3)
![image](https://github.com/user-attachments/assets/6ed60900-ad09-4eff-b2a6-cfc16a4e04ed)





Eye Gaze & Stress Detection Dashboard
Technologies Used

Backend:
- Python 3.x
- Flask (web framework)
- MediaPipe (face & eye detection)
- OpenCV (webcam handling)
- NumPy (math operations)

Frontend:
- HTML5, CSS3 (custom dashboard styling)
- JavaScript + Chart.js (line graphs)
- Chart.js Annotation Plugin (highlighting ranges and thresholds)

Project Structure

![image](https://github.com/user-attachments/assets/e6228ff4-ae81-474e-8db9-2b6fc3f8a306)








Setup Instructions
- Install VS code from the link 
https://code.visualstudio.com/download 
- Install pyhton from this link 
https://filehippo.com/download_python/3.10.0/ (remember to check box add path while installing)
- Open the folder in Vs code according to the structure
- Create a Virtual Environment:
   - python -m venv venv
   - source venv/bin/activate  (macOS/Linux)
   - venv\Scripts\activate   (Windows)

- Install Required Libraries:
   - pip install flask opencv-python mediapipe numpy
   - pip install mediapipe==0.10.9 if not worked (python -m pip install --upgrade pi)
   - pip install mediapipe
   - pip install cvzone
   - pip install flaskif error (python -m pip install flask,python -m pip install flask, py -3.10 -m pip install flask)
   - python -m pip install --upgrade pip
   - pip install opencv-python
   - source gaze_env/bin/activate  # For Windows: gaze_env\Scripts\activate
   - py -3.10 -m venv venv310
   - venv310\Scripts\activate
   - pip install flask opencv-python mediapipe

- Run the App:
   - source gaze_env/bin/activate  # For Windows:
   - venv310\Scripts\activate
   - python app.py

Visit: http://127.0.0.1:5000

Using on Another Desktop
If you copy the project to a new desktop/laptop:

- Make sure Python 3 is installed
- Open terminal inside the project folder
- Run:
   - all pip install
- Start the app:
   - source gaze_env/bin/activate  # For Windows:
   - venv310\Scripts\activate
   - python app.py

Visit: http://127.0.0.1:5000
 Features

- Real-time blink, gaze direction, and stress tracking
- Interactive line graphs with clear labels
- History view with merged metrics graph
- Stylish layout with clear UI sections
- Annotations for stress zones

Dependencies (pip freeze)

- flask==3.1.1
- mediapipe==0.10.9
- opencv-python==4.11.0.86
- numpy==1.26.4
- chartjs-plugin-annotation
