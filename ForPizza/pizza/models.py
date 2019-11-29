from django.db import models

class PizzaName(models.Model):
	name = models.CharField('Pizza', max_length=30)
	price = models.DecimalField('Price', max_digits=5, decimal_places=2, default=0)
	weight = models.IntegerField('Weight, grams', default=50)

	def __str__ (self):
		return 'Pizza: {}'.format(self.name)

class Ingredient(models.Model):
	name = models.CharField('Ingredient', max_length=30)
	price = models.DecimalField('Price', max_digits=5, decimal_places=2, default=0)
	weight = models.IntegerField('Weight, grams', default=50)
	is_vegan = models.BooleanField('Vegan')

	def __str__ (self):
		return 'Ingredient: {}'.format(self.name)

class Pizza(models.Model):
	pizza_name = models.ForeignKey(PizzaName, on_delete=models.CASCADE)
	ingredients = models.ManyToManyField(Ingredient)

	def __str__(self):
		return str(self.pizza_name)

class PizzaOrdered(models.Model):
	THIN = 'S'
	MEDIUM = 'M'
	THICK = 'L'
	GARLICKSAAUCE = 'GA'
	TOMATOSAUCE = 'TO'
	NOSAUCE = 'NO'
	ADDITION_SAUCE = [
	(GARLICKSAAUCE, 'Garlick sauce'),
	(TOMATOSAUCE, 'Tomato sauce'),
	(NOSAUCE, 'No sauce needed')
	]
	SIDE = [
	(THIN, 'Thin'),
	(MEDIUM, 'Medium'),
	(THICK, 'Thick')
	]
	pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
	side_name = models.CharField('Base thickness', max_length=50, choices=SIDE, default=THIN)
	additional_sauce = models.CharField('Additional sauce', max_length=50, choices=ADDITION_SAUCE, default=TOMATOSAUCE)
	number = models.IntegerField('Pizza number', default=1)

	def get_absolute_url(self):
		return reverse('order-detail', kwargs={'pk': self.pk})

class Every(models.Model):
	text = models.TextField(default='0')
	foreign = models.ForeignKey(Ingredient, on_delete=models.CASCADE, null=True)
	integer_field = models.IntegerField(null=True)
	charfield = models.CharField(max_length=256)
	positive_integer = models.PositiveIntegerField()
	binary = models.BinaryField(max_length=10, null=True)
	boolean = models.BooleanField(default=True)
	date = models.DateField(auto_now=True, auto_now_add=False, null=True)
	date_time = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
	float_f = models.FloatField(default=0)
	decimal = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	duration = models.DurationField(null=True)
	email = models.EmailField(max_length=50, null=True)
	generic_IP_adress = models.GenericIPAddressField(protocol='both', unpack_ipv4=False, null=True)
	file = models.FileField(upload_to=None, max_length=100, null=True)
	file_Path = models.FilePathField(path=None, match=None, recursive=False, max_length=100, null=True)
	image = models.ImageField(upload_to=None, height_field=100, width_field=None, max_length=100, null=True)
	slug = models.SlugField(max_length=20, null=True)
	url = models.URLField(max_length=100, null=True)

