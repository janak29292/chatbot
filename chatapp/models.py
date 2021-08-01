from django.db import models


# Create your models here.

class Intent(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=256)
    intents = models.ManyToManyField(Intent, related_name='states')

    def __str__(self):
        return self.name


class Option(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Response(models.Model):
    name = models.CharField(max_length=256)
    opions = models.ManyToManyField(Option)

    def __str__(self):
        return self.name


class Query(models.Model):
    query = models.ForeignKey(
        Response, null=True, blank=True,
        on_delete=models.CASCADE, related_name='responses'
    )
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='paths')
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='queries')

    def __str__(self):
        return f'{self.state.name}: {self.query.name} -> {self.option.name}'

    class Meta:
        unique_together = (
            ('query', 'state', 'option'),
        )
