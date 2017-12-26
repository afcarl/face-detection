from distutils.core import setup

setup(
	name="face-detection",
	version="1.0",
	description="dlib face detection wrapper",

	packages=["facedetection"],
	package_data={'facedetection': ['shape_predictor_68_face_landmarks.dat']},

	requires=["numpy", "dlib", "opencv-python"]
)
