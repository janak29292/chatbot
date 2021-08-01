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
    value = models.CharField(max_length=256)

    def __str__(self):
        return self.value


class Response(models.Model):
    description = models.CharField(max_length=256)
    options = models.ManyToManyField(Option, null=True, blank=True)

    def __str__(self):
        return self.description


class Query(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='paths')
    query = models.ForeignKey(
        Response, null=True, blank=True,
        on_delete=models.CASCADE, related_name='responses'
    )
    option = models.ForeignKey(Option, null=True, blank=True, on_delete=models.CASCADE)
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name='queries')

    def __str__(self):
        return self.response.description

    class Meta:
        unique_together = (
            ('intent', 'query', 'state', 'option'),
        )
