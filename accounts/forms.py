from django import forms

class RegistrationForm(forms.Form):
	first_name = forms.CharField(
		max_length=30, 
		label_suffix='',
		widget=forms.TextInput(
			attrs={'placeholder':'First name'}
			)
		)
	second_name = forms.CharField(max_length=30, label_suffix='')
	user_name = forms.CharField(max_length=30, label_suffix='')
	email = forms.EmailField(max_length=255, label_suffix='')
	phone = forms.CharField(max_length=12, label_suffix='')
	address = forms.CharField(max_length=30, label_suffix='')
	password = forms.CharField(
		min_length=8,
		max_length=20,
		widget=forms.PasswordInput(), 
		help_text='Your password must be 8-20 characters long, contain letters and numbers.',
		label_suffix='')
	confirm_password = forms.CharField(
		min_length=8,
		max_length=20,
		widget=forms.PasswordInput(), 
		help_text='This must be similar to the password given previously.',
		label_suffix='')

	def clean(self):
		cleaned_data = super(RegistrationForm, self).clean()
		first_name = cleaned_data.get('first_name')
		second_name = cleaned_data.get('second_name')
		user_name = cleaned_data.get('user_name')
		email = cleaned_data.get('email')
		phone = cleaned_data.get('phone')
		address = cleaned_data.get('address')
		password = cleaned_data.get('password')
		confirm_password = cleaned_data.get('confirm_password')

		if password != confirm_password:
			raise forms.ValidationError(
				"The Passwords do not Match!"
				)