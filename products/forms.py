# # from django import forms

# # class ProductForm(forms.Form):
# #     product_name = forms.CharField(label='Name', max_length=100)
# #     product_description = forms.CharField(label='Description', max_length=300)
# #     supplier_price = forms.FloatField(label='Supplier Price')
# #     selling_price = forms.FloatField(label='Selling Price')
# #     quantity = forms.FloatField(label='Quantity')

# from django import forms

# from .models import Product

# INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

# class NewItemForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'supplier_price', 'selling_price', 'quantity')
#         widgets = {
#                 'category': forms.Select(attrs={
#                     'class': INPUT_CLASSES
#                 }),
#                 'name': forms.TextInput(attrs={
#                     'class': INPUT_CLASSES
#                 }),
#                 'description': forms.Textarea(attrs={
#                     'class': INPUT_CLASSES
#                 }),
#                 'price': forms.TextInput(attrs={
#                     'class': INPUT_CLASSES
#                 }),
#                 'image': forms.FileInput(attrs={
#                     'class': INPUT_CLASSES
#                 })
#             }

# class EditItemForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'supplier_price', 'selling_price', 'quantity')
#         widgets = {
#             'name': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'description': forms.Textarea(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'price': forms.TextInput(attrs={
#                 'class': INPUT_CLASSES
#             }),
#             'image': forms.FileInput(attrs={
#                 'class': INPUT_CLASSES
#             })
#         }