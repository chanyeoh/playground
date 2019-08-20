# Data Transformation
The following code contains a demo of the following:
1. The algorithm would first generate two data sets, one of the datasets are within a circle, the other dataset is on the border of the circle, which is in 2D.
2. It would then transform the data into a 3D model using the cylinder formula for Z.
3. It would then use the transformed Z position and X to project it in a 2D plane
4. Finally, it would compress the Z data and form everything into a line

The purpose of this is to show that instead of trying to figure out a way to draw a circle around the datasets, one could re-transform it into another projection plane to segregate the data.

# Build & Run
To build and run the code:
```
pipenv install
pipenv run python data_transformation.py
```
