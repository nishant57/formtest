# Create your views here.
from django.shortcuts import render
from addnum.models import NumbersForm

def addnum(request):
	if request.method == 'POST':
		form = NumbersForm(request.POST) 
		a = form['num1'] 

# a.value is an instance method which can't be used for calculation.
# form.num1 doesn't work. Why(?)
# form['num1'] is a bound object. Comes with a form block and all.
# a.value() finally is a string.

		b = form['num2']
		sum = int(a.value()) + int(b.value()) #form.num1
	else:
		form = NumbersForm()
		sum = ''
	
	return render(request, 'addnum/addnum.html', {'form':form,'sum':sum})	
