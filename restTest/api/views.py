from django.shortcuts import render
from django.http import HttpResponse
import numpy as np


def getInfo(request):
    a = np.arange(11) # creates a range from 0 to 10
    b = a.ndim
    c = a.dtype
    returnString = "The numpy array a is " + str(a) + "\nIt is " + str(b) + " dimensions\nEach entry is of type " + str(c)
    return HttpResponse(returnString)

# Create your views here.
