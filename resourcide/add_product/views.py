from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect  # Import render and redirect.
from .forms import NameForm, DescriptionForm
from django.contrib import messages
from .models import Product

def first_step(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # Save the product name to the database.
            print('checked')
            try:
                product_name = form.cleaned_data.get("name")
                # print(product_name)
                product = Product(name=product_name)
                product.save()

                messages.success(request, 'Product name saved successfully.')
                # Redirect to the second page.
                return second_step()  # Change 'second_step' to your actual URL pattern name.
            except:
                print('fail')
    else:
        form = NameForm()

    return render(request, 'step1.html', {'form': form})
    # templates = loader.get_template('step1.html')
    # return HttpResponse(templates.render())

def second_step(request):
    try:
        # Retrieve the latest saved product from the database.
        latest_product = Product.objects.latest('id')  # Assuming 'id' is the primary key.
        for product in Product.objects.all():
            print(product.name, product.description)
    except Product.DoesNotExist:
        return redirect('first_step')  # Redirect if no product is found.

    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            # Save the product description to the database.
            product_description = form.cleaned_data['description']
            latest_product.description = product_description
            latest_product.save()

            # Redirect to the third step or any other page as needed.
            return redirect('third_step')  # Change 'third_step' to your actual URL pattern name.
    else:
        form = DescriptionForm()

    return render(request, 'step2.html', {'form': form, 'product_name': latest_product.name})

def third_step(request):
    templates = loader.get_template('step3.html')
    return HttpResponse(templates.render())

def fourth_step(request):
    templates = loader.get_template('step4.html')
    return HttpResponse(templates.render())

# def check_product(request):
#     # Retrieve the latest saved product from the database.
#     try:
#         latest_product = Product.objects.latest('id')  # Assuming 'id' is the primary key.
#         product_name = latest_product.name
#     except Product.DoesNotExist:
#         product_name = "No product found."

#     return render(request, 'check_product.html', {'product_name': product_name})
