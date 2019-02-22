from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120)
    budget = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    budget_left = models.IntegerField(blank=True, null=True, help_text="This field will be assigned automatically")

    def save(self, **kwargs):
        self.slug = slugify(self.name)

        # If there is no budget left assign budget to budget left.
        if not self.budget_left:
            self.budget_left = self.budget

        # Calculate the current budget left.
        self.budget_left = self.calculate_budget_left()

        super(Project, self).save()

    def calculate_budget_left(self):
        project_expenses = Expense.objects.filter(project=self)

        # if there are no expenses, then just return the current budget.
        if not project_expenses:
            return self.budget

        total_expenses = 0
        for expense in project_expenses:
            total_expenses += expense.amount

        budget_left = self.budget - total_expenses

        return budget_left

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Expense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET(value=None))
    title = models.CharField(max_length=120)
    amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return self.title

