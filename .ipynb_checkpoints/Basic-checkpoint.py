{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4bf7f3e8-c779-4316-aad2-d3be27444dfb",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'dlib'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn [1], line 3\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mcv2\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mcv\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[0;32m----> 3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mface_recognition\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mfr\u001b[39;00m\n\u001b[1;32m      5\u001b[0m img_Obama \u001b[38;5;241m=\u001b[39m fr\u001b[38;5;241m.\u001b[39mload_image_file(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mBasicImages/obama1.jpg\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m      6\u001b[0m img_Obama \u001b[38;5;241m=\u001b[39m cv\u001b[38;5;241m.\u001b[39mcvtColor(img_Obama,cv\u001b[38;5;241m.\u001b[39mCOLOR_BAYER_BG2BGR)\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/face_recognition/__init__.py:7\u001b[0m\n\u001b[1;32m      4\u001b[0m __email__ \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124mageitgey@gmail.com\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[1;32m      5\u001b[0m __version__ \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m0.1.0\u001b[39m\u001b[38;5;124m'\u001b[39m\n\u001b[0;32m----> 7\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mapi\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m load_image_file, face_locations, face_landmarks, face_encodings, compare_faces, face_distance\n",
      "File \u001b[0;32m~/.local/lib/python3.10/site-packages/face_recognition/api.py:4\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# -*- coding: utf-8 -*-\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mscipy\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mmisc\u001b[39;00m\n\u001b[0;32m----> 4\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mdlib\u001b[39;00m\n\u001b[1;32m      5\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mnumpy\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mnp\u001b[39;00m\n\u001b[1;32m      7\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'dlib'"
     ]
    }
   ],
   "source": [
    "import cv2 as cv\n",
    "import numpy as np\n",
    "import face_recognition as fr\n",
    "\n",
    "img_Obama = fr.load_image_file('BasicImages/obama1.jpg')\n",
    "img_Obama = cv.cvtColor(img_Obama,cv.COLOR_BAYER_BG2BGR)\n",
    "img_Test = fr.load_image_file('BasicImages/obama2.jpg')\n",
    "img_Test = cv.cvtColor(img_Test,cv.COLOR_BAYER_BG2BGR)\n",
    "\n",
    "faceLocator = fr.face_locations(img_Obama)[0]\n",
    "encodeObama = fr.face_encodings(img_Obama)[0]\n",
    "cv.rectangle(img_Obama,(faceLocator[3],faceLocator[0]),(faceLocator[1],faceLocator[2]),(255,0,255),2)\n",
    "\n",
    "faceLocator = fr.face_locations(img_Test)[0]\n",
    "encodeTest = fr.face_encodings(img_Test)[0]\n",
    "cv.rectangle(img_Test,(faceLocator[3],faceLocator[0]),(faceLocator[1],faceLocator[2]),(255,0,255),2)\n",
    "\n",
    "result = fr.compare_faces([encodeObama],encodeTest)\n",
    "print(result)\n",
    "\n",
    "cv.imshow('Obama',img_Obama)\n",
    "cv.imshow('Test',img_Test)\n",
    "cv.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c3f2ac5-a99f-44bf-bbdc-6398690dd471",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d544055c-367c-4158-9b36-c48fe6e7e48a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c22ffed3-6614-427f-992b-adbd111cf19c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
